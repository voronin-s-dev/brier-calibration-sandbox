# 📊 Отчёт симулятора Polymarket (Устав Grok Bot — Демо-счёт)
**Обновлено:** `2026-10-19 18:01:20 UTC`

## 💰 Состояние виртуального портфеля
| Показатель | Значение | Правило устава |
| :--- | :--- | :--- |
| **Стартовый капитал** | `$50.00 USDC` | Не добавлять деньги |
| **Текущий баланс (Equity)** | **`$27.76 USDC`** (`-22.24$` / `-44.48%`) | Cash + Mark-to-Market по CLOB Bid |
| **Свободный кэш / В сделках** | `$26.54` / `$1.22 USDC` | До 8 открытых позиций, макс 8% банка |
| **Цель окупаемости подписки** | `$-22.24 / $60.00` (`0.0%`) | Цель: +$60.00 в месяц |
| **Просадка от пика (Текущая / Макс)** | `1.02%` / `1.48%` (Пик: `$28.05`) | Стоп-кран при просадке 40% |
| **Закрытых сделок / Win Rate** | `34` / `23.5%` | Brier Score: `0.4280` |

## 📂 Открытые позиции (1 / 8)
| # | Рынок | Кат. | Исход | Вход (Ask VWAP) | Текущий Bid | Оценка бота | Размер ($) | Нереализ. PnL | Источник |
| :- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| #35 | Will Bitcoin dip to $80,000 in October? | Crypto | **YES** | `0.610` | `0.670` | `77.1%` | `$1.11` | `$+0.11` | Kraken BTCUSDT 1m/1h Spot Klin |

## 🔍 Последние проверенные кандидаты и фильтр стакана CLOB
| Рынок | Кат. | Сторона | Оценка бота | Цена Ask | Перекос (Edge) | Проскальзывание CLOB | Решение |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Will the price of Bitcoin be above $86,000 on Octo | Crypto | YES | `7.1%` | `2.0%` | `+5.1 п.п.` | `0.40%` | REJECTED: Edge +5.1 pp < 8 pp threshold (P_est=7.1% vs AskVWAP=2.0%) |
| Will the price of Bitcoin be above $92,000 on Octo | Crypto | YES | `2.0%` | `100.0%` | `-98.0 п.п.` | `100.00%` | REJECTED: Edge -98.0 pp < 8 pp threshold (P_est=2.0% vs AskVWAP=100.0%) |
| Will the price of Bitcoin be above $76,000 on Octo | Crypto | NO | `11.3%` | `6.0%` | `+5.3 п.п.` | `2.00%` | REJECTED: Edge +5.3 pp < 8 pp threshold (P_est=11.3% vs AskVWAP=6.0%) |
| Will Bitcoin dip to $72,500 in October? | Crypto | YES | `17.8%` | `11.0%` | `+6.8 п.п.` | `1.00%` | REJECTED: Edge +6.8 pp < 8 pp threshold (P_est=17.8% vs AskVWAP=11.0%) |
| Will Solana dip to $100 in October? | Crypto | YES | `76.0%` | `70.0%` | `+6.0 п.п.` | `2.00%` | REJECTED: Edge +6.0 pp < 8 pp threshold (P_est=76.0% vs AskVWAP=70.0%) |
| Will the highest temperature in Wuhan be 16°C on O | Weather | YES | `2.0%` | `100.0%` | `-98.0 п.п.` | `100.00%` | REJECTED: Edge -98.0 pp < 8 pp threshold (P_est=2.0% vs AskVWAP=100.0%) |
| Will the price of Bitcoin be above $80,000 on Octo | Crypto | NO | `23.6%` | `14.0%` | `+9.6 п.п.` | `1.44%` | REJECTED: Win probability 23.6% < 55% minimum (no underdog lottery bets) |
| Will the price of Bitcoin be above $74,000 on Octo | Crypto | NO | `0.5%` | `100.0%` | `-99.5 п.п.` | `100.00%` | REJECTED: Edge -99.5 pp < 8 pp threshold (P_est=0.5% vs AskVWAP=100.0%) |
| Will Bitcoin reach $92,500 in October? | Crypto | YES | `16.7%` | `8.0%` | `+8.7 п.п.` | `1.00%` | REJECTED: Win probability 16.7% < 55% minimum (no underdog lottery bets) |
| Will the price of Bitcoin be above $84,000 on Octo | Crypto | YES | `12.5%` | `5.0%` | `+7.5 п.п.` | `1.00%` | REJECTED: Edge +7.5 pp < 8 pp threshold (P_est=12.5% vs AskVWAP=5.0%) |
| Will the price of Ethereum be above $2,500 on Octo | Crypto | YES | `14.9%` | `10.0%` | `+4.9 п.п.` | `1.00%` | REJECTED: Edge +4.9 pp < 8 pp threshold (P_est=14.9% vs AskVWAP=10.0%) |
| Will the price of Bitcoin be above $78,000 on Octo | Crypto | NO | `8.0%` | `2.0%` | `+6.0 п.п.` | `0.63%` | REJECTED: Edge +6.0 pp < 8 pp threshold (P_est=8.0% vs AskVWAP=2.0%) |
| Will Bitcoin reach $95,000 in October? | Crypto | YES | `9.6%` | `3.3%` | `+6.3 п.п.` | `0.10%` | REJECTED: Edge +6.3 pp < 8 pp threshold (P_est=9.6% vs AskVWAP=3.3%) |
| Will Bitcoin dip to $77,500 in October? | Crypto | YES | `50.9%` | `37.0%` | `+14.0 п.п.` | `1.00%` | REJECTED: Win probability 50.9% < 55% minimum (no underdog lottery bets) |
| Will Bitcoin reach $85,000 in October? | Crypto | YES | `65.1%` | `56.0%` | `+9.1 п.п.` | `2.00%` | REJECTED: Duplicate underlying event (crypto:bitcoin:nodate) |
| Will Bitcoin reach $90,000 in October? | Crypto | YES | `27.8%` | `17.0%` | `+10.8 п.п.` | `1.00%` | REJECTED: Win probability 27.8% < 55% minimum (no underdog lottery bets) |
| Will Bitcoin dip to $75,000 in October? | Crypto | YES | `31.4%` | `20.0%` | `+11.4 п.п.` | `1.00%` | REJECTED: Win probability 31.4% < 55% minimum (no underdog lottery bets) |
| Will Bitcoin reach $87,500 in October? | Crypto | YES | `43.2%` | `31.0%` | `+12.2 п.п.` | `1.00%` | REJECTED: Win probability 43.2% < 55% minimum (no underdog lottery bets) |
