# 📊 Отчёт симулятора Polymarket (Устав Grok Bot — Демо-счёт)
**Обновлено:** `2026-11-19 14:31:03 UTC`

## 💰 Состояние виртуального портфеля
| Показатель | Значение | Правило устава |
| :--- | :--- | :--- |
| **Стартовый капитал** | `$50.00 USDC` | Не добавлять деньги |
| **Текущий баланс (Equity)** | **`$28.83 USDC`** (`-21.17$` / `-42.35%`) | Cash + Mark-to-Market по CLOB Bid |
| **Свободный кэш / В сделках** | `$27.76` / `$1.07 USDC` | До 8 открытых позиций, макс 8% банка |
| **Цель окупаемости подписки** | `$-21.17 / $60.00` (`0.0%`) | Цель: +$60.00 в месяц |
| **Просадка от пика (Текущая / Макс)** | `26.64%` / `28.95%` (Пик: `$39.29`) | Стоп-кран при просадке 40% |
| **Закрытых сделок / Win Rate** | `218` / `63.8%` | Brier Score: `0.1960` |

## 📂 Открытые позиции (1 / 8)
| # | Рынок | Кат. | Исход | Вход (Ask VWAP) | Текущий Bid | Оценка бота | Размер ($) | Нереализ. PnL | Источник |
| :- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| #212 | Fourth Jensen Huang affair reported by November 20? | Other | **NO** | `0.910` | `0.970` | `98.5%` | `$1.00` | `$+0.07` | reporting from the qualifying  |

## 🧪 Теневая песочница (Shadow Sandbox)
| Показатель | Значение |
| :--- | :--- |
| **Виртуальный баланс (Equity)** | **`$64.25 USDC`** |
| **Свободный кэш / В сделках** | `$50.39` / `$13.86 USDC` |
| **Открытых позиций** | `5 / 5` |
| **Текущая просадка** | `2.63%` |

### Открытые позиции в песочнице (5 / 5)
| # | Рынок | Кат. | Исход | Вход (Ask VWAP) | Текущий Bid | Оценка бота | Размер ($) | Нереализ. PnL | Источник |
| :- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| #157 | Will Ethereum reach $1,900 November 16-22? | Crypto | **YES** | `0.370` | `0.330` | `47.6%` | `$3.91` | `$-0.42` | https://www.binance.com/en/tra |
| #159 | Will the price of Ethereum be above $1,900 on November  | Crypto | **NO** | `0.900` | `0.900` | `93.5%` | `$3.90` | `$+0.00` | https://www.binance.com/en/tra |
| #160 | Will Bitcoin reach $66,000 November 16-22? | Crypto | **YES** | `0.470` | `0.400` | `55.0%` | `$3.59` | `$-0.53` | https://www.binance.com/en/tra |
| #164 | Canadiens vs. Hurricanes | Weather | **YES** | `0.280` | `0.270` | `33.0%` | `$1.23` | `$-0.04` | https://www.nhl.com/scores |
| #166 | Will Bitcoin reach $65,000 on November 19? | Crypto | **YES** | `0.410` | `0.360` | `45.7%` | `$2.54` | `$-0.31` | https://www.binance.com/en/tra |

### Доходность по замороженным категориям (Песочница)
| Категория | Сделок | PnL | Win Rate |
| :--- | :--- | :--- | :--- |
| **Crypto** | `129` | `+$14.93` | `64%` |
| **Geopolitics** | `8` | `+$1.02` | `62%` |
| **Macro** | `5` | `+$0.91` | `60%` |
| **Other** | `19` | `-$1.30` | `42%` |

