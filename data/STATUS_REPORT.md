# 📊 Отчёт симулятора Polymarket (Устав Grok Bot — Демо-счёт)
**Обновлено:** `2026-10-16 19:07:12 UTC`

## 💰 Состояние виртуального портфеля
| Показатель | Значение | Правило устава |
| :--- | :--- | :--- |
| **Стартовый капитал** | `$50.00 USDC` | Не добавлять деньги |
| **Текущий баланс (Equity)** | **`$32.60 USDC`** (`-17.40$` / `-34.81%`) | Cash + Mark-to-Market по CLOB Bid |
| **Свободный кэш / В сделках** | `$29.94` / `$2.66 USDC` | До 8 открытых позиций, макс 8% банка |
| **Цель окупаемости подписки** | `$-17.40 / $60.00` (`0.0%`) | Цель: +$60.00 в месяц |
| **Просадка от пика (Текущая / Макс)** | `39.36%` / `39.57%` (Пик: `$53.75`) | Стоп-кран при просадке 40% |
| **Закрытых сделок / Win Rate** | `29` / `27.6%` | Brier Score: `0.3143` |

## 📂 Открытые позиции (2 / 8)
| # | Рынок | Кат. | Исход | Вход (Ask VWAP) | Текущий Bid | Оценка бота | Размер ($) | Нереализ. PnL | Источник |
| :- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| #26 | Will the highest temperature in Seoul (Incheon) be 25°C | Weather | **NO** | `0.570` | `0.590` | `82.3%` | `$1.34` | `$+0.05` | METAR RKSI (Seoul Incheon) |
| #31 | Will Bitcoin dip to $80,000 October 12-18? | Crypto | **YES** | `0.480` | `0.470` | `68.4%` | `$1.30` | `$-0.03` | Kraken BTCUSDT 1m/1h Spot Klin |

## 🔍 Последние проверенные кандидаты и фильтр стакана CLOB
| Рынок | Кат. | Сторона | Оценка бота | Цена Ask | Перекос (Edge) | Проскальзывание CLOB | Решение |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Will the price of Bitcoin be above $88,000 on Octo | Crypto | YES | `2.0%` | `100.0%` | `-98.0 п.п.` | `100.00%` | REJECTED: Edge -98.0 pp < 8 pp threshold (P_est=2.0% vs AskVWAP=100.0%) |
| Will the highest temperature in Amsterdam be 14°C  | Weather | NO | `70.7%` | `47.0%` | `+23.7 п.п.` | `3.00%` | REJECTED: CLOB round-trip slippage 3.00% > 2.0% limit |
| Will the price of Bitcoin be between $80,000 and $ | Crypto | NO | `63.7%` | `41.0%` | `+22.7 п.п.` | `8.00%` | REJECTED: CLOB round-trip slippage 8.00% > 2.0% limit |
| Will the price of Bitcoin be above $88,000 on Octo | Crypto | YES | `7.6%` | `2.9%` | `+4.8 п.п.` | `2.02%` | REJECTED: Edge +4.7 pp < 8 pp threshold (P_est=7.6% vs AskVWAP=2.9%) |
| Will Bitcoin dip to $80,000 October 12-18? | Crypto | YES | `68.4%` | `48.0%` | `+20.4 п.п.` | `1.00%` | EXECUTED BUY #31 ($1.30 @ 0.4800) |
| Will the price of Bitcoin be above $80,000 on Octo | Crypto | NO | `39.0%` | `32.0%` | `+7.0 п.п.` | `2.00%` | REJECTED: Edge +7.0 pp < 8 pp threshold (P_est=39.0% vs AskVWAP=32.0%) |
| Will the price of Bitcoin be above $78,000 on Octo | Crypto | NO | `12.3%` | `2.6%` | `+9.7 п.п.` | `0.92%` | REJECTED: Win probability 12.3% < 55% minimum (no underdog lottery bets) |
| Will the price of Ethereum be above $2,500 on Octo | Crypto | YES | `6.6%` | `2.2%` | `+4.3 п.п.` | `1.20%` | REJECTED: Edge +4.4 pp < 8 pp threshold (P_est=6.6% vs AskVWAP=2.2%) |
| Will the price of Bitcoin be above $90,000 on Octo | Crypto | YES | `2.0%` | `100.0%` | `-98.0 п.п.` | `100.00%` | REJECTED: Edge -98.0 pp < 8 pp threshold (P_est=2.0% vs AskVWAP=100.0%) |
| Will the price of Ethereum be above $2,300 on Octo | Crypto | NO | `7.0%` | `2.6%` | `+4.4 п.п.` | `0.60%` | REJECTED: Edge +4.4 pp < 8 pp threshold (P_est=7.0% vs AskVWAP=2.6%) |
| Will the price of Bitcoin be between $80,000 and $ | Crypto | NO | `50.8%` | `25.0%` | `+25.8 п.п.` | `4.00%` | REJECTED: Win probability 50.8% < 55% minimum (no underdog lottery bets) |
| Will the price of Bitcoin be above $80,000 on Octo | Crypto | NO | `36.6%` | `28.0%` | `+8.6 п.п.` | `2.00%` | REJECTED: Win probability 36.6% < 55% minimum (no underdog lottery bets) |
| Will Bitcoin reach $84,000 October 12-18? | Crypto | YES | `28.5%` | `7.0%` | `+21.6 п.п.` | `2.00%` | REJECTED: Win probability 28.5% < 55% minimum (no underdog lottery bets) |
| Will the price of Bitcoin be between $78,000 and $ | Crypto | YES | `20.6%` | `10.7%` | `+9.9 п.п.` | `2.40%` | REJECTED: Win probability 20.6% < 55% minimum (no underdog lottery bets) |
| Will Bitcoin reach $86,000 October 12-18? | Crypto | YES | `11.2%` | `1.2%` | `+10.0 п.п.` | `0.73%` | REJECTED: Win probability 11.2% < 55% minimum (no underdog lottery bets) |
| Will the price of Bitcoin be between $82,000 and $ | Crypto | YES | `20.4%` | `13.0%` | `+7.4 п.п.` | `2.00%` | REJECTED: Edge +7.4 pp < 8 pp threshold (P_est=20.4% vs AskVWAP=13.0%) |
| Will the price of Bitcoin be above $84,000 on Octo | Crypto | YES | `23.5%` | `18.0%` | `+5.5 п.п.` | `3.00%` | REJECTED: Edge +5.5 pp < 8 pp threshold (P_est=23.5% vs AskVWAP=18.0%) |
| Will Bitcoin dip to $76,000 October 12-18? | Crypto | YES | `10.1%` | `2.0%` | `+8.1 п.п.` | `0.10%` | REJECTED: Win probability 10.1% < 55% minimum (no underdog lottery bets) |
