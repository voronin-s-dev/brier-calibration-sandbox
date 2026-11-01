# 📊 Отчёт симулятора Polymarket (Устав Grok Bot — Демо-счёт)
**Обновлено:** `2026-11-01 00:41:16 UTC`

## 💰 Состояние виртуального портфеля
| Показатель | Значение | Правило устава |
| :--- | :--- | :--- |
| **Стартовый капитал** | `$50.00 USDC` | Не добавлять деньги |
| **Текущий баланс (Equity)** | **`$27.98 USDC`** (`-22.02$` / `-44.04%`) | Cash + Mark-to-Market по CLOB Bid |
| **Свободный кэш / В сделках** | `$22.51` / `$5.47 USDC` | До 8 открытых позиций, макс 8% банка |
| **Цель окупаемости подписки** | `$-22.02 / $60.00` (`0.0%`) | Цель: +$60.00 в месяц |
| **Просадка от пика (Текущая / Макс)** | `20.77%` / `24.45%` (Пик: `$35.32`) | Стоп-кран при просадке 40% |
| **Закрытых сделок / Win Rate** | `81` / `63.0%` | Brier Score: `0.2333` |

## 📂 Открытые позиции (3 / 8)
| # | Рынок | Кат. | Исход | Вход (Ask VWAP) | Текущий Bid | Оценка бота | Размер ($) | Нереализ. PnL | Источник |
| :- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| #81 | Timberwolves vs. Spurs | Sports | **NO** | `0.850` | `0.850` | `91.0%` | `$2.15` | `$-0.00` | https://www.nba.com/ |
| #84 | Spread: Jets (-9.5) | Sports | **NO** | `0.790` | `0.780` | `82.0%` | `$1.59` | `$-0.02` | https://www.nfl.com/scores |
| #85 | Spread: Bills (-13.5) | Sports | **NO** | `0.810` | `0.800` | `84.0%` | `$1.77` | `$-0.02` | https://www.nfl.com/scores |

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
| Counter-Strike: NRG vs Wildcard - Map 2 Winner | Sports | NO | `1.5%` | `100.0%` | `-98.5 п.п.` | `100.00%` | REJECTED: Edge -98.5 pp < 2 pp threshold (P_est=1.5% vs AskVWAP=100.0%) |
| Counter-Strike: 100 Thieves vs Isurus (BO3) - FiRe | Sports | NO | `1.5%` | `100.0%` | `-98.5 п.п.` | `100.00%` | REJECTED: Edge -98.5 pp < 2 pp threshold (P_est=1.5% vs AskVWAP=100.0%) |
| Spread: Browns (-3.5) | Sports | NO | `97.5%` | `76.0%` | `+21.5 п.п.` | `1.00%` | REJECTED: Category cap reached (3/3 in Sports) |
| Spread: Lions (-3.5) | Sports | NO | `97.5%` | `53.0%` | `+44.5 п.п.` | `1.00%` | REJECTED: Contract price $0.530 outside sweet spot [$0.76, $0.89] |
| Will Real Racing Club vs. Real Madrid CF end in a  | Sports | NO | `96.5%` | `90.0%` | `+6.5 п.п.` | `1.00%` | REJECTED: Contract price $0.900 outside sweet spot [$0.76, $0.89] |
| Counter-Strike: NRG vs Wildcard - Map 2 Winner | Sports | NO | `1.5%` | `100.0%` | `-98.5 п.п.` | `100.00%` | REJECTED: Edge -98.5 pp < 2 pp threshold (P_est=1.5% vs AskVWAP=100.0%) |
| Games Total: O/U 2.5 | Sports | YES | `1.5%` | `100.0%` | `-98.5 п.п.` | `100.00%` | REJECTED: Edge -98.5 pp < 2 pp threshold (P_est=1.5% vs AskVWAP=100.0%) |
| Counter-Strike: 100 Thieves vs Isurus (BO3) - FiRe | Sports | NO | `1.5%` | `100.0%` | `-98.5 п.п.` | `100.00%` | REJECTED: Edge -98.5 pp < 2 pp threshold (P_est=1.5% vs AskVWAP=100.0%) |
| Spread: Browns (-3.5) | Sports | NO | `97.5%` | `76.0%` | `+21.5 п.п.` | `1.00%` | REJECTED: Category cap reached (3/3 in Sports) |
| Game Handicap: HLE (-1.5) vs Bilibili Gaming (+1.5 | Sports | YES | `1.5%` | `100.0%` | `-98.5 п.п.` | `100.00%` | REJECTED: Edge -98.5 pp < 2 pp threshold (P_est=1.5% vs AskVWAP=100.0%) |
| Spread: Lions (-3.5) | Sports | NO | `97.5%` | `53.0%` | `+44.5 п.п.` | `1.00%` | REJECTED: Contract price $0.530 outside sweet spot [$0.76, $0.89] |
| LoL: Hanwha Life Esports vs Bilibili Gaming - Game | Sports | YES | `1.5%` | `100.0%` | `-98.5 п.п.` | `100.00%` | REJECTED: Edge -98.5 pp < 2 pp threshold (P_est=1.5% vs AskVWAP=100.0%) |
| LoL: Hanwha Life Esports vs Bilibili Gaming (BO3)  | Sports | YES | `1.5%` | `100.0%` | `-98.5 п.п.` | `100.00%` | REJECTED: Edge -98.5 pp < 2 pp threshold (P_est=1.5% vs AskVWAP=100.0%) |
| Will Real Racing Club vs. Real Madrid CF end in a  | Sports | NO | `96.5%` | `90.0%` | `+6.5 п.п.` | `1.00%` | REJECTED: Contract price $0.900 outside sweet spot [$0.76, $0.89] |
| Counter-Strike: NRG vs Wildcard - Map 2 Winner | Sports | NO | `1.5%` | `100.0%` | `-98.5 п.п.` | `100.00%` | REJECTED: Edge -98.5 pp < 2 pp threshold (P_est=1.5% vs AskVWAP=100.0%) |
| Counter-Strike: 100 Thieves vs Isurus (BO3) - FiRe | Sports | NO | `1.5%` | `100.0%` | `-98.5 п.п.` | `100.00%` | REJECTED: Edge -98.5 pp < 2 pp threshold (P_est=1.5% vs AskVWAP=100.0%) |
| Games Total: O/U 2.5 | Sports | YES | `1.5%` | `100.0%` | `-98.5 п.п.` | `100.00%` | REJECTED: Edge -98.5 pp < 2 pp threshold (P_est=1.5% vs AskVWAP=100.0%) |
| Spread: Browns (-3.5) | Sports | NO | `97.5%` | `76.0%` | `+21.5 п.п.` | `1.00%` | REJECTED: Category cap reached (3/3 in Sports) |
