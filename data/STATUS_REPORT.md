# 📊 Отчёт симулятора Polymarket (Устав Grok Bot — Демо-счёт)
**Обновлено:** `2026-10-15 15:00:48 UTC`

## 💰 Состояние виртуального портфеля
| Показатель | Значение | Правило устава |
| :--- | :--- | :--- |
| **Стартовый капитал** | `$50.00 USDC` | Не добавлять деньги |
| **Текущий баланс (Equity)** | **`$36.23 USDC`** (`-13.77$` / `-27.54%`) | Cash + Mark-to-Market по CLOB Bid |
| **Свободный кэш / В сделках** | `$34.79` / `$1.44 USDC` | До 8 открытых позиций, макс 8% банка |
| **Цель окупаемости подписки** | `$-13.77 / $60.00` (`0.0%`) | Цель: +$60.00 в месяц |
| **Просадка от пика (Текущая / Макс)** | `32.59%` / `32.59%` (Пик: `$53.75`) | Стоп-кран при просадке 40% |
| **Закрытых сделок / Win Rate** | `17` / `23.5%` | Brier Score: `0.3143` |

## 📂 Открытые позиции (1 / 8)
| # | Рынок | Кат. | Исход | Вход (Ask VWAP) | Текущий Bid | Оценка бота | Размер ($) | Нереализ. PnL | Источник |
| :- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| #18 | Will Bitcoin reach $84,000 on October 15? | Crypto | **NO** | `0.891` | `0.886` | `94.5%` | `$1.45` | `$-0.01` | https://www.binance.com/en/tra |

## 🔍 Последние проверенные кандидаты и фильтр стакана CLOB
| Рынок | Кат. | Сторона | Оценка бота | Цена Ask | Перекос (Edge) | Проскальзывание CLOB | Решение |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Will the highest temperature in Wellington be 10°C | Weather | NO | `71.7%` | `62.0%` | `+9.7 п.п.` | `3.00%` | REJECTED: CLOB round-trip slippage 3.00% > 2.5% limit |
| Will Bitcoin reach $84,000 on October 15? | Crypto | NO | `94.5%` | `89.1%` | `+5.4 п.п.` | `0.50%` | EXECUTED BUY #18 ($1.45 @ 0.8910) |
| Will the highest temperature in Wellington be 9°C  | Weather | YES | `15.6%` | `100.0%` | `-84.4 п.п.` | `100.00%` | REJECTED: Edge -84.4 pp < 5 pp threshold (P_est=15.6% vs AskVWAP=100.0%) |
| Will the price of Bitcoin be above $80,000 on Octo | Crypto | NO | `22.0%` | `17.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Edge +5.0 pp < 5 pp threshold (P_est=22.0% vs AskVWAP=17.0%) |
| Will the price of Bitcoin be above $80,000 on Octo | Crypto | NO | `19.0%` | `14.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Edge +5.0 pp < 5 pp threshold (P_est=19.0% vs AskVWAP=14.0%) |
| Will Bitcoin dip to $79,000 on October 15? | Crypto | NO | `98.0%` | `94.0%` | `+4.0 п.п.` | `1.00%` | REJECTED: Edge +4.0 pp < 5 pp threshold (P_est=98.0% vs AskVWAP=94.0%) |
| Will the highest temperature in Wellington be 10°C | Weather | NO | `71.9%` | `62.0%` | `+9.9 п.п.` | `3.00%` | REJECTED: CLOB round-trip slippage 3.00% > 2.5% limit |
| Will the highest temperature in Wellington be 9°C  | Weather | YES | `15.6%` | `100.0%` | `-84.4 п.п.` | `100.00%` | REJECTED: Edge -84.4 pp < 5 pp threshold (P_est=15.6% vs AskVWAP=100.0%) |
| Will the price of Bitcoin be above $80,000 on Octo | Crypto | NO | `25.5%` | `21.0%` | `+4.5 п.п.` | `2.00%` | REJECTED: Edge +4.5 pp < 5 pp threshold (P_est=25.5% vs AskVWAP=21.0%) |
| Will the price of Ethereum be above $2,300 on Octo | Crypto | NO | `17.2%` | `12.9%` | `+4.2 п.п.` | `2.50%` | REJECTED: Edge +4.3 pp < 5 pp threshold (P_est=17.2% vs AskVWAP=12.9%) |
| Will Bitcoin reach $83,000 on October 15? | Crypto | NO | `74.5%` | `70.0%` | `+4.5 п.п.` | `2.00%` | REJECTED: Edge +4.5 pp < 5 pp threshold (P_est=74.5% vs AskVWAP=70.0%) |
| Will the price of Bitcoin be above $80,000 on Octo | Crypto | NO | `22.0%` | `17.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Edge +5.0 pp < 5 pp threshold (P_est=22.0% vs AskVWAP=17.0%) |
| Will the highest temperature in Houston be between | Weather | NO | `86.8%` | `67.0%` | `+19.8 п.п.` | `4.00%` | REJECTED: CLOB round-trip slippage 4.00% > 2.5% limit |
| Will Bitcoin reach $82,000 on October 15? | Crypto | YES | `34.7%` | `27.0%` | `+7.7 п.п.` | `2.00%` | REJECTED: Calculated 0.25x Kelly bet $0.99 below $1.00 min or > cash $34.60 |
| Will the price of Bitcoin be above $78,000 on Octo | Crypto | NO | `27.8%` | `21.0%` | `+6.8 п.п.` | `3.00%` | REJECTED: CLOB round-trip slippage 3.00% > 2.5% limit |
| Will the highest temperature in Wellington be 10°C | Weather | NO | `74.0%` | `69.0%` | `+5.0 п.п.` | `8.00%` | REJECTED: Edge +5.0 pp < 5 pp threshold (P_est=74.0% vs AskVWAP=69.0%) |
| Will the highest temperature in Wellington be 9°C  | Weather | YES | `15.2%` | `100.0%` | `-84.9 п.п.` | `100.00%` | REJECTED: Edge -84.9 pp < 5 pp threshold (P_est=15.2% vs AskVWAP=100.0%) |
| Will Ethereum dip to $2,300 October 12-18? | Crypto | YES | `72.0%` | `64.0%` | `+8.0 п.п.` | `1.00%` | EXECUTED BUY #17 ($1.50 @ 0.6400) |
