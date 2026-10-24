# 📊 Отчёт симулятора Polymarket (Устав Grok Bot — Демо-счёт)
**Обновлено:** `2026-10-24 02:04:11 UTC`

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
| #45 | US x Iran ceasefire continues through October 24? | Geopolitics | **YES** | `0.920` | `0.930` | `97.0%` | `$3.41` | `$+0.04` | Official NFL data feed |
| #47 | Israel x Iran ceasefire continues through October 24? | Geopolitics | **YES** | `0.950` | `0.979` | `98.0%` | `$3.57` | `$+0.11` | the totality of information av |
| #50 | Spread: Manchester City FC (-3.5) | Sports | **NO** | `0.940` | `0.920` | `97.5%` | `$3.59` | `$-0.08` | https://www.premierleague.com/ |

## 🔍 Последние проверенные кандидаты и фильтр стакана CLOB
| Рынок | Кат. | Сторона | Оценка бота | Цена Ask | Перекос (Edge) | Проскальзывание CLOB | Решение |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Will Harry Kane win the 2026 Ballon d'Or? | Other | YES | `87.4%` | `76.7%` | `+10.7 п.п.` | `0.10%` | REJECTED: Win probability 87.4% < 92% minimum (no underdog lottery bets) |
| Spread: Club Atlético de Madrid (-3.5) | Sports | NO | `97.5%` | `83.0%` | `+14.5 п.п.` | `1.00%` | REJECTED: Contract price $0.830 outside sweet spot [$0.84, $0.96] |
| Will Chelsea FC win on 2026-10-24? | Sports | YES | `58.0%` | `53.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Win probability 58.0% < 92% minimum (no underdog lottery bets) |
| Will the price of Bitcoin be above $78,000 on Octo | Crypto | NO | `18.0%` | `8.1%` | `+9.9 п.п.` | `1.50%` | REJECTED: Win probability 18.0% < 92% minimum (no underdog lottery bets) |
| Will the price of Ethereum be above $2,300 on Octo | Crypto | NO | `7.2%` | `3.0%` | `+4.2 п.п.` | `1.80%` | REJECTED: Win probability 7.2% < 92% minimum (no underdog lottery bets) |
| Will the price of Ethereum be above $2,300 on Octo | Crypto | NO | `16.9%` | `6.3%` | `+10.6 п.п.` | `3.30%` | REJECTED: Win probability 16.9% < 92% minimum (no underdog lottery bets) |
| Will Bitcoin reach $84,000 October 19-25? | Crypto | YES | `25.9%` | `3.9%` | `+22.0 п.п.` | `0.79%` | REJECTED: Win probability 25.9% < 92% minimum (no underdog lottery bets) |
| Will the price of Bitcoin be between $80,000 and $ | Crypto | NO | `44.4%` | `11.0%` | `+33.4 п.п.` | `1.00%` | REJECTED: Win probability 44.4% < 92% minimum (no underdog lottery bets) |
| Will the price of Bitcoin be between $78,000 and $ | Crypto | YES | `21.8%` | `7.6%` | `+14.2 п.п.` | `1.90%` | REJECTED: Win probability 21.8% < 92% minimum (no underdog lottery bets) |
| Will Ethereum reach $2,500 October 19-25? | Crypto | YES | `23.8%` | `6.3%` | `+17.5 п.п.` | `1.99%` | REJECTED: Win probability 23.8% < 92% minimum (no underdog lottery bets) |
| Will Iliana Iotova win the 2026 Bulgarian presiden | Geopolitics | YES | `23.4%` | `14.0%` | `+9.4 п.п.` | `1.08%` | REJECTED: Win probability 23.4% < 92% minimum (no underdog lottery bets) |
| Will FC Barcelona vs. Real Madrid CF end in a draw | Sports | NO | `96.2%` | `85.0%` | `+11.2 п.п.` | `1.00%` | REJECTED: Max open positions (4) reached |
| Will Ilija Srdanović be the next prime minister of | Geopolitics | YES | `19.8%` | `15.0%` | `+4.8 п.п.` | `2.00%` | REJECTED: Win probability 19.8% < 92% minimum (no underdog lottery bets) |
| Will Bitcoin dip to $76,000 October 19-25? | Crypto | YES | `9.6%` | `3.0%` | `+6.6 п.п.` | `0.33%` | REJECTED: Win probability 9.6% < 92% minimum (no underdog lottery bets) |
| Israel x Iran ceasefire continues through October  | Geopolitics | NO | `18.9%` | `10.0%` | `+8.9 п.п.` | `1.00%` | REJECTED: Win probability 18.9% < 92% minimum (no underdog lottery bets) |
| Will Аndrey Gyurov win the next Bulgarian presiden | Geopolitics | YES | `19.7%` | `13.0%` | `+6.7 п.п.` | `1.00%` | REJECTED: Win probability 19.7% < 92% minimum (no underdog lottery bets) |
| Will Bitcoin dip to $78,000 October 19-25? | Crypto | YES | `29.3%` | `7.5%` | `+21.8 п.п.` | `0.28%` | REJECTED: Win probability 29.3% < 92% minimum (no underdog lottery bets) |
| Will Lamine Yamal win the 2026 Ballon d'Or? | Other | YES | `20.5%` | `15.1%` | `+5.4 п.п.` | `0.14%` | REJECTED: Win probability 20.5% < 92% minimum (no underdog lottery bets) |
