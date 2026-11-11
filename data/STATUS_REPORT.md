# 📊 Отчёт симулятора Polymarket (Устав Grok Bot — Демо-счёт)
**Обновлено:** `2026-11-11 22:09:21 UTC`

## 💰 Состояние виртуального портфеля
| Показатель | Значение | Правило устава |
| :--- | :--- | :--- |
| **Стартовый капитал** | `$50.00 USDC` | Не добавлять деньги |
| **Текущий баланс (Equity)** | **`$37.01 USDC`** (`-12.99$` / `-25.97%`) | Cash + Mark-to-Market по CLOB Bid |
| **Свободный кэш / В сделках** | `$24.51` / `$12.50 USDC` | До 8 открытых позиций, макс 8% банка |
| **Цель окупаемости подписки** | `$-12.99 / $60.00` (`0.0%`) | Цель: +$60.00 в месяц |
| **Просадка от пика (Текущая / Макс)** | `5.80%` / `24.45%` (Пик: `$39.29`) | Стоп-кран при просадке 40% |
| **Закрытых сделок / Win Rate** | `140` / `74.3%` | Brier Score: `0.1960` |

## 📂 Открытые позиции (5 / 8)
| # | Рынок | Кат. | Исход | Вход (Ask VWAP) | Текущий Bid | Оценка бота | Размер ($) | Нереализ. PnL | Источник |
| :- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| #135 | Will Elon Musk post 300-319 tweets from November 6 to N | Geopolitics | **NO** | `0.850` | `0.971` | `98.5%` | `$2.99` | `$+0.43` | https://x.com/elonmusk |
| #139 | Spurs vs. Bulls | Sports | **YES** | `0.910` | `0.900` | `94.0%` | `$1.55` | `$-0.02` | https://www.nba.com/ |
| #141 | Will Elon Musk post 280-299 tweets from November 6 to N | Geopolitics | **NO** | `0.850` | `0.940` | `98.0%` | `$3.07` | `$+0.33` | https://x.com/elonmusk |
| #144 | Will Predict.fun launch a token by November 15, 2026? | Other | **NO** | `0.848` | `0.884` | `90.7%` | `$2.90` | `$+0.12` | information from predict.fun ( |
| #146 | Will Bitcoin reach $76,000 on November 11? | Crypto | **NO** | `0.919` | `0.966` | `98.5%` | `$1.08` | `$+0.06` | https://www.binance.com/en/tra |

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
| #5 | Total Kills Over/Under 27.5 in Game 2? | Other | **NO** | `0.500` | `0.490` | `54.6%` | `$1.42` | `$-0.03` | https://gol.gg/esports/home |
| #20 | Total Kills Over/Under 27.5 in Game 4? | Other | **NO** | `0.500` | `0.490` | `55.4%` | `$1.58` | `$-0.03` | https://gol.gg/esports/home |
| #31 | Total Kills Over/Under 27.5 in Game 3? | Other | **YES** | `0.510` | `0.490` | `54.4%` | `$1.15` | `$-0.05` | https://gol.gg/esports/home |

### Доходность по замороженным категориям (Песочница)
| Категория | Сделок | PnL | Win Rate |
| :--- | :--- | :--- | :--- |
| **Crypto** | `15` | `+$4.18` | `60%` |
| **Geopolitics** | `4` | `+$0.57` | `75%` |
| **Other** | `13` | `+$0.81` | `54%` |