## 🔍 Последние проверенные кандидаты и фильтр стакана CLOB
| Рынок | Кат. | Сторона | Оценка бота | Цена Ask | Перекос (Edge) | Проскальзывание CLOB | Решение |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Will Elon Musk post 340-359 tweets from November 1 | Geopolitics | NO | `94.0%` | `89.6%` | `+4.4 п.п.` | `0.50%` | REJECTED: Social Mention Count Guard: Tweet/post count bracket markets prohibited (burst variance trap) |
| Will Elon Musk post 340-359 tweets from November 1 | Geopolitics | NO | `95.1%` | `91.0%` | `+4.1 п.п.` | `0.20%` | REJECTED: Social Mention Count Guard: Tweet/post count bracket markets prohibited (burst variance trap) |
| Israel x Iran ceasefire continues through November | Geopolitics | YES | `98.0%` | `94.0%` | `+4.0 п.п.` | `1.00%` | REJECTED: Contract price $0.940 outside sweet spot [$0.70, $0.92] |
| Israel x Iran ceasefire continues through November | Geopolitics | YES | `98.0%` | `94.0%` | `+4.0 п.п.` | `1.00%` | REJECTED: Contract price $0.940 outside sweet spot [$0.70, $0.92] |
| Will Elon Musk post 400-419 tweets from November 1 | Geopolitics | NO | `94.5%` | `88.0%` | `+6.5 п.п.` | `1.70%` | REJECTED: Social Mention Count Guard: Tweet/post count bracket markets prohibited (burst variance trap) |
| Will Elon Musk post 400-419 tweets from November 1 | Geopolitics | NO | `95.8%` | `91.6%` | `+4.2 п.п.` | `0.90%` | REJECTED: Social Mention Count Guard: Tweet/post count bracket markets prohibited (burst variance trap) |
| Israel x Iran ceasefire continues through November | Geopolitics | YES | `98.0%` | `94.0%` | `+4.0 п.п.` | `1.00%` | REJECTED: Contract price $0.940 outside sweet spot [$0.70, $0.92] |
| Will Elon Musk post 400-419 tweets from November 1 | Geopolitics | NO | `96.7%` | `92.1%` | `+4.5 п.п.` | `1.60%` | REJECTED: Contract price $0.921 outside sweet spot [$0.70, $0.92] |
| Will South Africa win? | Other | YES | `98.0%` | `94.0%` | `+4.0 п.п.` | `2.00%` | REJECTED: Contract price $0.940 outside sweet spot [$0.70, $0.92] |
| Will Elon Musk post 400-419 tweets from November 1 | Geopolitics | NO | `97.0%` | `92.7%` | `+4.3 п.п.` | `0.10%` | REJECTED: Contract price $0.927 outside sweet spot [$0.70, $0.92] |
| Will South Africa win? | Other | YES | `98.0%` | `94.0%` | `+4.0 п.п.` | `2.00%` | REJECTED: Contract price $0.940 outside sweet spot [$0.70, $0.92] |
| Will Elon Musk post 320-339 tweets from November 1 | Geopolitics | NO | `94.2%` | `89.6%` | `+4.5 п.п.` | `1.00%` | REJECTED: Social Mention Count Guard: Tweet/post count bracket markets prohibited (burst variance trap) |
| Will Elon Musk post 380-399 tweets from November 1 | Geopolitics | NO | `94.8%` | `90.6%` | `+4.2 п.п.` | `0.50%` | REJECTED: Social Mention Count Guard: Tweet/post count bracket markets prohibited (burst variance trap) |
| Israel x Iran ceasefire continues through November | Geopolitics | YES | `98.0%` | `94.0%` | `+4.0 п.п.` | `1.00%` | REJECTED: Contract price $0.940 outside sweet spot [$0.70, $0.92] |
| Israel x Iran ceasefire continues through November | Geopolitics | YES | `98.0%` | `94.0%` | `+4.0 п.п.` | `1.00%` | REJECTED: Contract price $0.940 outside sweet spot [$0.70, $0.92] |
| Israel x Iran ceasefire continues through November | Geopolitics | YES | `98.0%` | `94.0%` | `+4.0 п.п.` | `1.00%` | REJECTED: Contract price $0.940 outside sweet spot [$0.70, $0.92] |
| Israel x Iran ceasefire continues through November | Geopolitics | YES | `98.0%` | `94.0%` | `+4.0 п.п.` | `1.00%` | REJECTED: Contract price $0.940 outside sweet spot [$0.70, $0.92] |
| Israel x Iran ceasefire continues through November | Geopolitics | YES | `98.0%` | `94.0%` | `+4.0 п.п.` | `1.00%` | REJECTED: Contract price $0.940 outside sweet spot [$0.70, $0.92] |
