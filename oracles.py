"""
Quantitative & Real-Time Data Oracles for Polymarket Probability Estimation:
1. CryptoOracle: Live Binance spot + klines (exact Polymarket resolution source) with
   Geometric Brownian Motion First-Passage Barrier & Log-Normal Terminal probabilities.
2. WeatherOracle: Live Open-Meteo / Airport Station (NOAA KORD, KAUS, KLGA, EGLC, EDDM, VHHH, ZSPD...)
   temperature max forecast & hourly observation probability distributions.
3. NewsSentimentOracle: Live Google News RSS + CLOB Orderbook Microstructure Imbalance analyzer.
"""

import math
import re
import urllib.parse
import xml.etree.ElementTree as ET
from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any, Dict, List, Optional, Tuple

from http_tls import fetch_standard_url
from polymarket_api import MarketInfo


def norm_cdf(x: float) -> float:
    """Standard normal cumulative distribution function."""
    return 0.5 * (1.0 + math.erf(x / math.sqrt(2.0)))


def calibrate_probability(p_raw: float, p_market: float, oracle_weight: float = 0.65) -> float:
    """
    Applies Bayesian shrinkage toward the market prior to prevent model overconfidence,
    while preserving genuine quantitative edge without over-dampening signals.
    P_cal = w * P_raw + (1 - w) * P_market, clamped to [0.02, 0.98].
    """
    p_market_clamped = min(max(p_market, 0.02), 0.98)
    blended = oracle_weight * p_raw + (1.0 - oracle_weight) * p_market_clamped
    return min(max(blended, 0.02), 0.98)


@dataclass
class EvaluationResult:
    market_id: str
    question: str
    category: str
    oracle_used: str
    official_source: str
    p_yes: float
    p_no: float
    confidence: float  # 0.0 to 1.0
    rationale: str
    supporting_data: Dict[str, Any] = field(default_factory=dict)


