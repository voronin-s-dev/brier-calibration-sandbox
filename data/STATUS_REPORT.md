# 📊 Отчёт симулятора Polymarket (Устав Grok Bot — Демо-счёт)
**Обновлено:** `2026-11-13 03:10:43 UTC`

## 💰 Состояние виртуального портфеля
| Показатель | Значение | Правило устава |
| :--- | :--- | :--- |
| **Стартовый капитал** | `$50.00 USDC` | Не добавлять деньги |
| **Текущий баланс (Equity)** | **`$37.76 USDC`** (`-12.24$` / `-24.48%`) | Cash + Mark-to-Market по CLOB Bid |
| **Свободный кэш / В сделках** | `$30.54` / `$7.22 USDC` | До 8 открытых позиций, макс 8% банка |
| **Цель окупаемости подписки** | `$-12.24 / $60.00` (`0.0%`) | Цель: +$60.00 в месяц |
| **Просадка от пика (Текущая / Макс)** | `3.90%` / `24.45%` (Пик: `$39.29`) | Стоп-кран при просадке 40% |
| **Закрытых сделок / Win Rate** | `162` / `71.0%` | Brier Score: `0.1960` |

## 📂 Открытые позиции (6 / 8)
| # | Рынок | Кат. | Исход | Вход (Ask VWAP) | Текущий Bid | Оценка бота | Размер ($) | Нереализ. PnL | Источник |
| :- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| #154 | Will Elon Musk post 220-239 tweets from November 6 to N | Geopolitics | **NO** | `0.670` | `0.694` | `68.0%` | `$2.33` | `$+0.08` | https://x.com/elonmusk |
| #155 | Will Elon Musk post 200-219 tweets from November 6 to N | Geopolitics | **NO** | `0.917` | `0.377` | `93.5%` | `$1.07` | `$-0.63` | https://x.com/elonmusk |
| #164 | Will the price of Bitcoin be above $74,000 on November  | Crypto | **NO** | `0.920` | `0.982` | `98.5%` | `$1.10` | `$+0.07` | https://www.binance.com/en/tra |
| #166 | Will Ethereum dip to $1,950 on November 12? | Crypto | **NO** | `0.920` | `0.880` | `94.5%` | `$1.10` | `$-0.05` | https://www.binance.com/en/tra |
| #168 | Will Bitcoin dip to $69,000 on November 12? | Crypto | **NO** | `0.908` | `0.840` | `94.5%` | `$1.12` | `$-0.08` | Kraken BTCUSDT 1m/1h Spot Klin |
| #169 | Jazz vs. Rockets | Sports | **NO** | `0.920` | `0.910` | `95.0%` | `$1.12` | `$-0.01` | https://www.nba.com/ |

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
| Will the price of Bitcoin be above $68,000 on Nove | Crypto | YES | `94.0%` | `89.6%` | `+4.5 п.п.` | `1.30%` | REJECTED: Duplicate underlying event (crypto:bitcoin:november 13) |
| Will the highest temperature in Houston be between | Weather | NO | `85.0%` | `62.0%` | `+23.1 п.п.` | `3.00%` | REJECTED: Narrow weather bracket NO bet prohibited (airport METAR microclimate tail risk) |
| Will the highest temperature in Houston be between | Weather | NO | `85.2%` | `62.0%` | `+23.2 п.п.` | `3.00%` | REJECTED: Narrow weather bracket NO bet prohibited (airport METAR microclimate tail risk) |
| Jazz vs. Rockets | Sports | NO | `95.0%` | `92.0%` | `+3.0 п.п.` | `1.00%` | EXECUTED BUY #169 ($1.12 @ 0.9200) |
| Will Bitcoin dip to $69,000 on November 12? | Crypto | NO | `98.2%` | `91.7%` | `+6.5 п.п.` | `1.20%` | EXECUTED BUY #168 ($1.12 @ 0.9080) |
| Will Bitcoin dip to $70,000 on November 12? | Crypto | NO | `75.7%` | `63.0%` | `+12.7 п.п.` | `7.00%` | REJECTED: CLOB round-trip slippage 7.00% > 2.0% limit |
| Will Bitcoin dip to $70,000 on November 12? | Crypto | NO | `85.6%` | `90.6%` | `-5.0 п.п.` | `4.00%` | REJECTED: Edge -5.0 pp < 2 pp threshold (P_est=85.6% vs AskVWAP=90.6%) |
| Will Bitcoin dip to $70,000 November 9-15? | Crypto | YES | `78.1%` | `70.0%` | `+8.1 п.п.` | `2.00%` | EXECUTED BUY #167 ($2.89 @ 0.7000) |
| Will Bitcoin dip to $71,000 on November 12? | Crypto | YES | `70.7%` | `75.0%` | `-4.3 п.п.` | `2.00%` | REJECTED: Edge -4.3 pp < 2 pp threshold (P_est=70.7% vs AskVWAP=75.0%) |
| Will Bitcoin dip to $71,000 on November 12? | Crypto | YES | `70.5%` | `53.0%` | `+17.5 п.п.` | `1.00%` | REJECTED: Contract price $0.530 outside sweet spot [$0.60, $0.92] |
| Israel x Iran ceasefire continues through November | Geopolitics | YES | `96.8%` | `92.3%` | `+4.5 п.п.` | `1.90%` | REJECTED: Contract price $0.923 outside sweet spot [$0.60, $0.92] |
| Will Ethereum dip to $1,950 on November 12? | Crypto | NO | `93.5%` | `92.0%` | `+1.5 п.п.` | `2.00%` | EXECUTED BUY #166 ($1.10 @ 0.9200) |
| Will Bitcoin dip to $70,000 on November 12? | Crypto | NO | `94.2%` | `90.8%` | `+3.4 п.п.` | `0.40%` | EXECUTED BUY #165 ($1.09 @ 0.9080) |
| Will the price of Bitcoin be above $74,000 on Nove | Crypto | NO | `95.0%` | `92.0%` | `+3.0 п.п.` | `1.00%` | EXECUTED BUY #164 ($1.10 @ 0.9200) |
| Will Bitcoin dip to $71,000 on November 12? | Crypto | YES | `70.3%` | `62.0%` | `+8.3 п.п.` | `1.00%` | EXECUTED BUY #163 ($3.05 @ 0.6200) |
| Will Bitcoin dip to $71,000 on November 12? | Crypto | YES | `76.8%` | `75.0%` | `+1.8 п.п.` | `2.00%` | EXECUTED BUY #162 ($1.07 @ 0.7500) |
| Will Bitcoin dip to $70,000 on November 12? | Crypto | NO | `77.4%` | `82.1%` | `-4.7 п.п.` | `4.40%` | REJECTED: Edge -4.7 pp < 2 pp threshold (P_est=77.4% vs AskVWAP=82.1%) |
| Will the price of Bitcoin be between $70,000 and $ | Crypto | NO | `75.6%` | `66.0%` | `+9.6 п.п.` | `3.50%` | REJECTED: CLOB round-trip slippage 3.50% > 2.0% limit |
