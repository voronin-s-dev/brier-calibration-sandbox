# 📊 Отчёт симулятора Polymarket (Устав Grok Bot — Демо-счёт)
**Обновлено:** `2026-10-19 05:20:45 UTC`

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
| #35 | Will Bitcoin dip to $80,000 in October? | Crypto | **YES** | `0.610` | `0.600` | `70.7%` | `$1.11` | `$-0.02` | Kraken BTCUSDT 1m/1h Spot Klin |

## 🔍 Последние проверенные кандидаты и фильтр стакана CLOB
| Рынок | Кат. | Сторона | Оценка бота | Цена Ask | Перекос (Edge) | Проскальзывание CLOB | Решение |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Will Bitcoin dip to $72,500 in October? | Crypto | YES | `16.0%` | `10.0%` | `+6.0 п.п.` | `1.00%` | REJECTED: Edge +6.0 pp < 8 pp threshold (P_est=16.0% vs AskVWAP=10.0%) |
| Will the price of Bitcoin be above $92,000 on Octo | Crypto | YES | `2.0%` | `100.0%` | `-98.0 п.п.` | `100.00%` | REJECTED: Edge -98.0 pp < 8 pp threshold (P_est=2.0% vs AskVWAP=100.0%) |
| Will the highest temperature in Buenos Aires be 21 | Weather | NO | `85.9%` | `54.0%` | `+31.9 п.п.` | `1.00%` | REJECTED: Narrow weather bracket NO bet prohibited (airport METAR microclimate tail risk) |
| Will Solana dip to $100 in October? | Crypto | YES | `68.7%` | `62.0%` | `+6.7 п.п.` | `4.00%` | REJECTED: Edge +6.7 pp < 8 pp threshold (P_est=68.7% vs AskVWAP=62.0%) |
| Will Ethereum reach $2,600 in October? | Crypto | YES | `52.5%` | `47.0%` | `+5.5 п.п.` | `2.00%` | REJECTED: Edge +5.5 pp < 8 pp threshold (P_est=52.5% vs AskVWAP=47.0%) |
| Will the price of Bitcoin be above $84,000 on Octo | Crypto | YES | `26.7%` | `21.0%` | `+5.7 п.п.` | `1.00%` | REJECTED: Edge +5.7 pp < 8 pp threshold (P_est=26.7% vs AskVWAP=21.0%) |
| Will the price of Bitcoin be above $88,000 on Octo | Crypto | YES | `10.5%` | `5.2%` | `+5.3 п.п.` | `0.60%` | REJECTED: Edge +5.3 pp < 8 pp threshold (P_est=10.5% vs AskVWAP=5.2%) |
| Will Bitcoin dip to $80,000 on October 19? | Crypto | YES | `18.6%` | `8.0%` | `+10.6 п.п.` | `1.00%` | REJECTED: Win probability 18.6% < 55% minimum (no underdog lottery bets) |
| Will Bitcoin dip to $79,000 on October 19? | Crypto | YES | `7.8%` | `2.9%` | `+4.9 п.п.` | `0.30%` | REJECTED: Edge +4.9 pp < 8 pp threshold (P_est=7.8% vs AskVWAP=2.9%) |
| Will Ethereum dip to $2,200 in October? | Crypto | YES | `38.4%` | `32.0%` | `+6.4 п.п.` | `1.00%` | REJECTED: Edge +6.4 pp < 8 pp threshold (P_est=38.4% vs AskVWAP=32.0%) |
| Will the price of Bitcoin be above $78,000 on Octo | Crypto | NO | `7.6%` | `2.9%` | `+4.7 п.п.` | `0.10%` | REJECTED: Edge +4.7 pp < 8 pp threshold (P_est=7.6% vs AskVWAP=2.9%) |
| Will Bitcoin reach $90,000 in October? | Crypto | YES | `33.2%` | `22.0%` | `+11.2 п.п.` | `1.00%` | REJECTED: Win probability 33.2% < 55% minimum (no underdog lottery bets) |
| Will the price of Bitcoin be above $86,000 on Octo | Crypto | YES | `20.1%` | `15.0%` | `+5.1 п.п.` | `4.00%` | REJECTED: Edge +5.1 pp < 8 pp threshold (P_est=20.1% vs AskVWAP=15.0%) |
| Will Bitcoin reach $92,500 in October? | Crypto | YES | `20.6%` | `11.0%` | `+9.6 п.п.` | `1.00%` | REJECTED: Win probability 20.6% < 55% minimum (no underdog lottery bets) |
| Will the price of Bitcoin be above $86,000 on Octo | Crypto | YES | `8.5%` | `4.0%` | `+4.5 п.п.` | `0.30%` | REJECTED: Edge +4.5 pp < 8 pp threshold (P_est=8.5% vs AskVWAP=4.0%) |
| Will Bitcoin reach $87,500 in October? | Crypto | YES | `50.1%` | `38.0%` | `+12.2 п.п.` | `1.00%` | REJECTED: Win probability 50.1% < 55% minimum (no underdog lottery bets) |
| Will Bitcoin reach $85,000 in October? | Crypto | YES | `73.2%` | `66.0%` | `+7.2 п.п.` | `2.00%` | REJECTED: Edge +7.2 pp < 8 pp threshold (P_est=73.2% vs AskVWAP=66.0%) |
| Will Bitcoin dip to $75,000 in October? | Crypto | YES | `28.1%` | `17.0%` | `+11.1 п.п.` | `1.00%` | REJECTED: Win probability 28.1% < 55% minimum (no underdog lottery bets) |
