# 📊 Отчёт симулятора Polymarket (Устав Grok Bot — Демо-счёт)
**Обновлено:** `2026-11-17 20:49:19 UTC`

## 💰 Состояние виртуального портфеля
| Показатель | Значение | Правило устава |
| :--- | :--- | :--- |
| **Стартовый капитал** | `$50.00 USDC` | Не добавлять деньги |
| **Текущий баланс (Equity)** | **`$29.13 USDC`** (`-20.87$` / `-41.75%`) | Cash + Mark-to-Market по CLOB Bid |
| **Свободный кэш / В сделках** | `$21.92` / `$7.21 USDC` | До 8 открытых позиций, макс 8% банка |
| **Цель окупаемости подписки** | `$-20.87 / $60.00` (`0.0%`) | Цель: +$60.00 в месяц |
| **Просадка от пика (Текущая / Макс)** | `25.87%` / `26.19%` (Пик: `$39.29`) | Стоп-кран при просадке 40% |
| **Закрытых сделок / Win Rate** | `204` / `63.7%` | Brier Score: `0.1960` |

## 📂 Открытые позиции (7 / 8)
| # | Рынок | Кат. | Исход | Вход (Ask VWAP) | Текущий Bid | Оценка бота | Размер ($) | Нереализ. PnL | Источник |
| :- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| #206 | Will Argentina win on 2026-11-17? | Sports | **YES** | `0.920` | `0.910` | `95.0%` | `$1.00` | `$-0.01` | https://www.fifa.com |
| #207 | Will Ethereum reach $1,850 on November 17? | Crypto | **NO** | `0.890` | `0.890` | `86.4%` | `$1.00` | `$+0.00` | Kraken ETHUSDT 1m/1h Spot Klin |
| #208 | Will the price of Ethereum be above $1,700 on November  | Crypto | **YES** | `0.882` | `0.927` | `95.2%` | `$1.00` | `$+0.05` | Kraken ETHUSDT 1m/1h Spot Klin |
| #209 | Will Bitcoin dip to $62,000 on November 17? | Crypto | **NO** | `0.876` | `0.908` | `95.5%` | `$1.16` | `$+0.04` | Kraken BTCUSDT 1m/1h Spot Klin |
| #210 | Will the price of Bitcoin be above $66,000 on November  | Crypto | **NO** | `0.893` | `0.899` | `90.0%` | `$1.00` | `$+0.01` | Kraken BTCUSDT 1m/1h Spot Klin |
| #211 | Will Elon Musk post 65-89 tweets from November 16 to No | Geopolitics | **NO** | `0.920` | `0.890` | `94.0%` | `$1.00` | `$-0.03` | https://x.com/elonmusk |
| #212 | Fourth Jensen Huang affair reported by November 20? | Other | **NO** | `0.910` | `0.900` | `96.0%` | `$1.00` | `$-0.01` | reporting from the qualifying  |

## 🧪 Теневая песочница (Shadow Sandbox)
| Показатель | Значение |
| :--- | :--- |
| **Виртуальный баланс (Equity)** | **`$58.96 USDC`** |
| **Свободный кэш / В сделках** | `$57.42` / `$1.54 USDC` |
| **Открытых позиций** | `1 / 5` |
| **Текущая просадка** | `2.76%` |

### Открытые позиции в песочнице (1 / 5)
| # | Рынок | Кат. | Исход | Вход (Ask VWAP) | Текущий Bid | Оценка бота | Размер ($) | Нереализ. PnL | Источник |
| :- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| #130 | Will Bitcoin dip to $62,000 on November 17? | Crypto | **NO** | `0.830` | `0.908` | `95.5%` | `$1.41` | `$+0.13` | https://www.binance.com/en/tra |

### Доходность по замороженным категориям (Песочница)
| Категория | Сделок | PnL | Win Rate |
| :--- | :--- | :--- | :--- |
| **Crypto** | `97` | `+$8.20` | `62%` |
| **Geopolitics** | `8` | `+$1.02` | `62%` |
| **Macro** | `5` | `+$0.91` | `60%` |
| **Other** | `19` | `-$1.30` | `42%` |

