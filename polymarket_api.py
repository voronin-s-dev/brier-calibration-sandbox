"""
Polymarket Gamma API & CLOB Order Book Simulator.
Fetches active markets, extracts official resolution sources, and simulates real orderbook
matching (VWAP entry across Asks, VWAP exit across Bids, and round-trip slippage checks).
"""

import json
import re
from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any, Dict, List, Optional, Tuple

from http_tls import fetch_polymarket_json


GAMMA_HOST = "gamma-api.polymarket.com"
CLOB_HOST = "clob.polymarket.com"


@dataclass
class MarketInfo:
    id: str
    question: str
    slug: str
    description: str
    resolution_source: str
    has_official_source: bool
    end_date_iso: str
    hours_to_close: float
    liquidity_usd: float
    volume_24h_usd: float
    outcomes: List[str]
    gamma_prices: List[float]
    clob_token_ids: List[str]
    order_min_size: float
    tick_size: float
    category: str
    closed: bool = False
    resolved: bool = False
    raw: Dict[str, Any] = field(default_factory=dict)


@dataclass
class OrderBookSimulation:
    token_id: str
    side_label: str  # "YES" or "NO"
    best_bid: float
    best_ask: float
    midpoint: float
    spread_pct: float
    bet_usdc: float
    shares_filled: float
    vwap_buy_price: float
    vwap_sell_price: float
    entry_slippage_pct: float
    exit_slippage_pct: float
    roundtrip_slippage_pct: float
    sufficient_depth: bool
    passes_slippage_limit: bool
    reject_reason: str = ""


def extract_resolution_source(raw_source: str, description: str) -> Tuple[str, bool]:
    """
    Extracts the official resolution source from market metadata or description text.
    Rule #2 & #28: Never trade without an official resolution source.
    """
    if raw_source and raw_source.strip():
        return raw_source.strip(), True

    if not description:
        return "Unspecified", False

    patterns = [
        r"(?:primary\s+)?resolution\s+source\s+for\s+this\s+market\s+(?:will\s+be|is)\s+([^\.\n]+(?:\.[^\.\n]+)?)",
        r"resolved?\s+(?:using|via|by|according\s+to|based\s+on)\s+([^\.\n]+)",
        r"(https?://[^\s\)\"]+)",
    ]
    for pat in patterns:
        m = re.search(pat, description, flags=re.IGNORECASE)
        if m:
            src = m.group(1).strip()
            # Filter out overly generic non-sources if needed, though "consensus of credible reporting" is standard on PM
            if len(src) > 4:
                return src[:220], True

    # Check known official entities mentioned in description
    known_entities = [
        "Binance", "NOAA", "Weather Underground", "Associated Press", "Fox News",
        "NBC", "Official League", "FIFA", "UEFA", "NBA", "NFL", "NHL", "MLB",
        "Federal Reserve", "Bureau of Labor Statistics", "BLS", "CoinGecko", "CoinMarketCap",
    ]
    for ent in known_entities:
        if ent.lower() in description.lower():
            return f"Official {ent} data feed", True

    return "Unspecified", False


def classify_market_category(question: str, description: str) -> str:
    """Classifies market into Weather, Crypto, Macro, Geopolitics, Sports, or Other."""
    q_low = question.lower()
    text = f"{question} {description}".lower()
    if any(k in text for k in ["highest temperature", "lowest temperature", "degrees fahrenheit", "degrees celsius", "noaa", "weather.gov", "rainfall", "hurricane"]):
        return "Weather"
    if any(k in text for k in ["bitcoin", "btc/usdt", "ethereum", "eth/usdt", "solana", "sol/usdt", "xrp", "dogecoin", "binance 1 minute"]):
        return "Crypto"
    if any(k in text for k in ["fed ", "interest rate", "fomc", "cpi", "inflation", "s&p 500", "nasdaq", "gdp", "recession", "tariff"]):
        return "Macro"
    if any(k in q_low for k in ["ceasefire", "invade", "president", "senate", "house", "election", "prime minister", "ukraine", "israel", "iran", "yemen", "china", "trump", "elon musk", "hormuz"]):
        return "Geopolitics"
    if re.search(r"\b(nba|nfl|nhl|mlb|ufc|fifa|uefa|atp|wta|f1)\b", text) or any(
        k in q_low for k in [" vs.", " vs ", "win on 202", "spread:", "o/u ", "counter-strike", "league of legends", "valorant", "dota", "rainbow six"]
    ):
        return "Sports"
    return "Other"


