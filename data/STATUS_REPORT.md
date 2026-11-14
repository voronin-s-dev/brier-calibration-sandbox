# 📊 Отчёт симулятора Polymarket (Устав Grok Bot — Демо-счёт)
**Обновлено:** `2026-11-14 16:08:03 UTC`

## 💰 Состояние виртуального портфеля
| Показатель | Значение | Правило устава |
| :--- | :--- | :--- |
| **Стартовый капитал** | `$50.00 USDC` | Не добавлять деньги |
| **Текущий баланс (Equity)** | **`$33.86 USDC`** (`-16.14$` / `-32.28%`) | Cash + Mark-to-Market по CLOB Bid |
| **Свободный кэш / В сделках** | `$28.37` / `$5.49 USDC` | До 8 открытых позиций, макс 8% банка |
| **Цель окупаемости подписки** | `$-16.14 / $60.00` (`0.0%`) | Цель: +$60.00 в месяц |
| **Просадка от пика (Текущая / Макс)** | `13.82%` / `24.45%` (Пик: `$39.29`) | Стоп-кран при просадке 40% |
| **Закрытых сделок / Win Rate** | `190` / `67.9%` | Brier Score: `0.1960` |

## 📂 Открытые позиции (2 / 8)
| # | Рынок | Кат. | Исход | Вход (Ask VWAP) | Текущий Bid | Оценка бота | Размер ($) | Нереализ. PnL | Источник |
| :- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| #192 | Will Bitcoin dip to $62,000 November 9-15? | Crypto | **NO** | `0.783` | `0.804` | `87.5%` | `$2.73` | `$+0.07` | Kraken BTCUSDT 1m/1h Spot Klin |
| #193 | Will Bitcoin dip to $64,000 on November 14? | Crypto | **NO** | `0.694` | `0.688` | `72.1%` | `$2.71` | `$-0.02` | Kraken BTCUSDT 1m/1h Spot Klin |

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
| Will Ethereum dip to $1,800 on November 14? | Crypto | NO | `77.9%` | `62.2%` | `+15.7 п.п.` | `4.90%` | REJECTED: CLOB round-trip slippage 4.90% > 2.0% limit |
| Will Ethereum dip to $1,800 November 9-15? | Crypto | NO | `74.2%` | `68.3%` | `+5.9 п.п.` | `3.50%` | REJECTED: CLOB round-trip slippage 3.50% > 2.0% limit |
| Will Bitcoin dip to $66,000 November 9-15? | Crypto | YES | `77.6%` | `71.0%` | `+6.6 п.п.` | `1.40%` | EXECUTED BUY #190 ($2.76 @ 0.7100) |
| Will China PR win on 2026-11-14? | Geopolitics | YES | `70.0%` | `65.0%` | `+5.0 п.п.` | `1.00%` | EXECUTED BUY #189 ($1.97 @ 0.6500) |
| Will the price of Bitcoin be above $68,000 on Nove | Crypto | NO | `81.2%` | `78.7%` | `+2.5 п.п.` | `0.10%` | EXECUTED BUY #188 ($1.61 @ 0.7870) |
| Will the price of Bitcoin be between $68,000 and $ | Crypto | NO | `93.7%` | `86.4%` | `+7.2 п.п.` | `3.00%` | REJECTED: CLOB round-trip slippage 3.00% > 2.0% limit |
| Will Bitcoin dip to $66,000 November 9-15? | Crypto | YES | `77.4%` | `73.2%` | `+4.2 п.п.` | `0.90%` | EXECUTED BUY #187 ($2.19 @ 0.7310) |
