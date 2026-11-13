# 📊 Отчёт симулятора Polymarket (Устав Grok Bot — Демо-счёт)
**Обновлено:** `2026-11-13 06:48:31 UTC`

## 💰 Состояние виртуального портфеля
| Показатель | Значение | Правило устава |
| :--- | :--- | :--- |
| **Стартовый капитал** | `$50.00 USDC` | Не добавлять деньги |
| **Текущий баланс (Equity)** | **`$35.94 USDC`** (`-14.06$` / `-28.13%`) | Cash + Mark-to-Market по CLOB Bid |
| **Свободный кэш / В сделках** | `$30.32` / `$5.62 USDC` | До 8 открытых позиций, макс 8% банка |
| **Цель окупаемости подписки** | `$-14.06 / $60.00` (`0.0%`) | Цель: +$60.00 в месяц |
| **Просадка от пика (Текущая / Макс)** | `8.54%` / `24.45%` (Пик: `$39.29`) | Стоп-кран при просадке 40% |
| **Закрытых сделок / Win Rate** | `168` / `70.2%` | Brier Score: `0.1960` |

## 📂 Открытые позиции (5 / 8)
| # | Рынок | Кат. | Исход | Вход (Ask VWAP) | Текущий Bid | Оценка бота | Размер ($) | Нереализ. PnL | Источник |
| :- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| #155 | Will Elon Musk post 200-219 tweets from November 6 to N | Geopolitics | **NO** | `0.917` | `0.796` | `93.5%` | `$1.07` | `$-0.14` | https://x.com/elonmusk |
| #169 | Jazz vs. Rockets | Sports | **NO** | `0.920` | `0.910` | `95.0%` | `$1.12` | `$-0.01` | https://www.nba.com/ |
| #170 | Bitcoin Up or Down on November 13? | Crypto | **NO** | `0.910` | `0.958` | `98.5%` | `$1.07` | `$+0.06` | https://www.binance.com/en/tra |
| #171 | Will the price of Bitcoin be above $66,000 on November  | Crypto | **YES** | `0.912` | `0.913` | `96.5%` | `$1.08` | `$+0.00` | https://www.binance.com/en/tra |
| #174 | Will the price of Ethereum be above $1,900 on November  | Crypto | **YES** | `0.743` | `0.730` | `77.5%` | `$1.40` | `$-0.02` | Kraken ETHUSDT 1m/1h Spot Klin |

## 🧪 Теневая песочница (Shadow Sandbox)
| Показатель | Значение |
| :--- | :--- |
| **Виртуальный баланс (Equity)** | **`$55.52 USDC`** |
| **Свободный кэш / В сделках** | `$51.42` / `$4.10 USDC` |
| **Открытых позиций** | `3 / 5` |
| **Текущая просадка** | `3.00%` |

### Открытые позиции в песочнице (3 / 5)
| # | Рынок | Кат. | Исход | Вход (Ask VWAP) | Текущий Bid | Оценка бота | Размер ($) | Нереализ. PnL | Источник |
| :- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| #5 | Total Kills Over/Under 27.5 in Game 2? | Other | **NO** | `0.500` | `0.510` | `56.5%` | `$1.42` | `$+0.03` | https://gol.gg/esports/home |
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
| Will the price of Bitcoin be above $70,000 on Nove | Crypto | NO | `83.5%` | `79.3%` | `+4.2 п.п.` | `1.10%` | REJECTED: Duplicate underlying event (crypto:bitcoin:november 13) |
| Will the price of Ethereum be above $1,900 on Nove | Crypto | YES | `76.8%` | `74.3%` | `+2.5 п.п.` | `0.90%` | EXECUTED BUY #174 ($1.40 @ 0.7430) |
| Will the price of Bitcoin be above $66,000 on Nove | Crypto | YES | `94.7%` | `90.6%` | `+4.1 п.п.` | `0.10%` | REJECTED: Duplicate underlying event (crypto:bitcoin:november 13) |
| Will the price of Bitcoin be above $70,000 on Nove | Crypto | NO | `92.8%` | `85.7%` | `+7.1 п.п.` | `0.70%` | REJECTED: Duplicate underlying event (crypto:bitcoin:november 13) |
| Will Bitcoin reach $69,000 on November 13? | Crypto | YES | `99.5%` | `79.0%` | `+20.5 п.п.` | `2.00%` | REJECTED: Duplicate underlying event (crypto:bitcoin:november 13) |
| Will Bitcoin dip to $65,000 on November 13? | Crypto | NO | `94.0%` | `88.0%` | `+6.0 п.п.` | `1.00%` | REJECTED: Duplicate underlying event (crypto:bitcoin:november 13) |
| Will the price of Bitcoin be above $70,000 on Nove | Crypto | NO | `92.7%` | `88.5%` | `+4.2 п.п.` | `0.90%` | REJECTED: Duplicate underlying event (crypto:bitcoin:november 13) |
| Will Bitcoin reach $69,000 on November 13? | Crypto | YES | `99.5%` | `68.0%` | `+31.5 п.п.` | `1.00%` | REJECTED: Duplicate underlying event (crypto:bitcoin:november 13) |
| Will the highest temperature in Houston be between | Weather | NO | `89.3%` | `62.0%` | `+27.3 п.п.` | `3.00%` | REJECTED: Narrow weather bracket NO bet prohibited (airport METAR microclimate tail risk) |
| Will the price of Bitcoin be above $70,000 on Nove | Crypto | NO | `80.8%` | `85.4%` | `-4.6 п.п.` | `3.90%` | REJECTED: Edge -4.6 pp < 2 pp threshold (P_est=80.8% vs AskVWAP=85.4%) |
| Will the highest temperature in Houston be between | Weather | NO | `89.2%` | `62.0%` | `+27.2 п.п.` | `4.00%` | REJECTED: Narrow weather bracket NO bet prohibited (airport METAR microclimate tail risk) |
| Will the price of Bitcoin be above $70,000 on Nove | Crypto | NO | `85.7%` | `80.6%` | `+5.1 п.п.` | `0.10%` | REJECTED: Duplicate underlying event (crypto:bitcoin:november 13) |
| Will the price of Ethereum be above $1,900 on Nove | Crypto | YES | `72.9%` | `67.7%` | `+5.2 п.п.` | `1.50%` | REJECTED: Category cap reached (4/4 in Crypto) |
| Will the price of Bitcoin be above $68,000 on Nove | Crypto | YES | `73.7%` | `67.2%` | `+6.5 п.п.` | `0.10%` | REJECTED: Duplicate underlying event (crypto:bitcoin:november 13) |
| Will the price of Ethereum be above $1,900 on Nove | Crypto | YES | `73.2%` | `68.1%` | `+5.1 п.п.` | `1.90%` | REJECTED: Category cap reached (4/4 in Crypto) |
| Will the price of Bitcoin be above $68,000 on Nove | Crypto | YES | `74.2%` | `70.0%` | `+4.2 п.п.` | `0.10%` | REJECTED: Duplicate underlying event (crypto:bitcoin:november 13) |
| Will the price of Ethereum be above $2,000 on Nove | Crypto | NO | `91.7%` | `87.0%` | `+4.7 п.п.` | `2.00%` | REJECTED: Category cap reached (4/4 in Crypto) |
| Will the price of Bitcoin be above $70,000 on Nove | Crypto | NO | `80.3%` | `73.6%` | `+6.7 п.п.` | `0.10%` | REJECTED: Duplicate underlying event (crypto:bitcoin:november 13) |
