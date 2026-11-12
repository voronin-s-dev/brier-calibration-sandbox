# 📊 Отчёт симулятора Polymarket (Устав Grok Bot — Демо-счёт)
**Обновлено:** `2026-11-12 19:30:59 UTC`

## 💰 Состояние виртуального портфеля
| Показатель | Значение | Правило устава |
| :--- | :--- | :--- |
| **Стартовый капитал** | `$50.00 USDC` | Не добавлять деньги |
| **Текущий баланс (Equity)** | **`$36.37 USDC`** (`-13.63$` / `-27.27%`) | Cash + Mark-to-Market по CLOB Bid |
| **Свободный кэш / В сделках** | `$30.57` / `$5.80 USDC` | До 8 открытых позиций, макс 8% банка |
| **Цель окупаемости подписки** | `$-13.63 / $60.00` (`0.0%`) | Цель: +$60.00 в месяц |
| **Просадка от пика (Текущая / Макс)** | `7.44%` / `24.45%` (Пик: `$39.29`) | Стоп-кран при просадке 40% |
| **Закрытых сделок / Win Rate** | `160` / `71.2%` | Brier Score: `0.1960` |

## 📂 Открытые позиции (5 / 8)
| # | Рынок | Кат. | Исход | Вход (Ask VWAP) | Текущий Bid | Оценка бота | Размер ($) | Нереализ. PnL | Источник |
| :- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| #154 | Will Elon Musk post 220-239 tweets from November 6 to N | Geopolitics | **NO** | `0.670` | `0.516` | `68.0%` | `$2.33` | `$-0.54` | https://x.com/elonmusk |
| #155 | Will Elon Musk post 200-219 tweets from November 6 to N | Geopolitics | **NO** | `0.917` | `0.690` | `93.5%` | `$1.07` | `$-0.26` | https://x.com/elonmusk |
| #164 | Will the price of Bitcoin be above $74,000 on November  | Crypto | **NO** | `0.920` | `0.930` | `97.0%` | `$1.10` | `$+0.01` | https://www.binance.com/en/tra |
| #165 | Will Bitcoin dip to $70,000 on November 12? | Crypto | **NO** | `0.908` | `0.871` | `79.7%` | `$1.09` | `$-0.04` | https://www.binance.com/en/tra |
| #166 | Will Ethereum dip to $1,950 on November 12? | Crypto | **NO** | `0.920` | `0.870` | `94.5%` | `$1.10` | `$-0.06` | https://www.binance.com/en/tra |

## 🧪 Теневая песочница (Shadow Sandbox)
| Показатель | Значение |
| :--- | :--- |
| **Виртуальный баланс (Equity)** | **`$55.46 USDC`** |
| **Свободный кэш / В сделках** | `$51.42` / `$4.04 USDC` |
| **Открытых позиций** | `3 / 5` |
| **Текущая просадка** | `3.10%` |

### Открытые позиции в песочнице (3 / 5)
| # | Рынок | Кат. | Исход | Вход (Ask VWAP) | Текущий Bid | Оценка бота | Размер ($) | Нереализ. PnL | Источник |
| :- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| #5 | Total Kills Over/Under 27.5 in Game 2? | Other | **NO** | `0.500` | `0.490` | `56.5%` | `$1.42` | `$-0.03` | https://gol.gg/esports/home |
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
| Israel x Iran ceasefire continues through November | Geopolitics | YES | `96.8%` | `92.3%` | `+4.5 п.п.` | `1.90%` | REJECTED: Contract price $0.923 outside sweet spot [$0.60, $0.92] |
| Will Ethereum dip to $1,950 on November 12? | Crypto | NO | `93.5%` | `92.0%` | `+1.5 п.п.` | `2.00%` | EXECUTED BUY #166 ($1.10 @ 0.9200) |
| Will Bitcoin dip to $70,000 on November 12? | Crypto | NO | `94.2%` | `90.8%` | `+3.4 п.п.` | `0.40%` | EXECUTED BUY #165 ($1.09 @ 0.9080) |
| Will the price of Bitcoin be above $74,000 on Nove | Crypto | NO | `95.0%` | `92.0%` | `+3.0 п.п.` | `1.00%` | EXECUTED BUY #164 ($1.10 @ 0.9200) |
| Will Bitcoin dip to $71,000 on November 12? | Crypto | YES | `70.3%` | `62.0%` | `+8.3 п.п.` | `1.00%` | EXECUTED BUY #163 ($3.05 @ 0.6200) |
| Will Bitcoin dip to $71,000 on November 12? | Crypto | YES | `76.8%` | `75.0%` | `+1.8 п.п.` | `2.00%` | EXECUTED BUY #162 ($1.07 @ 0.7500) |
| Will Bitcoin dip to $70,000 on November 12? | Crypto | NO | `77.4%` | `82.1%` | `-4.7 п.п.` | `4.40%` | REJECTED: Edge -4.7 pp < 2 pp threshold (P_est=77.4% vs AskVWAP=82.1%) |
| Will the price of Bitcoin be between $70,000 and $ | Crypto | NO | `75.6%` | `66.0%` | `+9.6 п.п.` | `3.50%` | REJECTED: CLOB round-trip slippage 3.50% > 2.0% limit |
| Will the price of Bitcoin be between $72,000 and $ | Crypto | YES | `72.9%` | `59.0%` | `+13.9 п.п.` | `2.00%` | REJECTED: Contract price $0.590 outside sweet spot [$0.60, $0.92] |
| Will the price of Bitcoin be above $72,000 on Nove | Crypto | YES | `73.7%` | `62.0%` | `+11.7 п.п.` | `1.90%` | REJECTED: Duplicate underlying event (crypto:bitcoin:november 12) |
| Will Ethereum dip to $1,950 on November 12? | Crypto | NO | `76.1%` | `72.0%` | `+4.1 п.п.` | `2.00%` | EXECUTED BUY #161 ($2.24 @ 0.7200) |
| Will the price of Bitcoin be between $72,000 and $ | Crypto | YES | `72.4%` | `64.0%` | `+8.4 п.п.` | `1.00%` | REJECTED: Duplicate underlying event (crypto:bitcoin:november 12) |
| Will Bitcoin dip to $72,000 on November 12? | Crypto | YES | `75.1%` | `80.0%` | `-4.9 п.п.` | `1.00%` | REJECTED: Edge -4.9 pp < 2 pp threshold (P_est=75.1% vs AskVWAP=80.0%) |
| Will the price of Bitcoin be above $72,000 on Nove | Crypto | YES | `74.7%` | `65.8%` | `+8.9 п.п.` | `0.10%` | REJECTED: Duplicate underlying event (crypto:bitcoin:november 12) |
| Will Bitcoin dip to $72,000 on November 12? | Crypto | YES | `74.0%` | `68.0%` | `+6.0 п.п.` | `2.00%` | REJECTED: Duplicate underlying event (crypto:bitcoin:november 12) |
| Will the price of Bitcoin be between $72,000 and $ | Crypto | YES | `74.1%` | `69.0%` | `+5.1 п.п.` | `1.00%` | REJECTED: Duplicate underlying event (crypto:bitcoin:november 12) |
| Will Bitcoin dip to $72,000 November 9-15? | Crypto | YES | `85.0%` | `77.0%` | `+8.1 п.п.` | `1.00%` | EXECUTED BUY #160 ($3.03 @ 0.7700) |
| Will the price of Bitcoin be between $72,000 and $ | Crypto | YES | `73.6%` | `64.0%` | `+9.6 п.п.` | `2.00%` | REJECTED: Duplicate underlying event (crypto:bitcoin:november 12) |