class CryptoOracle:
    """
    Quantitative Crypto Oracle using official Binance USDT spot klines.
    Calculates exact barrier-touching ("dip to" / "reach") and terminal ("above") probabilities
    using a multi-timeframe Parkinson + Close-to-Close volatility estimator with realistic asset floors.
    """

    SYMBOLS = {
        "bitcoin": "BTCUSDT",
        "btc": "BTCUSDT",
        "ethereum": "ETHUSDT",
        "eth": "ETHUSDT",
        "solana": "SOLUSDT",
        "sol": "SOLUSDT",
        "xrp": "XRPUSDT",
        "dogecoin": "DOGEUSDT",
        "doge": "DOGEUSDT",
        "bnb": "BNBUSDT",
    }

    # Realistic implied volatility floors (annualized -> hourly equivalent)
    # Prevents false "barrier impossible" outputs during 24-48h consolidation periods
    VOLATILITY_FLOORS = {
        "BTCUSDT": 0.0050,  # ~47% annualized floor
        "ETHUSDT": 0.0060,  # ~56% annualized floor
        "SOLUSDT": 0.0075,  # ~70% annualized floor
        "XRPUSDT": 0.0070,  # ~65% annualized floor
        "DOGEUSDT": 0.0085, # ~80% annualized floor
        "BNBUSDT": 0.0055,  # ~51% annualized floor
    }

    def __init__(self) -> None:
        self._cache: Dict[str, Dict[str, Any]] = {}

    def _fetch_klines_multisource(self, symbol: str) -> Tuple[Optional[str], Optional[List[List[Any]]]]:
        """
        Fetches hourly candles across 3 redundant sources:
        1. Binance API (preferred if available)
        2. Kraken Public API (global, fully accessible in US & GitHub Actions)
        3. Coinbase Public API (native US institutional exchange)
        """
        # 1. Binance
        try:
            url = f"https://api.binance.com/api/v3/klines?symbol={symbol}&interval=1h&limit=168"
            kl = fetch_standard_url(url, timeout=5.0)
            if kl and len(kl) >= 10:
                return "Binance", [[int(k[0]), float(k[1]), float(k[2]), float(k[3]), float(k[4])] for k in kl]
        except Exception:
            pass

        # 2. Kraken (failsafe for US cloud environments)
        try:
            km = {"BTCUSDT": "XBTUSD", "ETHUSDT": "ETHUSD", "SOLUSDT": "SOLUSD", "XRPUSDT": "XRPUSD", "DOGEUSDT": "XDGUSD"}
            pair = km.get(symbol)
            if pair:
                url = f"https://api.kraken.com/0/public/OHLC?pair={pair}&interval=60"
                d = fetch_standard_url(url, timeout=5.0)
                if d and isinstance(d, dict) and "result" in d:
                    pk = [k for k in d["result"].keys() if k != "last"][0]
                    candles = d["result"][pk]
                    if candles and len(candles) >= 10:
                        return "Kraken", [[int(c[0]) * 1000, float(c[1]), float(c[2]), float(c[3]), float(c[4])] for c in candles[-168:]]
        except Exception:
            pass

        # 3. Coinbase
        try:
            cm = {"BTCUSDT": "BTC", "ETHUSDT": "ETH", "SOLUSDT": "SOL", "XRPUSDT": "XRP", "DOGEUSDT": "DOGE"}
            coin = cm.get(symbol)
            if coin:
                url = f"https://api.exchange.coinbase.com/products/{coin}-USD/candles?granularity=3600"
                raw = fetch_standard_url(url, timeout=5.0)
                if raw and isinstance(raw, list) and len(raw) >= 10:
                    return "Coinbase", [[int(c[0]) * 1000, float(c[3]), float(c[2]), float(c[1]), float(c[4])] for c in reversed(raw[:168])]
        except Exception:
            pass

        return None, None

    def _get_symbol_stats(self, symbol: str) -> Optional[Dict[str, Any]]:
        if symbol in self._cache:
            return self._cache[symbol]
        try:
            source, klines = self._fetch_klines_multisource(symbol)
            if not klines or len(klines) < 10:
                return None

            closes = [float(k[4]) for k in klines]
            highs = [float(k[2]) for k in klines]
            lows = [float(k[3]) for k in klines]
            current_price = closes[-1]

            # 1. Close-to-close log returns variance
            log_returns = [
                math.log(closes[i] / closes[i - 1])
                for i in range(1, len(closes))
                if closes[i - 1] > 0
            ]
            mean_ret = sum(log_returns) / len(log_returns)
            var_close = sum((r - mean_ret) ** 2 for r in log_returns) / max(1, len(log_returns) - 1)

            # 2. Parkinson range-based variance: (ln(H/L))^2 / (4 * ln(2))
            park_terms = [
                (math.log(max(h, l * 1.0001) / max(l, 1e-6)) ** 2) / (4.0 * math.log(2.0))
                for h, l in zip(highs, lows)
                if h > 0 and l > 0
            ]
            var_park = sum(park_terms) / max(1, len(park_terms))

            # 3. Blended realized variance + asset-class floor
            blended_var = 0.40 * var_close + 0.60 * var_park
            floor_vol = self.VOLATILITY_FLOORS.get(symbol, 0.0055)
            hourly_vol = max(math.sqrt(max(blended_var, 1e-6)), floor_vol)

            # Also get today's high/low since 04:00 UTC (00:00 ET)
            now_utc = datetime.now(timezone.utc)
            et_midnight_utc = now_utc.replace(hour=4, minute=0, second=0, microsecond=0)
            if now_utc.hour < 4:
                et_midnight_ms = int((et_midnight_utc.timestamp() - 86400) * 1000)
            else:
                et_midnight_ms = int(et_midnight_utc.timestamp() * 1000)

            today_highs = [float(k[2]) for k in klines if int(k[0]) >= et_midnight_ms]
            today_lows = [float(k[3]) for k in klines if int(k[0]) >= et_midnight_ms]

            stats = {
                "symbol": symbol,
                "source": source,
                "current_price": current_price,
                "hourly_vol": hourly_vol,
                "annual_vol": hourly_vol * math.sqrt(24 * 365),
                "today_high": max(today_highs) if today_highs else highs[-1],
                "today_low": min(today_lows) if today_lows else lows[-1],
                "high_24h": max(highs[-24:]),
                "low_24h": min(lows[-24:]),
            }
            self._cache[symbol] = stats
            return stats
        except Exception:
            return None

    def evaluate(self, market: MarketInfo) -> Optional[EvaluationResult]:
        q_lower = market.question.lower()

        # Detect crypto symbol
        symbol = None
        for kw, sym in self.SYMBOLS.items():
            if re.search(rf"\b{kw}\b", q_lower):
                symbol = sym
                break
        if not symbol:
            return None

        # Parse dollar target(s) like $82,000 or $2,600 or $180
        price_matches = re.findall(r"\$([0-9,]+(?:\.[0-9]+)?)", market.question)
        if not price_matches:
            return None

        targets = [float(p.replace(",", "")) for p in price_matches]
        stats = self._get_symbol_stats(symbol)
        if not stats:
            return None

        s0 = stats["current_price"]
        sigma_h = stats["hourly_vol"]
        tau = max(market.hours_to_close, 0.25)
        # Apply a 1.12x fat-tail jump multiplier standard for crypto intraday distributions
        sigma_total = sigma_h * math.sqrt(tau) * 1.12

        target = targets[0]
        # Avoid non-price dollar mentions (e.g., "$1B market cap")
        if target < 0.01 * s0 or target > 10.0 * s0:
            return None

        p_yes: Optional[float] = None
        mode_desc = ""

        # Case 1: "dip to $X"
        if "dip to" in q_lower or "fall to" in q_lower or "drop to" in q_lower:
            if s0 <= target or (tau <= 24 and stats["today_low"] <= target):
                p_yes = 0.985
                mode_desc = f"{symbol} already touched/below ${target:,.0f} (Current=${s0:,.2f}, TodayLow=${stats['today_low']:,.2f})"
            else:
                # Reflection principle for first-passage time of GBM (zero-drift intraday)
                dist = abs(math.log(s0 / target))
                p_touch = math.erfc(dist / (sigma_total * math.sqrt(2.0)))
                p_yes = min(max(p_touch, 0.005), 0.99)
                mode_desc = (
                    f"First-passage dip model: {symbol}=${s0:,.2f} -> barrier=${target:,.0f} "
                    f"({(target - s0)/s0*100:+.2f}%), vol_h={sigma_h*100:.2f}%, tau={tau:.1f}h => P(touch)={p_yes*100:.1f}%"
                )

        # Case 2: "reach $X" or "hit $X"
        elif "reach" in q_lower or "hit" in q_lower or "touch" in q_lower:
            if (target >= s0 and tau <= 24 and stats["today_high"] >= target) or (target <= s0 and tau <= 24 and stats["today_low"] <= target):
                p_yes = 0.985
                mode_desc = f"{symbol} already reached ${target:,.0f} today"
            else:
                dist = abs(math.log(s0 / target))
                p_touch = math.erfc(dist / (sigma_total * math.sqrt(2.0)))
                p_yes = min(max(p_touch, 0.005), 0.99)
                mode_desc = (
                    f"First-passage reach model: {symbol}=${s0:,.2f} -> barrier=${target:,.0f} "
                    f"({(target - s0)/s0*100:+.2f}%), vol_h={sigma_h*100:.2f}%, tau={tau:.1f}h => P(touch)={p_yes*100:.1f}%"
                )

        # Case 3: "above $X" or "over $X"
        elif "above" in q_lower or "over" in q_lower or "higher than" in q_lower:
            d2 = (math.log(s0 / target) - 0.5 * (sigma_total ** 2)) / sigma_total
            p_yes = min(max(norm_cdf(d2), 0.005), 0.995)
            mode_desc = (
                f"Terminal GBM model: {symbol}=${s0:,.2f} vs strike=${target:,.0f} "
                f"({(s0 - target)/target*100:+.2f}%), vol_h={sigma_h*100:.2f}%, tau={tau:.1f}h => P(S_T > K)={p_yes*100:.1f}%"
            )

        # Case 4: "between $X and $Y"
        elif "between" in q_lower and len(targets) >= 2:
            low_k, high_k = min(targets[0], targets[1]), max(targets[0], targets[1])
            d2_low = (math.log(s0 / low_k) - 0.5 * (sigma_total ** 2)) / sigma_total
            d2_high = (math.log(s0 / high_k) - 0.5 * (sigma_total ** 2)) / sigma_total
            p_yes = min(max(norm_cdf(d2_low) - norm_cdf(d2_high), 0.005), 0.99)
            mode_desc = (
                f"Terminal range model: {symbol}=${s0:,.2f} in [${low_k:,.0f}, ${high_k:,.0f}], "
                f"vol_h={sigma_h*100:.2f}%, tau={tau:.1f}h => P={p_yes*100:.1f}%"
            )

        if p_yes is None:
            return None

        # Apply Bayesian shrinkage toward market prior unless barrier already touched today
        mkt_prior = market.gamma_prices[0] if market.gamma_prices else 0.5
        if p_yes < 0.98:
            p_raw = p_yes
            p_yes = calibrate_probability(p_raw, mkt_prior, oracle_weight=0.70)
            mode_desc += f" -> Calibrated(0.70x)={p_yes*100:.1f}%"

        src_label = stats.get("source", "Binance")
        return EvaluationResult(
            market_id=market.id,
            question=market.question,
            category="Crypto",
            oracle_used=f"CryptoQuantitativeGBM_{src_label}",
            official_source=f"{src_label} {symbol} 1m/1h Spot Klines",
            p_yes=round(p_yes, 4),
            p_no=round(1.0 - p_yes, 4),
            confidence=0.82,
            rationale=mode_desc,
            supporting_data=stats,
        )


