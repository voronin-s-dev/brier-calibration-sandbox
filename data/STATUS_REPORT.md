# 📊 Отчёт симулятора Polymarket (Устав Grok Bot — Демо-счёт)
**Обновлено:** `2026-10-16 18:58:00 UTC`

## 💰 Состояние виртуального портфеля
| Показатель | Значение | Правило устава |
| :--- | :--- | :--- |
| **Стартовый капитал** | `$50.00 USDC` | Не добавлять деньги |
| **Текущий баланс (Equity)** | **`$32.62 USDC`** (`-17.38$` / `-34.76%`) | Cash + Mark-to-Market по CLOB Bid |
| **Свободный кэш / В сделках** | `$31.24` / `$1.39 USDC` | До 8 открытых позиций, макс 8% банка |
| **Цель окупаемости подписки** | `$-17.38 / $60.00` (`0.0%`) | Цель: +$60.00 в месяц |
| **Просадка от пика (Текущая / Макс)** | `39.31%` / `39.57%` (Пик: `$53.75`) | Стоп-кран при просадке 40% |
| **Закрытых сделок / Win Rate** | `29` / `27.6%` | Brier Score: `0.3143` |

## 📂 Открытые позиции (1 / 8)
| # | Рынок | Кат. | Исход | Вход (Ask VWAP) | Текущий Bid | Оценка бота | Размер ($) | Нереализ. PnL | Источник |
| :- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| #26 | Will the highest temperature in Seoul (Incheon) be 25°C | Weather | **NO** | `0.570` | `0.590` | `82.3%` | `$1.34` | `$+0.05` | METAR RKSI (Seoul Incheon) |

## 🔍 Последние проверенные кандидаты и фильтр стакана CLOB
| Рынок | Кат. | Сторона | Оценка бота | Цена Ask | Перекос (Edge) | Проскальзывание CLOB | Решение |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Will the price of Bitcoin be above $88,000 on Octo | Crypto | YES | `2.0%` | `100.0%` | `-98.0 п.п.` | `100.00%` | REJECTED: Edge -98.0 pp < 8 pp threshold (P_est=2.0% vs AskVWAP=100.0%) |
| Will the price of Bitcoin be between $80,000 and $ | Crypto | NO | `63.7%` | `40.0%` | `+23.7 п.п.` | `3.00%` | REJECTED: CLOB round-trip slippage 3.00% > 2.0% limit |
| Will the price of Bitcoin be above $88,000 on Octo | Crypto | YES | `7.7%` | `3.2%` | `+4.5 п.п.` | `2.08%` | REJECTED: Edge +4.5 pp < 8 pp threshold (P_est=7.7% vs AskVWAP=3.2%) |
| Will Bitcoin dip to $80,000 October 12-18? | Crypto | YES | `70.6%` | `49.0%` | `+21.6 п.п.` | `3.00%` | REJECTED: CLOB round-trip slippage 3.00% > 2.0% limit |
| Will the price of Bitcoin be above $80,000 on Octo | Crypto | NO | `39.6%` | `33.0%` | `+6.6 п.п.` | `2.00%` | REJECTED: Edge +6.6 pp < 8 pp threshold (P_est=39.6% vs AskVWAP=33.0%) |
| Will the price of Bitcoin be above $78,000 on Octo | Crypto | NO | `12.3%` | `2.6%` | `+9.8 п.п.` | `0.78%` | REJECTED: Win probability 12.3% < 55% minimum (no underdog lottery bets) |
| Will the price of Ethereum be above $2,500 on Octo | Crypto | YES | `6.6%` | `2.0%` | `+4.6 п.п.` | `1.46%` | REJECTED: Edge +4.6 pp < 8 pp threshold (P_est=6.6% vs AskVWAP=2.0%) |
| Will the price of Bitcoin be above $90,000 on Octo | Crypto | YES | `2.0%` | `100.0%` | `-98.0 п.п.` | `100.00%` | REJECTED: Edge -98.0 pp < 8 pp threshold (P_est=2.0% vs AskVWAP=100.0%) |
| Will the price of Bitcoin be above $74,000 on Octo | Crypto | NO | `7.3%` | `3.3%` | `+4.0 п.п.` | `1.89%` | REJECTED: Edge +4.0 pp < 8 pp threshold (P_est=7.3% vs AskVWAP=3.3%) |
| Will the price of Ethereum be above $2,300 on Octo | Crypto | NO | `7.0%` | `2.9%` | `+4.0 п.п.` | `0.75%` | REJECTED: Edge +4.0 pp < 8 pp threshold (P_est=7.0% vs AskVWAP=2.9%) |
| Will the price of Bitcoin be between $80,000 and $ | Crypto | NO | `50.5%` | `23.0%` | `+27.5 п.п.` | `2.00%` | REJECTED: Win probability 50.5% < 55% minimum (no underdog lottery bets) |
| Will the price of Bitcoin be above $80,000 on Octo | Crypto | NO | `36.5%` | `29.0%` | `+7.5 п.п.` | `2.00%` | REJECTED: Edge +7.5 pp < 8 pp threshold (P_est=36.5% vs AskVWAP=29.0%) |
| Will Bitcoin reach $84,000 October 12-18? | Crypto | YES | `28.3%` | `6.0%` | `+22.3 п.п.` | `1.00%` | REJECTED: Win probability 28.3% < 55% minimum (no underdog lottery bets) |
| Will the price of Bitcoin be between $78,000 and $ | Crypto | YES | `20.4%` | `12.3%` | `+8.1 п.п.` | `1.60%` | REJECTED: Win probability 20.4% < 55% minimum (no underdog lottery bets) |
| Will Bitcoin reach $86,000 October 12-18? | Crypto | YES | `11.2%` | `1.0%` | `+10.2 п.п.` | `0.53%` | REJECTED: Win probability 11.2% < 55% minimum (no underdog lottery bets) |
| Will the price of Bitcoin be between $82,000 and $ | Crypto | YES | `18.8%` | `13.0%` | `+5.8 п.п.` | `3.00%` | REJECTED: Edge +5.8 pp < 8 pp threshold (P_est=18.8% vs AskVWAP=13.0%) |
| Will the price of Bitcoin be above $84,000 on Octo | Crypto | YES | `23.0%` | `19.0%` | `+4.0 п.п.` | `4.00%` | REJECTED: Edge +4.0 pp < 8 pp threshold (P_est=23.0% vs AskVWAP=19.0%) |
| Will Bitcoin dip to $76,000 October 12-18? | Crypto | YES | `10.1%` | `2.0%` | `+8.1 п.п.` | `0.10%` | REJECTED: Win probability 10.1% < 55% minimum (no underdog lottery bets) |
