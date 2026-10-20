# 📊 Отчёт симулятора Polymarket (Устав Grok Bot — Демо-счёт)
**Обновлено:** `2026-10-20 01:21:22 UTC`

## 💰 Состояние виртуального портфеля
| Показатель | Значение | Правило устава |
| :--- | :--- | :--- |
| **Стартовый капитал** | `$50.00 USDC` | Не добавлять деньги |
| **Текущий баланс (Equity)** | **`$27.87 USDC`** (`-22.13$` / `-44.26%`) | Cash + Mark-to-Market по CLOB Bid |
| **Свободный кэш / В сделках** | `$26.54` / `$1.33 USDC` | До 8 открытых позиций, макс 8% банка |
| **Цель окупаемости подписки** | `$-22.13 / $60.00` (`0.0%`) | Цель: +$60.00 в месяц |
| **Просадка от пика (Текущая / Макс)** | `0.64%` / `1.48%` (Пик: `$28.05`) | Стоп-кран при просадке 40% |
| **Закрытых сделок / Win Rate** | `34` / `23.5%` | Brier Score: `0.4280` |

## 📂 Открытые позиции (1 / 8)
| # | Рынок | Кат. | Исход | Вход (Ask VWAP) | Текущий Bid | Оценка бота | Размер ($) | Нереализ. PnL | Источник |
| :- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| #35 | Will Bitcoin dip to $80,000 in October? | Crypto | **YES** | `0.610` | `0.730` | `84.5%` | `$1.11` | `$+0.22` | Kraken BTCUSDT 1m/1h Spot Klin |

## 🔍 Последние проверенные кандидаты и фильтр стакана CLOB
| Рынок | Кат. | Сторона | Оценка бота | Цена Ask | Перекос (Edge) | Проскальзывание CLOB | Решение |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Will Bitcoin dip to $76,000 October 19-25? | Crypto | YES | `27.6%` | `15.0%` | `+12.6 п.п.` | `1.40%` | REJECTED: Win probability 27.6% < 55% minimum (no underdog lottery bets) |
| Will the price of Bitcoin be between $78,000 and $ | Crypto | YES | `18.2%` | `9.2%` | `+9.0 п.п.` | `1.00%` | REJECTED: Win probability 18.2% < 55% minimum (no underdog lottery bets) |
| Will the price of Bitcoin be above $76,000 on Octo | Crypto | NO | `13.4%` | `7.4%` | `+5.9 п.п.` | `2.68%` | REJECTED: Edge +5.9 pp < 8 pp threshold (P_est=13.4% vs AskVWAP=7.4%) |
| Will Solana dip to $100 in October? | Crypto | YES | `76.4%` | `70.0%` | `+6.4 п.п.` | `4.00%` | REJECTED: Edge +6.4 pp < 8 pp threshold (P_est=76.4% vs AskVWAP=70.0%) |
| Will the price of Bitcoin be above $80,000 on Octo | Crypto | NO | `30.6%` | `20.0%` | `+10.6 п.п.` | `1.00%` | REJECTED: Win probability 30.6% < 55% minimum (no underdog lottery bets) |
| Will Bitcoin reach $92,500 in October? | Crypto | YES | `13.6%` | `7.0%` | `+6.6 п.п.` | `1.00%` | REJECTED: Edge +6.6 pp < 8 pp threshold (P_est=13.6% vs AskVWAP=7.0%) |
| Will Bitcoin reach $95,000 in October? | Crypto | YES | `7.8%` | `3.0%` | `+4.8 п.п.` | `0.10%` | REJECTED: Edge +4.8 pp < 8 pp threshold (P_est=7.8% vs AskVWAP=3.0%) |
| Will Bitcoin dip to $77,500 in October? | Crypto | YES | `56.4%` | `42.0%` | `+14.4 п.п.` | `1.00%` | REJECTED: Duplicate underlying event (crypto:bitcoin:nodate) |
| Will the price of Bitcoin be above $92,000 on Octo | Crypto | YES | `2.0%` | `100.0%` | `-98.0 п.п.` | `100.00%` | REJECTED: Edge -98.0 pp < 8 pp threshold (P_est=2.0% vs AskVWAP=100.0%) |
| Will the price of Bitcoin be above $78,000 on Octo | Crypto | NO | `10.1%` | `3.2%` | `+6.9 п.п.` | `0.30%` | REJECTED: Edge +6.9 pp < 8 pp threshold (P_est=10.1% vs AskVWAP=3.2%) |
| Will the price of Bitcoin be above $74,000 on Octo | Crypto | NO | `0.5%` | `100.0%` | `-99.5 п.п.` | `100.00%` | REJECTED: Edge -99.5 pp < 8 pp threshold (P_est=0.5% vs AskVWAP=100.0%) |
| Will Bitcoin dip to $75,000 in October? | Crypto | YES | `35.6%` | `24.0%` | `+11.6 п.п.` | `1.00%` | REJECTED: Win probability 35.6% < 55% minimum (no underdog lottery bets) |
| Will Bitcoin reach $85,000 in October? | Crypto | YES | `58.3%` | `48.0%` | `+10.3 п.п.` | `1.00%` | REJECTED: Duplicate underlying event (crypto:bitcoin:nodate) |
| Will the price of Bitcoin be above $88,000 on Octo | Crypto | YES | `2.0%` | `100.0%` | `-98.0 п.п.` | `100.00%` | REJECTED: Edge -98.0 pp < 8 pp threshold (P_est=2.0% vs AskVWAP=100.0%) |
| Will Bitcoin reach $90,000 in October? | Crypto | YES | `23.3%` | `13.0%` | `+10.3 п.п.` | `1.00%` | REJECTED: Win probability 23.3% < 55% minimum (no underdog lottery bets) |
| Will the price of Bitcoin be above $80,000 on Octo | Crypto | NO | `21.6%` | `10.0%` | `+11.6 п.п.` | `0.10%` | REJECTED: Win probability 21.6% < 55% minimum (no underdog lottery bets) |
| Will Bitcoin reach $87,500 in October? | Crypto | YES | `37.5%` | `25.0%` | `+12.5 п.п.` | `1.00%` | REJECTED: Win probability 37.5% < 55% minimum (no underdog lottery bets) |
| Will Bitcoin dip to $76,000 October 19-25? | Crypto | YES | `27.0%` | `13.0%` | `+14.0 п.п.` | `1.00%` | REJECTED: Win probability 27.0% < 55% minimum (no underdog lottery bets) |
