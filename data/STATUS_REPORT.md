# 📊 Отчёт симулятора Polymarket (Устав Grok Bot — Демо-счёт)
**Обновлено:** `2026-10-26 00:15:24 UTC`

## 💰 Состояние виртуального портфеля
| Показатель | Значение | Правило устава |
| :--- | :--- | :--- |
| **Стартовый капитал** | `$50.00 USDC` | Не добавлять деньги |
| **Текущий баланс (Equity)** | **`$31.93 USDC`** (`-18.07$` / `-36.15%`) | Cash + Mark-to-Market по CLOB Bid |
| **Свободный кэш / В сделках** | `$0.30` / `$31.63 USDC` | До 8 открытых позиций, макс 8% банка |
| **Цель окупаемости подписки** | `$-18.07 / $60.00` (`0.0%`) | Цель: +$60.00 в месяц |
| **Просадка от пика (Текущая / Макс)** | `1.27%` / `6.31%` (Пик: `$32.34`) | Стоп-кран при просадке 40% |
| **Закрытых сделок / Win Rate** | `54` / `50.0%` | Brier Score: `0.2219` |

## 📂 Открытые позиции (8 / 8)
| # | Рынок | Кат. | Исход | Вход (Ask VWAP) | Текущий Bid | Оценка бота | Размер ($) | Нереализ. PnL | Источник |
| :- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| #51 | Will there be no change in Fed interest rates after the | Macro | **YES** | `0.940` | `0.940` | `96.5%` | `$3.67` | `$+0.00` | https://www.federalreserve.gov |
| #52 | Will the Fed increase interest rates by 25 bps after th | Macro | **NO** | `0.960` | `0.940` | `98.0%` | `$3.70` | `$-0.08` | https://www.federalreserve.gov |
| #55 | Will Bitcoin dip to $78,000 October 19-25? | Crypto | **NO** | `0.948` | `0.972` | `98.5%` | `$3.75` | `$+0.09` | https://www.binance.com/en/tra |
| #59 | Israel x Iran ceasefire continues through October 27? | Geopolitics | **YES** | `0.940` | `0.910` | `95.5%` | `$4.69` | `$-0.15` | the totality of information av |
| #60 | Clippers vs. Thunder | Sports | **NO** | `0.910` | `0.830` | `94.0%` | `$4.08` | `$-0.36` | https://www.nba.com/ |
| #61 | Will the price of Bitcoin be above $78,000 on October 2 | Crypto | **YES** | `0.940` | `0.931` | `97.1%` | `$4.58` | `$-0.04` | https://www.binance.com/en/tra |
| #62 | Will Elon Musk post 115-139 tweets from October 24 to O | Geopolitics | **NO** | `0.929` | `0.942` | `98.0%` | `$2.89` | `$+0.04` | https://x.com/elonmusk |
| #63 | Counter-Strike: Imperial vs paiN (BO3) - Circuit X Curi | Sports | **YES** | `0.960` | `0.952` | `98.5%` | `$4.80` | `$-0.04` | https://hltv.org |

## 🔍 Последние проверенные кандидаты и фильтр стакана CLOB
| Рынок | Кат. | Сторона | Оценка бота | Цена Ask | Перекос (Edge) | Проскальзывание CLOB | Решение |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Hawks vs. Rockets | Sports | YES | `40.0%` | `35.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Win probability 40.0% < 92% minimum (no underdog lottery bets) |
| Spread: Hornets (-1.5) | Sports | YES | `61.0%` | `56.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Win probability 61.0% < 92% minimum (no underdog lottery bets) |
| Counter-Strike: Spirit vs FURIA (BO3) - PGL Master | Sports | YES | `70.0%` | `65.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Win probability 70.0% < 92% minimum (no underdog lottery bets) |
| Counter-Strike: 9z vs TYLOO (BO3) - PGL Masters Bu | Sports | YES | `86.2%` | `75.0%` | `+11.2 п.п.` | `1.00%` | REJECTED: Win probability 86.2% < 92% minimum (no underdog lottery bets) |
| LoL: Team Liquid vs Anyone's Legend (BO3) - Worlds | Sports | NO | `79.8%` | `71.0%` | `+8.8 п.п.` | `1.00%` | REJECTED: Win probability 79.8% < 92% minimum (no underdog lottery bets) |
| Timberwolves vs. Cavaliers | Sports | NO | `56.0%` | `51.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Win probability 56.0% < 92% minimum (no underdog lottery bets) |
| Map Handicap: 9z (-1.5) vs TYLOO (+1.5) | Sports | YES | `57.3%` | `51.0%` | `+6.3 п.п.` | `1.00%` | REJECTED: Win probability 57.3% < 92% minimum (no underdog lottery bets) |
| Counter-Strike: BetBoom Team vs Natus Vincere (BO3 | Sports | NO | `68.7%` | `63.0%` | `+5.7 п.п.` | `1.00%` | REJECTED: Win probability 68.7% < 92% minimum (no underdog lottery bets) |
| Dota 2: OG vs GamerLegion (BO3) - PARI Universe Gr | Sports | NO | `49.3%` | `45.0%` | `+4.3 п.п.` | `1.00%` | REJECTED: Win probability 49.3% < 92% minimum (no underdog lottery bets) |
| LoL: LOS vs Team Secret Whales (BO3) - Worlds Grou | Sports | NO | `71.0%` | `66.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Win probability 71.0% < 92% minimum (no underdog lottery bets) |
| Warriors vs. Nuggets | Sports | YES | `33.0%` | `28.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Win probability 33.0% < 92% minimum (no underdog lottery bets) |
| Counter-Strike: TheMongolz vs MOUZ (BO3) - PGL Mas | Sports | YES | `32.0%` | `27.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Win probability 32.0% < 92% minimum (no underdog lottery bets) |
| Will AS Roma win on 2026-10-27? | Sports | YES | `78.0%` | `73.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Win probability 78.0% < 92% minimum (no underdog lottery bets) |
| Maple Leafs vs. Flames | Sports | YES | `63.0%` | `58.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Win probability 63.0% < 92% minimum (no underdog lottery bets) |
| Counter-Strike: Vitality vs FUT Esports (BO3) - PG | Sports | YES | `83.5%` | `75.0%` | `+8.5 п.п.` | `1.00%` | REJECTED: Win probability 83.5% < 92% minimum (no underdog lottery bets) |
| LoL: Karmine Corp vs Bilibili Gaming (BO1) - World | Sports | YES | `39.0%` | `30.0%` | `+9.0 п.п.` | `1.00%` | REJECTED: Win probability 39.0% < 92% minimum (no underdog lottery bets) |
| Bulls vs. Celtics | Sports | NO | `91.0%` | `86.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Win probability 91.0% < 92% minimum (no underdog lottery bets) |
| Counter-Strike: Imperial vs paiN (BO3) - Circuit X | Sports | YES | `98.5%` | `96.0%` | `+2.5 п.п.` | `0.80%` | EXECUTED BUY #63 ($4.80 @ 0.9600) |
