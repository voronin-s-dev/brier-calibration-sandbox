# 📊 Отчёт симулятора Polymarket (Устав Grok Bot — Демо-счёт)
**Обновлено:** `2026-10-27 22:52:33 UTC`

## 💰 Состояние виртуального портфеля
| Показатель | Значение | Правило устава |
| :--- | :--- | :--- |
| **Стартовый капитал** | `$50.00 USDC` | Не добавлять деньги |
| **Текущий баланс (Equity)** | **`$31.30 USDC`** (`-18.70$` / `-37.40%`) | Cash + Mark-to-Market по CLOB Bid |
| **Свободный кэш / В сделках** | `$14.73` / `$16.57 USDC` | До 8 открытых позиций, макс 8% банка |
| **Цель окупаемости подписки** | `$-18.70 / $60.00` (`0.0%`) | Цель: +$60.00 в месяц |
| **Просадка от пика (Текущая / Макс)** | `11.37%` / `14.94%` (Пик: `$35.32`) | Стоп-кран при просадке 40% |
| **Закрытых сделок / Win Rate** | `68` / `58.8%` | Brier Score: `0.2141` |

## 📂 Открытые позиции (4 / 8)
| # | Рынок | Кат. | Исход | Вход (Ask VWAP) | Текущий Bid | Оценка бота | Размер ($) | Нереализ. PnL | Источник |
| :- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| #51 | Will there be no change in Fed interest rates after the | Macro | **YES** | `0.940` | `0.957` | `96.5%` | `$3.67` | `$+0.07` | https://www.federalreserve.gov |
| #52 | Will the Fed increase interest rates by 25 bps after th | Macro | **NO** | `0.960` | `0.964` | `98.5%` | `$3.70` | `$+0.02` | https://www.federalreserve.gov |
| #70 | Kings vs. Spurs | Sports | **NO** | `0.930` | `0.920` | `96.0%` | `$4.54` | `$-0.05` | https://www.nba.com/ |
| #71 | Will Arsenal FC win on 2026-10-27? | Sports | **YES** | `0.900` | `0.920` | `96.0%` | `$4.53` | `$+0.10` | https://www.efl.com/ |

## 🔍 Последние проверенные кандидаты и фильтр стакана CLOB
| Рынок | Кат. | Сторона | Оценка бота | Цена Ask | Перекос (Edge) | Проскальзывание CLOB | Решение |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Will Liverpool FC win on 2026-10-28? | Sports | YES | `51.0%` | `46.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Win probability 51.0% < 92% minimum (no underdog lottery bets) |
| Thunder vs. Mavericks | Sports | NO | `30.7%` | `25.0%` | `+5.7 п.п.` | `1.00%` | REJECTED: Win probability 30.7% < 92% minimum (no underdog lottery bets) |
| Spread: Steelers (-3.5) | Sports | NO | `97.5%` | `53.0%` | `+44.5 п.п.` | `1.00%` | REJECTED: Contract price $0.530 outside sweet spot [$0.84, $0.96] |
| Raiders vs. Jets | Sports | YES | `51.0%` | `46.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Win probability 51.0% < 92% minimum (no underdog lottery bets) |
| Warriors vs. Timberwolves | Sports | NO | `71.0%` | `59.0%` | `+12.0 п.п.` | `1.00%` | REJECTED: Win probability 71.0% < 92% minimum (no underdog lottery bets) |
| Spread: Milwaukee Brewers (-1.5) | Sports | YES | `45.0%` | `40.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Win probability 45.0% < 92% minimum (no underdog lottery bets) |
| Trail Blazers vs. Lakers: O/U 237.5 | Sports | NO | `65.3%` | `61.0%` | `+4.3 п.п.` | `1.00%` | REJECTED: Win probability 65.3% < 92% minimum (no underdog lottery bets) |
| Counter-Strike: TheMongolz vs Nemiga (BO3) - PGL M | Sports | YES | `68.4%` | `59.0%` | `+9.4 п.п.` | `1.00%` | REJECTED: Win probability 68.4% < 92% minimum (no underdog lottery bets) |
| Kings vs. Blackhawks | Sports | YES | `56.0%` | `51.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Win probability 56.0% < 92% minimum (no underdog lottery bets) |
| 76ers vs. Pacers | Sports | NO | `44.0%` | `39.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Win probability 44.0% < 92% minimum (no underdog lottery bets) |
| Spread: Knicks (-4.5) | Sports | NO | `97.5%` | `53.0%` | `+44.5 п.п.` | `1.00%` | REJECTED: Contract price $0.530 outside sweet spot [$0.84, $0.96] |
| Browns vs. Steelers | Sports | YES | `41.0%` | `36.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Win probability 41.0% < 92% minimum (no underdog lottery bets) |
| Spread: Lakers (-3.5) | Sports | NO | `97.5%` | `58.0%` | `+39.5 п.п.` | `1.00%` | REJECTED: Contract price $0.580 outside sweet spot [$0.84, $0.96] |
| Spread: Knicks (-3.5) | Sports | NO | `97.5%` | `48.0%` | `+49.5 п.п.` | `1.00%` | REJECTED: Contract price $0.480 outside sweet spot [$0.84, $0.96] |
| Spread: Lakers (-2.5) | Sports | YES | `52.0%` | `47.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Win probability 52.0% < 92% minimum (no underdog lottery bets) |
| Pistons vs. Knicks | Sports | YES | `45.0%` | `40.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Win probability 45.0% < 92% minimum (no underdog lottery bets) |
| Dota 2: Team Yandex vs Astra Invicta (BO3) - PARI  | Sports | NO | `15.2%` | `10.0%` | `+5.2 п.п.` | `2.00%` | REJECTED: Win probability 15.2% < 92% minimum (no underdog lottery bets) |
| Will Liverpool FC win on 2026-10-28? | Sports | YES | `51.0%` | `46.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Win probability 51.0% < 92% minimum (no underdog lottery bets) |
