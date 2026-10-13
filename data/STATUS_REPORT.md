# 📊 Отчёт симулятора Polymarket (Устав Grok Bot — Демо-счёт)
**Обновлено:** `2026-10-13 18:20:19 UTC`

## 💰 Состояние виртуального портфеля
| Показатель | Значение | Правило устава |
| :--- | :--- | :--- |
| **Стартовый капитал** | `$50.00 USDC` | Не добавлять деньги |
| **Текущий баланс (Equity)** | **`$41.59 USDC`** (`-8.41$` / `-16.82%`) | Cash + Mark-to-Market по CLOB Bid |
| **Свободный кэш / В сделках** | `$34.43` / `$7.16 USDC` | До 8 открытых позиций, макс 8% банка |
| **Цель окупаемости подписки** | `$-8.41 / $60.00` (`0.0%`) | Цель: +$60.00 в месяц |
| **Просадка от пика (Текущая / Макс)** | `22.62%` / `22.62%` (Пик: `$53.75`) | Стоп-кран при просадке 40% |
| **Закрытых сделок / Win Rate** | `10` / `20.0%` | Brier Score: `0.3143` |

## 📂 Открытые позиции (3 / 8)
| # | Рынок | Кат. | Исход | Вход (Ask VWAP) | Текущий Bid | Оценка бота | Размер ($) | Нереализ. PnL | Источник |
| :- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| #9 | Will Bitcoin dip to $80,000 October 12-18? | Crypto | **YES** | `0.300` | `0.300` | `37.1%` | `$3.07` | `$-0.00` | Binance BTCUSDT 1m/1h Spot Kli |
| #12 | Will Bitcoin dip to $82,000 on October 13? | Crypto | **YES** | `0.130` | `0.120` | `21.7%` | `$2.10` | `$-0.16` | Binance BTCUSDT 1m/1h Spot Kli |
| #13 | Will Ethereum reach $2,700 October 12-18? | Crypto | **YES** | `0.130` | `0.120` | `22.7%` | `$2.33` | `$-0.18` | Binance ETHUSDT 1m/1h Spot Kli |

## 🔍 Последние проверенные кандидаты и фильтр стакана CLOB
| Рынок | Кат. | Сторона | Оценка бота | Цена Ask | Перекос (Edge) | Проскальзывание CLOB | Решение |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Will Ethereum reach $2,800 October 12-18? | Crypto | YES | `8.2%` | `3.5%` | `+4.7 п.п.` | `0.12%` | REJECTED: Edge +4.7 pp < 8 pp threshold (P_est=8.2% vs AskVWAP=3.5%) |
| Bitcoin Up or Down on October 14? | Crypto | YES | `46.0%` | `41.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Edge +5.0 pp < 8 pp threshold (P_est=46.0% vs AskVWAP=41.0%) |
| Will the price of Bitcoin be above $74,000 on Octo | Crypto | NO | `0.5%` | `100.0%` | `-99.5 п.п.` | `100.00%` | REJECTED: Edge -99.5 pp < 8 pp threshold (P_est=0.5% vs AskVWAP=100.0%) |
| Will the price of Bitcoin be above $92,000 on Octo | Crypto | YES | `2.0%` | `100.0%` | `-98.0 п.п.` | `100.00%` | REJECTED: Edge -98.0 pp < 8 pp threshold (P_est=2.0% vs AskVWAP=100.0%) |
| Will Ethereum reach $2,700 October 12-18? | Crypto | YES | `22.7%` | `13.0%` | `+9.7 п.п.` | `1.00%` | EXECUTED BUY #13 ($2.33 @ 0.1300) |
| Will the highest temperature in Manila be 33°C on  | Weather | NO | `72.2%` | `65.0%` | `+7.2 п.п.` | `4.00%` | REJECTED: Edge +7.2 pp < 8 pp threshold (P_est=72.2% vs AskVWAP=65.0%) |
| Will Ethereum dip to $2,450 on October 13? | Crypto | YES | `17.6%` | `9.2%` | `+8.4 п.п.` | `3.19%` | REJECTED: CLOB round-trip slippage 3.19% > 2.0% limit |
| Will the price of Bitcoin be above $82,000 on Octo | Crypto | NO | `21.1%` | `17.0%` | `+4.1 п.п.` | `1.00%` | REJECTED: Edge +4.1 pp < 8 pp threshold (P_est=21.1% vs AskVWAP=17.0%) |
| Will Bitcoin dip to $78,000 October 12-18? | Crypto | YES | `15.0%` | `11.0%` | `+4.0 п.п.` | `1.00%` | REJECTED: Edge +4.0 pp < 8 pp threshold (P_est=15.0% vs AskVWAP=11.0%) |
| Will the price of Bitcoin be above $90,000 on Octo | Crypto | YES | `2.0%` | `100.0%` | `-98.0 п.п.` | `100.00%` | REJECTED: Edge -98.0 pp < 8 pp threshold (P_est=2.0% vs AskVWAP=100.0%) |
| Will Bitcoin reach $85,000 on October 13? | Crypto | YES | `7.0%` | `2.8%` | `+4.2 п.п.` | `0.30%` | REJECTED: Edge +4.2 pp < 8 pp threshold (P_est=7.0% vs AskVWAP=2.8%) |
| Will Bitcoin dip to $82,000 on October 13? | Crypto | YES | `21.7%` | `13.0%` | `+8.7 п.п.` | `1.00%` | EXECUTED BUY #12 ($2.10 @ 0.1300) |
| Will Bitcoin reach $85,000 on October 13? | Crypto | NO | `97.0%` | `90.0%` | `+7.0 п.п.` | `3.00%` | REJECTED: Edge +7.1 pp < 8 pp threshold (P_est=97.0% vs AskVWAP=90.0%) |
| Will Bitcoin dip to $82,000 on October 13? | Crypto | NO | `77.5%` | `73.1%` | `+4.4 п.п.` | `2.13%` | REJECTED: Edge +4.4 pp < 8 pp threshold (P_est=77.5% vs AskVWAP=73.1%) |
| Will the price of Bitcoin be above $84,000 on Octo | Crypto | YES | `36.5%` | `31.0%` | `+5.5 п.п.` | `1.00%` | REJECTED: Edge +5.5 pp < 8 pp threshold (P_est=36.5% vs AskVWAP=31.0%) |
| Will the price of Bitcoin be between $80,000 and $ | Crypto | NO | `98.0%` | `93.8%` | `+4.2 п.п.` | `1.70%` | REJECTED: Edge +4.2 pp < 8 pp threshold (P_est=98.0% vs AskVWAP=93.8%) |
| Will the price of Bitcoin be above $84,000 on Octo | Crypto | YES | `41.0%` | `36.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Edge +5.0 pp < 8 pp threshold (P_est=41.0% vs AskVWAP=36.0%) |
| Capitals vs. Hurricanes | Weather | YES | `45.0%` | `40.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Edge +5.0 pp < 8 pp threshold (P_est=45.0% vs AskVWAP=40.0%) |
