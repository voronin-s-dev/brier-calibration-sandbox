# 📊 Отчёт симулятора Polymarket (Устав Grok Bot — Демо-счёт)
**Обновлено:** `2026-11-12 07:30:57 UTC`

## 💰 Состояние виртуального портфеля
| Показатель | Значение | Правило устава |
| :--- | :--- | :--- |
| **Стартовый капитал** | `$50.00 USDC` | Не добавлять деньги |
| **Текущий баланс (Equity)** | **`$36.32 USDC`** (`-13.68$` / `-27.36%`) | Cash + Mark-to-Market по CLOB Bid |
| **Свободный кэш / В сделках** | `$19.65` / `$16.67 USDC` | До 8 открытых позиций, макс 8% банка |
| **Цель окупаемости подписки** | `$-13.68 / $60.00` (`0.0%`) | Цель: +$60.00 в месяц |
| **Просадка от пика (Текущая / Макс)** | `7.56%` / `24.45%` (Пик: `$39.29`) | Стоп-кран при просадке 40% |
| **Закрытых сделок / Win Rate** | `147` / `72.8%` | Brier Score: `0.1960` |

## 📂 Открытые позиции (8 / 8)
| # | Рынок | Кат. | Исход | Вход (Ask VWAP) | Текущий Bid | Оценка бота | Размер ($) | Нереализ. PnL | Источник |
| :- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| #141 | Will Elon Musk post 280-299 tweets from November 6 to N | Geopolitics | **NO** | `0.850` | `0.954` | `98.5%` | `$3.07` | `$+0.38` | https://x.com/elonmusk |
| #144 | Will Predict.fun launch a token by November 15, 2026? | Other | **NO** | `0.848` | `0.944` | `90.7%` | `$2.90` | `$+0.33` | information from predict.fun ( |
| #147 | Will the price of Bitcoin be above $76,000 on November  | Crypto | **NO** | `0.910` | `0.973` | `98.5%` | `$1.11` | `$+0.08` | https://www.binance.com/en/tra |
| #152 | Will the price of Ethereum be above $2,000 on November  | Crypto | **YES** | `0.911` | `0.898` | `87.5%` | `$1.10` | `$-0.02` | https://www.binance.com/en/tra |
| #153 | Will Ethereum dip to $2,000 November 9-15? | Crypto | **YES** | `0.660` | `0.570` | `68.3%` | `$1.95` | `$-0.27` | Kraken ETHUSDT 1m/1h Spot Klin |
| #154 | Will Elon Musk post 220-239 tweets from November 6 to N | Geopolitics | **NO** | `0.670` | `0.621` | `72.5%` | `$2.33` | `$-0.17` | https://x.com/elonmusk |
| #155 | Will Elon Musk post 200-219 tweets from November 6 to N | Geopolitics | **NO** | `0.917` | `0.903` | `94.1%` | `$1.07` | `$-0.02` | https://x.com/elonmusk |
| #156 | Will Vitality Win the BLAST Rivals Hong Kong 2026? | Other | **NO** | `0.740` | `0.720` | `79.7%` | `$2.91` | `$-0.08` | https://www.hltv.org/events/82 |

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
| #5 | Total Kills Over/Under 27.5 in Game 2? | Other | **NO** | `0.500` | `0.490` | `56.2%` | `$1.42` | `$-0.03` | https://gol.gg/esports/home |
| #20 | Total Kills Over/Under 27.5 in Game 4? | Other | **NO** | `0.500` | `0.490` | `55.8%` | `$1.58` | `$-0.03` | https://gol.gg/esports/home |
| #31 | Total Kills Over/Under 27.5 in Game 3? | Other | **YES** | `0.510` | `0.490` | `54.6%` | `$1.15` | `$-0.05` | https://gol.gg/esports/home |

### Доходность по замороженным категориям (Песочница)
| Категория | Сделок | PnL | Win Rate |
| :--- | :--- | :--- | :--- |
| **Crypto** | `15` | `+$4.18` | `60%` |
| **Geopolitics** | `4` | `+$0.57` | `75%` |
| **Other** | `13` | `+$0.81` | `54%` |

