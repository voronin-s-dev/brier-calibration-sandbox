# 📊 Отчёт симулятора Polymarket (Устав Grok Bot — Демо-счёт)
**Обновлено:** `2026-10-16 19:16:24 UTC`

## 💰 Состояние виртуального портфеля
| Показатель | Значение | Правило устава |
| :--- | :--- | :--- |
| **Стартовый капитал** | `$50.00 USDC` | Не добавлять деньги |
| **Текущий баланс (Equity)** | **`$32.35 USDC`** (`-17.65$` / `-35.30%`) | Cash + Mark-to-Market по CLOB Bid |
| **Свободный кэш / В сделках** | `$29.94` / `$2.42 USDC` | До 8 открытых позиций, макс 8% банка |
| **Цель окупаемости подписки** | `$-17.65 / $60.00` (`0.0%`) | Цель: +$60.00 в месяц |
| **Просадка от пика (Текущая / Макс)** | `39.81%` / `39.81%` (Пик: `$53.75`) | Стоп-кран при просадке 40% |
| **Закрытых сделок / Win Rate** | `29` / `27.6%` | Brier Score: `0.3143` |

## 📂 Открытые позиции (2 / 8)
| # | Рынок | Кат. | Исход | Вход (Ask VWAP) | Текущий Bid | Оценка бота | Размер ($) | Нереализ. PnL | Источник |
| :- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| #26 | Will the highest temperature in Seoul (Incheon) be 25°C | Weather | **NO** | `0.570` | `0.590` | `82.3%` | `$1.34` | `$+0.05` | METAR RKSI (Seoul Incheon) |
| #31 | Will Bitcoin dip to $80,000 October 12-18? | Crypto | **YES** | `0.480` | `0.380` | `66.8%` | `$1.30` | `$-0.27` | Kraken BTCUSDT 1m/1h Spot Klin |

## 🔍 Последние проверенные кандидаты и фильтр стакана CLOB
| Рынок | Кат. | Сторона | Оценка бота | Цена Ask | Перекос (Edge) | Проскальзывание CLOB | Решение |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Will the Fed increase interest rates by 25 bps aft | Macro | YES | `19.0%` | `14.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Edge +5.0 pp < 8 pp threshold (P_est=19.0% vs AskVWAP=14.0%) |
| Will the price of Bitcoin be above $88,000 on Octo | Crypto | YES | `2.0%` | `100.0%` | `-98.0 п.п.` | `100.00%` | REJECTED: Edge -98.0 pp < 8 pp threshold (P_est=2.0% vs AskVWAP=100.0%) |
| Will the highest temperature in Amsterdam be 14°C  | Weather | NO | `70.7%` | `47.0%` | `+23.7 п.п.` | `4.00%` | REJECTED: CLOB round-trip slippage 4.00% > 2.0% limit |
| Will the price of Bitcoin be between $78,000 and $ | Crypto | YES | `19.0%` | `14.7%` | `+4.3 п.п.` | `5.80%` | REJECTED: Edge +4.3 pp < 8 pp threshold (P_est=19.0% vs AskVWAP=14.7%) |
| Will the price of Bitcoin be between $80,000 and $ | Crypto | NO | `65.3%` | `46.0%` | `+19.3 п.п.` | `3.00%` | REJECTED: CLOB round-trip slippage 3.00% > 2.0% limit |
| Will the price of Ethereum be above $2,400 on Octo | Crypto | NO | `47.3%` | `40.1%` | `+7.2 п.п.` | `5.70%` | REJECTED: Edge +7.2 pp < 8 pp threshold (P_est=47.3% vs AskVWAP=40.1%) |
| Will the price of Bitcoin be above $88,000 on Octo | Crypto | YES | `7.6%` | `2.9%` | `+4.7 п.п.` | `1.48%` | REJECTED: Edge +4.7 pp < 8 pp threshold (P_est=7.6% vs AskVWAP=2.9%) |
| Will the price of Bitcoin be above $78,000 on Octo | Crypto | NO | `12.2%` | `2.3%` | `+9.9 п.п.` | `0.49%` | REJECTED: Win probability 12.2% < 55% minimum (no underdog lottery bets) |
| Will the price of Bitcoin be above $80,000 on Octo | Crypto | NO | `38.6%` | `30.0%` | `+8.6 п.п.` | `2.00%` | REJECTED: Win probability 38.6% < 55% minimum (no underdog lottery bets) |
| Will the price of Ethereum be above $2,500 on Octo | Crypto | YES | `6.5%` | `2.1%` | `+4.4 п.п.` | `0.80%` | REJECTED: Edge +4.4 pp < 8 pp threshold (P_est=6.5% vs AskVWAP=2.1%) |
| Will the price of Bitcoin be above $90,000 on Octo | Crypto | YES | `2.0%` | `100.0%` | `-98.0 п.п.` | `100.00%` | REJECTED: Edge -98.0 pp < 8 pp threshold (P_est=2.0% vs AskVWAP=100.0%) |
| Will the price of Ethereum be above $2,300 on Octo | Crypto | NO | `6.8%` | `2.2%` | `+4.6 п.п.` | `0.79%` | REJECTED: Edge +4.6 pp < 8 pp threshold (P_est=6.8% vs AskVWAP=2.2%) |
| Will the price of Bitcoin be between $80,000 and $ | Crypto | NO | `51.9%` | `26.0%` | `+25.9 п.п.` | `1.00%` | REJECTED: Win probability 51.9% < 55% minimum (no underdog lottery bets) |
| Will the price of Bitcoin be above $80,000 on Octo | Crypto | NO | `35.9%` | `24.0%` | `+11.9 п.п.` | `2.00%` | REJECTED: Win probability 35.9% < 55% minimum (no underdog lottery bets) |
| Will Bitcoin reach $84,000 October 12-18? | Crypto | YES | `29.1%` | `11.0%` | `+18.1 п.п.` | `2.15%` | REJECTED: Win probability 29.1% < 55% minimum (no underdog lottery bets) |
| Will Bitcoin reach $86,000 October 12-18? | Crypto | YES | `11.2%` | `1.4%` | `+9.8 п.п.` | `0.62%` | REJECTED: Win probability 11.2% < 55% minimum (no underdog lottery bets) |
| Will the price of Bitcoin be between $78,000 and $ | Crypto | YES | `20.2%` | `5.8%` | `+14.4 п.п.` | `1.60%` | REJECTED: Win probability 20.2% < 55% minimum (no underdog lottery bets) |
| Will the price of Ethereum be above $2,400 on Octo | Crypto | NO | `48.7%` | `34.8%` | `+13.9 п.п.` | `5.60%` | REJECTED: Win probability 48.7% < 55% minimum (no underdog lottery bets) |
