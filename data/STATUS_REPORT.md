# 📊 Отчёт симулятора Polymarket (Устав Grok Bot — Демо-счёт)
**Обновлено:** `2026-10-25 12:39:05 UTC`

## 💰 Состояние виртуального портфеля
| Показатель | Значение | Правило устава |
| :--- | :--- | :--- |
| **Стартовый капитал** | `$50.00 USDC` | Не добавлять деньги |
| **Текущий баланс (Equity)** | **`$31.24 USDC`** (`-18.76$` / `-37.51%`) | Cash + Mark-to-Market по CLOB Bid |
| **Свободный кэш / В сделках** | `$16.39` / `$14.85 USDC` | До 8 открытых позиций, макс 8% банка |
| **Цель окупаемости подписки** | `$-18.76 / $60.00` (`0.0%`) | Цель: +$60.00 в месяц |
| **Просадка от пика (Текущая / Макс)** | `0.10%` / `6.31%` (Пик: `$31.28`) | Стоп-кран при просадке 40% |
| **Закрытых сделок / Win Rate** | `51` / `47.1%` | Brier Score: `0.2418` |

## 📂 Открытые позиции (4 / 8)
| # | Рынок | Кат. | Исход | Вход (Ask VWAP) | Текущий Bid | Оценка бота | Размер ($) | Нереализ. PnL | Источник |
| :- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| #51 | Will there be no change in Fed interest rates after the | Macro | **YES** | `0.940` | `0.950` | `96.5%` | `$3.67` | `$+0.04` | https://www.federalreserve.gov |
| #52 | Will the Fed increase interest rates by 25 bps after th | Macro | **NO** | `0.960` | `0.950` | `98.0%` | `$3.70` | `$-0.04` | https://www.federalreserve.gov |
| #53 | Will Flávio Bolsonaro win the second round of the 2026  | Geopolitics | **NO** | `0.939` | `0.955` | `98.5%` | `$3.71` | `$+0.06` | the margin of victory between  |
| #55 | Will Bitcoin dip to $78,000 October 19-25? | Crypto | **NO** | `0.948` | `0.938` | `97.0%` | `$3.75` | `$-0.04` | https://www.binance.com/en/tra |

## 🔍 Последние проверенные кандидаты и фильтр стакана CLOB
| Рынок | Кат. | Сторона | Оценка бота | Цена Ask | Перекос (Edge) | Проскальзывание CLOB | Решение |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Will the price of Bitcoin be above $78,000 on Octo | Crypto | NO | `21.4%` | `12.5%` | `+8.9 п.п.` | `1.90%` | REJECTED: Win probability 21.4% < 92% minimum (no underdog lottery bets) |
| Will US Lecce win on 2026-10-25? | Sports | YES | `19.0%` | `14.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Win probability 19.0% < 92% minimum (no underdog lottery bets) |
| FC Barcelona vs. Real Madrid CF: O/U 6.5 | Sports | YES | `20.0%` | `15.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Win probability 20.0% < 92% minimum (no underdog lottery bets) |
| Will Bitcoin reach $82,000 on October 25? | Crypto | YES | `27.5%` | `16.0%` | `+11.5 п.п.` | `2.00%` | REJECTED: Win probability 27.5% < 92% minimum (no underdog lottery bets) |
| Will the price of Bitcoin be above $84,000 on Octo | Crypto | YES | `14.4%` | `9.0%` | `+5.4 п.п.` | `2.00%` | REJECTED: Win probability 14.4% < 92% minimum (no underdog lottery bets) |
| Will the price of Bitcoin be between $78,000 and $ | Crypto | YES | `32.9%` | `15.0%` | `+17.9 п.п.` | `4.26%` | REJECTED: Win probability 32.9% < 92% minimum (no underdog lottery bets) |
| Will the price of Bitcoin be above $76,000 on Octo | Crypto | NO | `11.8%` | `6.9%` | `+4.9 п.п.` | `2.40%` | REJECTED: Win probability 11.8% < 92% minimum (no underdog lottery bets) |
| Exact Score: FC Barcelona 2 - 1 Real Madrid CF? | Other | YES | `14.0%` | `9.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Win probability 14.0% < 92% minimum (no underdog lottery bets) |
| Will the price of Bitcoin be above $82,000 on Octo | Crypto | YES | `20.4%` | `15.0%` | `+5.5 п.п.` | `1.00%` | REJECTED: Win probability 20.4% < 92% minimum (no underdog lottery bets) |
| Will Flavio Bolsonaro win the most votes in the se | Geopolitics | NO | `92.7%` | `87.0%` | `+5.7 п.п.` | `2.00%` | REJECTED: Max open positions (4) reached |
| Will Bitcoin reach $82,000 October 19-25? | Crypto | YES | `27.2%` | `16.0%` | `+11.2 п.п.` | `1.74%` | REJECTED: Win probability 27.2% < 92% minimum (no underdog lottery bets) |
| Will Lamine Yamal win the 2026 Ballon d'Or? | Other | YES | `23.1%` | `10.7%` | `+12.4 п.п.` | `0.10%` | REJECTED: Win probability 23.1% < 92% minimum (no underdog lottery bets) |
| Will the price of Bitcoin be above $78,000 on Octo | Crypto | NO | `21.4%` | `12.6%` | `+8.8 п.п.` | `1.50%` | REJECTED: Win probability 21.4% < 92% minimum (no underdog lottery bets) |
| Will US Lecce win on 2026-10-25? | Sports | YES | `19.0%` | `14.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Win probability 19.0% < 92% minimum (no underdog lottery bets) |
| FC Barcelona vs. Real Madrid CF: O/U 6.5 | Sports | YES | `23.2%` | `15.0%` | `+8.2 п.п.` | `1.00%` | REJECTED: Win probability 23.2% < 92% minimum (no underdog lottery bets) |
| Will Bitcoin reach $82,000 on October 25? | Crypto | YES | `27.8%` | `14.0%` | `+13.8 п.п.` | `1.00%` | REJECTED: Win probability 27.8% < 92% minimum (no underdog lottery bets) |
| Will the price of Bitcoin be above $82,000 on Octo | Crypto | YES | `20.2%` | `14.0%` | `+6.2 п.п.` | `1.00%` | REJECTED: Win probability 20.2% < 92% minimum (no underdog lottery bets) |
| Exact Score: FC Barcelona 2 - 1 Real Madrid CF? | Other | YES | `14.0%` | `9.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Win probability 14.0% < 92% minimum (no underdog lottery bets) |
