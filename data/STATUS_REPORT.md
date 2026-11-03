# 📊 Отчёт симулятора Polymarket (Устав Grok Bot — Демо-счёт)
**Обновлено:** `2026-11-03 02:53:46 UTC`

## 💰 Состояние виртуального портфеля
| Показатель | Значение | Правило устава |
| :--- | :--- | :--- |
| **Стартовый капитал** | `$50.00 USDC` | Не добавлять деньги |
| **Текущий баланс (Equity)** | **`$27.92 USDC`** (`-22.08$` / `-44.16%`) | Cash + Mark-to-Market по CLOB Bid |
| **Свободный кэш / В сделках** | `$25.64` / `$2.28 USDC` | До 8 открытых позиций, макс 8% банка |
| **Цель окупаемости подписки** | `$-22.08 / $60.00` (`0.0%`) | Цель: +$60.00 в месяц |
| **Просадка от пика (Текущая / Макс)** | `20.94%` / `24.45%` (Пик: `$35.32`) | Стоп-кран при просадке 40% |
| **Закрытых сделок / Win Rate** | `88` / `64.8%` | Brier Score: `0.2194` |

## 📂 Открытые позиции (2 / 8)
| # | Рынок | Кат. | Исход | Вход (Ask VWAP) | Текущий Bid | Оценка бота | Размер ($) | Нереализ. PnL | Источник |
| :- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| #88 | Kings vs. Mavericks | Sports | **NO** | `0.800` | `0.470` | `82.0%` | `$1.09` | `$-0.45` | https://www.nba.com/ |
| #91 | Will Villarreal CF win on 2026-11-03? | Sports | **NO** | `0.800` | `0.790` | `83.0%` | `$1.66` | `$-0.02` | https://www.uefa.com/ |

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
| Counter-Strike: Liquid vs PARIVISION - Map 1 Winne | Sports | YES | `1.5%` | `100.0%` | `-98.5 п.п.` | `100.00%` | REJECTED: Edge -98.5 pp < 2 pp threshold (P_est=1.5% vs AskVWAP=100.0%) |
| Will Villarreal CF win on 2026-11-03? | Sports | NO | `83.0%` | `80.0%` | `+3.0 п.п.` | `1.00%` | EXECUTED BUY #91 ($1.66 @ 0.8000) |
| Counter-Strike: Aurora Gaming vs G2 - Map 1 Winner | Sports | YES | `94.0%` | `87.0%` | `+7.0 п.п.` | `1.00%` | REJECTED: Category cap reached (3/3 in Sports) |
| Spread: Hawks (-3.5) | Sports | NO | `97.5%` | `33.0%` | `+64.5 п.п.` | `1.00%` | REJECTED: Contract price $0.330 outside sweet spot [$0.76, $0.89] |
| Spread: Cavaliers (-4.5) | Sports | NO | `97.5%` | `52.0%` | `+45.5 п.п.` | `1.00%` | REJECTED: Contract price $0.520 outside sweet spot [$0.76, $0.89] |
| Spread: Hawks (-4.5) | Sports | NO | `97.5%` | `37.0%` | `+60.5 п.п.` | `1.00%` | REJECTED: Contract price $0.370 outside sweet spot [$0.76, $0.89] |
| Dota 2: GamerLegion vs CyberHero - Game 1 Winner | Sports | NO | `1.5%` | `100.0%` | `-98.5 п.п.` | `100.00%` | REJECTED: Edge -98.5 pp < 2 pp threshold (P_est=1.5% vs AskVWAP=100.0%) |
| Spread: Rockets (-4.5) | Sports | NO | `97.5%` | `48.0%` | `+49.5 п.п.` | `1.00%` | REJECTED: Contract price $0.480 outside sweet spot [$0.76, $0.89] |
| Spread: Hawks (-3.5) | Sports | NO | `97.5%` | `33.0%` | `+64.5 п.п.` | `1.00%` | REJECTED: Contract price $0.330 outside sweet spot [$0.76, $0.89] |
| Spread: Cavaliers (-4.5) | Sports | NO | `97.5%` | `52.0%` | `+45.5 п.п.` | `1.00%` | REJECTED: Contract price $0.520 outside sweet spot [$0.76, $0.89] |
| Spread: Hawks (-4.5) | Sports | NO | `97.5%` | `37.0%` | `+60.5 п.п.` | `1.00%` | REJECTED: Contract price $0.370 outside sweet spot [$0.76, $0.89] |
| Dota 2: GamerLegion vs CyberHero - Game 1 Winner | Sports | NO | `1.5%` | `100.0%` | `-98.5 п.п.` | `100.00%` | REJECTED: Edge -98.5 pp < 2 pp threshold (P_est=1.5% vs AskVWAP=100.0%) |
| Spread: Rockets (-4.5) | Sports | NO | `97.5%` | `48.0%` | `+49.5 п.п.` | `1.00%` | REJECTED: Contract price $0.480 outside sweet spot [$0.76, $0.89] |
| Dota 2: GamerLegion vs CyberHero (BO3) - EPL Maste | Sports | YES | `97.5%` | `93.0%` | `+4.5 п.п.` | `1.00%` | REJECTED: Contract price $0.930 outside sweet spot [$0.76, $0.89] |
| Spread: Hawks (-3.5) | Sports | NO | `97.5%` | `33.0%` | `+64.5 п.п.` | `1.00%` | REJECTED: Contract price $0.330 outside sweet spot [$0.76, $0.89] |
| Spread: Cavaliers (-4.5) | Sports | NO | `97.5%` | `52.0%` | `+45.5 п.п.` | `1.00%` | REJECTED: Contract price $0.520 outside sweet spot [$0.76, $0.89] |
| Spread: Hawks (-4.5) | Sports | NO | `97.5%` | `37.0%` | `+60.5 п.п.` | `1.00%` | REJECTED: Contract price $0.370 outside sweet spot [$0.76, $0.89] |
| Spread: Rockets (-4.5) | Sports | NO | `97.5%` | `48.0%` | `+49.5 п.п.` | `1.00%` | REJECTED: Contract price $0.480 outside sweet spot [$0.76, $0.89] |
