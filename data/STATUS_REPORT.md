# 📊 Отчёт симулятора Polymarket (Устав Grok Bot — Демо-счёт)
**Обновлено:** `2026-11-14 23:31:06 UTC`

## 💰 Состояние виртуального портфеля
| Показатель | Значение | Правило устава |
| :--- | :--- | :--- |
| **Стартовый капитал** | `$50.00 USDC` | Не добавлять деньги |
| **Текущий баланс (Equity)** | **`$30.80 USDC`** (`-19.20$` / `-38.40%`) | Cash + Mark-to-Market по CLOB Bid |
| **Свободный кэш / В сделках** | `$24.63` / `$6.17 USDC` | До 8 открытых позиций, макс 8% банка |
| **Цель окупаемости подписки** | `$-19.20 / $60.00` (`0.0%`) | Цель: +$60.00 в месяц |
| **Просадка от пика (Текущая / Макс)** | `21.61%` / `24.45%` (Пик: `$39.29`) | Стоп-кран при просадке 40% |
| **Закрытых сделок / Win Rate** | `198` / `65.7%` | Brier Score: `0.1960` |

## 📂 Открытые позиции (4 / 8)
| # | Рынок | Кат. | Исход | Вход (Ask VWAP) | Текущий Bid | Оценка бота | Размер ($) | Нереализ. PnL | Источник |
| :- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| #200 | Will the price of Bitcoin be above $66,000 on November  | Crypto | **NO** | `0.662` | `0.785` | `83.4%` | `$1.58` | `$+0.29` | Kraken BTCUSDT 1m/1h Spot Klin |
| #201 | Will the price of Bitcoin be above $62,000 on November  | Crypto | **YES** | `0.738` | `0.680` | `70.5%` | `$2.50` | `$-0.20` | Kraken BTCUSDT 1m/1h Spot Klin |
| #202 | Will Bitcoin dip to $62,000 on November 14? | Crypto | **NO** | `0.883` | `0.752` | `90.0%` | `$1.00` | `$-0.15` | https://www.binance.com/en/tra |
| #203 | Will Bitcoin dip to $60,000 November 9-15? | Crypto | **NO** | `0.820` | `0.759` | `89.6%` | `$1.23` | `$-0.09` | Kraken BTCUSDT 1m/1h Spot Klin |

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
| Will the price of Ethereum be above $1,600 on Nove | Crypto | YES | `86.6%` | `82.5%` | `+4.1 п.п.` | `0.10%` | REJECTED: Category cap reached (4/4 in Crypto) |
| Will Ethereum dip to $1,600 November 9-15? | Crypto | NO | `98.2%` | `88.5%` | `+9.7 п.п.` | `3.40%` | REJECTED: CLOB round-trip slippage 3.40% > 2.0% limit |
| Will the price of Bitcoin be above $66,000 on Nove | Crypto | NO | `77.9%` | `72.7%` | `+5.2 п.п.` | `0.20%` | REJECTED: Duplicate underlying event (crypto:bitcoin:november 17) |
| Will the price of Ethereum be above $1,600 on Nove | Crypto | YES | `87.1%` | `82.9%` | `+4.2 п.п.` | `1.50%` | REJECTED: Category cap reached (4/4 in Crypto) |
| Will Ethereum dip to $1,600 November 9-15? | Crypto | NO | `98.5%` | `86.2%` | `+12.3 п.п.` | `2.80%` | REJECTED: CLOB round-trip slippage 2.80% > 2.0% limit |
| Will the price of Bitcoin be above $68,000 on Nove | Crypto | NO | `95.2%` | `91.2%` | `+4.0 п.п.` | `0.10%` | REJECTED: Duplicate underlying event (crypto:bitcoin:november 16) |
| Will Bitcoin dip to $61,000 on November 14? | Crypto | NO | `99.5%` | `90.7%` | `+8.8 п.п.` | `2.70%` | REJECTED: CLOB round-trip slippage 2.70% > 2.0% limit |
| Will the price of Bitcoin be above $66,000 on Nove | Crypto | NO | `77.6%` | `72.1%` | `+5.5 п.п.` | `0.10%` | REJECTED: Duplicate underlying event (crypto:bitcoin:november 17) |
| Will Ethereum dip to $1,600 November 9-15? | Crypto | NO | `98.5%` | `85.4%` | `+13.1 п.п.` | `4.00%` | REJECTED: CLOB round-trip slippage 4.00% > 2.0% limit |
| Will Bitcoin dip to $61,000 on November 14? | Crypto | NO | `99.5%` | `87.3%` | `+12.2 п.п.` | `0.50%` | REJECTED: Duplicate underlying event (crypto:bitcoin:november 14) |
| Will the price of Bitcoin be above $66,000 on Nove | Crypto | NO | `78.1%` | `73.9%` | `+4.2 п.п.` | `0.10%` | REJECTED: Duplicate underlying event (crypto:bitcoin:november 17) |
| Will the price of Ethereum be above $1,700 on Nove | Crypto | YES | `82.1%` | `75.9%` | `+6.2 п.п.` | `1.10%` | REJECTED: Category cap reached (4/4 in Crypto) |
| Will Ethereum dip to $1,600 November 9-15? | Crypto | NO | `98.5%` | `89.2%` | `+9.3 п.п.` | `5.50%` | REJECTED: CLOB round-trip slippage 5.50% > 2.0% limit |
| Will Bitcoin dip to $61,000 on November 14? | Crypto | NO | `99.5%` | `89.5%` | `+10.0 п.п.` | `2.90%` | REJECTED: CLOB round-trip slippage 2.90% > 2.0% limit |
| Will the price of Bitcoin be above $66,000 on Nove | Crypto | NO | `77.8%` | `72.7%` | `+5.1 п.п.` | `0.10%` | REJECTED: Duplicate underlying event (crypto:bitcoin:november 17) |
| Will Ethereum dip to $1,600 November 9-15? | Crypto | NO | `99.1%` | `90.6%` | `+8.5 п.п.` | `3.70%` | REJECTED: CLOB round-trip slippage 3.70% > 2.0% limit |
| Will Ethereum dip to $1,600 November 9-15? | Crypto | NO | `99.1%` | `87.0%` | `+12.1 п.п.` | `0.10%` | REJECTED: Category cap reached (4/4 in Crypto) |
| Will Bitcoin dip to $61,000 on November 14? | Crypto | NO | `99.5%` | `90.2%` | `+9.3 п.п.` | `8.20%` | REJECTED: CLOB round-trip slippage 8.20% > 2.0% limit |
