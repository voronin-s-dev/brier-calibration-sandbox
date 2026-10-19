# 📊 Отчёт симулятора Polymarket (Устав Grok Bot — Демо-счёт)
**Обновлено:** `2026-10-19 22:34:37 UTC`

## 💰 Состояние виртуального портфеля
| Показатель | Значение | Правило устава |
| :--- | :--- | :--- |
| **Стартовый капитал** | `$50.00 USDC` | Не добавлять деньги |
| **Текущий баланс (Equity)** | **`$27.71 USDC`** (`-22.29$` / `-44.59%`) | Cash + Mark-to-Market по CLOB Bid |
| **Свободный кэш / В сделках** | `$26.54` / `$1.16 USDC` | До 8 открытых позиций, макс 8% банка |
| **Цель окупаемости подписки** | `$-22.29 / $60.00` (`0.0%`) | Цель: +$60.00 в месяц |
| **Просадка от пика (Текущая / Макс)** | `1.22%` / `1.48%` (Пик: `$28.05`) | Стоп-кран при просадке 40% |
| **Закрытых сделок / Win Rate** | `34` / `23.5%` | Brier Score: `0.4280` |

## 📂 Открытые позиции (1 / 8)
| # | Рынок | Кат. | Исход | Вход (Ask VWAP) | Текущий Bid | Оценка бота | Размер ($) | Нереализ. PnL | Источник |
| :- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| #35 | Will Bitcoin dip to $80,000 in October? | Crypto | **YES** | `0.610` | `0.640` | `74.6%` | `$1.11` | `$+0.05` | Kraken BTCUSDT 1m/1h Spot Klin |

## 🔍 Последние проверенные кандидаты и фильтр стакана CLOB
| Рынок | Кат. | Сторона | Оценка бота | Цена Ask | Перекос (Edge) | Проскальзывание CLOB | Решение |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Will the price of Bitcoin be between $78,000 and $ | Crypto | YES | `9.4%` | `3.0%` | `+6.4 п.п.` | `0.30%` | REJECTED: Edge +6.4 pp < 8 pp threshold (P_est=9.4% vs AskVWAP=3.0%) |
| Will the price of Bitcoin be above $86,000 on Octo | Crypto | YES | `7.3%` | `2.2%` | `+5.1 п.п.` | `0.28%` | REJECTED: Edge +5.1 pp < 8 pp threshold (P_est=7.3% vs AskVWAP=2.2%) |
| Will the price of Bitcoin be above $76,000 on Octo | Crypto | NO | `10.0%` | `4.8%` | `+5.2 п.п.` | `2.10%` | REJECTED: Edge +5.2 pp < 8 pp threshold (P_est=10.0% vs AskVWAP=4.8%) |
| Will the price of Bitcoin be above $80,000 on Octo | Crypto | NO | `20.2%` | `11.0%` | `+9.2 п.п.` | `1.12%` | REJECTED: Win probability 20.2% < 55% minimum (no underdog lottery bets) |
| Will Solana dip to $100 in October? | Crypto | YES | `68.5%` | `64.0%` | `+4.5 п.п.` | `4.00%` | REJECTED: Edge +4.5 pp < 8 pp threshold (P_est=68.5% vs AskVWAP=64.0%) |
| Will the highest temperature in Wuhan be 16°C on O | Weather | YES | `2.0%` | `100.0%` | `-98.0 п.п.` | `100.00%` | REJECTED: Edge -98.0 pp < 8 pp threshold (P_est=2.0% vs AskVWAP=100.0%) |
| Will the price of Bitcoin be above $92,000 on Octo | Crypto | YES | `2.0%` | `100.0%` | `-98.0 п.п.` | `100.00%` | REJECTED: Edge -98.0 pp < 8 pp threshold (P_est=2.0% vs AskVWAP=100.0%) |
| Will Bitcoin reach $92,500 in October? | Crypto | YES | `16.9%` | `7.0%` | `+9.9 п.п.` | `1.00%` | REJECTED: Win probability 16.9% < 55% minimum (no underdog lottery bets) |
| Will the price of Ethereum be above $2,500 on Octo | Crypto | YES | `7.7%` | `3.7%` | `+4.0 п.п.` | `0.50%` | REJECTED: Edge +4.0 pp < 8 pp threshold (P_est=7.7% vs AskVWAP=3.7%) |
| Will Bitcoin dip to $77,500 in October? | Crypto | YES | `48.8%` | `35.0%` | `+13.8 п.п.` | `1.00%` | REJECTED: Win probability 48.8% < 55% minimum (no underdog lottery bets) |
| Will the price of Bitcoin be above $74,000 on Octo | Crypto | NO | `0.5%` | `100.0%` | `-99.5 п.п.` | `100.00%` | REJECTED: Edge -99.5 pp < 8 pp threshold (P_est=0.5% vs AskVWAP=100.0%) |
| Will the price of Bitcoin be above $78,000 on Octo | Crypto | NO | `6.3%` | `1.5%` | `+4.8 п.п.` | `0.48%` | REJECTED: Edge +4.8 pp < 8 pp threshold (P_est=6.3% vs AskVWAP=1.5%) |
| Will the price of Ethereum be above $2,500 on Octo | Crypto | YES | `16.6%` | `12.0%` | `+4.6 п.п.` | `2.00%` | REJECTED: Edge +4.6 pp < 8 pp threshold (P_est=16.6% vs AskVWAP=12.0%) |
| Will the price of Bitcoin be above $88,000 on Octo | Crypto | YES | `2.0%` | `100.0%` | `-98.0 п.п.` | `100.00%` | REJECTED: Edge -98.0 pp < 8 pp threshold (P_est=2.0% vs AskVWAP=100.0%) |
| Will Bitcoin reach $95,000 in October? | Crypto | YES | `9.9%` | `3.4%` | `+6.5 п.п.` | `0.20%` | REJECTED: Edge +6.5 pp < 8 pp threshold (P_est=9.9% vs AskVWAP=3.4%) |
| Will Bitcoin dip to $75,000 in October? | Crypto | YES | `29.5%` | `18.0%` | `+11.5 п.п.` | `1.00%` | REJECTED: Win probability 29.5% < 55% minimum (no underdog lottery bets) |
| Will the price of Bitcoin be above $84,000 on Octo | Crypto | YES | `12.8%` | `6.0%` | `+6.8 п.п.` | `1.00%` | REJECTED: Edge +6.8 pp < 8 pp threshold (P_est=12.8% vs AskVWAP=6.0%) |
| Will Bitcoin reach $90,000 in October? | Crypto | YES | `28.8%` | `17.0%` | `+11.8 п.п.` | `1.00%` | REJECTED: Win probability 28.8% < 55% minimum (no underdog lottery bets) |
