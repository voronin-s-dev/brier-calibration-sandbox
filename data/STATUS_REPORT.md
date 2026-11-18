# 📊 Отчёт симулятора Polymarket (Устав Grok Bot — Демо-счёт)
**Обновлено:** `2026-11-18 20:40:10 UTC`

## 💰 Состояние виртуального портфеля
| Показатель | Значение | Правило устава |
| :--- | :--- | :--- |
| **Стартовый капитал** | `$50.00 USDC` | Не добавлять деньги |
| **Текущий баланс (Equity)** | **`$28.62 USDC`** (`-21.38$` / `-42.76%`) | Cash + Mark-to-Market по CLOB Bid |
| **Свободный кэш / В сделках** | `$26.48` / `$2.14 USDC` | До 8 открытых позиций, макс 8% банка |
| **Цель окупаемости подписки** | `$-21.38 / $60.00` (`0.0%`) | Цель: +$60.00 в месяц |
| **Просадка от пика (Текущая / Макс)** | `27.15%` / `28.95%` (Пик: `$39.29`) | Стоп-кран при просадке 40% |
| **Закрытых сделок / Win Rate** | `217` / `63.6%` | Brier Score: `0.1960` |

## 📂 Открытые позиции (2 / 8)
| # | Рынок | Кат. | Исход | Вход (Ask VWAP) | Текущий Bid | Оценка бота | Размер ($) | Нереализ. PnL | Источник |
| :- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| #212 | Fourth Jensen Huang affair reported by November 20? | Other | **NO** | `0.910` | `0.957` | `98.0%` | `$1.00` | `$+0.05` | reporting from the qualifying  |
| #217 | Will the price of Ethereum be above $1,700 on November  | Crypto | **YES** | `0.844` | `0.813` | `80.8%` | `$1.13` | `$-0.04` | Kraken ETHUSDT 1m/1h Spot Klin |

## 🧪 Теневая песочница (Shadow Sandbox)
| Показатель | Значение |
| :--- | :--- |
| **Виртуальный баланс (Equity)** | **`$62.40 USDC`** |
| **Свободный кэш / В сделках** | `$52.22` / `$10.18 USDC` |
| **Открытых позиций** | `4 / 5` |
| **Текущая просадка** | `0.29%` |

### Открытые позиции в песочнице (4 / 5)
| # | Рынок | Кат. | Исход | Вход (Ask VWAP) | Текущий Bid | Оценка бота | Размер ($) | Нереализ. PnL | Источник |
| :- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| #134 | Will Ethereum dip to $1,600 November 16-22? | Crypto | **YES** | `0.230` | `0.210` | `28.6%` | `$1.26` | `$-0.11` | https://www.binance.com/en/tra |
| #137 | Will the price of Bitcoin be above $66,000 on November  | Crypto | **NO** | `0.920` | `0.950` | `98.5%` | `$3.59` | `$+0.12` | https://www.binance.com/en/tra |
| #139 | Will Bitcoin dip to $60,000 November 16-22? | Crypto | **YES** | `0.390` | `0.400` | `51.5%` | `$2.38` | `$+0.06` | https://www.binance.com/en/tra |
| #141 | Will Bitcoin dip to $62,000 on November 18? | Crypto | **YES** | `0.460` | `0.480` | `63.1%` | `$2.76` | `$+0.12` | https://www.binance.com/en/tra |

### Доходность по замороженным категориям (Песочница)
| Категория | Сделок | PnL | Win Rate |
| :--- | :--- | :--- | :--- |
| **Crypto** | `105` | `+$11.58` | `65%` |
| **Geopolitics** | `8` | `+$1.02` | `62%` |
| **Macro** | `5` | `+$0.91` | `60%` |
| **Other** | `19` | `-$1.30` | `42%` |

