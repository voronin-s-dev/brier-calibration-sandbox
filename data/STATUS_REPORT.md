# 📊 Отчёт симулятора Polymarket (Устав Grok Bot — Демо-счёт)
**Обновлено:** `2026-10-26 21:33:26 UTC`

## 💰 Состояние виртуального портфеля
| Показатель | Значение | Правило устава |
| :--- | :--- | :--- |
| **Стартовый капитал** | `$50.00 USDC` | Не добавлять деньги |
| **Текущий баланс (Equity)** | **`$34.31 USDC`** (`-15.69$` / `-31.38%`) | Cash + Mark-to-Market по CLOB Bid |
| **Свободный кэш / В сделках** | `$12.89` / `$21.42 USDC` | До 8 открытых позиций, макс 8% банка |
| **Цель окупаемости подписки** | `$-15.69 / $60.00` (`0.0%`) | Цель: +$60.00 в месяц |
| **Просадка от пика (Текущая / Макс)** | `0.14%` / `6.31%` (Пик: `$34.36`) | Стоп-кран при просадке 40% |
| **Закрытых сделок / Win Rate** | `62` / `56.5%` | Brier Score: `0.1778` |

## 📂 Открытые позиции (5 / 8)
| # | Рынок | Кат. | Исход | Вход (Ask VWAP) | Текущий Bid | Оценка бота | Размер ($) | Нереализ. PnL | Источник |
| :- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| #51 | Will there be no change in Fed interest rates after the | Macro | **YES** | `0.940` | `0.928` | `96.5%` | `$3.67` | `$-0.05` | https://www.federalreserve.gov |
| #52 | Will the Fed increase interest rates by 25 bps after th | Macro | **NO** | `0.960` | `0.930` | `87.0%` | `$3.70` | `$-0.12` | https://www.federalreserve.gov |
| #59 | Israel x Iran ceasefire continues through October 27? | Geopolitics | **YES** | `0.940` | `0.968` | `98.0%` | `$4.69` | `$+0.14` | the totality of information av |
| #66 | Pacers vs. Bucks: O/U 212.5 | Sports | **YES** | `0.960` | `0.920` | `96.5%` | `$5.06` | `$-0.21` | https://www.nba.com/ |
| #68 | Dota 2: BetBoom Team vs LEGION (BO3) - PARI Universe Gr | Sports | **YES** | `0.940` | `0.930` | `96.0%` | `$4.58` | `$-0.05` | https://www.dotabuff.com |

## 🔍 Последние проверенные кандидаты и фильтр стакана CLOB
| Рынок | Кат. | Сторона | Оценка бота | Цена Ask | Перекос (Edge) | Проскальзывание CLOB | Решение |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Spread: Eagles (-3.5) | Sports | NO | `97.5%` | `79.0%` | `+18.5 п.п.` | `1.00%` | REJECTED: Contract price $0.790 outside sweet spot [$0.84, $0.96] |
| Counter-Strike: Envy vs GamerLegion (BO3) - Tesla  | Sports | YES | `65.1%` | `60.0%` | `+5.1 п.п.` | `2.00%` | REJECTED: Win probability 65.1% < 92% minimum (no underdog lottery bets) |
| Games Total: O/U 2.5 | Sports | YES | `1.5%` | `100.0%` | `-98.5 п.п.` | `100.00%` | REJECTED: Edge -98.5 pp < 2 pp threshold (P_est=1.5% vs AskVWAP=100.0%) |
| Game Handicap: TSW (-1.5) vs LOS (+1.5) | Sports | YES | `1.5%` | `100.0%` | `-98.5 п.п.` | `100.00%` | REJECTED: Edge -98.5 pp < 2 pp threshold (P_est=1.5% vs AskVWAP=100.0%) |
| Spread: Pacers (-4.5) | Sports | NO | `97.5%` | `51.0%` | `+46.5 п.п.` | `1.00%` | REJECTED: Contract price $0.510 outside sweet spot [$0.84, $0.96] |
| Spread: Cavaliers (-3.5) | Sports | NO | `97.5%` | `47.0%` | `+50.5 п.п.` | `1.00%` | REJECTED: Contract price $0.470 outside sweet spot [$0.84, $0.96] |
| Spread: Heat (-7.5) | Sports | YES | `56.0%` | `51.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Win probability 56.0% < 92% minimum (no underdog lottery bets) |
| Spread: Cavaliers (-4.5) | Sports | NO | `97.5%` | `51.0%` | `+46.5 п.п.` | `1.18%` | REJECTED: Contract price $0.510 outside sweet spot [$0.84, $0.96] |
| Spread: Cowboys (-4.5) | Sports | NO | `97.5%` | `52.0%` | `+45.5 п.п.` | `1.00%` | REJECTED: Contract price $0.520 outside sweet spot [$0.84, $0.96] |
| Mavericks vs. Heat | Sports | YES | `35.0%` | `30.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Win probability 35.0% < 92% minimum (no underdog lottery bets) |
| Grizzlies vs. Jazz | Sports | YES | `56.0%` | `51.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Win probability 56.0% < 92% minimum (no underdog lottery bets) |
| Cowboys vs. Eagles | Sports | YES | `72.0%` | `67.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Win probability 72.0% < 92% minimum (no underdog lottery bets) |
| Spread: Rockets (-4.5) | Sports | NO | `97.5%` | `50.0%` | `+47.5 п.п.` | `1.00%` | REJECTED: Contract price $0.500 outside sweet spot [$0.84, $0.96] |
| Suns vs. Thunder | Sports | NO | `81.0%` | `76.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Win probability 81.0% < 92% minimum (no underdog lottery bets) |
| LoL: Team Liquid vs Anyone's Legend (BO3) - Worlds | Sports | YES | `64.6%` | `56.0%` | `+8.6 п.п.` | `1.00%` | REJECTED: Win probability 64.6% < 92% minimum (no underdog lottery bets) |
| LoL: LOS vs Team Secret Whales (BO3) - Worlds Grou | Sports | NO | `1.5%` | `100.0%` | `-98.5 п.п.` | `100.00%` | REJECTED: Edge -98.5 pp < 2 pp threshold (P_est=1.5% vs AskVWAP=100.0%) |
| LoL: LOS vs Team Secret Whales - Game 2 Winner | Sports | NO | `1.5%` | `100.0%` | `-98.5 п.п.` | `100.00%` | REJECTED: Edge -98.5 pp < 2 pp threshold (P_est=1.5% vs AskVWAP=100.0%) |
| Dota 2: BetBoom Team vs LEGION (BO3) - PARI Univer | Sports | YES | `96.0%` | `94.0%` | `+2.0 п.п.` | `1.00%` | EXECUTED BUY #68 ($4.58 @ 0.9400) |
