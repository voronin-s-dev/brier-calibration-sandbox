# 📊 Отчёт симулятора Polymarket (Устав Grok Bot — Демо-счёт)
**Обновлено:** `2026-10-19 11:09:54 UTC`

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
| #35 | Will Bitcoin dip to $80,000 in October? | Crypto | **YES** | `0.610` | `0.640` | `73.8%` | `$1.11` | `$+0.05` | Kraken BTCUSDT 1m/1h Spot Klin |

## 🔍 Последние проверенные кандидаты и фильтр стакана CLOB
| Рынок | Кат. | Сторона | Оценка бота | Цена Ask | Перекос (Edge) | Проскальзывание CLOB | Решение |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Will Ethereum reach $2,600 in October? | Crypto | YES | `51.0%` | `44.0%` | `+7.0 п.п.` | `1.00%` | REJECTED: Edge +7.0 pp < 8 pp threshold (P_est=51.0% vs AskVWAP=44.0%) |
| Will the price of Bitcoin be above $88,000 on Octo | Crypto | YES | `9.1%` | `5.0%` | `+4.1 п.п.` | `0.40%` | REJECTED: Edge +4.1 pp < 8 pp threshold (P_est=9.1% vs AskVWAP=5.0%) |
| Will the price of Bitcoin be above $80,000 on Octo | Crypto | NO | `21.4%` | `13.0%` | `+8.5 п.п.` | `1.00%` | REJECTED: Win probability 21.4% < 55% minimum (no underdog lottery bets) |
| Will Ethereum dip to $2,350 on October 19? | Crypto | YES | `25.3%` | `17.0%` | `+8.3 п.п.` | `3.00%` | REJECTED: Win probability 25.3% < 55% minimum (no underdog lottery bets) |
| Will Ethereum dip to $2,200 in October? | Crypto | YES | `38.4%` | `30.0%` | `+8.4 п.п.` | `1.00%` | REJECTED: Win probability 38.4% < 55% minimum (no underdog lottery bets) |
| Will the price of Bitcoin be above $84,000 on Octo | Crypto | YES | `20.3%` | `14.0%` | `+6.3 п.п.` | `1.00%` | REJECTED: Edge +6.3 pp < 8 pp threshold (P_est=20.3% vs AskVWAP=14.0%) |
| Will the highest temperature in Wellington be 18°C | Weather | YES | `14.8%` | `23.0%` | `-8.2 п.п.` | `8.00%` | REJECTED: Edge -8.2 pp < 8 pp threshold (P_est=14.8% vs AskVWAP=23.0%) |
| Will Solana dip to $100 in October? | Crypto | YES | `72.4%` | `67.0%` | `+5.4 п.п.` | `4.00%` | REJECTED: Edge +5.4 pp < 8 pp threshold (P_est=72.4% vs AskVWAP=67.0%) |
| Will Bitcoin reach $85,000 on October 19? | Crypto | YES | `11.7%` | `3.6%` | `+8.1 п.п.` | `0.10%` | REJECTED: Win probability 11.7% < 55% minimum (no underdog lottery bets) |
| Will the price of Bitcoin be above $78,000 on Octo | Crypto | NO | `7.9%` | `3.3%` | `+4.6 п.п.` | `0.70%` | REJECTED: Edge +4.6 pp < 8 pp threshold (P_est=7.9% vs AskVWAP=3.3%) |
| Will Bitcoin dip to $79,000 on October 19? | Crypto | YES | `6.3%` | `2.2%` | `+4.1 п.п.` | `0.40%` | REJECTED: Edge +4.1 pp < 8 pp threshold (P_est=6.3% vs AskVWAP=2.2%) |
| Will Bitcoin reach $90,000 in October? | Crypto | YES | `30.8%` | `20.0%` | `+10.8 п.п.` | `1.00%` | REJECTED: Win probability 30.8% < 55% minimum (no underdog lottery bets) |
| Will the price of Bitcoin be above $86,000 on Octo | Crypto | YES | `17.5%` | `12.0%` | `+5.5 п.п.` | `3.00%` | REJECTED: Edge +5.5 pp < 8 pp threshold (P_est=17.5% vs AskVWAP=12.0%) |
| Will Bitcoin reach $92,500 in October? | Crypto | YES | `18.9%` | `10.0%` | `+8.9 п.п.` | `1.00%` | REJECTED: Win probability 18.9% < 55% minimum (no underdog lottery bets) |
| Will the price of Ethereum be above $2,500 on Octo | Crypto | YES | `22.8%` | `18.0%` | `+4.8 п.п.` | `1.00%` | REJECTED: Edge +4.8 pp < 8 pp threshold (P_est=22.8% vs AskVWAP=18.0%) |
| Will the price of Bitcoin be above $80,000 on Octo | Crypto | NO | `14.8%` | `7.5%` | `+7.3 п.п.` | `0.60%` | REJECTED: Edge +7.3 pp < 8 pp threshold (P_est=14.8% vs AskVWAP=7.5%) |
| Will Bitcoin reach $87,500 in October? | Crypto | YES | `47.2%` | `34.0%` | `+13.2 п.п.` | `1.00%` | REJECTED: Win probability 47.2% < 55% minimum (no underdog lottery bets) |
| Will Bitcoin reach $85,000 in October? | Crypto | YES | `69.7%` | `61.0%` | `+8.7 п.п.` | `2.00%` | REJECTED: Duplicate underlying event (crypto:bitcoin:nodate) |