class WeatherOracle:
    """
    Official Airport Weather Station Oracle using Open-Meteo high-resolution models
    mapped to exact NOAA / METAR airport coordinates used by Polymarket rules.
    """

    STATIONS: Dict[str, Tuple[float, float, str, str, str]] = {
        "chicago": (41.9742, -87.9073, "America/Chicago", "fahrenheit", "NOAA KORD (Chicago O'Hare)"),
        "new york": (40.7769, -73.8740, "America/New_York", "fahrenheit", "NOAA KLGA (NYC LaGuardia)"),
        "nyc": (40.7769, -73.8740, "America/New_York", "fahrenheit", "NOAA KLGA (NYC LaGuardia)"),
        "austin": (30.1975, -97.6664, "America/Chicago", "fahrenheit", "NOAA KAUS (Austin-Bergstrom)"),
        "miami": (25.7959, -80.2870, "America/New_York", "fahrenheit", "NOAA KMIA (Miami Intl)"),
        "los angeles": (33.9416, -118.4085, "America/Los_Angeles", "fahrenheit", "NOAA KLAX (Los Angeles)"),
        "dallas": (32.8998, -97.0403, "America/Chicago", "fahrenheit", "NOAA KDFW (Dallas/Fort Worth)"),
        "atlanta": (33.6407, -84.4277, "America/New_York", "fahrenheit", "NOAA KATL (Atlanta)"),
        "seattle": (47.4502, -122.3088, "America/Los_Angeles", "fahrenheit", "NOAA KSEA (Seattle-Tacoma)"),
        "london": (51.5048, 0.0495, "Europe/London", "celsius", "METAR EGLC (London City Airport)"),
        "munich": (48.3537, 11.7750, "Europe/Berlin", "celsius", "METAR EDDM (Munich Airport)"),
        "paris": (49.0097, 2.5479, "Europe/Paris", "celsius", "METAR LFPG (Paris CDG)"),
        "hong kong": (22.3080, 113.9185, "Asia/Hong_Kong", "celsius", "HKO / VHHH (Hong Kong Intl)"),
        "shanghai": (31.1443, 121.8083, "Asia/Shanghai", "celsius", "METAR ZSPD (Shanghai Pudong)"),
        "seoul": (37.4602, 126.4407, "Asia/Seoul", "celsius", "METAR RKSI (Seoul Incheon)"),
        "tokyo": (35.5494, 139.7798, "Asia/Tokyo", "celsius", "METAR RJTT (Tokyo Haneda)"),
        "toronto": (43.6777, -79.6248, "America/Toronto", "celsius", "METAR CYYZ (Toronto Pearson)"),
        "buenos aires": (-34.5592, -58.4156, "America/Argentina/Buenos_Aires", "celsius", "METAR SABE (Buenos Aires)"),
        "ankara": (40.1281, 32.9951, "Europe/Istanbul", "celsius", "METAR LTAC (Ankara Esenboga)"),
        "sao paulo": (-23.4356, -46.4731, "America/Sao_Paulo", "celsius", "METAR SBGR (Sao Paulo Guarulhos)"),
        "mexico city": (19.4361, -99.0719, "America/Mexico_City", "celsius", "METAR MMMX (Mexico City Intl)"),
        "wellington": (-41.3272, 174.8053, "Pacific/Auckland", "celsius", "METAR NZWN (Wellington Intl)"),
        "shenzhen": (22.6393, 113.8107, "Asia/Shanghai", "celsius", "METAR ZGSZ (Shenzhen Bao'an)"),
        "lucknow": (26.7606, 80.8893, "Asia/Kolkata", "celsius", "METAR VILK (Lucknow Airport)"),
    }

    MONTHS = {
        "january": 1, "february": 2, "march": 3, "april": 4, "may": 5, "june": 6,
        "july": 7, "august": 8, "september": 9, "october": 10, "november": 11, "december": 12,
    }

    def __init__(self) -> None:
        self._cache: Dict[str, Dict[str, float]] = {}
        self._load_custom_stations()

    def _load_custom_stations(self) -> None:
        import json
        from pathlib import Path
        custom_path = Path(__file__).resolve().parent / "data" / "custom_stations.json"
        if custom_path.exists():
            try:
                raw = json.loads(custom_path.read_text(encoding="utf-8"))
                for city_k, val in raw.items():
                    if isinstance(val, list) and len(val) == 5:
                        self.STATIONS[city_k.lower().strip()] = (
                            float(val[0]), float(val[1]), str(val[2]), str(val[3]), str(val[4])
                        )
            except Exception:
                pass

    def _get_daily_max_forecasts(self, city_key: str) -> Optional[Dict[str, float]]:
        if city_key in self._cache:
            return self._cache[city_key]
        lat, lon, tz, unit, _ = self.STATIONS[city_key]
        url = (
            f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}"
            f"&daily=temperature_2m_max&temperature_unit={unit}"
            f"&timezone={urllib.parse.quote(tz)}&forecast_days=7&past_days=1"
        )
        try:
            data = fetch_standard_url(url, timeout=8.0)
            times = data.get("daily", {}).get("time", [])
            temps = data.get("daily", {}).get("temperature_2m_max", [])
            mapping = {str(t): float(v) for t, v in zip(times, temps) if v is not None}
            self._cache[city_key] = mapping
            return mapping
        except Exception:
            return None

    def evaluate(self, market: MarketInfo) -> Optional[EvaluationResult]:
        q_lower = market.question.lower()
        if "highest temperature" not in q_lower:
            return None

        matched_city = None
        for city in self.STATIONS:
            if city in q_lower:
                matched_city = city
                break
        if not matched_city:
            return None

        # Extract date (e.g., "on October 13")
        date_match = re.search(
            r"on\s+(january|february|march|april|may|june|july|august|september|october|november|december)\s+(\d{1,2})",
            q_lower,
        )
        if not date_match:
            return None

        month_num = self.MONTHS[date_match.group(1)]
        day_num = int(date_match.group(2))
        year_num = datetime.now(timezone.utc).year
        target_date_str = f"{year_num:04d}-{month_num:02d}-{day_num:02d}"

        forecasts = self._get_daily_max_forecasts(matched_city)
        if not forecasts or target_date_str not in forecasts:
            return None

        forecast_max = forecasts[target_date_str]
        _, _, _, unit, station_name = self.STATIONS[matched_city]
        unit_sym = "°F" if unit == "fahrenheit" else "°C"

        # Realistic meteorological uncertainty between gridded NWP model and airport METAR thermometer:
        # Minimum ~1.5°C (2.7°F) for same-day, scaling up for longer lead times and complex terrain
        base_sd = 3.1 if unit == "fahrenheit" else 1.75
        if matched_city in ("mexico city", "ankara", "sao paulo"):
            base_sd *= 1.15
        lead_factor = min(max(market.hours_to_close / 24.0, 0.85), 1.8)
        sd = base_sd * lead_factor

        # Parse temperature bracket from question
        # Pattern 1: "between 84-85°F" or "between 84 and 85°F"
        range_m = re.search(r"between\s+(-?\d+)\s*(?:-|and|to)\s*(-?\d+)\s*°?[fc]", q_lower)
        # Pattern 2: "be 26°C or below" / "be 80°F or lower"
        below_m = re.search(r"(-?\d+)\s*°?[fc]\s+or\s+(?:below|lower|less)", q_lower)
        # Pattern 3: "be 30°C or higher" / "be 90°F or above"
        above_m = re.search(r"(-?\d+)\s*°?[fc]\s+or\s+(?:higher|above|more)", q_lower)
        # Pattern 4: single degree "be 26°C on"
        exact_m = re.search(r"be\s+(-?\d+)\s*°?[fc]\s+on", q_lower)

        if range_m:
            low_b = float(range_m.group(1)) - 0.5
            high_b = float(range_m.group(2)) + 0.5
            p_raw = norm_cdf((high_b - forecast_max) / sd) - norm_cdf((low_b - forecast_max) / sd)
            bracket_str = f"[{range_m.group(1)}, {range_m.group(2)}]{unit_sym}"
        elif below_m:
            high_b = float(below_m.group(1)) + 0.5
            p_raw = norm_cdf((high_b - forecast_max) / sd)
            bracket_str = f"<={below_m.group(1)}{unit_sym}"
        elif above_m:
            low_b = float(above_m.group(1)) - 0.5
            p_raw = 1.0 - norm_cdf((low_b - forecast_max) / sd)
            bracket_str = f">={above_m.group(1)}{unit_sym}"
        elif exact_m:
            val = float(exact_m.group(1))
            low_b, high_b = val - 0.5, val + 0.5
            p_raw = norm_cdf((high_b - forecast_max) / sd) - norm_cdf((low_b - forecast_max) / sd)
            bracket_str = f"{val:.0f}{unit_sym} (±0.5)"
        else:
            return None

        p_raw = min(max(p_raw, 0.01), 0.99)
        mkt_prior = market.gamma_prices[0] if market.gamma_prices else 0.5
        p_yes = calibrate_probability(p_raw, mkt_prior, oracle_weight=0.80)
        rationale = (
            f"Station {station_name} ({target_date_str}): Model Max={forecast_max:.1f}{unit_sym} "
            f"(±{sd:.1f}{unit_sym}), Target={bracket_str} => RawP={p_raw*100:.1f}%, Calibrated(0.80x)={p_yes*100:.1f}%"
        )

        return EvaluationResult(
            market_id=market.id,
            question=market.question,
            category="Weather",
            oracle_used="AirportMeteorologicalModel",
            official_source=station_name,
            p_yes=round(p_yes, 4),
            p_no=round(1.0 - p_yes, 4),
            confidence=0.85,
            rationale=rationale,
            supporting_data={
                "station": station_name,
                "target_date": target_date_str,
                "forecast_max": forecast_max,
                "std_dev": round(sd, 2),
                "raw_p_yes": round(p_raw, 4),
                "bracket": bracket_str,
            },
        )


