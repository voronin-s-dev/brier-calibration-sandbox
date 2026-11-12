# 📊 Отчёт симулятора Polymarket (Устав Grok Bot — Демо-счёт)
**Обновлено:** `2026-11-12 10:52:00 UTC`

## 💰 Состояние виртуального портфеля
| Показатель | Значение | Правило устава |
| :--- | :--- | :--- |
| **Стартовый капитал** | `$50.00 USDC` | Не добавлять деньги |
| **Текущий баланс (Equity)** | **`$36.27 USDC`** (`-13.73$` / `-27.47%`) | Cash + Mark-to-Market по CLOB Bid |
| **Свободный кэш / В сделках** | `$21.94` / `$14.33 USDC` | До 8 открытых позиций, макс 8% банка |
| **Цель окупаемости подписки** | `$-13.73 / $60.00` (`0.0%`) | Цель: +$60.00 в месяц |
| **Просадка от пика (Текущая / Макс)** | `7.70%` / `24.45%` (Пик: `$39.29`) | Стоп-кран при просадке 40% |
| **Закрытых сделок / Win Rate** | `148` / `73.0%` | Brier Score: `0.1960` |

## 📂 Открытые позиции (8 / 8)
| # | Рынок | Кат. | Исход | Вход (Ask VWAP) | Текущий Bid | Оценка бота | Размер ($) | Нереализ. PnL | Источник |
| :- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| #141 | Will Elon Musk post 280-299 tweets from November 6 to N | Geopolitics | **NO** | `0.850` | `0.966` | `98.5%` | `$3.07` | `$+0.42` | https://x.com/elonmusk |
| #147 | Will the price of Bitcoin be above $76,000 on November  | Crypto | **NO** | `0.910` | `0.969` | `98.5%` | `$1.11` | `$+0.07` | https://www.binance.com/en/tra |
| #152 | Will the price of Ethereum be above $2,000 on November  | Crypto | **YES** | `0.911` | `0.909` | `95.3%` | `$1.10` | `$-0.00` | https://www.binance.com/en/tra |
| #153 | Will Ethereum dip to $2,000 November 9-15? | Crypto | **YES** | `0.660` | `0.590` | `68.5%` | `$1.95` | `$-0.21` | Kraken ETHUSDT 1m/1h Spot Klin |
| #154 | Will Elon Musk post 220-239 tweets from November 6 to N | Geopolitics | **NO** | `0.670` | `0.593` | `68.0%` | `$2.33` | `$-0.27` | https://x.com/elonmusk |
| #155 | Will Elon Musk post 200-219 tweets from November 6 to N | Geopolitics | **NO** | `0.917` | `0.887` | `93.5%` | `$1.07` | `$-0.04` | https://x.com/elonmusk |
| #156 | Will Vitality Win the BLAST Rivals Hong Kong 2026? | Other | **NO** | `0.740` | `0.670` | `80.0%` | `$2.91` | `$-0.28` | https://www.hltv.org/events/82 |
| #157 | Will Croatia win on 2026-11-12? | Sports | **NO** | `0.920` | `0.910` | `95.0%` | `$1.10` | `$-0.01` | https://www.uefa.com/uefanatio |

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
| #5 | Total Kills Over/Under 27.5 in Game 2? | Other | **NO** | `0.500` | `0.490` | `56.7%` | `$1.42` | `$-0.03` | https://gol.gg/esports/home |
| #20 | Total Kills Over/Under 27.5 in Game 4? | Other | **NO** | `0.500` | `0.490` | `55.9%` | `$1.58` | `$-0.03` | https://gol.gg/esports/home |
| #31 | Total Kills Over/Under 27.5 in Game 3? | Other | **YES** | `0.510` | `0.490` | `54.7%` | `$1.15` | `$-0.05` | https://gol.gg/esports/home |

### Доходность по замороженным категориям (Песочница)
| Категория | Сделок | PnL | Win Rate |
| :--- | :--- | :--- | :--- |
| **Crypto** | `15` | `+$4.18` | `60%` |
| **Geopolitics** | `4` | `+$0.57` | `75%` |
| **Other** | `13` | `+$0.81` | `54%` |

