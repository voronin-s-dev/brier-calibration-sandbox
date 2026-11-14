# 📊 Отчёт симулятора Polymarket (Устав Grok Bot — Демо-счёт)
**Обновлено:** `2026-11-14 23:49:20 UTC`

## 💰 Состояние виртуального портфеля
| Показатель | Значение | Правило устава |
| :--- | :--- | :--- |
| **Стартовый капитал** | `$50.00 USDC` | Не добавлять деньги |
| **Текущий баланс (Equity)** | **`$30.81 USDC`** (`-19.19$` / `-38.38%`) | Cash + Mark-to-Market по CLOB Bid |
| **Свободный кэш / В сделках** | `$24.63` / `$6.17 USDC` | До 8 открытых позиций, макс 8% банка |
| **Цель окупаемости подписки** | `$-19.19 / $60.00` (`0.0%`) | Цель: +$60.00 в месяц |
| **Просадка от пика (Текущая / Макс)** | `21.59%` / `24.45%` (Пик: `$39.29`) | Стоп-кран при просадке 40% |
| **Закрытых сделок / Win Rate** | `198` / `65.7%` | Brier Score: `0.1960` |

## 📂 Открытые позиции (4 / 8)
| # | Рынок | Кат. | Исход | Вход (Ask VWAP) | Текущий Bid | Оценка бота | Размер ($) | Нереализ. PnL | Источник |
| :- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| #200 | Will the price of Bitcoin be above $66,000 on November  | Crypto | **NO** | `0.662` | `0.744` | `82.5%` | `$1.58` | `$+0.20` | Kraken BTCUSDT 1m/1h Spot Klin |
| #201 | Will the price of Bitcoin be above $62,000 on November  | Crypto | **YES** | `0.738` | `0.705` | `70.8%` | `$2.50` | `$-0.11` | Kraken BTCUSDT 1m/1h Spot Klin |
| #202 | Will Bitcoin dip to $62,000 on November 14? | Crypto | **NO** | `0.883` | `0.798` | `90.5%` | `$1.00` | `$-0.10` | https://www.binance.com/en/tra |
| #203 | Will Bitcoin dip to $60,000 November 9-15? | Crypto | **NO** | `0.820` | `0.738` | `91.3%` | `$1.23` | `$-0.12` | Kraken BTCUSDT 1m/1h Spot Klin |

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
| Will Bitcoin reach $68,000 November 9-15? | Crypto | NO | `95.5%` | `91.0%` | `+4.5 п.п.` | `2.00%` | REJECTED: Duplicate underlying event (crypto:bitcoin:november 9) |
| Will Ethereum dip to $1,600 November 9-15? | Crypto | NO | `98.2%` | `92.0%` | `+6.2 п.п.` | `3.90%` | REJECTED: CLOB round-trip slippage 3.90% > 2.0% limit |
| UFC 334: Jared Gordon vs. Melquizael Costa (Lightw | Sports | NO | `94.0%` | `76.0%` | `+18.0 п.п.` | `3.00%` | REJECTED: CLOB round-trip slippage 3.00% > 2.0% limit |
| Will the price of Bitcoin be above $66,000 on Nove | Crypto | NO | `92.9%` | `86.1%` | `+6.8 п.п.` | `0.50%` | REJECTED: Category cap reached (4/4 in Crypto) |
| Will the price of Bitcoin be above $66,000 on Nove | Crypto | NO | `78.0%` | `72.1%` | `+5.9 п.п.` | `0.10%` | REJECTED: Duplicate underlying event (crypto:bitcoin:november 17) |
| Will the price of Bitcoin be above $66,000 on Nove | Crypto | NO | `72.9%` | `67.0%` | `+5.9 п.п.` | `1.00%` | REJECTED: Category cap reached (4/4 in Crypto) |
| Will the price of Ethereum be above $1,700 on Nove | Crypto | YES | `81.0%` | `85.8%` | `-4.8 п.п.` | `0.10%` | REJECTED: Edge -4.8 pp < 2 pp threshold (P_est=81.0% vs AskVWAP=85.8%) |
| Will the price of Ethereum be above $1,800 on Nove | Crypto | NO | `84.2%` | `72.2%` | `+12.0 п.п.` | `0.10%` | REJECTED: Category cap reached (4/4 in Crypto) |
| Will the price of Ethereum be above $1,600 on Nove | Crypto | YES | `86.2%` | `81.1%` | `+5.1 п.п.` | `0.30%` | REJECTED: Category cap reached (4/4 in Crypto) |
| Will Ethereum dip to $1,600 November 9-15? | Crypto | NO | `98.2%` | `87.1%` | `+11.1 п.п.` | `2.00%` | REJECTED: Category cap reached (4/4 in Crypto) |
| Will Bitcoin dip to $61,000 on November 14? | Crypto | NO | `94.0%` | `88.5%` | `+5.5 п.п.` | `1.30%` | REJECTED: Duplicate underlying event (crypto:bitcoin:november 14) |
| Will Bitcoin dip to $58,000 November 9-15? | Crypto | NO | `95.1%` | `90.9%` | `+4.2 п.п.` | `0.10%` | REJECTED: Duplicate underlying event (crypto:bitcoin:november 9) |
| Will the price of Ethereum be above $1,700 on Nove | Crypto | YES | `80.2%` | `75.8%` | `+4.3 п.п.` | `1.00%` | REJECTED: Category cap reached (4/4 in Crypto) |
| Will the price of Ethereum be above $1,600 on Nove | Crypto | YES | `86.6%` | `82.5%` | `+4.1 п.п.` | `0.10%` | REJECTED: Category cap reached (4/4 in Crypto) |
| Will Ethereum dip to $1,600 November 9-15? | Crypto | NO | `98.2%` | `88.5%` | `+9.7 п.п.` | `3.40%` | REJECTED: CLOB round-trip slippage 3.40% > 2.0% limit |
| Will the price of Bitcoin be above $66,000 on Nove | Crypto | NO | `77.9%` | `72.7%` | `+5.2 п.п.` | `0.20%` | REJECTED: Duplicate underlying event (crypto:bitcoin:november 17) |
| Will the price of Ethereum be above $1,600 on Nove | Crypto | YES | `87.1%` | `82.9%` | `+4.2 п.п.` | `1.50%` | REJECTED: Category cap reached (4/4 in Crypto) |
| Will Ethereum dip to $1,600 November 9-15? | Crypto | NO | `98.5%` | `86.2%` | `+12.3 п.п.` | `2.80%` | REJECTED: CLOB round-trip slippage 2.80% > 2.0% limit |
