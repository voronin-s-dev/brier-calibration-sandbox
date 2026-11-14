# 📊 Отчёт симулятора Polymarket (Устав Grok Bot — Демо-счёт)
**Обновлено:** `2026-11-14 22:19:18 UTC`

## 💰 Состояние виртуального портфеля
| Показатель | Значение | Правило устава |
| :--- | :--- | :--- |
| **Стартовый капитал** | `$50.00 USDC` | Не добавлять деньги |
| **Текущий баланс (Equity)** | **`$30.89 USDC`** (`-19.11$` / `-38.22%`) | Cash + Mark-to-Market по CLOB Bid |
| **Свободный кэш / В сделках** | `$25.86` / `$5.03 USDC` | До 8 открытых позиций, макс 8% банка |
| **Цель окупаемости подписки** | `$-19.11 / $60.00` (`0.0%`) | Цель: +$60.00 в месяц |
| **Просадка от пика (Текущая / Макс)** | `21.38%` / `24.45%` (Пик: `$39.29`) | Стоп-кран при просадке 40% |
| **Закрытых сделок / Win Rate** | `198` / `65.7%` | Brier Score: `0.1960` |

## 📂 Открытые позиции (3 / 8)
| # | Рынок | Кат. | Исход | Вход (Ask VWAP) | Текущий Bid | Оценка бота | Размер ($) | Нереализ. PnL | Источник |
| :- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| #200 | Will the price of Bitcoin be above $66,000 on November  | Crypto | **NO** | `0.662` | `0.746` | `77.2%` | `$1.58` | `$+0.20` | Kraken BTCUSDT 1m/1h Spot Klin |
| #201 | Will the price of Bitcoin be above $62,000 on November  | Crypto | **YES** | `0.738` | `0.713` | `75.9%` | `$2.50` | `$-0.08` | Kraken BTCUSDT 1m/1h Spot Klin |
| #202 | Will Bitcoin dip to $62,000 on November 14? | Crypto | **NO** | `0.883` | `0.735` | `98.8%` | `$1.00` | `$-0.17` | https://www.binance.com/en/tra |

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
| Will Bitcoin dip to $63,000 on November 14? | Crypto | NO | `71.9%` | `50.6%` | `+21.3 п.п.` | `3.10%` | REJECTED: Contract price $0.506 outside sweet spot [$0.60, $0.92] |
| Will Bitcoin dip to $60,000 November 9-15? | Crypto | NO | `92.7%` | `85.2%` | `+7.5 п.п.` | `2.10%` | REJECTED: CLOB round-trip slippage 2.10% > 2.0% limit |
| Will Bitcoin dip to $60,000 November 9-15? | Crypto | NO | `94.4%` | `82.4%` | `+12.0 п.п.` | `3.40%` | REJECTED: CLOB round-trip slippage 3.40% > 2.0% limit |
| Will Bitcoin dip to $63,000 on November 14? | Crypto | NO | `77.9%` | `36.8%` | `+41.1 п.п.` | `2.70%` | REJECTED: Contract price $0.368 outside sweet spot [$0.60, $0.92] |
| Will Bitcoin dip to $62,000 November 9-15? | Crypto | NO | `72.1%` | `47.6%` | `+24.5 п.п.` | `7.00%` | REJECTED: Contract price $0.476 outside sweet spot [$0.60, $0.92] |
| Will Bitcoin dip to $62,000 on November 14? | Crypto | NO | `93.5%` | `88.3%` | `+5.2 п.п.` | `0.60%` | EXECUTED BUY #202 ($1.00 @ 0.8830) |
| Will Bitcoin dip to $63,000 on November 14? | Crypto | NO | `80.7%` | `74.3%` | `+6.4 п.п.` | `8.30%` | REJECTED: CLOB round-trip slippage 8.30% > 2.0% limit |
| Will Bitcoin dip to $63,000 on November 14? | Crypto | NO | `84.8%` | `74.5%` | `+10.3 п.п.` | `6.50%` | REJECTED: CLOB round-trip slippage 6.50% > 2.0% limit |
| Will the price of Bitcoin be above $62,000 on Nove | Crypto | YES | `73.2%` | `78.1%` | `-4.9 п.п.` | `4.50%` | REJECTED: Edge -4.9 pp < 2 pp threshold (P_est=73.2% vs AskVWAP=78.1%) |
| Will the price of Bitcoin be above $66,000 on Nove | Crypto | NO | `81.6%` | `75.9%` | `+5.7 п.п.` | `0.10%` | REJECTED: Category cap reached (4/4 in Crypto) |
| Will Bitcoin dip to $63,000 on November 14? | Crypto | NO | `84.9%` | `73.4%` | `+11.5 п.п.` | `9.90%` | REJECTED: CLOB round-trip slippage 9.90% > 2.0% limit |
| Will Bitcoin dip to $63,000 on November 14? | Crypto | NO | `86.6%` | `69.8%` | `+16.8 п.п.` | `0.10%` | REJECTED: Category cap reached (4/4 in Crypto) |
| Will the price of Bitcoin be above $62,000 on Nove | Crypto | YES | `79.8%` | `73.8%` | `+6.0 п.п.` | `1.30%` | EXECUTED BUY #201 ($2.50 @ 0.7380) |
| Will Bitcoin dip to $63,000 on November 14? | Crypto | NO | `85.2%` | `65.0%` | `+20.2 п.п.` | `8.30%` | REJECTED: CLOB round-trip slippage 8.30% > 2.0% limit |
| Will the price of Bitcoin be above $66,000 on Nove | Crypto | NO | `70.4%` | `66.2%` | `+4.2 п.п.` | `0.10%` | EXECUTED BUY #200 ($1.58 @ 0.6620) |
| Will Ethereum dip to $1,700 November 9-15? | Crypto | NO | `85.8%` | `65.0%` | `+20.8 п.п.` | `1.20%` | EXECUTED BUY #199 ($2.56 @ 0.6500) |
| Will the price of Bitcoin be above $62,000 on Nove | Crypto | YES | `84.4%` | `79.8%` | `+4.6 п.п.` | `3.10%` | REJECTED: CLOB round-trip slippage 3.10% > 2.0% limit |
| Will Bitcoin dip to $63,000 on November 14? | Crypto | NO | `98.2%` | `77.7%` | `+20.5 п.п.` | `11.90%` | REJECTED: CLOB round-trip slippage 11.90% > 2.0% limit |
