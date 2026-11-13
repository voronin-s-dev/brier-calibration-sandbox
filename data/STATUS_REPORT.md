# 📊 Отчёт симулятора Polymarket (Устав Grok Bot — Демо-счёт)
**Обновлено:** `2026-11-13 03:31:30 UTC`

## 💰 Состояние виртуального портфеля
| Показатель | Значение | Правило устава |
| :--- | :--- | :--- |
| **Стартовый капитал** | `$50.00 USDC` | Не добавлять деньги |
| **Текущий баланс (Equity)** | **`$35.73 USDC`** (`-14.27$` / `-28.54%`) | Cash + Mark-to-Market по CLOB Bid |
| **Свободный кэш / В сделках** | `$30.65` / `$5.09 USDC` | До 8 открытых позиций, макс 8% банка |
| **Цель окупаемости подписки** | `$-14.27 / $60.00` (`0.0%`) | Цель: +$60.00 в месяц |
| **Просадка от пика (Текущая / Макс)** | `9.06%` / `24.45%` (Пик: `$39.29`) | Стоп-кран при просадке 40% |
| **Закрытых сделок / Win Rate** | `165` / `70.3%` | Brier Score: `0.1960` |

## 📂 Открытые позиции (4 / 8)
| # | Рынок | Кат. | Исход | Вход (Ask VWAP) | Текущий Bid | Оценка бота | Размер ($) | Нереализ. PnL | Источник |
| :- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| #154 | Will Elon Musk post 220-239 tweets from November 6 to N | Geopolitics | **NO** | `0.670` | `0.722` | `68.0%` | `$2.33` | `$+0.18` | https://x.com/elonmusk |
| #155 | Will Elon Musk post 200-219 tweets from November 6 to N | Geopolitics | **NO** | `0.917` | `0.350` | `93.5%` | `$1.07` | `$-0.66` | https://x.com/elonmusk |
| #169 | Jazz vs. Rockets | Sports | **NO** | `0.920` | `0.910` | `95.0%` | `$1.12` | `$-0.01` | https://www.nba.com/ |
| #170 | Bitcoin Up or Down on November 13? | Crypto | **NO** | `0.910` | `0.900` | `95.0%` | `$1.07` | `$-0.01` | https://www.binance.com/en/tra |

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
| Bitcoin Up or Down on November 13? | Crypto | NO | `95.0%` | `91.0%` | `+4.0 п.п.` | `1.00%` | EXECUTED BUY #170 ($1.07 @ 0.9100) |
| Will the price of Bitcoin be above $70,000 on Nove | Crypto | NO | `70.4%` | `65.9%` | `+4.5 п.п.` | `2.10%` | REJECTED: CLOB round-trip slippage 2.10% > 2.0% limit |
| Will the price of Bitcoin be above $68,000 on Nove | Crypto | YES | `91.4%` | `84.2%` | `+7.2 п.п.` | `1.20%` | REJECTED: Duplicate underlying event (crypto:bitcoin:november 13) |
| Will the highest temperature in Houston be between | Weather | NO | `85.0%` | `62.0%` | `+23.1 п.п.` | `3.00%` | REJECTED: Narrow weather bracket NO bet prohibited (airport METAR microclimate tail risk) |
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
