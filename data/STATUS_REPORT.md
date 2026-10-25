# 📊 Отчёт симулятора Polymarket (Устав Grok Bot — Демо-счёт)
**Обновлено:** `2026-10-25 06:52:21 UTC`

## 💰 Состояние виртуального портфеля
| Показатель | Значение | Правило устава |
| :--- | :--- | :--- |
| **Стартовый капитал** | `$50.00 USDC` | Не добавлять деньги |
| **Текущий баланс (Equity)** | **`$31.15 USDC`** (`-18.85$` / `-37.70%`) | Cash + Mark-to-Market по CLOB Bid |
| **Свободный кэш / В сделках** | `$16.39` / `$14.76 USDC` | До 8 открытых позиций, макс 8% банка |
| **Цель окупаемости подписки** | `$-18.85 / $60.00` (`0.0%`) | Цель: +$60.00 в месяц |
| **Просадка от пика (Текущая / Макс)** | `0.40%` / `6.31%` (Пик: `$31.28`) | Стоп-кран при просадке 40% |
| **Закрытых сделок / Win Rate** | `51` / `47.1%` | Brier Score: `0.2418` |

## 📂 Открытые позиции (4 / 8)
| # | Рынок | Кат. | Исход | Вход (Ask VWAP) | Текущий Bid | Оценка бота | Размер ($) | Нереализ. PnL | Источник |
| :- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| #51 | Will there be no change in Fed interest rates after the | Macro | **YES** | `0.940` | `0.940` | `96.5%` | `$3.67` | `$+0.00` | https://www.federalreserve.gov |
| #52 | Will the Fed increase interest rates by 25 bps after th | Macro | **NO** | `0.960` | `0.950` | `98.0%` | `$3.70` | `$-0.04` | https://www.federalreserve.gov |
| #53 | Will Flávio Bolsonaro win the second round of the 2026  | Geopolitics | **NO** | `0.939` | `0.949` | `98.5%` | `$3.71` | `$+0.04` | the margin of victory between  |
| #55 | Will Bitcoin dip to $78,000 October 19-25? | Crypto | **NO** | `0.948` | `0.930` | `97.0%` | `$3.75` | `$-0.07` | https://www.binance.com/en/tra |

## 🔍 Последние проверенные кандидаты и фильтр стакана CLOB
| Рынок | Кат. | Сторона | Оценка бота | Цена Ask | Перекос (Edge) | Проскальзывание CLOB | Решение |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Steelers vs. Saints: O/U 44.5 | Sports | NO | `61.3%` | `57.0%` | `+4.3 п.п.` | `1.00%` | REJECTED: Win probability 61.3% < 92% minimum (no underdog lottery bets) |
| Will Real Madrid CF win on 2026-10-25? | Sports | YES | `32.0%` | `27.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Win probability 32.0% < 92% minimum (no underdog lottery bets) |
| Will Harry Kane win the 2026 Ballon d'Or? | Other | YES | `83.1%` | `70.5%` | `+12.6 п.п.` | `0.10%` | REJECTED: Win probability 83.1% < 92% minimum (no underdog lottery bets) |
| Will Kylian Mbappé win the 2026 Ballon d'Or? | Other | YES | `21.9%` | `16.5%` | `+5.5 п.п.` | `0.10%` | REJECTED: Win probability 21.9% < 92% minimum (no underdog lottery bets) |
| Will the price of Ethereum be between $2,300 and $ | Crypto | NO | `24.6%` | `12.0%` | `+12.6 п.п.` | `3.00%` | REJECTED: Win probability 24.6% < 92% minimum (no underdog lottery bets) |
| Spread: Chiefs (-13.5) | Sports | YES | `17.2%` | `12.0%` | `+5.2 п.п.` | `1.00%` | REJECTED: Win probability 17.2% < 92% minimum (no underdog lottery bets) |
| Will Flávio Bolsonaro win the second round of the  | Geopolitics | YES | `19.4%` | `15.0%` | `+4.3 п.п.` | `1.00%` | REJECTED: Win probability 19.4% < 92% minimum (no underdog lottery bets) |
| Will Bitcoin dip to $78,000 on October 25? | Crypto | YES | `18.5%` | `6.3%` | `+12.2 п.п.` | `0.10%` | REJECTED: Win probability 18.5% < 92% minimum (no underdog lottery bets) |
| Will the price of Ethereum be above $2,400 on Octo | Crypto | YES | `9.9%` | `2.5%` | `+7.4 п.п.` | `1.20%` | REJECTED: Win probability 9.9% < 92% minimum (no underdog lottery bets) |
| Will the price of Bitcoin be above $78,000 on Octo | Crypto | NO | `20.5%` | `12.8%` | `+7.7 п.п.` | `2.50%` | REJECTED: Win probability 20.5% < 92% minimum (no underdog lottery bets) |
| Will Naftali Bennett be the next Prime Minister of | Geopolitics | YES | `24.4%` | `13.0%` | `+11.4 п.п.` | `1.00%` | REJECTED: Win probability 24.4% < 92% minimum (no underdog lottery bets) |
| Will Аndrey Gyurov win the next Bulgarian presiden | Geopolitics | YES | `19.7%` | `13.0%` | `+6.7 п.п.` | `1.00%` | REJECTED: Win probability 19.7% < 92% minimum (no underdog lottery bets) |
| Will the price of Ethereum be above $2,300 on Octo | Crypto | YES | `96.2%` | `90.5%` | `+5.7 п.п.` | `0.80%` | REJECTED: Max open positions (4) reached |
| LoL: T1 vs CTBC Flying Oyster (BO1) - Worlds Group | Sports | NO | `18.2%` | `13.0%` | `+5.2 п.п.` | `1.00%` | REJECTED: Win probability 18.2% < 92% minimum (no underdog lottery bets) |
| LoL: Gen.G vs LYON (BO3) - Worlds Group Stage | Sports | YES | `95.0%` | `90.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Max open positions (4) reached |
| Will FC Barcelona vs. Real Madrid CF end in a draw | Sports | NO | `89.7%` | `85.0%` | `+4.7 п.п.` | `1.00%` | REJECTED: Win probability 89.7% < 92% minimum (no underdog lottery bets) |
| Steelers vs. Saints: O/U 44.5 | Sports | NO | `61.3%` | `57.0%` | `+4.3 п.п.` | `1.00%` | REJECTED: Win probability 61.3% < 92% minimum (no underdog lottery bets) |
| Will Real Madrid CF win on 2026-10-25? | Sports | YES | `32.0%` | `27.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Win probability 32.0% < 92% minimum (no underdog lottery bets) |
