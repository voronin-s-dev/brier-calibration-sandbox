# 📊 Отчёт симулятора Polymarket (Устав Grok Bot — Демо-счёт)
**Обновлено:** `2026-10-29 23:04:48 UTC`

## 💰 Состояние виртуального портфеля
| Показатель | Значение | Правило устава |
| :--- | :--- | :--- |
| **Стартовый капитал** | `$50.00 USDC` | Не добавлять деньги |
| **Текущий баланс (Equity)** | **`$28.53 USDC`** (`-21.47$` / `-42.94%`) | Cash + Mark-to-Market по CLOB Bid |
| **Свободный кэш / В сделках** | `$21.13` / `$7.40 USDC` | До 8 открытых позиций, макс 8% банка |
| **Цель окупаемости подписки** | `$-21.47 / $60.00` (`0.0%`) | Цель: +$60.00 в месяц |
| **Просадка от пика (Текущая / Макс)** | `19.22%` / `24.45%` (Пик: `$35.32`) | Стоп-кран при просадке 40% |
| **Закрытых сделок / Win Rate** | `76` / `61.8%` | Brier Score: `0.2283` |

## 📂 Открытые позиции (3 / 8)
| # | Рынок | Кат. | Исход | Вход (Ask VWAP) | Текущий Bid | Оценка бота | Размер ($) | Нереализ. PnL | Источник |
| :- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| #75 | Will FC Barcelona win on 2026-10-31? | Sports | **YES** | `0.890` | `0.870` | `91.0%` | `$3.78` | `$-0.08` | https://www.laliga.com/ |
| #79 | LoL: Hanwha Life Esports vs G2 Esports (BO3) - Worlds G | Sports | **YES** | `0.790` | `0.780` | `82.0%` | `$1.61` | `$-0.02` | https://gol.gg/esports/home |
| #80 | Counter-Strike: Nemiga vs Vitality (BO3) - PGL Masters  | Sports | **NO** | `0.840` | `0.830` | `87.0%` | `$2.14` | `$-0.03` | https://hltv.org |

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
| Spread: Broncos (-3.5) | Sports | NO | `97.5%` | `66.0%` | `+31.5 п.п.` | `1.00%` | REJECTED: Contract price $0.660 outside sweet spot [$0.76, $0.89] |
| Dota 2: Rottweilas Latam vs Roshan Hunters (BO3) - | Sports | NO | `1.5%` | `100.0%` | `-98.5 п.п.` | `100.00%` | REJECTED: Edge -98.5 pp < 2 pp threshold (P_est=1.5% vs AskVWAP=100.0%) |
| Games Total: O/U 2.5 | Sports | YES | `1.5%` | `100.0%` | `-98.5 п.п.` | `100.00%` | REJECTED: Edge -98.5 pp < 2 pp threshold (P_est=1.5% vs AskVWAP=100.0%) |
| Game Handicap: KC (-1.5) vs CTBC Flying Oyster (+1 | Sports | NO | `1.5%` | `100.0%` | `-98.5 п.п.` | `100.00%` | REJECTED: Edge -98.5 pp < 2 pp threshold (P_est=1.5% vs AskVWAP=100.0%) |
| Spread: Packers (-3.5) | Sports | NO | `97.5%` | `50.0%` | `+47.5 п.п.` | `1.00%` | REJECTED: Contract price $0.500 outside sweet spot [$0.76, $0.89] |
| LoL: Karmine Corp vs CTBC Flying Oyster (BO3) - Wo | Sports | NO | `1.5%` | `100.0%` | `-98.5 п.п.` | `100.00%` | REJECTED: Edge -98.5 pp < 2 pp threshold (P_est=1.5% vs AskVWAP=100.0%) |
| LoL: Karmine Corp vs CTBC Flying Oyster - Game 2 W | Sports | NO | `1.5%` | `100.0%` | `-98.5 п.п.` | `100.00%` | REJECTED: Edge -98.5 pp < 2 pp threshold (P_est=1.5% vs AskVWAP=100.0%) |
| Spread: Broncos (-3.5) | Sports | NO | `97.5%` | `66.0%` | `+31.5 п.п.` | `1.00%` | REJECTED: Contract price $0.660 outside sweet spot [$0.76, $0.89] |
| Dota 2: Rottweilas Latam vs Roshan Hunters (BO3) - | Sports | NO | `1.5%` | `100.0%` | `-98.5 п.п.` | `100.00%` | REJECTED: Edge -98.5 pp < 2 pp threshold (P_est=1.5% vs AskVWAP=100.0%) |
| Games Total: O/U 2.5 | Sports | YES | `1.5%` | `100.0%` | `-98.5 п.п.` | `100.00%` | REJECTED: Edge -98.5 pp < 2 pp threshold (P_est=1.5% vs AskVWAP=100.0%) |
| Counter-Strike: Nemiga vs Vitality (BO3) - PGL Mas | Sports | NO | `87.0%` | `84.0%` | `+3.0 п.п.` | `1.00%` | EXECUTED BUY #80 ($2.14 @ 0.8400) |
| Game Handicap: KC (-1.5) vs CTBC Flying Oyster (+1 | Sports | NO | `1.5%` | `100.0%` | `-98.5 п.п.` | `100.00%` | REJECTED: Edge -98.5 pp < 2 pp threshold (P_est=1.5% vs AskVWAP=100.0%) |
| Spread: Packers (-3.5) | Sports | NO | `97.5%` | `50.0%` | `+47.5 п.п.` | `1.00%` | REJECTED: Contract price $0.500 outside sweet spot [$0.76, $0.89] |
| LoL: Karmine Corp vs CTBC Flying Oyster (BO3) - Wo | Sports | NO | `1.5%` | `100.0%` | `-98.5 п.п.` | `100.00%` | REJECTED: Edge -98.5 pp < 2 pp threshold (P_est=1.5% vs AskVWAP=100.0%) |
| LoL: Karmine Corp vs CTBC Flying Oyster - Game 1 W | Sports | NO | `1.5%` | `100.0%` | `-98.5 п.п.` | `100.00%` | REJECTED: Edge -98.5 pp < 2 pp threshold (P_est=1.5% vs AskVWAP=100.0%) |
| LoL: Karmine Corp vs CTBC Flying Oyster - Game 2 W | Sports | NO | `1.5%` | `100.0%` | `-98.5 п.п.` | `100.00%` | REJECTED: Edge -98.5 pp < 2 pp threshold (P_est=1.5% vs AskVWAP=100.0%) |
| Counter-Strike: Fortress vs DNK (BO3) - Exort Fies | Sports | YES | `1.5%` | `100.0%` | `-98.5 п.п.` | `100.00%` | REJECTED: Edge -98.5 pp < 2 pp threshold (P_est=1.5% vs AskVWAP=100.0%) |
| Spread: Packers (-4.5) | Sports | NO | `97.5%` | `55.0%` | `+42.5 п.п.` | `1.00%` | REJECTED: Contract price $0.550 outside sweet spot [$0.76, $0.89] |
