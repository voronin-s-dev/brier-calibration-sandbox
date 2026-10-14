# 📊 Отчёт симулятора Polymarket (Устав Grok Bot — Демо-счёт)
**Обновлено:** `2026-10-14 08:16:22 UTC`

## 💰 Состояние виртуального портфеля
| Показатель | Значение | Правило устава |
| :--- | :--- | :--- |
| **Стартовый капитал** | `$50.00 USDC` | Не добавлять деньги |
| **Текущий баланс (Equity)** | **`$40.36 USDC`** (`-9.64$` / `-19.28%`) | Cash + Mark-to-Market по CLOB Bid |
| **Свободный кэш / В сделках** | `$35.15` / `$5.21 USDC` | До 8 открытых позиций, макс 8% банка |
| **Цель окупаемости подписки** | `$-9.64 / $60.00` (`0.0%`) | Цель: +$60.00 в месяц |
| **Просадка от пика (Текущая / Макс)** | `24.91%` / `24.91%` (Пик: `$53.75`) | Стоп-кран при просадке 40% |
| **Закрытых сделок / Win Rate** | `12` / `33.3%` | Brier Score: `0.3143` |

## 📂 Открытые позиции (3 / 8)
| # | Рынок | Кат. | Исход | Вход (Ask VWAP) | Текущий Bid | Оценка бота | Размер ($) | Нереализ. PnL | Источник |
| :- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| #9 | Will Bitcoin dip to $80,000 October 12-18? | Crypto | **YES** | `0.300` | `0.170` | `35.4%` | `$3.07` | `$-1.33` | Binance BTCUSDT 1m/1h Spot Kli |
| #13 | Will Ethereum reach $2,700 October 12-18? | Crypto | **YES** | `0.130` | `0.120` | `20.8%` | `$2.33` | `$-0.18` | Binance ETHUSDT 1m/1h Spot Kli |
| #15 | Will the highest temperature in Munich be 18°C or highe | Weather | **NO** | `0.390` | `0.310` | `56.2%` | `$1.66` | `$-0.34` | METAR EDDM (Munich Airport) |

## 🔍 Последние проверенные кандидаты и фильтр стакана CLOB
| Рынок | Кат. | Сторона | Оценка бота | Цена Ask | Перекос (Edge) | Проскальзывание CLOB | Решение |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Will the highest temperature in Houston be between | Weather | NO | `72.7%` | `61.0%` | `+11.7 п.п.` | `3.00%` | REJECTED: CLOB round-trip slippage 3.00% > 2.0% limit |
| Will the highest temperature in Houston be between | Weather | NO | `72.8%` | `61.0%` | `+11.8 п.п.` | `3.00%` | REJECTED: CLOB round-trip slippage 3.00% > 2.0% limit |
| Will the highest temperature in Houston be between | Weather | NO | `72.8%` | `61.0%` | `+11.8 п.п.` | `3.00%` | REJECTED: CLOB round-trip slippage 3.00% > 2.0% limit |
| Will the highest temperature in Houston be between | Weather | NO | `77.6%` | `69.0%` | `+8.6 п.п.` | `4.00%` | REJECTED: CLOB round-trip slippage 4.00% > 2.0% limit |
| Will the highest temperature in Houston be between | Weather | NO | `77.4%` | `69.0%` | `+8.4 п.п.` | `5.00%` | REJECTED: CLOB round-trip slippage 5.00% > 2.0% limit |
| Will the highest temperature in Munich be 18°C or  | Weather | NO | `62.5%` | `39.0%` | `+23.5 п.п.` | `1.00%` | EXECUTED BUY #15 ($1.66 @ 0.3900) |
| Will Ethereum reach $2,800 October 12-18? | Crypto | YES | `7.2%` | `3.2%` | `+4.0 п.п.` | `0.90%` | REJECTED: Edge +4.0 pp < 8 pp threshold (P_est=7.2% vs AskVWAP=3.2%) |
| Will the price of Bitcoin be above $92,000 on Octo | Crypto | YES | `2.0%` | `100.0%` | `-98.0 п.п.` | `100.00%` | REJECTED: Edge -98.0 pp < 8 pp threshold (P_est=2.0% vs AskVWAP=100.0%) |
| Will the price of Bitcoin be above $74,000 on Octo | Crypto | NO | `0.5%` | `100.0%` | `-99.5 п.п.` | `100.00%` | REJECTED: Edge -99.5 pp < 8 pp threshold (P_est=0.5% vs AskVWAP=100.0%) |
| Will the price of Bitcoin be above $76,000 on Octo | Crypto | NO | `0.5%` | `100.0%` | `-99.5 п.п.` | `100.00%` | REJECTED: Edge -99.5 pp < 8 pp threshold (P_est=0.5% vs AskVWAP=100.0%) |
| Will the highest temperature in Cape Town be 19°C  | Weather | NO | `76.7%` | `63.1%` | `+13.7 п.п.` | `2.06%` | REJECTED: CLOB round-trip slippage 2.06% > 2.0% limit |
| Will the price of Ethereum be above $2,400 on Octo | Crypto | YES | `91.0%` | `87.0%` | `+4.0 п.п.` | `3.00%` | REJECTED: Edge +4.0 pp < 8 pp threshold (P_est=91.0% vs AskVWAP=87.0%) |
| Will the price of Ethereum be above $2,600 on Octo | Crypto | NO | `91.0%` | `87.0%` | `+4.0 п.п.` | `3.00%` | REJECTED: Edge +4.0 pp < 8 pp threshold (P_est=91.0% vs AskVWAP=87.0%) |
| Will the price of Bitcoin be above $84,000 on Octo | Crypto | YES | `40.0%` | `35.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Edge +5.0 pp < 8 pp threshold (P_est=40.0% vs AskVWAP=35.0%) |
| Will the highest temperature in Cape Town be 19°C  | Weather | NO | `77.8%` | `70.0%` | `+7.8 п.п.` | `4.00%` | REJECTED: Edge +7.8 pp < 8 pp threshold (P_est=77.8% vs AskVWAP=70.0%) |
| Will the price of Ethereum be above $2,600 on Octo | Crypto | NO | `90.5%` | `86.0%` | `+4.5 п.п.` | `2.00%` | REJECTED: Edge +4.5 pp < 8 pp threshold (P_est=90.5% vs AskVWAP=86.0%) |
| Will the highest temperature in Manila be 33°C on  | Weather | NO | `71.6%` | `64.0%` | `+7.6 п.п.` | `5.00%` | REJECTED: Edge +7.6 pp < 8 pp threshold (P_est=71.6% vs AskVWAP=64.0%) |
| Will the price of Bitcoin be above $80,000 on Octo | Crypto | NO | `17.0%` | `12.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Edge +5.0 pp < 8 pp threshold (P_est=17.0% vs AskVWAP=12.0%) |
