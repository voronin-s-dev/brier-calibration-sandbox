# 📊 Отчёт симулятора Polymarket (Устав Grok Bot — Демо-счёт)
**Обновлено:** `2026-11-14 21:07:38 UTC`

## 💰 Состояние виртуального портфеля
| Показатель | Значение | Правило устава |
| :--- | :--- | :--- |
| **Стартовый капитал** | `$50.00 USDC` | Не добавлять деньги |
| **Текущий баланс (Equity)** | **`$32.00 USDC`** (`-18.00$` / `-35.99%`) | Cash + Mark-to-Market по CLOB Bid |
| **Свободный кэш / В сделках** | `$26.34` / `$5.66 USDC` | До 8 открытых позиций, макс 8% банка |
| **Цель окупаемости подписки** | `$-18.00 / $60.00` (`0.0%`) | Цель: +$60.00 в месяц |
| **Просадка от пика (Текущая / Макс)** | `18.55%` / `24.45%` (Пик: `$39.29`) | Стоп-кран при просадке 40% |
| **Закрытых сделок / Win Rate** | `195` / `66.7%` | Brier Score: `0.1960` |

## 📂 Открытые позиции (3 / 8)
| # | Рынок | Кат. | Исход | Вход (Ask VWAP) | Текущий Bid | Оценка бота | Размер ($) | Нереализ. PnL | Источник |
| :- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| #192 | Will Bitcoin dip to $62,000 November 9-15? | Crypto | **NO** | `0.783` | `0.667` | `84.9%` | `$2.73` | `$-0.40` | Kraken BTCUSDT 1m/1h Spot Klin |
| #198 | Will the price of Bitcoin be above $64,000 on November  | Crypto | **YES** | `0.694` | `0.570` | `65.3%` | `$1.00` | `$-0.18` | Kraken BTCUSDT 1m/1h Spot Klin |
| #199 | Will Ethereum dip to $1,700 November 9-15? | Crypto | **NO** | `0.650` | `0.638` | `85.8%` | `$2.56` | `$-0.05` | Kraken ETHUSDT 1m/1h Spot Klin |

## 🧪 Теневая песочница (Shadow Sandbox)
| Показатель | Значение |
| :--- | :--- |
| **Виртуальный баланс (Equity)** | **`$54.42 USDC`** |
| **Свободный кэш / В сделках** | `$52.81` / `$1.61 USDC` |
| **Открытых позиций** | `1 / 5` |
| **Текущая просадка** | `4.92%` |

### Открытые позиции в песочнице (1 / 5)
| # | Рынок | Кат. | Исход | Вход (Ask VWAP) | Текущий Bid | Оценка бота | Размер ($) | Нереализ. PnL | Источник |
| :- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| #20 | Total Kills Over/Under 27.5 in Game 4? | Other | **NO** | `0.500` | `0.510` | `55.9%` | `$1.58` | `$+0.03` | https://gol.gg/esports/home |

### Доходность по замороженным категориям (Песочница)
| Категория | Сделок | PnL | Win Rate |
| :--- | :--- | :--- | :--- |
| **Crypto** | `15` | `+$4.18` | `60%` |
| **Geopolitics** | `4` | `+$0.57` | `75%` |
| **Other** | `15` | `-$0.36` | `47%` |

