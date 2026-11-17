# 📊 Отчёт симулятора Polymarket (Устав Grok Bot — Демо-счёт)
**Обновлено:** `2026-11-17 22:20:32 UTC`

## 💰 Состояние виртуального портфеля
| Показатель | Значение | Правило устава |
| :--- | :--- | :--- |
| **Стартовый капитал** | `$50.00 USDC` | Не добавлять деньги |
| **Текущий баланс (Equity)** | **`$29.18 USDC`** (`-20.82$` / `-41.64%`) | Cash + Mark-to-Market по CLOB Bid |
| **Свободный кэш / В сделках** | `$22.91` / `$6.27 USDC` | До 8 открытых позиций, макс 8% банка |
| **Цель окупаемости подписки** | `$-20.82 / $60.00` (`0.0%`) | Цель: +$60.00 в месяц |
| **Просадка от пика (Текущая / Макс)** | `25.73%` / `26.35%` (Пик: `$39.29`) | Стоп-кран при просадке 40% |
| **Закрытых сделок / Win Rate** | `205` / `63.4%` | Brier Score: `0.1960` |

## 📂 Открытые позиции (6 / 8)
| # | Рынок | Кат. | Исход | Вход (Ask VWAP) | Текущий Bid | Оценка бота | Размер ($) | Нереализ. PnL | Источник |
| :- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| #207 | Will Ethereum reach $1,850 on November 17? | Crypto | **NO** | `0.890` | `0.870` | `86.4%` | `$1.00` | `$-0.02` | Kraken ETHUSDT 1m/1h Spot Klin |
| #208 | Will the price of Ethereum be above $1,700 on November  | Crypto | **YES** | `0.882` | `0.950` | `96.6%` | `$1.00` | `$+0.08` | Kraken ETHUSDT 1m/1h Spot Klin |
| #209 | Will Bitcoin dip to $62,000 on November 17? | Crypto | **NO** | `0.876` | `0.964` | `98.5%` | `$1.16` | `$+0.12` | Kraken BTCUSDT 1m/1h Spot Klin |
| #210 | Will the price of Bitcoin be above $66,000 on November  | Crypto | **NO** | `0.893` | `0.869` | `87.2%` | `$1.00` | `$-0.03` | Kraken BTCUSDT 1m/1h Spot Klin |
| #211 | Will Elon Musk post 65-89 tweets from November 16 to No | Geopolitics | **NO** | `0.920` | `0.900` | `94.0%` | `$1.00` | `$-0.02` | https://x.com/elonmusk |
| #212 | Fourth Jensen Huang affair reported by November 20? | Other | **NO** | `0.910` | `0.900` | `96.0%` | `$1.00` | `$-0.01` | reporting from the qualifying  |

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
| Fourth Jensen Huang affair reported by November 20 | Other | NO | `96.0%` | `91.0%` | `+5.0 п.п.` | `1.00%` | EXECUTED BUY #212 ($1.00 @ 0.9100) |
| Will Ethereum dip to $1,750 on November 17? | Crypto | YES | `99.5%` | `19.0%` | `+80.5 п.п.` | `1.00%` | REJECTED: Contract price $0.190 outside sweet spot [$0.60, $0.92] |
| Will Ethereum dip to $1,750 on November 17? | Crypto | YES | `99.5%` | `22.0%` | `+77.5 п.п.` | `1.00%` | REJECTED: Contract price $0.220 outside sweet spot [$0.60, $0.92] |
| Will Ethereum dip to $1,750 on November 17? | Crypto | YES | `99.5%` | `26.0%` | `+73.5 п.п.` | `1.00%` | REJECTED: Contract price $0.260 outside sweet spot [$0.60, $0.92] |
| Will Ethereum dip to $1,750 on November 17? | Crypto | YES | `99.5%` | `25.0%` | `+74.5 п.п.` | `1.00%` | REJECTED: Contract price $0.250 outside sweet spot [$0.60, $0.92] |
| Will South Africa win? | Other | YES | `82.5%` | `73.0%` | `+9.5 п.п.` | `3.00%` | REJECTED: CLOB round-trip slippage 3.00% > 2.0% limit |