def parse_market_dict(m: Dict[str, Any], now_utc: Optional[datetime] = None) -> Optional[MarketInfo]:
    """Parses a raw Gamma API market dictionary into a structured MarketInfo."""
    if now_utc is None:
        now_utc = datetime.now(timezone.utc)

    if not m.get("enableOrderBook", True):
        return None

    try:
        outcomes = json.loads(m.get("outcomes", "[]")) if isinstance(m.get("outcomes"), str) else (m.get("outcomes") or [])
        prices_raw = json.loads(m.get("outcomePrices", "[]")) if isinstance(m.get("outcomePrices"), str) else (m.get("outcomePrices") or [])
        tokens = json.loads(m.get("clobTokenIds", "[]")) if isinstance(m.get("clobTokenIds"), str) else (m.get("clobTokenIds") or [])
    except Exception:
        return None

    if len(outcomes) != 2 or len(tokens) != 2:
        # Focus on binary Yes/No markets with valid CLOB tokens
        return None

    try:
        gamma_prices = [float(p) for p in prices_raw]
    except Exception:
        gamma_prices = [0.5, 0.5]

    if len(gamma_prices) != 2:
        gamma_prices = [0.5, 0.5]

    end_str = m.get("endDate") or m.get("endDateIso") or ""
    hours_to_close = 9999.0
    if end_str:
        try:
            if "T" not in end_str:
                end_str = end_str + "T23:59:59Z"
            end_dt = datetime.fromisoformat(end_str.replace("Z", "+00:00"))
            hours_to_close = (end_dt - now_utc).total_seconds() / 3600.0
        except Exception:
            pass

    q = m.get("question", "").strip()
    desc = m.get("description", "").strip()
    res_src, has_src = extract_resolution_source(m.get("resolutionSource", ""), desc)
    cat = classify_market_category(q, desc)

    liq = float(m.get("liquidityNum") or m.get("liquidity") or 0.0)
    vol24 = float(m.get("volume24hr") or 0.0)
    min_size = float(m.get("orderMinSize") or 5.0)
    tick_size = float(m.get("orderPriceMinTickSize") or 0.001)

    closed = bool(m.get("closed", False))
    uma_status = str(m.get("umaResolutionStatus", "")).lower()
    resolved = closed and (uma_status == "resolved" or gamma_prices in ([1.0, 0.0], [0.0, 1.0]))

    return MarketInfo(
        id=str(m.get("id", "")),
        question=q,
        slug=str(m.get("slug", "")),
        description=desc,
        resolution_source=res_src,
        has_official_source=has_src,
        end_date_iso=end_str,
        hours_to_close=hours_to_close,
        liquidity_usd=liq,
        volume_24h_usd=vol24,
        outcomes=[str(o) for o in outcomes],
        gamma_prices=gamma_prices,
        clob_token_ids=[str(t) for t in tokens],
        order_min_size=min_size,
        tick_size=tick_size,
        category=cat,
        closed=closed,
        resolved=resolved,
        raw=m,
    )


def fetch_active_markets(max_Count: int = 600) -> List[MarketInfo]:
    """
    Fetches up to max_Count active markets from Polymarket Gamma API,
    sorted by 24h volume descending.
    """
    now_utc = datetime.now(timezone.utc)
    results: List[MarketInfo] = []
    seen_ids = set()

    batch_size = 100
    for offset in range(0, max_Count, batch_size):
        path = (
            f"/markets?active=true&closed=false&limit={batch_size}"
            f"&offset={offset}&order=volume24hr&ascending=false"
        )
        try:
            batch = fetch_polymarket_json(GAMMA_HOST, path)
        except Exception as e:
            if offset == 0:
                raise
            break

        if not isinstance(batch, list) or not batch:
            break

        for item in batch:
            mid = str(item.get("id", ""))
            if mid in seen_ids:
                continue
            seen_ids.add(mid)
            parsed = parse_market_dict(item, now_utc=now_utc)
            if parsed is not None:
                results.append(parsed)

    return results


