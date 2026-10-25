# 📊 Отчёт симулятора Polymarket (Устав Grok Bot — Демо-счёт)
**Обновлено:** `2026-10-25 18:45:57 UTC`

## 💰 Состояние виртуального портфеля
| Показатель | Значение | Правило устава |
| :--- | :--- | :--- |
| **Стартовый капитал** | `$50.00 USDC` | Не добавлять деньги |
| **Текущий баланс (Equity)** | **`$31.15 USDC`** (`-18.85$` / `-37.70%`) | Cash + Mark-to-Market по CLOB Bid |
| **Свободный кэш / В сделках** | `$2.31` / `$28.84 USDC` | До 8 открытых позиций, макс 8% банка |
| **Цель окупаемости подписки** | `$-18.85 / $60.00` (`0.0%`) | Цель: +$60.00 в месяц |
| **Просадка от пика (Текущая / Макс)** | `0.71%` / `6.31%` (Пик: `$31.38`) | Стоп-кран при просадке 40% |
| **Закрытых сделок / Win Rate** | `51` / `47.1%` | Brier Score: `0.2418` |

## 📂 Открытые позиции (7 / 8)
| # | Рынок | Кат. | Исход | Вход (Ask VWAP) | Текущий Bid | Оценка бота | Размер ($) | Нереализ. PnL | Источник |
| :- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| #51 | Will there be no change in Fed interest rates after the | Macro | **YES** | `0.940` | `0.940` | `96.5%` | `$3.67` | `$+0.00` | https://www.federalreserve.gov |
| #52 | Will the Fed increase interest rates by 25 bps after th | Macro | **NO** | `0.960` | `0.940` | `98.0%` | `$3.70` | `$-0.08` | https://www.federalreserve.gov |
| #53 | Will Flávio Bolsonaro win the second round of the 2026  | Geopolitics | **NO** | `0.939` | `0.958` | `98.5%` | `$3.71` | `$+0.08` | the margin of victory between  |
| #55 | Will Bitcoin dip to $78,000 October 19-25? | Crypto | **NO** | `0.948` | `0.983` | `98.5%` | `$3.75` | `$+0.14` | https://www.binance.com/en/tra |
| #56 | Spread: FC Barcelona (-3.5) | Sports | **NO** | `0.880` | `0.870` | `97.5%` | `$4.70` | `$-0.05` | https://www.laliga.com/ |
| #58 | LoL: Gen.G vs LYON (BO3) - Worlds Group Stage | Sports | **YES** | `0.920` | `0.910` | `95.0%` | `$4.69` | `$-0.05` | https://gol.gg/esports/home |
| #59 | Israel x Iran ceasefire continues through October 27? | Geopolitics | **YES** | `0.940` | `0.920` | `96.5%` | `$4.69` | `$-0.10` | the totality of information av |

## 🔍 Последние проверенные кандидаты и фильтр стакана CLOB
| Рынок | Кат. | Сторона | Оценка бота | Цена Ask | Перекос (Edge) | Проскальзывание CLOB | Решение |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Will the price of Bitcoin be above $84,000 on Octo | Crypto | YES | `16.1%` | `9.0%` | `+7.1 п.п.` | `1.00%` | REJECTED: Max open positions (8) reached |
| Will Bitcoin reach $83,000 on October 25? | Crypto | YES | `7.7%` | `2.1%` | `+5.6 п.п.` | `0.17%` | REJECTED: Max open positions (8) reached |
| Exact Score: FC Barcelona 3 - 1 Real Madrid CF? | Other | NO | `98.5%` | `93.0%` | `+5.5 п.п.` | `1.00%` | REJECTED: Max open positions (8) reached |
| Exact Score: FC Barcelona 2 - 2 Real Madrid CF? | Other | NO | `98.5%` | `94.3%` | `+4.2 п.п.` | `0.20%` | REJECTED: Max open positions (8) reached |
| Will the price of Bitcoin be above $76,000 on Octo | Crypto | NO | `8.8%` | `4.5%` | `+4.3 п.п.` | `1.10%` | REJECTED: Max open positions (8) reached |
| Exact Score: FC Barcelona 3 - 2 Real Madrid CF? | Other | NO | `98.5%` | `94.2%` | `+4.3 п.п.` | `0.40%` | REJECTED: Max open positions (8) reached |
| Will Bitcoin reach $82,000 on October 25? | Crypto | YES | `28.2%` | `12.0%` | `+16.2 п.п.` | `1.00%` | REJECTED: Max open positions (8) reached |
| Will the price of Bitcoin be above $78,000 on Octo | Crypto | NO | `21.5%` | `13.8%` | `+7.7 п.п.` | `1.20%` | REJECTED: Max open positions (8) reached |
| Will Dejan Šoškić be the next Prime Minister of Se | Geopolitics | NO | `90.6%` | `86.2%` | `+4.4 п.п.` | `4.90%` | REJECTED: Max open positions (8) reached |
| Will Bitcoin reach $82,000 October 19-25? | Crypto | YES | `28.3%` | `12.0%` | `+16.3 п.п.` | `1.00%` | REJECTED: Max open positions (8) reached |
| Will Naftali Bennett be the next Prime Minister of | Geopolitics | YES | `20.0%` | `15.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Max open positions (8) reached |
| Israel x Iran ceasefire continues through October  | Geopolitics | YES | `96.5%` | `94.0%` | `+2.5 п.п.` | `2.00%` | EXECUTED BUY #59 ($4.69 @ 0.9400) |
| LoL: Gen.G vs LYON (BO3) - Worlds Group Stage | Sports | YES | `95.0%` | `92.0%` | `+3.0 п.п.` | `1.00%` | EXECUTED BUY #58 ($4.69 @ 0.9200) |
| Will Lamine Yamal win the 2026 Ballon d'Or? | Other | YES | `17.1%` | `11.7%` | `+5.4 п.п.` | `0.20%` | EXECUTED BUY #57 ($1.00 @ 0.1170) |
| Spread: FC Barcelona (-3.5) | Sports | NO | `97.5%` | `88.0%` | `+9.5 п.п.` | `1.00%` | EXECUTED BUY #56 ($4.70 @ 0.8800) |
| Exact Score: FC Barcelona 3 - 1 Real Madrid CF? | Other | NO | `98.5%` | `93.0%` | `+5.5 п.п.` | `1.00%` | REJECTED: Max open positions (4) reached |
| Udinese Calcio vs. AC Milan: O/U 0.5 | Sports | NO | `11.5%` | `7.0%` | `+4.5 п.п.` | `1.00%` | REJECTED: Win probability 11.5% < 92% minimum (no underdog lottery bets) |
| Exact Score: FC Barcelona 3 - 2 Real Madrid CF? | Other | NO | `98.5%` | `93.9%` | `+4.6 п.п.` | `0.30%` | REJECTED: Max open positions (4) reached |
