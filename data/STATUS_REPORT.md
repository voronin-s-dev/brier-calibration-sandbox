# 📊 Отчёт симулятора Polymarket (Устав Grok Bot — Демо-счёт)
**Обновлено:** `2026-11-17 19:03:59 UTC`

## 💰 Состояние виртуального портфеля
| Показатель | Значение | Правило устава |
| :--- | :--- | :--- |
| **Стартовый капитал** | `$50.00 USDC` | Не добавлять деньги |
| **Текущий баланс (Equity)** | **`$29.09 USDC`** (`-20.91$` / `-41.81%`) | Cash + Mark-to-Market по CLOB Bid |
| **Свободный кэш / В сделках** | `$23.92` / `$5.17 USDC` | До 8 открытых позиций, макс 8% банка |
| **Цель окупаемости подписки** | `$-20.91 / $60.00` (`0.0%`) | Цель: +$60.00 в месяц |
| **Просадка от пика (Текущая / Макс)** | `25.95%` / `26.19%` (Пик: `$39.29`) | Стоп-кран при просадке 40% |
| **Закрытых сделок / Win Rate** | `204` / `63.7%` | Brier Score: `0.1960` |

## 📂 Открытые позиции (5 / 8)
| # | Рынок | Кат. | Исход | Вход (Ask VWAP) | Текущий Bid | Оценка бота | Размер ($) | Нереализ. PnL | Источник |
| :- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| #206 | Will Argentina win on 2026-11-17? | Sports | **YES** | `0.920` | `0.910` | `95.0%` | `$1.00` | `$-0.01` | https://www.fifa.com |
| #207 | Will Ethereum reach $1,850 on November 17? | Crypto | **NO** | `0.890` | `0.890` | `88.2%` | `$1.00` | `$+0.00` | Kraken ETHUSDT 1m/1h Spot Klin |
| #208 | Will the price of Ethereum be above $1,700 on November  | Crypto | **YES** | `0.882` | `0.910` | `92.8%` | `$1.00` | `$+0.03` | Kraken ETHUSDT 1m/1h Spot Klin |
| #209 | Will Bitcoin dip to $62,000 on November 17? | Crypto | **NO** | `0.876` | `0.858` | `87.2%` | `$1.16` | `$-0.02` | Kraken BTCUSDT 1m/1h Spot Klin |
| #210 | Will the price of Bitcoin be above $66,000 on November  | Crypto | **NO** | `0.893` | `0.908` | `91.1%` | `$1.00` | `$+0.02` | Kraken BTCUSDT 1m/1h Spot Klin |

## 🧪 Теневая песочница (Shadow Sandbox)
| Показатель | Значение |
| :--- | :--- |
| **Виртуальный баланс (Equity)** | **`$58.88 USDC`** |
| **Свободный кэш / В сделках** | `$57.42` / `$1.46 USDC` |
| **Открытых позиций** | `1 / 5` |
| **Текущая просадка** | `2.90%` |

### Открытые позиции в песочнице (1 / 5)
| # | Рынок | Кат. | Исход | Вход (Ask VWAP) | Текущий Bid | Оценка бота | Размер ($) | Нереализ. PnL | Источник |
| :- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| #130 | Will Bitcoin dip to $62,000 on November 17? | Crypto | **NO** | `0.830` | `0.858` | `87.2%` | `$1.41` | `$+0.05` | https://www.binance.com/en/tra |

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
| Will Ethereum dip to $1,750 on November 17? | Crypto | YES | `99.5%` | `30.0%` | `+69.5 п.п.` | `1.00%` | REJECTED: Contract price $0.300 outside sweet spot [$0.60, $0.92] |
| Will Ethereum dip to $1,750 on November 17? | Crypto | YES | `99.5%` | `31.0%` | `+68.5 п.п.` | `1.00%` | REJECTED: Contract price $0.310 outside sweet spot [$0.60, $0.92] |
| Will the price of Bitcoin be above $66,000 on Nove | Crypto | NO | `91.7%` | `89.2%` | `+2.5 п.п.` | `0.10%` | EXECUTED BUY #210 ($1.00 @ 0.8930) |
| Will Ethereum dip to $1,750 on November 17? | Crypto | YES | `99.5%` | `27.0%` | `+72.5 п.п.` | `1.00%` | REJECTED: Contract price $0.270 outside sweet spot [$0.60, $0.92] |
| Will Ethereum dip to $1,750 on November 17? | Crypto | YES | `99.5%` | `33.0%` | `+66.5 п.п.` | `1.00%` | REJECTED: Contract price $0.330 outside sweet spot [$0.60, $0.92] |
| Will South Africa win? | Other | YES | `76.0%` | `72.0%` | `+4.0 п.п.` | `3.00%` | REJECTED: CLOB round-trip slippage 3.00% > 2.0% limit |
| Will Ethereum dip to $1,750 on November 17? | Crypto | YES | `99.5%` | `33.0%` | `+66.5 п.п.` | `1.00%` | REJECTED: Contract price $0.330 outside sweet spot [$0.60, $0.92] |
| Will Bitcoin dip to $62,000 on November 17? | Crypto | NO | `89.4%` | `87.6%` | `+1.8 п.п.` | `0.30%` | EXECUTED BUY #209 ($1.16 @ 0.8760) |
| Will Ethereum dip to $1,750 on November 17? | Crypto | YES | `99.5%` | `26.0%` | `+73.5 п.п.` | `1.00%` | REJECTED: Contract price $0.260 outside sweet spot [$0.60, $0.92] |
| Will Ethereum dip to $1,700 on November 17? | Crypto | NO | `98.2%` | `94.0%` | `+4.2 п.п.` | `2.00%` | REJECTED: Contract price $0.940 outside sweet spot [$0.60, $0.92] |
| Will Ethereum dip to $1,750 on November 17? | Crypto | YES | `99.5%` | `24.0%` | `+75.5 п.п.` | `1.00%` | REJECTED: Contract price $0.240 outside sweet spot [$0.60, $0.92] |
| Will Ethereum dip to $1,750 on November 17? | Crypto | YES | `99.5%` | `31.0%` | `+68.5 п.п.` | `1.00%` | REJECTED: Contract price $0.310 outside sweet spot [$0.60, $0.92] |
| Will Ethereum dip to $1,750 on November 17? | Crypto | YES | `99.5%` | `37.0%` | `+62.5 п.п.` | `1.00%` | REJECTED: Contract price $0.370 outside sweet spot [$0.60, $0.92] |
| Will South Africa win? | Other | YES | `80.9%` | `73.0%` | `+7.9 п.п.` | `4.00%` | REJECTED: CLOB round-trip slippage 4.00% > 2.0% limit |
| Will Ethereum dip to $1,750 on November 17? | Crypto | YES | `99.5%` | `38.0%` | `+61.5 п.п.` | `1.00%` | REJECTED: Contract price $0.380 outside sweet spot [$0.60, $0.92] |
| Will the price of Ethereum be above $1,700 on Nove | Crypto | YES | `90.6%` | `88.2%` | `+2.4 п.п.` | `0.20%` | EXECUTED BUY #208 ($1.00 @ 0.8820) |
| Will Ethereum dip to $1,700 on November 17? | Crypto | NO | `93.5%` | `88.0%` | `+5.5 п.п.` | `2.00%` | REJECTED: Duplicate underlying event (crypto:ethereum:november 17) |
| Will Ethereum dip to $1,700 on November 17? | Crypto | NO | `93.5%` | `89.0%` | `+4.5 п.п.` | `1.00%` | REJECTED: Duplicate underlying event (crypto:ethereum:november 17) |
