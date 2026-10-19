# 📊 Отчёт симулятора Polymarket (Устав Grok Bot — Демо-счёт)
**Обновлено:** `2026-10-19 05:29:55 UTC`

## 💰 Состояние виртуального портфеля
| Показатель | Значение | Правило устава |
| :--- | :--- | :--- |
| **Стартовый капитал** | `$50.00 USDC` | Не добавлять деньги |
| **Текущий баланс (Equity)** | **`$27.63 USDC`** (`-22.37$` / `-44.73%`) | Cash + Mark-to-Market по CLOB Bid |
| **Свободный кэш / В сделках** | `$26.54` / `$1.09 USDC` | До 8 открытых позиций, макс 8% банка |
| **Цель окупаемости подписки** | `$-22.37 / $60.00` (`0.0%`) | Цель: +$60.00 в месяц |
| **Просадка от пика (Текущая / Макс)** | `1.48%` / `1.48%` (Пик: `$28.05`) | Стоп-кран при просадке 40% |
| **Закрытых сделок / Win Rate** | `34` / `23.5%` | Brier Score: `0.4280` |

## 📂 Открытые позиции (1 / 8)
| # | Рынок | Кат. | Исход | Вход (Ask VWAP) | Текущий Bid | Оценка бота | Размер ($) | Нереализ. PnL | Источник |
| :- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| #35 | Will Bitcoin dip to $80,000 in October? | Crypto | **YES** | `0.610` | `0.600` | `70.6%` | `$1.11` | `$-0.02` | Kraken BTCUSDT 1m/1h Spot Klin |

## 🔍 Последние проверенные кандидаты и фильтр стакана CLOB
| Рынок | Кат. | Сторона | Оценка бота | Цена Ask | Перекос (Edge) | Проскальзывание CLOB | Решение |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Will the price of Bitcoin be above $92,000 on Octo | Crypto | YES | `2.0%` | `100.0%` | `-98.0 п.п.` | `100.00%` | REJECTED: Edge -98.0 pp < 8 pp threshold (P_est=2.0% vs AskVWAP=100.0%) |
| Will the highest temperature in Buenos Aires be 21 | Weather | NO | `85.9%` | `54.0%` | `+31.9 п.п.` | `1.00%` | REJECTED: Narrow weather bracket NO bet prohibited (airport METAR microclimate tail risk) |
| Will Solana dip to $100 in October? | Crypto | YES | `68.5%` | `60.0%` | `+8.5 п.п.` | `3.00%` | REJECTED: CLOB round-trip slippage 3.00% > 2.0% limit |
| Will Ethereum reach $2,600 in October? | Crypto | YES | `52.5%` | `47.0%` | `+5.5 п.п.` | `2.00%` | REJECTED: Edge +5.5 pp < 8 pp threshold (P_est=52.5% vs AskVWAP=47.0%) |
| Will the price of Bitcoin be above $84,000 on Octo | Crypto | YES | `26.7%` | `22.0%` | `+4.7 п.п.` | `1.00%` | REJECTED: Edge +4.7 pp < 8 pp threshold (P_est=26.7% vs AskVWAP=22.0%) |
| Will the price of Bitcoin be above $88,000 on Octo | Crypto | YES | `10.5%` | `4.8%` | `+5.7 п.п.` | `0.20%` | REJECTED: Edge +5.7 pp < 8 pp threshold (P_est=10.5% vs AskVWAP=4.8%) |
| Will Bitcoin dip to $80,000 on October 19? | Crypto | YES | `18.8%` | `8.0%` | `+10.8 п.п.` | `1.00%` | REJECTED: Win probability 18.8% < 55% minimum (no underdog lottery bets) |
| Will Bitcoin dip to $79,000 on October 19? | Crypto | YES | `7.7%` | `3.0%` | `+4.7 п.п.` | `0.20%` | REJECTED: Edge +4.7 pp < 8 pp threshold (P_est=7.7% vs AskVWAP=3.0%) |
| Will Ethereum dip to $2,200 in October? | Crypto | YES | `38.4%` | `32.0%` | `+6.4 п.п.` | `1.00%` | REJECTED: Edge +6.4 pp < 8 pp threshold (P_est=38.4% vs AskVWAP=32.0%) |
| Will the price of Bitcoin be above $78,000 on Octo | Crypto | NO | `7.5%` | `2.8%` | `+4.8 п.п.` | `0.10%` | REJECTED: Edge +4.7 pp < 8 pp threshold (P_est=7.5% vs AskVWAP=2.8%) |
| Will Bitcoin reach $90,000 in October? | Crypto | YES | `33.2%` | `22.0%` | `+11.2 п.п.` | `1.00%` | REJECTED: Win probability 33.2% < 55% minimum (no underdog lottery bets) |
| Will the price of Bitcoin be above $80,000 on Octo | Crypto | NO | `14.1%` | `7.0%` | `+7.1 п.п.` | `1.00%` | REJECTED: Edge +7.1 pp < 8 pp threshold (P_est=14.1% vs AskVWAP=7.0%) |
| Will the price of Bitcoin be above $86,000 on Octo | Crypto | YES | `20.1%` | `14.0%` | `+6.1 п.п.` | `3.00%` | REJECTED: Edge +6.1 pp < 8 pp threshold (P_est=20.1% vs AskVWAP=14.0%) |
| Will the price of Bitcoin be above $86,000 on Octo | Crypto | YES | `8.4%` | `3.8%` | `+4.6 п.п.` | `0.20%` | REJECTED: Edge +4.6 pp < 8 pp threshold (P_est=8.4% vs AskVWAP=3.8%) |
| Will Bitcoin reach $92,500 in October? | Crypto | YES | `20.6%` | `11.0%` | `+9.6 п.п.` | `1.00%` | REJECTED: Win probability 20.6% < 55% minimum (no underdog lottery bets) |
| Will Bitcoin reach $87,500 in October? | Crypto | YES | `50.1%` | `38.0%` | `+12.1 п.п.` | `1.00%` | REJECTED: Win probability 50.1% < 55% minimum (no underdog lottery bets) |
| Will Bitcoin reach $85,000 in October? | Crypto | YES | `73.2%` | `66.0%` | `+7.2 п.п.` | `2.00%` | REJECTED: Edge +7.2 pp < 8 pp threshold (P_est=73.2% vs AskVWAP=66.0%) |
| Will Bitcoin dip to $75,000 in October? | Crypto | YES | `28.1%` | `17.0%` | `+11.1 п.п.` | `1.00%` | REJECTED: Win probability 28.1% < 55% minimum (no underdog lottery bets) |
