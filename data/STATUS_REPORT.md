# 📊 Отчёт симулятора Polymarket (Устав Grok Bot — Демо-счёт)
**Обновлено:** `2026-11-15 00:19:22 UTC`

## 💰 Состояние виртуального портфеля
| Показатель | Значение | Правило устава |
| :--- | :--- | :--- |
| **Стартовый капитал** | `$50.00 USDC` | Не добавлять деньги |
| **Текущий баланс (Equity)** | **`$31.03 USDC`** (`-18.97$` / `-37.94%`) | Cash + Mark-to-Market по CLOB Bid |
| **Свободный кэш / В сделках** | `$24.63` / `$6.40 USDC` | До 8 открытых позиций, макс 8% банка |
| **Цель окупаемости подписки** | `$-18.97 / $60.00` (`0.0%`) | Цель: +$60.00 в месяц |
| **Просадка от пика (Текущая / Макс)** | `21.03%` / `24.45%` (Пик: `$39.29`) | Стоп-кран при просадке 40% |
| **Закрытых сделок / Win Rate** | `198` / `65.7%` | Brier Score: `0.1960` |

## 📂 Открытые позиции (4 / 8)
| # | Рынок | Кат. | Исход | Вход (Ask VWAP) | Текущий Bid | Оценка бота | Размер ($) | Нереализ. PnL | Источник |
| :- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| #200 | Will the price of Bitcoin be above $66,000 on November  | Crypto | **NO** | `0.662` | `0.699` | `77.7%` | `$1.58` | `$+0.09` | Kraken BTCUSDT 1m/1h Spot Klin |
| #201 | Will the price of Bitcoin be above $62,000 on November  | Crypto | **YES** | `0.738` | `0.743` | `76.0%` | `$2.50` | `$+0.02` | Kraken BTCUSDT 1m/1h Spot Klin |
| #202 | Will Bitcoin dip to $62,000 on November 14? | Crypto | **NO** | `0.883` | `0.856` | `99.4%` | `$1.00` | `$-0.03` | https://www.binance.com/en/tra |
| #203 | Will Bitcoin dip to $60,000 November 9-15? | Crypto | **NO** | `0.820` | `0.827` | `93.6%` | `$1.23` | `$+0.01` | Kraken BTCUSDT 1m/1h Spot Klin |

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
| Will the price of Bitcoin be between $66,000 and $ | Crypto | NO | `89.2%` | `84.6%` | `+4.6 п.п.` | `0.20%` | REJECTED: Category cap reached (4/4 in Crypto) |
| Will the price of Ethereum be above $1,600 on Nove | Crypto | YES | `90.4%` | `86.0%` | `+4.4 п.п.` | `0.20%` | REJECTED: Category cap reached (4/4 in Crypto) |
| Will Bitcoin reach $68,000 November 9-15? | Crypto | NO | `93.8%` | `87.0%` | `+6.8 п.п.` | `2.00%` | REJECTED: Duplicate underlying event (crypto:bitcoin:november 9 - november 15) |
| Will the price of Bitcoin be above $68,000 on Nove | Crypto | NO | `93.4%` | `87.7%` | `+5.7 п.п.` | `0.20%` | REJECTED: Duplicate underlying event (crypto:bitcoin:november 16) |
| Will the price of Bitcoin be above $66,000 on Nove | Crypto | NO | `88.2%` | `81.3%` | `+6.9 п.п.` | `0.10%` | REJECTED: Category cap reached (4/4 in Crypto) |
| Will the price of Bitcoin be above $66,000 on Nove | Crypto | NO | `73.0%` | `66.3%` | `+6.7 п.п.` | `0.10%` | REJECTED: Duplicate underlying event (crypto:bitcoin:november 17) |
| Will Bitcoin dip to $63,000 on November 14? | Crypto | NO | `80.8%` | `73.8%` | `+7.0 п.п.` | `1.00%` | REJECTED: Duplicate underlying event (crypto:bitcoin:november 14) |
| Will Bitcoin dip to $63,000 on November 14? | Crypto | NO | `76.6%` | `65.8%` | `+10.8 п.п.` | `9.50%` | REJECTED: CLOB round-trip slippage 9.50% > 2.0% limit |
| Will the price of Ethereum be above $1,600 on Nove | Crypto | YES | `89.7%` | `85.3%` | `+4.4 п.п.` | `0.10%` | REJECTED: Category cap reached (4/4 in Crypto) |
| Will Ethereum dip to $1,600 November 9-15? | Crypto | NO | `99.4%` | `92.0%` | `+7.4 п.п.` | `2.70%` | REJECTED: CLOB round-trip slippage 2.70% > 2.0% limit |
| Will the price of Bitcoin be above $68,000 on Nove | Crypto | NO | `93.5%` | `89.4%` | `+4.2 п.п.` | `0.10%` | REJECTED: Duplicate underlying event (crypto:bitcoin:november 16) |
| Will the price of Bitcoin be above $66,000 on Nove | Crypto | NO | `73.5%` | `68.7%` | `+4.8 п.п.` | `0.10%` | REJECTED: Duplicate underlying event (crypto:bitcoin:november 17) |
| Will the price of Ethereum be above $1,600 on Nove | Crypto | YES | `89.8%` | `85.7%` | `+4.1 п.п.` | `0.40%` | REJECTED: Category cap reached (4/4 in Crypto) |
| Will the price of Bitcoin be above $68,000 on Nove | Crypto | NO | `93.7%` | `89.3%` | `+4.4 п.п.` | `0.40%` | REJECTED: Duplicate underlying event (crypto:bitcoin:november 16) |
| Will the price of Bitcoin be above $66,000 on Nove | Crypto | NO | `73.3%` | `68.4%` | `+4.9 п.п.` | `0.10%` | REJECTED: Duplicate underlying event (crypto:bitcoin:november 17) |
| Will Bitcoin dip to $63,000 on November 14? | Crypto | NO | `78.3%` | `70.1%` | `+8.2 п.п.` | `6.90%` | REJECTED: CLOB round-trip slippage 6.90% > 2.0% limit |
| Will Bitcoin reach $68,000 November 9-15? | Crypto | NO | `95.5%` | `91.0%` | `+4.5 п.п.` | `2.00%` | REJECTED: Duplicate underlying event (crypto:bitcoin:november 9) |
| Will Ethereum dip to $1,600 November 9-15? | Crypto | NO | `98.2%` | `92.0%` | `+6.2 п.п.` | `3.90%` | REJECTED: CLOB round-trip slippage 3.90% > 2.0% limit |
