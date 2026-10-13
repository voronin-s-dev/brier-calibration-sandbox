# 📊 Отчёт симулятора Polymarket (Устав Grok Bot — Демо-счёт)
**Обновлено:** `2026-10-13 12:22:01 UTC`

## 💰 Состояние виртуального портфеля
| Показатель | Значение | Правило устава |
| :--- | :--- | :--- |
| **Стартовый капитал** | `$50.00 USDC` | Не добавлять деньги |
| **Текущий баланс (Equity)** | **`$52.89 USDC`** (`+2.89$` / `+5.78%`) | Cash + Mark-to-Market по CLOB Bid |
| **Свободный кэш / В сделках** | `$38.86` / `$14.03 USDC` | До 8 открытых позиций, макс 8% банка |
| **Цель окупаемости подписки** | `$+2.89 / $60.00` (`4.8%`) | Цель: +$60.00 в месяц |
| **Просадка от пика (Текущая / Макс)** | `1.59%` / `2.43%` (Пик: `$53.75`) | Стоп-кран при просадке 40% |
| **Закрытых сделок / Win Rate** | `7` / `28.6%` | Brier Score: `N/A (ожидание экспирации)` |

## 📂 Открытые позиции (4 / 8)
| # | Рынок | Кат. | Исход | Вход (Ask VWAP) | Текущий Bid | Оценка бота | Размер ($) | Нереализ. PnL | Источник |
| :- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| #4 | Will the highest temperature in Seoul (Incheon) be 21°C | Weather | **NO** | `0.380` | `0.396` | `65.0%` | `$2.99` | `$+0.13` | METAR RKSI (Seoul Incheon) |
| #9 | Will Bitcoin dip to $80,000 October 12-18? | Crypto | **YES** | `0.300` | `0.300` | `38.1%` | `$3.07` | `$-0.00` | Binance BTCUSDT 1m/1h Spot Kli |
| #10 | Will the price of Bitcoin be above $84,000 on October 1 | Crypto | **YES** | `0.130` | `0.135` | `25.1%` | `$3.68` | `$+0.13` | https://www.binance.com/en/tra |
| #11 | Will the price of Ethereum be above $2,500 on October 1 | Crypto | **NO** | `0.568` | `0.540` | `60.0%` | `$4.24` | `$-0.21` | https://www.binance.com/en/tra |

## 🔍 Последние проверенные кандидаты и фильтр стакана CLOB
| Рынок | Кат. | Сторона | Оценка бота | Цена Ask | Перекос (Edge) | Проскальзывание CLOB | Решение |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Will Bitcoin reach $85,000 on October 13? | Crypto | NO | `97.0%` | `90.0%` | `+7.0 п.п.` | `3.00%` | REJECTED: Edge +7.1 pp < 8 pp threshold (P_est=97.0% vs AskVWAP=90.0%) |
| Will Bitcoin dip to $82,000 on October 13? | Crypto | NO | `77.5%` | `73.1%` | `+4.4 п.п.` | `2.13%` | REJECTED: Edge +4.4 pp < 8 pp threshold (P_est=77.5% vs AskVWAP=73.1%) |
| Will the price of Bitcoin be above $84,000 on Octo | Crypto | YES | `36.5%` | `31.0%` | `+5.5 п.п.` | `1.00%` | REJECTED: Edge +5.5 pp < 8 pp threshold (P_est=36.5% vs AskVWAP=31.0%) |
| Will the price of Bitcoin be between $80,000 and $ | Crypto | NO | `98.0%` | `93.8%` | `+4.2 п.п.` | `1.70%` | REJECTED: Edge +4.2 pp < 8 pp threshold (P_est=98.0% vs AskVWAP=93.8%) |
| Will the price of Bitcoin be above $84,000 on Octo | Crypto | YES | `41.0%` | `36.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Edge +5.0 pp < 8 pp threshold (P_est=41.0% vs AskVWAP=36.0%) |
| Capitals vs. Hurricanes | Weather | YES | `45.0%` | `40.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Edge +5.0 pp < 8 pp threshold (P_est=45.0% vs AskVWAP=40.0%) |
| Will Bitcoin dip to $76,000 October 12-18? | Crypto | YES | `11.7%` | `5.0%` | `+6.7 п.п.` | `0.40%` | REJECTED: Edge +6.7 pp < 8 pp threshold (P_est=11.7% vs AskVWAP=5.0%) |
| Bitcoin Up or Down on October 13? | Crypto | YES | `77.5%` | `73.0%` | `+4.5 п.п.` | `2.00%` | REJECTED: Edge +4.5 pp < 8 pp threshold (P_est=77.5% vs AskVWAP=73.0%) |
| Will the price of Bitcoin be above $84,000 on Octo | Crypto | YES | `35.0%` | `30.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Edge +5.0 pp < 8 pp threshold (P_est=35.0% vs AskVWAP=30.0%) |
| Will Bitcoin dip to $81,000 on October 13? | Crypto | YES | `12.7%` | `7.1%` | `+5.6 п.п.` | `1.30%` | REJECTED: Edge +5.6 pp < 8 pp threshold (P_est=12.7% vs AskVWAP=7.1%) |
| Will the price of Bitcoin be between $80,000 and $ | Crypto | NO | `98.0%` | `93.8%` | `+4.2 п.п.` | `1.70%` | REJECTED: Edge +4.2 pp < 8 pp threshold (P_est=98.0% vs AskVWAP=93.8%) |
| Will the price of Bitcoin be above $84,000 on Octo | Crypto | YES | `40.0%` | `35.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Edge +5.0 pp < 8 pp threshold (P_est=40.0% vs AskVWAP=35.0%) |
| Will the price of Ethereum be above $2,500 on Octo | Crypto | NO | `67.2%` | `56.8%` | `+10.3 п.п.` | `2.84%` | EXECUTED BUY #11 ($4.24 @ 0.5684) |
| Capitals vs. Hurricanes | Weather | YES | `45.0%` | `40.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Edge +5.0 pp < 8 pp threshold (P_est=45.0% vs AskVWAP=40.0%) |
| Bitcoin Up or Down on October 13? | Crypto | YES | `77.5%` | `73.0%` | `+4.5 п.п.` | `2.00%` | REJECTED: Edge +4.5 pp < 8 pp threshold (P_est=77.5% vs AskVWAP=73.0%) |
| Will the price of Bitcoin be above $84,000 on Octo | Crypto | YES | `25.1%` | `13.0%` | `+12.1 п.п.` | `0.20%` | EXECUTED BUY #10 ($3.68 @ 0.1300) |
| Will Bitcoin dip to $82,000 on October 13? | Crypto | YES | `32.6%` | `25.3%` | `+7.3 п.п.` | `2.27%` | REJECTED: Edge +7.3 pp < 8 pp threshold (P_est=32.6% vs AskVWAP=25.3%) |
| Will Bitcoin reach $90,000 October 12-18? | Crypto | YES | `10.2%` | `5.9%` | `+4.2 п.п.` | `0.70%` | REJECTED: Edge +4.3 pp < 8 pp threshold (P_est=10.2% vs AskVWAP=5.9%) |
