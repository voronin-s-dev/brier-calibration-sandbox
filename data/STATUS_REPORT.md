# 📊 Отчёт симулятора Polymarket (Устав Grok Bot — Демо-счёт)
**Обновлено:** `2026-11-21 13:40:08 UTC`

## 💰 Состояние виртуального портфеля
| Показатель | Значение | Правило устава |
| :--- | :--- | :--- |
| **Стартовый капитал** | `$50.00 USDC` | Не добавлять деньги |
| **Текущий баланс (Equity)** | **`$25.83 USDC`** (`-24.17$` / `-48.34%`) | Cash + Mark-to-Market по CLOB Bid |
| **Свободный кэш / В сделках** | `$22.81` / `$3.02 USDC` | До 8 открытых позиций, макс 8% банка |
| **Цель окупаемости подписки** | `$-24.17 / $60.00` (`0.0%`) | Цель: +$60.00 в месяц |
| **Просадка от пика (Текущая / Макс)** | `34.27%` / `34.28%` (Пик: `$39.29`) | Стоп-кран при просадке 40% |
| **Закрытых сделок / Win Rate** | `220` / `64.1%` | Brier Score: `0.1960` |

## 📂 Открытые позиции (5 / 8)
| # | Рынок | Кат. | Исход | Вход (Ask VWAP) | Текущий Bid | Оценка бота | Размер ($) | Нереализ. PnL | Источник |
| :- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| #222 | Will Kai Cenat finish his GTA VI marathon by November 2 | Other | **NO** | `0.780` | `0.000` | `79.0%` | `$2.33` | `$-2.33` | https://www.twitch.tv/kaicenat |
| #223 | Israel x Iran ceasefire continues through November 22? | Geopolitics | **YES** | `0.920` | `0.961` | `98.0%` | `$1.00` | `$+0.04` | the totality of information av |
| #224 | Will Kai Cenat finish his GTA VI marathon by November 2 | Other | **NO** | `0.900` | `0.000` | `93.0%` | `$1.00` | `$-1.00` | footage from Kai Cenat's offic |
| #225 | Dolphins vs. Bills | Sports | **NO** | `0.920` | `0.910` | `95.0%` | `$1.00` | `$-0.01` | https://www.nfl.com/scores |
| #226 | Pelicans vs. Spurs | Sports | **NO** | `0.910` | `0.900` | `94.0%` | `$1.00` | `$-0.01` | https://www.nba.com/ |

## 🧪 Теневая песочница (Shadow Sandbox)
| Показатель | Значение |
| :--- | :--- |
| **Виртуальный баланс (Equity)** | **`$53.00 USDC`** |
| **Свободный кэш / В сделках** | `$40.05` / `$12.95 USDC` |
| **Открытых позиций** | `5 / 5` |
| **Текущая просадка** | `19.69%` |

### Открытые позиции в песочнице (5 / 5)
| # | Рынок | Кат. | Исход | Вход (Ask VWAP) | Текущий Bid | Оценка бота | Размер ($) | Нереализ. PnL | Источник |
| :- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| #230 | Oilers vs. Hurricanes | Weather | **YES** | `0.390` | `0.340` | `44.0%` | `$1.40` | `$-0.18` | https://www.nhl.com/scores |
| #288 | Will Ethereum dip to $1,500 November 16-22? | Crypto | **NO** | `0.906` | `0.936` | `96.0%` | `$3.31` | `$+0.11` | https://www.binance.com/en/tra |
| #290 | Will Anthropic close below its IPO price by November 23 | Macro | **NO** | `0.750` | `0.740` | `83.0%` | `$3.28` | `$-0.04` | https://www.nasdaq.com/market- |
| #291 | Will Bitcoin reach $61,000 on November 21? | Crypto | **NO** | `0.270` | `0.270` | `58.1%` | `$3.18` | `$+0.00` | https://www.binance.com/en/tra |
| #292 | Will the price of Bitcoin be above $60,000 on November  | Crypto | **NO** | `0.380` | `0.380` | `60.2%` | `$1.89` | `$+0.00` | https://www.binance.com/en/tra |

### Доходность по замороженным категориям (Песочница)
| Категория | Сделок | PnL | Win Rate |
| :--- | :--- | :--- | :--- |
| **Crypto** | `249` | `+$3.64` | `58%` |
| **Geopolitics** | `8` | `+$1.02` | `62%` |
| **Macro** | `8` | `+$0.84` | `62%` |
| **Other** | `19` | `-$1.30` | `42%` |
| **Weather** | `3` | `-$1.10` | `0%` |

