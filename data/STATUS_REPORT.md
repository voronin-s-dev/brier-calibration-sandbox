# 📊 Отчёт симулятора Polymarket (Устав Grok Bot — Демо-счёт)
**Обновлено:** `2026-10-14 18:27:58 UTC`

## 💰 Состояние виртуального портфеля
| Показатель | Значение | Правило устава |
| :--- | :--- | :--- |
| **Стартовый капитал** | `$50.00 USDC` | Не добавлять деньги |
| **Текущий баланс (Equity)** | **`$38.79 USDC`** (`-11.21$` / `-22.41%`) | Cash + Mark-to-Market по CLOB Bid |
| **Свободный кэш / В сделках** | `$37.30` / `$1.49 USDC` | До 8 открытых позиций, макс 8% банка |
| **Цель окупаемости подписки** | `$-11.21 / $60.00` (`0.0%`) | Цель: +$60.00 в месяц |
| **Просадка от пика (Текущая / Макс)** | `27.82%` / `27.82%` (Пик: `$53.75`) | Стоп-кран при просадке 40% |
| **Закрытых сделок / Win Rate** | `13` / `30.8%` | Brier Score: `0.3143` |

## 📂 Открытые позиции (2 / 8)
| # | Рынок | Кат. | Исход | Вход (Ask VWAP) | Текущий Bid | Оценка бота | Размер ($) | Нереализ. PnL | Источник |
| :- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| #13 | Will Ethereum reach $2,700 October 12-18? | Crypto | **YES** | `0.130` | `0.024` | `18.7%` | `$2.33` | `$-1.90` | Binance ETHUSDT 1m/1h Spot Kli |
| #15 | Will the highest temperature in Munich be 18°C or highe | Weather | **NO** | `0.390` | `0.250` | `64.1%` | `$1.66` | `$-0.60` | METAR EDDM (Munich Airport) |

## 🔍 Последние проверенные кандидаты и фильтр стакана CLOB
| Рынок | Кат. | Сторона | Оценка бота | Цена Ask | Перекос (Edge) | Проскальзывание CLOB | Решение |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Will the highest temperature in Wuhan be 20°C on O | Weather | YES | `7.9%` | `100.0%` | `-92.1 п.п.` | `100.00%` | REJECTED: Edge -92.1 pp < 8 pp threshold (P_est=7.9% vs AskVWAP=100.0%) |
| Will the highest temperature in Wuhan be 22°C on O | Weather | YES | `17.8%` | `100.0%` | `-82.2 п.п.` | `100.00%` | REJECTED: Edge -82.2 pp < 8 pp threshold (P_est=17.8% vs AskVWAP=100.0%) |
| Will the highest temperature in Wuhan be 21°C on O | Weather | YES | `14.5%` | `100.0%` | `-85.5 п.п.` | `100.00%` | REJECTED: Edge -85.5 pp < 8 pp threshold (P_est=14.5% vs AskVWAP=100.0%) |
| Will the highest temperature in Wellington be 15°C | Weather | YES | `14.5%` | `100.0%` | `-85.5 п.п.` | `100.00%` | REJECTED: Edge -85.5 pp < 8 pp threshold (P_est=14.5% vs AskVWAP=100.0%) |
| Will the highest temperature in Wuhan be 20°C on O | Weather | YES | `7.9%` | `100.0%` | `-92.1 п.п.` | `100.00%` | REJECTED: Edge -92.1 pp < 8 pp threshold (P_est=7.9% vs AskVWAP=100.0%) |
| Will the highest temperature in Wuhan be 22°C on O | Weather | YES | `17.8%` | `100.0%` | `-82.2 п.п.` | `100.00%` | REJECTED: Edge -82.2 pp < 8 pp threshold (P_est=17.8% vs AskVWAP=100.0%) |
| Will the highest temperature in Wuhan be 21°C on O | Weather | YES | `14.5%` | `100.0%` | `-85.5 п.п.` | `100.00%` | REJECTED: Edge -85.5 pp < 8 pp threshold (P_est=14.5% vs AskVWAP=100.0%) |
| Will the highest temperature in Wellington be 15°C | Weather | YES | `14.5%` | `100.0%` | `-85.5 п.п.` | `100.00%` | REJECTED: Edge -85.5 pp < 8 pp threshold (P_est=14.5% vs AskVWAP=100.0%) |
| Will the highest temperature in Wuhan be 20°C on O | Weather | YES | `7.9%` | `100.0%` | `-92.1 п.п.` | `100.00%` | REJECTED: Edge -92.1 pp < 8 pp threshold (P_est=7.9% vs AskVWAP=100.0%) |
| Will the highest temperature in Wuhan be 22°C on O | Weather | YES | `17.8%` | `100.0%` | `-82.2 п.п.` | `100.00%` | REJECTED: Edge -82.2 pp < 8 pp threshold (P_est=17.8% vs AskVWAP=100.0%) |
| Will the highest temperature in Wuhan be 21°C on O | Weather | YES | `14.5%` | `100.0%` | `-85.5 п.п.` | `100.00%` | REJECTED: Edge -85.5 pp < 8 pp threshold (P_est=14.5% vs AskVWAP=100.0%) |
| Will the highest temperature in Wellington be 15°C | Weather | YES | `13.8%` | `100.0%` | `-86.2 п.п.` | `100.00%` | REJECTED: Edge -86.2 pp < 8 pp threshold (P_est=13.8% vs AskVWAP=100.0%) |
| Will the highest temperature in Wellington be 15°C | Weather | YES | `13.8%` | `100.0%` | `-86.2 п.п.` | `100.00%` | REJECTED: Edge -86.2 pp < 8 pp threshold (P_est=13.8% vs AskVWAP=100.0%) |
| Will the highest temperature in Wellington be 15°C | Weather | YES | `13.7%` | `100.0%` | `-86.3 п.п.` | `100.00%` | REJECTED: Edge -86.3 pp < 8 pp threshold (P_est=13.7% vs AskVWAP=100.0%) |
| Will the highest temperature in Houston be between | Weather | NO | `72.7%` | `61.0%` | `+11.7 п.п.` | `3.00%` | REJECTED: CLOB round-trip slippage 3.00% > 2.0% limit |
| Will the highest temperature in Houston be between | Weather | NO | `72.8%` | `61.0%` | `+11.8 п.п.` | `3.00%` | REJECTED: CLOB round-trip slippage 3.00% > 2.0% limit |
| Will the highest temperature in Houston be between | Weather | NO | `72.8%` | `61.0%` | `+11.8 п.п.` | `3.00%` | REJECTED: CLOB round-trip slippage 3.00% > 2.0% limit |
| Will the highest temperature in Houston be between | Weather | NO | `77.6%` | `69.0%` | `+8.6 п.п.` | `4.00%` | REJECTED: CLOB round-trip slippage 4.00% > 2.0% limit |
