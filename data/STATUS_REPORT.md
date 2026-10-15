# 📊 Отчёт симулятора Polymarket (Устав Grok Bot — Демо-счёт)
**Обновлено:** `2026-10-15 09:56:54 UTC`

## 💰 Состояние виртуального портфеля
| Показатель | Значение | Правило устава |
| :--- | :--- | :--- |
| **Стартовый капитал** | `$50.00 USDC` | Не добавлять деньги |
| **Текущий баланс (Equity)** | **`$38.47 USDC`** (`-11.53$` / `-23.06%`) | Cash + Mark-to-Market по CLOB Bid |
| **Свободный кэш / В сделках** | `$37.30` / `$1.17 USDC` | До 8 открытых позиций, макс 8% банка |
| **Цель окупаемости подписки** | `$-11.53 / $60.00` (`0.0%`) | Цель: +$60.00 в месяц |
| **Просадка от пика (Текущая / Макс)** | `28.42%` / `28.60%` (Пик: `$53.75`) | Стоп-кран при просадке 40% |
| **Закрытых сделок / Win Rate** | `13` / `30.8%` | Brier Score: `0.3143` |

## 📂 Открытые позиции (2 / 8)
| # | Рынок | Кат. | Исход | Вход (Ask VWAP) | Текущий Bid | Оценка бота | Размер ($) | Нереализ. PnL | Источник |
| :- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| #13 | Will Ethereum reach $2,700 October 12-18? | Crypto | **YES** | `0.130` | `0.006` | `18.7%` | `$2.33` | `$-2.22` | Binance ETHUSDT 1m/1h Spot Kli |
| #15 | Will the highest temperature in Munich be 18°C or highe | Weather | **NO** | `0.390` | `0.250` | `58.0%` | `$1.66` | `$-0.60` | METAR EDDM (Munich Airport) |

## 🔍 Последние проверенные кандидаты и фильтр стакана CLOB
| Рынок | Кат. | Сторона | Оценка бота | Цена Ask | Перекос (Edge) | Проскальзывание CLOB | Решение |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Will the highest temperature in Toronto be 16°C or | Weather | YES | `84.8%` | `77.0%` | `+7.8 п.п.` | `2.00%` | REJECTED: Edge +7.8 pp < 8 pp threshold (P_est=84.8% vs AskVWAP=77.0%) |
| Will the highest temperature in Toronto be 16°C or | Weather | YES | `84.7%` | `77.0%` | `+7.7 п.п.` | `2.00%` | REJECTED: Edge +7.7 pp < 8 pp threshold (P_est=84.7% vs AskVWAP=77.0%) |
| Will the highest temperature in Toronto be 16°C or | Weather | YES | `84.6%` | `77.0%` | `+7.6 п.п.` | `2.00%` | REJECTED: Edge +7.6 pp < 8 pp threshold (P_est=84.6% vs AskVWAP=77.0%) |
| Will the highest temperature in Wuhan be 20°C on O | Weather | YES | `7.2%` | `100.0%` | `-92.8 п.п.` | `100.00%` | REJECTED: Edge -92.8 pp < 8 pp threshold (P_est=7.2% vs AskVWAP=100.0%) |
| Will the highest temperature in Wuhan be 21°C on O | Weather | YES | `13.9%` | `100.0%` | `-86.2 п.п.` | `100.00%` | REJECTED: Edge -86.1 pp < 8 pp threshold (P_est=13.9% vs AskVWAP=100.0%) |
| Will the highest temperature in Wuhan be 22°C on O | Weather | YES | `17.8%` | `100.0%` | `-82.2 п.п.` | `100.00%` | REJECTED: Edge -82.2 pp < 8 pp threshold (P_est=17.8% vs AskVWAP=100.0%) |
| Will the highest temperature in Istanbul be 14°C o | Weather | YES | `4.6%` | `0.4%` | `+4.3 п.п.` | `0.26%` | REJECTED: Edge +4.3 pp < 8 pp threshold (P_est=4.6% vs AskVWAP=0.4%) |
| Will the highest temperature in Wellington be 15°C | Weather | YES | `17.8%` | `100.0%` | `-82.2 п.п.` | `100.00%` | REJECTED: Edge -82.2 pp < 8 pp threshold (P_est=17.8% vs AskVWAP=100.0%) |
| Will the highest temperature in Wuhan be 20°C on O | Weather | YES | `7.2%` | `100.0%` | `-92.8 п.п.` | `100.00%` | REJECTED: Edge -92.8 pp < 8 pp threshold (P_est=7.2% vs AskVWAP=100.0%) |
| Will the highest temperature in Istanbul be 14°C o | Weather | YES | `4.6%` | `0.4%` | `+4.2 п.п.` | `0.28%` | REJECTED: Edge +4.2 pp < 8 pp threshold (P_est=4.6% vs AskVWAP=0.4%) |
| Will the highest temperature in Wuhan be 21°C on O | Weather | YES | `13.9%` | `100.0%` | `-86.2 п.п.` | `100.00%` | REJECTED: Edge -86.1 pp < 8 pp threshold (P_est=13.9% vs AskVWAP=100.0%) |
| Will the highest temperature in Wuhan be 22°C on O | Weather | YES | `17.8%` | `100.0%` | `-82.2 п.п.` | `100.00%` | REJECTED: Edge -82.2 pp < 8 pp threshold (P_est=17.8% vs AskVWAP=100.0%) |
| Will the highest temperature in Wellington be 15°C | Weather | YES | `17.8%` | `100.0%` | `-82.2 п.п.` | `100.00%` | REJECTED: Edge -82.2 pp < 8 pp threshold (P_est=17.8% vs AskVWAP=100.0%) |
| Will the highest temperature in Wuhan be 20°C on O | Weather | YES | `7.2%` | `100.0%` | `-92.8 п.п.` | `100.00%` | REJECTED: Edge -92.8 pp < 8 pp threshold (P_est=7.2% vs AskVWAP=100.0%) |
| Will the highest temperature in Istanbul be 14°C o | Weather | YES | `4.6%` | `0.4%` | `+4.3 п.п.` | `0.26%` | REJECTED: Edge +4.3 pp < 8 pp threshold (P_est=4.6% vs AskVWAP=0.4%) |
| Will the highest temperature in Wuhan be 21°C on O | Weather | YES | `13.9%` | `100.0%` | `-86.2 п.п.` | `100.00%` | REJECTED: Edge -86.1 pp < 8 pp threshold (P_est=13.9% vs AskVWAP=100.0%) |
| Will the highest temperature in Wuhan be 22°C on O | Weather | YES | `17.8%` | `100.0%` | `-82.2 п.п.` | `100.00%` | REJECTED: Edge -82.2 pp < 8 pp threshold (P_est=17.8% vs AskVWAP=100.0%) |
| Will the highest temperature in Wellington be 15°C | Weather | YES | `17.8%` | `100.0%` | `-82.2 п.п.` | `100.00%` | REJECTED: Edge -82.2 pp < 8 pp threshold (P_est=17.8% vs AskVWAP=100.0%) |
