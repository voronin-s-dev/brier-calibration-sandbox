# 📊 Отчёт симулятора Polymarket (Устав Grok Bot — Демо-счёт)
**Обновлено:** `2026-10-26 21:42:56 UTC`

## 💰 Состояние виртуального портфеля
| Показатель | Значение | Правило устава |
| :--- | :--- | :--- |
| **Стартовый капитал** | `$50.00 USDC` | Не добавлять деньги |
| **Текущий баланс (Equity)** | **`$34.42 USDC`** (`-15.58$` / `-31.16%`) | Cash + Mark-to-Market по CLOB Bid |
| **Свободный кэш / В сделках** | `$7.71` / `$26.71 USDC` | До 8 открытых позиций, макс 8% банка |
| **Цель окупаемости подписки** | `$-15.58 / $60.00` (`0.0%`) | Цель: +$60.00 в месяц |
| **Просадка от пика (Текущая / Макс)** | `0.32%` / `6.31%` (Пик: `$34.53`) | Стоп-кран при просадке 40% |
| **Закрытых сделок / Win Rate** | `62` / `56.5%` | Brier Score: `0.1778` |

## 📂 Открытые позиции (6 / 8)
| # | Рынок | Кат. | Исход | Вход (Ask VWAP) | Текущий Bid | Оценка бота | Размер ($) | Нереализ. PnL | Источник |
| :- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| #51 | Will there be no change in Fed interest rates after the | Macro | **YES** | `0.940` | `0.930` | `96.5%` | `$3.67` | `$-0.04` | https://www.federalreserve.gov |
| #52 | Will the Fed increase interest rates by 25 bps after th | Macro | **NO** | `0.960` | `0.930` | `87.0%` | `$3.70` | `$-0.12` | https://www.federalreserve.gov |
| #59 | Israel x Iran ceasefire continues through October 27? | Geopolitics | **YES** | `0.940` | `0.971` | `98.0%` | `$4.69` | `$+0.15` | the totality of information av |
| #66 | Pacers vs. Bucks: O/U 212.5 | Sports | **YES** | `0.960` | `0.920` | `96.5%` | `$5.06` | `$-0.21` | https://www.nba.com/ |
| #68 | Dota 2: BetBoom Team vs LEGION (BO3) - PARI Universe Gr | Sports | **YES** | `0.940` | `0.970` | `98.5%` | `$4.58` | `$+0.15` | https://www.dotabuff.com |
| #69 | Valorant: G2 Gozen vs Team Liquid Brazil (BO3) - VCT Ga | Sports | **NO** | `0.940` | `0.920` | `98.0%` | `$5.18` | `$-0.11` | https://vlr.gg |

## 🔍 Последние проверенные кандидаты и фильтр стакана CLOB
| Рынок | Кат. | Сторона | Оценка бота | Цена Ask | Перекос (Edge) | Проскальзывание CLOB | Решение |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Counter-Strike: Envy vs GamerLegion (BO3) - Tesla  | Sports | YES | `63.6%` | `58.0%` | `+5.6 п.п.` | `2.00%` | REJECTED: Win probability 63.6% < 92% minimum (no underdog lottery bets) |
| Spread: Eagles (-3.5) | Sports | NO | `97.5%` | `79.0%` | `+18.5 п.п.` | `1.00%` | REJECTED: Contract price $0.790 outside sweet spot [$0.84, $0.96] |
| Counter-Strike: Nuclear TigeRES vs UNiTY esports ( | Sports | NO | `1.5%` | `100.0%` | `-98.5 п.п.` | `100.00%` | REJECTED: Edge -98.5 pp < 2 pp threshold (P_est=1.5% vs AskVWAP=100.0%) |
| Counter-Strike: Inner Circle Esports vs Team Nemes | Sports | YES | `78.3%` | `74.0%` | `+4.3 п.п.` | `2.00%` | REJECTED: Win probability 78.3% < 92% minimum (no underdog lottery bets) |
| Spread: Pacers (-4.5) | Sports | NO | `97.5%` | `51.0%` | `+46.5 п.п.` | `1.00%` | REJECTED: Contract price $0.510 outside sweet spot [$0.84, $0.96] |
| Spread: Cavaliers (-3.5) | Sports | NO | `97.5%` | `49.0%` | `+48.5 п.п.` | `1.00%` | REJECTED: Contract price $0.490 outside sweet spot [$0.84, $0.96] |
| Cowboys vs. Eagles: O/U 44.5 | Sports | YES | `51.7%` | `46.7%` | `+5.0 п.п.` | `0.10%` | REJECTED: Win probability 51.7% < 92% minimum (no underdog lottery bets) |
| Spread: Heat (-7.5) | Sports | YES | `56.0%` | `51.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Win probability 56.0% < 92% minimum (no underdog lottery bets) |
| Spread: Cavaliers (-4.5) | Sports | NO | `97.5%` | `53.0%` | `+44.5 п.п.` | `1.00%` | REJECTED: Contract price $0.530 outside sweet spot [$0.84, $0.96] |
| Spread: Cowboys (-4.5) | Sports | NO | `97.5%` | `52.0%` | `+45.5 п.п.` | `1.00%` | REJECTED: Contract price $0.520 outside sweet spot [$0.84, $0.96] |
| Game Handicap: AL (-1.5) vs Team Liquid (+1.5) | Sports | YES | `1.5%` | `100.0%` | `-98.5 п.п.` | `100.00%` | REJECTED: Edge -98.5 pp < 2 pp threshold (P_est=1.5% vs AskVWAP=100.0%) |
| Warriors vs. Nuggets | Sports | YES | `34.0%` | `29.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Win probability 34.0% < 92% minimum (no underdog lottery bets) |
| Mavericks vs. Heat | Sports | YES | `35.0%` | `30.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Win probability 35.0% < 92% minimum (no underdog lottery bets) |
| Grizzlies vs. Jazz | Sports | YES | `59.3%` | `51.0%` | `+8.3 п.п.` | `1.00%` | REJECTED: Win probability 59.3% < 92% minimum (no underdog lottery bets) |
| Cowboys vs. Eagles | Sports | YES | `72.0%` | `67.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Win probability 72.0% < 92% minimum (no underdog lottery bets) |
| Spread: Rockets (-4.5) | Sports | NO | `97.5%` | `50.0%` | `+47.5 п.п.` | `1.00%` | REJECTED: Contract price $0.500 outside sweet spot [$0.84, $0.96] |
| Suns vs. Thunder | Sports | NO | `81.0%` | `76.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Win probability 81.0% < 92% minimum (no underdog lottery bets) |
| LoL: Team Liquid vs Anyone's Legend (BO3) - Worlds | Sports | YES | `68.7%` | `60.0%` | `+8.6 п.п.` | `1.00%` | REJECTED: Win probability 68.7% < 92% minimum (no underdog lottery bets) |
