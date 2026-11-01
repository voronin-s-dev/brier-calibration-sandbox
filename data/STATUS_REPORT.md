# 📊 Отчёт симулятора Polymarket (Устав Grok Bot — Демо-счёт)
**Обновлено:** `2026-11-01 06:52:51 UTC`

## 💰 Состояние виртуального портфеля
| Показатель | Значение | Правило устава |
| :--- | :--- | :--- |
| **Стартовый капитал** | `$50.00 USDC` | Не добавлять деньги |
| **Текущий баланс (Equity)** | **`$28.34 USDC`** (`-21.66$` / `-43.32%`) | Cash + Mark-to-Market по CLOB Bid |
| **Свободный кэш / В сделках** | `$23.04` / `$5.29 USDC` | До 8 открытых позиций, макс 8% банка |
| **Цель окупаемости подписки** | `$-21.66 / $60.00` (`0.0%`) | Цель: +$60.00 в месяц |
| **Просадка от пика (Текущая / Макс)** | `19.76%` / `24.45%` (Пик: `$35.32`) | Стоп-кран при просадке 40% |
| **Закрытых сделок / Win Rate** | `82` / `63.4%` | Brier Score: `0.2242` |

## 📂 Открытые позиции (3 / 8)
| # | Рынок | Кат. | Исход | Вход (Ask VWAP) | Текущий Bid | Оценка бота | Размер ($) | Нереализ. PnL | Источник |
| :- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| #84 | Spread: Jets (-9.5) | Sports | **NO** | `0.790` | `0.780` | `82.0%` | `$1.59` | `$-0.02` | https://www.nfl.com/scores |
| #85 | Spread: Bills (-13.5) | Sports | **NO** | `0.810` | `0.800` | `84.0%` | `$1.77` | `$-0.02` | https://www.nfl.com/scores |
| #86 | Spread: Commanders (-17.5) | Sports | **NO** | `0.830` | `0.820` | `86.0%` | `$2.00` | `$-0.02` | https://www.nfl.com/scores |

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
| Counter-Strike: FlyQuest vs Alter Ego (BO5) - DFRA | Sports | NO | `1.5%` | `100.0%` | `-98.5 п.п.` | `100.00%` | REJECTED: Edge -98.5 pp < 2 pp threshold (P_est=1.5% vs AskVWAP=100.0%) |
| Counter-Strike: FlyQuest vs Alter Ego - Map 3 Winn | Sports | NO | `1.5%` | `100.0%` | `-98.5 п.п.` | `100.00%` | REJECTED: Edge -98.5 pp < 2 pp threshold (P_est=1.5% vs AskVWAP=100.0%) |
| Spread: Browns (-3.5) | Sports | NO | `97.5%` | `76.0%` | `+21.5 п.п.` | `1.00%` | REJECTED: Category cap reached (3/3 in Sports) |
| Spread: Lions (-3.5) | Sports | NO | `97.5%` | `53.0%` | `+44.5 п.п.` | `1.00%` | REJECTED: Contract price $0.530 outside sweet spot [$0.76, $0.89] |
| Will Real Racing Club vs. Real Madrid CF end in a  | Sports | NO | `96.5%` | `89.0%` | `+7.5 п.п.` | `1.00%` | REJECTED: Contract price $0.890 outside sweet spot [$0.76, $0.89] |
| Counter-Strike: FlyQuest vs Alter Ego (BO5) - DFRA | Sports | NO | `1.5%` | `100.0%` | `-98.5 п.п.` | `100.00%` | REJECTED: Edge -98.5 pp < 2 pp threshold (P_est=1.5% vs AskVWAP=100.0%) |
| Counter-Strike: FlyQuest vs Alter Ego - Map 3 Winn | Sports | NO | `1.5%` | `100.0%` | `-98.5 п.п.` | `100.00%` | REJECTED: Edge -98.5 pp < 2 pp threshold (P_est=1.5% vs AskVWAP=100.0%) |
| Spread: Browns (-3.5) | Sports | NO | `97.5%` | `76.0%` | `+21.5 п.п.` | `1.00%` | REJECTED: Category cap reached (3/3 in Sports) |
| Spread: Commanders (-17.5) | Sports | NO | `86.0%` | `83.0%` | `+3.0 п.п.` | `1.00%` | EXECUTED BUY #86 ($2.00 @ 0.8300) |
| Spread: Lions (-3.5) | Sports | NO | `97.5%` | `53.0%` | `+44.5 п.п.` | `1.00%` | REJECTED: Contract price $0.530 outside sweet spot [$0.76, $0.89] |
| Will Real Racing Club vs. Real Madrid CF end in a  | Sports | NO | `96.5%` | `89.0%` | `+7.5 п.п.` | `1.00%` | REJECTED: Contract price $0.890 outside sweet spot [$0.76, $0.89] |
| Counter-Strike: NRG vs Wildcard - Map 2 Winner | Sports | NO | `1.5%` | `100.0%` | `-98.5 п.п.` | `100.00%` | REJECTED: Edge -98.5 pp < 2 pp threshold (P_est=1.5% vs AskVWAP=100.0%) |
| Counter-Strike: 100 Thieves vs Isurus (BO3) - FiRe | Sports | NO | `1.5%` | `100.0%` | `-98.5 п.п.` | `100.00%` | REJECTED: Edge -98.5 pp < 2 pp threshold (P_est=1.5% vs AskVWAP=100.0%) |
| Spread: Browns (-3.5) | Sports | NO | `97.5%` | `76.0%` | `+21.5 п.п.` | `1.00%` | REJECTED: Category cap reached (3/3 in Sports) |
| Spread: Lions (-3.5) | Sports | NO | `97.5%` | `53.0%` | `+44.5 п.п.` | `1.00%` | REJECTED: Contract price $0.530 outside sweet spot [$0.76, $0.89] |
| Will Real Racing Club vs. Real Madrid CF end in a  | Sports | NO | `96.5%` | `90.0%` | `+6.5 п.п.` | `1.00%` | REJECTED: Contract price $0.900 outside sweet spot [$0.76, $0.89] |
| Counter-Strike: NRG vs Wildcard - Map 2 Winner | Sports | NO | `1.5%` | `100.0%` | `-98.5 п.п.` | `100.00%` | REJECTED: Edge -98.5 pp < 2 pp threshold (P_est=1.5% vs AskVWAP=100.0%) |
