# 📊 Отчёт симулятора Polymarket (Устав Grok Bot — Демо-счёт)
**Обновлено:** `2026-10-27 18:33:12 UTC`

## 💰 Состояние виртуального портфеля
| Показатель | Значение | Правило устава |
| :--- | :--- | :--- |
| **Стартовый капитал** | `$50.00 USDC` | Не добавлять деньги |
| **Текущий баланс (Equity)** | **`$30.63 USDC`** (`-19.37$` / `-38.74%`) | Cash + Mark-to-Market по CLOB Bid |
| **Свободный кэш / В сделках** | `$9.73` / `$20.90 USDC` | До 8 открытых позиций, макс 8% банка |
| **Цель окупаемости подписки** | `$-19.37 / $60.00` (`0.0%`) | Цель: +$60.00 в месяц |
| **Просадка от пика (Текущая / Макс)** | `13.27%` / `14.94%` (Пик: `$35.32`) | Стоп-кран при просадке 40% |
| **Закрытых сделок / Win Rate** | `67` / `58.2%` | Brier Score: `0.2273` |

## 📂 Открытые позиции (5 / 8)
| # | Рынок | Кат. | Исход | Вход (Ask VWAP) | Текущий Bid | Оценка бота | Размер ($) | Нереализ. PnL | Источник |
| :- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| #51 | Will there be no change in Fed interest rates after the | Macro | **YES** | `0.940` | `0.934` | `96.5%` | `$3.67` | `$-0.02` | https://www.federalreserve.gov |
| #52 | Will the Fed increase interest rates by 25 bps after th | Macro | **NO** | `0.960` | `0.930` | `97.0%` | `$3.70` | `$-0.12` | https://www.federalreserve.gov |
| #70 | Kings vs. Spurs | Sports | **NO** | `0.930` | `0.920` | `96.0%` | `$4.54` | `$-0.05` | https://www.nba.com/ |
| #71 | Will Arsenal FC win on 2026-10-27? | Sports | **YES** | `0.900` | `0.920` | `96.0%` | `$4.53` | `$+0.10` | https://www.efl.com/ |
| #73 | Will Cagliari Calcio win on 2026-10-27? | Sports | **NO** | `0.920` | `0.910` | `95.0%` | `$4.60` | `$-0.05` | https://www.legaseriea.it/ |

## 🔍 Последние проверенные кандидаты и фильтр стакана CLOB
| Рынок | Кат. | Сторона | Оценка бота | Цена Ask | Перекос (Edge) | Проскальзывание CLOB | Решение |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Counter-Strike: MORROW vs maybe (BO3) - European P | Sports | NO | `1.5%` | `100.0%` | `-98.5 п.п.` | `100.00%` | REJECTED: Edge -98.5 pp < 2 pp threshold (P_est=1.5% vs AskVWAP=100.0%) |
| 76ers vs. Pacers | Sports | YES | `65.0%` | `60.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Win probability 65.0% < 92% minimum (no underdog lottery bets) |
| Kings vs. Blackhawks | Sports | NO | `55.0%` | `50.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Win probability 55.0% < 92% minimum (no underdog lottery bets) |
| Counter-Strike: Wingman vs Revise (BO3) - Exort Fi | Sports | YES | `1.5%` | `100.0%` | `-98.5 п.п.` | `100.00%` | REJECTED: Edge -98.5 pp < 2 pp threshold (P_est=1.5% vs AskVWAP=100.0%) |
| LoL: Top Esports vs Bilibili Gaming (BO3) - Worlds | Sports | NO | `82.2%` | `76.0%` | `+6.2 п.п.` | `1.00%` | REJECTED: Win probability 82.2% < 92% minimum (no underdog lottery bets) |
| Spread: Lakers (-3.5) | Sports | NO | `97.5%` | `56.0%` | `+41.5 п.п.` | `1.00%` | REJECTED: Contract price $0.560 outside sweet spot [$0.84, $0.96] |
| Counter-Strike: Envy vs GamerLegion - Map 1 Winner | Sports | YES | `1.5%` | `100.0%` | `-98.5 п.п.` | `100.00%` | REJECTED: Edge -98.5 pp < 2 pp threshold (P_est=1.5% vs AskVWAP=100.0%) |
| LoL: Invictus Gaming vs LYON (BO3) - Worlds Group  | Sports | NO | `41.0%` | `36.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Win probability 41.0% < 92% minimum (no underdog lottery bets) |
| Spread: Knicks (-3.5) | Sports | NO | `97.5%` | `48.0%` | `+49.5 п.п.` | `1.00%` | REJECTED: Contract price $0.480 outside sweet spot [$0.84, $0.96] |
| Spread: Lakers (-2.5) | Sports | YES | `53.0%` | `48.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Win probability 53.0% < 92% minimum (no underdog lottery bets) |
| Counter-Strike: Vitality vs Natus Vincere - Map 1  | Sports | NO | `1.5%` | `100.0%` | `-98.5 п.п.` | `100.00%` | REJECTED: Edge -98.5 pp < 2 pp threshold (P_est=1.5% vs AskVWAP=100.0%) |
| Counter-Strike: Envy vs GamerLegion (BO3) - Tesla  | Sports | NO | `74.2%` | `68.0%` | `+6.2 п.п.` | `1.00%` | REJECTED: Win probability 74.2% < 92% minimum (no underdog lottery bets) |
| Map Handicap: VIT (-1.5) vs Natus Vincere (+1.5) | Sports | NO | `30.2%` | `25.0%` | `+5.2 п.п.` | `1.00%` | REJECTED: Win probability 30.2% < 92% minimum (no underdog lottery bets) |
| Pistons vs. Knicks | Sports | YES | `46.0%` | `41.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Win probability 46.0% < 92% minimum (no underdog lottery bets) |
| Dota 2: BetBoom Team vs LEGION (BO1) - PARI Univer | Sports | YES | `1.5%` | `100.0%` | `-98.5 п.п.` | `100.00%` | REJECTED: Edge -98.5 pp < 2 pp threshold (P_est=1.5% vs AskVWAP=100.0%) |
| Fleetwood Town FC vs. Arsenal FC: O/U 1.5 | Sports | NO | `15.0%` | `10.0%` | `+5.0 п.п.` | `1.22%` | REJECTED: Win probability 15.0% < 92% minimum (no underdog lottery bets) |
| Nets vs. Celtics | Sports | YES | `20.0%` | `15.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Win probability 20.0% < 92% minimum (no underdog lottery bets) |
| Counter-Strike: MORROW vs maybe (BO3) - European P | Sports | NO | `1.5%` | `100.0%` | `-98.5 п.п.` | `100.00%` | REJECTED: Edge -98.5 pp < 2 pp threshold (P_est=1.5% vs AskVWAP=100.0%) |
