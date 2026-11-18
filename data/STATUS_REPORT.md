# 📊 Отчёт симулятора Polymarket (Устав Grok Bot — Демо-счёт)
**Обновлено:** `2026-11-18 17:01:24 UTC`

## 💰 Состояние виртуального портфеля
| Показатель | Значение | Правило устава |
| :--- | :--- | :--- |
| **Стартовый капитал** | `$50.00 USDC` | Не добавлять деньги |
| **Текущий баланс (Equity)** | **`$28.47 USDC`** (`-21.53$` / `-43.05%`) | Cash + Mark-to-Market по CLOB Bid |
| **Свободный кэш / В сделках** | `$23.88` / `$4.59 USDC` | До 8 открытых позиций, макс 8% банка |
| **Цель окупаемости подписки** | `$-21.53 / $60.00` (`0.0%`) | Цель: +$60.00 в месяц |
| **Просадка от пика (Текущая / Макс)** | `27.53%` / `28.95%` (Пик: `$39.29`) | Стоп-кран при просадке 40% |
| **Закрытых сделок / Win Rate** | `216` / `63.4%` | Brier Score: `0.1960` |

## 📂 Открытые позиции (3 / 8)
| # | Рынок | Кат. | Исход | Вход (Ask VWAP) | Текущий Bid | Оценка бота | Размер ($) | Нереализ. PnL | Источник |
| :- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| #212 | Fourth Jensen Huang affair reported by November 20? | Other | **NO** | `0.910` | `0.950` | `98.0%` | `$1.00` | `$+0.04` | reporting from the qualifying  |
| #217 | Will the price of Ethereum be above $1,700 on November  | Crypto | **YES** | `0.844` | `0.776` | `78.0%` | `$1.13` | `$-0.09` | Kraken ETHUSDT 1m/1h Spot Klin |
| #220 | Will Bitcoin dip to $61,000 on November 18? | Crypto | **NO** | `0.701` | `0.774` | `76.2%` | `$2.27` | `$+0.24` | Kraken BTCUSDT 1m/1h Spot Klin |

## 🧪 Теневая песочница (Shadow Sandbox)
| Показатель | Значение |
| :--- | :--- |
| **Виртуальный баланс (Equity)** | **`$59.66 USDC`** |
| **Свободный кэш / В сделках** | `$53.29` / `$6.37 USDC` |
| **Открытых позиций** | `2 / 5` |
| **Текущая просадка** | `1.62%` |

### Открытые позиции в песочнице (2 / 5)
| # | Рынок | Кат. | Исход | Вход (Ask VWAP) | Текущий Bid | Оценка бота | Размер ($) | Нереализ. PnL | Источник |
| :- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| #132 | Will Bitcoin dip to $60,000 on November 18? | Crypto | **NO** | `0.857` | `0.903` | `93.8%` | `$2.93` | `$+0.16` | https://www.binance.com/en/tra |
| #133 | Will Bitcoin reach $66,000 November 16-22? | Crypto | **YES** | `0.290` | `0.290` | `41.1%` | `$3.28` | `$+0.00` | https://www.binance.com/en/tra |

### Доходность по замороженным категориям (Песочница)
| Категория | Сделок | PnL | Win Rate |
| :--- | :--- | :--- | :--- |
| **Crypto** | `99` | `+$8.87` | `63%` |
| **Geopolitics** | `8` | `+$1.02` | `62%` |
| **Macro** | `5` | `+$0.91` | `60%` |
| **Other** | `19` | `-$1.30` | `42%` |

