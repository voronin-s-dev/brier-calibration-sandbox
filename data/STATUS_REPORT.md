# 📊 Отчёт симулятора Polymarket (Устав Grok Bot — Демо-счёт)
**Обновлено:** `2026-11-18 14:40:10 UTC`

## 💰 Состояние виртуального портфеля
| Показатель | Значение | Правило устава |
| :--- | :--- | :--- |
| **Стартовый капитал** | `$50.00 USDC` | Не добавлять деньги |
| **Текущий баланс (Equity)** | **`$28.33 USDC`** (`-21.67$` / `-43.34%`) | Cash + Mark-to-Market по CLOB Bid |
| **Свободный кэш / В сделках** | `$21.57` / `$6.76 USDC` | До 8 открытых позиций, макс 8% банка |
| **Цель окупаемости подписки** | `$-21.67 / $60.00` (`0.0%`) | Цель: +$60.00 в месяц |
| **Просадка от пика (Текущая / Макс)** | `27.90%` / `27.90%` (Пик: `$39.29`) | Стоп-кран при просадке 40% |
| **Закрытых сделок / Win Rate** | `211` / `63.5%` | Brier Score: `0.1960` |

## 📂 Открытые позиции (5 / 8)
| # | Рынок | Кат. | Исход | Вход (Ask VWAP) | Текущий Bid | Оценка бота | Размер ($) | Нереализ. PnL | Источник |
| :- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| #210 | Will the price of Bitcoin be above $66,000 on November  | Crypto | **NO** | `0.893` | `0.982` | `98.5%` | `$1.00` | `$+0.10` | Kraken BTCUSDT 1m/1h Spot Klin |
| #212 | Fourth Jensen Huang affair reported by November 20? | Other | **NO** | `0.910` | `0.944` | `98.0%` | `$1.00` | `$+0.04` | reporting from the qualifying  |
| #215 | Will the price of Bitcoin be above $62,000 on November  | Crypto | **YES** | `0.738` | `0.726` | `76.7%` | `$1.26` | `$-0.02` | Kraken BTCUSDT 1m/1h Spot Klin |
| #216 | Will the price of Bitcoin be above $62,000 on November  | Crypto | **YES** | `0.791` | `0.790` | `85.0%` | `$2.27` | `$-0.00` | Kraken BTCUSDT 1m/1h Spot Klin |
| #217 | Will the price of Ethereum be above $1,700 on November  | Crypto | **YES** | `0.844` | `0.835` | `91.6%` | `$1.13` | `$-0.01` | Kraken ETHUSDT 1m/1h Spot Klin |

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
| Will the highest temperature in Chengdu be 19°C on | Weather | NO | `96.2%` | `85.0%` | `+11.2 п.п.` | `6.20%` | REJECTED: Narrow weather bracket NO bet prohibited (airport METAR microclimate tail risk) |
| Will Bitcoin reach $66,000 November 16-22? | Crypto | YES | `73.6%` | `65.0%` | `+8.6 п.п.` | `1.00%` | REJECTED: Contract price $0.650 outside sweet spot [$0.70, $0.87] |
