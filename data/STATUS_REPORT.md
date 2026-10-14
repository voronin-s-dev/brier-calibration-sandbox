# 📊 Отчёт симулятора Polymarket (Устав Grok Bot — Демо-счёт)
**Обновлено:** `2026-10-14 13:53:45 UTC`

## 💰 Состояние виртуального портфеля
| Показатель | Значение | Правило устава |
| :--- | :--- | :--- |
| **Стартовый капитал** | `$50.00 USDC` | Не добавлять деньги |
| **Текущий баланс (Equity)** | **`$39.29 USDC`** (`-10.71$` / `-21.41%`) | Cash + Mark-to-Market по CLOB Bid |
| **Свободный кэш / В сделках** | `$37.30` / `$1.99 USDC` | До 8 открытых позиций, макс 8% банка |
| **Цель окупаемости подписки** | `$-10.71 / $60.00` (`0.0%`) | Цель: +$60.00 в месяц |
| **Просадка от пика (Текущая / Макс)** | `26.89%` / `27.21%` (Пик: `$53.75`) | Стоп-кран при просадке 40% |
| **Закрытых сделок / Win Rate** | `13` / `30.8%` | Brier Score: `0.3143` |

## 📂 Открытые позиции (2 / 8)
| # | Рынок | Кат. | Исход | Вход (Ask VWAP) | Текущий Bid | Оценка бота | Размер ($) | Нереализ. PnL | Источник |
| :- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| #13 | Will Ethereum reach $2,700 October 12-18? | Crypto | **YES** | `0.130` | `0.040` | `18.7%` | `$2.33` | `$-1.61` | Binance ETHUSDT 1m/1h Spot Kli |
| #15 | Will the highest temperature in Munich be 18°C or highe | Weather | **NO** | `0.390` | `0.300` | `67.6%` | `$1.66` | `$-0.38` | METAR EDDM (Munich Airport) |

## 🔍 Последние проверенные кандидаты и фильтр стакана CLOB
| Рынок | Кат. | Сторона | Оценка бота | Цена Ask | Перекос (Edge) | Проскальзывание CLOB | Решение |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Will the highest temperature in Wellington be 15°C | Weather | YES | `13.8%` | `100.0%` | `-86.2 п.п.` | `100.00%` | REJECTED: Edge -86.2 pp < 8 pp threshold (P_est=13.8% vs AskVWAP=100.0%) |
| Will the highest temperature in Wellington be 15°C | Weather | YES | `13.8%` | `100.0%` | `-86.2 п.п.` | `100.00%` | REJECTED: Edge -86.2 pp < 8 pp threshold (P_est=13.8% vs AskVWAP=100.0%) |
| Will the highest temperature in Wellington be 15°C | Weather | YES | `13.7%` | `100.0%` | `-86.3 п.п.` | `100.00%` | REJECTED: Edge -86.3 pp < 8 pp threshold (P_est=13.7% vs AskVWAP=100.0%) |
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
