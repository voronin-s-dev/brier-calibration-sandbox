# 📊 Отчёт симулятора Polymarket (Устав Grok Bot — Демо-счёт)
**Обновлено:** `2026-11-18 15:10:28 UTC`

## 💰 Состояние виртуального портфеля
| Показатель | Значение | Правило устава |
| :--- | :--- | :--- |
| **Стартовый капитал** | `$50.00 USDC` | Не добавлять деньги |
| **Текущий баланс (Equity)** | **`$28.81 USDC`** (`-21.19$` / `-42.37%`) | Cash + Mark-to-Market по CLOB Bid |
| **Свободный кэш / В сделках** | `$23.02` / `$5.79 USDC` | До 8 открытых позиций, макс 8% банка |
| **Цель окупаемости подписки** | `$-21.19 / $60.00` (`0.0%`) | Цель: +$60.00 в месяц |
| **Просадка от пика (Текущая / Макс)** | `26.67%` / `28.41%` (Пик: `$39.29`) | Стоп-кран при просадке 40% |
| **Закрытых сделок / Win Rate** | `213` / `63.8%` | Brier Score: `0.1960` |

## 📂 Открытые позиции (4 / 8)
| # | Рынок | Кат. | Исход | Вход (Ask VWAP) | Текущий Bid | Оценка бота | Размер ($) | Нереализ. PnL | Источник |
| :- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| #212 | Fourth Jensen Huang affair reported by November 20? | Other | **NO** | `0.910` | `0.943` | `98.0%` | `$1.00` | `$+0.04` | reporting from the qualifying  |
| #215 | Will the price of Bitcoin be above $62,000 on November  | Crypto | **YES** | `0.738` | `0.753` | `75.3%` | `$1.26` | `$+0.03` | Kraken BTCUSDT 1m/1h Spot Klin |
| #216 | Will the price of Bitcoin be above $62,000 on November  | Crypto | **YES** | `0.791` | `0.802` | `83.0%` | `$2.27` | `$+0.03` | Kraken BTCUSDT 1m/1h Spot Klin |
| #217 | Will the price of Ethereum be above $1,700 on November  | Crypto | **YES** | `0.844` | `0.872` | `88.4%` | `$1.13` | `$+0.04` | Kraken ETHUSDT 1m/1h Spot Klin |

## 🧪 Теневая песочница (Shadow Sandbox)
| Показатель | Значение |
| :--- | :--- |
| **Виртуальный баланс (Equity)** | **`$59.06 USDC`** |
| **Свободный кэш / В сделках** | `$59.06` / `$0.00 USDC` |
| **Открытых позиций** | `0 / 5` |
| **Текущая просадка** | `2.60%` |

### Доходность по замороженным категориям (Песочница)
| Категория | Сделок | PnL | Win Rate |
| :--- | :--- | :--- | :--- |
| **Crypto** | `98` | `+$8.42` | `62%` |
| **Geopolitics** | `8` | `+$1.02` | `62%` |
| **Macro** | `5` | `+$0.91` | `60%` |
| **Other** | `19` | `-$1.30` | `42%` |

## 🔍 Последние проверенные кандидаты и фильтр стакана CLOB
| Рынок | Кат. | Сторона | Оценка бота | Цена Ask | Перекос (Edge) | Проскальзывание CLOB | Решение |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Will Bitcoin dip to $61,000 on November 18? | Crypto | NO | `91.2%` | `82.6%` | `+8.6 п.п.` | `3.20%` | REJECTED: CLOB round-trip slippage 3.20% > 2.0% limit |
| Will Ethereum dip to $1,700 on November 18? | Crypto | NO | `86.2%` | `71.0%` | `+15.2 п.п.` | `1.00%` | EXECUTED BUY #218 ($2.25 @ 0.7100) |
| Will the price of Ethereum be above $1,700 on Nove | Crypto | YES | `91.6%` | `84.4%` | `+7.2 п.п.` | `0.90%` | EXECUTED BUY #217 ($1.13 @ 0.8440) |
| Will the price of Bitcoin be above $62,000 on Nove | Crypto | YES | `85.0%` | `79.1%` | `+5.9 п.п.` | `0.10%` | EXECUTED BUY #216 ($2.27 @ 0.7910) |
| Will Bitcoin dip to $61,000 on November 18? | Crypto | NO | `91.2%` | `86.6%` | `+4.6 п.п.` | `5.50%` | REJECTED: Net EV edge -0.9 pp < 1.5 pp (Gross +4.6 pp - Slippage 5.50%) |
| Will the price of Bitcoin be above $62,000 on Nove | Crypto | YES | `76.7%` | `73.8%` | `+2.9 п.п.` | `1.20%` | EXECUTED BUY #215 ($1.26 @ 0.7380) |
| Will Bitcoin dip to $62,000 on November 18? | Crypto | NO | `76.8%` | `66.0%` | `+10.8 п.п.` | `4.00%` | REJECTED: Contract price $0.660 outside sweet spot [$0.70, $0.87] |
| Will Bitcoin dip to $64,000 on November 18? | Crypto | YES | `90.1%` | `86.0%` | `+4.1 п.п.` | `1.00%` | REJECTED: Duplicate underlying event (crypto:bitcoin:november 18) |
| Will Bitcoin dip to $64,000 on November 18? | Crypto | YES | `93.6%` | `79.0%` | `+14.6 п.п.` | `2.00%` | REJECTED: Duplicate underlying event (crypto:bitcoin:november 18) |
| Will Bitcoin dip to $64,000 on November 18? | Crypto | YES | `92.5%` | `88.0%` | `+4.5 п.п.` | `2.00%` | REJECTED: Contract price $0.880 outside sweet spot [$0.70, $0.87] |
| Will Bitcoin dip to $64,000 on November 18? | Crypto | YES | `86.6%` | `82.0%` | `+4.6 п.п.` | `2.00%` | REJECTED: Duplicate underlying event (crypto:bitcoin:november 18) |
| Will Bitcoin dip to $64,000 on November 18? | Crypto | YES | `88.5%` | `81.0%` | `+7.5 п.п.` | `1.00%` | REJECTED: Duplicate underlying event (crypto:bitcoin:november 18) |
| Will Bitcoin dip to $64,000 on November 18? | Crypto | YES | `89.2%` | `85.0%` | `+4.2 п.п.` | `2.00%` | REJECTED: Duplicate underlying event (crypto:bitcoin:november 18) |
| Will Bitcoin dip to $64,000 on November 18? | Crypto | YES | `87.2%` | `82.0%` | `+5.2 п.п.` | `2.00%` | REJECTED: Duplicate underlying event (crypto:bitcoin:november 18) |
| Will Bitcoin reach $65,000 on November 18? | Crypto | YES | `80.4%` | `75.0%` | `+5.4 п.п.` | `1.00%` | REJECTED: Duplicate underlying event (crypto:bitcoin:november 18) |
| Will Bitcoin reach $65,000 on November 18? | Crypto | YES | `81.1%` | `77.0%` | `+4.1 п.п.` | `1.00%` | REJECTED: Duplicate underlying event (crypto:bitcoin:november 18) |
| Will Bitcoin reach $65,000 on November 18? | Crypto | YES | `82.2%` | `78.0%` | `+4.2 п.п.` | `1.00%` | REJECTED: Duplicate underlying event (crypto:bitcoin:november 18) |
| Will Bitcoin reach $66,000 November 16-22? | Crypto | YES | `77.3%` | `70.0%` | `+7.3 п.п.` | `1.00%` | EXECUTED BUY #214 ($2.34 @ 0.7000) |
