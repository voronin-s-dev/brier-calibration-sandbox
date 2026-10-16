# 📊 Отчёт симулятора Polymarket (Устав Grok Bot — Демо-счёт)
**Обновлено:** `2026-10-16 15:48:08 UTC`

## 💰 Состояние виртуального портфеля
| Показатель | Значение | Правило устава |
| :--- | :--- | :--- |
| **Стартовый капитал** | `$50.00 USDC` | Не добавлять деньги |
| **Текущий баланс (Equity)** | **`$32.60 USDC`** (`-17.40$` / `-34.79%`) | Cash + Mark-to-Market по CLOB Bid |
| **Свободный кэш / В сделках** | `$29.25` / `$3.35 USDC` | До 8 открытых позиций, макс 8% банка |
| **Цель окупаемости подписки** | `$-17.40 / $60.00` (`0.0%`) | Цель: +$60.00 в месяц |
| **Просадка от пика (Текущая / Макс)** | `39.34%` / `39.37%` (Пик: `$53.75`) | Стоп-кран при просадке 40% |
| **Закрытых сделок / Win Rate** | `25` / `28.0%` | Brier Score: `0.3143` |

## 📂 Открытые позиции (3 / 8)
| # | Рынок | Кат. | Исход | Вход (Ask VWAP) | Текущий Bid | Оценка бота | Размер ($) | Нереализ. PnL | Источник |
| :- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| #26 | Will the highest temperature in Seoul (Incheon) be 25°C | Weather | **NO** | `0.570` | `0.570` | `82.0%` | `$1.34` | `$+0.00` | METAR RKSI (Seoul Incheon) |
| #27 | Will the price of Bitcoin be above $80,000 on October 1 | Crypto | **NO** | `0.089` | `0.062` | `12.6%` | `$1.01` | `$-0.31` | https://www.binance.com/en/tra |
| #28 | Will Bitcoin reach $83,000 on October 16? | Crypto | **NO** | `0.870` | `0.870` | `93.2%` | `$1.31` | `$-0.00` | https://www.binance.com/en/tra |

## 🔍 Последние проверенные кандидаты и фильтр стакана CLOB
| Рынок | Кат. | Сторона | Оценка бота | Цена Ask | Перекос (Edge) | Проскальзывание CLOB | Решение |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Israel x Iran ceasefire continues through October  | Geopolitics | NO | `11.3%` | `7.0%` | `+4.3 п.п.` | `1.00%` | REJECTED: Edge +4.3 pp < 5 pp threshold (P_est=11.3% vs AskVWAP=7.0%) |
| Will the Fed increase interest rates by 25 bps aft | Macro | YES | `18.0%` | `13.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Edge +5.0 pp < 5 pp threshold (P_est=18.0% vs AskVWAP=13.0%) |
| Will the highest temperature in Amsterdam be 14°C  | Weather | NO | `69.7%` | `42.0%` | `+27.7 п.п.` | `4.00%` | REJECTED: CLOB round-trip slippage 4.00% > 2.5% limit |
| Will the price of Bitcoin be above $80,000 on Octo | Crypto | NO | `27.0%` | `23.0%` | `+4.0 п.п.` | `3.00%` | REJECTED: Edge +4.0 pp < 5 pp threshold (P_est=27.0% vs AskVWAP=23.0%) |
| Will the price of Bitcoin be above $84,000 on Octo | Crypto | YES | `26.0%` | `20.0%` | `+6.0 п.п.` | `1.00%` | REJECTED: Calculated 0.25x Kelly bet $0.61 below $1.00 min or > cash $29.25 |
| Will Bitcoin dip to $80,000 on October 16? | Crypto | NO | `97.5%` | `92.1%` | `+5.4 п.п.` | `2.00%` | REJECTED: Duplicate underlying event (crypto:bitcoin:october 16) |
| Will Bitcoin dip to $81,000 on October 16? | Crypto | YES | `46.0%` | `41.0%` | `+5.0 п.п.` | `2.00%` | REJECTED: Edge +5.0 pp < 5 pp threshold (P_est=46.0% vs AskVWAP=41.0%) |
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