## 🔍 Последние проверенные кандидаты и фильтр стакана CLOB
| Рынок | Кат. | Сторона | Оценка бота | Цена Ask | Перекос (Edge) | Проскальзывание CLOB | Решение |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Will Ethereum dip to $1,750 on November 17? | Crypto | YES | `99.5%` | `19.0%` | `+80.5 п.п.` | `1.00%` | REJECTED: Contract price $0.190 outside sweet spot [$0.60, $0.92] |
| Will Ethereum dip to $1,750 on November 17? | Crypto | YES | `99.5%` | `17.0%` | `+82.5 п.п.` | `2.00%` | REJECTED: Contract price $0.170 outside sweet spot [$0.60, $0.92] |
| Will Ethereum dip to $1,750 on November 17? | Crypto | YES | `99.5%` | `18.0%` | `+81.5 п.п.` | `1.00%` | REJECTED: Contract price $0.180 outside sweet spot [$0.60, $0.92] |
| Fourth Jensen Huang affair reported by November 20 | Other | NO | `96.0%` | `91.0%` | `+5.0 п.п.` | `1.00%` | EXECUTED BUY #212 ($1.00 @ 0.9100) |
| Will Ethereum dip to $1,750 on November 17? | Crypto | YES | `99.5%` | `19.0%` | `+80.5 п.п.` | `1.00%` | REJECTED: Contract price $0.190 outside sweet spot [$0.60, $0.92] |
| Will Ethereum dip to $1,750 on November 17? | Crypto | YES | `99.5%` | `22.0%` | `+77.5 п.п.` | `1.00%` | REJECTED: Contract price $0.220 outside sweet spot [$0.60, $0.92] |
| Will Ethereum dip to $1,750 on November 17? | Crypto | YES | `99.5%` | `26.0%` | `+73.5 п.п.` | `1.00%` | REJECTED: Contract price $0.260 outside sweet spot [$0.60, $0.92] |
| Will Ethereum dip to $1,750 on November 17? | Crypto | YES | `99.5%` | `25.0%` | `+74.5 п.п.` | `1.00%` | REJECTED: Contract price $0.250 outside sweet spot [$0.60, $0.92] |
| Will South Africa win? | Other | YES | `82.5%` | `73.0%` | `+9.5 п.п.` | `3.00%` | REJECTED: CLOB round-trip slippage 3.00% > 2.0% limit |
| Will Ethereum dip to $1,750 on November 17? | Crypto | YES | `99.5%` | `29.0%` | `+70.5 п.п.` | `2.00%` | REJECTED: Contract price $0.290 outside sweet spot [$0.60, $0.92] |
| Will Ethereum dip to $1,750 on November 17? | Crypto | YES | `99.5%` | `28.0%` | `+71.5 п.п.` | `1.00%` | REJECTED: Contract price $0.280 outside sweet spot [$0.60, $0.92] |
| Will Elon Musk post 65-89 tweets from November 16  | Geopolitics | NO | `95.0%` | `92.0%` | `+3.0 п.п.` | `1.00%` | EXECUTED BUY #211 ($1.00 @ 0.9200) |
| Will South Africa win? | Other | YES | `82.0%` | `74.0%` | `+8.0 п.п.` | `4.00%` | REJECTED: CLOB round-trip slippage 4.00% > 2.0% limit |
| Will Ethereum dip to $1,750 on November 17? | Crypto | YES | `99.5%` | `25.4%` | `+74.2 п.п.` | `1.35%` | REJECTED: Contract price $0.253 outside sweet spot [$0.60, $0.92] |
| Will South Africa win? | Other | YES | `82.5%` | `74.0%` | `+8.5 п.п.` | `4.00%` | REJECTED: CLOB round-trip slippage 4.00% > 2.0% limit |
| Will Ethereum dip to $1,750 on November 17? | Crypto | YES | `99.5%` | `25.0%` | `+74.5 п.п.` | `1.00%` | REJECTED: Contract price $0.250 outside sweet spot [$0.60, $0.92] |
| Will Ethereum dip to $1,750 on November 17? | Crypto | YES | `99.5%` | `30.0%` | `+69.5 п.п.` | `1.00%` | REJECTED: Contract price $0.300 outside sweet spot [$0.60, $0.92] |
| Will Ethereum dip to $1,750 on November 17? | Crypto | YES | `99.5%` | `31.0%` | `+68.5 п.п.` | `1.00%` | REJECTED: Contract price $0.310 outside sweet spot [$0.60, $0.92] |
