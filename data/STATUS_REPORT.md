# 📊 Отчёт симулятора Polymarket (Устав Grok Bot — Демо-счёт)
**Обновлено:** `2026-11-10 13:10:28 UTC`

## 💰 Состояние виртуального портфеля
| Показатель | Значение | Правило устава |
| :--- | :--- | :--- |
| **Стартовый капитал** | `$50.00 USDC` | Не добавлять деньги |
| **Текущий баланс (Equity)** | **`$37.03 USDC`** (`-12.97$` / `-25.94%`) | Cash + Mark-to-Market по CLOB Bid |
| **Свободный кэш / В сделках** | `$30.99` / `$6.04 USDC` | До 8 открытых позиций, макс 8% банка |
| **Цель окупаемости подписки** | `$-12.97 / $60.00` (`0.0%`) | Цель: +$60.00 в месяц |
| **Просадка от пика (Текущая / Макс)** | `5.76%` / `24.45%` (Пик: `$39.29`) | Стоп-кран при просадке 40% |
| **Закрытых сделок / Win Rate** | `126` / `73.8%` | Brier Score: `0.1960` |

## 📂 Открытые позиции (2 / 8)
| # | Рынок | Кат. | Исход | Вход (Ask VWAP) | Текущий Bid | Оценка бота | Размер ($) | Нереализ. PnL | Источник |
| :- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| #125 | Bucks vs. Knicks | Sports | **NO** | `0.910` | `0.900` | `94.0%` | `$3.14` | `$-0.03` | https://www.nba.com/ |
| #129 | Counter-Strike: FORZE Reload vs MOUZ NXT (BO3) - Europe | Sports | **YES** | `0.880` | `0.870` | `94.0%` | `$2.97` | `$-0.03` | https://hltv.org |

## 🧪 Теневая песочница (Shadow Sandbox)
| Показатель | Значение |
| :--- | :--- |
| **Виртуальный баланс (Equity)** | **`$50.10 USDC`** |
| **Свободный кэш / В сделках** | `$41.78` / `$8.32 USDC` |
| **Открытых позиций** | `5 / 5` |
| **Текущая просадка** | `1.06%` |

### Открытые позиции в песочнице (5 / 5)
| # | Рынок | Кат. | Исход | Вход (Ask VWAP) | Текущий Bid | Оценка бота | Размер ($) | Нереализ. PnL | Источник |
| :- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| #1 | Will Elon Musk post 40-64 tweets from November 9 to Nov | Geopolitics | **NO** | `0.800` | `0.660` | `84.6%` | `$2.47` | `$-0.43` | https://x.com/elonmusk |
| #5 | Total Kills Over/Under 27.5 in Game 2? | Other | **NO** | `0.500` | `0.490` | `56.2%` | `$1.42` | `$-0.03` | https://gol.gg/esports/home |
| #14 | Total Kills Over/Under 27.5 in Game 3? | Other | **NO** | `0.500` | `0.490` | `55.4%` | `$1.25` | `$-0.02` | https://gol.gg/esports/home |
| #17 | Will the price of Bitcoin be above $74,000 on November  | Crypto | **NO** | `0.369` | `0.287` | `37.0%` | `$2.72` | `$-0.60` | https://www.binance.com/en/tra |
| #20 | Total Kills Over/Under 27.5 in Game 4? | Other | **NO** | `0.500` | `0.490` | `55.8%` | `$1.58` | `$-0.03` | https://gol.gg/esports/home |

### Доходность по замороженным категориям (Песочница)
| Категория | Сделок | PnL | Win Rate |
| :--- | :--- | :--- | :--- |
| **Crypto** | `5` | `-$0.57` | `40%` |
| **Geopolitics** | `2` | `+$0.66` | `100%` |
| **Other** | `8` | `+$1.14` | `75%` |

## 🔍 Последние проверенные кандидаты и фильтр стакана CLOB
| Рынок | Кат. | Сторона | Оценка бота | Цена Ask | Перекос (Edge) | Проскальзывание CLOB | Решение |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
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
| Spread: Bills (-3.5) | Sports | NO | `97.5%` | `54.0%` | `+43.5 п.п.` | `1.00%` | REJECTED: Contract price $0.540 outside sweet spot [$0.76, $0.92] |
| Spread: Rockets (-4.5) | Sports | NO | `97.5%` | `37.0%` | `+60.5 п.п.` | `2.00%` | REJECTED: Contract price $0.370 outside sweet spot [$0.76, $0.92] |
