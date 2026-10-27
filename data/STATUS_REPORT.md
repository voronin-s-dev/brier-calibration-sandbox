# 📊 Отчёт симулятора Polymarket (Устав Grok Bot — Демо-счёт)
**Обновлено:** `2026-10-27 06:10:09 UTC`

## 💰 Состояние виртуального портфеля
| Показатель | Значение | Правило устава |
| :--- | :--- | :--- |
| **Стартовый капитал** | `$50.00 USDC` | Не добавлять деньги |
| **Текущий баланс (Equity)** | **`$30.18 USDC`** (`-19.82$` / `-39.64%`) | Cash + Mark-to-Market по CLOB Bid |
| **Свободный кэш / В сделках** | `$13.93` / `$16.25 USDC` | До 8 открытых позиций, макс 8% банка |
| **Цель окупаемости подписки** | `$-19.82 / $60.00` (`0.0%`) | Цель: +$60.00 в месяц |
| **Просадка от пика (Текущая / Макс)** | `14.54%` / `14.54%` (Пик: `$35.32`) | Стоп-кран при просадке 40% |
| **Закрытых сделок / Win Rate** | `66` / `57.6%` | Brier Score: `0.2273` |

## 📂 Открытые позиции (4 / 8)
| # | Рынок | Кат. | Исход | Вход (Ask VWAP) | Текущий Bid | Оценка бота | Размер ($) | Нереализ. PnL | Источник |
| :- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| #51 | Will there be no change in Fed interest rates after the | Macro | **YES** | `0.940` | `0.937` | `96.5%` | `$3.67` | `$-0.01` | https://www.federalreserve.gov |
| #52 | Will the Fed increase interest rates by 25 bps after th | Macro | **NO** | `0.960` | `0.939` | `98.0%` | `$3.70` | `$-0.08` | https://www.federalreserve.gov |
| #70 | Kings vs. Spurs | Sports | **NO** | `0.930` | `0.920` | `96.0%` | `$4.54` | `$-0.05` | https://www.nba.com/ |
| #71 | Will Arsenal FC win on 2026-10-27? | Sports | **YES** | `0.900` | `0.890` | `95.0%` | `$4.53` | `$-0.05` | https://www.efl.com/ |

## 🔍 Последние проверенные кандидаты и фильтр стакана CLOB
| Рынок | Кат. | Сторона | Оценка бота | Цена Ask | Перекос (Edge) | Проскальзывание CLOB | Решение |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Spread: Lakers (-3.5) | Sports | NO | `97.5%` | `53.0%` | `+44.5 п.п.` | `1.00%` | REJECTED: Contract price $0.530 outside sweet spot [$0.84, $0.96] |
| Will Liverpool FC win on 2026-10-28? | Sports | YES | `48.0%` | `43.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Win probability 48.0% < 92% minimum (no underdog lottery bets) |
| Shanghai Port FC vs. Cong An Ha Noi FC: O/U 3.5 | Sports | YES | `45.0%` | `40.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Win probability 45.0% < 92% minimum (no underdog lottery bets) |
| Shanghai Port FC vs. Cong An Ha Noi FC: O/U 2.5 | Sports | YES | `67.0%` | `62.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Win probability 67.0% < 92% minimum (no underdog lottery bets) |
| LoL: Hanwha Life Esports vs G2 Esports (BO3) - Wor | Sports | NO | `26.5%` | `21.0%` | `+5.5 п.п.` | `1.00%` | REJECTED: Win probability 26.5% < 92% minimum (no underdog lottery bets) |
| LoL: Movistar KOI vs T1 (BO3) - Worlds Group Stage | Sports | NO | `89.6%` | `84.0%` | `+5.6 п.п.` | `1.00%` | REJECTED: Win probability 89.6% < 92% minimum (no underdog lottery bets) |
| Will FC Internazionale Milano win on 2026-10-28? | Sports | YES | `78.0%` | `73.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Win probability 78.0% < 92% minimum (no underdog lottery bets) |
| LoL: Top Esports vs Bilibili Gaming (BO3) - Worlds | Sports | NO | `82.0%` | `77.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Win probability 82.0% < 92% minimum (no underdog lottery bets) |
| Counter-Strike: Astralis vs fnatic (BO3) - Stake R | Sports | NO | `51.8%` | `45.0%` | `+6.8 п.п.` | `1.00%` | REJECTED: Win probability 51.8% < 92% minimum (no underdog lottery bets) |
| Counter-Strike: Vitality vs Natus Vincere (BO3) -  | Sports | YES | `76.0%` | `71.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Win probability 76.0% < 92% minimum (no underdog lottery bets) |
| Trail Blazers vs. Lakers | Sports | NO | `63.0%` | `58.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Win probability 63.0% < 92% minimum (no underdog lottery bets) |
| Spread: Knicks (-3.5) | Sports | NO | `97.5%` | `48.0%` | `+49.5 п.п.` | `1.00%` | REJECTED: Contract price $0.480 outside sweet spot [$0.84, $0.96] |
| Map Handicap: VIT (-1.5) vs Natus Vincere (+1.5) | Sports | NO | `62.2%` | `58.0%` | `+4.2 п.п.` | `1.00%` | REJECTED: Win probability 62.2% < 92% minimum (no underdog lottery bets) |
| LoL: Invictus Gaming vs LYON (BO3) - Worlds Group  | Sports | NO | `44.0%` | `39.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Win probability 44.0% < 92% minimum (no underdog lottery bets) |
| Will SS Lazio win on 2026-10-27? | Sports | YES | `51.0%` | `46.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Win probability 51.0% < 92% minimum (no underdog lottery bets) |
| Counter-Strike: Spirit vs MOUZ (BO3) - PGL Masters | Sports | YES | `66.7%` | `56.0%` | `+10.7 п.п.` | `1.00%` | REJECTED: Win probability 66.7% < 92% minimum (no underdog lottery bets) |
| Counter-Strike: Liquid vs Aurora Gaming (BO3) - PG | Sports | YES | `32.0%` | `27.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Win probability 32.0% < 92% minimum (no underdog lottery bets) |
| Will Como 1907 win on 2026-10-27? | Sports | YES | `64.0%` | `59.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Win probability 64.0% < 92% minimum (no underdog lottery bets) |