## 🔍 Последние проверенные кандидаты и фильтр стакана CLOB
| Рынок | Кат. | Сторона | Оценка бота | Цена Ask | Перекос (Edge) | Проскальзывание CLOB | Решение |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Will Bitcoin reach $74,000 on November 12? | Crypto | YES | `72.4%` | `65.0%` | `+7.4 п.п.` | `1.00%` | REJECTED: Duplicate underlying event (crypto:bitcoin:november 12) |
| Will Bitcoin reach $74,000 on November 12? | Crypto | YES | `73.5%` | `68.0%` | `+5.5 п.п.` | `1.00%` | REJECTED: Duplicate underlying event (crypto:bitcoin:november 12) |
| Will Bitcoin reach $74,000 on November 12? | Crypto | YES | `74.0%` | `67.0%` | `+7.0 п.п.` | `1.00%` | REJECTED: Duplicate underlying event (crypto:bitcoin:november 12) |
| Will Bitcoin reach $74,000 on November 12? | Crypto | YES | `70.3%` | `66.0%` | `+4.3 п.п.` | `1.00%` | REJECTED: Duplicate underlying event (crypto:bitcoin:november 12) |
| Will the highest temperature in Austin be between  | Weather | NO | `74.6%` | `70.0%` | `+4.6 п.п.` | `5.00%` | REJECTED: Narrow weather bracket NO bet prohibited (airport METAR microclimate tail risk) |
| Will Bitcoin reach $74,000 on November 12? | Crypto | YES | `71.4%` | `61.0%` | `+10.4 п.п.` | `1.00%` | REJECTED: Duplicate underlying event (crypto:bitcoin:november 12) |
| Will Bitcoin reach $74,000 on November 12? | Crypto | YES | `71.5%` | `66.0%` | `+5.5 п.п.` | `1.00%` | REJECTED: Duplicate underlying event (crypto:bitcoin:november 12) |
| Will the highest temperature in Austin be between  | Weather | NO | `72.9%` | `68.0%` | `+4.9 п.п.` | `3.00%` | REJECTED: Narrow weather bracket NO bet prohibited (airport METAR microclimate tail risk) |
| Will Bitcoin reach $74,000 on November 12? | Crypto | YES | `70.2%` | `63.0%` | `+7.2 п.п.` | `1.00%` | REJECTED: Duplicate underlying event (crypto:bitcoin:november 12) |
| Will Bitcoin reach $74,000 on November 12? | Crypto | YES | `70.5%` | `65.0%` | `+5.5 п.п.` | `1.00%` | REJECTED: Duplicate underlying event (crypto:bitcoin:november 12) |
| Will Bitcoin reach $74,000 on November 12? | Crypto | YES | `71.1%` | `65.0%` | `+6.1 п.п.` | `1.00%` | REJECTED: Duplicate underlying event (crypto:bitcoin:november 12) |
| Will Bitcoin reach $74,000 on November 12? | Crypto | YES | `71.5%` | `57.0%` | `+14.5 п.п.` | `1.00%` | REJECTED: Contract price $0.570 outside sweet spot [$0.60, $0.92] |
| Will Bitcoin reach $74,000 on November 12? | Crypto | YES | `72.3%` | `64.0%` | `+8.3 п.п.` | `1.00%` | REJECTED: Duplicate underlying event (crypto:bitcoin:november 12) |
| Will Bitcoin reach $74,000 on November 12? | Crypto | YES | `75.1%` | `69.0%` | `+6.1 п.п.` | `1.00%` | REJECTED: Duplicate underlying event (crypto:bitcoin:november 12) |
| Will Bitcoin reach $74,000 on November 12? | Crypto | YES | `74.5%` | `68.0%` | `+6.5 п.п.` | `1.00%` | REJECTED: Duplicate underlying event (crypto:bitcoin:november 12) |
| Will Croatia win on 2026-11-12? | Sports | NO | `95.0%` | `92.0%` | `+3.0 п.п.` | `1.00%` | EXECUTED BUY #157 ($1.10 @ 0.9200) |
| Will Vitality Win the BLAST Rivals Hong Kong 2026? | Other | NO | `79.7%` | `74.0%` | `+5.7 п.п.` | `2.00%` | EXECUTED BUY #156 ($2.91 @ 0.7400) |
| Will Bitcoin reach $74,000 on November 12? | Crypto | YES | `78.2%` | `72.0%` | `+6.2 п.п.` | `2.00%` | REJECTED: Duplicate underlying event (crypto:bitcoin:november 12) |
