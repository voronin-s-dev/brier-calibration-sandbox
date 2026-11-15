# 📊 Отчёт симулятора Polymarket (Устав Grok Bot — Демо-счёт)
**Обновлено:** `2026-11-15 00:38:01 UTC`

## 💰 Состояние виртуального портфеля
| Показатель | Значение | Правило устава |
| :--- | :--- | :--- |
| **Стартовый капитал** | `$50.00 USDC` | Не добавлять деньги |
| **Текущий баланс (Equity)** | **`$30.77 USDC`** (`-19.23$` / `-38.46%`) | Cash + Mark-to-Market по CLOB Bid |
| **Свободный кэш / В сделках** | `$24.63` / `$6.13 USDC` | До 8 открытых позиций, макс 8% банка |
| **Цель окупаемости подписки** | `$-19.23 / $60.00` (`0.0%`) | Цель: +$60.00 в месяц |
| **Просадка от пика (Текущая / Макс)** | `21.69%` / `24.45%` (Пик: `$39.29`) | Стоп-кран при просадке 40% |
| **Закрытых сделок / Win Rate** | `198` / `65.7%` | Brier Score: `0.1960` |

## 📂 Открытые позиции (4 / 8)
| # | Рынок | Кат. | Исход | Вход (Ask VWAP) | Текущий Bid | Оценка бота | Размер ($) | Нереализ. PnL | Источник |
| :- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| #200 | Will the price of Bitcoin be above $66,000 on November  | Crypto | **NO** | `0.662` | `0.765` | `82.6%` | `$1.58` | `$+0.25` | Kraken BTCUSDT 1m/1h Spot Klin |
| #201 | Will the price of Bitcoin be above $62,000 on November  | Crypto | **YES** | `0.738` | `0.679` | `70.8%` | `$2.50` | `$-0.20` | Kraken BTCUSDT 1m/1h Spot Klin |
| #202 | Will Bitcoin dip to $62,000 on November 14? | Crypto | **NO** | `0.883` | `0.760` | `93.6%` | `$1.00` | `$-0.14` | https://www.binance.com/en/tra |
| #203 | Will Bitcoin dip to $60,000 November 9-15? | Crypto | **NO** | `0.820` | `0.765` | `91.3%` | `$1.23` | `$-0.08` | Kraken BTCUSDT 1m/1h Spot Klin |

## 🧪 Теневая песочница (Shadow Sandbox)
| Показатель | Значение |
| :--- | :--- |
| **Виртуальный баланс (Equity)** | **`$53.82 USDC`** |
| **Свободный кэш / В сделках** | `$53.82` / `$0.00 USDC` |
| **Открытых позиций** | `0 / 5` |
| **Текущая просадка** | `5.96%` |

### Доходность по замороженным категориям (Песочница)
| Категория | Сделок | PnL | Win Rate |
| :--- | :--- | :--- | :--- |
| **Crypto** | `15` | `+$4.18` | `60%` |
| **Geopolitics** | `4` | `+$0.57` | `75%` |
| **Other** | `16` | `-$0.93` | `44%` |

## 🔍 Последние проверенные кандидаты и фильтр стакана CLOB
| Рынок | Кат. | Сторона | Оценка бота | Цена Ask | Перекос (Edge) | Проскальзывание CLOB | Решение |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Will Ethereum dip to $1,600 November 9-15? | Crypto | NO | `98.7%` | `88.4%` | `+10.3 п.п.` | `1.60%` | REJECTED: Category cap reached (4/4 in Crypto) |
| Will the price of Bitcoin be above $66,000 on Nove | Crypto | NO | `77.2%` | `71.7%` | `+5.5 п.п.` | `0.20%` | REJECTED: Duplicate underlying event (crypto:bitcoin:november 17) |
| Will Bitcoin dip to $62,000 November 9-15? | Crypto | NO | `70.5%` | `50.7%` | `+19.9 п.п.` | `3.70%` | REJECTED: Contract price $0.507 outside sweet spot [$0.60, $0.92] |
| Will the price of Ethereum be above $1,600 on Nove | Crypto | YES | `92.0%` | `86.8%` | `+5.2 п.п.` | `3.20%` | REJECTED: CLOB round-trip slippage 3.20% > 2.0% limit |
| Will the price of Ethereum be above $1,600 on Nove | Crypto | YES | `90.0%` | `84.0%` | `+6.0 п.п.` | `1.70%` | REJECTED: Category cap reached (4/4 in Crypto) |
| Will the price of Ethereum be above $1,700 on Nove | Crypto | YES | `89.9%` | `82.4%` | `+7.5 п.п.` | `1.70%` | REJECTED: Category cap reached (4/4 in Crypto) |
| Will Ethereum dip to $1,600 November 9-15? | Crypto | NO | `99.5%` | `88.2%` | `+11.3 п.п.` | `1.10%` | REJECTED: Category cap reached (4/4 in Crypto) |
| Will the price of Bitcoin be above $62,000 on Nove | Crypto | YES | `70.7%` | `79.3%` | `-8.6 п.п.` | `14.50%` | REJECTED: Edge -8.6 pp < 2 pp threshold (P_est=70.7% vs AskVWAP=79.3%) |
| Will Bitcoin dip to $62,000 November 9-15? | Crypto | NO | `72.6%` | `52.1%` | `+20.5 п.п.` | `0.10%` | REJECTED: Contract price $0.521 outside sweet spot [$0.60, $0.92] |
| Will the price of Ethereum be above $1,600 on Nove | Crypto | YES | `89.8%` | `83.4%` | `+6.3 п.п.` | `2.20%` | REJECTED: CLOB round-trip slippage 2.20% > 2.0% limit |
| Will the price of Ethereum be above $1,700 on Nove | Crypto | YES | `90.7%` | `83.8%` | `+6.9 п.п.` | `1.10%` | REJECTED: Category cap reached (4/4 in Crypto) |
| Will Ethereum dip to $1,600 November 9-15? | Crypto | NO | `99.5%` | `90.8%` | `+8.7 п.п.` | `3.00%` | REJECTED: CLOB round-trip slippage 3.00% > 2.0% limit |
| Will Bitcoin dip to $63,000 on November 14? | Crypto | NO | `85.1%` | `59.7%` | `+25.4 п.п.` | `6.40%` | REJECTED: Contract price $0.597 outside sweet spot [$0.60, $0.92] |
| Will the price of Ethereum be above $1,600 on Nove | Crypto | YES | `90.7%` | `85.9%` | `+4.8 п.п.` | `0.10%` | REJECTED: Category cap reached (4/4 in Crypto) |
| Will Bitcoin reach $68,000 November 9-15? | Crypto | NO | `92.7%` | `87.0%` | `+5.7 п.п.` | `1.00%` | REJECTED: Duplicate underlying event (crypto:bitcoin:november 9 - november 15) |
| Will the price of Bitcoin be above $68,000 on Nove | Crypto | NO | `92.6%` | `87.8%` | `+4.8 п.п.` | `0.30%` | REJECTED: Duplicate underlying event (crypto:bitcoin:november 16) |
| Will the price of Bitcoin be above $66,000 on Nove | Crypto | NO | `86.0%` | `81.4%` | `+4.6 п.п.` | `0.10%` | REJECTED: Category cap reached (4/4 in Crypto) |
| Will the price of Bitcoin be above $66,000 on Nove | Crypto | NO | `71.0%` | `66.3%` | `+4.7 п.п.` | `0.10%` | REJECTED: Duplicate underlying event (crypto:bitcoin:november 17) |
