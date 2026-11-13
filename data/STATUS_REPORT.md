# 📊 Отчёт симулятора Polymarket (Устав Grok Bot — Демо-счёт)
**Обновлено:** `2026-11-13 04:19:30 UTC`

## 💰 Состояние виртуального портфеля
| Показатель | Значение | Правило устава |
| :--- | :--- | :--- |
| **Стартовый капитал** | `$50.00 USDC` | Не добавлять деньги |
| **Текущий баланс (Equity)** | **`$35.51 USDC`** (`-14.49$` / `-28.98%`) | Cash + Mark-to-Market по CLOB Bid |
| **Свободный кэш / В сделках** | `$26.40` / `$9.11 USDC` | До 8 открытых позиций, макс 8% банка |
| **Цель окупаемости подписки** | `$-14.49 / $60.00` (`0.0%`) | Цель: +$60.00 в месяц |
| **Просадка от пика (Текущая / Макс)** | `9.63%` / `24.45%` (Пик: `$39.29`) | Стоп-кран при просадке 40% |
| **Закрытых сделок / Win Rate** | `165` / `70.3%` | Brier Score: `0.1960` |

## 📂 Открытые позиции (7 / 8)
| # | Рынок | Кат. | Исход | Вход (Ask VWAP) | Текущий Bid | Оценка бота | Размер ($) | Нереализ. PnL | Источник |
| :- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| #154 | Will Elon Musk post 220-239 tweets from November 6 to N | Geopolitics | **NO** | `0.670` | `0.751` | `68.0%` | `$2.33` | `$+0.28` | https://x.com/elonmusk |
| #155 | Will Elon Musk post 200-219 tweets from November 6 to N | Geopolitics | **NO** | `0.917` | `0.314` | `93.5%` | `$1.07` | `$-0.70` | https://x.com/elonmusk |
| #169 | Jazz vs. Rockets | Sports | **NO** | `0.920` | `0.910` | `95.0%` | `$1.12` | `$-0.01` | https://www.nba.com/ |
| #170 | Bitcoin Up or Down on November 13? | Crypto | **NO** | `0.910` | `0.930` | `97.5%` | `$1.07` | `$+0.02` | https://www.binance.com/en/tra |
| #171 | Will the price of Bitcoin be above $66,000 on November  | Crypto | **YES** | `0.912` | `0.891` | `93.5%` | `$1.08` | `$-0.02` | https://www.binance.com/en/tra |
| #172 | Will Bitcoin dip to $68,000 November 9-15? | Crypto | **YES** | `0.760` | `0.690` | `80.8%` | `$1.90` | `$-0.18` | Kraken BTCUSDT 1m/1h Spot Klin |
| #173 | Will Ethereum dip to $1,900 November 9-15? | Crypto | **YES** | `0.760` | `0.690` | `76.3%` | `$1.27` | `$-0.12` | Kraken ETHUSDT 1m/1h Spot Klin |

## 🧪 Теневая песочница (Shadow Sandbox)
| Показатель | Значение |
| :--- | :--- |
| **Виртуальный баланс (Equity)** | **`$55.52 USDC`** |
| **Свободный кэш / В сделках** | `$51.42` / `$4.10 USDC` |
| **Открытых позиций** | `3 / 5` |
| **Текущая просадка** | `3.00%` |

### Открытые позиции в песочнице (3 / 5)
| # | Рынок | Кат. | Исход | Вход (Ask VWAP) | Текущий Bid | Оценка бота | Размер ($) | Нереализ. PnL | Источник |
| :- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| #5 | Total Kills Over/Under 27.5 in Game 2? | Other | **NO** | `0.500` | `0.510` | `56.5%` | `$1.42` | `$+0.03` | https://gol.gg/esports/home |
| #20 | Total Kills Over/Under 27.5 in Game 4? | Other | **NO** | `0.500` | `0.490` | `55.9%` | `$1.58` | `$-0.03` | https://gol.gg/esports/home |
| #31 | Total Kills Over/Under 27.5 in Game 3? | Other | **YES** | `0.510` | `0.490` | `54.3%` | `$1.15` | `$-0.05` | https://gol.gg/esports/home |

### Доходность по замороженным категориям (Песочница)
| Категория | Сделок | PnL | Win Rate |
| :--- | :--- | :--- | :--- |
| **Crypto** | `15` | `+$4.18` | `60%` |
| **Geopolitics** | `4` | `+$0.57` | `75%` |
| **Other** | `13` | `+$0.81` | `54%` |

