# 📊 Отчёт симулятора Polymarket (Устав Grok Bot — Демо-счёт)
**Обновлено:** `2026-11-13 14:20:12 UTC`

## 💰 Состояние виртуального портфеля
| Показатель | Значение | Правило устава |
| :--- | :--- | :--- |
| **Стартовый капитал** | `$50.00 USDC` | Не добавлять деньги |
| **Текущий баланс (Equity)** | **`$37.07 USDC`** (`-12.93$` / `-25.87%`) | Cash + Mark-to-Market по CLOB Bid |
| **Свободный кэш / В сделках** | `$27.90` / `$9.17 USDC` | До 8 открытых позиций, макс 8% банка |
| **Цель окупаемости подписки** | `$-12.93 / $60.00` (`0.0%`) | Цель: +$60.00 в месяц |
| **Просадка от пика (Текущая / Макс)** | `5.66%` / `24.45%` (Пик: `$39.29`) | Стоп-кран при просадке 40% |
| **Закрытых сделок / Win Rate** | `170` / `70.6%` | Brier Score: `0.1960` |

## 📂 Открытые позиции (7 / 8)
| # | Рынок | Кат. | Исход | Вход (Ask VWAP) | Текущий Bid | Оценка бота | Размер ($) | Нереализ. PnL | Источник |
| :- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| #169 | Jazz vs. Rockets | Sports | **NO** | `0.920` | `0.900` | `94.0%` | `$1.12` | `$-0.02` | https://www.nba.com/ |
| #170 | Bitcoin Up or Down on November 13? | Crypto | **NO** | `0.910` | `0.959` | `98.5%` | `$1.07` | `$+0.06` | https://www.binance.com/en/tra |
| #171 | Will the price of Bitcoin be above $66,000 on November  | Crypto | **YES** | `0.912` | `0.968` | `98.5%` | `$1.08` | `$+0.07` | https://www.binance.com/en/tra |
| #175 | Fourth Jensen Huang affair reported by November 13? | Other | **NO** | `0.910` | `0.920` | `94.0%` | `$1.08` | `$+0.01` | reporting from the qualifying  |
| #176 | S&P 500 (SPX) Up or Down on November 13? | Macro | **YES** | `0.650` | `0.790` | `86.5%` | `$2.07` | `$+0.45` | https://www.wsj.com/market-dat |
| #177 | Will the price of Ethereum be above $2,000 on November  | Crypto | **NO** | `0.880` | `0.890` | `93.4%` | `$1.09` | `$+0.01` | Kraken ETHUSDT 1m/1h Spot Klin |
| #178 | Will Serbia win on 2026-11-13? | Sports | **NO** | `0.920` | `0.910` | `95.0%` | `$1.10` | `$-0.01` | https://www.uefa.com/uefanatio |

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
| Will the price of Bitcoin be between $68,000 and $ | Crypto | YES | `77.4%` | `71.4%` | `+6.0 п.п.` | `4.30%` | REJECTED: CLOB round-trip slippage 4.30% > 2.0% limit |
| Will the price of Bitcoin be above $70,000 on Nove | Crypto | NO | `79.7%` | `74.9%` | `+4.8 п.п.` | `2.20%` | REJECTED: CLOB round-trip slippage 2.20% > 2.0% limit |
| Will the price of Bitcoin be between $68,000 and $ | Crypto | YES | `75.3%` | `67.8%` | `+7.5 п.п.` | `3.20%` | REJECTED: CLOB round-trip slippage 3.20% > 2.0% limit |
| Will the price of Bitcoin be above $70,000 on Nove | Crypto | NO | `78.0%` | `72.6%` | `+5.4 п.п.` | `0.50%` | REJECTED: Duplicate underlying event (crypto:bitcoin:november 13) |
| Will Serbia win on 2026-11-13? | Sports | NO | `95.0%` | `92.0%` | `+3.0 п.п.` | `1.00%` | EXECUTED BUY #178 ($1.10 @ 0.9200) |
| Will the price of Bitcoin be above $68,000 on Nove | Crypto | YES | `95.4%` | `91.4%` | `+4.0 п.п.` | `3.90%` | REJECTED: CLOB round-trip slippage 3.90% > 2.0% limit |
| Will the price of Bitcoin be between $68,000 and $ | Crypto | YES | `79.0%` | `69.3%` | `+9.7 п.п.` | `0.10%` | REJECTED: Duplicate underlying event (crypto:bitcoin:november 13) |
| Will the price of Bitcoin be above $70,000 on Nove | Crypto | NO | `87.1%` | `79.6%` | `+7.4 п.п.` | `0.10%` | REJECTED: Duplicate underlying event (crypto:bitcoin:november 13) |
| Will the price of Bitcoin be above $70,000 on Nove | Crypto | NO | `86.3%` | `79.0%` | `+7.3 п.п.` | `0.10%` | REJECTED: Duplicate underlying event (crypto:bitcoin:november 13) |
| Will the price of Bitcoin be between $68,000 and $ | Crypto | YES | `76.3%` | `66.0%` | `+10.3 п.п.` | `4.00%` | REJECTED: CLOB round-trip slippage 4.00% > 2.0% limit |
| Will the price of Bitcoin be above $70,000 on Nove | Crypto | NO | `85.9%` | `80.2%` | `+5.7 п.п.` | `0.10%` | REJECTED: Duplicate underlying event (crypto:bitcoin:november 13) |
| Will the price of Bitcoin be between $68,000 and $ | Crypto | YES | `72.9%` | `64.3%` | `+8.6 п.п.` | `4.70%` | REJECTED: CLOB round-trip slippage 4.70% > 2.0% limit |
| Will the price of Bitcoin be above $70,000 on Nove | Crypto | NO | `79.9%` | `74.0%` | `+5.9 п.п.` | `0.10%` | REJECTED: Duplicate underlying event (crypto:bitcoin:november 13) |
| Will the price of Bitcoin be between $68,000 and $ | Crypto | YES | `72.0%` | `64.5%` | `+7.5 п.п.` | `4.50%` | REJECTED: CLOB round-trip slippage 4.50% > 2.0% limit |
| Will the price of Bitcoin be above $70,000 on Nove | Crypto | NO | `79.5%` | `75.5%` | `+4.0 п.п.` | `1.20%` | REJECTED: Duplicate underlying event (crypto:bitcoin:november 13) |
| Will the price of Bitcoin be above $68,000 on Nove | Crypto | YES | `92.8%` | `88.6%` | `+4.2 п.п.` | `0.10%` | REJECTED: Duplicate underlying event (crypto:bitcoin:november 13) |
| Will the price of Bitcoin be between $68,000 and $ | Crypto | YES | `72.1%` | `64.3%` | `+7.8 п.п.` | `4.70%` | REJECTED: CLOB round-trip slippage 4.70% > 2.0% limit |
| Will the price of Bitcoin be above $70,000 on Nove | Crypto | NO | `79.2%` | `73.0%` | `+6.2 п.п.` | `2.40%` | REJECTED: CLOB round-trip slippage 2.40% > 2.0% limit |
