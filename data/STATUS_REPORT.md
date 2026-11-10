# 📊 Отчёт симулятора Polymarket (Устав Grok Bot — Демо-счёт)
**Обновлено:** `2026-11-10 15:01:25 UTC`

## 💰 Состояние виртуального портфеля
| Показатель | Значение | Правило устава |
| :--- | :--- | :--- |
| **Стартовый капитал** | `$50.00 USDC` | Не добавлять деньги |
| **Текущий баланс (Equity)** | **`$37.43 USDC`** (`-12.57$` / `-25.14%`) | Cash + Mark-to-Market по CLOB Bid |
| **Свободный кэш / В сделках** | `$34.36` / `$3.07 USDC` | До 8 открытых позиций, макс 8% банка |
| **Цель окупаемости подписки** | `$-12.57 / $60.00` (`0.0%`) | Цель: +$60.00 в месяц |
| **Просадка от пика (Текущая / Макс)** | `4.74%` / `24.45%` (Пик: `$39.29`) | Стоп-кран при просадке 40% |
| **Закрытых сделок / Win Rate** | `127` / `74.0%` | Brier Score: `0.1960` |

## 📂 Открытые позиции (1 / 8)
| # | Рынок | Кат. | Исход | Вход (Ask VWAP) | Текущий Bid | Оценка бота | Размер ($) | Нереализ. PnL | Источник |
| :- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| #125 | Bucks vs. Knicks | Sports | **NO** | `0.910` | `0.890` | `94.0%` | `$3.14` | `$-0.07` | https://www.nba.com/ |

## 🧪 Теневая песочница (Shadow Sandbox)
| Показатель | Значение |
| :--- | :--- |
| **Виртуальный баланс (Equity)** | **`$51.19 USDC`** |
| **Свободный кэш / В сделках** | `$45.21` / `$5.99 USDC` |
| **Открытых позиций** | `4 / 5` |
| **Текущая просадка** | `0.14%` |

### Открытые позиции в песочнице (4 / 5)
| # | Рынок | Кат. | Исход | Вход (Ask VWAP) | Текущий Bid | Оценка бота | Размер ($) | Нереализ. PnL | Источник |
| :- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| #1 | Will Elon Musk post 40-64 tweets from November 9 to Nov | Geopolitics | **NO** | `0.800` | `0.590` | `84.6%` | `$2.47` | `$-0.65` | https://x.com/elonmusk |
| #5 | Total Kills Over/Under 27.5 in Game 2? | Other | **NO** | `0.500` | `0.490` | `56.0%` | `$1.42` | `$-0.03` | https://gol.gg/esports/home |
| #14 | Total Kills Over/Under 27.5 in Game 3? | Other | **NO** | `0.500` | `0.490` | `55.4%` | `$1.25` | `$-0.02` | https://gol.gg/esports/home |
| #20 | Total Kills Over/Under 27.5 in Game 4? | Other | **NO** | `0.500` | `0.490` | `55.8%` | `$1.58` | `$-0.03` | https://gol.gg/esports/home |

### Доходность по замороженным категориям (Песочница)
| Категория | Сделок | PnL | Win Rate |
| :--- | :--- | :--- | :--- |
| **Crypto** | `7` | `+$0.19` | `57%` |
| **Geopolitics** | `2` | `+$0.66` | `100%` |
| **Other** | `9` | `+$1.08` | `67%` |