def fetch_market_by_id(market_id: str) -> Optional[MarketInfo]:
    """Fetches a single market by ID from Gamma API (used to check resolution & status)."""
    try:
        data = fetch_polymarket_json(GAMMA_HOST, f"/markets/{market_id}")
        if isinstance(data, dict):
            return parse_market_dict(data)
    except Exception:
        pass
    return None


def fetch_clob_book(token_id: str) -> Dict[str, List[Tuple[float, float]]]:
    """
    Fetches live CLOB order book for token_id.
    Returns:
      {
        "bids": [(price_desc, size), ...],  # Highest (best) bid first!
        "asks": [(price_asc, size), ...],   # Lowest (best) ask first!
      }
    """
    raw_book = fetch_polymarket_json(CLOB_HOST, f"/book?token_id={token_id}")
    raw_bids = raw_book.get("bids", []) if isinstance(raw_book, dict) else []
    raw_asks = raw_book.get("asks", []) if isinstance(raw_book, dict) else []

    bids: List[Tuple[float, float]] = []
    for b in raw_bids:
        try:
            p = float(b["price"])
            s = float(b["size"])
            if p > 0 and s > 0:
                bids.append((p, s))
        except Exception:
            continue

    asks: List[Tuple[float, float]] = []
    for a in raw_asks:
        try:
            p = float(a["price"])
            s = float(a["size"])
            if p > 0 and s > 0:
                asks.append((p, s))
        except Exception:
            continue

    # CRITICAL: Sort bids descending (highest price first) and asks ascending (lowest price first)
    bids.sort(key=lambda x: x[0], reverse=True)
    asks.sort(key=lambda x: x[0], reverse=False)

    return {"bids": bids, "asks": asks}