## 🔍 Последние проверенные кандидаты и фильтр стакана CLOB
| Рынок | Кат. | Сторона | Оценка бота | Цена Ask | Перекос (Edge) | Проскальзывание CLOB | Решение |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Will Bitcoin reach $75,000 on November 11? | Crypto | YES | `70.0%` | `37.0%` | `+33.1 п.п.` | `3.00%` | REJECTED: Contract price $0.370 outside sweet spot [$0.60, $0.92] |
| Will Bitcoin reach $76,000 on November 11? | Crypto | NO | `93.6%` | `91.9%` | `+1.7 п.п.` | `0.70%` | EXECUTED BUY #146 ($1.08 @ 0.9190) |
| Will Juventus FC win on 2026-11-11? | Sports | NO | `97.5%` | `93.4%` | `+4.0 п.п.` | `0.10%` | REJECTED: Contract price $0.934 outside sweet spot [$0.76, $0.92] |
| Will Juventus FC win on 2026-11-11? | Sports | NO | `97.5%` | `93.4%` | `+4.0 п.п.` | `0.10%` | REJECTED: Contract price $0.934 outside sweet spot [$0.76, $0.92] |
| Will the price of Bitcoin be above $74,000 on Nove | Crypto | NO | `81.1%` | `31.8%` | `+49.3 п.п.` | `3.00%` | REJECTED: Contract price $0.318 outside sweet spot [$0.76, $0.92] |
| Will the price of Bitcoin be between $72,000 and $ | Crypto | YES | `84.1%` | `79.1%` | `+5.0 п.п.` | `2.80%` | REJECTED: CLOB round-trip slippage 2.80% > 2.0% limit |
| Bitcoin Up or Down on November 11? | Crypto | YES | `94.0%` | `88.0%` | `+6.0 п.п.` | `1.00%` | EXECUTED BUY #145 ($2.90 @ 0.8800) |
| Will Predict.fun launch a token by November 15, 20 | Other | NO | `90.9%` | `84.8%` | `+6.1 п.п.` | `1.30%` | EXECUTED BUY #144 ($2.90 @ 0.8480) |
| Dota 2: HULIGANI vs PuckChamp (BO3) - DreamLeague  | Sports | YES | `94.3%` | `90.9%` | `+3.4 п.п.` | `1.90%` | EXECUTED BUY #143 ($1.45 @ 0.9090) |
| Counter-Strike: MOUZ vs G2 (BO3) - BLAST Rivals Gr | Sports | YES | `95.7%` | `88.4%` | `+7.2 п.п.` | `0.10%` | EXECUTED BUY #142 ($3.13 @ 0.8840) |
| Counter-Strike: MOUZ vs G2 (BO3) - BLAST Rivals Gr | Sports | YES | `94.0%` | `98.0%` | `-4.0 п.п.` | `1.00%` | REJECTED: Edge -4.0 pp < 2 pp threshold (P_est=94.0% vs AskVWAP=98.0%) |
| Spread: Spain (-4.5) | Sports | NO | `97.5%` | `93.0%` | `+4.5 п.п.` | `3.00%` | REJECTED: Contract price $0.930 outside sweet spot [$0.76, $0.92] |
| LoL: Ground Zero Gaming vs Frank Esports - Game 1  | Sports | NO | `98.5%` | `93.0%` | `+5.5 п.п.` | `1.00%` | REJECTED: Contract price $0.930 outside sweet spot [$0.76, $0.92] |
| Will Elon Musk post 280-299 tweets from November 6 | Geopolitics | NO | `90.2%` | `85.0%` | `+5.2 п.п.` | `1.00%` | EXECUTED BUY #141 ($3.07 @ 0.8500) |
| Counter-Strike: Spirit vs FUT Esports - Map 1 Winn | Sports | YES | `95.0%` | `87.0%` | `+8.0 п.п.` | `1.00%` | REJECTED: Duplicate underlying event (sports:counter-strike: spirit vs fut espor:nodate) |
| Counter-Strike: Spirit vs FUT Esports - Map 1 Winn | Sports | YES | `96.0%` | `91.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Duplicate underlying event (sports:counter-strike: spirit vs fut espor:nodate) |
| Counter-Strike: Spirit vs FUT Esports - Map 1 Winn | Sports | YES | `96.0%` | `89.0%` | `+7.0 п.п.` | `1.00%` | REJECTED: Duplicate underlying event (sports:counter-strike: spirit vs fut espor:nodate) |
| Counter-Strike: Spirit vs FUT Esports (BO3) - BLAS | Sports | YES | `97.0%` | `92.0%` | `+5.0 п.п.` | `1.00%` | EXECUTED BUY #140 ($1.55 @ 0.9200) |
