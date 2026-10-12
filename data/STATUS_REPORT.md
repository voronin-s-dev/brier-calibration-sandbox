# 📊 Отчёт симулятора Polymarket (Устав Grok Bot — Демо-счёт)
**Обновлено:** `2026-10-12 21:05:36 UTC`

## 💰 Состояние виртуального портфеля
| Показатель | Значение | Правило устава |
| :--- | :--- | :--- |
| **Стартовый капитал** | `$50.00 USDC` | Не добавлять деньги |
| **Текущий баланс (Equity)** | **`$49.35 USDC`** (`-0.65$` / `-1.30%`) | Cash + Mark-to-Market по CLOB Bid |
| **Свободный кэш / В сделках** | `$37.84` / `$11.51 USDC` | До 5 открытых позиций, макс 6% банка |
| **Цель окупаемости подписки** | `$-0.65 / $60.00` (`0.0%`) | Цель: +$60.00 в месяц |
| **Просадка от пика (Текущая / Макс)** | `1.30%` / `1.30%` (Пик: `$50.00`) | Стоп-кран при просадке 40% |
| **Закрытых сделок / Win Rate** | `1` / `0.0%` | Brier Score: `N/A (ожидание экспирации)` |

## 📂 Открытые позиции (4 / 5)
| # | Рынок | Кат. | Исход | Вход (Ask VWAP) | Текущий Bid | Оценка бота | Размер ($) | Нереализ. PnL | Источник |
| :- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| #2 | Will the highest temperature in Shanghai be 26°C on Oct | Weather | **NO** | `0.650` | `0.630` | `89.6%` | `$3.00` | `$-0.09` | METAR ZSPD (Shanghai Pudong) |
| #3 | Will the highest temperature in Sao Paulo be 26°C on Oc | Weather | **NO** | `0.810` | `0.790` | `98.4%` | `$2.99` | `$-0.07` | METAR SBGR (Sao Paulo Guarulho |
| #4 | Will the highest temperature in Seoul (Incheon) be 21°C | Weather | **NO** | `0.380` | `0.360` | `65.6%` | `$2.99` | `$-0.16` | METAR RKSI (Seoul Incheon) |
| #5 | Will the highest temperature in Mexico City be 26°C or  | Weather | **NO** | `0.492` | `0.470` | `99.5%` | `$2.99` | `$-0.13` | METAR MMMX (Mexico City Intl) |

## 🔍 Последние проверенные кандидаты и фильтр стакана CLOB
| Рынок | Кат. | Сторона | Оценка бота | Цена Ask | Перекос (Edge) | Проскальзывание CLOB | Решение |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Will the highest temperature in Lucknow be 33°C on | Weather | NO | `99.5%` | `93.0%` | `+6.5 п.п.` | `8.00%` | REJECTED: Edge +6.5 pp < 8 pp threshold (P_est=99.5% vs AskVWAP=93.0%) |
| Will the highest temperature in Shenzhen be 31°C o | Weather | NO | `99.5%` | `77.0%` | `+22.5 п.п.` | `6.00%` | REJECTED: CLOB round-trip slippage 6.00% > 3.0% limit |
| Will the highest temperature in Shanghai be 27°C o | Weather | YES | `59.9%` | `54.2%` | `+5.7 п.п.` | `2.21%` | REJECTED: Edge +5.7 pp < 8 pp threshold (P_est=59.9% vs AskVWAP=54.2%) |
| Will the price of Bitcoin be above $84,000 on Octo | Crypto | YES | `33.0%` | `28.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Edge +5.0 pp < 8 pp threshold (P_est=33.0% vs AskVWAP=28.0%) |
| Will the highest temperature in Seoul (Incheon) be | Weather | YES | `1.6%` | `100.0%` | `-98.4 п.п.` | `100.00%` | REJECTED: Edge -98.4 pp < 8 pp threshold (P_est=1.6% vs AskVWAP=100.0%) |
| Will the price of Bitcoin be above $84,000 on Octo | Crypto | YES | `21.0%` | `16.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Edge +5.0 pp < 8 pp threshold (P_est=21.0% vs AskVWAP=16.0%) |
| Will Bitcoin reach $88,000 on October 12? | Crypto | YES | `0.5%` | `100.0%` | `-99.5 п.п.` | `100.00%` | REJECTED: Edge -99.5 pp < 8 pp threshold (P_est=0.5% vs AskVWAP=100.0%) |
| Will the highest temperature in Tokyo be 25°C on O | Weather | NO | `97.5%` | `62.0%` | `+35.5 п.п.` | `6.00%` | REJECTED: CLOB round-trip slippage 6.00% > 3.0% limit |
| Will the highest temperature in Lucknow be 33°C on | Weather | NO | `99.5%` | `93.0%` | `+6.5 п.п.` | `8.00%` | REJECTED: Edge +6.5 pp < 8 pp threshold (P_est=99.5% vs AskVWAP=93.0%) |
| Will the highest temperature in Shenzhen be 31°C o | Weather | NO | `99.5%` | `77.0%` | `+22.5 п.п.` | `6.00%` | REJECTED: CLOB round-trip slippage 6.00% > 3.0% limit |
| Will Bitcoin reach $87,000 on October 12? | Crypto | YES | `0.5%` | `100.0%` | `-99.5 п.п.` | `100.00%` | REJECTED: Edge -99.5 pp < 8 pp threshold (P_est=0.5% vs AskVWAP=100.0%) |
| Will the highest temperature in Shanghai be 27°C o | Weather | YES | `59.8%` | `54.2%` | `+5.6 п.п.` | `1.17%` | REJECTED: Edge +5.6 pp < 8 pp threshold (P_est=59.8% vs AskVWAP=54.2%) |
| Will Ethereum reach $2,700 on October 12? | Crypto | YES | `0.5%` | `100.0%` | `-99.5 п.п.` | `100.00%` | REJECTED: Edge -99.5 pp < 8 pp threshold (P_est=0.5% vs AskVWAP=100.0%) |
| Will Ethereum reach $2,750 on October 12? | Crypto | YES | `0.5%` | `100.0%` | `-99.5 п.п.` | `100.00%` | REJECTED: Edge -99.5 pp < 8 pp threshold (P_est=0.5% vs AskVWAP=100.0%) |
| Will the highest temperature in Seoul (Incheon) be | Weather | YES | `1.6%` | `100.0%` | `-98.4 п.п.` | `100.00%` | REJECTED: Edge -98.4 pp < 8 pp threshold (P_est=1.6% vs AskVWAP=100.0%) |
| Will the price of Bitcoin be above $84,000 on Octo | Crypto | YES | `23.1%` | `16.0%` | `+7.1 п.п.` | `1.00%` | REJECTED: Edge +7.1 pp < 8 pp threshold (P_est=23.1% vs AskVWAP=16.0%) |
| Will the price of Bitcoin be above $76,000 on Octo | Crypto | NO | `0.5%` | `100.0%` | `-99.5 п.п.` | `100.00%` | REJECTED: Edge -99.5 pp < 8 pp threshold (P_est=0.5% vs AskVWAP=100.0%) |
| Will Bitcoin dip to $82,000 on October 12? | Crypto | YES | `12.9%` | `8.0%` | `+4.9 п.п.` | `1.00%` | REJECTED: Edge +4.9 pp < 8 pp threshold (P_est=12.9% vs AskVWAP=8.0%) |
