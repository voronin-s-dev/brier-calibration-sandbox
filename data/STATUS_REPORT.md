# 📊 Отчёт симулятора Polymarket (Устав Grok Bot — Демо-счёт)
**Обновлено:** `2026-10-15 13:23:44 UTC`

## 💰 Состояние виртуального портфеля
| Показатель | Значение | Правило устава |
| :--- | :--- | :--- |
| **Стартовый капитал** | `$50.00 USDC` | Не добавлять деньги |
| **Текущий баланс (Equity)** | **`$37.56 USDC`** (`-12.44$` / `-24.88%`) | Cash + Mark-to-Market по CLOB Bid |
| **Свободный кэш / В сделках** | `$34.60` / `$2.96 USDC` | До 8 открытых позиций, макс 8% банка |
| **Цель окупаемости подписки** | `$-12.44 / $60.00` (`0.0%`) | Цель: +$60.00 в месяц |
| **Просадка от пика (Текущая / Макс)** | `30.12%` / `30.12%` (Пик: `$53.75`) | Стоп-кран при просадке 40% |
| **Закрытых сделок / Win Rate** | `15` / `26.7%` | Brier Score: `0.3143` |

## 📂 Открытые позиции (2 / 8)
| # | Рынок | Кат. | Исход | Вход (Ask VWAP) | Текущий Bid | Оценка бота | Размер ($) | Нереализ. PnL | Источник |
| :- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| #16 | Will Bitcoin dip to $76,000 October 12-18? | Crypto | **YES** | `0.100` | `0.099` | `24.4%` | `$1.50` | `$-0.01` | Binance BTCUSDT 1m/1h Spot Kli |
| #17 | Will Ethereum dip to $2,300 October 12-18? | Crypto | **YES** | `0.640` | `0.630` | `72.0%` | `$1.50` | `$-0.02` | Binance ETHUSDT 1m/1h Spot Kli |

## 🔍 Последние проверенные кандидаты и фильтр стакана CLOB
| Рынок | Кат. | Сторона | Оценка бота | Цена Ask | Перекос (Edge) | Проскальзывание CLOB | Решение |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Will the highest temperature in Houston be between | Weather | NO | `86.8%` | `67.0%` | `+19.8 п.п.` | `4.00%` | REJECTED: CLOB round-trip slippage 4.00% > 2.5% limit |
| Will Bitcoin reach $82,000 on October 15? | Crypto | YES | `34.7%` | `27.0%` | `+7.7 п.п.` | `2.00%` | REJECTED: Calculated 0.25x Kelly bet $0.99 below $1.00 min or > cash $34.60 |
| Will the price of Bitcoin be above $78,000 on Octo | Crypto | NO | `27.8%` | `21.0%` | `+6.8 п.п.` | `3.00%` | REJECTED: CLOB round-trip slippage 3.00% > 2.5% limit |
| Will the highest temperature in Wellington be 10°C | Weather | NO | `74.0%` | `69.0%` | `+5.0 п.п.` | `8.00%` | REJECTED: Edge +5.0 pp < 5 pp threshold (P_est=74.0% vs AskVWAP=69.0%) |
| Will the highest temperature in Wellington be 9°C  | Weather | YES | `15.2%` | `100.0%` | `-84.9 п.п.` | `100.00%` | REJECTED: Edge -84.9 pp < 5 pp threshold (P_est=15.2% vs AskVWAP=100.0%) |
| Will Ethereum dip to $2,300 October 12-18? | Crypto | YES | `72.0%` | `64.0%` | `+8.0 п.п.` | `1.00%` | EXECUTED BUY #17 ($1.50 @ 0.6400) |
| Will the price of Bitcoin be above $90,000 on Octo | Crypto | YES | `2.0%` | `100.0%` | `-98.0 п.п.` | `100.00%` | REJECTED: Edge -98.0 pp < 5 pp threshold (P_est=2.0% vs AskVWAP=100.0%) |
| Will the price of Bitcoin be above $78,000 on Octo | Crypto | NO | `20.9%` | `13.1%` | `+7.8 п.п.` | `1.00%` | REJECTED: Calculated 0.25x Kelly bet $0.84 below $1.00 min or > cash $36.10 |
| Will Bitcoin reach $83,000 on October 15? | Crypto | YES | `12.8%` | `8.0%` | `+4.8 п.п.` | `1.00%` | REJECTED: Edge +4.8 pp < 5 pp threshold (P_est=12.8% vs AskVWAP=8.0%) |
| Will Bitcoin dip to $78,000 October 12-18? | Crypto | YES | `51.9%` | `37.0%` | `+14.9 п.п.` | `2.00%` | REJECTED: Duplicate underlying event (crypto:bitcoin:october 12) |
| Will Bitcoin dip to $76,000 October 12-18? | Crypto | YES | `24.4%` | `10.0%` | `+14.4 п.п.` | `0.10%` | EXECUTED BUY #16 ($1.50 @ 0.1000) |
| Will Bitcoin reach $88,000 October 12-18? | Crypto | YES | `7.0%` | `1.3%` | `+5.8 п.п.` | `0.30%` | REJECTED: Calculated 0.25x Kelly bet $0.55 below $1.00 min or > cash $37.60 |
| Will Bitcoin dip to $79,000 on October 15? | Crypto | YES | `39.6%` | `35.0%` | `+4.6 п.п.` | `1.00%` | REJECTED: Edge +4.6 pp < 5 pp threshold (P_est=39.6% vs AskVWAP=35.0%) |
| Will Bitcoin dip to $74,000 October 12-18? | Crypto | YES | `9.7%` | `3.7%` | `+5.9 п.п.` | `0.10%` | REJECTED: Calculated 0.25x Kelly bet $0.58 below $1.00 min or > cash $37.60 |
| Will the highest temperature in Toronto be 16°C or | Weather | YES | `84.8%` | `77.0%` | `+7.8 п.п.` | `2.00%` | REJECTED: Edge +7.8 pp < 8 pp threshold (P_est=84.8% vs AskVWAP=77.0%) |
| Will the highest temperature in Toronto be 16°C or | Weather | YES | `84.7%` | `77.0%` | `+7.7 п.п.` | `2.00%` | REJECTED: Edge +7.7 pp < 8 pp threshold (P_est=84.7% vs AskVWAP=77.0%) |
| Will the highest temperature in Toronto be 16°C or | Weather | YES | `84.6%` | `77.0%` | `+7.6 п.п.` | `2.00%` | REJECTED: Edge +7.6 pp < 8 pp threshold (P_est=84.6% vs AskVWAP=77.0%) |
| Will the highest temperature in Wuhan be 20°C on O | Weather | YES | `7.2%` | `100.0%` | `-92.8 п.п.` | `100.00%` | REJECTED: Edge -92.8 pp < 8 pp threshold (P_est=7.2% vs AskVWAP=100.0%) |
