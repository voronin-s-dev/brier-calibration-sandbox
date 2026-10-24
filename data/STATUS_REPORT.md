# 📊 Отчёт симулятора Polymarket (Устав Grok Bot — Демо-счёт)
**Обновлено:** `2026-10-24 07:28:52 UTC`

## 💰 Состояние виртуального портфеля
| Показатель | Значение | Правило устава |
| :--- | :--- | :--- |
| **Стартовый капитал** | `$50.00 USDC` | Не добавлять деньги |
| **Текущий баланс (Equity)** | **`$30.25 USDC`** (`-19.75$` / `-39.50%`) | Cash + Mark-to-Market по CLOB Bid |
| **Свободный кэш / В сделках** | `$18.04` / `$12.21 USDC` | До 8 открытых позиций, макс 8% банка |
| **Цель окупаемости подписки** | `$-19.75 / $60.00` (`0.0%`) | Цель: +$60.00 в месяц |
| **Просадка от пика (Текущая / Макс)** | `0.16%` / `6.31%` (Пик: `$30.30`) | Стоп-кран при просадке 40% |
| **Закрытых сделок / Win Rate** | `46` / `41.3%` | Brier Score: `0.2574` |

## 📂 Открытые позиции (4 / 8)
| # | Рынок | Кат. | Исход | Вход (Ask VWAP) | Текущий Bid | Оценка бота | Размер ($) | Нереализ. PnL | Источник |
| :- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| #35 | Will Bitcoin dip to $80,000 in October? | Crypto | **YES** | `0.610` | `0.800` | `99.5%` | `$1.11` | `$+0.35` | Kraken BTCUSDT 1m/1h Spot Klin |
| #45 | US x Iran ceasefire continues through October 24? | Geopolitics | **YES** | `0.920` | `0.974` | `98.0%` | `$3.41` | `$+0.20` | Official NFL data feed |
| #47 | Israel x Iran ceasefire continues through October 24? | Geopolitics | **YES** | `0.950` | `0.977` | `98.0%` | `$3.57` | `$+0.10` | the totality of information av |
| #50 | Spread: Manchester City FC (-3.5) | Sports | **NO** | `0.940` | `0.910` | `97.5%` | `$3.59` | `$-0.11` | https://www.premierleague.com/ |

## 🔍 Последние проверенные кандидаты и фильтр стакана CLOB
| Рынок | Кат. | Сторона | Оценка бота | Цена Ask | Перекос (Edge) | Проскальзывание CLOB | Решение |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Will the price of Ethereum be above $2,300 on Octo | Crypto | NO | `16.4%` | `4.9%` | `+11.5 п.п.` | `1.70%` | REJECTED: Win probability 16.4% < 92% minimum (no underdog lottery bets) |
| Exact Score: Chelsea FC 0 - 0 Tottenham Hotspur FC | Other | YES | `16.0%` | `4.2%` | `+11.8 п.п.` | `0.20%` | REJECTED: Win probability 16.0% < 92% minimum (no underdog lottery bets) |
| Coventry City FC vs. Fulham FC: O/U 4.5 | Sports | NO | `90.0%` | `85.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Win probability 90.0% < 92% minimum (no underdog lottery bets) |
| Will the price of Ethereum be above $2,400 on Octo | Crypto | YES | `25.8%` | `13.0%` | `+12.8 п.п.` | `1.00%` | REJECTED: Win probability 25.8% < 92% minimum (no underdog lottery bets) |
| Will Flávio Bolsonaro win the second round of the  | Geopolitics | YES | `23.4%` | `15.0%` | `+8.4 п.п.` | `1.00%` | REJECTED: Win probability 23.4% < 92% minimum (no underdog lottery bets) |
| Will Iliana Iotova win the 2026 Bulgarian presiden | Geopolitics | YES | `24.6%` | `16.0%` | `+8.6 п.п.` | `3.00%` | REJECTED: Win probability 24.6% < 92% minimum (no underdog lottery bets) |
| Will Ethereum dip to $2,300 October 19-25? | Crypto | YES | `39.3%` | `16.0%` | `+23.3 п.п.` | `1.00%` | REJECTED: Win probability 39.3% < 92% minimum (no underdog lottery bets) |
| Will FC Barcelona vs. Real Madrid CF end in a draw | Sports | NO | `92.5%` | `85.0%` | `+7.5 п.п.` | `1.00%` | REJECTED: Max open positions (4) reached |
| Will Ilija Srdanović be the next prime minister of | Geopolitics | NO | `93.0%` | `88.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Category cap reached (2/2 in Geopolitics) |
| Israel x Iran ceasefire continues through October  | Geopolitics | NO | `17.7%` | `11.0%` | `+6.7 п.п.` | `1.00%` | REJECTED: Win probability 17.7% < 92% minimum (no underdog lottery bets) |
| Will Аndrey Gyurov win the next Bulgarian presiden | Geopolitics | YES | `19.5%` | `13.0%` | `+6.5 п.п.` | `1.00%` | REJECTED: Win probability 19.5% < 92% minimum (no underdog lottery bets) |
| Will Lamine Yamal win the 2026 Ballon d'Or? | Other | YES | `25.1%` | `13.6%` | `+11.5 п.п.` | `0.10%` | REJECTED: Win probability 25.1% < 92% minimum (no underdog lottery bets) |
| US x Iran ceasefire continues through October 28? | Geopolitics | NO | `19.3%` | `15.0%` | `+4.3 п.п.` | `1.00%` | REJECTED: Win probability 19.3% < 92% minimum (no underdog lottery bets) |
| Will the Fed increase interest rates by 25 bps aft | Macro | NO | `98.0%` | `94.0%` | `+4.0 п.п.` | `1.00%` | REJECTED: Max open positions (4) reached |
| Will the price of Ethereum be above $2,300 on Octo | Crypto | NO | `16.6%` | `4.3%` | `+12.2 п.п.` | `1.15%` | REJECTED: Win probability 16.6% < 92% minimum (no underdog lottery bets) |
| Exact Score: Chelsea FC 0 - 0 Tottenham Hotspur FC | Other | YES | `10.5%` | `4.2%` | `+6.3 п.п.` | `0.20%` | REJECTED: Win probability 10.5% < 92% minimum (no underdog lottery bets) |
| Coventry City FC vs. Fulham FC: O/U 4.5 | Sports | NO | `90.0%` | `85.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Win probability 90.0% < 92% minimum (no underdog lottery bets) |
| Will the price of Ethereum be above $2,400 on Octo | Crypto | YES | `25.8%` | `20.0%` | `+5.8 п.п.` | `2.00%` | REJECTED: Win probability 25.8% < 92% minimum (no underdog lottery bets) |
