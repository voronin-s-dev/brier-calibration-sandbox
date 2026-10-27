# 📊 Отчёт симулятора Polymarket (Устав Grok Bot — Демо-счёт)
**Обновлено:** `2026-10-27 06:29:07 UTC`

## 💰 Состояние виртуального портфеля
| Показатель | Значение | Правило устава |
| :--- | :--- | :--- |
| **Стартовый капитал** | `$50.00 USDC` | Не добавлять деньги |
| **Текущий баланс (Equity)** | **`$30.09 USDC`** (`-19.91$` / `-39.81%`) | Cash + Mark-to-Market по CLOB Bid |
| **Свободный кэш / В сделках** | `$9.91` / `$20.18 USDC` | До 8 открытых позиций, макс 8% банка |
| **Цель окупаемости подписки** | `$-19.91 / $60.00` (`0.0%`) | Цель: +$60.00 в месяц |
| **Просадка от пика (Текущая / Макс)** | `14.79%` / `14.79%` (Пик: `$35.32`) | Стоп-кран при просадке 40% |
| **Закрытых сделок / Win Rate** | `66` / `57.6%` | Brier Score: `0.2273` |

## 📂 Открытые позиции (5 / 8)
| # | Рынок | Кат. | Исход | Вход (Ask VWAP) | Текущий Bid | Оценка бота | Размер ($) | Нереализ. PnL | Источник |
| :- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| #51 | Will there be no change in Fed interest rates after the | Macro | **YES** | `0.940` | `0.937` | `96.5%` | `$3.67` | `$-0.01` | https://www.federalreserve.gov |
| #52 | Will the Fed increase interest rates by 25 bps after th | Macro | **NO** | `0.960` | `0.940` | `98.0%` | `$3.70` | `$-0.08` | https://www.federalreserve.gov |
| #70 | Kings vs. Spurs | Sports | **NO** | `0.930` | `0.910` | `95.5%` | `$4.54` | `$-0.10` | https://www.nba.com/ |
| #71 | Will Arsenal FC win on 2026-10-27? | Sports | **YES** | `0.900` | `0.890` | `95.0%` | `$4.53` | `$-0.05` | https://www.efl.com/ |
| #72 | Counter-Strike: FURIA vs TYLOO (BO3) - PGL Masters Buch | Sports | **YES** | `0.910` | `0.900` | `94.0%` | `$4.02` | `$-0.04` | https://hltv.org |

## 🔍 Последние проверенные кандидаты и фильтр стакана CLOB
| Рынок | Кат. | Сторона | Оценка бота | Цена Ask | Перекос (Edge) | Проскальзывание CLOB | Решение |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Spread: Lakers (-3.5) | Sports | NO | `97.5%` | `53.0%` | `+44.5 п.п.` | `1.00%` | REJECTED: Contract price $0.530 outside sweet spot [$0.84, $0.96] |
| Will Liverpool FC win on 2026-10-28? | Sports | YES | `48.0%` | `43.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Win probability 48.0% < 92% minimum (no underdog lottery bets) |
| Spread: Beijing Royal Fighters (-8.5) | Sports | YES | `50.8%` | `46.5%` | `+4.3 п.п.` | `2.50%` | REJECTED: Win probability 50.8% < 92% minimum (no underdog lottery bets) |
| Will FC Internazionale Milano win on 2026-10-28? | Sports | YES | `78.0%` | `73.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Win probability 78.0% < 92% minimum (no underdog lottery bets) |
| Counter-Strike: Astralis vs fnatic (BO3) - Stake R | Sports | NO | `51.8%` | `45.0%` | `+6.8 п.п.` | `1.00%` | REJECTED: Win probability 51.8% < 92% minimum (no underdog lottery bets) |
| LoL: Top Esports vs Bilibili Gaming (BO3) - Worlds | Sports | NO | `82.0%` | `77.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Win probability 82.0% < 92% minimum (no underdog lottery bets) |
| Trail Blazers vs. Lakers | Sports | NO | `63.0%` | `58.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Win probability 63.0% < 92% minimum (no underdog lottery bets) |
| Counter-Strike: Vitality vs Natus Vincere (BO3) -  | Sports | YES | `75.0%` | `70.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Win probability 75.0% < 92% minimum (no underdog lottery bets) |
| LoL: Invictus Gaming vs LYON (BO3) - Worlds Group  | Sports | NO | `44.0%` | `39.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Win probability 44.0% < 92% minimum (no underdog lottery bets) |
| Spread: Knicks (-3.5) | Sports | NO | `97.5%` | `48.0%` | `+49.5 п.п.` | `1.00%` | REJECTED: Contract price $0.480 outside sweet spot [$0.84, $0.96] |
| Counter-Strike: Spirit vs MOUZ (BO3) - PGL Masters | Sports | YES | `67.1%` | `57.0%` | `+10.1 п.п.` | `1.00%` | REJECTED: Win probability 67.1% < 92% minimum (no underdog lottery bets) |
| Counter-Strike: Liquid vs Aurora Gaming (BO3) - PG | Sports | YES | `32.0%` | `27.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Win probability 32.0% < 92% minimum (no underdog lottery bets) |
| Counter-Strike: TheMongolz vs Legacy (BO3) - PGL M | Sports | YES | `50.0%` | `45.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Win probability 50.0% < 92% minimum (no underdog lottery bets) |
| Counter-Strike: Envy vs GamerLegion (BO3) - Tesla  | Sports | YES | `65.3%` | `61.0%` | `+4.3 п.п.` | `1.00%` | REJECTED: Win probability 65.3% < 92% minimum (no underdog lottery bets) |
| Counter-Strike: Nemiga vs DENDELE CS (BO3) - PGL M | Sports | YES | `65.2%` | `60.0%` | `+5.2 п.п.` | `1.00%` | REJECTED: Win probability 65.2% < 92% minimum (no underdog lottery bets) |
| Will Ratchaburi FC win on 2026-10-27? | Sports | YES | `18.0%` | `13.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Win probability 18.0% < 92% minimum (no underdog lottery bets) |
| Counter-Strike: FURIA vs TYLOO (BO3) - PGL Masters | Sports | YES | `94.0%` | `91.0%` | `+3.0 п.п.` | `1.00%` | EXECUTED BUY #72 ($4.02 @ 0.9100) |
| Spread: Lakers (-3.5) | Sports | NO | `97.5%` | `53.0%` | `+44.5 п.п.` | `1.00%` | REJECTED: Contract price $0.530 outside sweet spot [$0.84, $0.96] |
