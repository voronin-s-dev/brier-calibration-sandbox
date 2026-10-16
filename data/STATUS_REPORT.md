# 📊 Отчёт симулятора Polymarket (Устав Grok Bot — Демо-счёт)
**Обновлено:** `2026-10-16 15:38:51 UTC`

## 💰 Состояние виртуального портфеля
| Показатель | Значение | Правило устава |
| :--- | :--- | :--- |
| **Стартовый капитал** | `$50.00 USDC` | Не добавлять деньги |
| **Текущий баланс (Equity)** | **`$32.68 USDC`** (`-17.32$` / `-34.64%`) | Cash + Mark-to-Market по CLOB Bid |
| **Свободный кэш / В сделках** | `$29.25` / `$3.43 USDC` | До 8 открытых позиций, макс 8% банка |
| **Цель окупаемости подписки** | `$-17.32 / $60.00` (`0.0%`) | Цель: +$60.00 в месяц |
| **Просадка от пика (Текущая / Макс)** | `39.20%` / `39.20%` (Пик: `$53.75`) | Стоп-кран при просадке 40% |
| **Закрытых сделок / Win Rate** | `25` / `28.0%` | Brier Score: `0.3143` |

## 📂 Открытые позиции (3 / 8)
| # | Рынок | Кат. | Исход | Вход (Ask VWAP) | Текущий Bid | Оценка бота | Размер ($) | Нереализ. PnL | Источник |
| :- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| #26 | Will the highest temperature in Seoul (Incheon) be 25°C | Weather | **NO** | `0.570` | `0.570` | `82.1%` | `$1.34` | `$+0.00` | METAR RKSI (Seoul Incheon) |
| #27 | Will the price of Bitcoin be above $80,000 on October 1 | Crypto | **NO** | `0.089` | `0.070` | `13.5%` | `$1.01` | `$-0.22` | https://www.binance.com/en/tra |
| #28 | Will Bitcoin reach $83,000 on October 16? | Crypto | **NO** | `0.870` | `0.860` | `93.2%` | `$1.31` | `$-0.02` | https://www.binance.com/en/tra |

## 🔍 Последние проверенные кандидаты и фильтр стакана CLOB
| Рынок | Кат. | Сторона | Оценка бота | Цена Ask | Перекос (Edge) | Проскальзывание CLOB | Решение |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Israel x Iran ceasefire continues through October  | Geopolitics | NO | `11.2%` | `7.0%` | `+4.2 п.п.` | `2.00%` | REJECTED: Edge +4.2 pp < 5 pp threshold (P_est=11.2% vs AskVWAP=7.0%) |
| Will the Fed increase interest rates by 25 bps aft | Macro | YES | `19.0%` | `14.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Edge +5.0 pp < 5 pp threshold (P_est=19.0% vs AskVWAP=14.0%) |
| Will the highest temperature in Seoul (Incheon) be | Weather | NO | `87.5%` | `56.0%` | `+31.5 п.п.` | `3.00%` | REJECTED: CLOB round-trip slippage 3.00% > 2.5% limit |
| Will the highest temperature in Amsterdam be 14°C  | Weather | NO | `69.7%` | `42.0%` | `+27.7 п.п.` | `4.00%` | REJECTED: CLOB round-trip slippage 4.00% > 2.5% limit |
| Will the price of Bitcoin be above $80,000 on Octo | Crypto | NO | `27.0%` | `23.0%` | `+4.0 п.п.` | `3.00%` | REJECTED: Edge +4.0 pp < 5 pp threshold (P_est=27.0% vs AskVWAP=23.0%) |
| Will Bitcoin reach $83,000 on October 16? | Crypto | NO | `93.2%` | `87.0%` | `+6.2 п.п.` | `1.00%` | EXECUTED BUY #28 ($1.31 @ 0.8700) |
| Will the price of Bitcoin be above $80,000 on Octo | Crypto | NO | `11.0%` | `5.7%` | `+5.3 п.п.` | `0.40%` | REJECTED: Calculated 0.25x Kelly bet $0.46 below $1.00 min or > cash $30.56 |
| Will the Fed increase interest rates by 25 bps aft | Macro | YES | `19.0%` | `14.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Edge +5.0 pp < 5 pp threshold (P_est=19.0% vs AskVWAP=14.0%) |
| Will the highest temperature in Seoul (Incheon) be | Weather | NO | `87.5%` | `56.0%` | `+31.5 п.п.` | `3.00%` | REJECTED: CLOB round-trip slippage 3.00% > 2.5% limit |
| Will the highest temperature in Amsterdam be 14°C  | Weather | NO | `69.8%` | `42.0%` | `+27.8 п.п.` | `4.00%` | REJECTED: CLOB round-trip slippage 4.00% > 2.5% limit |
| Will the price of Bitcoin be above $80,000 on Octo | Crypto | NO | `28.5%` | `24.0%` | `+4.5 п.п.` | `2.00%` | REJECTED: Edge +4.5 pp < 5 pp threshold (P_est=28.5% vs AskVWAP=24.0%) |
| Will the price of Bitcoin be above $80,000 on Octo | Crypto | NO | `20.1%` | `8.9%` | `+11.2 п.п.` | `0.80%` | EXECUTED BUY #27 ($1.01 @ 0.0890) |
| Will the price of Bitcoin be above $84,000 on Octo | Crypto | NO | `86.0%` | `81.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Edge +5.0 pp < 5 pp threshold (P_est=86.0% vs AskVWAP=81.0%) |
| Will the price of Bitcoin be above $80,000 on Octo | Crypto | NO | `12.4%` | `7.6%` | `+4.8 п.п.` | `1.46%` | REJECTED: Edge +4.8 pp < 5 pp threshold (P_est=12.4% vs AskVWAP=7.6%) |
| Will the highest temperature in Seoul (Incheon) be | Weather | NO | `82.2%` | `57.0%` | `+25.2 п.п.` | `2.00%` | EXECUTED BUY #26 ($1.34 @ 0.5700) |
| Will Bitcoin reach $84,000 on October 16? | Crypto | NO | `78.7%` | `74.0%` | `+4.7 п.п.` | `1.00%` | REJECTED: Edge +4.7 pp < 5 pp threshold (P_est=78.7% vs AskVWAP=74.0%) |
| Will the price of Bitcoin be above $80,000 on Octo | Crypto | NO | `20.0%` | `16.0%` | `+4.0 п.п.` | `3.00%` | REJECTED: Edge +4.0 pp < 5 pp threshold (P_est=20.0% vs AskVWAP=16.0%) |
| Shanghai Rolex Masters: Daniil Medvedev vs Tommy P | Sports | NO | `24.0%` | `31.0%` | `-7.0 п.п.` | `3.00%` | REJECTED: Edge -7.0 pp < 5 pp threshold (P_est=24.0% vs AskVWAP=31.0%) |
