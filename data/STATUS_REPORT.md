# 📊 Отчёт симулятора Polymarket (Устав Grok Bot — Демо-счёт)
**Обновлено:** `2026-11-13 12:31:05 UTC`

## 💰 Состояние виртуального портфеля
| Показатель | Значение | Правило устава |
| :--- | :--- | :--- |
| **Стартовый капитал** | `$50.00 USDC` | Не добавлять деньги |
| **Текущий баланс (Equity)** | **`$36.28 USDC`** (`-13.72$` / `-27.45%`) | Cash + Mark-to-Market по CLOB Bid |
| **Свободный кэш / В сделках** | `$27.83` / `$8.44 USDC` | До 8 открытых позиций, макс 8% банка |
| **Цель окупаемости подписки** | `$-13.72 / $60.00` (`0.0%`) | Цель: +$60.00 в месяц |
| **Просадка от пика (Текущая / Макс)** | `7.67%` / `24.45%` (Пик: `$39.29`) | Стоп-кран при просадке 40% |
| **Закрытых сделок / Win Rate** | `169` / `70.4%` | Brier Score: `0.1960` |

## 📂 Открытые позиции (7 / 8)
| # | Рынок | Кат. | Исход | Вход (Ask VWAP) | Текущий Bid | Оценка бота | Размер ($) | Нереализ. PnL | Источник |
| :- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| #155 | Will Elon Musk post 200-219 tweets from November 6 to N | Geopolitics | **NO** | `0.917` | `0.650` | `93.5%` | `$1.07` | `$-0.31` | https://x.com/elonmusk |
| #169 | Jazz vs. Rockets | Sports | **NO** | `0.920` | `0.910` | `95.0%` | `$1.12` | `$-0.01` | https://www.nba.com/ |
| #170 | Bitcoin Up or Down on November 13? | Crypto | **NO** | `0.910` | `0.953` | `98.5%` | `$1.07` | `$+0.05` | https://www.binance.com/en/tra |
| #171 | Will the price of Bitcoin be above $66,000 on November  | Crypto | **YES** | `0.912` | `0.949` | `98.5%` | `$1.08` | `$+0.04` | https://www.binance.com/en/tra |
| #175 | Fourth Jensen Huang affair reported by November 13? | Other | **NO** | `0.910` | `0.880` | `94.0%` | `$1.08` | `$-0.04` | reporting from the qualifying  |
| #176 | S&P 500 (SPX) Up or Down on November 13? | Macro | **YES** | `0.650` | `0.690` | `75.0%` | `$2.07` | `$+0.13` | https://www.wsj.com/market-dat |
| #177 | Will the price of Ethereum be above $2,000 on November  | Crypto | **NO** | `0.880` | `0.880` | `92.0%` | `$1.09` | `$-0.00` | Kraken ETHUSDT 1m/1h Spot Klin |

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
| Will the price of Bitcoin be above $68,000 on Nove | Crypto | YES | `92.8%` | `88.6%` | `+4.2 п.п.` | `0.10%` | REJECTED: Duplicate underlying event (crypto:bitcoin:november 13) |
| Will the price of Bitcoin be between $68,000 and $ | Crypto | YES | `72.1%` | `64.3%` | `+7.8 п.п.` | `4.70%` | REJECTED: CLOB round-trip slippage 4.70% > 2.0% limit |
| Will the price of Bitcoin be above $70,000 on Nove | Crypto | NO | `79.2%` | `73.0%` | `+6.2 п.п.` | `2.40%` | REJECTED: CLOB round-trip slippage 2.40% > 2.0% limit |
| Will the price of Ethereum be above $2,000 on Nove | Crypto | NO | `90.1%` | `88.0%` | `+2.1 п.п.` | `1.00%` | EXECUTED BUY #177 ($1.09 @ 0.8800) |
| Will the price of Bitcoin be above $70,000 on Nove | Crypto | NO | `75.5%` | `68.0%` | `+7.5 п.п.` | `0.30%` | REJECTED: Duplicate underlying event (crypto:bitcoin:november 13) |
| Will the price of Bitcoin be above $70,000 on Nove | Crypto | NO | `75.4%` | `68.0%` | `+7.4 п.п.` | `1.70%` | REJECTED: Duplicate underlying event (crypto:bitcoin:november 13) |
| Will the price of Bitcoin be above $70,000 on Nove | Crypto | NO | `76.1%` | `69.3%` | `+6.8 п.п.` | `1.50%` | REJECTED: Duplicate underlying event (crypto:bitcoin:november 13) |
| Will the price of Bitcoin be between $68,000 and $ | Crypto | YES | `70.0%` | `61.6%` | `+8.4 п.п.` | `4.20%` | REJECTED: CLOB round-trip slippage 4.20% > 2.0% limit |
| Will the price of Bitcoin be above $70,000 on Nove | Crypto | NO | `78.3%` | `68.9%` | `+9.4 п.п.` | `1.90%` | REJECTED: Duplicate underlying event (crypto:bitcoin:november 13) |
| Will the price of Bitcoin be between $68,000 and $ | Crypto | YES | `70.1%` | `63.8%` | `+6.3 п.п.` | `4.30%` | REJECTED: CLOB round-trip slippage 4.30% > 2.0% limit |
| Will the price of Bitcoin be above $70,000 on Nove | Crypto | NO | `79.8%` | `73.8%` | `+6.0 п.п.` | `1.80%` | REJECTED: Duplicate underlying event (crypto:bitcoin:november 13) |
| Will the price of Bitcoin be above $70,000 on Nove | Crypto | NO | `79.0%` | `74.2%` | `+4.8 п.п.` | `1.20%` | REJECTED: Duplicate underlying event (crypto:bitcoin:november 13) |
| Will the price of Bitcoin be above $70,000 on Nove | Crypto | NO | `77.2%` | `72.1%` | `+5.1 п.п.` | `0.10%` | REJECTED: Duplicate underlying event (crypto:bitcoin:november 13) |
| S&P 500 (SPX) Up or Down on November 13? | Macro | YES | `70.0%` | `65.0%` | `+5.0 п.п.` | `1.00%` | EXECUTED BUY #176 ($2.07 @ 0.6500) |
| Will the price of Bitcoin be above $70,000 on Nove | Crypto | NO | `79.5%` | `69.7%` | `+9.8 п.п.` | `0.10%` | REJECTED: Duplicate underlying event (crypto:bitcoin:november 13) |
| Will the price of Bitcoin be above $70,000 on Nove | Crypto | NO | `80.1%` | `74.1%` | `+6.0 п.п.` | `0.10%` | REJECTED: Duplicate underlying event (crypto:bitcoin:november 13) |
| Will the price of Bitcoin be above $70,000 on Nove | Crypto | NO | `81.2%` | `76.9%` | `+4.3 п.п.` | `0.30%` | REJECTED: Duplicate underlying event (crypto:bitcoin:november 13) |
| Will the price of Bitcoin be above $70,000 on Nove | Crypto | NO | `83.8%` | `79.2%` | `+4.6 п.п.` | `1.20%` | REJECTED: Duplicate underlying event (crypto:bitcoin:november 13) |
