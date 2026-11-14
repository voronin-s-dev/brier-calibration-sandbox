# 📊 Отчёт симулятора Polymarket (Устав Grok Bot — Демо-счёт)
**Обновлено:** `2026-11-14 03:40:14 UTC`

## 💰 Состояние виртуального портфеля
| Показатель | Значение | Правило устава |
| :--- | :--- | :--- |
| **Стартовый капитал** | `$50.00 USDC` | Не добавлять деньги |
| **Текущий баланс (Equity)** | **`$34.72 USDC`** (`-15.28$` / `-30.57%`) | Cash + Mark-to-Market по CLOB Bid |
| **Свободный кэш / В сделках** | `$31.60` / `$3.12 USDC` | До 8 открытых позиций, макс 8% банка |
| **Цель окупаемости подписки** | `$-15.28 / $60.00` (`0.0%`) | Цель: +$60.00 в месяц |
| **Просадка от пика (Текущая / Макс)** | `11.65%` / `24.45%` (Пик: `$39.29`) | Стоп-кран при просадке 40% |
| **Закрытых сделок / Win Rate** | `182` / `69.2%` | Brier Score: `0.1960` |

## 📂 Открытые позиции (3 / 8)
| # | Рынок | Кат. | Исход | Вход (Ask VWAP) | Текущий Bid | Оценка бота | Размер ($) | Нереализ. PnL | Источник |
| :- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| #180 | Will the price of Bitcoin be above $70,000 on November  | Crypto | **NO** | `0.914` | `0.977` | `98.5%` | `$1.08` | `$+0.07` | https://www.binance.com/en/tra |
| #181 | Will Elon Musk post 90-114 tweets from November 12 to N | Geopolitics | **NO** | `0.918` | `0.945` | `98.4%` | `$1.08` | `$+0.03` | https://x.com/elonmusk |
| #184 | Will the price of Bitcoin be above $66,000 on November  | Crypto | **YES** | `0.910` | `0.717` | `70.5%` | `$1.08` | `$-0.23` | https://www.binance.com/en/tra |

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
| Will Bitcoin reach $70,000 November 9-15? | Crypto | YES | `99.5%` | `12.0%` | `+87.5 п.п.` | `1.00%` | REJECTED: Contract price $0.120 outside sweet spot [$0.60, $0.92] |
| Will Bitcoin reach $70,000 November 9-15? | Crypto | YES | `99.5%` | `15.0%` | `+84.5 п.п.` | `1.46%` | REJECTED: Contract price $0.150 outside sweet spot [$0.60, $0.92] |
| Will the price of Bitcoin be above $66,000 on Nove | Crypto | YES | `94.0%` | `89.1%` | `+5.0 п.п.` | `0.70%` | REJECTED: Duplicate underlying event (crypto:bitcoin:november 14) |
| Will the price of Bitcoin be between $68,000 and $ | Crypto | NO | `74.1%` | `78.9%` | `-4.8 п.п.` | `1.70%` | REJECTED: Edge -4.8 pp < 2 pp threshold (P_est=74.1% vs AskVWAP=78.9%) |
| Will the price of Bitcoin be above $68,000 on Nove | Crypto | NO | `72.1%` | `76.7%` | `-4.6 п.п.` | `0.10%` | REJECTED: Edge -4.6 pp < 2 pp threshold (P_est=72.1% vs AskVWAP=76.7%) |
| Will Bitcoin reach $70,000 November 9-15? | Crypto | YES | `99.5%` | `16.0%` | `+83.5 п.п.` | `1.00%` | REJECTED: Contract price $0.160 outside sweet spot [$0.60, $0.92] |
| Will Bitcoin reach $70,000 November 9-15? | Crypto | YES | `99.5%` | `19.0%` | `+80.5 п.п.` | `1.00%` | REJECTED: Contract price $0.190 outside sweet spot [$0.60, $0.92] |
| Will Bitcoin reach $70,000 November 9-15? | Crypto | YES | `99.5%` | `19.0%` | `+80.5 п.п.` | `1.98%` | REJECTED: Contract price $0.190 outside sweet spot [$0.60, $0.92] |
| Will the price of Bitcoin be between $68,000 and $ | Crypto | NO | `75.0%` | `64.8%` | `+10.2 п.п.` | `1.30%` | REJECTED: Duplicate underlying event (crypto:bitcoin:november 14) |
| Will the price of Bitcoin be above $68,000 on Nove | Crypto | NO | `72.9%` | `63.4%` | `+9.5 п.п.` | `0.10%` | REJECTED: Duplicate underlying event (crypto:bitcoin:november 14) |
| Will the price of Bitcoin be between $68,000 and $ | Crypto | NO | `74.8%` | `69.5%` | `+5.3 п.п.` | `0.10%` | REJECTED: Duplicate underlying event (crypto:bitcoin:november 14) |
| Will the price of Bitcoin be above $68,000 on Nove | Crypto | NO | `72.9%` | `68.2%` | `+4.7 п.п.` | `0.10%` | REJECTED: Duplicate underlying event (crypto:bitcoin:november 14) |
| Will the price of Bitcoin be between $68,000 and $ | Crypto | NO | `73.6%` | `80.5%` | `-6.9 п.п.` | `11.40%` | REJECTED: Edge -6.9 pp < 2 pp threshold (P_est=73.6% vs AskVWAP=80.5%) |
| Will the price of Bitcoin be above $68,000 on Nove | Crypto | NO | `71.2%` | `81.8%` | `-10.6 п.п.` | `3.70%` | REJECTED: Edge -10.6 pp < 2 pp threshold (P_est=71.2% vs AskVWAP=81.8%) |
| Will the FAA's nationwide ground stop be lifted by | Other | NO | `72.5%` | `68.0%` | `+4.5 п.п.` | `2.00%` | REJECTED: Max open positions (8) reached |
| Will the FAA's nationwide ground stop be lifted by | Other | NO | `78.5%` | `74.0%` | `+4.5 п.п.` | `2.00%` | REJECTED: Max open positions (8) reached |
| Will the FAA's nationwide ground stop be lifted by | Other | NO | `94.0%` | `91.0%` | `+3.0 п.п.` | `2.00%` | EXECUTED BUY #186 ($1.12 @ 0.9100) |
| Will the FAA's nationwide ground stop be lifted by | Other | NO | `78.2%` | `69.0%` | `+9.2 п.п.` | `1.00%` | EXECUTED BUY #185 ($2.91 @ 0.6900) |
