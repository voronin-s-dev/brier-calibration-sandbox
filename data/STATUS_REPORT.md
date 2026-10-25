# 📊 Отчёт симулятора Polymarket (Устав Grok Bot — Демо-счёт)
**Обновлено:** `2026-10-25 19:30:35 UTC`

## 💰 Состояние виртуального портфеля
| Показатель | Значение | Правило устава |
| :--- | :--- | :--- |
| **Стартовый капитал** | `$50.00 USDC` | Не добавлять деньги |
| **Текущий баланс (Equity)** | **`$31.16 USDC`** (`-18.84$` / `-37.67%`) | Cash + Mark-to-Market по CLOB Bid |
| **Свободный кэш / В сделках** | `$2.31` / `$28.85 USDC` | До 8 открытых позиций, макс 8% банка |
| **Цель окупаемости подписки** | `$-18.84 / $60.00` (`0.0%`) | Цель: +$60.00 в месяц |
| **Просадка от пика (Текущая / Макс)** | `0.68%` / `6.31%` (Пик: `$31.38`) | Стоп-кран при просадке 40% |
| **Закрытых сделок / Win Rate** | `51` / `47.1%` | Brier Score: `0.2418` |

## 📂 Открытые позиции (7 / 8)
| # | Рынок | Кат. | Исход | Вход (Ask VWAP) | Текущий Bid | Оценка бота | Размер ($) | Нереализ. PnL | Источник |
| :- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| #51 | Will there be no change in Fed interest rates after the | Macro | **YES** | `0.940` | `0.940` | `96.5%` | `$3.67` | `$+0.00` | https://www.federalreserve.gov |
| #52 | Will the Fed increase interest rates by 25 bps after th | Macro | **NO** | `0.960` | `0.940` | `98.0%` | `$3.70` | `$-0.08` | https://www.federalreserve.gov |
| #53 | Will Flávio Bolsonaro win the second round of the 2026  | Geopolitics | **NO** | `0.939` | `0.962` | `98.5%` | `$3.71` | `$+0.09` | the margin of victory between  |
| #55 | Will Bitcoin dip to $78,000 October 19-25? | Crypto | **NO** | `0.948` | `0.982` | `98.5%` | `$3.75` | `$+0.13` | https://www.binance.com/en/tra |
| #56 | Spread: FC Barcelona (-3.5) | Sports | **NO** | `0.880` | `0.870` | `97.5%` | `$4.70` | `$-0.05` | https://www.laliga.com/ |
| #58 | LoL: Gen.G vs LYON (BO3) - Worlds Group Stage | Sports | **YES** | `0.920` | `0.910` | `95.0%` | `$4.69` | `$-0.05` | https://gol.gg/esports/home |
| #59 | Israel x Iran ceasefire continues through October 27? | Geopolitics | **YES** | `0.940` | `0.920` | `96.5%` | `$4.69` | `$-0.10` | the totality of information av |

## 🔍 Последние проверенные кандидаты и фильтр стакана CLOB
| Рынок | Кат. | Сторона | Оценка бота | Цена Ask | Перекос (Edge) | Проскальзывание CLOB | Решение |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Will Harry Kane win the 2026 Ballon d'Or? | Other | YES | `81.4%` | `71.7%` | `+9.7 п.п.` | `0.10%` | REJECTED: Win probability 81.4% < 92% minimum (no underdog lottery bets) |
| Will Benjamin Netanyahu be the next Prime Minister | Geopolitics | NO | `85.0%` | `74.0%` | `+11.0 п.п.` | `1.00%` | REJECTED: Win probability 85.0% < 92% minimum (no underdog lottery bets) |
| LoL: Dplus KIA vs Movistar KOI (BO3) - Worlds Grou | Sports | YES | `93.0%` | `88.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Available cash $2.31 below $1.00 minimum bet |
| LoL: Dplus KIA vs Movistar KOI - Game 1 Winner | Sports | YES | `93.0%` | `88.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Available cash $2.31 below $1.00 minimum bet |
| Will Flávio Bolsonaro win the 2026 Brazilian presi | Geopolitics | YES | `83.2%` | `77.8%` | `+5.3 п.п.` | `0.20%` | REJECTED: Win probability 83.2% < 92% minimum (no underdog lottery bets) |
| LoL: Top Esports vs G2 Esports (BO1) - Worlds Grou | Sports | NO | `1.5%` | `100.0%` | `-98.5 п.п.` | `100.00%` | REJECTED: Edge -98.5 pp < 2 pp threshold (P_est=1.5% vs AskVWAP=100.0%) |
| Will the price of Bitcoin be above $84,000 on Octo | Crypto | YES | `14.6%` | `8.0%` | `+6.7 п.п.` | `1.00%` | REJECTED: Win probability 14.6% < 92% minimum (no underdog lottery bets) |
| Will the price of Bitcoin be above $76,000 on Octo | Crypto | NO | `9.5%` | `3.7%` | `+5.7 п.п.` | `0.44%` | REJECTED: Win probability 9.5% < 92% minimum (no underdog lottery bets) |
| Will the price of Bitcoin be above $78,000 on Octo | Crypto | NO | `22.8%` | `13.8%` | `+9.0 п.п.` | `0.50%` | REJECTED: Win probability 22.8% < 92% minimum (no underdog lottery bets) |
| Will Kylian Mbappé win the 2026 Ballon d'Or? | Other | YES | `20.3%` | `14.9%` | `+5.4 п.п.` | `0.20%` | REJECTED: Win probability 20.3% < 92% minimum (no underdog lottery bets) |
| Will the price of Bitcoin be above $84,000 on Octo | Crypto | YES | `16.1%` | `9.0%` | `+7.1 п.п.` | `1.00%` | REJECTED: Max open positions (8) reached |
| Will Bitcoin reach $83,000 on October 25? | Crypto | YES | `7.7%` | `2.1%` | `+5.6 п.п.` | `0.17%` | REJECTED: Max open positions (8) reached |
| Exact Score: FC Barcelona 3 - 1 Real Madrid CF? | Other | NO | `98.5%` | `93.0%` | `+5.5 п.п.` | `1.00%` | REJECTED: Max open positions (8) reached |
| Exact Score: FC Barcelona 2 - 2 Real Madrid CF? | Other | NO | `98.5%` | `94.3%` | `+4.2 п.п.` | `0.20%` | REJECTED: Max open positions (8) reached |
| Will the price of Bitcoin be above $76,000 on Octo | Crypto | NO | `8.8%` | `4.5%` | `+4.3 п.п.` | `1.10%` | REJECTED: Max open positions (8) reached |
| Exact Score: FC Barcelona 3 - 2 Real Madrid CF? | Other | NO | `98.5%` | `94.2%` | `+4.3 п.п.` | `0.40%` | REJECTED: Max open positions (8) reached |
| Will Bitcoin reach $82,000 on October 25? | Crypto | YES | `28.2%` | `12.0%` | `+16.2 п.п.` | `1.00%` | REJECTED: Max open positions (8) reached |
| Will the price of Bitcoin be above $78,000 on Octo | Crypto | NO | `21.5%` | `13.8%` | `+7.7 п.п.` | `1.20%` | REJECTED: Max open positions (8) reached |