## 🔍 Последние проверенные кандидаты и фильтр стакана CLOB
| Рынок | Кат. | Сторона | Оценка бота | Цена Ask | Перекос (Edge) | Проскальзывание CLOB | Решение |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Will Ethereum dip to $1,700 November 9-15? | Crypto | NO | `85.8%` | `65.0%` | `+20.8 п.п.` | `1.20%` | EXECUTED BUY #199 ($2.56 @ 0.6500) |
| Will the price of Bitcoin be above $62,000 on Nove | Crypto | YES | `84.4%` | `79.8%` | `+4.6 п.п.` | `3.10%` | REJECTED: CLOB round-trip slippage 3.10% > 2.0% limit |
| Will Bitcoin dip to $63,000 on November 14? | Crypto | NO | `98.2%` | `77.7%` | `+20.5 п.п.` | `11.90%` | REJECTED: CLOB round-trip slippage 11.90% > 2.0% limit |
| Will Bitcoin dip to $64,000 on November 14? | Crypto | NO | `71.8%` | `39.9%` | `+31.9 п.п.` | `7.80%` | REJECTED: Contract price $0.399 outside sweet spot [$0.60, $0.92] |
| Will Ethereum dip to $1,700 November 9-15? | Crypto | NO | `86.0%` | `69.8%` | `+16.2 п.п.` | `2.20%` | REJECTED: CLOB round-trip slippage 2.20% > 2.0% limit |
| Will the price of Bitcoin be above $64,000 on Nove | Crypto | YES | `71.2%` | `69.4%` | `+1.8 п.п.` | `0.60%` | EXECUTED BUY #198 ($1.00 @ 0.6940) |
| Will Bitcoin dip to $64,000 on November 14? | Crypto | NO | `88.2%` | `76.6%` | `+11.6 п.п.` | `1.00%` | EXECUTED BUY #197 ($2.74 @ 0.7660) |
| Will Bitcoin dip to $64,000 on November 14? | Crypto | NO | `88.5%` | `83.8%` | `+4.7 п.п.` | `4.80%` | REJECTED: CLOB round-trip slippage 4.80% > 2.0% limit |
| Will the price of Ethereum be above $1,800 on Nove | Crypto | YES | `77.6%` | `73.1%` | `+4.5 п.п.` | `0.80%` | EXECUTED BUY #196 ($2.32 @ 0.7310) |
| Will Ethereum dip to $1,800 on November 14? | Crypto | NO | `71.1%` | `58.2%` | `+12.9 п.п.` | `6.10%` | REJECTED: Contract price $0.582 outside sweet spot [$0.60, $0.92] |
| Will Ethereum dip to $1,800 on November 14? | Crypto | NO | `71.3%` | `66.0%` | `+5.3 п.п.` | `6.80%` | REJECTED: CLOB round-trip slippage 6.80% > 2.0% limit |
| Will the price of Bitcoin be above $64,000 on Nove | Crypto | YES | `73.2%` | `77.6%` | `-4.4 п.п.` | `2.80%` | REJECTED: Edge -4.4 pp < 2 pp threshold (P_est=73.2% vs AskVWAP=77.6%) |
| Will Bitcoin dip to $64,000 on November 14? | Crypto | NO | `79.9%` | `86.5%` | `-6.6 п.п.` | `3.90%` | REJECTED: Edge -6.6 pp < 2 pp threshold (P_est=79.9% vs AskVWAP=86.5%) |
| Will Ethereum dip to $1,750 on November 14? | Crypto | NO | `85.7%` | `77.6%` | `+8.1 п.п.` | `8.50%` | REJECTED: CLOB round-trip slippage 8.50% > 2.0% limit |
| Will Ethereum dip to $1,750 on November 14? | Crypto | NO | `86.8%` | `77.8%` | `+9.0 п.п.` | `15.50%` | REJECTED: CLOB round-trip slippage 15.50% > 2.0% limit |
| Will Ethereum dip to $1,800 November 9-15? | Crypto | YES | `80.1%` | `87.3%` | `-7.2 п.п.` | `5.90%` | REJECTED: Edge -7.2 pp < 2 pp threshold (P_est=80.1% vs AskVWAP=87.3%) |
| Will Ethereum dip to $1,800 November 9-15? | Crypto | YES | `75.9%` | `88.0%` | `-12.1 п.п.` | `3.00%` | REJECTED: Edge -12.1 pp < 2 pp threshold (P_est=75.9% vs AskVWAP=88.0%) |
| Will Bitcoin dip to $65,000 on November 14? | Crypto | YES | `80.0%` | `100.0%` | `-20.0 п.п.` | `100.00%` | REJECTED: Edge -20.0 pp < 2 pp threshold (P_est=80.0% vs AskVWAP=100.0%) |
