# 📊 Отчёт симулятора Polymarket (Устав Grok Bot — Демо-счёт)
**Обновлено:** `2026-10-28 19:48:27 UTC`

## 💰 Состояние виртуального портфеля
| Показатель | Значение | Правило устава |
| :--- | :--- | :--- |
| **Стартовый капитал** | `$50.00 USDC` | Не добавлять деньги |
| **Текущий баланс (Equity)** | **`$27.08 USDC`** (`-22.92$` / `-45.85%`) | Cash + Mark-to-Market по CLOB Bid |
| **Свободный кэш / В сделках** | `$17.36` / `$9.72 USDC` | До 8 открытых позиций, макс 8% банка |
| **Цель окупаемости подписки** | `$-22.92 / $60.00` (`0.0%`) | Цель: +$60.00 в месяц |
| **Просадка от пика (Текущая / Макс)** | `23.33%` / `24.45%` (Пик: `$35.32`) | Стоп-кран при просадке 40% |
| **Закрытых сделок / Win Rate** | `72` / `59.7%` | Brier Score: `0.2524` |

## 📂 Открытые позиции (3 / 8)
| # | Рынок | Кат. | Исход | Вход (Ask VWAP) | Текущий Bid | Оценка бота | Размер ($) | Нереализ. PnL | Источник |
| :- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| #74 | Will the Milwaukee Brewers win the 2026 World Series? | Sports | **YES** | `0.953` | `0.908` | `98.0%` | `$4.06` | `$-0.19` | https://www.mlb.com/ |
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
| Spread: Timberwolves (-4.5) | Sports | NO | `97.5%` | `53.0%` | `+44.5 п.п.` | `1.00%` | REJECTED: Contract price $0.530 outside sweet spot [$0.76, $0.89] |
| Game Handicap: TS (-1.5) vs OG (+1.5) | Sports | YES | `1.5%` | `100.0%` | `-98.5 п.п.` | `100.00%` | REJECTED: Edge -98.5 pp < 2 pp threshold (P_est=1.5% vs AskVWAP=100.0%) |
| Spread: Lakers (-4.5) | Sports | NO | `97.5%` | `51.0%` | `+46.5 п.п.` | `1.00%` | REJECTED: Contract price $0.510 outside sweet spot [$0.76, $0.89] |
| Spread: Hawks (-3.5) | Sports | NO | `97.5%` | `55.0%` | `+42.5 п.п.` | `1.00%` | REJECTED: Contract price $0.550 outside sweet spot [$0.76, $0.89] |
| Spread: Jacksonville State (-3.5) | Sports | NO | `97.5%` | `55.0%` | `+42.5 п.п.` | `1.00%` | REJECTED: Contract price $0.550 outside sweet spot [$0.76, $0.89] |
| Spread: Raptors (-4.5) | Sports | NO | `97.5%` | `49.0%` | `+48.5 п.п.` | `1.00%` | REJECTED: Contract price $0.490 outside sweet spot [$0.76, $0.89] |
| Counter-Strike: Luminosity vs Envy (BO3) - Tesla C | Sports | YES | `1.5%` | `100.0%` | `-98.5 п.п.` | `100.00%` | REJECTED: Edge -98.5 pp < 2 pp threshold (P_est=1.5% vs AskVWAP=100.0%) |
| Counter-Strike: Team Nemesis vs Eternal Fire - Map | Sports | NO | `86.0%` | `92.0%` | `-6.0 п.п.` | `1.00%` | REJECTED: Edge -6.0 pp < 2 pp threshold (P_est=86.0% vs AskVWAP=92.0%) |
| Spread: Hawks (-3.5) | Sports | NO | `97.5%` | `56.0%` | `+41.5 п.п.` | `1.00%` | REJECTED: Contract price $0.560 outside sweet spot [$0.76, $0.89] |
| Spread: Jacksonville State (-3.5) | Sports | NO | `97.5%` | `55.0%` | `+42.5 п.п.` | `1.00%` | REJECTED: Contract price $0.550 outside sweet spot [$0.76, $0.89] |
| Counter-Strike: K27 vs B8 (BO3) - Tesla Cup Group  | Sports | YES | `1.5%` | `100.0%` | `-98.5 п.п.` | `100.00%` | REJECTED: Edge -98.5 pp < 2 pp threshold (P_est=1.5% vs AskVWAP=100.0%) |
| Counter-Strike: Liquid vs FURIA - Map 1 Winner | Sports | YES | `1.5%` | `100.0%` | `-98.5 п.п.` | `100.00%` | REJECTED: Edge -98.5 pp < 2 pp threshold (P_est=1.5% vs AskVWAP=100.0%) |
| Counter-Strike: DNK vs Dark Moon (BO3) - Exort Fie | Sports | YES | `1.5%` | `100.0%` | `-98.5 п.п.` | `100.00%` | REJECTED: Edge -98.5 pp < 2 pp threshold (P_est=1.5% vs AskVWAP=100.0%) |
| Spread: Hawks (-3.5) | Sports | NO | `97.5%` | `56.0%` | `+41.5 п.п.` | `1.00%` | REJECTED: Contract price $0.560 outside sweet spot [$0.76, $0.89] |
| Spread: Jacksonville State (-3.5) | Sports | NO | `97.5%` | `55.0%` | `+42.5 п.п.` | `1.00%` | REJECTED: Contract price $0.550 outside sweet spot [$0.76, $0.89] |
| Counter-Strike: Team Nemesis vs Eternal Fire (BO3) | Sports | NO | `83.0%` | `87.0%` | `-4.0 п.п.` | `2.00%` | REJECTED: Edge -4.0 pp < 2 pp threshold (P_est=83.0% vs AskVWAP=87.0%) |
| Counter-Strike: K27 vs B8 (BO3) - Tesla Cup Group  | Sports | YES | `1.5%` | `100.0%` | `-98.5 п.п.` | `100.00%` | REJECTED: Edge -98.5 pp < 2 pp threshold (P_est=1.5% vs AskVWAP=100.0%) |
| Spread: Steelers (-3.5) | Sports | NO | `97.5%` | `52.0%` | `+45.5 п.п.` | `1.00%` | REJECTED: Contract price $0.520 outside sweet spot [$0.76, $0.89] |
