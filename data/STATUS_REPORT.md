# 📊 Отчёт симулятора Polymarket (Устав Grok Bot — Демо-счёт)
**Обновлено:** `2026-11-17 09:27:53 UTC`

## 💰 Состояние виртуального портфеля
| Показатель | Значение | Правило устава |
| :--- | :--- | :--- |
| **Стартовый капитал** | `$50.00 USDC` | Не добавлять деньги |
| **Текущий баланс (Equity)** | **`$29.08 USDC`** (`-20.92$` / `-41.84%`) | Cash + Mark-to-Market по CLOB Bid |
| **Свободный кэш / В сделках** | `$29.08` / `$0.00 USDC` | До 8 открытых позиций, макс 8% банка |
| **Цель окупаемости подписки** | `$-20.92 / $60.00` (`0.0%`) | Цель: +$60.00 в месяц |
| **Просадка от пика (Текущая / Макс)** | `25.99%` / `26.05%` (Пик: `$39.29`) | Стоп-кран при просадке 40% |
| **Закрытых сделок / Win Rate** | `204` / `63.7%` | Brier Score: `0.1960` |

## 📂 Открытые позиции (0 / 8)
*Нет активных позиций.*

## 🧪 Теневая песочница (Shadow Sandbox)
| Показатель | Значение |
| :--- | :--- |
| **Виртуальный баланс (Equity)** | **`$56.95 USDC`** |
| **Свободный кэш / В сделках** | `$43.80` / `$13.15 USDC` |
| **Открытых позиций** | `5 / 5` |
| **Текущая просадка** | `1.41%` |

### Открытые позиции в песочнице (5 / 5)
| # | Рынок | Кат. | Исход | Вход (Ask VWAP) | Текущий Bid | Оценка бота | Размер ($) | Нереализ. PnL | Источник |
| :- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| #95 | Will the price of Bitcoin be above $62,000 on November  | Crypto | **YES** | `0.888` | `0.962` | `98.5%` | `$3.39` | `$+0.28` | https://www.binance.com/en/tra |
| #100 | Fourth Jensen Huang affair reported by November 20? | Other | **NO** | `0.780` | `0.830` | `89.0%` | `$3.40` | `$+0.22` | reporting from the qualifying  |
| #105 | Will China PR win on 2026-11-17? | Geopolitics | **YES** | `0.530` | `0.510` | `57.0%` | `$1.64` | `$-0.06` | https://www.fifa.com |
| #107 | Will Zimbabwe win? | Other | **YES** | `0.780` | `0.720` | `82.6%` | `$3.43` | `$-0.26` | https://www.espncricinfo.com/ |
| #109 | Will the price of Ethereum be above $1,800 on November  | Crypto | **NO** | `0.368` | `0.379` | `40.2%` | `$1.08` | `$+0.03` | https://www.binance.com/en/tra |

### Доходность по замороженным категориям (Песочница)
| Категория | Сделок | PnL | Win Rate |
| :--- | :--- | :--- | :--- |
| **Crypto** | `81` | `+$6.81` | `60%` |
| **Geopolitics** | `6` | `+$1.14` | `83%` |
| **Other** | `17` | `-$1.21` | `41%` |

## 🔍 Последние проверенные кандидаты и фильтр стакана CLOB
| Рынок | Кат. | Сторона | Оценка бота | Цена Ask | Перекос (Edge) | Проскальзывание CLOB | Решение |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Will France vs. Türkiye end in a draw? | Sports | NO | `96.5%` | `89.0%` | `+7.5 п.п.` | `1.00%` | EXECUTED BUY #205 ($1.00 @ 0.8900) |
| Spurs vs. Jazz | Sports | YES | `95.0%` | `92.0%` | `+3.0 п.п.` | `1.00%` | EXECUTED BUY #204 ($1.00 @ 0.9200) |
| Will Ethereum dip to $1,600 November 9-15? | Crypto | NO | `98.7%` | `88.4%` | `+10.3 п.п.` | `1.60%` | REJECTED: Category cap reached (4/4 in Crypto) |
| Will the price of Bitcoin be above $66,000 on Nove | Crypto | NO | `77.2%` | `71.7%` | `+5.5 п.п.` | `0.20%` | REJECTED: Duplicate underlying event (crypto:bitcoin:november 17) |
| Will Bitcoin dip to $62,000 November 9-15? | Crypto | NO | `70.5%` | `50.7%` | `+19.9 п.п.` | `3.70%` | REJECTED: Contract price $0.507 outside sweet spot [$0.60, $0.92] |
| Will the price of Ethereum be above $1,600 on Nove | Crypto | YES | `92.0%` | `86.8%` | `+5.2 п.п.` | `3.20%` | REJECTED: CLOB round-trip slippage 3.20% > 2.0% limit |
| Will the price of Ethereum be above $1,600 on Nove | Crypto | YES | `90.0%` | `84.0%` | `+6.0 п.п.` | `1.70%` | REJECTED: Category cap reached (4/4 in Crypto) |
| Will the price of Ethereum be above $1,700 on Nove | Crypto | YES | `89.9%` | `82.4%` | `+7.5 п.п.` | `1.70%` | REJECTED: Category cap reached (4/4 in Crypto) |
| Will Ethereum dip to $1,600 November 9-15? | Crypto | NO | `99.5%` | `88.2%` | `+11.3 п.п.` | `1.10%` | REJECTED: Category cap reached (4/4 in Crypto) |
| Will the price of Bitcoin be above $62,000 on Nove | Crypto | YES | `70.7%` | `79.3%` | `-8.6 п.п.` | `14.50%` | REJECTED: Edge -8.6 pp < 2 pp threshold (P_est=70.7% vs AskVWAP=79.3%) |
| Will Bitcoin dip to $62,000 November 9-15? | Crypto | NO | `72.6%` | `52.1%` | `+20.5 п.п.` | `0.10%` | REJECTED: Contract price $0.521 outside sweet spot [$0.60, $0.92] |
| Will the price of Ethereum be above $1,600 on Nove | Crypto | YES | `89.8%` | `83.4%` | `+6.3 п.п.` | `2.20%` | REJECTED: CLOB round-trip slippage 2.20% > 2.0% limit |
| Will the price of Ethereum be above $1,700 on Nove | Crypto | YES | `90.7%` | `83.8%` | `+6.9 п.п.` | `1.10%` | REJECTED: Category cap reached (4/4 in Crypto) |
| Will Ethereum dip to $1,600 November 9-15? | Crypto | NO | `99.5%` | `90.8%` | `+8.7 п.п.` | `3.00%` | REJECTED: CLOB round-trip slippage 3.00% > 2.0% limit |
| Will Bitcoin dip to $63,000 on November 14? | Crypto | NO | `85.1%` | `59.7%` | `+25.4 п.п.` | `6.40%` | REJECTED: Contract price $0.597 outside sweet spot [$0.60, $0.92] |
| Will the price of Ethereum be above $1,600 on Nove | Crypto | YES | `90.7%` | `85.9%` | `+4.8 п.п.` | `0.10%` | REJECTED: Category cap reached (4/4 in Crypto) |
| Will Bitcoin reach $68,000 November 9-15? | Crypto | NO | `92.7%` | `87.0%` | `+5.7 п.п.` | `1.00%` | REJECTED: Duplicate underlying event (crypto:bitcoin:november 9 - november 15) |
| Will the price of Bitcoin be above $68,000 on Nove | Crypto | NO | `92.6%` | `87.8%` | `+4.8 п.п.` | `0.30%` | REJECTED: Duplicate underlying event (crypto:bitcoin:november 16) |
