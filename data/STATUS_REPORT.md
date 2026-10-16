# 📊 Отчёт симулятора Polymarket (Устав Grok Bot — Демо-счёт)
**Обновлено:** `2026-10-16 11:31:48 UTC`

## 💰 Состояние виртуального портфеля
| Показатель | Значение | Правило устава |
| :--- | :--- | :--- |
| **Стартовый капитал** | `$50.00 USDC` | Не добавлять деньги |
| **Текущий баланс (Equity)** | **`$33.51 USDC`** (`-16.49$` / `-32.98%`) | Cash + Mark-to-Market по CLOB Bid |
| **Свободный кэш / В сделках** | `$30.83` / `$2.68 USDC` | До 8 открытых позиций, макс 8% банка |
| **Цель окупаемости подписки** | `$-16.49 / $60.00` (`0.0%`) | Цель: +$60.00 в месяц |
| **Просадка от пика (Текущая / Макс)** | `37.65%` / `37.88%` (Пик: `$53.75`) | Стоп-кран при просадке 40% |
| **Закрытых сделок / Win Rate** | `24` / `29.2%` | Brier Score: `0.3143` |

## 📂 Открытые позиции (2 / 8)
| # | Рынок | Кат. | Исход | Вход (Ask VWAP) | Текущий Bid | Оценка бота | Размер ($) | Нереализ. PnL | Источник |
| :- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| #25 | Will Bitcoin dip to $81,000 on October 16? | Crypto | **NO** | `0.870` | `0.900` | `92.6%` | `$1.34` | `$+0.05` | https://www.binance.com/en/tra |
| #26 | Will the highest temperature in Seoul (Incheon) be 25°C | Weather | **NO** | `0.570` | `0.550` | `82.2%` | `$1.34` | `$-0.05` | METAR RKSI (Seoul Incheon) |

## 🔍 Последние проверенные кандидаты и фильтр стакана CLOB
| Рынок | Кат. | Сторона | Оценка бота | Цена Ask | Перекос (Edge) | Проскальзывание CLOB | Решение |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Will the highest temperature in Seoul (Incheon) be | Weather | NO | `82.2%` | `57.0%` | `+25.2 п.п.` | `2.00%` | EXECUTED BUY #26 ($1.34 @ 0.5700) |
| Will Bitcoin reach $84,000 on October 16? | Crypto | NO | `78.7%` | `74.0%` | `+4.7 п.п.` | `1.00%` | REJECTED: Edge +4.7 pp < 5 pp threshold (P_est=78.7% vs AskVWAP=74.0%) |
| Will the price of Bitcoin be above $80,000 on Octo | Crypto | NO | `20.0%` | `16.0%` | `+4.0 п.п.` | `3.00%` | REJECTED: Edge +4.0 pp < 5 pp threshold (P_est=20.0% vs AskVWAP=16.0%) |
| Shanghai Rolex Masters: Daniil Medvedev vs Tommy P | Sports | NO | `24.0%` | `31.0%` | `-7.0 п.п.` | `3.00%` | REJECTED: Edge -7.0 pp < 5 pp threshold (P_est=24.0% vs AskVWAP=31.0%) |
| Will there be no change in Fed interest rates afte | Macro | NO | `18.7%` | `14.0%` | `+4.7 п.п.` | `1.00%` | REJECTED: Edge +4.7 pp < 5 pp threshold (P_est=18.7% vs AskVWAP=14.0%) |
| Will the price of Bitcoin be above $80,000 on Octo | Crypto | NO | `19.5%` | `15.0%` | `+4.5 п.п.` | `2.00%` | REJECTED: Edge +4.5 pp < 5 pp threshold (P_est=19.5% vs AskVWAP=15.0%) |
| Will the price of Bitcoin be above $84,000 on Octo | Crypto | YES | `18.6%` | `13.2%` | `+5.4 п.п.` | `1.00%` | REJECTED: Calculated 0.25x Kelly bet $0.52 below $1.00 min or > cash $30.86 |
| Shanghai Rolex Masters: Daniil Medvedev vs Tommy P | Sports | NO | `19.0%` | `25.0%` | `-6.0 п.п.` | `1.00%` | REJECTED: Edge -6.0 pp < 5 pp threshold (P_est=19.0% vs AskVWAP=25.0%) |
| Will there be no change in Fed interest rates afte | Macro | NO | `18.7%` | `14.0%` | `+4.7 п.п.` | `1.00%` | REJECTED: Edge +4.7 pp < 5 pp threshold (P_est=18.7% vs AskVWAP=14.0%) |
| Will the price of Ethereum be above $2,300 on Octo | Crypto | NO | `10.2%` | `5.9%` | `+4.3 п.п.` | `3.70%` | REJECTED: Edge +4.3 pp < 5 pp threshold (P_est=10.2% vs AskVWAP=5.9%) |
| Will the price of Bitcoin be above $80,000 on Octo | Crypto | NO | `22.0%` | `18.0%` | `+4.0 п.п.` | `3.00%` | REJECTED: Edge +4.0 pp < 5 pp threshold (P_est=22.0% vs AskVWAP=18.0%) |
| Will Bitcoin dip to $81,000 on October 16? | Crypto | NO | `92.6%` | `87.0%` | `+5.6 п.п.` | `1.00%` | EXECUTED BUY #25 ($1.34 @ 0.8700) |
| Will the price of Bitcoin be above $82,000 on Octo | Crypto | YES | `64.2%` | `58.0%` | `+6.2 п.п.` | `1.00%` | EXECUTED BUY #24 ($1.23 @ 0.5800) |
| Wuhan Tennis Open: Elina Svitolina vs Sonay Kartal | Sports | YES | `57.0%` | `52.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Edge +5.0 pp < 5 pp threshold (P_est=57.0% vs AskVWAP=52.0%) |
| Will the highest temperature in Seoul (Incheon) be | Weather | NO | `81.5%` | `57.0%` | `+24.5 п.п.` | `3.00%` | REJECTED: CLOB round-trip slippage 3.00% > 2.5% limit |
| Will the price of Bitcoin be above $82,000 on Octo | Crypto | NO | `52.0%` | `47.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Duplicate underlying event (crypto:bitcoin:october 17) |
| Will the price of Bitcoin be above $80,000 on Octo | Crypto | NO | `14.0%` | `9.0%` | `+5.0 п.п.` | `1.05%` | REJECTED: Edge +5.0 pp < 5 pp threshold (P_est=14.0% vs AskVWAP=9.0%) |
| Will the price of Bitcoin be above $78,000 on Octo | Crypto | NO | `11.5%` | `5.0%` | `+6.5 п.п.` | `1.78%` | REJECTED: Calculated 0.25x Kelly bet $0.59 below $1.00 min or > cash $32.89 |
