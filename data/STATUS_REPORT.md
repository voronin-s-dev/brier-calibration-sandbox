# 📊 Отчёт симулятора Polymarket (Устав Grok Bot — Демо-счёт)
**Обновлено:** `2026-11-17 18:33:44 UTC`

## 💰 Состояние виртуального портфеля
| Показатель | Значение | Правило устава |
| :--- | :--- | :--- |
| **Стартовый капитал** | `$50.00 USDC` | Не добавлять деньги |
| **Текущий баланс (Equity)** | **`$29.05 USDC`** (`-20.95$` / `-41.90%`) | Cash + Mark-to-Market по CLOB Bid |
| **Свободный кэш / В сделках** | `$24.92` / `$4.13 USDC` | До 8 открытых позиций, макс 8% банка |
| **Цель окупаемости подписки** | `$-20.95 / $60.00` (`0.0%`) | Цель: +$60.00 в месяц |
| **Просадка от пика (Текущая / Макс)** | `26.06%` / `26.19%` (Пик: `$39.29`) | Стоп-кран при просадке 40% |
| **Закрытых сделок / Win Rate** | `204` / `63.7%` | Brier Score: `0.1960` |

## 📂 Открытые позиции (4 / 8)
| # | Рынок | Кат. | Исход | Вход (Ask VWAP) | Текущий Bid | Оценка бота | Размер ($) | Нереализ. PnL | Источник |
| :- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| #206 | Will Argentina win on 2026-11-17? | Sports | **YES** | `0.920` | `0.910` | `95.0%` | `$1.00` | `$-0.01` | https://www.fifa.com |
| #207 | Will Ethereum reach $1,850 on November 17? | Crypto | **NO** | `0.890` | `0.840` | `82.1%` | `$1.00` | `$-0.06` | Kraken ETHUSDT 1m/1h Spot Klin |
| #208 | Will the price of Ethereum be above $1,700 on November  | Crypto | **YES** | `0.882` | `0.920` | `94.1%` | `$1.00` | `$+0.04` | Kraken ETHUSDT 1m/1h Spot Klin |
| #209 | Will Bitcoin dip to $62,000 on November 17? | Crypto | **NO** | `0.876` | `0.873` | `89.4%` | `$1.16` | `$-0.00` | Kraken BTCUSDT 1m/1h Spot Klin |

## 🧪 Теневая песочница (Shadow Sandbox)
| Показатель | Значение |
| :--- | :--- |
| **Виртуальный баланс (Equity)** | **`$58.99 USDC`** |
| **Свободный кэш / В сделках** | `$56.12` / `$2.87 USDC` |
| **Открытых позиций** | `2 / 5` |
| **Текущая просадка** | `2.71%` |

### Открытые позиции в песочнице (2 / 5)
| # | Рынок | Кат. | Исход | Вход (Ask VWAP) | Текущий Bid | Оценка бота | Размер ($) | Нереализ. PnL | Источник |
| :- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| #126 | Will Ukraine win on 2026-11-17? | Geopolitics | **YES** | `0.470` | `0.470` | `52.0%` | `$1.39` | `$+0.00` | https://www.uefa.com/uefanatio |
| #130 | Will Bitcoin dip to $62,000 on November 17? | Crypto | **NO** | `0.830` | `0.873` | `89.4%` | `$1.41` | `$+0.07` | https://www.binance.com/en/tra |

### Доходность по замороженным категориям (Песочница)
| Категория | Сделок | PnL | Win Rate |
| :--- | :--- | :--- | :--- |
| **Crypto** | `97` | `+$8.20` | `62%` |
| **Geopolitics** | `7` | `+$1.11` | `71%` |
| **Macro** | `5` | `+$0.91` | `60%` |
| **Other** | `19` | `-$1.30` | `42%` |

## 🔍 Последние проверенные кандидаты и фильтр стакана CLOB
| Рынок | Кат. | Сторона | Оценка бота | Цена Ask | Перекос (Edge) | Проскальзывание CLOB | Решение |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
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
| Will Ethereum dip to $1,750 on November 17? | Crypto | YES | `99.5%` | `33.0%` | `+66.5 п.п.` | `1.00%` | REJECTED: Contract price $0.330 outside sweet spot [$0.60, $0.92] |
| Will Ethereum reach $1,850 on November 17? | Crypto | NO | `90.8%` | `89.0%` | `+1.8 п.п.` | `2.00%` | EXECUTED BUY #207 ($1.00 @ 0.8900) |
| Will Argentina win on 2026-11-17? | Sports | YES | `95.0%` | `92.0%` | `+3.0 п.п.` | `1.00%` | EXECUTED BUY #206 ($1.00 @ 0.9200) |
| Will France vs. Türkiye end in a draw? | Sports | NO | `96.5%` | `89.0%` | `+7.5 п.п.` | `1.00%` | EXECUTED BUY #205 ($1.00 @ 0.8900) |
| Spurs vs. Jazz | Sports | YES | `95.0%` | `92.0%` | `+3.0 п.п.` | `1.00%` | EXECUTED BUY #204 ($1.00 @ 0.9200) |
| Will Ethereum dip to $1,600 November 9-15? | Crypto | NO | `98.7%` | `88.4%` | `+10.3 п.п.` | `1.60%` | REJECTED: Category cap reached (4/4 in Crypto) |
| Will the price of Bitcoin be above $66,000 on Nove | Crypto | NO | `77.2%` | `71.7%` | `+5.5 п.п.` | `0.20%` | REJECTED: Duplicate underlying event (crypto:bitcoin:november 17) |
