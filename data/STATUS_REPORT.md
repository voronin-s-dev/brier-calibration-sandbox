# 📊 Отчёт симулятора Polymarket (Устав Grok Bot — Демо-счёт)
**Обновлено:** `2026-11-12 13:19:27 UTC`

## 💰 Состояние виртуального портфеля
| Показатель | Значение | Правило устава |
| :--- | :--- | :--- |
| **Стартовый капитал** | `$50.00 USDC` | Не добавлять деньги |
| **Текущий баланс (Equity)** | **`$37.94 USDC`** (`-12.06$` / `-24.12%`) | Cash + Mark-to-Market по CLOB Bid |
| **Свободный кэш / В сделках** | `$28.85` / `$9.10 USDC` | До 8 открытых позиций, макс 8% банка |
| **Цель окупаемости подписки** | `$-12.06 / $60.00` (`0.0%`) | Цель: +$60.00 в месяц |
| **Просадка от пика (Текущая / Макс)** | `3.44%` / `24.45%` (Пик: `$39.29`) | Стоп-кран при просадке 40% |
| **Закрытых сделок / Win Rate** | `153` / `72.5%` | Brier Score: `0.1960` |

## 📂 Открытые позиции (5 / 8)
| # | Рынок | Кат. | Исход | Вход (Ask VWAP) | Текущий Bid | Оценка бота | Размер ($) | Нереализ. PnL | Источник |
| :- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| #141 | Will Elon Musk post 280-299 tweets from November 6 to N | Geopolitics | **NO** | `0.850` | `0.970` | `98.5%` | `$3.07` | `$+0.43` | https://x.com/elonmusk |
| #154 | Will Elon Musk post 220-239 tweets from November 6 to N | Geopolitics | **NO** | `0.670` | `0.565` | `68.0%` | `$2.33` | `$-0.37` | https://x.com/elonmusk |
| #155 | Will Elon Musk post 200-219 tweets from November 6 to N | Geopolitics | **NO** | `0.917` | `0.877` | `93.5%` | `$1.07` | `$-0.05` | https://x.com/elonmusk |
| #157 | Will Croatia win on 2026-11-12? | Sports | **NO** | `0.920` | `0.900` | `94.0%` | `$1.10` | `$-0.02` | https://www.uefa.com/uefanatio |
| #159 | Will the price of Bitcoin be above $74,000 on November  | Crypto | **NO** | `0.860` | `0.900` | `94.0%` | `$1.46` | `$+0.07` | Kraken BTCUSDT 1m/1h Spot Klin |

## 🧪 Теневая песочница (Shadow Sandbox)
| Показатель | Значение |
| :--- | :--- |
| **Виртуальный баланс (Equity)** | **`$55.46 USDC`** |
| **Свободный кэш / В сделках** | `$51.42` / `$4.04 USDC` |
| **Открытых позиций** | `3 / 5` |
| **Текущая просадка** | `3.10%` |

