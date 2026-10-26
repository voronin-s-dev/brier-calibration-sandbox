# 📊 Отчёт симулятора Polymarket (Устав Grok Bot — Демо-счёт)
**Обновлено:** `2026-10-26 21:52:25 UTC`

## 💰 Состояние виртуального портфеля
| Показатель | Значение | Правило устава |
| :--- | :--- | :--- |
| **Стартовый капитал** | `$50.00 USDC` | Не добавлять деньги |
| **Текущий баланс (Equity)** | **`$34.99 USDC`** (`-15.01$` / `-30.01%`) | Cash + Mark-to-Market по CLOB Bid |
| **Свободный кэш / В сделках** | `$18.09` / `$16.91 USDC` | До 8 открытых позиций, макс 8% банка |
| **Цель окупаемости подписки** | `$-15.01 / $60.00` (`0.0%`) | Цель: +$60.00 в месяц |
| **Просадка от пика (Текущая / Макс)** | `0.00%` / `6.31%` (Пик: `$34.99`) | Стоп-кран при просадке 40% |
| **Закрытых сделок / Win Rate** | `64` / `57.8%` | Brier Score: `0.1778` |

## 📂 Открытые позиции (4 / 8)
| # | Рынок | Кат. | Исход | Вход (Ask VWAP) | Текущий Bid | Оценка бота | Размер ($) | Нереализ. PnL | Источник |
| :- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| #51 | Will there be no change in Fed interest rates after the | Macro | **YES** | `0.940` | `0.930` | `96.5%` | `$3.67` | `$-0.04` | https://www.federalreserve.gov |
| #52 | Will the Fed increase interest rates by 25 bps after th | Macro | **NO** | `0.960` | `0.930` | `87.0%` | `$3.70` | `$-0.12` | https://www.federalreserve.gov |
| #59 | Israel x Iran ceasefire continues through October 27? | Geopolitics | **YES** | `0.940` | `0.971` | `98.0%` | `$4.69` | `$+0.15` | the totality of information av |
| #66 | Pacers vs. Bucks: O/U 212.5 | Sports | **YES** | `0.960` | `0.920` | `96.5%` | `$5.06` | `$-0.21` | https://www.nba.com/ |

## 🔍 Последние проверенные кандидаты и фильтр стакана CLOB
| Рынок | Кат. | Сторона | Оценка бота | Цена Ask | Перекос (Edge) | Проскальзывание CLOB | Решение |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Will CR Flamengo win on 2026-10-26? | Sports | YES | `83.0%` | `78.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Win probability 83.0% < 92% minimum (no underdog lottery bets) |
| Counter-Strike: Envy vs GamerLegion (BO3) - Tesla  | Sports | YES | `64.7%` | `59.0%` | `+5.7 п.п.` | `2.00%` | REJECTED: Win probability 64.7% < 92% minimum (no underdog lottery bets) |
| Spread: Eagles (-3.5) | Sports | NO | `97.5%` | `78.0%` | `+19.5 п.п.` | `1.00%` | REJECTED: Contract price $0.780 outside sweet spot [$0.84, $0.96] |
| Counter-Strike: Nuclear TigeRES vs UNiTY esports ( | Sports | NO | `1.5%` | `100.0%` | `-98.5 п.п.` | `100.00%` | REJECTED: Edge -98.5 pp < 2 pp threshold (P_est=1.5% vs AskVWAP=100.0%) |
| Spread: Pacers (-4.5) | Sports | NO | `97.5%` | `51.0%` | `+46.5 п.п.` | `1.00%` | REJECTED: Contract price $0.510 outside sweet spot [$0.84, $0.96] |
| Spread: Cavaliers (-3.5) | Sports | NO | `97.5%` | `51.0%` | `+46.5 п.п.` | `1.00%` | REJECTED: Contract price $0.510 outside sweet spot [$0.84, $0.96] |
| Cowboys vs. Eagles: O/U 44.5 | Sports | YES | `52.4%` | `46.7%` | `+5.7 п.п.` | `0.10%` | REJECTED: Win probability 52.4% < 92% minimum (no underdog lottery bets) |
| Spread: Heat (-7.5) | Sports | YES | `56.0%` | `51.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Win probability 56.0% < 92% minimum (no underdog lottery bets) |
| Spread: Cavaliers (-4.5) | Sports | NO | `97.5%` | `55.0%` | `+42.5 п.п.` | `1.00%` | REJECTED: Contract price $0.550 outside sweet spot [$0.84, $0.96] |
| Spread: Cowboys (-4.5) | Sports | NO | `97.5%` | `52.0%` | `+45.5 п.п.` | `1.00%` | REJECTED: Contract price $0.520 outside sweet spot [$0.84, $0.96] |
| Game Handicap: AL (-1.5) vs Team Liquid (+1.5) | Sports | YES | `1.5%` | `100.0%` | `-98.5 п.п.` | `100.00%` | REJECTED: Edge -98.5 pp < 2 pp threshold (P_est=1.5% vs AskVWAP=100.0%) |
| Warriors vs. Nuggets | Sports | YES | `34.0%` | `29.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Win probability 34.0% < 92% minimum (no underdog lottery bets) |
| Mavericks vs. Heat | Sports | YES | `35.0%` | `30.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Win probability 35.0% < 92% minimum (no underdog lottery bets) |
| Grizzlies vs. Jazz | Sports | YES | `59.8%` | `51.0%` | `+8.8 п.п.` | `1.00%` | REJECTED: Win probability 59.8% < 92% minimum (no underdog lottery bets) |
| Cowboys vs. Eagles | Sports | YES | `72.0%` | `67.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Win probability 72.0% < 92% minimum (no underdog lottery bets) |
| Spread: Rockets (-4.5) | Sports | NO | `97.5%` | `50.0%` | `+47.5 п.п.` | `1.00%` | REJECTED: Contract price $0.500 outside sweet spot [$0.84, $0.96] |
| Suns vs. Thunder | Sports | NO | `81.0%` | `76.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Win probability 81.0% < 92% minimum (no underdog lottery bets) |
| LoL: Team Liquid vs Anyone's Legend (BO3) - Worlds | Sports | YES | `69.4%` | `61.0%` | `+8.4 п.п.` | `1.00%` | REJECTED: Win probability 69.4% < 92% minimum (no underdog lottery bets) |
