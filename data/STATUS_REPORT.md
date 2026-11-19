# 📊 Отчёт симулятора Polymarket (Устав Grok Bot — Демо-счёт)
**Обновлено:** `2026-11-19 23:31:00 UTC`

## 💰 Состояние виртуального портфеля
| Показатель | Значение | Правило устава |
| :--- | :--- | :--- |
| **Стартовый капитал** | `$50.00 USDC` | Не добавлять деньги |
| **Текущий баланс (Equity)** | **`$28.84 USDC`** (`-21.16$` / `-42.31%`) | Cash + Mark-to-Market по CLOB Bid |
| **Свободный кэш / В сделках** | `$28.84` / `$0.00 USDC` | До 8 открытых позиций, макс 8% банка |
| **Цель окупаемости подписки** | `$-21.16 / $60.00` (`0.0%`) | Цель: +$60.00 в месяц |
| **Просадка от пика (Текущая / Макс)** | `26.59%` / `28.95%` (Пик: `$39.29`) | Стоп-кран при просадке 40% |
| **Закрытых сделок / Win Rate** | `219` / `63.9%` | Brier Score: `0.1960` |

## 📂 Открытые позиции (0 / 8)
*Нет активных позиций.*

## 🧪 Теневая песочница (Shadow Sandbox)
| Показатель | Значение |
| :--- | :--- |
| **Виртуальный баланс (Equity)** | **`$62.78 USDC`** |
| **Свободный кэш / В сделках** | `$48.79` / `$13.99 USDC` |
| **Открытых позиций** | `5 / 5` |
| **Текущая просадка** | `4.86%` |

### Открытые позиции в песочнице (5 / 5)
| # | Рынок | Кат. | Исход | Вход (Ask VWAP) | Текущий Bid | Оценка бота | Размер ($) | Нереализ. PnL | Источник |
| :- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| #177 | Will Bitcoin dip to $60,000 on November 19? | Crypto | **NO** | `0.851` | `0.849` | `92.2%` | `$2.76` | `$-0.01` | https://www.binance.com/en/tra |
| #190 | Will Bitcoin dip to $60,000 November 16-22? | Crypto | **YES** | `0.450` | `0.490` | `58.1%` | `$1.83` | `$+0.16` | https://www.binance.com/en/tra |
| #191 | Will Ethereum dip to $1,700 November 16-22? | Crypto | **YES** | `0.510` | `0.570` | `66.2%` | `$2.45` | `$+0.29` | https://www.binance.com/en/tra |
| #192 | Will the price of Bitcoin be above $64,000 on November  | Crypto | **NO** | `0.850` | `0.880` | `92.1%` | `$3.68` | `$+0.13` | https://www.binance.com/en/tra |
| #193 | S&P 500 (SPX) Up or Down on November 20? | Macro | **YES** | `0.530` | `0.530` | `61.1%` | `$2.70` | `$+0.00` | https://www.wsj.com/market-dat |

### Доходность по замороженным категориям (Песочница)
| Категория | Сделок | PnL | Win Rate |
| :--- | :--- | :--- | :--- |
| **Crypto** | `154` | `+$11.71` | `62%` |
| **Geopolitics** | `8` | `+$1.02` | `62%` |
| **Macro** | `5` | `+$0.91` | `60%` |
| **Other** | `19` | `-$1.30` | `42%` |
| **Weather** | `2` | `-$0.13` | `0%` |

