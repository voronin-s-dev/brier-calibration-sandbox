# 📊 Отчёт симулятора Polymarket (Устав Grok Bot — Демо-счёт)
**Обновлено:** `2026-10-29 05:33:19 UTC`

## 💰 Состояние виртуального портфеля
| Показатель | Значение | Правило устава |
| :--- | :--- | :--- |
| **Стартовый капитал** | `$50.00 USDC` | Не добавлять деньги |
| **Текущий баланс (Equity)** | **`$28.17 USDC`** (`-21.83$` / `-43.65%`) | Cash + Mark-to-Market по CLOB Bid |
| **Свободный кэш / В сделках** | `$22.77` / `$5.41 USDC` | До 8 открытых позиций, макс 8% банка |
| **Цель окупаемости подписки** | `$-21.83 / $60.00` (`0.0%`) | Цель: +$60.00 в месяц |
| **Просадка от пика (Текущая / Макс)** | `20.22%` / `24.45%` (Пик: `$35.32`) | Стоп-кран при просадке 40% |
| **Закрытых сделок / Win Rate** | `75` / `61.3%` | Brier Score: `0.2283` |

## 📂 Открытые позиции (2 / 8)
| # | Рынок | Кат. | Исход | Вход (Ask VWAP) | Текущий Bid | Оценка бота | Размер ($) | Нереализ. PnL | Источник |
| :- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| #75 | Will FC Barcelona win on 2026-10-31? | Sports | **YES** | `0.890` | `0.880` | `92.8%` | `$3.78` | `$-0.04` | https://www.laliga.com/ |
| #78 | LoL: Karmine Corp vs CTBC Flying Oyster (BO3) - Worlds  | Sports | **YES** | `0.800` | `0.790` | `83.0%` | `$1.69` | `$-0.02` | https://gol.gg/esports/home |

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
| Spread: Trail Blazers (-4.5) | Sports | NO | `97.5%` | `41.0%` | `+56.5 п.п.` | `1.00%` | REJECTED: Contract price $0.410 outside sweet spot [$0.76, $0.89] |
| Spread: Steelers (-3.5) | Sports | NO | `97.5%` | `52.0%` | `+45.5 п.п.` | `1.00%` | REJECTED: Contract price $0.520 outside sweet spot [$0.76, $0.89] |
| Spread: Broncos (-3.5) | Sports | NO | `97.5%` | `67.0%` | `+30.5 п.п.` | `1.00%` | REJECTED: Contract price $0.670 outside sweet spot [$0.76, $0.89] |
| LoL: Karmine Corp vs CTBC Flying Oyster (BO3) - Wo | Sports | YES | `83.0%` | `80.0%` | `+3.0 п.п.` | `1.00%` | EXECUTED BUY #78 ($1.69 @ 0.8000) |
| Spread: Packers (-3.5) | Sports | NO | `97.5%` | `50.0%` | `+47.5 п.п.` | `1.00%` | REJECTED: Contract price $0.500 outside sweet spot [$0.76, $0.89] |
| Spread: Packers (-4.5) | Sports | NO | `97.5%` | `54.0%` | `+43.5 п.п.` | `1.00%` | REJECTED: Contract price $0.540 outside sweet spot [$0.76, $0.89] |
| Spread: Thunder (-3.5) | Sports | NO | `97.5%` | `44.0%` | `+53.5 п.п.` | `1.00%` | REJECTED: Contract price $0.440 outside sweet spot [$0.76, $0.89] |
| Counter-Strike: Hermine Esports Club vs TTG Esport | Sports | YES | `1.5%` | `100.0%` | `-98.5 п.п.` | `100.00%` | REJECTED: Edge -98.5 pp < 2 pp threshold (P_est=1.5% vs AskVWAP=100.0%) |
| Spread: Packers (-3.5) | Sports | NO | `97.5%` | `50.0%` | `+47.5 п.п.` | `1.00%` | REJECTED: Contract price $0.500 outside sweet spot [$0.76, $0.89] |
| Games Total: O/U 2.5 | Sports | NO | `1.5%` | `100.0%` | `-98.5 п.п.` | `100.00%` | REJECTED: Edge -98.5 pp < 2 pp threshold (P_est=1.5% vs AskVWAP=100.0%) |
| Spread: Packers (-4.5) | Sports | NO | `97.5%` | `54.0%` | `+43.5 п.п.` | `1.00%` | REJECTED: Contract price $0.540 outside sweet spot [$0.76, $0.89] |
| Spread: Thunder (-4.5) | Sports | NO | `97.5%` | `48.0%` | `+49.5 п.п.` | `1.00%` | REJECTED: Contract price $0.480 outside sweet spot [$0.76, $0.89] |
| Game Handicap: IG (-1.5) vs LYON (+1.5) | Sports | YES | `1.5%` | `100.0%` | `-98.5 п.п.` | `100.00%` | REJECTED: Edge -98.5 pp < 2 pp threshold (P_est=1.5% vs AskVWAP=100.0%) |
| Spread: Lakers (-4.5) | Sports | NO | `97.5%` | `63.0%` | `+34.5 п.п.` | `1.00%` | REJECTED: Contract price $0.630 outside sweet spot [$0.76, $0.89] |
| Spread: Lakers (-3.5) | Sports | NO | `97.5%` | `60.0%` | `+37.5 п.п.` | `1.00%` | REJECTED: Contract price $0.600 outside sweet spot [$0.76, $0.89] |
| Dota 2: GamerLegion vs LEGION (BO3) - PARI Univers | Sports | NO | `1.5%` | `100.0%` | `-98.5 п.п.` | `100.00%` | REJECTED: Edge -98.5 pp < 2 pp threshold (P_est=1.5% vs AskVWAP=100.0%) |
| LoL: Invictus Gaming vs LYON - Game 1 Winner | Sports | NO | `1.5%` | `100.0%` | `-98.5 п.п.` | `100.00%` | REJECTED: Edge -98.5 pp < 2 pp threshold (P_est=1.5% vs AskVWAP=100.0%) |
| LoL: Invictus Gaming vs LYON - Game 2 Winner | Sports | YES | `1.5%` | `100.0%` | `-98.5 п.п.` | `100.00%` | REJECTED: Edge -98.5 pp < 2 pp threshold (P_est=1.5% vs AskVWAP=100.0%) |
