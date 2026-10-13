# 📊 Отчёт симулятора Polymarket (Устав Grok Bot — Демо-счёт)
**Обновлено:** `2026-10-13 23:24:23 UTC`

## 💰 Состояние виртуального портфеля
| Показатель | Значение | Правило устава |
| :--- | :--- | :--- |
| **Стартовый капитал** | `$50.00 USDC` | Не добавлять деньги |
| **Текущий баланс (Equity)** | **`$41.75 USDC`** (`-8.25$` / `-16.50%`) | Cash + Mark-to-Market по CLOB Bid |
| **Свободный кэш / В сделках** | `$36.81` / `$4.94 USDC` | До 8 открытых позиций, макс 8% банка |
| **Цель окупаемости подписки** | `$-8.25 / $60.00` (`0.0%`) | Цель: +$60.00 в месяц |
| **Просадка от пика (Текущая / Макс)** | `22.32%` / `22.81%` (Пик: `$53.75`) | Стоп-кран при просадке 40% |
| **Закрытых сделок / Win Rate** | `12` / `33.3%` | Brier Score: `0.3143` |

## 📂 Открытые позиции (2 / 8)
| # | Рынок | Кат. | Исход | Вход (Ask VWAP) | Текущий Bid | Оценка бота | Размер ($) | Нереализ. PnL | Источник |
| :- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| #9 | Will Bitcoin dip to $80,000 October 12-18? | Crypto | **YES** | `0.300` | `0.290` | `36.1%` | `$3.07` | `$-0.10` | Binance BTCUSDT 1m/1h Spot Kli |
| #13 | Will Ethereum reach $2,700 October 12-18? | Crypto | **YES** | `0.130` | `0.110` | `23.4%` | `$2.33` | `$-0.36` | Binance ETHUSDT 1m/1h Spot Kli |

## 🔍 Последние проверенные кандидаты и фильтр стакана CLOB
| Рынок | Кат. | Сторона | Оценка бота | Цена Ask | Перекос (Edge) | Проскальзывание CLOB | Решение |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Will the highest temperature in Cape Town be 19°C  | Weather | NO | `76.7%` | `63.1%` | `+13.7 п.п.` | `2.06%` | REJECTED: CLOB round-trip slippage 2.06% > 2.0% limit |
| Will the price of Ethereum be above $2,400 on Octo | Crypto | YES | `91.0%` | `87.0%` | `+4.0 п.п.` | `3.00%` | REJECTED: Edge +4.0 pp < 8 pp threshold (P_est=91.0% vs AskVWAP=87.0%) |
| Will the price of Ethereum be above $2,600 on Octo | Crypto | NO | `91.0%` | `87.0%` | `+4.0 п.п.` | `3.00%` | REJECTED: Edge +4.0 pp < 8 pp threshold (P_est=91.0% vs AskVWAP=87.0%) |
| Will the price of Bitcoin be above $84,000 on Octo | Crypto | YES | `40.0%` | `35.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Edge +5.0 pp < 8 pp threshold (P_est=40.0% vs AskVWAP=35.0%) |
| Will the highest temperature in Cape Town be 19°C  | Weather | NO | `77.8%` | `70.0%` | `+7.8 п.п.` | `4.00%` | REJECTED: Edge +7.8 pp < 8 pp threshold (P_est=77.8% vs AskVWAP=70.0%) |
| Will the price of Ethereum be above $2,600 on Octo | Crypto | NO | `90.5%` | `86.0%` | `+4.5 п.п.` | `2.00%` | REJECTED: Edge +4.5 pp < 8 pp threshold (P_est=90.5% vs AskVWAP=86.0%) |
| Will the highest temperature in Manila be 33°C on  | Weather | NO | `71.6%` | `64.0%` | `+7.6 п.п.` | `5.00%` | REJECTED: Edge +7.6 pp < 8 pp threshold (P_est=71.6% vs AskVWAP=64.0%) |
| Will the price of Bitcoin be above $80,000 on Octo | Crypto | NO | `17.0%` | `12.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Edge +5.0 pp < 8 pp threshold (P_est=17.0% vs AskVWAP=12.0%) |
| Will the price of Bitcoin be above $80,000 on Octo | Crypto | NO | `12.0%` | `7.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Edge +5.0 pp < 8 pp threshold (P_est=12.0% vs AskVWAP=7.0%) |
| Will the price of Ethereum be above $2,400 on Octo | Crypto | YES | `92.5%` | `88.0%` | `+4.5 п.п.` | `2.00%` | REJECTED: Edge +4.5 pp < 8 pp threshold (P_est=92.5% vs AskVWAP=88.0%) |
| Will the price of Bitcoin be above $84,000 on Octo | Crypto | YES | `39.0%` | `34.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Edge +5.0 pp < 8 pp threshold (P_est=39.0% vs AskVWAP=34.0%) |
| Will Bitcoin dip to $82,000 on October 13? | Crypto | NO | `98.0%` | `90.0%` | `+8.0 п.п.` | `2.00%` | REJECTED: Edge +8.0 pp < 8 pp threshold (P_est=98.0% vs AskVWAP=90.0%) |
| Bitcoin Up or Down on October 14? | Crypto | YES | `47.0%` | `42.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Edge +5.0 pp < 8 pp threshold (P_est=47.0% vs AskVWAP=42.0%) |
| Will the highest temperature in Cape Town be 19°C  | Weather | NO | `78.0%` | `70.0%` | `+8.0 п.п.` | `4.00%` | REJECTED: Edge +8.0 pp < 8 pp threshold (P_est=78.0% vs AskVWAP=70.0%) |
| Will the price of Ethereum be above $2,600 on Octo | Crypto | NO | `89.5%` | `85.0%` | `+4.5 п.п.` | `2.00%` | REJECTED: Edge +4.5 pp < 8 pp threshold (P_est=89.5% vs AskVWAP=85.0%) |
| Will the highest temperature in Manila be 33°C on  | Weather | NO | `71.5%` | `63.0%` | `+8.5 п.п.` | `4.00%` | REJECTED: CLOB round-trip slippage 4.00% > 2.0% limit |
| Will the price of Bitcoin be above $80,000 on Octo | Crypto | NO | `17.0%` | `12.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Edge +5.0 pp < 8 pp threshold (P_est=17.0% vs AskVWAP=12.0%) |
| Will the price of Bitcoin be above $80,000 on Octo | Crypto | NO | `11.5%` | `7.0%` | `+4.5 п.п.` | `2.00%` | REJECTED: Edge +4.5 pp < 8 pp threshold (P_est=11.5% vs AskVWAP=7.0%) |
