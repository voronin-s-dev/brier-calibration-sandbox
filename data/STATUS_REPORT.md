# 📊 Отчёт симулятора Polymarket (Устав Grok Bot — Демо-счёт)
**Обновлено:** `2026-10-25 12:29:46 UTC`

## 💰 Состояние виртуального портфеля
| Показатель | Значение | Правило устава |
| :--- | :--- | :--- |
| **Стартовый капитал** | `$50.00 USDC` | Не добавлять деньги |
| **Текущий баланс (Equity)** | **`$31.20 USDC`** (`-18.80$` / `-37.59%`) | Cash + Mark-to-Market по CLOB Bid |
| **Свободный кэш / В сделках** | `$16.39` / `$14.81 USDC` | До 8 открытых позиций, макс 8% банка |
| **Цель окупаемости подписки** | `$-18.80 / $60.00` (`0.0%`) | Цель: +$60.00 в месяц |
| **Просадка от пика (Текущая / Макс)** | `0.23%` / `6.31%` (Пик: `$31.28`) | Стоп-кран при просадке 40% |
| **Закрытых сделок / Win Rate** | `51` / `47.1%` | Brier Score: `0.2418` |

## 📂 Открытые позиции (4 / 8)
| # | Рынок | Кат. | Исход | Вход (Ask VWAP) | Текущий Bid | Оценка бота | Размер ($) | Нереализ. PnL | Источник |
| :- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| #51 | Will there be no change in Fed interest rates after the | Macro | **YES** | `0.940` | `0.950` | `96.5%` | `$3.67` | `$+0.04` | https://www.federalreserve.gov |
| #52 | Will the Fed increase interest rates by 25 bps after th | Macro | **NO** | `0.960` | `0.950` | `98.0%` | `$3.70` | `$-0.04` | https://www.federalreserve.gov |
| #53 | Will Flávio Bolsonaro win the second round of the 2026  | Geopolitics | **NO** | `0.939` | `0.954` | `98.5%` | `$3.71` | `$+0.06` | the margin of victory between  |
| #55 | Will Bitcoin dip to $78,000 October 19-25? | Crypto | **NO** | `0.948` | `0.929` | `96.5%` | `$3.75` | `$-0.08` | https://www.binance.com/en/tra |

## 🔍 Последние проверенные кандидаты и фильтр стакана CLOB
| Рынок | Кат. | Сторона | Оценка бота | Цена Ask | Перекос (Edge) | Проскальзывание CLOB | Решение |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Will the price of Bitcoin be above $78,000 on Octo | Crypto | NO | `21.4%` | `12.6%` | `+8.8 п.п.` | `1.50%` | REJECTED: Win probability 21.4% < 92% minimum (no underdog lottery bets) |
| Will US Lecce win on 2026-10-25? | Sports | YES | `19.0%` | `14.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Win probability 19.0% < 92% minimum (no underdog lottery bets) |
| FC Barcelona vs. Real Madrid CF: O/U 6.5 | Sports | YES | `23.2%` | `15.0%` | `+8.2 п.п.` | `1.00%` | REJECTED: Win probability 23.2% < 92% minimum (no underdog lottery bets) |
| Will Bitcoin reach $82,000 on October 25? | Crypto | YES | `27.8%` | `14.0%` | `+13.8 п.п.` | `1.00%` | REJECTED: Win probability 27.8% < 92% minimum (no underdog lottery bets) |
| Will the price of Bitcoin be above $82,000 on Octo | Crypto | YES | `20.2%` | `14.0%` | `+6.2 п.п.` | `1.00%` | REJECTED: Win probability 20.2% < 92% minimum (no underdog lottery bets) |
| Exact Score: FC Barcelona 2 - 1 Real Madrid CF? | Other | YES | `14.0%` | `9.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Win probability 14.0% < 92% minimum (no underdog lottery bets) |
| Will Flavio Bolsonaro win the most votes in the se | Geopolitics | NO | `92.9%` | `88.0%` | `+4.9 п.п.` | `3.00%` | REJECTED: CLOB round-trip slippage 3.00% > 2.0% limit |
| Will the price of Ethereum be above $2,300 on Octo | Crypto | YES | `94.4%` | `90.3%` | `+4.1 п.п.` | `1.10%` | REJECTED: Max open positions (4) reached |
| Will Bitcoin reach $82,000 October 19-25? | Crypto | YES | `27.7%` | `13.8%` | `+13.9 п.п.` | `1.78%` | REJECTED: Win probability 27.7% < 92% minimum (no underdog lottery bets) |
| Will Lamine Yamal win the 2026 Ballon d'Or? | Other | YES | `23.4%` | `10.7%` | `+12.7 п.п.` | `0.10%` | REJECTED: Win probability 23.4% < 92% minimum (no underdog lottery bets) |
| Steelers vs. Saints: O/U 44.5 | Sports | NO | `61.3%` | `57.0%` | `+4.3 п.п.` | `1.00%` | REJECTED: Win probability 61.3% < 92% minimum (no underdog lottery bets) |
| Will Brentford FC win on 2026-10-25? | Sports | NO | `47.0%` | `42.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Win probability 47.0% < 92% minimum (no underdog lottery bets) |
| Will Real Madrid CF win on 2026-10-25? | Sports | YES | `32.0%` | `27.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Win probability 32.0% < 92% minimum (no underdog lottery bets) |
| Will Harry Kane win the 2026 Ballon d'Or? | Other | YES | `83.3%` | `70.6%` | `+12.7 п.п.` | `0.10%` | REJECTED: Win probability 83.3% < 92% minimum (no underdog lottery bets) |
| Will the price of Ethereum be between $2,300 and $ | Crypto | NO | `24.6%` | `10.0%` | `+14.6 п.п.` | `2.00%` | REJECTED: Win probability 24.6% < 92% minimum (no underdog lottery bets) |
| Spread: 49ers (-20.5) | Sports | NO | `98.0%` | `94.0%` | `+4.0 п.п.` | `1.00%` | REJECTED: Max open positions (4) reached |
| Will Getafe CF win on 2026-10-25? | Sports | YES | `18.0%` | `13.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Win probability 18.0% < 92% minimum (no underdog lottery bets) |
| Will the price of Ethereum be above $2,400 on Octo | Crypto | YES | `9.6%` | `2.7%` | `+6.9 п.п.` | `0.70%` | REJECTED: Win probability 9.6% < 92% minimum (no underdog lottery bets) |