## 🔍 Последние проверенные кандидаты и фильтр стакана CLOB
| Рынок | Кат. | Сторона | Оценка бота | Цена Ask | Перекос (Edge) | Проскальзывание CLOB | Решение |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Israel x Iran ceasefire continues through November | Geopolitics | YES | `98.0%` | `94.0%` | `+4.0 п.п.` | `1.00%` | REJECTED: Contract price $0.940 outside sweet spot [$0.70, $0.92] |
| Israel x Iran ceasefire continues through November | Geopolitics | YES | `98.0%` | `94.0%` | `+4.0 п.п.` | `1.00%` | REJECTED: Contract price $0.940 outside sweet spot [$0.70, $0.92] |
| Israel x Iran ceasefire continues through November | Geopolitics | YES | `98.0%` | `94.0%` | `+4.0 п.п.` | `1.00%` | REJECTED: Contract price $0.940 outside sweet spot [$0.70, $0.92] |
| Israel x Iran ceasefire continues through November | Geopolitics | YES | `98.0%` | `94.0%` | `+4.0 п.п.` | `1.00%` | REJECTED: Contract price $0.940 outside sweet spot [$0.70, $0.92] |
| Israel x Iran ceasefire continues through November | Geopolitics | YES | `98.0%` | `94.0%` | `+4.0 п.п.` | `1.00%` | REJECTED: Contract price $0.940 outside sweet spot [$0.70, $0.92] |
| Israel x Iran ceasefire continues through November | Geopolitics | YES | `98.0%` | `94.0%` | `+4.0 п.п.` | `1.00%` | REJECTED: Contract price $0.940 outside sweet spot [$0.70, $0.92] |
| Israel x Iran ceasefire continues through November | Geopolitics | YES | `98.0%` | `94.0%` | `+4.0 п.п.` | `1.00%` | REJECTED: Contract price $0.940 outside sweet spot [$0.70, $0.92] |
| Will Elon Musk post 300-319 tweets from November 1 | Geopolitics | NO | `95.4%` | `91.3%` | `+4.1 п.п.` | `0.70%` | REJECTED: Social Mention Count Guard: Tweet/post count bracket markets prohibited (burst variance trap) |
| Israel x Iran ceasefire continues through November | Geopolitics | YES | `98.0%` | `94.0%` | `+4.0 п.п.` | `1.00%` | REJECTED: Contract price $0.940 outside sweet spot [$0.70, $0.92] |
| Will Bitcoin dip to $62,000 on November 18? | Crypto | YES | `76.3%` | `84.0%` | `-7.7 п.п.` | `1.00%` | REJECTED: Edge -7.7 pp < 2.5 pp threshold (P_est=76.3% vs AskVWAP=84.0%) |
| Will Bitcoin dip to $59,000 on November 18? | Crypto | NO | `97.7%` | `93.5%` | `+4.2 п.п.` | `0.10%` | REJECTED: Contract price $0.935 outside sweet spot [$0.70, $0.87] |
| Will Bitcoin dip to $60,000 on November 18? | Crypto | NO | `95.3%` | `87.7%` | `+7.6 п.п.` | `0.10%` | REJECTED: Contract price $0.877 outside sweet spot [$0.70, $0.87] |
| Will the price of Bitcoin be above $60,000 on Nove | Crypto | YES | `87.8%` | `83.5%` | `+4.3 п.п.` | `0.10%` | REJECTED: Duplicate underlying event (crypto:bitcoin:november 20) |
| Will Ethereum dip to $1,750 on November 18? | Crypto | YES | `76.3%` | `94.0%` | `-17.6 п.п.` | `2.00%` | REJECTED: Edge -17.6 pp < 2.5 pp threshold (P_est=76.3% vs AskVWAP=94.0%) |
| Will Bitcoin dip to $61,000 on November 18? | Crypto | NO | `80.9%` | `70.5%` | `+10.4 п.п.` | `0.10%` | EXECUTED BUY #220 ($2.27 @ 0.7010) |
| Israel x Iran ceasefire continues through November | Geopolitics | YES | `98.0%` | `94.0%` | `+4.0 п.п.` | `1.00%` | REJECTED: Contract price $0.940 outside sweet spot [$0.70, $0.87] |
| Will Bitcoin dip to $62,000 November 16-22? | Crypto | YES | `79.7%` | `74.0%` | `+5.7 п.п.` | `1.00%` | EXECUTED BUY #219 ($2.28 @ 0.7400) |
| Will Bitcoin dip to $60,000 on November 18? | Crypto | NO | `97.3%` | `92.8%` | `+4.5 п.п.` | `0.10%` | REJECTED: Contract price $0.928 outside sweet spot [$0.70, $0.87] |
