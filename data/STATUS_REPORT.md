# 📊 Отчёт симулятора Polymarket (Устав Grok Bot — Демо-счёт)
**Обновлено:** `2026-10-13 09:44:30 UTC`

## 💰 Состояние виртуального портфеля
| Показатель | Значение | Правило устава |
| :--- | :--- | :--- |
| **Стартовый капитал** | `$50.00 USDC` | Не добавлять деньги |
| **Текущий баланс (Equity)** | **`$52.64 USDC`** (`+2.64$` / `+5.28%`) | Cash + Mark-to-Market по CLOB Bid |
| **Свободный кэш / В сделках** | `$49.07` / `$3.57 USDC` | До 5 открытых позиций, макс 6% банка |
| **Цель окупаемости подписки** | `$+2.64 / $60.00` (`4.4%`) | Цель: +$60.00 в месяц |
| **Просадка от пика (Текущая / Макс)** | `2.06%` / `2.43%` (Пик: `$53.75`) | Стоп-кран при просадке 40% |
| **Закрытых сделок / Win Rate** | `6` / `33.3%` | Brier Score: `N/A (ожидание экспирации)` |

## 📂 Открытые позиции (2 / 5)
| # | Рынок | Кат. | Исход | Вход (Ask VWAP) | Текущий Bid | Оценка бота | Размер ($) | Нереализ. PnL | Источник |
| :- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| #4 | Will the highest temperature in Seoul (Incheon) be 21°C | Weather | **NO** | `0.380` | `0.396` | `65.0%` | `$2.99` | `$+0.13` | METAR RKSI (Seoul Incheon) |
| #8 | Will the price of Bitcoin be above $80,000 on October 1 | Crypto | **NO** | `0.067` | `0.019` | `18.2%` | `$1.58` | `$-1.13` | https://www.binance.com/en/tra |

## 🔍 Последние проверенные кандидаты и фильтр стакана CLOB
| Рынок | Кат. | Сторона | Оценка бота | Цена Ask | Перекос (Edge) | Проскальзывание CLOB | Решение |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Will the highest temperature in Tokyo be 23°C on O | Weather | NO | `48.7%` | `0.5%` | `+48.2 п.п.` | `100.00%` | REJECTED: Insufficient Bid depth to exit position |
| Will the highest temperature in Hong Kong be 31°C  | Weather | NO | `55.2%` | `0.2%` | `+55.0 п.п.` | `100.00%` | REJECTED: Insufficient Bid depth to exit position |
| Will the highest temperature in Beijing be 21°C on | Weather | YES | `16.9%` | `100.0%` | `-83.1 п.п.` | `100.00%` | REJECTED: Edge -83.1 pp < 8 pp threshold (P_est=16.9% vs AskVWAP=100.0%) |
| Will the highest temperature in Chengdu be 28°C on | Weather | YES | `5.6%` | `100.0%` | `-94.4 п.п.` | `100.00%` | REJECTED: Edge -94.4 pp < 8 pp threshold (P_est=5.6% vs AskVWAP=100.0%) |
| Will the highest temperature in Lucknow be 32°C on | Weather | NO | `57.5%` | `25.0%` | `+32.5 п.п.` | `9.40%` | REJECTED: CLOB round-trip slippage 9.40% > 3.0% limit |
| Will Bitcoin reach $90,000 October 12-18? | Crypto | NO | `98.0%` | `93.9%` | `+4.1 п.п.` | `0.80%` | REJECTED: Edge +4.1 pp < 8 pp threshold (P_est=98.0% vs AskVWAP=93.9%) |
| Will the highest temperature in Seoul (Incheon) be | Weather | YES | `9.8%` | `100.0%` | `-90.2 п.п.` | `100.00%` | REJECTED: Edge -90.2 pp < 8 pp threshold (P_est=9.8% vs AskVWAP=100.0%) |
| Will the highest temperature in Hong Kong be 30°C  | Weather | YES | `16.9%` | `100.0%` | `-83.1 п.п.` | `100.00%` | REJECTED: Edge -83.1 pp < 8 pp threshold (P_est=16.9% vs AskVWAP=100.0%) |
| Will the highest temperature in Shanghai be 29°C o | Weather | NO | `59.2%` | `100.0%` | `-40.8 п.п.` | `100.00%` | REJECTED: Edge -40.8 pp < 8 pp threshold (P_est=59.2% vs AskVWAP=100.0%) |
| Will the highest temperature in Shanghai be 28°C o | Weather | YES | `13.9%` | `100.0%` | `-86.2 п.п.` | `100.00%` | REJECTED: Edge -86.1 pp < 8 pp threshold (P_est=13.9% vs AskVWAP=100.0%) |
| Bitcoin Up or Down on October 13? | Crypto | YES | `95.0%` | `90.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Edge +5.0 pp < 8 pp threshold (P_est=95.0% vs AskVWAP=90.0%) |
| Will the price of Bitcoin be above $84,000 on Octo | Crypto | NO | `75.3%` | `69.3%` | `+6.0 п.п.` | `1.90%` | REJECTED: Edge +6.0 pp < 8 pp threshold (P_est=75.3% vs AskVWAP=69.3%) |
| Will the highest temperature in Wellington be 18°C | Weather | YES | `17.2%` | `100.0%` | `-82.8 п.п.` | `100.00%` | REJECTED: Edge -82.8 pp < 8 pp threshold (P_est=17.2% vs AskVWAP=100.0%) |
| Will the highest temperature in Beijing be 20°C on | Weather | YES | `13.2%` | `100.0%` | `-86.8 п.п.` | `100.00%` | REJECTED: Edge -86.8 pp < 8 pp threshold (P_est=13.2% vs AskVWAP=100.0%) |
| Will the highest temperature in Shanghai be 27°C o | Weather | NO | `58.9%` | `35.0%` | `+23.9 п.п.` | `8.41%` | REJECTED: CLOB round-trip slippage 8.41% > 3.0% limit |
| Will the highest temperature in Wellington be 17°C | Weather | YES | `16.5%` | `100.0%` | `-83.5 п.п.` | `100.00%` | REJECTED: Edge -83.5 pp < 8 pp threshold (P_est=16.5% vs AskVWAP=100.0%) |
| Will the price of Bitcoin be above $84,000 on Octo | Crypto | YES | `34.0%` | `29.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Edge +5.0 pp < 8 pp threshold (P_est=34.0% vs AskVWAP=29.0%) |
| Will the price of Bitcoin be above $80,000 on Octo | Crypto | NO | `18.2%` | `6.7%` | `+11.5 п.п.` | `0.10%` | EXECUTED BUY #8 ($1.58 @ 0.0670) |