def simulate_clob_buy_and_exit_check(
    token_id: str,
    side_label: str,
    bet_usdc: float,
    max_slippage_pct: float = 0.03,
) -> OrderBookSimulation:
    """
    Walks the real CLOB orderbook to simulate:
    1) Buying `bet_usdc` worth of `token_id` across the Asks (lowest ask upwards).
    2) Immediately selling those exact `shares_filled` across the Bids (highest bid downwards)
       to verify Rule #6: "входи, только если выйдешь из всей позиции с проскальзыванием до 3%".
    """
    book = fetch_clob_book(token_id)
    bids = book["bids"]
    asks = book["asks"]

    if not asks or not bids:
        return OrderBookSimulation(
            token_id=token_id,
            side_label=side_label,
            best_bid=bids[0][0] if bids else 0.0,
            best_ask=asks[0][0] if asks else 1.0,
            midpoint=0.5,
            spread_pct=1.0,
            bet_usdc=bet_usdc,
            shares_filled=0.0,
            vwap_buy_price=1.0,
            vwap_sell_price=0.0,
            entry_slippage_pct=1.0,
            exit_slippage_pct=1.0,
            roundtrip_slippage_pct=1.0,
            sufficient_depth=False,
            passes_slippage_limit=False,
            reject_reason="Empty bids or asks in CLOB orderbook",
        )

    best_bid = bids[0][0]
    best_ask = asks[0][0]
    midpoint = 0.5 * (best_bid + best_ask)
    spread_pct = (best_ask - best_bid) / best_ask if best_ask > 0 else 1.0

    # Step 1: Walk Asks to buy `bet_usdc`
    remaining_usdc = bet_usdc
    total_shares = 0.0
    total_spent = 0.0

    for ask_price, ask_size in asks:
        level_max_cost = ask_price * ask_size
        if remaining_usdc <= level_max_cost:
            shares_at_level = remaining_usdc / ask_price
            total_shares += shares_at_level
            total_spent += remaining_usdc
            remaining_usdc = 0.0
            break
        else:
            total_shares += ask_size
            total_spent += level_max_cost
            remaining_usdc -= level_max_cost

    if remaining_usdc > 0.01 or total_shares <= 0:
        return OrderBookSimulation(
            token_id=token_id,
            side_label=side_label,
            best_bid=best_bid,
            best_ask=best_ask,
            midpoint=midpoint,
            spread_pct=spread_pct,
            bet_usdc=bet_usdc,
            shares_filled=total_shares,
            vwap_buy_price=1.0,
            vwap_sell_price=0.0,
            entry_slippage_pct=1.0,
            exit_slippage_pct=1.0,
            roundtrip_slippage_pct=1.0,
            sufficient_depth=False,
            passes_slippage_limit=False,
            reject_reason="Insufficient Ask depth for order size",
        )

    vwap_buy = total_spent / total_shares
    entry_slippage = (vwap_buy - best_ask) / best_ask if best_ask > 0 else 0.0

    # Step 2: Walk Bids to simulate exiting all `total_shares`
    remaining_shares = total_shares
    total_proceeds = 0.0

    for bid_price, bid_size in bids:
        if remaining_shares <= bid_size:
            total_proceeds += remaining_shares * bid_price
            remaining_shares = 0.0
            break
        else:
            total_proceeds += bid_size * bid_price
            remaining_shares -= bid_size

    if remaining_shares > 0.01:
        return OrderBookSimulation(
            token_id=token_id,
            side_label=side_label,
            best_bid=best_bid,
            best_ask=best_ask,
            midpoint=midpoint,
            spread_pct=spread_pct,
            bet_usdc=bet_usdc,
            shares_filled=total_shares,
            vwap_buy_price=vwap_buy,
            vwap_sell_price=0.0,
            entry_slippage_pct=entry_slippage,
            exit_slippage_pct=1.0,
            roundtrip_slippage_pct=1.0,
            sufficient_depth=False,
            passes_slippage_limit=False,
            reject_reason="Insufficient Bid depth to exit position",
        )

    vwap_sell = total_proceeds / total_shares
    exit_slippage = (best_bid - vwap_sell) / best_bid if best_bid > 0 else 0.0
    # In binary prediction markets ($1.00 payout), both Edge (e.g. 8 pp = 0.08) and
    # CLOB Round-Trip Slippage/Spread (e.g. 3% = 0.03 = 3 cents per share) are measured on the $1.00 notional base:
    roundtrip_slippage = round(max(0.0, vwap_buy - vwap_sell), 6)

    passes = roundtrip_slippage <= (max_slippage_pct + 1e-6)
    reason = (
        ""
        if passes
        else f"Round-trip CLOB slippage {roundtrip_slippage*100:.2f}% exceeds limit {max_slippage_pct*100:.1f}% (Ask VWAP={vwap_buy:.4f}, Bid VWAP={vwap_sell:.4f})"
    )

    return OrderBookSimulation(
        token_id=token_id,
        side_label=side_label,
        best_bid=best_bid,
        best_ask=best_ask,
        midpoint=midpoint,
        spread_pct=spread_pct,
        bet_usdc=bet_usdc,
        shares_filled=total_shares,
        vwap_buy_price=vwap_buy,
        vwap_sell_price=vwap_sell,
        entry_slippage_pct=entry_slippage,
        exit_slippage_pct=exit_slippage,
        roundtrip_slippage_pct=roundtrip_slippage,
        sufficient_depth=True,
        passes_slippage_limit=passes,
        reject_reason=reason,
    )


def simulate_clob_sell_shares(token_id: str, shares_to_sell: float) -> Tuple[float, float, float]:
    """
    Simulates selling `shares_to_sell` into the live CLOB Bid orderbook.
    Returns (vwap_sell_price, total_usdc_proceeds, best_bid).
    """
    book = fetch_clob_book(token_id)
    bids = book["bids"]
    if not bids or shares_to_sell <= 0:
        return 0.0, 0.0, 0.0

    best_bid = bids[0][0]
    remaining = shares_to_sell
    proceeds = 0.0
    for bid_price, bid_size in bids:
        if remaining <= bid_size:
            proceeds += remaining * bid_price
            remaining = 0.0
            break
        else:
            proceeds += bid_size * bid_price
            remaining -= bid_size

    filled = shares_to_sell - remaining
    vwap = proceeds / filled if filled > 0 else 0.0
    return vwap, proceeds, best_bid
