# 📊 Отчёт симулятора Polymarket (Устав Grok Bot — Демо-счёт)
**Обновлено:** `2026-10-28 07:21:24 UTC`

## 💰 Состояние виртуального портфеля
| Показатель | Значение | Правило устава |
| :--- | :--- | :--- |
| **Стартовый капитал** | `$50.00 USDC` | Не добавлять деньги |
| **Текущий баланс (Equity)** | **`$26.72 USDC`** (`-23.28$` / `-46.56%`) | Cash + Mark-to-Market по CLOB Bid |
| **Свободный кэш / В сделках** | `$9.61` / `$17.11 USDC` | До 8 открытых позиций, макс 8% банка |
| **Цель окупаемости подписки** | `$-23.28 / $60.00` (`0.0%`) | Цель: +$60.00 в месяц |
| **Просадка от пика (Текущая / Макс)** | `24.34%` / `24.34%` (Пик: `$35.32`) | Стоп-кран при просадке 40% |
| **Закрытых сделок / Win Rate** | `70` / `58.6%` | Brier Score: `0.2524` |

## 📂 Открытые позиции (5 / 8)
| # | Рынок | Кат. | Исход | Вход (Ask VWAP) | Текущий Bid | Оценка бота | Размер ($) | Нереализ. PnL | Источник |
| :- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| #51 | Will there be no change in Fed interest rates after the | Macro | **YES** | `0.940` | `0.952` | `96.5%` | `$3.67` | `$+0.05` | https://www.federalreserve.gov |
| #52 | Will the Fed increase interest rates by 25 bps after th | Macro | **NO** | `0.960` | `0.955` | `98.5%` | `$3.70` | `$-0.02` | https://www.federalreserve.gov |
| #74 | Will the Milwaukee Brewers win the 2026 World Series? | Sports | **YES** | `0.953` | `0.907` | `98.0%` | `$4.06` | `$-0.20` | https://www.mlb.com/ |
| #75 | Will FC Barcelona win on 2026-10-31? | Sports | **YES** | `0.890` | `0.880` | `92.8%` | `$3.78` | `$-0.04` | https://www.laliga.com/ |
| #76 | LoL: Movistar KOI vs T1 (BO3) - Worlds Group Stage | Sports | **NO** | `0.860` | `0.850` | `89.0%` | `$2.14` | `$-0.02` | https://gol.gg/esports/home |

## 🧪 Теневая песочница (Shadow Sandbox)
| Показатель | Значение |
| :--- | :--- |
| **Виртуальный баланс (Equity)** | **`$50.00 USDC`** |
| **Свободный кэш / В сделках** | `$50.00` / `$0.00 USDC` |
| **Открытых позиций** | `0 / 5` |
| **Текущая просадка** | `0.00%` |

### Доходность по замороженным категориям (Песочница)
*Теневые сделки пока не закрыты (накапливается история).*

## 🔍 Последние проверенные кандидаты и фильтр стакана CLOB
| Рынок | Кат. | Сторона | Оценка бота | Цена Ask | Перекос (Edge) | Проскальзывание CLOB | Решение |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Spread: Steelers (-3.5) | Sports | NO | `97.5%` | `53.0%` | `+44.5 п.п.` | `1.00%` | REJECTED: Contract price $0.530 outside sweet spot [$0.76, $0.89] |
| LoL: Movistar KOI vs T1 (BO3) - Worlds Group Stage | Sports | NO | `89.0%` | `86.0%` | `+3.0 п.п.` | `1.00%` | EXECUTED BUY #76 ($2.14 @ 0.8600) |
| Counter-Strike: Liquid vs FURIA (BO3) - PGL Master | Sports | YES | `33.0%` | `28.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Win probability 33.0% < 92% minimum (no underdog lottery bets) |
| Will Elche CF win on 2026-11-01? | Sports | YES | `46.0%` | `41.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Win probability 46.0% < 92% minimum (no underdog lottery bets) |
| Spread: Lakers (-4.5) | Sports | NO | `97.5%` | `60.0%` | `+37.5 п.п.` | `1.00%` | REJECTED: Contract price $0.600 outside sweet spot [$0.84, $0.96] |
| Magic vs. Raptors | Sports | NO | `70.0%` | `65.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Win probability 70.0% < 92% minimum (no underdog lottery bets) |
| Heat vs. Hawks | Sports | YES | `48.0%` | `43.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Win probability 48.0% < 92% minimum (no underdog lottery bets) |
| Will FC Internazionale Milano win on 2026-10-28? | Sports | YES | `78.0%` | `73.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Win probability 78.0% < 92% minimum (no underdog lottery bets) |
| Will Manchester City FC win on 2026-10-28? | Sports | YES | `63.0%` | `58.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Win probability 63.0% < 92% minimum (no underdog lottery bets) |
| Counter-Strike: Spirit vs Natus Vincere (BO3) - PG | Sports | YES | `74.0%` | `69.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Win probability 74.0% < 92% minimum (no underdog lottery bets) |
| Will Liverpool FC win on 2026-10-28? | Sports | YES | `51.0%` | `46.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Win probability 51.0% < 92% minimum (no underdog lottery bets) |
| Map Handicap: B8 (-1.5) vs Alliance (+1.5) | Sports | NO | `66.9%` | `62.0%` | `+4.9 п.п.` | `1.00%` | REJECTED: Win probability 66.9% < 92% minimum (no underdog lottery bets) |
| Spread: Steelers (-3.5) | Sports | NO | `97.5%` | `53.0%` | `+44.5 п.п.` | `1.00%` | REJECTED: Contract price $0.530 outside sweet spot [$0.84, $0.96] |
| Raiders vs. Jets | Sports | YES | `52.0%` | `47.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Win probability 52.0% < 92% minimum (no underdog lottery bets) |
| 76ers vs. Pacers | Sports | NO | `53.7%` | `42.0%` | `+11.7 п.п.` | `1.00%` | REJECTED: Win probability 53.7% < 92% minimum (no underdog lottery bets) |
| Browns vs. Steelers | Sports | YES | `41.0%` | `36.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Win probability 41.0% < 92% minimum (no underdog lottery bets) |
| Spread: Lakers (-3.5) | Sports | NO | `97.5%` | `57.0%` | `+40.5 п.п.` | `1.00%` | REJECTED: Contract price $0.570 outside sweet spot [$0.84, $0.96] |
| Counter-Strike: TheMongolz vs Nemiga (BO3) - PGL M | Sports | YES | `63.0%` | `58.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Win probability 63.0% < 92% minimum (no underdog lottery bets) |
