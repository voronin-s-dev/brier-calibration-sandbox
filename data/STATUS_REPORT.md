# 📊 Отчёт симулятора Polymarket (Устав Grok Bot — Демо-счёт)
**Обновлено:** `2026-10-26 00:05:59 UTC`

## 💰 Состояние виртуального портфеля
| Показатель | Значение | Правило устава |
| :--- | :--- | :--- |
| **Стартовый капитал** | `$50.00 USDC` | Не добавлять деньги |
| **Текущий баланс (Equity)** | **`$31.83 USDC`** (`-18.17$` / `-36.35%`) | Cash + Mark-to-Market по CLOB Bid |
| **Свободный кэш / В сделках** | `$5.10` / `$26.73 USDC` | До 8 открытых позиций, макс 8% банка |
| **Цель окупаемости подписки** | `$-18.17 / $60.00` (`0.0%`) | Цель: +$60.00 в месяц |
| **Просадка от пика (Текущая / Макс)** | `1.57%` / `6.31%` (Пик: `$32.34`) | Стоп-кран при просадке 40% |
| **Закрытых сделок / Win Rate** | `54` / `50.0%` | Brier Score: `0.2219` |

## 📂 Открытые позиции (7 / 8)
| # | Рынок | Кат. | Исход | Вход (Ask VWAP) | Текущий Bid | Оценка бота | Размер ($) | Нереализ. PnL | Источник |
| :- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| #51 | Will there be no change in Fed interest rates after the | Macro | **YES** | `0.940` | `0.940` | `96.5%` | `$3.67` | `$+0.00` | https://www.federalreserve.gov |
| #52 | Will the Fed increase interest rates by 25 bps after th | Macro | **NO** | `0.960` | `0.940` | `98.0%` | `$3.70` | `$-0.08` | https://www.federalreserve.gov |
| #55 | Will Bitcoin dip to $78,000 October 19-25? | Crypto | **NO** | `0.948` | `0.967` | `98.5%` | `$3.75` | `$+0.08` | https://www.binance.com/en/tra |
| #59 | Israel x Iran ceasefire continues through October 27? | Geopolitics | **YES** | `0.940` | `0.910` | `95.0%` | `$4.69` | `$-0.15` | the totality of information av |
| #60 | Clippers vs. Thunder | Sports | **NO** | `0.910` | `0.820` | `94.0%` | `$4.08` | `$-0.40` | https://www.nba.com/ |
| #61 | Will the price of Bitcoin be above $78,000 on October 2 | Crypto | **YES** | `0.940` | `0.922` | `97.0%` | `$4.58` | `$-0.09` | https://www.binance.com/en/tra |
| #62 | Will Elon Musk post 115-139 tweets from October 24 to O | Geopolitics | **NO** | `0.929` | `0.932` | `96.0%` | `$2.89` | `$+0.01` | https://x.com/elonmusk |

## 🔍 Последние проверенные кандидаты и фильтр стакана CLOB
| Рынок | Кат. | Сторона | Оценка бота | Цена Ask | Перекос (Edge) | Проскальзывание CLOB | Решение |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Hawks vs. Rockets | Sports | YES | `40.0%` | `35.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Win probability 40.0% < 92% minimum (no underdog lottery bets) |
| Spread: Hornets (-1.5) | Sports | YES | `61.1%` | `56.0%` | `+5.1 п.п.` | `1.00%` | REJECTED: Win probability 61.1% < 92% minimum (no underdog lottery bets) |
| Counter-Strike: Spirit vs FURIA (BO3) - PGL Master | Sports | YES | `70.0%` | `65.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Win probability 70.0% < 92% minimum (no underdog lottery bets) |
| Counter-Strike: 9z vs TYLOO (BO3) - PGL Masters Bu | Sports | YES | `86.1%` | `75.0%` | `+11.1 п.п.` | `1.43%` | REJECTED: Win probability 86.1% < 92% minimum (no underdog lottery bets) |
| Map Handicap: 9z (-1.5) vs TYLOO (+1.5) | Sports | YES | `57.2%` | `52.0%` | `+5.2 п.п.` | `2.00%` | REJECTED: Win probability 57.2% < 92% minimum (no underdog lottery bets) |
| LoL: Team Liquid vs Anyone's Legend (BO3) - Worlds | Sports | NO | `79.8%` | `71.0%` | `+8.8 п.п.` | `1.00%` | REJECTED: Win probability 79.8% < 92% minimum (no underdog lottery bets) |
| Counter-Strike: BetBoom Team vs Natus Vincere (BO3 | Sports | NO | `68.9%` | `63.0%` | `+5.9 п.п.` | `1.00%` | REJECTED: Win probability 68.9% < 92% minimum (no underdog lottery bets) |
| Dota 2: OG vs GamerLegion (BO3) - PARI Universe Gr | Sports | NO | `50.3%` | `45.0%` | `+5.3 п.п.` | `1.00%` | REJECTED: Win probability 50.3% < 92% minimum (no underdog lottery bets) |
| LoL: LOS vs Team Secret Whales (BO3) - Worlds Grou | Sports | NO | `71.0%` | `66.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Win probability 71.0% < 92% minimum (no underdog lottery bets) |
| Warriors vs. Nuggets | Sports | YES | `33.0%` | `28.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Win probability 33.0% < 92% minimum (no underdog lottery bets) |
| Counter-Strike: TheMongolz vs MOUZ (BO3) - PGL Mas | Sports | YES | `32.0%` | `27.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Win probability 32.0% < 92% minimum (no underdog lottery bets) |
| Will AS Roma win on 2026-10-27? | Sports | YES | `78.0%` | `73.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Win probability 78.0% < 92% minimum (no underdog lottery bets) |
| Counter-Strike: Imperial vs paiN - Map 1 Winner | Sports | NO | `1.5%` | `100.0%` | `-98.5 п.п.` | `100.00%` | REJECTED: Edge -98.5 pp < 2 pp threshold (P_est=1.5% vs AskVWAP=100.0%) |
| Maple Leafs vs. Flames | Sports | YES | `63.0%` | `58.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Win probability 63.0% < 92% minimum (no underdog lottery bets) |
| Counter-Strike: Vitality vs FUT Esports (BO3) - PG | Sports | YES | `83.6%` | `75.0%` | `+8.6 п.п.` | `1.00%` | REJECTED: Win probability 83.6% < 92% minimum (no underdog lottery bets) |
| Spread: Grizzlies (-4.5) | Sports | NO | `97.5%` | `55.0%` | `+42.5 п.п.` | `1.00%` | REJECTED: Contract price $0.550 outside sweet spot [$0.84, $0.96] |
| LoL: Karmine Corp vs Bilibili Gaming (BO1) - World | Sports | YES | `38.7%` | `30.0%` | `+8.7 п.п.` | `1.00%` | REJECTED: Win probability 38.7% < 92% minimum (no underdog lottery bets) |
| Spread: Grizzlies (-3.5) | Sports | NO | `97.5%` | `51.0%` | `+46.5 п.п.` | `1.00%` | REJECTED: Contract price $0.510 outside sweet spot [$0.84, $0.96] |