### Открытые позиции в песочнице (3 / 5)
| # | Рынок | Кат. | Исход | Вход (Ask VWAP) | Текущий Bid | Оценка бота | Размер ($) | Нереализ. PnL | Источник |
| :- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| #5 | Total Kills Over/Under 27.5 in Game 2? | Other | **NO** | `0.500` | `0.490` | `56.5%` | `$1.42` | `$-0.03` | https://gol.gg/esports/home |
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
| Will the price of Bitcoin be between $72,000 and $ | Crypto | YES | `73.6%` | `64.0%` | `+9.6 п.п.` | `2.00%` | REJECTED: Duplicate underlying event (crypto:bitcoin:november 12) |
| Will the price of Bitcoin be above $72,000 on Nove | Crypto | YES | `79.5%` | `71.3%` | `+8.2 п.п.` | `0.60%` | REJECTED: Duplicate underlying event (crypto:bitcoin:november 12) |
| Will the price of Ethereum be between $2,000 and $ | Crypto | YES | `73.0%` | `43.0%` | `+30.0 п.п.` | `5.00%` | REJECTED: Contract price $0.430 outside sweet spot [$0.60, $0.92] |
| Will Ethereum dip to $1,950 on November 12? | Crypto | NO | `78.4%` | `52.0%` | `+26.4 п.п.` | `4.00%` | REJECTED: Contract price $0.520 outside sweet spot [$0.60, $0.92] |
| Will the price of Bitcoin be between $72,000 and $ | Crypto | YES | `76.3%` | `59.0%` | `+17.3 п.п.` | `1.00%` | REJECTED: Contract price $0.590 outside sweet spot [$0.60, $0.92] |
| Will Bitcoin dip to $72,000 November 9-15? | Crypto | YES | `81.0%` | `91.0%` | `-10.0 п.п.` | `2.00%` | REJECTED: Edge -10.0 pp < 2 pp threshold (P_est=81.0% vs AskVWAP=91.0%) |
| Will the price of Ethereum be above $2,000 on Nove | Crypto | YES | `72.0%` | `46.7%` | `+25.4 п.п.` | `2.80%` | REJECTED: Contract price $0.467 outside sweet spot [$0.60, $0.92] |
| Will the price of Bitcoin be above $74,000 on Nove | Crypto | NO | `89.8%` | `86.0%` | `+3.8 п.п.` | `1.00%` | EXECUTED BUY #159 ($1.46 @ 0.8600) |
| Will Zoran Janković win the 2026 Ljubljana mayoral | Geopolitics | YES | `76.5%` | `70.0%` | `+6.5 п.п.` | `2.00%` | REJECTED: Category cap reached (3/3 in Geopolitics) |
| Will Zoran Janković win the 2026 Ljubljana mayoral | Geopolitics | YES | `75.2%` | `70.0%` | `+5.2 п.п.` | `3.00%` | REJECTED: CLOB round-trip slippage 3.00% > 2.0% limit |
| Will Bitcoin dip to $72,000 November 9-15? | Crypto | YES | `74.6%` | `65.0%` | `+9.6 п.п.` | `1.00%` | EXECUTED BUY #158 ($2.92 @ 0.6500) |
| Will Zoran Janković win the 2026 Ljubljana mayoral | Geopolitics | YES | `75.3%` | `70.0%` | `+5.3 п.п.` | `3.00%` | REJECTED: CLOB round-trip slippage 3.00% > 2.0% limit |
| Will Zoran Janković win the 2026 Ljubljana mayoral | Geopolitics | YES | `75.3%` | `70.0%` | `+5.3 п.п.` | `3.00%` | REJECTED: CLOB round-trip slippage 3.00% > 2.0% limit |
| Will Zoran Janković win the 2026 Ljubljana mayoral | Geopolitics | YES | `76.0%` | `71.0%` | `+5.0 п.п.` | `4.00%` | REJECTED: CLOB round-trip slippage 4.00% > 2.0% limit |
| Will Zoran Janković win the 2026 Ljubljana mayoral | Geopolitics | YES | `75.6%` | `70.0%` | `+5.6 п.п.` | `3.00%` | REJECTED: CLOB round-trip slippage 3.00% > 2.0% limit |
| Will Zoran Janković win the 2026 Ljubljana mayoral | Geopolitics | YES | `75.7%` | `70.0%` | `+5.7 п.п.` | `3.00%` | REJECTED: CLOB round-trip slippage 3.00% > 2.0% limit |
| Will Bitcoin reach $74,000 on November 12? | Crypto | YES | `70.7%` | `66.0%` | `+4.7 п.п.` | `1.00%` | REJECTED: Duplicate underlying event (crypto:bitcoin:november 12) |
| Will Bitcoin reach $74,000 on November 12? | Crypto | YES | `70.7%` | `66.0%` | `+4.7 п.п.` | `2.00%` | REJECTED: Duplicate underlying event (crypto:bitcoin:november 12) |
