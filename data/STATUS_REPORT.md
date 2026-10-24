# 📊 Отчёт симулятора Polymarket (Устав Grok Bot — Демо-счёт)
**Обновлено:** `2026-10-24 12:11:22 UTC`

## 💰 Состояние виртуального портфеля
| Показатель | Значение | Правило устава |
| :--- | :--- | :--- |
| **Стартовый капитал** | `$50.00 USDC` | Не добавлять деньги |
| **Текущий баланс (Equity)** | **`$30.61 USDC`** (`-19.39$` / `-38.77%`) | Cash + Mark-to-Market по CLOB Bid |
| **Свободный кэш / В сделках** | `$18.04` / `$12.57 USDC` | До 8 открытых позиций, макс 8% банка |
| **Цель окупаемости подписки** | `$-19.39 / $60.00` (`0.0%`) | Цель: +$60.00 в месяц |
| **Просадка от пика (Текущая / Макс)** | `0.00%` / `6.31%` (Пик: `$30.61`) | Стоп-кран при просадке 40% |
| **Закрытых сделок / Win Rate** | `46` / `41.3%` | Brier Score: `0.2574` |

## 📂 Открытые позиции (4 / 8)
| # | Рынок | Кат. | Исход | Вход (Ask VWAP) | Текущий Bid | Оценка бота | Размер ($) | Нереализ. PnL | Источник |
| :- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| #35 | Will Bitcoin dip to $80,000 in October? | Crypto | **YES** | `0.610` | `0.850` | `99.5%` | `$1.11` | `$+0.44` | Kraken BTCUSDT 1m/1h Spot Klin |
| #45 | US x Iran ceasefire continues through October 24? | Geopolitics | **YES** | `0.920` | `0.973` | `98.0%` | `$3.41` | `$+0.20` | Official NFL data feed |
| #47 | Israel x Iran ceasefire continues through October 24? | Geopolitics | **YES** | `0.950` | `0.977` | `98.0%` | `$3.57` | `$+0.10` | the totality of information av |
| #50 | Spread: Manchester City FC (-3.5) | Sports | **NO** | `0.940` | `0.982` | `97.5%` | `$3.59` | `$+0.16` | https://www.premierleague.com/ |

## 🔍 Последние проверенные кандидаты и фильтр стакана CLOB
| Рынок | Кат. | Сторона | Оценка бота | Цена Ask | Перекос (Edge) | Проскальзывание CLOB | Решение |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Exact Score: Chelsea FC 0 - 0 Tottenham Hotspur FC | Other | YES | `9.5%` | `4.8%` | `+4.7 п.п.` | `0.34%` | REJECTED: Win probability 9.5% < 92% minimum (no underdog lottery bets) |
| Will US Sassuolo Calcio win on 2026-10-24? | Sports | NO | `90.0%` | `85.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Win probability 90.0% < 92% minimum (no underdog lottery bets) |
| Will the price of Bitcoin be above $78,000 on Octo | Crypto | NO | `18.1%` | `5.3%` | `+12.7 п.п.` | `0.15%` | REJECTED: Win probability 18.1% < 92% minimum (no underdog lottery bets) |
| Will Ilija Srdanović be the next prime minister of | Geopolitics | NO | `98.0%` | `89.0%` | `+9.0 п.п.` | `2.00%` | REJECTED: Category cap reached (2/2 in Geopolitics) |
| Will the price of Ethereum be above $2,400 on Octo | Crypto | YES | `8.7%` | `2.9%` | `+5.8 п.п.` | `0.68%` | REJECTED: Win probability 8.7% < 92% minimum (no underdog lottery bets) |
| Will Iliana Iotova win the 2026 Bulgarian presiden | Geopolitics | YES | `25.1%` | `13.0%` | `+12.1 п.п.` | `1.00%` | REJECTED: Win probability 25.1% < 92% minimum (no underdog lottery bets) |
| Will Naftali Bennett be the next Prime Minister of | Geopolitics | YES | `19.7%` | `15.0%` | `+4.7 п.п.` | `1.00%` | REJECTED: Win probability 19.7% < 92% minimum (no underdog lottery bets) |
| Will the price of Bitcoin be between $80,000 and $ | Crypto | NO | `26.6%` | `7.0%` | `+19.6 п.п.` | `1.89%` | REJECTED: Win probability 26.6% < 92% minimum (no underdog lottery bets) |
| Will FC Barcelona vs. Real Madrid CF end in a draw | Sports | NO | `90.7%` | `85.0%` | `+5.7 п.п.` | `1.00%` | REJECTED: Win probability 90.7% < 92% minimum (no underdog lottery bets) |
| Israel x Iran ceasefire continues through October  | Geopolitics | NO | `15.4%` | `11.0%` | `+4.5 п.п.` | `1.00%` | REJECTED: Win probability 15.4% < 92% minimum (no underdog lottery bets) |
| Will Аndrey Gyurov win the next Bulgarian presiden | Geopolitics | YES | `19.9%` | `14.0%` | `+5.9 п.п.` | `2.00%` | REJECTED: Win probability 19.9% < 92% minimum (no underdog lottery bets) |
| Dota 2: Team Yandex vs OG (BO3) - PARI Universe Gr | Sports | YES | `94.5%` | `90.0%` | `+4.5 п.п.` | `1.00%` | REJECTED: Max open positions (4) reached |
| US x Iran ceasefire continues through October 28? | Geopolitics | NO | `19.8%` | `13.0%` | `+6.8 п.п.` | `1.00%` | REJECTED: Win probability 19.8% < 92% minimum (no underdog lottery bets) |
| Will the Fed increase interest rates by 25 bps aft | Macro | NO | `98.0%` | `94.0%` | `+4.0 п.п.` | `1.00%` | REJECTED: Max open positions (4) reached |
| Will the price of Ethereum be above $2,300 on Octo | Crypto | NO | `16.4%` | `4.9%` | `+11.5 п.п.` | `1.70%` | REJECTED: Win probability 16.4% < 92% minimum (no underdog lottery bets) |
| Exact Score: Chelsea FC 0 - 0 Tottenham Hotspur FC | Other | YES | `16.0%` | `4.2%` | `+11.8 п.п.` | `0.20%` | REJECTED: Win probability 16.0% < 92% minimum (no underdog lottery bets) |
| Coventry City FC vs. Fulham FC: O/U 4.5 | Sports | NO | `90.0%` | `85.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Win probability 90.0% < 92% minimum (no underdog lottery bets) |
| Will the price of Ethereum be above $2,400 on Octo | Crypto | YES | `25.8%` | `13.0%` | `+12.8 п.п.` | `1.00%` | REJECTED: Win probability 25.8% < 92% minimum (no underdog lottery bets) |