## 🔍 Последние проверенные кандидаты и фильтр стакана CLOB
| Рынок | Кат. | Сторона | Оценка бота | Цена Ask | Перекос (Edge) | Проскальзывание CLOB | Решение |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Pelicans vs. Spurs | Sports | NO | `94.0%` | `91.0%` | `+3.0 п.п.` | `1.00%` | EXECUTED BUY #226 ($1.00 @ 0.9100) |
| Dolphins vs. Bills | Sports | NO | `95.0%` | `92.0%` | `+3.0 п.п.` | `1.00%` | EXECUTED BUY #225 ($1.00 @ 0.9200) |
| Will Kai Cenat finish his GTA VI marathon by Novem | Other | NO | `94.5%` | `90.0%` | `+4.5 п.п.` | `2.00%` | EXECUTED BUY #224 ($1.00 @ 0.9000) |
| Israel x Iran ceasefire continues through November | Geopolitics | YES | `96.0%` | `92.0%` | `+4.0 п.п.` | `2.00%` | EXECUTED BUY #223 ($1.00 @ 0.9200) |
| Will Elon Musk post 320-339 tweets from November 1 | Geopolitics | NO | `96.2%` | `92.1%` | `+4.2 п.п.` | `0.40%` | REJECTED: Contract price $0.921 outside sweet spot [$0.70, $0.92] |
| Will Kai Cenat finish his GTA VI marathon by Novem | Other | NO | `82.5%` | `78.0%` | `+4.5 п.п.` | `2.00%` | EXECUTED BUY #222 ($2.33 @ 0.7800) |
| Israel x Iran ceasefire continues through November | Geopolitics | YES | `98.0%` | `94.0%` | `+4.0 п.п.` | `1.00%` | REJECTED: Contract price $0.940 outside sweet spot [$0.70, $0.92] |
| Will Elon Musk post 380-399 tweets from November 1 | Geopolitics | NO | `95.3%` | `90.8%` | `+4.5 п.п.` | `3.00%` | REJECTED: Social Mention Count Guard: Tweet/post count bracket markets prohibited (burst variance trap) |
| Will Kai Cenat finish his GTA VI marathon by Novem | Other | NO | `87.7%` | `79.0%` | `+8.7 п.п.` | `2.00%` | EXECUTED BUY #221 ($2.31 @ 0.7900) |
| Will Elon Musk post 340-359 tweets from November 1 | Geopolitics | NO | `93.8%` | `88.9%` | `+4.9 п.п.` | `1.80%` | REJECTED: Social Mention Count Guard: Tweet/post count bracket markets prohibited (burst variance trap) |
| Will Elon Musk post 400-419 tweets from November 1 | Geopolitics | NO | `97.1%` | `92.4%` | `+4.7 п.п.` | `1.30%` | REJECTED: Contract price $0.924 outside sweet spot [$0.70, $0.92] |
| Will Elon Musk post 340-359 tweets from November 1 | Geopolitics | NO | `94.0%` | `89.6%` | `+4.4 п.п.` | `0.50%` | REJECTED: Social Mention Count Guard: Tweet/post count bracket markets prohibited (burst variance trap) |
| Will Elon Musk post 340-359 tweets from November 1 | Geopolitics | NO | `95.1%` | `91.0%` | `+4.1 п.п.` | `0.20%` | REJECTED: Social Mention Count Guard: Tweet/post count bracket markets prohibited (burst variance trap) |
| Israel x Iran ceasefire continues through November | Geopolitics | YES | `98.0%` | `94.0%` | `+4.0 п.п.` | `1.00%` | REJECTED: Contract price $0.940 outside sweet spot [$0.70, $0.92] |
| Israel x Iran ceasefire continues through November | Geopolitics | YES | `98.0%` | `94.0%` | `+4.0 п.п.` | `1.00%` | REJECTED: Contract price $0.940 outside sweet spot [$0.70, $0.92] |
| Will Elon Musk post 400-419 tweets from November 1 | Geopolitics | NO | `94.5%` | `88.0%` | `+6.5 п.п.` | `1.70%` | REJECTED: Social Mention Count Guard: Tweet/post count bracket markets prohibited (burst variance trap) |
| Will Elon Musk post 400-419 tweets from November 1 | Geopolitics | NO | `95.8%` | `91.6%` | `+4.2 п.п.` | `0.90%` | REJECTED: Social Mention Count Guard: Tweet/post count bracket markets prohibited (burst variance trap) |
| Israel x Iran ceasefire continues through November | Geopolitics | YES | `98.0%` | `94.0%` | `+4.0 п.п.` | `1.00%` | REJECTED: Contract price $0.940 outside sweet spot [$0.70, $0.92] |
