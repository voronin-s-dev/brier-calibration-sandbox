# 📊 Отчёт симулятора Polymarket (Устав Grok Bot — Демо-счёт)
**Обновлено:** `2026-10-17 18:57:00 UTC`

## 💰 Состояние виртуального портфеля
| Показатель | Значение | Правило устава |
| :--- | :--- | :--- |
| **Стартовый капитал** | `$50.00 USDC` | Не добавлять деньги |
| **Текущий баланс (Equity)** | **`$31.87 USDC`** (`-18.13$` / `-36.26%`) | Cash + Mark-to-Market по CLOB Bid |
| **Свободный кэш / В сделках** | `$28.03` / `$3.85 USDC` | До 8 открытых позиций, макс 8% банка |
| **Цель окупаемости подписки** | `$-18.13 / $60.00` (`0.0%`) | Цель: +$60.00 в месяц |
| **Просадка от пика (Текущая / Макс)** | `40.70%` / `40.70%` (Пик: `$53.75`) | Стоп-кран при просадке 40% |
| **Закрытых сделок / Win Rate** | `30` / `26.7%` | Brier Score: `0.3143` |

## 📂 Открытые позиции (3 / 8)
| # | Рынок | Кат. | Исход | Вход (Ask VWAP) | Текущий Bid | Оценка бота | Размер ($) | Нереализ. PnL | Источник |
| :- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| #26 | Will the highest temperature in Seoul (Incheon) be 25°C | Weather | **NO** | `0.570` | `0.580` | `82.4%` | `$1.34` | `$+0.02` | METAR RKSI (Seoul Incheon) |
| #32 | Will the price of Bitcoin be between $80,000 and $82,00 | Crypto | **NO** | `0.460` | `0.450` | `65.2%` | `$1.28` | `$-0.03` | Kraken BTCUSDT 1m/1h Spot Klin |
| #33 | Will the highest temperature in Amsterdam be 14°C on Oc | Weather | **NO** | `0.520` | `0.500` | `72.4%` | `$1.28` | `$-0.05` | Auto-Meteo Amsterdam (NL) |

## 🔍 Последние проверенные кандидаты и фильтр стакана CLOB
| Рынок | Кат. | Сторона | Оценка бота | Цена Ask | Перекос (Edge) | Проскальзывание CLOB | Решение |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Will the price of Bitcoin be above $88,000 on Octo | Crypto | YES | `2.0%` | `100.0%` | `-98.0 п.п.` | `100.00%` | REJECTED: Edge -98.0 pp < 8 pp threshold (P_est=2.0% vs AskVWAP=100.0%) |
| Will the highest temperature in Amsterdam be 14°C  | Weather | NO | `72.4%` | `52.0%` | `+20.4 п.п.` | `2.00%` | EXECUTED BUY #33 ($1.28 @ 0.5200) |
| Will the price of Bitcoin be above $84,000 on Octo | Crypto | YES | `15.2%` | `2.8%` | `+12.4 п.п.` | `0.23%` | REJECTED: Win probability 15.2% < 55% minimum (no underdog lottery bets) |
| Will the price of Bitcoin be between $78,000 and $ | Crypto | YES | `14.8%` | `5.7%` | `+9.1 п.п.` | `1.30%` | REJECTED: Win probability 14.8% < 55% minimum (no underdog lottery bets) |
| Will the price of Ethereum be above $2,400 on Octo | Crypto | NO | `41.9%` | `34.3%` | `+7.6 п.п.` | `1.80%` | REJECTED: Edge +7.6 pp < 8 pp threshold (P_est=41.9% vs AskVWAP=34.3%) |
| Will the price of Bitcoin be between $80,000 and $ | Crypto | NO | `65.2%` | `46.0%` | `+19.2 п.п.` | `1.00%` | EXECUTED BUY #32 ($1.28 @ 0.4600) |
| Will the price of Bitcoin be above $86,000 on Octo | Crypto | YES | `5.5%` | `1.1%` | `+4.5 п.п.` | `0.10%` | REJECTED: Edge +4.5 pp < 8 pp threshold (P_est=5.5% vs AskVWAP=1.1%) |
| Will the price of Bitcoin be above $88,000 on Octo | Crypto | YES | `9.3%` | `4.3%` | `+5.0 п.п.` | `2.31%` | REJECTED: Edge +5.0 pp < 8 pp threshold (P_est=9.3% vs AskVWAP=4.3%) |
| Will Bitcoin dip to $80,000 October 12-18? | Crypto | YES | `51.8%` | `26.0%` | `+25.9 п.п.` | `2.00%` | REJECTED: Win probability 51.8% < 55% minimum (no underdog lottery bets) |
| Will the price of Ethereum be above $2,400 on Octo | Crypto | NO | `44.6%` | `40.0%` | `+4.6 п.п.` | `2.00%` | REJECTED: Edge +4.6 pp < 8 pp threshold (P_est=44.6% vs AskVWAP=40.0%) |
| Will the price of Ethereum be above $2,500 on Octo | Crypto | YES | `8.0%` | `1.6%` | `+6.4 п.п.` | `0.19%` | REJECTED: Edge +6.4 pp < 8 pp threshold (P_est=8.0% vs AskVWAP=1.6%) |
| Will the price of Bitcoin be above $90,000 on Octo | Crypto | YES | `2.0%` | `100.0%` | `-98.0 п.п.` | `100.00%` | REJECTED: Edge -98.0 pp < 8 pp threshold (P_est=2.0% vs AskVWAP=100.0%) |
| Will the price of Bitcoin be above $80,000 on Octo | Crypto | NO | `32.7%` | `25.0%` | `+7.7 п.п.` | `3.00%` | REJECTED: Edge +7.7 pp < 8 pp threshold (P_est=32.7% vs AskVWAP=25.0%) |
| Will the price of Bitcoin be between $80,000 and $ | Crypto | NO | `52.6%` | `32.0%` | `+20.6 п.п.` | `1.00%` | REJECTED: Win probability 52.6% < 55% minimum (no underdog lottery bets) |
| Will the price of Bitcoin be above $80,000 on Octo | Crypto | NO | `29.1%` | `18.0%` | `+11.2 п.п.` | `1.00%` | REJECTED: Win probability 29.1% < 55% minimum (no underdog lottery bets) |
| Will the price of Bitcoin be above $78,000 on Octo | Crypto | NO | `8.4%` | `1.5%` | `+6.9 п.п.` | `0.10%` | REJECTED: Edge +6.9 pp < 8 pp threshold (P_est=8.4% vs AskVWAP=1.5%) |
| Will Bitcoin reach $86,000 October 12-18? | Crypto | YES | `14.6%` | `1.3%` | `+13.3 п.п.` | `0.40%` | REJECTED: Win probability 14.6% < 55% minimum (no underdog lottery bets) |
| Will Bitcoin reach $84,000 October 12-18? | Crypto | YES | `37.1%` | `13.0%` | `+24.1 п.п.` | `2.00%` | REJECTED: Win probability 37.1% < 55% minimum (no underdog lottery bets) |
