# 📊 Отчёт симулятора Polymarket (Устав Grok Bot — Демо-счёт)
**Обновлено:** `2026-11-01 19:06:24 UTC`

## 💰 Состояние виртуального портфеля
| Показатель | Значение | Правило устава |
| :--- | :--- | :--- |
| **Стартовый капитал** | `$50.00 USDC` | Не добавлять деньги |
| **Текущий баланс (Equity)** | **`$27.97 USDC`** (`-22.03$` / `-44.06%`) | Cash + Mark-to-Market по CLOB Bid |
| **Свободный кэш / В сделках** | `$23.04` / `$4.93 USDC` | До 8 открытых позиций, макс 8% банка |
| **Цель окупаемости подписки** | `$-22.03 / $60.00` (`0.0%`) | Цель: +$60.00 в месяц |
| **Просадка от пика (Текущая / Макс)** | `20.80%` / `24.45%` (Пик: `$35.32`) | Стоп-кран при просадке 40% |
| **Закрытых сделок / Win Rate** | `82` / `63.4%` | Brier Score: `0.2242` |

## 📂 Открытые позиции (3 / 8)
| # | Рынок | Кат. | Исход | Вход (Ask VWAP) | Текущий Bid | Оценка бота | Размер ($) | Нереализ. PnL | Источник |
| :- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| #84 | Spread: Jets (-9.5) | Sports | **NO** | `0.790` | `0.750` | `82.0%` | `$1.59` | `$-0.08` | https://www.nfl.com/scores |
| #85 | Spread: Bills (-13.5) | Sports | **NO** | `0.810` | `0.660` | `84.0%` | `$1.77` | `$-0.33` | https://www.nfl.com/scores |
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
| Valorant: Gentle Mates GC vs KRÜ Blaze - Map 1 Win | Sports | NO | `1.5%` | `100.0%` | `-98.5 п.п.` | `100.00%` | REJECTED: Edge -98.5 pp < 2 pp threshold (P_est=1.5% vs AskVWAP=100.0%) |
| Counter-Strike: prodigy vs Ducks - Map 1 Winner | Sports | YES | `1.5%` | `100.0%` | `-98.5 п.п.` | `100.00%` | REJECTED: Edge -98.5 pp < 2 pp threshold (P_est=1.5% vs AskVWAP=100.0%) |
| Spread: Broncos (-3.5) | Sports | NO | `97.5%` | `65.0%` | `+32.5 п.п.` | `1.00%` | REJECTED: Contract price $0.650 outside sweet spot [$0.76, $0.89] |
| Counter-Strike: JiJieHao vs Iberian Soul (BO3) - C | Sports | YES | `1.5%` | `100.0%` | `-98.5 п.п.` | `100.00%` | REJECTED: Edge -98.5 pp < 2 pp threshold (P_est=1.5% vs AskVWAP=100.0%) |
| Counter-Strike: prodigy vs Ducks - Map 2 Winner | Sports | NO | `1.5%` | `100.0%` | `-98.5 п.п.` | `100.00%` | REJECTED: Edge -98.5 pp < 2 pp threshold (P_est=1.5% vs AskVWAP=100.0%) |
| Counter-Strike: JiJieHao vs Iberian Soul - Map 2 W | Sports | YES | `1.5%` | `100.0%` | `-98.5 п.п.` | `100.00%` | REJECTED: Edge -98.5 pp < 2 pp threshold (P_est=1.5% vs AskVWAP=100.0%) |
| Spread: Browns (-3.5) | Sports | NO | `97.5%` | `77.0%` | `+20.5 п.п.` | `1.00%` | REJECTED: Category cap reached (3/3 in Sports) |
| Dota 2: Xipto Esports vs potn9ki - Game 2 Winner | Sports | YES | `1.5%` | `100.0%` | `-98.5 п.п.` | `100.00%` | REJECTED: Edge -98.5 pp < 2 pp threshold (P_est=1.5% vs AskVWAP=100.0%) |
| Spread: Lions (-3.5) | Sports | NO | `97.5%` | `53.0%` | `+44.5 п.п.` | `1.00%` | REJECTED: Contract price $0.530 outside sweet spot [$0.76, $0.89] |
| Counter-Strike: Betclic Apogee Esports vs Phantom  | Sports | NO | `1.5%` | `100.0%` | `-98.5 п.п.` | `100.00%` | REJECTED: Edge -98.5 pp < 2 pp threshold (P_est=1.5% vs AskVWAP=100.0%) |
| Games Total: O/U 3.5 | Sports | YES | `89.0%` | `97.0%` | `-8.0 п.п.` | `12.00%` | REJECTED: Edge -8.0 pp < 2 pp threshold (P_est=89.0% vs AskVWAP=97.0%) |
| Spread: Lions (-3.5) | Sports | NO | `97.5%` | `53.0%` | `+44.5 п.п.` | `1.00%` | REJECTED: Contract price $0.530 outside sweet spot [$0.76, $0.89] |
| Counter-Strike: Betclic Apogee Esports vs Phantom  | Sports | NO | `1.5%` | `100.0%` | `-98.5 п.п.` | `100.00%` | REJECTED: Edge -98.5 pp < 2 pp threshold (P_est=1.5% vs AskVWAP=100.0%) |
| Will Real Racing Club vs. Real Madrid CF end in a  | Sports | NO | `96.5%` | `89.0%` | `+7.5 п.п.` | `1.00%` | REJECTED: Contract price $0.890 outside sweet spot [$0.76, $0.89] |
| Spread: Lions (-3.5) | Sports | NO | `97.5%` | `53.0%` | `+44.5 п.п.` | `1.00%` | REJECTED: Contract price $0.530 outside sweet spot [$0.76, $0.89] |
| Counter-Strike: JiJieHao vs Metizport - Map 2 Winn | Sports | YES | `1.5%` | `100.0%` | `-98.5 п.п.` | `100.00%` | REJECTED: Edge -98.5 pp < 2 pp threshold (P_est=1.5% vs AskVWAP=100.0%) |
| Counter-Strike: HOTU vs 1WIN (BO3) - Moscow Cyber  | Sports | NO | `84.5%` | `89.0%` | `-4.5 п.п.` | `1.00%` | REJECTED: Edge -4.5 pp < 2 pp threshold (P_est=84.5% vs AskVWAP=89.0%) |
| Counter-Strike: JiJieHao vs Metizport (BO3) - Circ | Sports | YES | `1.5%` | `100.0%` | `-98.5 п.п.` | `100.00%` | REJECTED: Edge -98.5 pp < 2 pp threshold (P_est=1.5% vs AskVWAP=100.0%) |