## 🔍 Последние проверенные кандидаты и фильтр стакана CLOB
| Рынок | Кат. | Сторона | Оценка бота | Цена Ask | Перекос (Edge) | Проскальзывание CLOB | Решение |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Will Elon Musk post 340-359 tweets from November 1 | Geopolitics | NO | `93.8%` | `88.9%` | `+4.9 п.п.` | `1.80%` | REJECTED: Social Mention Count Guard: Tweet/post count bracket markets prohibited (burst variance trap) |
| Will Elon Musk post 400-419 tweets from November 1 | Geopolitics | NO | `97.1%` | `92.4%` | `+4.7 п.п.` | `1.30%` | REJECTED: Contract price $0.924 outside sweet spot [$0.70, $0.92] |
| Will Elon Musk post 340-359 tweets from November 1 | Geopolitics | NO | `94.0%` | `89.6%` | `+4.4 п.п.` | `0.50%` | REJECTED: Social Mention Count Guard: Tweet/post count bracket markets prohibited (burst variance trap) |
| Will Elon Musk post 340-359 tweets from November 1 | Geopolitics | NO | `95.1%` | `91.0%` | `+4.1 п.п.` | `0.20%` | REJECTED: Social Mention Count Guard: Tweet/post count bracket markets prohibited (burst variance trap) |
| Israel x Iran ceasefire continues through November | Geopolitics | YES | `98.0%` | `94.0%` | `+4.0 п.п.` | `1.00%` | REJECTED: Contract price $0.940 outside sweet spot [$0.70, $0.92] |
| Israel x Iran ceasefire continues through November | Geopolitics | YES | `98.0%` | `94.0%` | `+4.0 п.п.` | `1.00%` | REJECTED: Contract price $0.940 outside sweet spot [$0.70, $0.92] |
| Will Elon Musk post 400-419 tweets from November 1 | Geopolitics | NO | `94.5%` | `88.0%` | `+6.5 п.п.` | `1.70%` | REJECTED: Social Mention Count Guard: Tweet/post count bracket markets prohibited (burst variance trap) |
| Will Elon Musk post 400-419 tweets from November 1 | Geopolitics | NO | `95.8%` | `91.6%` | `+4.2 п.п.` | `0.90%` | REJECTED: Social Mention Count Guard: Tweet/post count bracket markets prohibited (burst variance trap) |
| Israel x Iran ceasefire continues through November | Geopolitics | YES | `98.0%` | `94.0%` | `+4.0 п.п.` | `1.00%` | REJECTED: Contract price $0.940 outside sweet spot [$0.70, $0.92] |
| Will Elon Musk post 400-419 tweets from November 1 | Geopolitics | NO | `96.7%` | `92.1%` | `+4.5 п.п.` | `1.60%` | REJECTED: Contract price $0.921 outside sweet spot [$0.70, $0.92] |
| Will South Africa win? | Other | YES | `98.0%` | `94.0%` | `+4.0 п.п.` | `2.00%` | REJECTED: Contract price $0.940 outside sweet spot [$0.70, $0.92] |
| Will Elon Musk post 400-419 tweets from November 1 | Geopolitics | NO | `97.0%` | `92.7%` | `+4.3 п.п.` | `0.10%` | REJECTED: Contract price $0.927 outside sweet spot [$0.70, $0.92] |
| Will South Africa win? | Other | YES | `98.0%` | `94.0%` | `+4.0 п.п.` | `2.00%` | REJECTED: Contract price $0.940 outside sweet spot [$0.70, $0.92] |
| Will Elon Musk post 320-339 tweets from November 1 | Geopolitics | NO | `94.2%` | `89.6%` | `+4.5 п.п.` | `1.00%` | REJECTED: Social Mention Count Guard: Tweet/post count bracket markets prohibited (burst variance trap) |
| Will Elon Musk post 380-399 tweets from November 1 | Geopolitics | NO | `94.8%` | `90.6%` | `+4.2 п.п.` | `0.50%` | REJECTED: Social Mention Count Guard: Tweet/post count bracket markets prohibited (burst variance trap) |
| Israel x Iran ceasefire continues through November | Geopolitics | YES | `98.0%` | `94.0%` | `+4.0 п.п.` | `1.00%` | REJECTED: Contract price $0.940 outside sweet spot [$0.70, $0.92] |
| Israel x Iran ceasefire continues through November | Geopolitics | YES | `98.0%` | `94.0%` | `+4.0 п.п.` | `1.00%` | REJECTED: Contract price $0.940 outside sweet spot [$0.70, $0.92] |
| Israel x Iran ceasefire continues through November | Geopolitics | YES | `98.0%` | `94.0%` | `+4.0 п.п.` | `1.00%` | REJECTED: Contract price $0.940 outside sweet spot [$0.70, $0.92] |
