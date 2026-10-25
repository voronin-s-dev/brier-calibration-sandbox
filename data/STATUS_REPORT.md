# 📊 Отчёт симулятора Polymarket (Устав Grok Bot — Демо-счёт)
**Обновлено:** `2026-10-25 17:02:37 UTC`

## 💰 Состояние виртуального портфеля
| Показатель | Значение | Правило устава |
| :--- | :--- | :--- |
| **Стартовый капитал** | `$50.00 USDC` | Не добавлять деньги |
| **Текущий баланс (Equity)** | **`$31.34 USDC`** (`-18.66$` / `-37.31%`) | Cash + Mark-to-Market по CLOB Bid |
| **Свободный кэш / В сделках** | `$16.39` / `$14.95 USDC` | До 8 открытых позиций, макс 8% банка |
| **Цель окупаемости подписки** | `$-18.66 / $60.00` (`0.0%`) | Цель: +$60.00 в месяц |
| **Просадка от пика (Текущая / Макс)** | `0.10%` / `6.31%` (Пик: `$31.38`) | Стоп-кран при просадке 40% |
| **Закрытых сделок / Win Rate** | `51` / `47.1%` | Brier Score: `0.2418` |

## 📂 Открытые позиции (4 / 8)
| # | Рынок | Кат. | Исход | Вход (Ask VWAP) | Текущий Bid | Оценка бота | Размер ($) | Нереализ. PnL | Источник |
| :- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| #51 | Will there be no change in Fed interest rates after the | Macro | **YES** | `0.940` | `0.940` | `96.5%` | `$3.67` | `$+0.00` | https://www.federalreserve.gov |
| #52 | Will the Fed increase interest rates by 25 bps after th | Macro | **NO** | `0.960` | `0.940` | `98.0%` | `$3.70` | `$-0.08` | https://www.federalreserve.gov |
| #53 | Will Flávio Bolsonaro win the second round of the 2026  | Geopolitics | **NO** | `0.939` | `0.957` | `98.5%` | `$3.71` | `$+0.07` | the margin of victory between  |
| #55 | Will Bitcoin dip to $78,000 October 19-25? | Crypto | **NO** | `0.948` | `0.981` | `98.5%` | `$3.75` | `$+0.13` | https://www.binance.com/en/tra |

## 🔍 Последние проверенные кандидаты и фильтр стакана CLOB
| Рынок | Кат. | Сторона | Оценка бота | Цена Ask | Перекос (Edge) | Проскальзывание CLOB | Решение |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Exact Score: FC Barcelona 3 - 1 Real Madrid CF? | Other | NO | `98.5%` | `93.0%` | `+5.5 п.п.` | `1.00%` | REJECTED: Max open positions (4) reached |
| Udinese Calcio vs. AC Milan: O/U 0.5 | Sports | NO | `11.5%` | `7.0%` | `+4.5 п.п.` | `1.00%` | REJECTED: Win probability 11.5% < 92% minimum (no underdog lottery bets) |
| Exact Score: FC Barcelona 3 - 2 Real Madrid CF? | Other | NO | `98.5%` | `93.9%` | `+4.6 п.п.` | `0.30%` | REJECTED: Max open positions (4) reached |
| Will Bitcoin reach $83,000 on October 25? | Crypto | YES | `8.4%` | `4.0%` | `+4.4 п.п.` | `0.35%` | REJECTED: Win probability 8.4% < 92% minimum (no underdog lottery bets) |
| Will the price of Bitcoin be above $84,000 on Octo | Crypto | YES | `15.8%` | `11.0%` | `+4.8 п.п.` | `2.00%` | REJECTED: Win probability 15.8% < 92% minimum (no underdog lottery bets) |
| Will the price of Bitcoin be above $78,000 on Octo | Crypto | NO | `10.0%` | `3.6%` | `+6.4 п.п.` | `0.20%` | REJECTED: Win probability 10.0% < 92% minimum (no underdog lottery bets) |
| Will Elon Musk post 360-379 tweets from October 20 | Geopolitics | YES | `20.3%` | `13.8%` | `+6.5 п.п.` | `0.40%` | REJECTED: Win probability 20.3% < 92% minimum (no underdog lottery bets) |
| Will the price of Bitcoin be above $76,000 on Octo | Crypto | NO | `9.7%` | `4.5%` | `+5.2 п.п.` | `1.24%` | REJECTED: Win probability 9.7% < 92% minimum (no underdog lottery bets) |
| Spread: Chiefs (-14.5) | Sports | YES | `15.5%` | `11.0%` | `+4.5 п.п.` | `1.00%` | REJECTED: Win probability 15.5% < 92% minimum (no underdog lottery bets) |
| Will Ilija Srdanović be the next prime minister of | Geopolitics | NO | `95.0%` | `90.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Max open positions (4) reached |
| Will the price of Bitcoin be above $78,000 on Octo | Crypto | NO | `22.8%` | `15.0%` | `+7.8 п.п.` | `2.40%` | REJECTED: Win probability 22.8% < 92% minimum (no underdog lottery bets) |
| Will Lamine Yamal win the 2026 Ballon d'Or? | Other | YES | `24.9%` | `12.5%` | `+12.4 п.п.` | `0.50%` | REJECTED: Win probability 24.9% < 92% minimum (no underdog lottery bets) |
| Spread: FC Barcelona (-3.5) | Sports | NO | `97.5%` | `90.0%` | `+7.5 п.п.` | `1.00%` | REJECTED: Max open positions (4) reached |
| Exact Score: FC Barcelona 3 - 2 Real Madrid CF? | Other | NO | `98.5%` | `93.9%` | `+4.6 п.п.` | `0.20%` | REJECTED: Max open positions (4) reached |
| Will Bitcoin reach $83,000 on October 25? | Crypto | YES | `8.3%` | `3.1%` | `+5.2 п.п.` | `0.45%` | REJECTED: Win probability 8.3% < 92% minimum (no underdog lottery bets) |
| Will the price of Bitcoin be above $84,000 on Octo | Crypto | YES | `15.3%` | `10.0%` | `+5.3 п.п.` | `2.00%` | REJECTED: Win probability 15.3% < 92% minimum (no underdog lottery bets) |
| Will Bitcoin reach $82,000 on October 25? | Crypto | YES | `27.6%` | `14.0%` | `+13.6 п.п.` | `1.00%` | REJECTED: Win probability 27.6% < 92% minimum (no underdog lottery bets) |
| Will the price of Bitcoin be above $76,000 on Octo | Crypto | NO | `9.8%` | `4.9%` | `+4.9 п.п.` | `1.16%` | REJECTED: Win probability 9.8% < 92% minimum (no underdog lottery bets) |
