# 📊 Отчёт симулятора Polymarket (Устав Grok Bot — Демо-счёт)
**Обновлено:** `2026-10-23 23:33:46 UTC`

## 💰 Состояние виртуального портфеля
| Показатель | Значение | Правило устава |
| :--- | :--- | :--- |
| **Стартовый капитал** | `$50.00 USDC` | Не добавлять деньги |
| **Текущий баланс (Equity)** | **`$29.88 USDC`** (`-20.12$` / `-40.24%`) | Cash + Mark-to-Market по CLOB Bid |
| **Свободный кэш / В сделках** | `$18.04` / `$11.84 USDC` | До 8 открытых позиций, макс 8% банка |
| **Цель окупаемости подписки** | `$-20.12 / $60.00` (`0.0%`) | Цель: +$60.00 в месяц |
| **Просадка от пика (Текущая / Макс)** | `0.85%` / `6.31%` (Пик: `$30.14`) | Стоп-кран при просадке 40% |
| **Закрытых сделок / Win Rate** | `46` / `41.3%` | Brier Score: `0.2574` |

## 📂 Открытые позиции (4 / 8)
| # | Рынок | Кат. | Исход | Вход (Ask VWAP) | Текущий Bid | Оценка бота | Размер ($) | Нереализ. PnL | Источник |
| :- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| #35 | Will Bitcoin dip to $80,000 in October? | Crypto | **YES** | `0.610` | `0.760` | `99.5%` | `$1.11` | `$+0.27` | Kraken BTCUSDT 1m/1h Spot Klin |
| #45 | US x Iran ceasefire continues through October 24? | Geopolitics | **YES** | `0.920` | `0.920` | `96.0%` | `$3.41` | `$-0.00` | Official NFL data feed |
| #47 | Israel x Iran ceasefire continues through October 24? | Geopolitics | **YES** | `0.950` | `0.930` | `97.5%` | `$3.57` | `$-0.08` | the totality of information av |
| #50 | Spread: Manchester City FC (-3.5) | Sports | **NO** | `0.940` | `0.930` | `97.5%` | `$3.59` | `$-0.04` | https://www.premierleague.com/ |

## 🔍 Последние проверенные кандидаты и фильтр стакана CLOB
| Рынок | Кат. | Сторона | Оценка бота | Цена Ask | Перекос (Edge) | Проскальзывание CLOB | Решение |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| LoL: Team Liquid vs CTBC Flying Oyster (BO1) - Wor | Sports | YES | `1.5%` | `100.0%` | `-98.5 п.п.` | `100.00%` | REJECTED: Edge -98.5 pp < 2 pp threshold (P_est=1.5% vs AskVWAP=100.0%) |
| Will the price of Ethereum be above $2,300 on Octo | Crypto | NO | `9.8%` | `3.4%` | `+6.4 п.п.` | `1.20%` | REJECTED: Win probability 9.8% < 92% minimum (no underdog lottery bets) |
| Will the price of Ethereum be above $2,300 on Octo | Crypto | NO | `18.8%` | `7.9%` | `+10.9 п.п.` | `2.20%` | REJECTED: Win probability 18.8% < 92% minimum (no underdog lottery bets) |
| Will Ethereum dip to $2,200 October 19-25? | Crypto | YES | `9.4%` | `3.6%` | `+5.8 п.п.` | `0.66%` | REJECTED: Win probability 9.4% < 92% minimum (no underdog lottery bets) |
| Will Bitcoin reach $84,000 October 19-25? | Crypto | YES | `26.9%` | `3.5%` | `+23.4 п.п.` | `0.76%` | REJECTED: Win probability 26.9% < 92% minimum (no underdog lottery bets) |
| Will the price of Bitcoin be between $80,000 and $ | Crypto | NO | `47.5%` | `14.0%` | `+33.5 п.п.` | `1.22%` | REJECTED: Win probability 47.5% < 92% minimum (no underdog lottery bets) |
| Will the price of Bitcoin be between $78,000 and $ | Crypto | YES | `21.7%` | `9.1%` | `+12.6 п.п.` | `1.61%` | REJECTED: Win probability 21.7% < 92% minimum (no underdog lottery bets) |
| Will the price of Bitcoin be above $80,000 on Octo | Crypto | NO | `33.0%` | `16.8%` | `+16.2 п.п.` | `0.40%` | REJECTED: Win probability 33.0% < 92% minimum (no underdog lottery bets) |
| Will Ethereum reach $2,500 October 19-25? | Crypto | YES | `23.5%` | `6.2%` | `+17.3 п.п.` | `2.25%` | REJECTED: Win probability 23.5% < 92% minimum (no underdog lottery bets) |
| Will Iliana Iotova win the 2026 Bulgarian presiden | Geopolitics | YES | `18.5%` | `14.0%` | `+4.5 п.п.` | `2.00%` | REJECTED: Win probability 18.5% < 92% minimum (no underdog lottery bets) |
| Will FC Barcelona vs. Real Madrid CF end in a draw | Sports | NO | `96.2%` | `85.0%` | `+11.2 п.п.` | `1.00%` | REJECTED: Max open positions (4) reached |
| Will Ilija Srdanović be the next prime minister of | Geopolitics | YES | `18.5%` | `14.0%` | `+4.5 п.п.` | `2.00%` | REJECTED: Win probability 18.5% < 92% minimum (no underdog lottery bets) |
| Will Bitcoin dip to $76,000 October 19-25? | Crypto | YES | `10.2%` | `3.2%` | `+7.0 п.п.` | `0.19%` | REJECTED: Win probability 10.2% < 92% minimum (no underdog lottery bets) |
| Israel x Iran ceasefire continues through October  | Geopolitics | NO | `21.7%` | `13.0%` | `+8.7 п.п.` | `2.00%` | REJECTED: Win probability 21.7% < 92% minimum (no underdog lottery bets) |
| Will Ethereum dip to $2,350 on October 23? | Crypto | YES | `99.5%` | `22.0%` | `+77.5 п.п.` | `5.00%` | REJECTED: Contract price $0.220 outside sweet spot [$0.84, $0.96] |
| Will Аndrey Gyurov win the next Bulgarian presiden | Geopolitics | YES | `19.2%` | `13.0%` | `+6.2 п.п.` | `1.00%` | REJECTED: Win probability 19.2% < 92% minimum (no underdog lottery bets) |
| Will Bitcoin dip to $78,000 October 19-25? | Crypto | YES | `29.8%` | `7.5%` | `+22.3 п.п.` | `0.20%` | REJECTED: Win probability 29.8% < 92% minimum (no underdog lottery bets) |
| Will Bitcoin dip to $80,000 on October 23? | Crypto | NO | `96.0%` | `91.6%` | `+4.5 п.п.` | `0.30%` | REJECTED: Max open positions (4) reached |