## 🔍 Последние проверенные кандидаты и фильтр стакана CLOB
| Рынок | Кат. | Сторона | Оценка бота | Цена Ask | Перекос (Edge) | Проскальзывание CLOB | Решение |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Will the price of Ethereum be above $2,000 on Nove | Crypto | NO | `91.7%` | `87.0%` | `+4.7 п.п.` | `2.00%` | REJECTED: Category cap reached (4/4 in Crypto) |
| Will the price of Bitcoin be above $70,000 on Nove | Crypto | NO | `80.3%` | `73.6%` | `+6.7 п.п.` | `0.10%` | REJECTED: Duplicate underlying event (crypto:bitcoin:november 13) |
| Will the price of Ethereum be above $2,000 on Nove | Crypto | NO | `91.5%` | `87.0%` | `+4.5 п.п.` | `2.00%` | REJECTED: Category cap reached (4/4 in Crypto) |
| Will the highest temperature in Houston be between | Weather | NO | `85.2%` | `59.0%` | `+26.2 п.п.` | `4.00%` | REJECTED: Contract price $0.590 outside sweet spot [$0.60, $0.92] |
| Will the price of Bitcoin be above $70,000 on Nove | Crypto | NO | `80.3%` | `74.9%` | `+5.4 п.п.` | `0.10%` | REJECTED: Duplicate underlying event (crypto:bitcoin:november 13) |
| Will the highest temperature in Houston be between | Weather | NO | `85.0%` | `62.0%` | `+23.1 п.п.` | `2.00%` | REJECTED: Narrow weather bracket NO bet prohibited (airport METAR microclimate tail risk) |
| Will Ethereum dip to $1,900 November 9-15? | Crypto | YES | `78.1%` | `76.0%` | `+2.1 п.п.` | `2.00%` | EXECUTED BUY #173 ($1.27 @ 0.7600) |
| Will Bitcoin dip to $68,000 November 9-15? | Crypto | YES | `79.2%` | `76.0%` | `+3.2 п.п.` | `2.00%` | EXECUTED BUY #172 ($1.90 @ 0.7600) |
| Will the price of Ethereum be above $1,900 on Nove | Crypto | YES | `88.0%` | `80.5%` | `+7.5 п.п.` | `2.90%` | REJECTED: CLOB round-trip slippage 2.90% > 2.0% limit |
| Will the price of Bitcoin be above $66,000 on Nove | Crypto | YES | `94.8%` | `91.2%` | `+3.5 п.п.` | `0.80%` | EXECUTED BUY #171 ($1.08 @ 0.9120) |
| Will the highest temperature in Houston be between | Weather | NO | `85.0%` | `62.0%` | `+23.1 п.п.` | `3.00%` | REJECTED: Narrow weather bracket NO bet prohibited (airport METAR microclimate tail risk) |
| Will the price of Bitcoin be above $68,000 on Nove | Crypto | YES | `79.8%` | `74.6%` | `+5.2 п.п.` | `1.20%` | REJECTED: Duplicate underlying event (crypto:bitcoin:november 13) |
| Will the price of Ethereum be above $1,900 on Nove | Crypto | YES | `87.8%` | `83.3%` | `+4.5 п.п.` | `3.40%` | REJECTED: CLOB round-trip slippage 3.40% > 2.0% limit |
| Will the highest temperature in Houston be between | Weather | NO | `85.0%` | `62.0%` | `+23.1 п.п.` | `3.00%` | REJECTED: Narrow weather bracket NO bet prohibited (airport METAR microclimate tail risk) |
| Will the price of Bitcoin be above $68,000 on Nove | Crypto | YES | `80.0%` | `75.0%` | `+5.1 п.п.` | `0.10%` | REJECTED: Duplicate underlying event (crypto:bitcoin:november 13) |
| Bitcoin Up or Down on November 13? | Crypto | NO | `95.0%` | `91.0%` | `+4.0 п.п.` | `1.00%` | EXECUTED BUY #170 ($1.07 @ 0.9100) |
| Will the price of Bitcoin be above $70,000 on Nove | Crypto | NO | `70.4%` | `65.9%` | `+4.5 п.п.` | `2.10%` | REJECTED: CLOB round-trip slippage 2.10% > 2.0% limit |
| Will the price of Bitcoin be above $68,000 on Nove | Crypto | YES | `91.4%` | `84.2%` | `+7.2 п.п.` | `1.20%` | REJECTED: Duplicate underlying event (crypto:bitcoin:november 13) |
