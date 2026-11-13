# 📊 Отчёт симулятора Polymarket (Устав Grok Bot — Демо-счёт)
**Обновлено:** `2026-11-13 06:01:15 UTC`

## 💰 Состояние виртуального портфеля
| Показатель | Значение | Правило устава |
| :--- | :--- | :--- |
| **Стартовый капитал** | `$50.00 USDC` | Не добавлять деньги |
| **Текущий баланс (Equity)** | **`$36.12 USDC`** (`-13.88$` / `-27.75%`) | Cash + Mark-to-Market по CLOB Bid |
| **Свободный кэш / В сделках** | `$30.56` / `$5.56 USDC` | До 8 открытых позиций, макс 8% банка |
| **Цель окупаемости подписки** | `$-13.88 / $60.00` (`0.0%`) | Цель: +$60.00 в месяц |
| **Просадка от пика (Текущая / Макс)** | `8.06%` / `24.45%` (Пик: `$39.29`) | Стоп-кран при просадке 40% |
| **Закрытых сделок / Win Rate** | `167` / `70.7%` | Brier Score: `0.1960` |

## 📂 Открытые позиции (5 / 8)
| # | Рынок | Кат. | Исход | Вход (Ask VWAP) | Текущий Bid | Оценка бота | Размер ($) | Нереализ. PnL | Источник |
| :- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| #154 | Will Elon Musk post 220-239 tweets from November 6 to N | Geopolitics | **NO** | `0.670` | `0.411` | `68.0%` | `$2.33` | `$-0.90` | https://x.com/elonmusk |
| #155 | Will Elon Musk post 200-219 tweets from November 6 to N | Geopolitics | **NO** | `0.917` | `0.768` | `93.5%` | `$1.07` | `$-0.17` | https://x.com/elonmusk |
| #169 | Jazz vs. Rockets | Sports | **NO** | `0.920` | `0.910` | `95.0%` | `$1.12` | `$-0.01` | https://www.nba.com/ |
| #170 | Bitcoin Up or Down on November 13? | Crypto | **NO** | `0.910` | `0.963` | `98.5%` | `$1.07` | `$+0.06` | https://www.binance.com/en/tra |
| #171 | Will the price of Bitcoin be above $66,000 on November  | Crypto | **YES** | `0.912` | `0.840` | `82.3%` | `$1.08` | `$-0.09` | https://www.binance.com/en/tra |

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
| Will the highest temperature in Houston be between | Weather | NO | `89.3%` | `62.0%` | `+27.3 п.п.` | `3.00%` | REJECTED: Narrow weather bracket NO bet prohibited (airport METAR microclimate tail risk) |
| Will the price of Bitcoin be above $70,000 on Nove | Crypto | NO | `80.8%` | `85.4%` | `-4.6 п.п.` | `3.90%` | REJECTED: Edge -4.6 pp < 2 pp threshold (P_est=80.8% vs AskVWAP=85.4%) |
| Will the highest temperature in Houston be between | Weather | NO | `89.2%` | `62.0%` | `+27.2 п.п.` | `4.00%` | REJECTED: Narrow weather bracket NO bet prohibited (airport METAR microclimate tail risk) |
| Will the price of Bitcoin be above $70,000 on Nove | Crypto | NO | `85.7%` | `80.6%` | `+5.1 п.п.` | `0.10%` | REJECTED: Duplicate underlying event (crypto:bitcoin:november 13) |
| Will the price of Ethereum be above $1,900 on Nove | Crypto | YES | `72.9%` | `67.7%` | `+5.2 п.п.` | `1.50%` | REJECTED: Category cap reached (4/4 in Crypto) |
| Will the price of Bitcoin be above $68,000 on Nove | Crypto | YES | `73.7%` | `67.2%` | `+6.5 п.п.` | `0.10%` | REJECTED: Duplicate underlying event (crypto:bitcoin:november 13) |
| Will the price of Ethereum be above $1,900 on Nove | Crypto | YES | `73.2%` | `68.1%` | `+5.1 п.п.` | `1.90%` | REJECTED: Category cap reached (4/4 in Crypto) |
| Will the price of Bitcoin be above $68,000 on Nove | Crypto | YES | `74.2%` | `70.0%` | `+4.2 п.п.` | `0.10%` | REJECTED: Duplicate underlying event (crypto:bitcoin:november 13) |
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
