# 📊 Отчёт симулятора Polymarket (Устав Grok Bot — Демо-счёт)
**Обновлено:** `2026-11-19 04:49:13 UTC`

## 💰 Состояние виртуального портфеля
| Показатель | Значение | Правило устава |
| :--- | :--- | :--- |
| **Стартовый капитал** | `$50.00 USDC` | Не добавлять деньги |
| **Текущий баланс (Equity)** | **`$28.81 USDC`** (`-21.19$` / `-42.38%`) | Cash + Mark-to-Market по CLOB Bid |
| **Свободный кэш / В сделках** | `$27.76` / `$1.05 USDC` | До 8 открытых позиций, макс 8% банка |
| **Цель окупаемости подписки** | `$-21.19 / $60.00` (`0.0%`) | Цель: +$60.00 в месяц |
| **Просадка от пика (Текущая / Макс)** | `26.67%` / `28.95%` (Пик: `$39.29`) | Стоп-кран при просадке 40% |
| **Закрытых сделок / Win Rate** | `218` / `63.8%` | Brier Score: `0.1960` |

## 📂 Открытые позиции (1 / 8)
| # | Рынок | Кат. | Исход | Вход (Ask VWAP) | Текущий Bid | Оценка бота | Размер ($) | Нереализ. PnL | Источник |
| :- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| #212 | Fourth Jensen Huang affair reported by November 20? | Other | **NO** | `0.910` | `0.958` | `98.0%` | `$1.00` | `$+0.05` | reporting from the qualifying  |

## 🧪 Теневая песочница (Shadow Sandbox)
| Показатель | Значение |
| :--- | :--- |
| **Виртуальный баланс (Equity)** | **`$65.45 USDC`** |
| **Свободный кэш / В сделках** | `$50.10` / `$15.35 USDC` |
| **Открытых позиций** | `5 / 5` |
| **Текущая просадка** | `0.73%` |

### Открытые позиции в песочнице (5 / 5)
| # | Рынок | Кат. | Исход | Вход (Ask VWAP) | Текущий Bid | Оценка бота | Размер ($) | Нереализ. PnL | Источник |
| :- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| #137 | Will the price of Bitcoin be above $66,000 on November  | Crypto | **NO** | `0.920` | `0.935` | `98.5%` | `$3.59` | `$+0.06` | https://www.binance.com/en/tra |
| #150 | Will the price of Bitcoin be above $60,000 on November  | Crypto | **YES** | `0.844` | `0.938` | `96.7%` | `$2.86` | `$+0.32` | https://www.binance.com/en/tra |
| #153 | Will Ethereum reach $1,900 November 16-22? | Crypto | **YES** | `0.310` | `0.324` | `45.4%` | `$3.93` | `$+0.18` | https://www.binance.com/en/tra |
| #154 | Will Bitcoin dip to $62,000 November 16-22? | Crypto | **YES** | `0.644` | `0.560` | `71.0%` | `$3.95` | `$-0.52` | https://www.binance.com/en/tra |
| #155 | Will the price of Ethereum be above $1,800 on November  | Crypto | **NO** | `0.490` | `0.450` | `52.0%` | `$1.07` | `$-0.09` | https://www.binance.com/en/tra |

### Доходность по замороженным категориям (Песочница)
| Категория | Сделок | PnL | Win Rate |
| :--- | :--- | :--- | :--- |
| **Crypto** | `118` | `+$14.87` | `65%` |
| **Geopolitics** | `8` | `+$1.02` | `62%` |
| **Macro** | `5` | `+$0.91` | `60%` |
| **Other** | `19` | `-$1.30` | `42%` |

## 🔍 Последние проверенные кандидаты и фильтр стакана CLOB
| Рынок | Кат. | Сторона | Оценка бота | Цена Ask | Перекос (Edge) | Проскальзывание CLOB | Решение |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Will Elon Musk post 320-339 tweets from November 1 | Geopolitics | NO | `94.2%` | `89.6%` | `+4.5 п.п.` | `1.00%` | REJECTED: Social Mention Count Guard: Tweet/post count bracket markets prohibited (burst variance trap) |
| Will Elon Musk post 380-399 tweets from November 1 | Geopolitics | NO | `94.8%` | `90.6%` | `+4.2 п.п.` | `0.50%` | REJECTED: Social Mention Count Guard: Tweet/post count bracket markets prohibited (burst variance trap) |
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
