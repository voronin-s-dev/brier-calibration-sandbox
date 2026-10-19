# 📊 Отчёт симулятора Polymarket (Устав Grok Bot — Демо-счёт)
**Обновлено:** `2026-10-19 22:25:28 UTC`

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
| #35 | Will Bitcoin dip to $80,000 in October? | Crypto | **YES** | `0.610` | `0.640` | `74.4%` | `$1.11` | `$+0.05` | Kraken BTCUSDT 1m/1h Spot Klin |

## 🔍 Последние проверенные кандидаты и фильтр стакана CLOB
| Рынок | Кат. | Сторона | Оценка бота | Цена Ask | Перекос (Edge) | Проскальзывание CLOB | Решение |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Will the price of Bitcoin be between $78,000 and $ | Crypto | YES | `9.4%` | `2.6%` | `+6.8 п.п.` | `0.10%` | REJECTED: Edge +6.8 pp < 8 pp threshold (P_est=9.4% vs AskVWAP=2.6%) |
| Will the price of Bitcoin be above $86,000 on Octo | Crypto | YES | `7.3%` | `2.0%` | `+5.3 п.п.` | `0.50%` | REJECTED: Edge +5.3 pp < 8 pp threshold (P_est=7.3% vs AskVWAP=2.0%) |
| Will the price of Bitcoin be above $76,000 on Octo | Crypto | NO | `10.1%` | `4.8%` | `+5.3 п.п.` | `2.00%` | REJECTED: Edge +5.3 pp < 8 pp threshold (P_est=10.1% vs AskVWAP=4.8%) |
| Will the price of Bitcoin be above $80,000 on Octo | Crypto | NO | `20.2%` | `11.0%` | `+9.2 п.п.` | `1.12%` | REJECTED: Win probability 20.2% < 55% minimum (no underdog lottery bets) |
| Will Solana dip to $100 in October? | Crypto | YES | `68.4%` | `63.0%` | `+5.4 п.п.` | `3.00%` | REJECTED: Edge +5.4 pp < 8 pp threshold (P_est=68.4% vs AskVWAP=63.0%) |
| Will the highest temperature in Wuhan be 16°C on O | Weather | YES | `2.0%` | `100.0%` | `-98.0 п.п.` | `100.00%` | REJECTED: Edge -98.0 pp < 8 pp threshold (P_est=2.0% vs AskVWAP=100.0%) |
| Will the price of Bitcoin be above $92,000 on Octo | Crypto | YES | `2.0%` | `100.0%` | `-98.0 п.п.` | `100.00%` | REJECTED: Edge -98.0 pp < 8 pp threshold (P_est=2.0% vs AskVWAP=100.0%) |
| Will Bitcoin reach $92,500 in October? | Crypto | YES | `16.9%` | `7.0%` | `+9.9 п.п.` | `1.00%` | REJECTED: Win probability 16.9% < 55% minimum (no underdog lottery bets) |
| Will Bitcoin dip to $77,500 in October? | Crypto | YES | `48.3%` | `35.0%` | `+13.3 п.п.` | `2.00%` | REJECTED: Win probability 48.3% < 55% minimum (no underdog lottery bets) |
| Will the price of Bitcoin be above $74,000 on Octo | Crypto | NO | `0.5%` | `100.0%` | `-99.5 п.п.` | `100.00%` | REJECTED: Edge -99.5 pp < 8 pp threshold (P_est=0.5% vs AskVWAP=100.0%) |
| Will the price of Bitcoin be above $78,000 on Octo | Crypto | NO | `6.3%` | `1.4%` | `+4.9 п.п.` | `0.40%` | REJECTED: Edge +4.9 pp < 8 pp threshold (P_est=6.3% vs AskVWAP=1.4%) |
| Will the price of Ethereum be above $2,500 on Octo | Crypto | YES | `17.0%` | `12.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Edge +5.0 pp < 8 pp threshold (P_est=17.0% vs AskVWAP=12.0%) |
| Will the price of Bitcoin be above $88,000 on Octo | Crypto | YES | `2.0%` | `100.0%` | `-98.0 п.п.` | `100.00%` | REJECTED: Edge -98.0 pp < 8 pp threshold (P_est=2.0% vs AskVWAP=100.0%) |
| Will Bitcoin reach $95,000 in October? | Crypto | YES | `9.9%` | `3.4%` | `+6.5 п.п.` | `0.20%` | REJECTED: Edge +6.5 pp < 8 pp threshold (P_est=9.9% vs AskVWAP=3.4%) |
| Will Bitcoin dip to $75,000 in October? | Crypto | YES | `29.5%` | `18.0%` | `+11.5 п.п.` | `1.00%` | REJECTED: Win probability 29.5% < 55% minimum (no underdog lottery bets) |
| Will the price of Bitcoin be above $84,000 on Octo | Crypto | YES | `12.8%` | `6.0%` | `+6.9 п.п.` | `1.00%` | REJECTED: Edge +6.9 pp < 8 pp threshold (P_est=12.8% vs AskVWAP=6.0%) |
| Will Bitcoin reach $90,000 in October? | Crypto | YES | `28.6%` | `17.0%` | `+11.6 п.п.` | `1.00%` | REJECTED: Win probability 28.6% < 55% minimum (no underdog lottery bets) |
| Will Bitcoin reach $85,000 in October? | Crypto | YES | `67.5%` | `58.0%` | `+9.5 п.п.` | `2.00%` | REJECTED: Duplicate underlying event (crypto:bitcoin:nodate) |