## 🔍 Последние проверенные кандидаты и фильтр стакана CLOB
| Рынок | Кат. | Сторона | Оценка бота | Цена Ask | Перекос (Edge) | Проскальзывание CLOB | Решение |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Will Vitality Win the BLAST Rivals Hong Kong 2026? | Other | NO | `79.7%` | `74.0%` | `+5.7 п.п.` | `2.00%` | EXECUTED BUY #156 ($2.91 @ 0.7400) |
| Will Bitcoin reach $74,000 on November 12? | Crypto | YES | `78.2%` | `72.0%` | `+6.2 п.п.` | `2.00%` | REJECTED: Duplicate underlying event (crypto:bitcoin:november 12) |
| Will Elon Musk post 200-219 tweets from November 6 | Geopolitics | NO | `95.1%` | `91.7%` | `+3.4 п.п.` | `0.70%` | EXECUTED BUY #155 ($1.07 @ 0.9170) |
| Will Elon Musk post 220-239 tweets from November 6 | Geopolitics | NO | `72.5%` | `67.0%` | `+5.5 п.п.` | `0.20%` | EXECUTED BUY #154 ($2.33 @ 0.6700) |
| Will the highest temperature in Dallas be between  | Weather | NO | `86.6%` | `64.0%` | `+22.6 п.п.` | `3.00%` | REJECTED: Narrow weather bracket NO bet prohibited (airport METAR microclimate tail risk) |
| Will Ethereum dip to $2,000 November 9-15? | Crypto | YES | `70.5%` | `66.0%` | `+4.5 п.п.` | `2.00%` | EXECUTED BUY #153 ($1.95 @ 0.6600) |
| Will the price of Ethereum be above $2,000 on Nove | Crypto | YES | `93.9%` | `91.1%` | `+2.8 п.п.` | `0.60%` | EXECUTED BUY #152 ($1.10 @ 0.9110) |
| Will Bitcoin dip to $73,000 on November 11? | Crypto | NO | `93.6%` | `88.0%` | `+5.6 п.п.` | `1.90%` | REJECTED: Duplicate underlying event (crypto:bitcoin:november 11) |
| Spurs vs. Bulls | Sports | YES | `94.0%` | `91.0%` | `+3.0 п.п.` | `1.00%` | EXECUTED BUY #151 ($1.11 @ 0.9100) |
| Spurs vs. Bulls | Sports | YES | `94.0%` | `91.0%` | `+3.0 п.п.` | `1.00%` | EXECUTED BUY #150 ($1.11 @ 0.9100) |
| Will Ethereum dip to $2,000 November 9-15? | Crypto | YES | `70.2%` | `62.0%` | `+8.2 п.п.` | `2.00%` | EXECUTED BUY #149 ($2.98 @ 0.6200) |
| Will Bitcoin reach $75,000 on November 11? | Crypto | NO | `95.0%` | `91.0%` | `+4.0 п.п.` | `2.00%` | EXECUTED BUY #148 ($1.11 @ 0.9100) |
| Will the price of Bitcoin be above $76,000 on Nove | Crypto | NO | `94.0%` | `91.0%` | `+3.0 п.п.` | `1.00%` | EXECUTED BUY #147 ($1.11 @ 0.9100) |
| Will Bitcoin reach $75,000 on November 11? | Crypto | YES | `70.0%` | `37.0%` | `+33.1 п.п.` | `3.00%` | REJECTED: Contract price $0.370 outside sweet spot [$0.60, $0.92] |
| Will Bitcoin reach $76,000 on November 11? | Crypto | NO | `93.6%` | `91.9%` | `+1.7 п.п.` | `0.70%` | EXECUTED BUY #146 ($1.08 @ 0.9190) |
| Will Juventus FC win on 2026-11-11? | Sports | NO | `97.5%` | `93.4%` | `+4.0 п.п.` | `0.10%` | REJECTED: Contract price $0.934 outside sweet spot [$0.76, $0.92] |
| Will Juventus FC win on 2026-11-11? | Sports | NO | `97.5%` | `93.4%` | `+4.0 п.п.` | `0.10%` | REJECTED: Contract price $0.934 outside sweet spot [$0.76, $0.92] |
| Will the price of Bitcoin be above $74,000 on Nove | Crypto | NO | `81.1%` | `31.8%` | `+49.3 п.п.` | `3.00%` | REJECTED: Contract price $0.318 outside sweet spot [$0.76, $0.92] |
