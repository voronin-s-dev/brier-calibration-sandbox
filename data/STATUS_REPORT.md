# 📊 Отчёт симулятора Polymarket (Устав Grok Bot — Демо-счёт)
**Обновлено:** `2026-11-10 18:27:35 UTC`

## 💰 Состояние виртуального портфеля
| Показатель | Значение | Правило устава |
| :--- | :--- | :--- |
| **Стартовый капитал** | `$50.00 USDC` | Не добавлять деньги |
| **Текущий баланс (Equity)** | **`$37.36 USDC`** (`-12.64$` / `-25.29%`) | Cash + Mark-to-Market по CLOB Bid |
| **Свободный кэш / В сделках** | `$31.37` / `$5.99 USDC` | До 8 открытых позиций, макс 8% банка |
| **Цель окупаемости подписки** | `$-12.64 / $60.00` (`0.0%`) | Цель: +$60.00 в месяц |
| **Просадка от пика (Текущая / Макс)** | `4.92%` / `24.45%` (Пик: `$39.29`) | Стоп-кран при просадке 40% |
| **Закрытых сделок / Win Rate** | `127` / `74.0%` | Brier Score: `0.1960` |

## 📂 Открытые позиции (2 / 8)
| # | Рынок | Кат. | Исход | Вход (Ask VWAP) | Текущий Bid | Оценка бота | Размер ($) | Нереализ. PnL | Источник |
| :- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| #125 | Bucks vs. Knicks | Sports | **NO** | `0.910` | `0.890` | `94.0%` | `$3.14` | `$-0.07` | https://www.nba.com/ |
| #130 | Will Kai Cenat finish his GTA marathon by November 11,  | Other | **YES** | `0.820` | `0.800` | `86.7%` | `$2.99` | `$-0.07` | https://www.twitch.tv/kaicenat |

## 🧪 Теневая песочница (Shadow Sandbox)
| Показатель | Значение |
| :--- | :--- |
| **Виртуальный баланс (Equity)** | **`$55.99 USDC`** |
| **Свободный кэш / В сделках** | `$48.98` / `$7.00 USDC` |
| **Открытых позиций** | `5 / 5` |
| **Текущая просадка** | `2.18%` |

### Открытые позиции в песочнице (5 / 5)
| # | Рынок | Кат. | Исход | Вход (Ask VWAP) | Текущий Bid | Оценка бота | Размер ($) | Нереализ. PnL | Источник |
| :- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| #5 | Total Kills Over/Under 27.5 in Game 2? | Other | **NO** | `0.500` | `0.490` | `54.7%` | `$1.42` | `$-0.03` | https://gol.gg/esports/home |
| #20 | Total Kills Over/Under 27.5 in Game 4? | Other | **NO** | `0.500` | `0.490` | `55.0%` | `$1.58` | `$-0.03` | https://gol.gg/esports/home |
| #31 | Total Kills Over/Under 27.5 in Game 3? | Other | **YES** | `0.510` | `0.490` | `54.0%` | `$1.15` | `$-0.05` | https://gol.gg/esports/home |
| #34 | Will the price of Ethereum be above $2,000 on November  | Crypto | **NO** | `0.371` | `0.287` | `32.5%` | `$1.50` | `$-0.34` | https://www.binance.com/en/tra |
| #35 | Will Kai Cenat finish his GTA marathon by November 11,  | Other | **YES** | `0.660` | `0.590` | `64.0%` | `$2.01` | `$-0.21` | https://www.twitch.tv/kaicenat |

### Доходность по замороженным категориям (Песочница)
| Категория | Сделок | PnL | Win Rate |
| :--- | :--- | :--- | :--- |
| **Crypto** | `14` | `+$4.83` | `64%` |
| **Geopolitics** | `4` | `+$0.57` | `75%` |
| **Other** | `12` | `+$1.24` | `58%` |

## 🔍 Последние проверенные кандидаты и фильтр стакана CLOB
| Рынок | Кат. | Сторона | Оценка бота | Цена Ask | Перекос (Edge) | Проскальзывание CLOB | Решение |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Will Kai Cenat finish his GTA marathon by November | Other | YES | `86.7%` | `82.0%` | `+4.7 п.п.` | `2.00%` | EXECUTED BUY #130 ($2.99 @ 0.8200) |
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
