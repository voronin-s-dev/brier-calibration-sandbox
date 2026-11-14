# 📊 Отчёт симулятора Polymarket (Устав Grok Bot — Демо-счёт)
**Обновлено:** `2026-11-14 04:49:05 UTC`

## 💰 Состояние виртуального портфеля
| Показатель | Значение | Правило устава |
| :--- | :--- | :--- |
| **Стартовый капитал** | `$50.00 USDC` | Не добавлять деньги |
| **Текущий баланс (Equity)** | **`$34.20 USDC`** (`-15.80$` / `-31.60%`) | Cash + Mark-to-Market по CLOB Bid |
| **Свободный кэш / В сделках** | `$29.82` / `$4.38 USDC` | До 8 открытых позиций, макс 8% банка |
| **Цель окупаемости подписки** | `$-15.80 / $60.00` (`0.0%`) | Цель: +$60.00 в месяц |
| **Просадка от пика (Текущая / Макс)** | `12.96%` / `24.45%` (Пик: `$39.29`) | Стоп-кран при просадке 40% |
| **Закрытых сделок / Win Rate** | `184` / `69.0%` | Brier Score: `0.1960` |

## 📂 Открытые позиции (3 / 8)
| # | Рынок | Кат. | Исход | Вход (Ask VWAP) | Текущий Bid | Оценка бота | Размер ($) | Нереализ. PnL | Источник |
| :- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| #181 | Will Elon Musk post 90-114 tweets from November 12 to N | Geopolitics | **NO** | `0.918` | `0.966` | `98.5%` | `$1.08` | `$+0.06` | https://x.com/elonmusk |
| #187 | Will Bitcoin dip to $66,000 November 9-15? | Crypto | **YES** | `0.731` | `0.547` | `70.6%` | `$2.19` | `$-0.55` | Kraken BTCUSDT 1m/1h Spot Klin |
| #188 | Will the price of Bitcoin be above $68,000 on November  | Crypto | **NO** | `0.787` | `0.786` | `81.2%` | `$1.61` | `$-0.00` | Kraken BTCUSDT 1m/1h Spot Klin |

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
| Will the price of Bitcoin be above $68,000 on Nove | Crypto | NO | `81.2%` | `78.7%` | `+2.5 п.п.` | `0.10%` | EXECUTED BUY #188 ($1.61 @ 0.7870) |
| Will the price of Bitcoin be between $68,000 and $ | Crypto | NO | `93.7%` | `86.4%` | `+7.2 п.п.` | `3.00%` | REJECTED: CLOB round-trip slippage 3.00% > 2.0% limit |
| Will Bitcoin dip to $66,000 November 9-15? | Crypto | YES | `77.4%` | `73.2%` | `+4.2 п.п.` | `0.90%` | EXECUTED BUY #187 ($2.19 @ 0.7310) |
| Will Bitcoin reach $70,000 November 9-15? | Crypto | YES | `99.5%` | `15.0%` | `+84.5 п.п.` | `1.00%` | REJECTED: Contract price $0.150 outside sweet spot [$0.60, $0.92] |
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
