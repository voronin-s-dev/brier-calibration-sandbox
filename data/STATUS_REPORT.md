# 📊 Отчёт симулятора Polymarket (Устав Grok Bot — Демо-счёт)
**Обновлено:** `2026-11-12 05:01:12 UTC`

## 💰 Состояние виртуального портфеля
| Показатель | Значение | Правило устава |
| :--- | :--- | :--- |
| **Стартовый капитал** | `$50.00 USDC` | Не добавлять деньги |
| **Текущий баланс (Equity)** | **`$36.45 USDC`** (`-13.55$` / `-27.09%`) | Cash + Mark-to-Market по CLOB Bid |
| **Свободный кэш / В сделках** | `$27.91` / `$8.55 USDC` | До 8 открытых позиций, макс 8% банка |
| **Цель окупаемости подписки** | `$-13.55 / $60.00` (`0.0%`) | Цель: +$60.00 в месяц |
| **Просадка от пика (Текущая / Макс)** | `7.22%` / `24.45%` (Пик: `$39.29`) | Стоп-кран при просадке 40% |
| **Закрытых сделок / Win Rate** | `147` / `72.8%` | Brier Score: `0.1960` |

## 📂 Открытые позиции (4 / 8)
| # | Рынок | Кат. | Исход | Вход (Ask VWAP) | Текущий Bid | Оценка бота | Размер ($) | Нереализ. PnL | Источник |
| :- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| #141 | Will Elon Musk post 280-299 tweets from November 6 to N | Geopolitics | **NO** | `0.850` | `0.951` | `98.5%` | `$3.07` | `$+0.36` | https://x.com/elonmusk |
| #144 | Will Predict.fun launch a token by November 15, 2026? | Other | **NO** | `0.848` | `0.846` | `90.7%` | `$2.90` | `$-0.01` | information from predict.fun ( |
| #147 | Will the price of Bitcoin be above $76,000 on November  | Crypto | **NO** | `0.910` | `0.955` | `98.5%` | `$1.11` | `$+0.05` | https://www.binance.com/en/tra |
| #152 | Will the price of Ethereum be above $2,000 on November  | Crypto | **YES** | `0.911` | `0.872` | `84.6%` | `$1.10` | `$-0.05` | https://www.binance.com/en/tra |

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
| #5 | Total Kills Over/Under 27.5 in Game 2? | Other | **NO** | `0.500` | `0.490` | `54.7%` | `$1.42` | `$-0.03` | https://gol.gg/esports/home |
| #20 | Total Kills Over/Under 27.5 in Game 4? | Other | **NO** | `0.500` | `0.490` | `55.5%` | `$1.58` | `$-0.03` | https://gol.gg/esports/home |
| #31 | Total Kills Over/Under 27.5 in Game 3? | Other | **YES** | `0.510` | `0.490` | `55.1%` | `$1.15` | `$-0.05` | https://gol.gg/esports/home |

### Доходность по замороженным категориям (Песочница)
| Категория | Сделок | PnL | Win Rate |
| :--- | :--- | :--- | :--- |
| **Crypto** | `15` | `+$4.18` | `60%` |
| **Geopolitics** | `4` | `+$0.57` | `75%` |
| **Other** | `13` | `+$0.81` | `54%` |

