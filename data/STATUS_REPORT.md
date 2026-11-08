# 📊 Отчёт симулятора Polymarket (Устав Grok Bot — Демо-счёт)
**Обновлено:** `2026-11-08 09:10:21 UTC`

## 💰 Состояние виртуального портфеля
| Показатель | Значение | Правило устава |
| :--- | :--- | :--- |
| **Стартовый капитал** | `$50.00 USDC` | Не добавлять деньги |
| **Текущий баланс (Equity)** | **`$33.88 USDC`** (`-16.12$` / `-32.24%`) | Cash + Mark-to-Market по CLOB Bid |
| **Свободный кэш / В сделках** | `$18.40` / `$15.48 USDC` | До 8 открытых позиций, макс 8% банка |
| **Цель окупаемости подписки** | `$-16.12 / $60.00` (`0.0%`) | Цель: +$60.00 в месяц |
| **Просадка от пика (Текущая / Макс)** | `4.07%` / `24.45%` (Пик: `$35.32`) | Стоп-кран при просадке 40% |
| **Закрытых сделок / Win Rate** | `94` / `78.7%` | Brier Score: `0.1849` |

## 📂 Открытые позиции (6 / 8)
| # | Рынок | Кат. | Исход | Вход (Ask VWAP) | Текущий Bid | Оценка бота | Размер ($) | Нереализ. PnL | Источник |
| :- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| #100 | Spread: Colts (-3.5) | Sports | **NO** | `0.840` | `0.790` | `97.5%` | `$2.42` | `$-0.14` | https://www.nfl.com/scores |
| #107 | Spread: Commanders (-3.5) | Sports | **NO** | `0.790` | `0.780` | `97.5%` | `$2.56` | `$-0.03` | https://www.nfl.com/scores |
| #110 | Spread: Dolphins (-3.5) | Sports | **NO** | `0.840` | `0.830` | `97.5%` | `$2.58` | `$-0.03` | https://www.nfl.com/scores |
| #114 | Spread: Chargers (-3.5) | Sports | **NO** | `0.810` | `0.800` | `97.5%` | `$2.68` | `$-0.03` | https://www.nfl.com/scores |
| #115 | Will FC RFS win on 2026-11-08? | Sports | **NO** | `0.919` | `0.960` | `98.5%` | `$2.68` | `$+0.12` | https://www.virsliga.lv/ |
| #117 | Brighton & Hove Albion FC vs. Brentford FC: O/U 5.5 | Sports | **NO** | `0.910` | `0.900` | `94.0%` | `$2.71` | `$-0.03` | https://www.premierleague.com/ |

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
| Spread: Rams (-3.5) | Sports | NO | `97.5%` | `48.0%` | `+49.5 п.п.` | `1.00%` | REJECTED: Contract price $0.480 outside sweet spot [$0.76, $0.92] |
| Spread: Eagles (-3.5) | Sports | NO | `97.5%` | `73.0%` | `+24.5 п.п.` | `1.00%` | REJECTED: Contract price $0.730 outside sweet spot [$0.76, $0.92] |
| Spread: 49ers (-3.5) | Sports | NO | `97.5%` | `29.0%` | `+68.5 п.п.` | `1.00%` | REJECTED: Contract price $0.290 outside sweet spot [$0.76, $0.92] |
| Spread: Rams (-4.5) | Sports | NO | `97.5%` | `51.0%` | `+46.5 п.п.` | `1.00%` | REJECTED: Contract price $0.510 outside sweet spot [$0.76, $0.92] |
| Spread: Bengals (-3.5) | Sports | NO | `97.5%` | `54.0%` | `+43.5 п.п.` | `1.00%` | REJECTED: Contract price $0.540 outside sweet spot [$0.76, $0.92] |
| Spread: Giants (-3.5) | Sports | NO | `97.5%` | `56.0%` | `+41.5 п.п.` | `1.00%` | REJECTED: Contract price $0.560 outside sweet spot [$0.76, $0.92] |
| Counter-Strike: TheMongolz vs MOUZ - Map 2 Winner | Sports | YES | `1.5%` | `100.0%` | `-98.5 п.п.` | `100.00%` | REJECTED: Edge -98.5 pp < 2 pp threshold (P_est=1.5% vs AskVWAP=100.0%) |
| Spread: Chiefs (-3.5) | Sports | NO | `97.5%` | `30.0%` | `+67.5 п.п.` | `1.00%` | REJECTED: Contract price $0.300 outside sweet spot [$0.76, $0.92] |
| Spread: Rams (-3.5) | Sports | NO | `97.5%` | `48.0%` | `+49.5 п.п.` | `1.00%` | REJECTED: Contract price $0.480 outside sweet spot [$0.76, $0.92] |
| Spread: Eagles (-3.5) | Sports | NO | `97.5%` | `73.0%` | `+24.5 п.п.` | `1.00%` | REJECTED: Contract price $0.730 outside sweet spot [$0.76, $0.92] |
| Spread: 49ers (-3.5) | Sports | NO | `97.5%` | `29.0%` | `+68.5 п.п.` | `1.00%` | REJECTED: Contract price $0.290 outside sweet spot [$0.76, $0.92] |
| Spread: Rams (-4.5) | Sports | NO | `97.5%` | `51.0%` | `+46.5 п.п.` | `1.00%` | REJECTED: Contract price $0.510 outside sweet spot [$0.76, $0.92] |
| Spread: Bengals (-3.5) | Sports | NO | `97.5%` | `54.0%` | `+43.5 п.п.` | `1.00%` | REJECTED: Contract price $0.540 outside sweet spot [$0.76, $0.92] |
| Spread: Giants (-3.5) | Sports | NO | `97.5%` | `56.0%` | `+41.5 п.п.` | `1.00%` | REJECTED: Contract price $0.560 outside sweet spot [$0.76, $0.92] |
| Spread: Rams (-3.5) | Sports | NO | `97.5%` | `48.0%` | `+49.5 п.п.` | `1.00%` | REJECTED: Contract price $0.480 outside sweet spot [$0.76, $0.92] |
| Spread: Eagles (-3.5) | Sports | NO | `97.5%` | `73.0%` | `+24.5 п.п.` | `1.00%` | REJECTED: Contract price $0.730 outside sweet spot [$0.76, $0.92] |
| Spread: 49ers (-3.5) | Sports | NO | `97.5%` | `29.0%` | `+68.5 п.п.` | `1.00%` | REJECTED: Contract price $0.290 outside sweet spot [$0.76, $0.92] |
| Spread: Rams (-4.5) | Sports | NO | `97.5%` | `51.0%` | `+46.5 п.п.` | `1.00%` | REJECTED: Contract price $0.510 outside sweet spot [$0.76, $0.92] |
