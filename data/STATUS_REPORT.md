# 📊 Отчёт симулятора Polymarket (Устав Grok Bot — Демо-счёт)
**Обновлено:** `2026-10-13 12:15:19 UTC`

## 💰 Состояние виртуального портфеля
| Показатель | Значение | Правило устава |
| :--- | :--- | :--- |
| **Стартовый капитал** | `$50.00 USDC` | Не добавлять деньги |
| **Текущий баланс (Equity)** | **`$52.82 USDC`** (`+2.82$` / `+5.63%`) | Cash + Mark-to-Market по CLOB Bid |
| **Свободный кэш / В сделках** | `$46.78` / `$6.03 USDC` | До 8 открытых позиций, макс 8% банка |
| **Цель окупаемости подписки** | `$+2.82 / $60.00` (`4.7%`) | Цель: +$60.00 в месяц |
| **Просадка от пика (Текущая / Макс)** | `1.74%` / `2.43%` (Пик: `$53.75`) | Стоп-кран при просадке 40% |
| **Закрытых сделок / Win Rate** | `7` / `28.6%` | Brier Score: `N/A (ожидание экспирации)` |

## 📂 Открытые позиции (2 / 8)
| # | Рынок | Кат. | Исход | Вход (Ask VWAP) | Текущий Bid | Оценка бота | Размер ($) | Нереализ. PnL | Источник |
| :- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| #4 | Will the highest temperature in Seoul (Incheon) be 21°C | Weather | **NO** | `0.380` | `0.396` | `65.0%` | `$2.99` | `$+0.13` | METAR RKSI (Seoul Incheon) |
| #9 | Will Bitcoin dip to $80,000 October 12-18? | Crypto | **YES** | `0.300` | `0.285` | `38.1%` | `$3.07` | `$-0.15` | Binance BTCUSDT 1m/1h Spot Kli |

## 🔍 Последние проверенные кандидаты и фильтр стакана CLOB
| Рынок | Кат. | Сторона | Оценка бота | Цена Ask | Перекос (Edge) | Проскальзывание CLOB | Решение |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Will Bitcoin dip to $82,000 on October 13? | Crypto | YES | `32.6%` | `25.3%` | `+7.3 п.п.` | `2.27%` | REJECTED: Edge +7.3 pp < 8 pp threshold (P_est=32.6% vs AskVWAP=25.3%) |
| Will Bitcoin reach $90,000 October 12-18? | Crypto | YES | `10.2%` | `5.9%` | `+4.2 п.п.` | `0.70%` | REJECTED: Edge +4.3 pp < 8 pp threshold (P_est=10.2% vs AskVWAP=5.9%) |
| Will Bitcoin dip to $80,000 October 12-18? | Crypto | YES | `38.1%` | `30.0%` | `+8.1 п.п.` | `1.56%` | EXECUTED BUY #9 ($3.07 @ 0.3000) |
| Will the price of Bitcoin be above $90,000 on Octo | Crypto | YES | `2.0%` | `100.0%` | `-98.0 п.п.` | `100.00%` | REJECTED: Edge -98.0 pp < 8 pp threshold (P_est=2.0% vs AskVWAP=100.0%) |
| Capitals vs. Hurricanes | Weather | YES | `45.0%` | `40.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Edge +5.0 pp < 8 pp threshold (P_est=45.0% vs AskVWAP=40.0%) |
| Will the price of Ethereum be above $2,300 on Octo | Crypto | NO | `0.5%` | `100.0%` | `-99.5 п.п.` | `100.00%` | REJECTED: Edge -99.5 pp < 8 pp threshold (P_est=0.5% vs AskVWAP=100.0%) |
| Will the price of Ethereum be above $2,700 on Octo | Crypto | YES | `2.0%` | `100.0%` | `-98.0 п.п.` | `100.00%` | REJECTED: Edge -98.0 pp < 8 pp threshold (P_est=2.0% vs AskVWAP=100.0%) |
| Will the price of Bitcoin be above $76,000 on Octo | Crypto | NO | `0.5%` | `100.0%` | `-99.5 п.п.` | `100.00%` | REJECTED: Edge -99.5 pp < 8 pp threshold (P_est=0.5% vs AskVWAP=100.0%) |
| Will the price of Bitcoin be above $78,000 on Octo | Crypto | NO | `0.5%` | `100.0%` | `-99.5 п.п.` | `100.00%` | REJECTED: Edge -99.5 pp < 8 pp threshold (P_est=0.5% vs AskVWAP=100.0%) |
| Bitcoin Up or Down on October 13? | Crypto | YES | `82.0%` | `77.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Edge +5.0 pp < 8 pp threshold (P_est=82.0% vs AskVWAP=77.0%) |
| Will the highest temperature in Tokyo be 23°C on O | Weather | NO | `48.7%` | `0.5%` | `+48.2 п.п.` | `100.00%` | REJECTED: Insufficient Bid depth to exit position |
| Will the highest temperature in Hong Kong be 31°C  | Weather | NO | `55.2%` | `0.2%` | `+55.0 п.п.` | `100.00%` | REJECTED: Insufficient Bid depth to exit position |
| Will the highest temperature in Beijing be 21°C on | Weather | YES | `16.9%` | `100.0%` | `-83.1 п.п.` | `100.00%` | REJECTED: Edge -83.1 pp < 8 pp threshold (P_est=16.9% vs AskVWAP=100.0%) |
| Will the highest temperature in Chengdu be 28°C on | Weather | YES | `5.6%` | `100.0%` | `-94.4 п.п.` | `100.00%` | REJECTED: Edge -94.4 pp < 8 pp threshold (P_est=5.6% vs AskVWAP=100.0%) |
| Will the highest temperature in Lucknow be 32°C on | Weather | NO | `57.5%` | `25.0%` | `+32.5 п.п.` | `9.40%` | REJECTED: CLOB round-trip slippage 9.40% > 3.0% limit |
| Will Bitcoin reach $90,000 October 12-18? | Crypto | NO | `98.0%` | `93.9%` | `+4.1 п.п.` | `0.80%` | REJECTED: Edge +4.1 pp < 8 pp threshold (P_est=98.0% vs AskVWAP=93.9%) |
| Will the highest temperature in Seoul (Incheon) be | Weather | YES | `9.8%` | `100.0%` | `-90.2 п.п.` | `100.00%` | REJECTED: Edge -90.2 pp < 8 pp threshold (P_est=9.8% vs AskVWAP=100.0%) |
| Will the highest temperature in Hong Kong be 30°C  | Weather | YES | `16.9%` | `100.0%` | `-83.1 п.п.` | `100.00%` | REJECTED: Edge -83.1 pp < 8 pp threshold (P_est=16.9% vs AskVWAP=100.0%) |
