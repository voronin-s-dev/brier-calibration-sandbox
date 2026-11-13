# 📊 Отчёт симулятора Polymarket (Устав Grok Bot — Демо-счёт)
**Обновлено:** `2026-11-13 08:19:41 UTC`

## 💰 Состояние виртуального портфеля
| Показатель | Значение | Правило устава |
| :--- | :--- | :--- |
| **Стартовый капитал** | `$50.00 USDC` | Не добавлять деньги |
| **Текущий баланс (Equity)** | **`$35.87 USDC`** (`-14.13$` / `-28.26%`) | Cash + Mark-to-Market по CLOB Bid |
| **Свободный кэш / В сделках** | `$29.24` / `$6.64 USDC` | До 8 открытых позиций, макс 8% банка |
| **Цель окупаемости подписки** | `$-14.13 / $60.00` (`0.0%`) | Цель: +$60.00 в месяц |
| **Просадка от пика (Текущая / Макс)** | `8.70%` / `24.45%` (Пик: `$39.29`) | Стоп-кран при просадке 40% |
| **Закрытых сделок / Win Rate** | `168` / `70.2%` | Brier Score: `0.1960` |

## 📂 Открытые позиции (6 / 8)
| # | Рынок | Кат. | Исход | Вход (Ask VWAP) | Текущий Bid | Оценка бота | Размер ($) | Нереализ. PnL | Источник |
| :- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| #155 | Will Elon Musk post 200-219 tweets from November 6 to N | Geopolitics | **NO** | `0.917` | `0.701` | `93.5%` | `$1.07` | `$-0.25` | https://x.com/elonmusk |
| #169 | Jazz vs. Rockets | Sports | **NO** | `0.920` | `0.910` | `95.0%` | `$1.12` | `$-0.01` | https://www.nba.com/ |
| #170 | Bitcoin Up or Down on November 13? | Crypto | **NO** | `0.910` | `0.968` | `98.5%` | `$1.07` | `$+0.07` | https://www.binance.com/en/tra |
| #171 | Will the price of Bitcoin be above $66,000 on November  | Crypto | **YES** | `0.912` | `0.925` | `96.9%` | `$1.08` | `$+0.02` | https://www.binance.com/en/tra |
| #174 | Will the price of Ethereum be above $1,900 on November  | Crypto | **YES** | `0.743` | `0.747` | `80.5%` | `$1.40` | `$+0.01` | Kraken ETHUSDT 1m/1h Spot Klin |
| #175 | Fourth Jensen Huang affair reported by November 13? | Other | **NO** | `0.910` | `0.900` | `94.0%` | `$1.08` | `$-0.01` | reporting from the qualifying  |

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
| Fourth Jensen Huang affair reported by November 13 | Other | NO | `94.0%` | `91.0%` | `+3.0 п.п.` | `1.00%` | EXECUTED BUY #175 ($1.08 @ 0.9100) |
| Will the price of Bitcoin be above $68,000 on Nove | Crypto | YES | `77.4%` | `72.7%` | `+4.7 п.п.` | `0.20%` | REJECTED: Duplicate underlying event (crypto:bitcoin:november 13) |
| Will the price of Bitcoin be above $68,000 on Nove | Crypto | YES | `77.3%` | `71.9%` | `+5.5 п.п.` | `0.10%` | REJECTED: Duplicate underlying event (crypto:bitcoin:november 13) |
| Will the highest temperature in Houston be between | Weather | NO | `91.5%` | `69.0%` | `+22.5 п.п.` | `7.00%` | REJECTED: Narrow weather bracket NO bet prohibited (airport METAR microclimate tail risk) |
| Will the price of Bitcoin be above $68,000 on Nove | Crypto | YES | `82.7%` | `77.6%` | `+5.1 п.п.` | `0.60%` | REJECTED: Duplicate underlying event (crypto:bitcoin:november 13) |
| Will the price of Bitcoin be above $70,000 on Nove | Crypto | NO | `71.2%` | `66.9%` | `+4.3 п.п.` | `0.10%` | REJECTED: Duplicate underlying event (crypto:bitcoin:november 14) |
| Will the price of Bitcoin be above $70,000 on Nove | Crypto | NO | `82.9%` | `72.7%` | `+10.2 п.п.` | `0.10%` | REJECTED: Duplicate underlying event (crypto:bitcoin:november 13) |
| Will the price of Ethereum be above $2,000 on Nove | Crypto | NO | `95.0%` | `90.0%` | `+5.0 п.п.` | `2.00%` | REJECTED: Duplicate underlying event (crypto:ethereum:november 13) |
| Will the price of Bitcoin be above $70,000 on Nove | Crypto | NO | `83.9%` | `75.5%` | `+8.4 п.п.` | `0.10%` | REJECTED: Duplicate underlying event (crypto:bitcoin:november 13) |
| Will the price of Bitcoin be above $68,000 on Nove | Crypto | YES | `72.3%` | `78.8%` | `-6.5 п.п.` | `1.10%` | REJECTED: Edge -6.5 pp < 2 pp threshold (P_est=72.3% vs AskVWAP=78.8%) |
| Will the highest temperature in Houston be between | Weather | NO | `90.6%` | `71.0%` | `+19.6 п.п.` | `4.00%` | REJECTED: Narrow weather bracket NO bet prohibited (airport METAR microclimate tail risk) |
| Will the price of Bitcoin be above $70,000 on Nove | Crypto | NO | `83.5%` | `79.3%` | `+4.2 п.п.` | `1.10%` | REJECTED: Duplicate underlying event (crypto:bitcoin:november 13) |
| Will the price of Ethereum be above $1,900 on Nove | Crypto | YES | `76.8%` | `74.3%` | `+2.5 п.п.` | `0.90%` | EXECUTED BUY #174 ($1.40 @ 0.7430) |
| Will the price of Bitcoin be above $66,000 on Nove | Crypto | YES | `94.7%` | `90.6%` | `+4.1 п.п.` | `0.10%` | REJECTED: Duplicate underlying event (crypto:bitcoin:november 13) |
| Will the price of Bitcoin be above $70,000 on Nove | Crypto | NO | `92.8%` | `85.7%` | `+7.1 п.п.` | `0.70%` | REJECTED: Duplicate underlying event (crypto:bitcoin:november 13) |
| Will Bitcoin reach $69,000 on November 13? | Crypto | YES | `99.5%` | `79.0%` | `+20.5 п.п.` | `2.00%` | REJECTED: Duplicate underlying event (crypto:bitcoin:november 13) |
| Will Bitcoin dip to $65,000 on November 13? | Crypto | NO | `94.0%` | `88.0%` | `+6.0 п.п.` | `1.00%` | REJECTED: Duplicate underlying event (crypto:bitcoin:november 13) |
| Will the price of Bitcoin be above $70,000 on Nove | Crypto | NO | `92.7%` | `88.5%` | `+4.2 п.п.` | `0.90%` | REJECTED: Duplicate underlying event (crypto:bitcoin:november 13) |