## 🔍 Последние проверенные кандидаты и фильтр стакана CLOB
| Рынок | Кат. | Сторона | Оценка бота | Цена Ask | Перекос (Edge) | Проскальзывание CLOB | Решение |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Will the price of Ethereum be above $2,000 on Nove | Crypto | YES | `93.9%` | `91.1%` | `+2.8 п.п.` | `0.60%` | EXECUTED BUY #152 ($1.10 @ 0.9110) |
| Will Bitcoin dip to $73,000 on November 11? | Crypto | NO | `93.6%` | `88.0%` | `+5.6 п.п.` | `1.90%` | REJECTED: Duplicate underlying event (crypto:bitcoin:november 11) |
| Spurs vs. Bulls | Sports | YES | `94.0%` | `91.0%` | `+3.0 п.п.` | `1.00%` | EXECUTED BUY #151 ($1.11 @ 0.9100) |
| Spurs vs. Bulls | Sports | YES | `94.0%` | `91.0%` | `+3.0 п.п.` | `1.00%` | EXECUTED BUY #150 ($1.11 @ 0.9100) |
| Will Ethereum dip to $2,000 November 9-15? | Crypto | YES | `70.2%` | `62.0%` | `+8.2 п.п.` | `2.00%` | EXECUTED BUY #149 ($2.98 @ 0.6200) |
| Will Bitcoin reach $75,000 on November 11? | Crypto | NO | `95.0%` | `91.0%` | `+4.0 п.п.` | `2.00%` | EXECUTED BUY #148 ($1.11 @ 0.9100) |
| Will the price of Bitcoin be above $76,000 on Nove | Crypto | NO | `94.0%` | `91.0%` | `+3.0 п.п.` | `1.00%` | EXECUTED BUY #147 ($1.11 @ 0.9100) |
| Will Bitcoin reach $75,000 on November 11? | Crypto | YES | `70.0%` | `37.0%` | `+33.1 п.п.` | `3.00%` | REJECTED: Contract price $0.370 outside sweet spot [$0.60, $0.92] |
| Will Bitcoin reach $76,000 on November 11? | Crypto | NO | `93.6%` | `91.9%` | `+1.7 п.п.` | `0.70%` | EXECUTED BUY #146 ($1.08 @ 0.9190) |
| Will Juventus FC win on 2026-11-11? | Sports | NO | `97.5%` | `93.4%` | `+4.0 п.п.` | `0.10%` | REJECTED: Contract price $0.934 outside sweet spot [$0.76, $0.92] |
| Will Juventus FC win on 2026-11-11? | Sports | NO | `97.5%` | `93.4%` | `+4.0 п.п.` | `0.10%` | REJECTED: Contract price $0.934 outside sweet spot [$0.76, $0.92] |
| Will the price of Bitcoin be above $74,000 on Nove | Crypto | NO | `81.1%` | `31.8%` | `+49.3 п.п.` | `3.00%` | REJECTED: Contract price $0.318 outside sweet spot [$0.76, $0.92] |
| Will the price of Bitcoin be between $72,000 and $ | Crypto | YES | `84.1%` | `79.1%` | `+5.0 п.п.` | `2.80%` | REJECTED: CLOB round-trip slippage 2.80% > 2.0% limit |
| Bitcoin Up or Down on November 11? | Crypto | YES | `94.0%` | `88.0%` | `+6.0 п.п.` | `1.00%` | EXECUTED BUY #145 ($2.90 @ 0.8800) |
| Will Predict.fun launch a token by November 15, 20 | Other | NO | `90.9%` | `84.8%` | `+6.1 п.п.` | `1.30%` | EXECUTED BUY #144 ($2.90 @ 0.8480) |
| Dota 2: HULIGANI vs PuckChamp (BO3) - DreamLeague  | Sports | YES | `94.3%` | `90.9%` | `+3.4 п.п.` | `1.90%` | EXECUTED BUY #143 ($1.45 @ 0.9090) |
| Counter-Strike: MOUZ vs G2 (BO3) - BLAST Rivals Gr | Sports | YES | `95.7%` | `88.4%` | `+7.2 п.п.` | `0.10%` | EXECUTED BUY #142 ($3.13 @ 0.8840) |
| Counter-Strike: MOUZ vs G2 (BO3) - BLAST Rivals Gr | Sports | YES | `94.0%` | `98.0%` | `-4.0 п.п.` | `1.00%` | REJECTED: Edge -4.0 pp < 2 pp threshold (P_est=94.0% vs AskVWAP=98.0%) |
