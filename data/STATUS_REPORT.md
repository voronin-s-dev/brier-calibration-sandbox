# 📊 Отчёт симулятора Polymarket (Устав Grok Bot — Демо-счёт)
**Обновлено:** `2026-10-13 23:42:54 UTC`

## 💰 Состояние виртуального портфеля
| Показатель | Значение | Правило устава |
| :--- | :--- | :--- |
| **Стартовый капитал** | `$50.00 USDC` | Не добавлять деньги |
| **Текущий баланс (Equity)** | **`$41.65 USDC`** (`-8.35$` / `-16.71%`) | Cash + Mark-to-Market по CLOB Bid |
| **Свободный кэш / В сделках** | `$36.81` / `$4.84 USDC` | До 8 открытых позиций, макс 8% банка |
| **Цель окупаемости подписки** | `$-8.35 / $60.00` (`0.0%`) | Цель: +$60.00 в месяц |
| **Просадка от пика (Текущая / Макс)** | `22.51%` / `22.81%` (Пик: `$53.75`) | Стоп-кран при просадке 40% |
| **Закрытых сделок / Win Rate** | `12` / `33.3%` | Brier Score: `0.3143` |

## 📂 Открытые позиции (2 / 8)
| # | Рынок | Кат. | Исход | Вход (Ask VWAP) | Текущий Bid | Оценка бота | Размер ($) | Нереализ. PnL | Источник |
| :- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| #9 | Will Bitcoin dip to $80,000 October 12-18? | Crypto | **YES** | `0.300` | `0.280` | `36.1%` | `$3.07` | `$-0.20` | Binance BTCUSDT 1m/1h Spot Kli |
| #13 | Will Ethereum reach $2,700 October 12-18? | Crypto | **YES** | `0.130` | `0.110` | `23.4%` | `$2.33` | `$-0.36` | Binance ETHUSDT 1m/1h Spot Kli |

## 🔍 Последние проверенные кандидаты и фильтр стакана CLOB
| Рынок | Кат. | Сторона | Оценка бота | Цена Ask | Перекос (Edge) | Проскальзывание CLOB | Решение |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Will the price of Ethereum be above $2,400 on Octo | Crypto | YES | `91.5%` | `87.0%` | `+4.5 п.п.` | `2.00%` | REJECTED: Edge +4.5 pp < 8 pp threshold (P_est=91.5% vs AskVWAP=87.0%) |
| Will the highest temperature in Cape Town be 19°C  | Weather | NO | `77.2%` | `64.0%` | `+13.2 п.п.` | `2.04%` | REJECTED: CLOB round-trip slippage 2.04% > 2.0% limit |
| Bitcoin Up or Down on October 14? | Crypto | YES | `47.5%` | `43.0%` | `+4.5 п.п.` | `2.00%` | REJECTED: Edge +4.5 pp < 8 pp threshold (P_est=47.5% vs AskVWAP=43.0%) |
| Will the price of Bitcoin be above $84,000 on Octo | Crypto | YES | `40.0%` | `35.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Edge +5.0 pp < 8 pp threshold (P_est=40.0% vs AskVWAP=35.0%) |
| Will Bitcoin dip to $82,000 on October 13? | Crypto | NO | `98.0%` | `94.0%` | `+4.0 п.п.` | `2.00%` | REJECTED: Edge +4.0 pp < 8 pp threshold (P_est=98.0% vs AskVWAP=94.0%) |
| Will the price of Ethereum be above $2,400 on Octo | Crypto | YES | `91.0%` | `87.0%` | `+4.0 п.п.` | `3.00%` | REJECTED: Edge +4.0 pp < 8 pp threshold (P_est=91.0% vs AskVWAP=87.0%) |
| Will the highest temperature in Cape Town be 19°C  | Weather | NO | `76.9%` | `63.1%` | `+13.8 п.п.` | `2.06%` | REJECTED: CLOB round-trip slippage 2.06% > 2.0% limit |
| Bitcoin Up or Down on October 14? | Crypto | YES | `46.0%` | `41.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Edge +5.0 pp < 8 pp threshold (P_est=46.0% vs AskVWAP=41.0%) |
| Will the price of Bitcoin be above $84,000 on Octo | Crypto | YES | `40.0%` | `35.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Edge +5.0 pp < 8 pp threshold (P_est=40.0% vs AskVWAP=35.0%) |
| Will Bitcoin dip to $82,000 on October 13? | Crypto | NO | `98.0%` | `93.0%` | `+5.0 п.п.` | `2.00%` | REJECTED: Edge +5.0 pp < 8 pp threshold (P_est=98.0% vs AskVWAP=93.0%) |
| Will the highest temperature in Cape Town be 19°C  | Weather | NO | `76.7%` | `63.1%` | `+13.7 п.п.` | `2.06%` | REJECTED: CLOB round-trip slippage 2.06% > 2.0% limit |
| Will the price of Ethereum be above $2,400 on Octo | Crypto | YES | `91.0%` | `87.0%` | `+4.0 п.п.` | `3.00%` | REJECTED: Edge +4.0 pp < 8 pp threshold (P_est=91.0% vs AskVWAP=87.0%) |
| Will the price of Ethereum be above $2,600 on Octo | Crypto | NO | `91.0%` | `87.0%` | `+4.0 п.п.` | `3.00%` | REJECTED: Edge +4.0 pp < 8 pp threshold (P_est=91.0% vs AskVWAP=87.0%) |
| Will the price of Bitcoin be above $84,000 on Octo | Crypto | YES | `40.0%` | `35.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Edge +5.0 pp < 8 pp threshold (P_est=40.0% vs AskVWAP=35.0%) |
| Will the highest temperature in Cape Town be 19°C  | Weather | NO | `77.8%` | `70.0%` | `+7.8 п.п.` | `4.00%` | REJECTED: Edge +7.8 pp < 8 pp threshold (P_est=77.8% vs AskVWAP=70.0%) |
| Will the price of Ethereum be above $2,600 on Octo | Crypto | NO | `90.5%` | `86.0%` | `+4.5 п.п.` | `2.00%` | REJECTED: Edge +4.5 pp < 8 pp threshold (P_est=90.5% vs AskVWAP=86.0%) |
| Will the highest temperature in Manila be 33°C on  | Weather | NO | `71.6%` | `64.0%` | `+7.6 п.п.` | `5.00%` | REJECTED: Edge +7.6 pp < 8 pp threshold (P_est=71.6% vs AskVWAP=64.0%) |
| Will the price of Bitcoin be above $80,000 on Octo | Crypto | NO | `17.0%` | `12.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Edge +5.0 pp < 8 pp threshold (P_est=17.0% vs AskVWAP=12.0%) |
