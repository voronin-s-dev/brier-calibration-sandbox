# 📊 Отчёт симулятора Polymarket (Устав Grok Bot — Демо-счёт)
**Обновлено:** `2026-10-24 07:10:12 UTC`

## 💰 Состояние виртуального портфеля
| Показатель | Значение | Правило устава |
| :--- | :--- | :--- |
| **Стартовый капитал** | `$50.00 USDC` | Не добавлять деньги |
| **Текущий баланс (Equity)** | **`$30.27 USDC`** (`-19.73$` / `-39.47%`) | Cash + Mark-to-Market по CLOB Bid |
| **Свободный кэш / В сделках** | `$18.04` / `$12.23 USDC` | До 8 открытых позиций, макс 8% банка |
| **Цель окупаемости подписки** | `$-19.73 / $60.00` (`0.0%`) | Цель: +$60.00 в месяц |
| **Просадка от пика (Текущая / Макс)** | `0.00%` / `6.31%` (Пик: `$30.27`) | Стоп-кран при просадке 40% |
| **Закрытых сделок / Win Rate** | `46` / `41.3%` | Brier Score: `0.2574` |

## 📂 Открытые позиции (4 / 8)
| # | Рынок | Кат. | Исход | Вход (Ask VWAP) | Текущий Bid | Оценка бота | Размер ($) | Нереализ. PnL | Источник |
| :- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| #35 | Will Bitcoin dip to $80,000 in October? | Crypto | **YES** | `0.610` | `0.790` | `99.5%` | `$1.11` | `$+0.33` | Kraken BTCUSDT 1m/1h Spot Klin |
| #45 | US x Iran ceasefire continues through October 24? | Geopolitics | **YES** | `0.920` | `0.969` | `98.0%` | `$3.41` | `$+0.18` | Official NFL data feed |
| #47 | Israel x Iran ceasefire continues through October 24? | Geopolitics | **YES** | `0.950` | `0.980` | `98.0%` | `$3.57` | `$+0.11` | the totality of information av |
| #50 | Spread: Manchester City FC (-3.5) | Sports | **NO** | `0.940` | `0.920` | `97.5%` | `$3.59` | `$-0.08` | https://www.premierleague.com/ |

## 🔍 Последние проверенные кандидаты и фильтр стакана CLOB
| Рынок | Кат. | Сторона | Оценка бота | Цена Ask | Перекос (Edge) | Проскальзывание CLOB | Решение |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Will the price of Ethereum be above $2,300 on Octo | Crypto | NO | `16.5%` | `5.6%` | `+11.0 п.п.` | `1.98%` | REJECTED: Win probability 16.5% < 92% minimum (no underdog lottery bets) |
| Exact Score: Chelsea FC 0 - 0 Tottenham Hotspur FC | Other | YES | `11.0%` | `4.2%` | `+6.8 п.п.` | `0.30%` | REJECTED: Win probability 11.0% < 92% minimum (no underdog lottery bets) |
| Coventry City FC vs. Fulham FC: O/U 4.5 | Sports | NO | `90.0%` | `85.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Win probability 90.0% < 92% minimum (no underdog lottery bets) |
| Will the price of Ethereum be above $2,400 on Octo | Crypto | YES | `26.4%` | `13.0%` | `+13.4 п.п.` | `1.00%` | REJECTED: Win probability 26.4% < 92% minimum (no underdog lottery bets) |
| Will Bitcoin reach $84,000 October 19-25? | Crypto | YES | `22.0%` | `3.1%` | `+18.9 п.п.` | `0.70%` | REJECTED: Win probability 22.0% < 92% minimum (no underdog lottery bets) |
| Will Flávio Bolsonaro win the second round of the  | Geopolitics | YES | `22.0%` | `15.0%` | `+7.0 п.п.` | `1.00%` | REJECTED: Win probability 22.0% < 92% minimum (no underdog lottery bets) |
| Will Parma Calcio 1913 win on 2026-10-24? | Sports | YES | `17.0%` | `12.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Win probability 17.0% < 92% minimum (no underdog lottery bets) |
| Will Bitcoin dip to $79,000 on October 24? | Crypto | YES | `31.1%` | `4.0%` | `+27.1 п.п.` | `0.72%` | REJECTED: Win probability 31.1% < 92% minimum (no underdog lottery bets) |
| Will the price of Bitcoin be above $80,000 on Octo | Crypto | NO | `34.0%` | `18.7%` | `+15.3 п.п.` | `1.11%` | REJECTED: Win probability 34.0% < 92% minimum (no underdog lottery bets) |
| Will the price of Bitcoin be between $80,000 and $ | Crypto | YES | `98.0%` | `93.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Max open positions (4) reached |
| Will Iliana Iotova win the 2026 Bulgarian presiden | Geopolitics | YES | `20.0%` | `16.0%` | `+4.0 п.п.` | `3.00%` | REJECTED: Win probability 20.0% < 92% minimum (no underdog lottery bets) |
| Will Ethereum dip to $2,300 October 19-25? | Crypto | YES | `39.4%` | `17.0%` | `+22.4 п.п.` | `1.00%` | REJECTED: Win probability 39.4% < 92% minimum (no underdog lottery bets) |
| Will FC Barcelona vs. Real Madrid CF end in a draw | Sports | NO | `96.2%` | `85.0%` | `+11.2 п.п.` | `1.00%` | REJECTED: Max open positions (4) reached |
| Will Ilija Srdanović be the next prime minister of | Geopolitics | NO | `93.0%` | `88.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Category cap reached (2/2 in Geopolitics) |
| Israel x Iran ceasefire continues through October  | Geopolitics | NO | `16.4%` | `12.0%` | `+4.4 п.п.` | `2.00%` | REJECTED: Win probability 16.4% < 92% minimum (no underdog lottery bets) |
| Will Аndrey Gyurov win the next Bulgarian presiden | Geopolitics | YES | `19.6%` | `13.0%` | `+6.6 п.п.` | `1.00%` | REJECTED: Win probability 19.6% < 92% minimum (no underdog lottery bets) |
| Will the price of Bitcoin be above $80,000 on Octo | Crypto | YES | `98.5%` | `93.6%` | `+4.9 п.п.` | `0.70%` | REJECTED: Max open positions (4) reached |
| Will Lamine Yamal win the 2026 Ballon d'Or? | Other | YES | `19.9%` | `14.5%` | `+5.3 п.п.` | `0.30%` | REJECTED: Win probability 19.9% < 92% minimum (no underdog lottery bets) |
