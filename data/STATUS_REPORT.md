# 📊 Отчёт симулятора Polymarket (Устав Grok Bot — Демо-счёт)
**Обновлено:** `2026-11-14 02:08:17 UTC`

## 💰 Состояние виртуального портфеля
| Показатель | Значение | Правило устава |
| :--- | :--- | :--- |
| **Стартовый капитал** | `$50.00 USDC` | Не добавлять деньги |
| **Текущий баланс (Equity)** | **`$36.07 USDC`** (`-13.93$` / `-27.87%`) | Cash + Mark-to-Market по CLOB Bid |
| **Свободный кэш / В сделках** | `$29.02` / `$7.04 USDC` | До 8 открытых позиций, макс 8% банка |
| **Цель окупаемости подписки** | `$-13.93 / $60.00` (`0.0%`) | Цель: +$60.00 в месяц |
| **Просадка от пика (Текущая / Макс)** | `8.20%` / `24.45%` (Пик: `$39.29`) | Стоп-кран при просадке 40% |
| **Закрытых сделок / Win Rate** | `179` / `69.8%` | Brier Score: `0.1960` |

## 📂 Открытые позиции (6 / 8)
| # | Рынок | Кат. | Исход | Вход (Ask VWAP) | Текущий Bid | Оценка бота | Размер ($) | Нереализ. PnL | Источник |
| :- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| #175 | Fourth Jensen Huang affair reported by November 13? | Other | **NO** | `0.910` | `0.981` | `98.5%` | `$1.08` | `$+0.08` | reporting from the qualifying  |
| #180 | Will the price of Bitcoin be above $70,000 on November  | Crypto | **NO** | `0.914` | `0.967` | `98.5%` | `$1.08` | `$+0.06` | https://www.binance.com/en/tra |
| #181 | Will Elon Musk post 90-114 tweets from November 12 to N | Geopolitics | **NO** | `0.918` | `0.932` | `96.9%` | `$1.08` | `$+0.02` | https://x.com/elonmusk |
| #182 | Will Bitcoin dip to $67,000 on November 13? | Crypto | **NO** | `0.903` | `0.931` | `97.0%` | `$1.09` | `$+0.03` | https://www.binance.com/en/tra |
| #183 | Spread: Colorado (-4.5) | Sports | **NO** | `0.870` | `0.840` | `97.5%` | `$1.45` | `$-0.05` | https://www.ncaa.com/ |
| #184 | Will the price of Bitcoin be above $66,000 on November  | Crypto | **YES** | `0.910` | `0.941` | `98.2%` | `$1.08` | `$+0.04` | https://www.binance.com/en/tra |

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
| Will the FAA's nationwide ground stop be lifted by | Other | NO | `72.5%` | `68.0%` | `+4.5 п.п.` | `2.00%` | REJECTED: Max open positions (8) reached |
| Will the FAA's nationwide ground stop be lifted by | Other | NO | `78.5%` | `74.0%` | `+4.5 п.п.` | `2.00%` | REJECTED: Max open positions (8) reached |
| Will the FAA's nationwide ground stop be lifted by | Other | NO | `94.0%` | `91.0%` | `+3.0 п.п.` | `2.00%` | EXECUTED BUY #186 ($1.12 @ 0.9100) |
| Will the FAA's nationwide ground stop be lifted by | Other | NO | `78.2%` | `69.0%` | `+9.2 п.п.` | `1.00%` | EXECUTED BUY #185 ($2.91 @ 0.6900) |
| Will the FAA's nationwide ground stop be lifted by | Other | NO | `72.0%` | `63.0%` | `+9.0 п.п.` | `1.00%` | REJECTED: Max open positions (8) reached |
| Will the price of Bitcoin be above $66,000 on Nove | Crypto | YES | `94.4%` | `91.0%` | `+3.4 п.п.` | `0.70%` | EXECUTED BUY #184 ($1.08 @ 0.9100) |
| Spread: Colorado (-4.5) | Sports | NO | `97.5%` | `87.0%` | `+10.5 п.п.` | `2.00%` | EXECUTED BUY #183 ($1.45 @ 0.8700) |
| Will Bitcoin dip to $67,000 on November 13? | Crypto | NO | `94.5%` | `90.2%` | `+4.3 п.п.` | `1.60%` | EXECUTED BUY #182 ($1.09 @ 0.9030) |
| Will Bitcoin dip to $67,000 on November 13? | Crypto | NO | `94.7%` | `90.6%` | `+4.0 п.п.` | `3.10%` | REJECTED: CLOB round-trip slippage 3.10% > 2.0% limit |
| Will Elon Musk post 90-114 tweets from November 12 | Geopolitics | NO | `94.8%` | `91.8%` | `+3.0 п.п.` | `0.10%` | EXECUTED BUY #181 ($1.08 @ 0.9180) |
| Will the price of Bitcoin be above $70,000 on Nove | Crypto | NO | `94.7%` | `91.4%` | `+3.2 п.п.` | `0.30%` | EXECUTED BUY #180 ($1.08 @ 0.9140) |
| Will the price of Bitcoin be above $70,000 on Nove | Crypto | NO | `94.8%` | `89.5%` | `+5.3 п.п.` | `0.50%` | REJECTED: Duplicate underlying event (crypto:bitcoin:november 14) |
| Will the price of Bitcoin be above $70,000 on Nove | Crypto | NO | `95.0%` | `90.8%` | `+4.2 п.п.` | `0.10%` | REJECTED: Duplicate underlying event (crypto:bitcoin:november 14) |
| Will the price of Ethereum be above $2,000 on Nove | Crypto | NO | `95.0%` | `92.0%` | `+3.0 п.п.` | `1.00%` | EXECUTED BUY #179 ($1.08 @ 0.9200) |
| Will Bitcoin dip to $66,000 on November 13? | Crypto | NO | `89.7%` | `95.1%` | `-5.4 п.п.` | `3.80%` | REJECTED: Edge -5.4 pp < 2 pp threshold (P_est=89.7% vs AskVWAP=95.1%) |
| Will the price of Bitcoin be between $68,000 and $ | Crypto | YES | `88.1%` | `82.6%` | `+5.5 п.п.` | `4.00%` | REJECTED: CLOB round-trip slippage 4.00% > 2.0% limit |
| Will the price of Bitcoin be between $68,000 and $ | Crypto | YES | `87.1%` | `77.7%` | `+9.4 п.п.` | `0.40%` | REJECTED: Duplicate underlying event (crypto:bitcoin:november 13) |
| Will the price of Bitcoin be between $68,000 and $ | Crypto | YES | `86.1%` | `77.7%` | `+8.4 п.п.` | `2.20%` | REJECTED: CLOB round-trip slippage 2.20% > 2.0% limit |