## 🔍 Последние проверенные кандидаты и фильтр стакана CLOB
| Рынок | Кат. | Сторона | Оценка бота | Цена Ask | Перекос (Edge) | Проскальзывание CLOB | Решение |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Will Bitcoin dip to $62,000 on November 18? | Crypto | YES | `76.3%` | `84.0%` | `-7.7 п.п.` | `1.00%` | REJECTED: Edge -7.7 pp < 2.5 pp threshold (P_est=76.3% vs AskVWAP=84.0%) |
| Will Bitcoin dip to $59,000 on November 18? | Crypto | NO | `97.7%` | `93.5%` | `+4.2 п.п.` | `0.10%` | REJECTED: Contract price $0.935 outside sweet spot [$0.70, $0.87] |
| Will Bitcoin dip to $60,000 on November 18? | Crypto | NO | `95.3%` | `87.7%` | `+7.6 п.п.` | `0.10%` | REJECTED: Contract price $0.877 outside sweet spot [$0.70, $0.87] |
| Will the price of Bitcoin be above $60,000 on Nove | Crypto | YES | `87.8%` | `83.5%` | `+4.3 п.п.` | `0.10%` | REJECTED: Duplicate underlying event (crypto:bitcoin:november 20) |
| Will Ethereum dip to $1,750 on November 18? | Crypto | YES | `76.3%` | `94.0%` | `-17.6 п.п.` | `2.00%` | REJECTED: Edge -17.6 pp < 2.5 pp threshold (P_est=76.3% vs AskVWAP=94.0%) |
| Will Bitcoin dip to $61,000 on November 18? | Crypto | NO | `80.9%` | `70.5%` | `+10.4 п.п.` | `0.10%` | EXECUTED BUY #220 ($2.27 @ 0.7010) |
| Israel x Iran ceasefire continues through November | Geopolitics | YES | `98.0%` | `94.0%` | `+4.0 п.п.` | `1.00%` | REJECTED: Contract price $0.940 outside sweet spot [$0.70, $0.87] |
| Will Bitcoin dip to $62,000 November 16-22? | Crypto | YES | `79.7%` | `74.0%` | `+5.7 п.п.` | `1.00%` | EXECUTED BUY #219 ($2.28 @ 0.7400) |
| Will Bitcoin dip to $60,000 on November 18? | Crypto | NO | `97.3%` | `92.8%` | `+4.5 п.п.` | `0.10%` | REJECTED: Contract price $0.928 outside sweet spot [$0.70, $0.87] |
| Israel x Iran ceasefire continues through November | Geopolitics | YES | `98.0%` | `94.0%` | `+4.0 п.п.` | `1.00%` | REJECTED: Contract price $0.940 outside sweet spot [$0.70, $0.87] |
| Will Bitcoin dip to $61,000 on November 18? | Crypto | NO | `88.1%` | `82.7%` | `+5.4 п.п.` | `4.20%` | REJECTED: Net EV edge +1.2 pp < 1.5 pp (Gross +5.4 pp - Slippage 4.20%) |
| Israel x Iran ceasefire continues through November | Geopolitics | YES | `98.0%` | `94.0%` | `+4.0 п.п.` | `1.00%` | REJECTED: Contract price $0.940 outside sweet spot [$0.70, $0.87] |
| Israel x Iran ceasefire continues through November | Geopolitics | YES | `98.0%` | `94.0%` | `+4.0 п.п.` | `1.00%` | REJECTED: Contract price $0.940 outside sweet spot [$0.70, $0.87] |
| Will Bitcoin dip to $61,000 on November 18? | Crypto | NO | `91.2%` | `82.6%` | `+8.6 п.п.` | `3.20%` | REJECTED: CLOB round-trip slippage 3.20% > 2.0% limit |
| Will Ethereum dip to $1,700 on November 18? | Crypto | NO | `86.2%` | `71.0%` | `+15.2 п.п.` | `1.00%` | EXECUTED BUY #218 ($2.25 @ 0.7100) |
| Will the price of Ethereum be above $1,700 on Nove | Crypto | YES | `91.6%` | `84.4%` | `+7.2 п.п.` | `0.90%` | EXECUTED BUY #217 ($1.13 @ 0.8440) |
| Will the price of Bitcoin be above $62,000 on Nove | Crypto | YES | `85.0%` | `79.1%` | `+5.9 п.п.` | `0.10%` | EXECUTED BUY #216 ($2.27 @ 0.7910) |
| Will Bitcoin dip to $61,000 on November 18? | Crypto | NO | `91.2%` | `86.6%` | `+4.6 п.п.` | `5.50%` | REJECTED: Net EV edge -0.9 pp < 1.5 pp (Gross +4.6 pp - Slippage 5.50%) |