## 🔍 Последние проверенные кандидаты и фильтр стакана CLOB
| Рынок | Кат. | Сторона | Оценка бота | Цена Ask | Перекос (Edge) | Проскальзывание CLOB | Решение |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Dota 2: Xipto Esports vs PlayTime - Game 1 Winner | Sports | YES | `94.0%` | `100.0%` | `-6.0 п.п.` | `100.00%` | REJECTED: Edge -6.0 pp < 2 pp threshold (P_est=94.0% vs AskVWAP=100.0%) |
| Dota 2: HULIGANI vs Amaru Gaming - Game 1 Winner | Sports | YES | `97.5%` | `67.0%` | `+30.5 п.п.` | `1.00%` | REJECTED: Contract price $0.670 outside sweet spot [$0.76, $0.92] |
| Counter-Strike: FORZE Reload vs MOUZ NXT (BO3) - E | Sports | YES | `94.0%` | `88.0%` | `+6.0 п.п.` | `1.00%` | EXECUTED BUY #129 ($2.97 @ 0.8800) |
| Dota 2: PlayTime vs Nemiga Gaming - Game 1 Winner | Sports | YES | `94.0%` | `80.0%` | `+14.0 п.п.` | `2.00%` | EXECUTED BUY #128 ($2.91 @ 0.8000) |
| LoL: Saigon Warriors vs Gromp Esports - Game 2 Win | Sports | YES | `98.0%` | `93.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Contract price $0.930 outside sweet spot [$0.76, $0.92] |
| LoL: Saigon Warriors vs Gromp Esports (BO5) - LCP  | Sports | YES | `94.5%` | `92.0%` | `+2.5 п.п.` | `2.00%` | EXECUTED BUY #127 ($2.89 @ 0.9200) |
| LoL: FENNEL vs Nothin'Here - Game 2 Winner | Sports | YES | `98.5%` | `65.0%` | `+33.5 п.п.` | `1.00%` | REJECTED: Contract price $0.650 outside sweet spot [$0.76, $0.92] |
| LoL: FENNEL vs Nothin'Here (BO5) - LCP Promotion P | Sports | YES | `98.0%` | `90.0%` | `+8.0 п.п.` | `1.00%` | EXECUTED BUY #126 ($3.14 @ 0.9000) |
| LoL: FENNEL vs Nothin'Here (BO5) - LCP Promotion P | Sports | YES | `98.0%` | `94.0%` | `+4.0 п.п.` | `1.00%` | REJECTED: Contract price $0.940 outside sweet spot [$0.76, $0.92] |
| Bucks vs. Knicks | Sports | NO | `94.0%` | `91.0%` | `+3.0 п.п.` | `1.00%` | EXECUTED BUY #125 ($3.14 @ 0.9100) |
| Spread: Rockets (-4.5) | Sports | NO | `97.5%` | `37.0%` | `+60.5 п.п.` | `2.00%` | REJECTED: Contract price $0.370 outside sweet spot [$0.76, $0.92] |
| Counter-Strike: Sökerorg vs Prestige - Map 2 Winne | Sports | NO | `1.5%` | `100.0%` | `-98.5 п.п.` | `100.00%` | REJECTED: Edge -98.5 pp < 2 pp threshold (P_est=1.5% vs AskVWAP=100.0%) |
| Dota 2: PlayTime vs potn9ki - Game 1 Winner | Sports | YES | `1.5%` | `100.0%` | `-98.5 п.п.` | `100.00%` | REJECTED: Edge -98.5 pp < 2 pp threshold (P_est=1.5% vs AskVWAP=100.0%) |
| Dota 2: Power Rangers vs Nemiga Gaming - Game 1 Wi | Sports | YES | `1.5%` | `100.0%` | `-98.5 п.п.` | `100.00%` | REJECTED: Edge -98.5 pp < 2 pp threshold (P_est=1.5% vs AskVWAP=100.0%) |
| Dota 2: Froglings vs Team Synapse - Game 1 Winner | Sports | NO | `1.5%` | `100.0%` | `-98.5 п.п.` | `100.00%` | REJECTED: Edge -98.5 pp < 2 pp threshold (P_est=1.5% vs AskVWAP=100.0%) |
| Dota 2: Xipto Esports vs HULIGANI - Game 1 Winner | Sports | NO | `1.5%` | `100.0%` | `-98.5 п.п.` | `100.00%` | REJECTED: Edge -98.5 pp < 2 pp threshold (P_est=1.5% vs AskVWAP=100.0%) |
| Spread: Bills (-3.5) | Sports | NO | `97.5%` | `54.0%` | `+43.5 п.п.` | `1.00%` | REJECTED: Contract price $0.540 outside sweet spot [$0.76, $0.92] |
| Spread: Rockets (-4.5) | Sports | NO | `97.5%` | `37.0%` | `+60.5 п.п.` | `2.00%` | REJECTED: Contract price $0.370 outside sweet spot [$0.76, $0.92] |
