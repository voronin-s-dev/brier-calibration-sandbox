# 📊 Отчёт симулятора Polymarket (Устав Grok Bot — Демо-счёт)
**Обновлено:** `2026-11-18 03:19:31 UTC`

## 💰 Состояние виртуального портфеля
| Показатель | Значение | Правило устава |
| :--- | :--- | :--- |
| **Стартовый капитал** | `$50.00 USDC` | Не добавлять деньги |
| **Текущий баланс (Equity)** | **`$29.20 USDC`** (`-20.80$` / `-41.60%`) | Cash + Mark-to-Market по CLOB Bid |
| **Свободный кэш / В сделках** | `$23.80` / `$5.40 USDC` | До 8 открытых позиций, макс 8% банка |
| **Цель окупаемости подписки** | `$-20.80 / $60.00` (`0.0%`) | Цель: +$60.00 в месяц |
| **Просадка от пика (Текущая / Макс)** | `25.68%` / `26.82%` (Пик: `$39.29`) | Стоп-кран при просадке 40% |
| **Закрытых сделок / Win Rate** | `207` / `63.3%` | Brier Score: `0.1960` |

## 📂 Открытые позиции (5 / 8)
| # | Рынок | Кат. | Исход | Вход (Ask VWAP) | Текущий Bid | Оценка бота | Размер ($) | Нереализ. PnL | Источник |
| :- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| #208 | Will the price of Ethereum be above $1,700 on November  | Crypto | **YES** | `0.882` | `0.961` | `98.8%` | `$1.00` | `$+0.09` | Kraken ETHUSDT 1m/1h Spot Klin |
| #210 | Will the price of Bitcoin be above $66,000 on November  | Crypto | **NO** | `0.893` | `0.890` | `89.5%` | `$1.00` | `$-0.00` | Kraken BTCUSDT 1m/1h Spot Klin |
| #211 | Will Elon Musk post 65-89 tweets from November 16 to No | Geopolitics | **NO** | `0.920` | `0.979` | `95.0%` | `$1.00` | `$+0.06` | https://x.com/elonmusk |
| #212 | Fourth Jensen Huang affair reported by November 20? | Other | **NO** | `0.910` | `0.910` | `98.0%` | `$1.00` | `$-0.00` | reporting from the qualifying  |
| #213 | Will the price of Ethereum be above $1,900 on November  | Crypto | **NO** | `0.810` | `0.880` | `88.7%` | `$1.15` | `$+0.10` | Kraken ETHUSDT 1m/1h Spot Klin |

## 🧪 Теневая песочница (Shadow Sandbox)
| Показатель | Значение |
| :--- | :--- |
| **Виртуальный баланс (Equity)** | **`$59.06 USDC`** |
| **Свободный кэш / В сделках** | `$59.06` / `$0.00 USDC` |
| **Открытых позиций** | `0 / 5` |
| **Текущая просадка** | `2.60%` |

### Доходность по замороженным категориям (Песочница)
| Категория | Сделок | PnL | Win Rate |
| :--- | :--- | :--- | :--- |
| **Crypto** | `98` | `+$8.42` | `62%` |
| **Geopolitics** | `8` | `+$1.02` | `62%` |
| **Macro** | `5` | `+$0.91` | `60%` |
| **Other** | `19` | `-$1.30` | `42%` |

