# 📊 Отчёт симулятора Polymarket (Устав Grok Bot — Демо-счёт)
**Обновлено:** `2026-11-18 13:19:22 UTC`

## 💰 Состояние виртуального портфеля
| Показатель | Значение | Правило устава |
| :--- | :--- | :--- |
| **Стартовый капитал** | `$50.00 USDC` | Не добавлять деньги |
| **Текущий баланс (Equity)** | **`$28.78 USDC`** (`-21.22$` / `-42.45%`) | Cash + Mark-to-Market по CLOB Bid |
| **Свободный кэш / В сделках** | `$24.96` / `$3.82 USDC` | До 8 открытых позиций, макс 8% банка |
| **Цель окупаемости подписки** | `$-21.22 / $60.00` (`0.0%`) | Цель: +$60.00 в месяц |
| **Просадка от пика (Текущая / Макс)** | `26.76%` / `26.89%` (Пик: `$39.29`) | Стоп-кран при просадке 40% |
| **Закрытых сделок / Win Rate** | `210` / `63.8%` | Brier Score: `0.1960` |

## 📂 Открытые позиции (3 / 8)
| # | Рынок | Кат. | Исход | Вход (Ask VWAP) | Текущий Bid | Оценка бота | Размер ($) | Нереализ. PnL | Источник |
| :- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| #210 | Will the price of Bitcoin be above $66,000 on November  | Crypto | **NO** | `0.893` | `0.961` | `98.5%` | `$1.00` | `$+0.08` | Kraken BTCUSDT 1m/1h Spot Klin |
| #212 | Fourth Jensen Huang affair reported by November 20? | Other | **NO** | `0.910` | `0.945` | `98.0%` | `$1.00` | `$+0.04` | reporting from the qualifying  |
| #214 | Will Bitcoin reach $66,000 November 16-22? | Crypto | **YES** | `0.700` | `0.510` | `62.9%` | `$2.34` | `$-0.64` | Kraken BTCUSDT 1m/1h Spot Klin |

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
| Will Bitcoin reach $66,000 November 16-22? | Crypto | YES | `73.5%` | `66.0%` | `+7.5 п.п.` | `1.00%` | REJECTED: Contract price $0.660 outside sweet spot [$0.70, $0.87] |
| Will the match end in a draw? | Other | NO | `86.1%` | `76.9%` | `+9.2 п.п.` | `2.90%` | REJECTED: CLOB round-trip slippage 2.90% > 2.0% limit |
| Will Bitcoin reach $66,000 November 16-22? | Crypto | YES | `73.5%` | `66.0%` | `+7.5 п.п.` | `1.00%` | REJECTED: Contract price $0.660 outside sweet spot [$0.70, $0.87] |
| Will Bitcoin reach $66,000 November 16-22? | Crypto | YES | `73.5%` | `65.0%` | `+8.5 п.п.` | `1.00%` | REJECTED: Contract price $0.650 outside sweet spot [$0.70, $0.87] |
| Will Bitcoin reach $66,000 November 16-22? | Crypto | YES | `75.5%` | `66.0%` | `+9.5 п.п.` | `1.00%` | REJECTED: Contract price $0.660 outside sweet spot [$0.70, $0.87] |
