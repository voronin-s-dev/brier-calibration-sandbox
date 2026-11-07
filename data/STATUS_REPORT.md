# 📊 Отчёт симулятора Polymarket (Устав Grok Bot — Демо-счёт)
**Обновлено:** `2026-11-07 22:10:19 UTC`

## 💰 Состояние виртуального портфеля
| Показатель | Значение | Правило устава |
| :--- | :--- | :--- |
| **Стартовый капитал** | `$50.00 USDC` | Не добавлять деньги |
| **Текущий баланс (Equity)** | **`$31.75 USDC`** (`-18.25$` / `-36.50%`) | Cash + Mark-to-Market по CLOB Bid |
| **Свободный кэш / В сделках** | `$29.41` / `$2.33 USDC` | До 8 открытых позиций, макс 8% банка |
| **Цель окупаемости подписки** | `$-18.25 / $60.00` (`0.0%`) | Цель: +$60.00 в месяц |
| **Просадка от пика (Текущая / Макс)** | `10.11%` / `24.45%` (Пик: `$35.32`) | Стоп-кран при просадке 40% |
| **Закрытых сделок / Win Rate** | `99` / `70.7%` | Brier Score: `0.1960` |

## 📂 Открытые позиции (1 / 8)
| # | Рынок | Кат. | Исход | Вход (Ask VWAP) | Текущий Bid | Оценка бота | Размер ($) | Нереализ. PnL | Источник |
| :- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| #100 | Spread: Colts (-3.5) | Sports | **NO** | `0.840` | `0.810` | `97.5%` | `$2.42` | `$-0.09` | https://www.nfl.com/scores |

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
| Spread: Giants (-3.5) | Sports | NO | `97.5%` | `55.0%` | `+42.5 п.п.` | `1.00%` | REJECTED: Contract price $0.550 outside sweet spot [$0.76, $0.92] |
| Dota 2: Yakult Brothers vs Amaru Gaming (BO3) - Dr | Sports | YES | `1.5%` | `100.0%` | `-98.5 п.п.` | `100.00%` | REJECTED: Edge -98.5 pp < 2 pp threshold (P_est=1.5% vs AskVWAP=100.0%) |
| Spread: Giants (-3.5) | Sports | NO | `97.5%` | `55.0%` | `+42.5 п.п.` | `1.00%` | REJECTED: Contract price $0.550 outside sweet spot [$0.76, $0.92] |
| Spread: Giants (-3.5) | Sports | NO | `97.5%` | `55.0%` | `+42.5 п.п.` | `1.00%` | REJECTED: Contract price $0.550 outside sweet spot [$0.76, $0.92] |
| Dota 2: Froglings vs angry birds (BO3) - 1win Esse | Sports | NO | `1.5%` | `100.0%` | `-98.5 п.п.` | `100.00%` | REJECTED: Edge -98.5 pp < 2 pp threshold (P_est=1.5% vs AskVWAP=100.0%) |
| Spread: Giants (-3.5) | Sports | NO | `97.5%` | `55.0%` | `+42.5 п.п.` | `1.00%` | REJECTED: Contract price $0.550 outside sweet spot [$0.76, $0.92] |
| Dota 2: Froglings vs angry birds (BO3) - 1win Esse | Sports | NO | `1.5%` | `100.0%` | `-98.5 п.п.` | `100.00%` | REJECTED: Edge -98.5 pp < 2 pp threshold (P_est=1.5% vs AskVWAP=100.0%) |
| Spread: Giants (-3.5) | Sports | NO | `97.5%` | `55.0%` | `+42.5 п.п.` | `1.00%` | REJECTED: Contract price $0.550 outside sweet spot [$0.76, $0.92] |
| Dota 2: Froglings vs angry birds (BO3) - 1win Esse | Sports | NO | `1.5%` | `100.0%` | `-98.5 п.п.` | `100.00%` | REJECTED: Edge -98.5 pp < 2 pp threshold (P_est=1.5% vs AskVWAP=100.0%) |
| Spread: Giants (-3.5) | Sports | NO | `97.5%` | `55.0%` | `+42.5 п.п.` | `1.00%` | REJECTED: Contract price $0.550 outside sweet spot [$0.76, $0.92] |
| Dota 2: Yakult Brothers vs Amaru Gaming - Game 2 W | Sports | YES | `1.5%` | `100.0%` | `-98.5 п.п.` | `100.00%` | REJECTED: Edge -98.5 pp < 2 pp threshold (P_est=1.5% vs AskVWAP=100.0%) |
| Dota 2: Froglings vs angry birds (BO3) - 1win Esse | Sports | NO | `1.5%` | `100.0%` | `-98.5 п.п.` | `100.00%` | REJECTED: Edge -98.5 pp < 2 pp threshold (P_est=1.5% vs AskVWAP=100.0%) |
| Dota 2: InterActive Philippines vs PuckChamp (BO3) | Sports | YES | `1.5%` | `100.0%` | `-98.5 п.п.` | `100.00%` | REJECTED: Edge -98.5 pp < 2 pp threshold (P_est=1.5% vs AskVWAP=100.0%) |
| Counter-Strike: Nexus vs FORZE Reload (BO3) - CCT  | Sports | NO | `1.5%` | `100.0%` | `-98.5 п.п.` | `100.00%` | REJECTED: Edge -98.5 pp < 2 pp threshold (P_est=1.5% vs AskVWAP=100.0%) |
| Spread: Giants (-3.5) | Sports | NO | `97.5%` | `55.0%` | `+42.5 п.п.` | `1.00%` | REJECTED: Contract price $0.550 outside sweet spot [$0.76, $0.92] |
| Dota 2: Yakult Brothers vs Amaru Gaming - Game 2 W | Sports | YES | `1.5%` | `100.0%` | `-98.5 п.п.` | `100.00%` | REJECTED: Edge -98.5 pp < 2 pp threshold (P_est=1.5% vs AskVWAP=100.0%) |
| Dota 2: Froglings vs angry birds (BO3) - 1win Esse | Sports | NO | `1.5%` | `100.0%` | `-98.5 п.п.` | `100.00%` | REJECTED: Edge -98.5 pp < 2 pp threshold (P_est=1.5% vs AskVWAP=100.0%) |
| Dota 2: InterActive Philippines vs PuckChamp (BO3) | Sports | YES | `1.5%` | `100.0%` | `-98.5 п.п.` | `100.00%` | REJECTED: Edge -98.5 pp < 2 pp threshold (P_est=1.5% vs AskVWAP=100.0%) |
