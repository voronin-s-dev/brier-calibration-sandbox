# 📊 Отчёт симулятора Polymarket (Устав Grok Bot — Демо-счёт)
**Обновлено:** `2026-10-28 01:37:27 UTC`

## 💰 Состояние виртуального портфеля
| Показатель | Значение | Правило устава |
| :--- | :--- | :--- |
| **Стартовый капитал** | `$50.00 USDC` | Не добавлять деньги |
| **Текущий баланс (Equity)** | **`$27.05 USDC`** (`-22.95$` / `-45.89%`) | Cash + Mark-to-Market по CLOB Bid |
| **Свободный кэш / В сделках** | `$19.59` / `$7.47 USDC` | До 8 открытых позиций, макс 8% банка |
| **Цель окупаемости подписки** | `$-22.95 / $60.00` (`0.0%`) | Цель: +$60.00 в месяц |
| **Просадка от пика (Текущая / Макс)** | `23.40%` / `23.40%` (Пик: `$35.32`) | Стоп-кран при просадке 40% |
| **Закрытых сделок / Win Rate** | `70` / `58.6%` | Brier Score: `0.2524` |

## 📂 Открытые позиции (2 / 8)
| # | Рынок | Кат. | Исход | Вход (Ask VWAP) | Текущий Bid | Оценка бота | Размер ($) | Нереализ. PnL | Источник |
| :- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| #51 | Will there be no change in Fed interest rates after the | Macro | **YES** | `0.940` | `0.961` | `96.5%` | `$3.67` | `$+0.08` | https://www.federalreserve.gov |
| #52 | Will the Fed increase interest rates by 25 bps after th | Macro | **NO** | `0.960` | `0.964` | `98.5%` | `$3.70` | `$+0.02` | https://www.federalreserve.gov |

## 🔍 Последние проверенные кандидаты и фильтр стакана CLOB
| Рынок | Кат. | Сторона | Оценка бота | Цена Ask | Перекос (Edge) | Проскальзывание CLOB | Решение |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Counter-Strike: Liquid vs FURIA (BO3) - PGL Master | Sports | YES | `33.0%` | `28.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Win probability 33.0% < 92% minimum (no underdog lottery bets) |
| Will Elche CF win on 2026-11-01? | Sports | YES | `46.0%` | `41.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Win probability 46.0% < 92% minimum (no underdog lottery bets) |
| Spread: Lakers (-4.5) | Sports | NO | `97.5%` | `60.0%` | `+37.5 п.п.` | `1.00%` | REJECTED: Contract price $0.600 outside sweet spot [$0.84, $0.96] |
| Magic vs. Raptors | Sports | NO | `73.6%` | `64.0%` | `+9.6 п.п.` | `1.00%` | REJECTED: Win probability 73.6% < 92% minimum (no underdog lottery bets) |
| Will FC Internazionale Milano win on 2026-10-28? | Sports | YES | `78.0%` | `73.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Win probability 78.0% < 92% minimum (no underdog lottery bets) |
| Will Manchester City FC win on 2026-10-28? | Sports | YES | `63.0%` | `58.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Win probability 63.0% < 92% minimum (no underdog lottery bets) |
| Counter-Strike: Spirit vs Natus Vincere (BO3) - PG | Sports | YES | `74.0%` | `69.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Win probability 74.0% < 92% minimum (no underdog lottery bets) |
| Will Liverpool FC win on 2026-10-28? | Sports | YES | `51.0%` | `46.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Win probability 51.0% < 92% minimum (no underdog lottery bets) |
| SV 07 Elversberg vs. 1. FSV Mainz 05: O/U 2.5 | Sports | NO | `40.0%` | `35.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Win probability 40.0% < 92% minimum (no underdog lottery bets) |
| Map Handicap: B8 (-1.5) vs Alliance (+1.5) | Sports | NO | `66.9%` | `62.0%` | `+4.9 п.п.` | `1.00%` | REJECTED: Win probability 66.9% < 92% minimum (no underdog lottery bets) |
| Spread: Steelers (-3.5) | Sports | NO | `97.5%` | `53.0%` | `+44.5 п.п.` | `1.00%` | REJECTED: Contract price $0.530 outside sweet spot [$0.84, $0.96] |
| Raiders vs. Jets | Sports | YES | `52.0%` | `47.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Win probability 52.0% < 92% minimum (no underdog lottery bets) |
| 76ers vs. Pacers | Sports | NO | `43.5%` | `39.0%` | `+4.5 п.п.` | `2.00%` | REJECTED: Win probability 43.5% < 92% minimum (no underdog lottery bets) |
| Spread: Lakers (-3.5) | Sports | NO | `97.5%` | `57.0%` | `+40.5 п.п.` | `1.00%` | REJECTED: Contract price $0.570 outside sweet spot [$0.84, $0.96] |
| Warriors vs. Timberwolves | Sports | NO | `64.0%` | `59.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Win probability 64.0% < 92% minimum (no underdog lottery bets) |
| Counter-Strike: TheMongolz vs Nemiga (BO3) - PGL M | Sports | YES | `63.0%` | `58.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Win probability 63.0% < 92% minimum (no underdog lottery bets) |
| Spread: Lakers (-1.5) | Sports | YES | `56.1%` | `52.0%` | `+4.1 п.п.` | `1.00%` | REJECTED: Win probability 56.1% < 92% minimum (no underdog lottery bets) |
| Spread: Lakers (-2.5) | Sports | YES | `56.5%` | `48.0%` | `+8.5 п.п.` | `1.00%` | REJECTED: Win probability 56.5% < 92% minimum (no underdog lottery bets) |
