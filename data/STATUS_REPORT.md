# 📊 Отчёт симулятора Polymarket (Устав Grok Bot — Демо-счёт)
**Обновлено:** `2026-10-24 01:54:55 UTC`

## 💰 Состояние виртуального портфеля
| Показатель | Значение | Правило устава |
| :--- | :--- | :--- |
| **Стартовый капитал** | `$50.00 USDC` | Не добавлять деньги |
| **Текущий баланс (Equity)** | **`$30.06 USDC`** (`-19.94$` / `-39.88%`) | Cash + Mark-to-Market по CLOB Bid |
| **Свободный кэш / В сделках** | `$18.04` / `$12.02 USDC` | До 8 открытых позиций, макс 8% банка |
| **Цель окупаемости подписки** | `$-19.94 / $60.00` (`0.0%`) | Цель: +$60.00 в месяц |
| **Просадка от пика (Текущая / Макс)** | `0.25%` / `6.31%` (Пик: `$30.14`) | Стоп-кран при просадке 40% |
| **Закрытых сделок / Win Rate** | `46` / `41.3%` | Brier Score: `0.2574` |

## 📂 Открытые позиции (4 / 8)
| # | Рынок | Кат. | Исход | Вход (Ask VWAP) | Текущий Bid | Оценка бота | Размер ($) | Нереализ. PnL | Источник |
| :- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| #35 | Will Bitcoin dip to $80,000 in October? | Crypto | **YES** | `0.610` | `0.760` | `99.5%` | `$1.11` | `$+0.27` | Kraken BTCUSDT 1m/1h Spot Klin |
| #45 | US x Iran ceasefire continues through October 24? | Geopolitics | **YES** | `0.920` | `0.930` | `96.5%` | `$3.41` | `$+0.04` | Official NFL data feed |
| #47 | Israel x Iran ceasefire continues through October 24? | Geopolitics | **YES** | `0.950` | `0.979` | `98.0%` | `$3.57` | `$+0.11` | the totality of information av |
| #50 | Spread: Manchester City FC (-3.5) | Sports | **NO** | `0.940` | `0.920` | `97.5%` | `$3.59` | `$-0.08` | https://www.premierleague.com/ |

## 🔍 Последние проверенные кандидаты и фильтр стакана CLOB
| Рынок | Кат. | Сторона | Оценка бота | Цена Ask | Перекос (Edge) | Проскальзывание CLOB | Решение |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Will Manchester City FC win on 2026-10-24? | Sports | YES | `66.0%` | `61.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Win probability 66.0% < 92% minimum (no underdog lottery bets) |
| Will Harry Kane win the 2026 Ballon d'Or? | Other | YES | `88.6%` | `76.8%` | `+11.8 п.п.` | `0.20%` | REJECTED: Win probability 88.6% < 92% minimum (no underdog lottery bets) |
| Spread: Club Atlético de Madrid (-3.5) | Sports | NO | `97.5%` | `83.0%` | `+14.5 п.п.` | `1.00%` | REJECTED: Contract price $0.830 outside sweet spot [$0.84, $0.96] |
| Will Chelsea FC win on 2026-10-24? | Sports | YES | `58.0%` | `53.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Win probability 58.0% < 92% minimum (no underdog lottery bets) |
| Will the price of Ethereum be above $2,300 on Octo | Crypto | NO | `7.4%` | `3.1%` | `+4.3 п.п.` | `1.98%` | REJECTED: Win probability 7.4% < 92% minimum (no underdog lottery bets) |
| Will Flavio Bolsonaro win the most votes in the se | Geopolitics | YES | `17.5%` | `13.0%` | `+4.5 п.п.` | `2.00%` | REJECTED: Win probability 17.5% < 92% minimum (no underdog lottery bets) |
| Will the price of Ethereum be above $2,300 on Octo | Crypto | NO | `17.1%` | `6.0%` | `+11.1 п.п.` | `1.12%` | REJECTED: Win probability 17.1% < 92% minimum (no underdog lottery bets) |
| Will Bitcoin reach $84,000 October 19-25? | Crypto | YES | `25.9%` | `4.0%` | `+21.9 п.п.` | `0.79%` | REJECTED: Win probability 25.9% < 92% minimum (no underdog lottery bets) |
| Will the price of Bitcoin be between $80,000 and $ | Crypto | NO | `44.8%` | `12.0%` | `+32.8 п.п.` | `2.00%` | REJECTED: Win probability 44.8% < 92% minimum (no underdog lottery bets) |
| Will the price of Bitcoin be between $78,000 and $ | Crypto | YES | `22.1%` | `7.8%` | `+14.3 п.п.` | `1.30%` | REJECTED: Win probability 22.1% < 92% minimum (no underdog lottery bets) |
| Will Ethereum reach $2,500 October 19-25? | Crypto | YES | `23.9%` | `6.5%` | `+17.4 п.п.` | `2.19%` | REJECTED: Win probability 23.9% < 92% minimum (no underdog lottery bets) |
| Will Iliana Iotova win the 2026 Bulgarian presiden | Geopolitics | YES | `23.3%` | `14.0%` | `+9.3 п.п.` | `1.08%` | REJECTED: Win probability 23.3% < 92% minimum (no underdog lottery bets) |
| Will FC Barcelona vs. Real Madrid CF end in a draw | Sports | NO | `96.2%` | `85.0%` | `+11.2 п.п.` | `1.00%` | REJECTED: Max open positions (4) reached |
| Will Ilija Srdanović be the next prime minister of | Geopolitics | YES | `20.4%` | `15.0%` | `+5.4 п.п.` | `2.00%` | REJECTED: Win probability 20.4% < 92% minimum (no underdog lottery bets) |
| Will Bitcoin dip to $76,000 October 19-25? | Crypto | YES | `9.8%` | `3.2%` | `+6.7 п.п.` | `0.19%` | REJECTED: Win probability 9.8% < 92% minimum (no underdog lottery bets) |
| Israel x Iran ceasefire continues through October  | Geopolitics | NO | `18.7%` | `10.0%` | `+8.7 п.п.` | `1.00%` | REJECTED: Win probability 18.7% < 92% minimum (no underdog lottery bets) |
| Will Аndrey Gyurov win the next Bulgarian presiden | Geopolitics | YES | `19.3%` | `13.0%` | `+6.3 п.п.` | `2.00%` | REJECTED: Win probability 19.3% < 92% minimum (no underdog lottery bets) |
| Will Bitcoin dip to $78,000 October 19-25? | Crypto | YES | `29.4%` | `7.6%` | `+21.8 п.п.` | `0.10%` | REJECTED: Win probability 29.4% < 92% minimum (no underdog lottery bets) |