## 🔍 Последние проверенные кандидаты и фильтр стакана CLOB
| Рынок | Кат. | Сторона | Оценка бота | Цена Ask | Перекос (Edge) | Проскальзывание CLOB | Решение |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Will South Africa win? | Other | YES | `77.0%` | `73.0%` | `+4.0 п.п.` | `3.00%` | REJECTED: Net EV edge +1.0 pp < 1.5 pp (Gross +4.0 pp - Slippage 3.00%) |
| Will Bitcoin reach $66,000 on November 17? | Crypto | NO | `94.1%` | `88.9%` | `+5.2 п.п.` | `0.40%` | REJECTED: Contract price $0.889 outside sweet spot [$0.70, $0.87] |
| Will South Africa win? | Other | YES | `77.0%` | `73.0%` | `+4.0 п.п.` | `3.00%` | REJECTED: CLOB round-trip slippage 3.00% > 2.0% limit |
| Will the price of Ethereum be above $1,900 on Nove | Crypto | NO | `95.3%` | `90.6%` | `+4.8 п.п.` | `0.70%` | REJECTED: Duplicate underlying event (crypto:ethereum:november 18) |
| Will the price of Ethereum be above $1,900 on Nove | Crypto | NO | `84.2%` | `81.0%` | `+3.2 п.п.` | `1.00%` | EXECUTED BUY #213 ($1.15 @ 0.8100) |
| Will Ethereum dip to $1,750 on November 17? | Crypto | YES | `99.5%` | `10.5%` | `+89.0 п.п.` | `2.50%` | REJECTED: Contract price $0.105 outside sweet spot [$0.60, $0.92] |
| Will Ethereum dip to $1,750 on November 17? | Crypto | YES | `99.5%` | `13.0%` | `+86.5 п.п.` | `2.00%` | REJECTED: Contract price $0.130 outside sweet spot [$0.60, $0.92] |
| Will Ethereum dip to $1,750 on November 17? | Crypto | YES | `99.5%` | `13.0%` | `+86.5 п.п.` | `2.00%` | REJECTED: Contract price $0.130 outside sweet spot [$0.60, $0.92] |
| Will Ethereum dip to $1,750 on November 17? | Crypto | YES | `99.5%` | `14.0%` | `+85.5 п.п.` | `2.00%` | REJECTED: Contract price $0.140 outside sweet spot [$0.60, $0.92] |
| Will Ethereum dip to $1,750 on November 17? | Crypto | YES | `99.5%` | `12.7%` | `+86.8 п.п.` | `3.13%` | REJECTED: Contract price $0.127 outside sweet spot [$0.60, $0.92] |
| Will Ethereum dip to $1,750 on November 17? | Crypto | YES | `99.5%` | `10.0%` | `+89.5 п.п.` | `2.00%` | REJECTED: Contract price $0.100 outside sweet spot [$0.60, $0.92] |
| Will Bitcoin reach $66,000 on November 17? | Crypto | NO | `94.0%` | `88.4%` | `+5.5 п.п.` | `2.80%` | REJECTED: CLOB round-trip slippage 2.80% > 2.0% limit |
| Will Ethereum dip to $1,750 on November 17? | Crypto | YES | `99.5%` | `16.0%` | `+83.5 п.п.` | `1.00%` | REJECTED: Contract price $0.160 outside sweet spot [$0.60, $0.92] |
| Will Ethereum dip to $1,750 on November 17? | Crypto | YES | `99.5%` | `17.0%` | `+82.5 п.п.` | `1.00%` | REJECTED: Contract price $0.170 outside sweet spot [$0.60, $0.92] |
| Will Ethereum dip to $1,750 on November 17? | Crypto | YES | `99.5%` | `11.0%` | `+88.5 п.п.` | `1.00%` | REJECTED: Contract price $0.110 outside sweet spot [$0.60, $0.92] |
| Will Ethereum dip to $1,750 on November 17? | Crypto | YES | `99.5%` | `19.0%` | `+80.5 п.п.` | `1.00%` | REJECTED: Contract price $0.190 outside sweet spot [$0.60, $0.92] |
| Will Ethereum dip to $1,750 on November 17? | Crypto | YES | `99.5%` | `17.0%` | `+82.5 п.п.` | `2.00%` | REJECTED: Contract price $0.170 outside sweet spot [$0.60, $0.92] |
| Will Ethereum dip to $1,750 on November 17? | Crypto | YES | `99.5%` | `18.0%` | `+81.5 п.п.` | `1.00%` | REJECTED: Contract price $0.180 outside sweet spot [$0.60, $0.92] |
