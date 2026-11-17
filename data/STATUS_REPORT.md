# 📊 Отчёт симулятора Polymarket (Устав Grok Bot — Демо-счёт)
**Обновлено:** `2026-11-17 15:19:43 UTC`

## 💰 Состояние виртуального портфеля
| Показатель | Значение | Правило устава |
| :--- | :--- | :--- |
| **Стартовый капитал** | `$50.00 USDC` | Не добавлять деньги |
| **Текущий баланс (Equity)** | **`$29.07 USDC`** (`-20.93$` / `-41.86%`) | Cash + Mark-to-Market по CLOB Bid |
| **Свободный кэш / В сделках** | `$28.08` / `$0.99 USDC` | До 8 открытых позиций, макс 8% банка |
| **Цель окупаемости подписки** | `$-20.93 / $60.00` (`0.0%`) | Цель: +$60.00 в месяц |
| **Просадка от пика (Текущая / Макс)** | `26.02%` / `26.05%` (Пик: `$39.29`) | Стоп-кран при просадке 40% |
| **Закрытых сделок / Win Rate** | `204` / `63.7%` | Brier Score: `0.1960` |

## 📂 Открытые позиции (1 / 8)
| # | Рынок | Кат. | Исход | Вход (Ask VWAP) | Текущий Bid | Оценка бота | Размер ($) | Нереализ. PnL | Источник |
| :- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| #206 | Will Argentina win on 2026-11-17? | Sports | **YES** | `0.920` | `0.910` | `95.0%` | `$1.00` | `$-0.01` | https://www.fifa.com |

## 🧪 Теневая песочница (Shadow Sandbox)
| Показатель | Значение |
| :--- | :--- |
| **Виртуальный баланс (Equity)** | **`$58.50 USDC`** |
| **Свободный кэш / В сделках** | `$48.45` / `$10.05 USDC` |
| **Открытых позиций** | `3 / 5` |
| **Текущая просадка** | `0.00%` |

### Открытые позиции в песочнице (3 / 5)
| # | Рынок | Кат. | Исход | Вход (Ask VWAP) | Текущий Bid | Оценка бота | Размер ($) | Нереализ. PnL | Источник |
| :- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| #100 | Fourth Jensen Huang affair reported by November 20? | Other | **NO** | `0.780` | `0.840` | `90.0%` | `$3.40` | `$+0.26` | reporting from the qualifying  |
| #123 | Will Bitcoin reach $66,000 on November 17? | Crypto | **YES** | `0.250` | `0.250` | `36.2%` | `$2.88` | `$+0.00` | https://www.binance.com/en/tra |
| #124 | S&P 500 (SPX) Up or Down on November 17? | Macro | **NO** | `0.720` | `0.720` | `84.4%` | `$3.51` | `$+0.00` | https://www.wsj.com/market-dat |

### Доходность по замороженным категориям (Песочница)
| Категория | Сделок | PnL | Win Rate |
| :--- | :--- | :--- | :--- |
| **Crypto** | `92` | `+$8.63` | `62%` |
| **Geopolitics** | `7` | `+$1.11` | `71%` |
| **Macro** | `4` | `+$0.28` | `50%` |
| **Other** | `18` | `-$1.78` | `39%` |

## 🔍 Последние проверенные кандидаты и фильтр стакана CLOB
| Рынок | Кат. | Сторона | Оценка бота | Цена Ask | Перекос (Edge) | Проскальзывание CLOB | Решение |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Will Argentina win on 2026-11-17? | Sports | YES | `95.0%` | `92.0%` | `+3.0 п.п.` | `1.00%` | EXECUTED BUY #206 ($1.00 @ 0.9200) |
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
