# 📊 Отчёт симулятора Polymarket (Устав Grok Bot — Демо-счёт)
**Обновлено:** `2026-11-10 23:10:27 UTC`

## 💰 Состояние виртуального портфеля
| Показатель | Значение | Правило устава |
| :--- | :--- | :--- |
| **Стартовый капитал** | `$50.00 USDC` | Не добавлять деньги |
| **Текущий баланс (Equity)** | **`$37.72 USDC`** (`-12.28$` / `-24.55%`) | Cash + Mark-to-Market по CLOB Bid |
| **Свободный кэш / В сделках** | `$22.15` / `$15.57 USDC` | До 8 открытых позиций, макс 8% банка |
| **Цель окупаемости подписки** | `$-12.28 / $60.00` (`0.0%`) | Цель: +$60.00 в месяц |
| **Просадка от пика (Текущая / Макс)** | `3.99%` / `24.45%` (Пик: `$39.29`) | Стоп-кран при просадке 40% |
| **Закрытых сделок / Win Rate** | `128` / `73.4%` | Brier Score: `0.1960` |

## 📂 Открытые позиции (7 / 8)
| # | Рынок | Кат. | Исход | Вход (Ask VWAP) | Текущий Bid | Оценка бота | Размер ($) | Нереализ. PnL | Источник |
| :- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| #125 | Bucks vs. Knicks | Sports | **NO** | `0.910` | `0.890` | `94.0%` | `$3.14` | `$-0.07` | https://www.nba.com/ |
| #130 | Will Kai Cenat finish his GTA marathon by November 11,  | Other | **YES** | `0.820` | `0.940` | `89.3%` | `$2.99` | `$+0.44` | https://www.twitch.tv/kaicenat |
| #132 | Will the price of Ethereum be above $2,100 on November  | Crypto | **NO** | `0.815` | `0.864` | `84.7%` | `$1.58` | `$+0.10` | Kraken ETHUSDT 1m/1h Spot Klin |
| #133 | Will the price of Bitcoin be above $72,000 on November  | Crypto | **YES** | `0.913` | `0.879` | `82.7%` | `$1.49` | `$-0.06` | https://www.binance.com/en/tra |
| #134 | Will Ethereum dip to $2,000 on November 10? | Crypto | **NO** | `0.920` | `0.860` | `81.9%` | `$1.49` | `$-0.10` | https://www.binance.com/en/tra |
| #135 | Will Elon Musk post 300-319 tweets from November 6 to N | Geopolitics | **NO** | `0.850` | `0.850` | `82.1%` | `$2.99` | `$-0.00` | https://x.com/elonmusk |
| #136 | Will Bitcoin reach $75,000 on November 10? | Crypto | **NO** | `0.897` | `0.940` | `97.7%` | `$1.51` | `$+0.07` | https://www.binance.com/en/tra |

## 🧪 Теневая песочница (Shadow Sandbox)
| Показатель | Значение |
| :--- | :--- |
| **Виртуальный баланс (Equity)** | **`$55.46 USDC`** |
| **Свободный кэш / В сделках** | `$51.42` / `$4.04 USDC` |
| **Открытых позиций** | `3 / 5` |
| **Текущая просадка** | `3.10%` |

### Открытые позиции в песочнице (3 / 5)
| # | Рынок | Кат. | Исход | Вход (Ask VWAP) | Текущий Bid | Оценка бота | Размер ($) | Нереализ. PnL | Источник |
| :- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| #5 | Total Kills Over/Under 27.5 in Game 2? | Other | **NO** | `0.500` | `0.490` | `54.9%` | `$1.42` | `$-0.03` | https://gol.gg/esports/home |
| #20 | Total Kills Over/Under 27.5 in Game 4? | Other | **NO** | `0.500` | `0.490` | `55.0%` | `$1.58` | `$-0.03` | https://gol.gg/esports/home |
| #31 | Total Kills Over/Under 27.5 in Game 3? | Other | **YES** | `0.510` | `0.490` | `54.0%` | `$1.15` | `$-0.05` | https://gol.gg/esports/home |

### Доходность по замороженным категориям (Песочница)
| Категория | Сделок | PnL | Win Rate |
| :--- | :--- | :--- | :--- |
| **Crypto** | `15` | `+$4.18` | `60%` |
| **Geopolitics** | `4` | `+$0.57` | `75%` |
| **Other** | `13` | `+$0.81` | `54%` |

