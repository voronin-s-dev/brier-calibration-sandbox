# 📊 Отчёт симулятора Polymarket (Устав Grok Bot — Демо-счёт)
**Обновлено:** `2026-11-11 08:40:05 UTC`

## 💰 Состояние виртуального портфеля
| Показатель | Значение | Правило устава |
| :--- | :--- | :--- |
| **Стартовый капитал** | `$50.00 USDC` | Не добавлять деньги |
| **Текущий баланс (Equity)** | **`$38.53 USDC`** (`-11.47$` / `-22.95%`) | Cash + Mark-to-Market по CLOB Bid |
| **Свободный кэш / В сделках** | `$26.10` / `$12.42 USDC` | До 8 открытых позиций, макс 8% банка |
| **Цель окупаемости подписки** | `$-11.47 / $60.00` (`0.0%`) | Цель: +$60.00 в месяц |
| **Просадка от пика (Текущая / Макс)** | `1.95%` / `24.45%` (Пик: `$39.29`) | Стоп-кран при просадке 40% |
| **Закрытых сделок / Win Rate** | `134` / `73.9%` | Brier Score: `0.1960` |

## 📂 Открытые позиции (6 / 8)
| # | Рынок | Кат. | Исход | Вход (Ask VWAP) | Текущий Bid | Оценка бота | Размер ($) | Нереализ. PnL | Источник |
| :- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| #132 | Will the price of Ethereum be above $2,100 on November  | Crypto | **NO** | `0.815` | `0.890` | `87.1%` | `$1.58` | `$+0.15` | Kraken ETHUSDT 1m/1h Spot Klin |
| #133 | Will the price of Bitcoin be above $72,000 on November  | Crypto | **YES** | `0.913` | `0.943` | `97.9%` | `$1.49` | `$+0.05` | https://www.binance.com/en/tra |
| #135 | Will Elon Musk post 300-319 tweets from November 6 to N | Geopolitics | **NO** | `0.850` | `0.930` | `85.3%` | `$2.99` | `$+0.28` | https://x.com/elonmusk |
| #139 | Spurs vs. Bulls | Sports | **YES** | `0.910` | `0.900` | `94.0%` | `$1.55` | `$-0.02` | https://www.nba.com/ |
| #140 | Counter-Strike: Spirit vs FUT Esports (BO3) - BLAST Riv | Sports | **YES** | `0.920` | `0.740` | `97.0%` | `$1.55` | `$-0.30` | https://hltv.org |
| #141 | Will Elon Musk post 280-299 tweets from November 6 to N | Geopolitics | **NO** | `0.850` | `0.860` | `90.2%` | `$3.07` | `$+0.04` | https://x.com/elonmusk |

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
| #5 | Total Kills Over/Under 27.5 in Game 2? | Other | **NO** | `0.500` | `0.490` | `56.4%` | `$1.42` | `$-0.03` | https://gol.gg/esports/home |
| #20 | Total Kills Over/Under 27.5 in Game 4? | Other | **NO** | `0.500` | `0.490` | `55.8%` | `$1.58` | `$-0.03` | https://gol.gg/esports/home |
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
| Will Elon Musk post 280-299 tweets from November 6 | Geopolitics | NO | `90.2%` | `85.0%` | `+5.2 п.п.` | `1.00%` | EXECUTED BUY #141 ($3.07 @ 0.8500) |
| Counter-Strike: Spirit vs FUT Esports - Map 1 Winn | Sports | YES | `95.0%` | `87.0%` | `+8.0 п.п.` | `1.00%` | REJECTED: Duplicate underlying event (sports:counter-strike: spirit vs fut espor:nodate) |
| Counter-Strike: Spirit vs FUT Esports - Map 1 Winn | Sports | YES | `96.0%` | `91.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Duplicate underlying event (sports:counter-strike: spirit vs fut espor:nodate) |
| Counter-Strike: Spirit vs FUT Esports - Map 1 Winn | Sports | YES | `96.0%` | `89.0%` | `+7.0 п.п.` | `1.00%` | REJECTED: Duplicate underlying event (sports:counter-strike: spirit vs fut espor:nodate) |
| Counter-Strike: Spirit vs FUT Esports (BO3) - BLAS | Sports | YES | `97.0%` | `92.0%` | `+5.0 п.п.` | `1.00%` | EXECUTED BUY #140 ($1.55 @ 0.9200) |
| Spurs vs. Bulls | Sports | YES | `94.0%` | `91.0%` | `+3.0 п.п.` | `1.00%` | EXECUTED BUY #139 ($1.55 @ 0.9100) |
| Will Predict.fun launch a token by November 15, 20 | Other | NO | `91.5%` | `86.3%` | `+5.2 п.п.` | `3.20%` | REJECTED: CLOB round-trip slippage 3.20% > 2.0% limit |
| Will Predict.fun launch a token by November 15, 20 | Other | NO | `91.7%` | `86.3%` | `+5.4 п.п.` | `3.20%` | REJECTED: CLOB round-trip slippage 3.20% > 2.0% limit |
| Will Predict.fun launch a token by November 15, 20 | Other | NO | `91.7%` | `86.3%` | `+5.4 п.п.` | `3.20%` | REJECTED: CLOB round-trip slippage 3.20% > 2.0% limit |
| Will Predict.fun launch a token by November 15, 20 | Other | NO | `91.7%` | `86.3%` | `+5.4 п.п.` | `3.20%` | REJECTED: CLOB round-trip slippage 3.20% > 2.0% limit |
| Counter-Strike: Legacy vs FURIA (BO3) - BLAST Riva | Sports | NO | `98.4%` | `91.2%` | `+7.1 п.п.` | `0.20%` | EXECUTED BUY #138 ($1.54 @ 0.9120) |
| Will Kai Cenat finish his GTA marathon by November | Other | YES | `85.2%` | `80.0%` | `+5.2 п.п.` | `2.00%` | REJECTED: Duplicate underlying event (other:will kai cenat finish his gta marathon b) |
| Counter-Strike: Legacy vs FURIA - Map 1 Winner | Sports | NO | `98.5%` | `94.0%` | `+4.5 п.п.` | `1.00%` | REJECTED: Contract price $0.940 outside sweet spot [$0.76, $0.92] |
| Will the price of Bitcoin be above $76,000 on Nove | Crypto | NO | `98.5%` | `94.4%` | `+4.1 п.п.` | `0.10%` | REJECTED: Contract price $0.944 outside sweet spot [$0.76, $0.92] |
| Will Kai Cenat finish his GTA marathon by November | Other | YES | `85.1%` | `94.0%` | `-8.9 п.п.` | `5.00%` | REJECTED: Edge -8.9 pp < 2 pp threshold (P_est=85.1% vs AskVWAP=94.0%) |
| Will Kai Cenat finish his GTA marathon by November | Other | YES | `84.4%` | `94.0%` | `-9.6 п.п.` | `5.00%` | REJECTED: Edge -9.6 pp < 2 pp threshold (P_est=84.4% vs AskVWAP=94.0%) |
| Will Bitcoin dip to $72,000 on November 10? | Crypto | NO | `98.0%` | `94.0%` | `+4.0 п.п.` | `1.00%` | REJECTED: Contract price $0.940 outside sweet spot [$0.76, $0.92] |
| Dota 2: CyberHero vs Power Rangers (BO3) - 1win Es | Sports | YES | `95.0%` | `91.0%` | `+4.0 п.п.` | `1.00%` | EXECUTED BUY #137 ($1.51 @ 0.9100) |
