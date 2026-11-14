# 📊 Отчёт симулятора Polymarket (Устав Grok Bot — Демо-счёт)
**Обновлено:** `2026-11-14 17:30:57 UTC`

## 💰 Состояние виртуального портфеля
| Показатель | Значение | Правило устава |
| :--- | :--- | :--- |
| **Стартовый капитал** | `$50.00 USDC` | Не добавлять деньги |
| **Текущий баланс (Equity)** | **`$34.48 USDC`** (`-15.52$` / `-31.04%`) | Cash + Mark-to-Market по CLOB Bid |
| **Свободный кэш / В сделках** | `$30.74` / `$3.74 USDC` | До 8 открытых позиций, макс 8% банка |
| **Цель окупаемости подписки** | `$-15.52 / $60.00` (`0.0%`) | Цель: +$60.00 в месяц |
| **Просадка от пика (Текущая / Макс)** | `12.25%` / `24.45%` (Пик: `$39.29`) | Стоп-кран при просадке 40% |
| **Закрытых сделок / Win Rate** | `192` / `67.7%` | Brier Score: `0.1960` |

## 📂 Открытые позиции (2 / 8)
| # | Рынок | Кат. | Исход | Вход (Ask VWAP) | Текущий Bid | Оценка бота | Размер ($) | Нереализ. PnL | Источник |
| :- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| #192 | Will Bitcoin dip to $62,000 November 9-15? | Crypto | **NO** | `0.783` | `0.811` | `88.4%` | `$2.73` | `$+0.10` | Kraken BTCUSDT 1m/1h Spot Klin |
| #195 | Will the price of Bitcoin be between $66,000 and $68,00 | Crypto | **NO** | `0.696` | `0.633` | `67.5%` | `$1.00` | `$-0.09` | Kraken BTCUSDT 1m/1h Spot Klin |

## 🧪 Теневая песочница (Shadow Sandbox)
| Показатель | Значение |
| :--- | :--- |
| **Виртуальный баланс (Equity)** | **`$55.49 USDC`** |
| **Свободный кэш / В сделках** | `$51.42` / `$4.07 USDC` |
| **Открытых позиций** | `3 / 5` |
| **Текущая просадка** | `3.05%` |

### Открытые позиции в песочнице (3 / 5)
| # | Рынок | Кат. | Исход | Вход (Ask VWAP) | Текущий Bid | Оценка бота | Размер ($) | Нереализ. PnL | Источник |
| :- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| #5 | Total Kills Over/Under 27.5 in Game 2? | Other | **NO** | `0.500` | `0.500` | `56.5%` | `$1.42` | `$+0.00` | https://gol.gg/esports/home |
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
| Will Ethereum dip to $1,750 on November 14? | Crypto | NO | `85.7%` | `77.6%` | `+8.1 п.п.` | `8.50%` | REJECTED: CLOB round-trip slippage 8.50% > 2.0% limit |
| Will Ethereum dip to $1,750 on November 14? | Crypto | NO | `86.8%` | `77.8%` | `+9.0 п.п.` | `15.50%` | REJECTED: CLOB round-trip slippage 15.50% > 2.0% limit |
| Will Ethereum dip to $1,800 November 9-15? | Crypto | YES | `80.1%` | `87.3%` | `-7.2 п.п.` | `5.90%` | REJECTED: Edge -7.2 pp < 2 pp threshold (P_est=80.1% vs AskVWAP=87.3%) |
| Will Ethereum dip to $1,800 November 9-15? | Crypto | YES | `75.9%` | `88.0%` | `-12.1 п.п.` | `3.00%` | REJECTED: Edge -12.1 pp < 2 pp threshold (P_est=75.9% vs AskVWAP=88.0%) |
| Will Bitcoin dip to $65,000 on November 14? | Crypto | YES | `80.0%` | `100.0%` | `-20.0 п.п.` | `100.00%` | REJECTED: Edge -20.0 pp < 2 pp threshold (P_est=80.0% vs AskVWAP=100.0%) |
| Will the price of Bitcoin be between $66,000 and $ | Crypto | NO | `71.4%` | `69.6%` | `+1.8 п.п.` | `1.20%` | EXECUTED BUY #195 ($1.00 @ 0.6960) |
| Will Bitcoin dip to $65,000 on November 14? | Crypto | YES | `79.6%` | `74.0%` | `+5.6 п.п.` | `1.00%` | EXECUTED BUY #194 ($2.69 @ 0.7400) |
| Will Bitcoin dip to $64,000 on November 14? | Crypto | NO | `79.4%` | `69.4%` | `+10.0 п.п.` | `0.10%` | EXECUTED BUY #193 ($2.71 @ 0.6940) |
| Will Bitcoin dip to $64,000 on November 14? | Crypto | NO | `78.5%` | `72.1%` | `+6.4 п.п.` | `2.60%` | REJECTED: CLOB round-trip slippage 2.60% > 2.0% limit |
| Will the price of Bitcoin be between $66,000 and $ | Crypto | NO | `71.7%` | `63.0%` | `+8.7 п.п.` | `2.70%` | REJECTED: CLOB round-trip slippage 2.70% > 2.0% limit |
| Will Ethereum dip to $1,800 November 9-15? | Crypto | YES | `70.1%` | `62.9%` | `+7.2 п.п.` | `5.70%` | REJECTED: CLOB round-trip slippage 5.70% > 2.0% limit |
| Will Bitcoin dip to $65,000 on November 14? | Crypto | YES | `85.2%` | `58.0%` | `+27.2 п.п.` | `1.00%` | REJECTED: Contract price $0.580 outside sweet spot [$0.60, $0.92] |
| Will Bitcoin dip to $62,000 November 9-15? | Crypto | NO | `83.0%` | `78.3%` | `+4.7 п.п.` | `0.40%` | EXECUTED BUY #192 ($2.73 @ 0.7830) |
| Will Bitcoin dip to $62,000 November 9-15? | Crypto | NO | `82.5%` | `76.4%` | `+6.1 п.п.` | `3.70%` | REJECTED: CLOB round-trip slippage 3.70% > 2.0% limit |
| Will Ethereum dip to $1,800 on November 14? | Crypto | NO | `73.1%` | `59.7%` | `+13.4 п.п.` | `10.00%` | REJECTED: Contract price $0.597 outside sweet spot [$0.60, $0.92] |
| Will Bitcoin dip to $62,000 November 9-15? | Crypto | NO | `91.0%` | `85.5%` | `+5.5 п.п.` | `3.70%` | REJECTED: CLOB round-trip slippage 3.70% > 2.0% limit |
| Will Bitcoin dip to $64,000 on November 14? | Crypto | NO | `82.8%` | `77.6%` | `+5.2 п.п.` | `0.10%` | EXECUTED BUY #191 ($2.81 @ 0.7760) |
| Will Ethereum dip to $1,800 on November 14? | Crypto | NO | `78.0%` | `71.6%` | `+6.4 п.п.` | `8.10%` | REJECTED: CLOB round-trip slippage 8.10% > 2.0% limit |
