# 📊 Отчёт симулятора Polymarket (Устав Grok Bot — Демо-счёт)
**Обновлено:** `2026-11-12 14:19:27 UTC`

## 💰 Состояние виртуального портфеля
| Показатель | Значение | Правило устава |
| :--- | :--- | :--- |
| **Стартовый капитал** | `$50.00 USDC` | Не добавлять деньги |
| **Текущий баланс (Equity)** | **`$38.15 USDC`** (`-11.85$` / `-23.69%`) | Cash + Mark-to-Market по CLOB Bid |
| **Свободный кэш / В сделках** | `$23.58` / `$14.58 USDC` | До 8 открытых позиций, макс 8% банка |
| **Цель окупаемости подписки** | `$-11.85 / $60.00` (`0.0%`) | Цель: +$60.00 в месяц |
| **Просадка от пика (Текущая / Макс)** | `2.89%` / `24.45%` (Пик: `$39.29`) | Стоп-кран при просадке 40% |
| **Закрытых сделок / Win Rate** | `153` / `72.5%` | Brier Score: `0.1960` |

## 📂 Открытые позиции (7 / 8)
| # | Рынок | Кат. | Исход | Вход (Ask VWAP) | Текущий Bid | Оценка бота | Размер ($) | Нереализ. PnL | Источник |
| :- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| #141 | Will Elon Musk post 280-299 tweets from November 6 to N | Geopolitics | **NO** | `0.850` | `0.972` | `98.5%` | `$3.07` | `$+0.44` | https://x.com/elonmusk |
| #154 | Will Elon Musk post 220-239 tweets from November 6 to N | Geopolitics | **NO** | `0.670` | `0.550` | `68.0%` | `$2.33` | `$-0.42` | https://x.com/elonmusk |
| #155 | Will Elon Musk post 200-219 tweets from November 6 to N | Geopolitics | **NO** | `0.917` | `0.890` | `93.5%` | `$1.07` | `$-0.03` | https://x.com/elonmusk |
| #157 | Will Croatia win on 2026-11-12? | Sports | **NO** | `0.920` | `0.910` | `95.0%` | `$1.10` | `$-0.01` | https://www.uefa.com/uefanatio |
| #159 | Will the price of Bitcoin be above $74,000 on November  | Crypto | **NO** | `0.860` | `0.940` | `97.0%` | `$1.46` | `$+0.14` | Kraken BTCUSDT 1m/1h Spot Klin |
| #160 | Will Bitcoin dip to $72,000 November 9-15? | Crypto | **YES** | `0.770` | `0.930` | `89.7%` | `$3.03` | `$+0.63` | Kraken BTCUSDT 1m/1h Spot Klin |
| #161 | Will Ethereum dip to $1,950 on November 12? | Crypto | **NO** | `0.720` | `0.570` | `74.5%` | `$2.24` | `$-0.47` | Kraken ETHUSDT 1m/1h Spot Klin |

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
| Will the price of Bitcoin be above $72,000 on Nove | Crypto | YES | `79.5%` | `71.3%` | `+8.2 п.п.` | `0.60%` | REJECTED: Duplicate underlying event (crypto:bitcoin:november 12) |
| Will the price of Ethereum be between $2,000 and $ | Crypto | YES | `73.0%` | `43.0%` | `+30.0 п.п.` | `5.00%` | REJECTED: Contract price $0.430 outside sweet spot [$0.60, $0.92] |
| Will Ethereum dip to $1,950 on November 12? | Crypto | NO | `78.4%` | `52.0%` | `+26.4 п.п.` | `4.00%` | REJECTED: Contract price $0.520 outside sweet spot [$0.60, $0.92] |
| Will the price of Bitcoin be between $72,000 and $ | Crypto | YES | `76.3%` | `59.0%` | `+17.3 п.п.` | `1.00%` | REJECTED: Contract price $0.590 outside sweet spot [$0.60, $0.92] |
| Will Bitcoin dip to $72,000 November 9-15? | Crypto | YES | `81.0%` | `91.0%` | `-10.0 п.п.` | `2.00%` | REJECTED: Edge -10.0 pp < 2 pp threshold (P_est=81.0% vs AskVWAP=91.0%) |
| Will the price of Ethereum be above $2,000 on Nove | Crypto | YES | `72.0%` | `46.7%` | `+25.4 п.п.` | `2.80%` | REJECTED: Contract price $0.467 outside sweet spot [$0.60, $0.92] |
| Will the price of Bitcoin be above $74,000 on Nove | Crypto | NO | `89.8%` | `86.0%` | `+3.8 п.п.` | `1.00%` | EXECUTED BUY #159 ($1.46 @ 0.8600) |