class NewsAndOrderbookOracle:
    """
    Combines live News/Search headlines (freshness & authority weighted) with
    CLOB Order Book depth imbalance and Gamma-vs-CLOB divergence for general events.
    """

    AUTHORITY_SOURCES = {
        "reuters", "associated press", "ap news", "bloomberg", "bbc", "financial times",
        "wall street journal", "cnbc", "espn", "the athletic", "sky sports", "coindesk",
        "politico", "axios", "nytimes", "the guardian", "al jazeera", "forbes",
    }

    POSITIVE_WORDS = {
        "win", "wins", "won", "victory", "confirmed", "approved", "passes", "passed",
        "surge", "surges", "rally", "agreemement", "reached", "signed", "extends",
        "continues", "leads", "leading", "dominant", "clear", "official", "announces",
    }

    NEGATIVE_WORDS = {
        "lose", "loses", "lost", "defeat", "rejected", "fails", "failed", "collapsed",
        "denied", "denies", "postponed", "canceled", "injured", "out", "unlikely",
        "doubt", "violation", "broken", "ends", "halted", "crash", "drops",
    }

    def _extract_search_query(self, question: str) -> str:
        cleaned = re.sub(r"^(Will|Does|Is|Can|Who will win)\s+", "", question, flags=re.IGNORECASE)
        cleaned = re.sub(r"\?$", "", cleaned)
        cleaned = re.sub(r"\bon\s+202\d-\d{2}-\d{2}\b", "", cleaned)
        words = cleaned.split()
        return " ".join(words[:7])

    def fetch_news_sentiment(self, query: str) -> Tuple[float, int, List[str]]:
        """
        Fetches fresh Google News RSS items (last 24h) for `query`.
        Returns (sentiment_score [-1..+1], article_count, top_headlines).
        """
        url = (
            f"https://news.google.com/rss/search?q={urllib.parse.quote(query + ' when:2d')}"
            f"&hl=en-US&gl=US&ceid=US:en"
        )
        try:
            xml_text = fetch_standard_url(url, timeout=7.0, as_json=False)
            root = ET.fromstring(xml_text)
            items = root.findall(".//item")[:12]
            if not items:
                return 0.0, 0, []

            total_weight = 0.0
            weighted_score = 0.0
            headlines: List[str] = []

            for item in items:
                title = (item.findtext("title") or "").strip()
                source = (item.findtext("source") or "").strip().lower()
                if not title:
                    continue
                if len(headlines) < 3:
                    headlines.append(title[:110])

                # Authority weight
                weight = 1.6 if any(auth in source for auth in self.AUTHORITY_SOURCES) else 1.0
                words = set(re.findall(r"[a-z]+", title.lower()))
                pos = len(words & self.POSITIVE_WORDS)
                neg = len(words & self.NEGATIVE_WORDS)
                if pos > 0 or neg > 0:
                    item_score = (pos - neg) / (pos + neg)
                    weighted_score += item_score * weight
                    total_weight += weight

            net_sentiment = (weighted_score / total_weight) if total_weight > 0 else 0.0
            return net_sentiment, len(items), headlines
        except Exception:
            return 0.0, 0, []

    def evaluate_with_orderbook(
        self,
        market: MarketInfo,
        bids: List[Tuple[float, float]],
        asks: List[Tuple[float, float]],
    ) -> Optional[EvaluationResult]:
        if not bids or not asks:
            return None

        best_bid = bids[0][0]
        best_ask = asks[0][0]
        midpoint = 0.5 * (best_bid + best_ask)
        spread = best_ask - best_bid

        # Ignore extreme 99.5%+ or 0.5%- dead markets or super wide spread > 6%
        if midpoint < 0.04 or midpoint > 0.96 or spread > 0.06:
            return None

        # Calculate near-touch Order Book Imbalance (top 3 levels within 3 cents of touch)
        bid_depth_usdc = sum(p * s for p, s in bids[:4] if best_bid - p <= 0.035)
        ask_depth_usdc = sum(p * s for p, s in asks[:4] if p - best_ask <= 0.035)
        total_near_depth = bid_depth_usdc + ask_depth_usdc
        if total_near_depth < 500:
            return None

        # Imbalance in [-1, +1]: +1 means massive bid wall (buying pressure), -1 means massive ask wall
        obi = (bid_depth_usdc - ask_depth_usdc) / total_near_depth

        # Also calculate Micro-price (volume-weighted touch price)
        top_bid_p, top_bid_s = bids[0]
        top_ask_p, top_ask_s = asks[0]
        micro_price = (top_bid_p * top_ask_s + top_ask_p * top_bid_s) / (top_bid_s + top_ask_s)

        # Fetch news sentiment for this event
        query = self._extract_search_query(market.question)
        sentiment, news_count, headlines = self.fetch_news_sentiment(query)

        # Combine Order Book Imbalance + News Sentiment + Gamma-vs-CLOB lead-lag
        # Notice: Only generate a strong >8pp signal when BOTH microstructure (strong OBI >= 0.45)
        # AND news/momentum align, or when Gamma indicative price lags a sharp CLOB move.
        shift = 0.0
        reasons = []

        if abs(obi) >= 0.40:
            obi_shift = obi * 0.075  # up to ±7.5 pp from strong orderbook absorption/imbalance
            shift += obi_shift
            reasons.append(
                f"CLOB near-touch depth imbalance OBI={obi:+.2f} "
                f"(BidDepth=${bid_depth_usdc:,.0f} vs AskDepth=${ask_depth_usdc:,.0f})"
            )

        if news_count >= 3 and abs(sentiment) >= 0.20:
            news_shift = sentiment * 0.055  # up to ±5.5 pp from authoritative news consensus
            shift += news_shift
            reasons.append(
                f"News sentiment={sentiment:+.2f} ({news_count} articles; top: '{headlines[0] if headlines else ''}')"
            )

        if abs(shift) < 0.04:
            return None

        p_yes = min(max(midpoint + shift, 0.02), 0.98)

        return EvaluationResult(
            market_id=market.id,
            question=market.question,
            category=market.category,
            oracle_used="NewsAndCLOBMicrostructure",
            official_source=market.resolution_source,
            p_yes=round(p_yes, 4),
            p_no=round(1.0 - p_yes, 4),
            confidence=round(min(0.55 + abs(shift) * 2.5, 0.85), 2),
            rationale=" | ".join(reasons),
            supporting_data={
                "midpoint": midpoint,
                "micro_price": round(micro_price, 4),
                "obi": round(obi, 3),
                "bid_depth_usdc": round(bid_depth_usdc, 2),
                "ask_depth_usdc": round(ask_depth_usdc, 2),
                "news_sentiment": round(sentiment, 3),
                "news_count": news_count,
                "headlines": headlines,
            },
        )