## 🔍 Последние проверенные кандидаты и фильтр стакана CLOB
| Рынок | Кат. | Сторона | Оценка бота | Цена Ask | Перекос (Edge) | Проскальзывание CLOB | Решение |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Will Bitcoin reach $75,000 on November 10? | Crypto | NO | `94.2%` | `89.7%` | `+4.5 п.п.` | `0.90%` | EXECUTED BUY #136 ($1.51 @ 0.8970) |
| Will Bitcoin reach $75,000 on November 10? | Crypto | NO | `94.5%` | `87.8%` | `+6.7 п.п.` | `1.00%` | REJECTED on final sizing: slippage=2.40% |
| Will Elon Musk post 300-319 tweets from November 6 | Geopolitics | NO | `88.6%` | `85.0%` | `+3.6 п.п.` | `1.00%` | EXECUTED BUY #135 ($2.99 @ 0.8500) |
| Will Kai Cenat finish his GTA marathon by November | Other | YES | `86.6%` | `82.0%` | `+4.6 п.п.` | `2.00%` | REJECTED: Duplicate underlying event (other:will kai cenat finish his gta marathon b) |
| Will Ethereum dip to $2,000 on November 10? | Crypto | NO | `95.0%` | `92.0%` | `+3.0 п.п.` | `2.00%` | EXECUTED BUY #134 ($1.49 @ 0.9200) |
| Will the price of Bitcoin be above $72,000 on Nove | Crypto | YES | `94.0%` | `91.3%` | `+2.8 п.п.` | `0.10%` | EXECUTED BUY #133 ($1.49 @ 0.9130) |
| Counter-Strike: Isurus vs RED Canids Academy (BO3) | Sports | YES | `95.0%` | `99.0%` | `-4.0 п.п.` | `1.00%` | REJECTED: Edge -4.0 pp < 2 pp threshold (P_est=95.0% vs AskVWAP=99.0%) |
| Dota 2: Froglings vs Power Rangers - Game 2 Winner | Sports | NO | `98.5%` | `90.0%` | `+8.5 п.п.` | `5.00%` | REJECTED: CLOB round-trip slippage 5.00% > 2.0% limit |
| Will the price of Ethereum be above $2,100 on Nove | Crypto | NO | `83.5%` | `81.5%` | `+1.9 п.п.` | `0.60%` | EXECUTED BUY #132 ($1.58 @ 0.8150) |
| Will Bitcoin reach $75,000 on November 10? | Crypto | NO | `93.5%` | `89.6%` | `+4.0 п.п.` | `0.10%` | EXECUTED BUY #131 ($1.49 @ 0.8960) |
| Will Bitcoin reach $75,000 on November 10? | Crypto | NO | `95.2%` | `86.9%` | `+8.3 п.п.` | `3.50%` | REJECTED: CLOB round-trip slippage 3.50% > 2.0% limit |
| Will Kai Cenat finish his GTA marathon by November | Other | YES | `86.7%` | `82.0%` | `+4.7 п.п.` | `2.00%` | EXECUTED BUY #130 ($2.99 @ 0.8200) |
| Dota 2: Xipto Esports vs PlayTime - Game 1 Winner | Sports | YES | `94.0%` | `100.0%` | `-6.0 п.п.` | `100.00%` | REJECTED: Edge -6.0 pp < 2 pp threshold (P_est=94.0% vs AskVWAP=100.0%) |
| Dota 2: HULIGANI vs Amaru Gaming - Game 1 Winner | Sports | YES | `97.5%` | `67.0%` | `+30.5 п.п.` | `1.00%` | REJECTED: Contract price $0.670 outside sweet spot [$0.76, $0.92] |
| Counter-Strike: FORZE Reload vs MOUZ NXT (BO3) - E | Sports | YES | `94.0%` | `88.0%` | `+6.0 п.п.` | `1.00%` | EXECUTED BUY #129 ($2.97 @ 0.8800) |
| Dota 2: PlayTime vs Nemiga Gaming - Game 1 Winner | Sports | YES | `94.0%` | `80.0%` | `+14.0 п.п.` | `2.00%` | EXECUTED BUY #128 ($2.91 @ 0.8000) |
| LoL: Saigon Warriors vs Gromp Esports - Game 2 Win | Sports | YES | `98.0%` | `93.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Contract price $0.930 outside sweet spot [$0.76, $0.92] |
| LoL: Saigon Warriors vs Gromp Esports (BO5) - LCP  | Sports | YES | `94.5%` | `92.0%` | `+2.5 п.п.` | `2.00%` | EXECUTED BUY #127 ($2.89 @ 0.9200) |
