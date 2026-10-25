# 📊 Отчёт симулятора Polymarket (Устав Grok Bot — Демо-счёт)
**Обновлено:** `2026-10-25 07:01:40 UTC`

## 💰 Состояние виртуального портфеля
| Показатель | Значение | Правило устава |
| :--- | :--- | :--- |
| **Стартовый капитал** | `$50.00 USDC` | Не добавлять деньги |
| **Текущий баланс (Equity)** | **`$31.17 USDC`** (`-18.83$` / `-37.67%`) | Cash + Mark-to-Market по CLOB Bid |
| **Свободный кэш / В сделках** | `$16.39` / `$14.78 USDC` | До 8 открытых позиций, макс 8% банка |
| **Цель окупаемости подписки** | `$-18.83 / $60.00` (`0.0%`) | Цель: +$60.00 в месяц |
| **Просадка от пика (Текущая / Макс)** | `0.35%` / `6.31%` (Пик: `$31.28`) | Стоп-кран при просадке 40% |
| **Закрытых сделок / Win Rate** | `51` / `47.1%` | Brier Score: `0.2418` |

## 📂 Открытые позиции (4 / 8)
| # | Рынок | Кат. | Исход | Вход (Ask VWAP) | Текущий Bid | Оценка бота | Размер ($) | Нереализ. PnL | Источник |
| :- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| #51 | Will there be no change in Fed interest rates after the | Macro | **YES** | `0.940` | `0.940` | `96.5%` | `$3.67` | `$+0.00` | https://www.federalreserve.gov |
| #52 | Will the Fed increase interest rates by 25 bps after th | Macro | **NO** | `0.960` | `0.950` | `98.0%` | `$3.70` | `$-0.04` | https://www.federalreserve.gov |
| #53 | Will Flávio Bolsonaro win the second round of the 2026  | Geopolitics | **NO** | `0.939` | `0.949` | `98.5%` | `$3.71` | `$+0.04` | the margin of victory between  |
| #55 | Will Bitcoin dip to $78,000 October 19-25? | Crypto | **NO** | `0.948` | `0.934` | `96.7%` | `$3.75` | `$-0.06` | https://www.binance.com/en/tra |

## 🔍 Последние проверенные кандидаты и фильтр стакана CLOB
| Рынок | Кат. | Сторона | Оценка бота | Цена Ask | Перекос (Edge) | Проскальзывание CLOB | Решение |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Steelers vs. Saints: O/U 44.5 | Sports | NO | `61.3%` | `57.0%` | `+4.3 п.п.` | `1.00%` | REJECTED: Win probability 61.3% < 92% minimum (no underdog lottery bets) |
| Will Brentford FC win on 2026-10-25? | Sports | NO | `47.0%` | `42.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Win probability 47.0% < 92% minimum (no underdog lottery bets) |
| Will Real Madrid CF win on 2026-10-25? | Sports | YES | `32.0%` | `27.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Win probability 32.0% < 92% minimum (no underdog lottery bets) |
| Will Harry Kane win the 2026 Ballon d'Or? | Other | YES | `83.3%` | `70.6%` | `+12.7 п.п.` | `0.10%` | REJECTED: Win probability 83.3% < 92% minimum (no underdog lottery bets) |
| Will the price of Ethereum be between $2,300 and $ | Crypto | NO | `24.6%` | `10.0%` | `+14.6 п.п.` | `2.00%` | REJECTED: Win probability 24.6% < 92% minimum (no underdog lottery bets) |
| Spread: 49ers (-20.5) | Sports | NO | `98.0%` | `94.0%` | `+4.0 п.п.` | `1.00%` | REJECTED: Max open positions (4) reached |
| Will Getafe CF win on 2026-10-25? | Sports | YES | `18.0%` | `13.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Win probability 18.0% < 92% minimum (no underdog lottery bets) |
| Will the price of Ethereum be above $2,400 on Octo | Crypto | YES | `9.6%` | `2.7%` | `+6.9 п.п.` | `0.70%` | REJECTED: Win probability 9.6% < 92% minimum (no underdog lottery bets) |
| Will the price of Bitcoin be above $78,000 on Octo | Crypto | NO | `20.7%` | `12.1%` | `+8.6 п.п.` | `2.00%` | REJECTED: Win probability 20.7% < 92% minimum (no underdog lottery bets) |
| Will Bitcoin dip to $78,000 on October 25? | Crypto | YES | `18.5%` | `6.3%` | `+12.2 п.п.` | `0.60%` | REJECTED: Win probability 18.5% < 92% minimum (no underdog lottery bets) |
| Spread: Chiefs (-13.5) | Sports | YES | `17.1%` | `12.0%` | `+5.1 п.п.` | `1.00%` | REJECTED: Win probability 17.1% < 92% minimum (no underdog lottery bets) |
| Will Elon Musk post 115-139 tweets from October 24 | Geopolitics | YES | `14.6%` | `8.1%` | `+6.5 п.п.` | `1.15%` | REJECTED: Win probability 14.6% < 92% minimum (no underdog lottery bets) |
| Will Naftali Bennett be the next Prime Minister of | Geopolitics | YES | `23.9%` | `13.0%` | `+10.9 п.п.` | `1.00%` | REJECTED: Win probability 23.9% < 92% minimum (no underdog lottery bets) |
| Will Аndrey Gyurov win the next Bulgarian presiden | Geopolitics | YES | `19.7%` | `13.0%` | `+6.7 п.п.` | `1.00%` | REJECTED: Win probability 19.7% < 92% minimum (no underdog lottery bets) |
| LoL: T1 vs CTBC Flying Oyster (BO1) - Worlds Group | Sports | NO | `17.8%` | `13.0%` | `+4.8 п.п.` | `1.00%` | REJECTED: Win probability 17.8% < 92% minimum (no underdog lottery bets) |
| LoL: Gen.G vs LYON (BO3) - Worlds Group Stage | Sports | YES | `95.0%` | `90.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Max open positions (4) reached |
| US x Iran ceasefire continues through October 28? | Geopolitics | NO | `16.6%` | `10.0%` | `+6.6 п.п.` | `1.00%` | REJECTED: Win probability 16.6% < 92% minimum (no underdog lottery bets) |
| Steelers vs. Saints: O/U 44.5 | Sports | NO | `61.3%` | `57.0%` | `+4.3 п.п.` | `1.00%` | REJECTED: Win probability 61.3% < 92% minimum (no underdog lottery bets) |
