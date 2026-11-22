# 📊 Отчёт симулятора Polymarket (Устав Grok Bot — Демо-счёт)
**Обновлено:** `2026-11-22 04:40:06 UTC`

## 💰 Состояние виртуального портфеля
| Показатель | Значение | Правило устава |
| :--- | :--- | :--- |
| **Стартовый капитал** | `$50.00 USDC` | Не добавлять деньги |
| **Текущий баланс (Equity)** | **`$25.56 USDC`** (`-24.44$` / `-48.88%`) | Cash + Mark-to-Market по CLOB Bid |
| **Свободный кэш / В сделках** | `$21.54` / `$4.02 USDC` | До 8 открытых позиций, макс 8% банка |
| **Цель окупаемости подписки** | `$-24.44 / $60.00` (`0.0%`) | Цель: +$60.00 в месяц |
| **Просадка от пика (Текущая / Макс)** | `34.95%` / `35.52%` (Пик: `$39.29`) | Стоп-кран при просадке 40% |
| **Закрытых сделок / Win Rate** | `225` / `63.6%` | Brier Score: `0.2280` |

## 📂 Открытые позиции (4 / 8)
| # | Рынок | Кат. | Исход | Вход (Ask VWAP) | Текущий Bid | Оценка бота | Размер ($) | Нереализ. PnL | Источник |
| :- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| #223 | Israel x Iran ceasefire continues through November 22? | Geopolitics | **YES** | `0.920` | `0.982` | `98.0%` | `$1.00` | `$+0.07` | the totality of information av |
| #225 | Dolphins vs. Bills | Sports | **NO** | `0.920` | `0.910` | `95.0%` | `$1.00` | `$-0.01` | https://www.nfl.com/scores |
| #227 | San Diego State vs. Boise State | Sports | **NO** | `0.910` | `0.885` | `94.2%` | `$1.00` | `$-0.03` | https://www.ncaa.com/ |
| #230 | Spread: Manchester United FC (-1.5) | Sports | **NO** | `0.920` | `0.910` | `95.0%` | `$1.00` | `$-0.01` | https://www.premierleague.com/ |

## 🧪 Теневая песочница (Shadow Sandbox)
| Показатель | Значение |
| :--- | :--- |
| **Виртуальный баланс (Equity)** | **`$49.36 USDC`** |
| **Свободный кэш / В сделках** | `$36.59` / `$12.77 USDC` |
| **Открытых позиций** | `5 / 5` |
| **Текущая просадка** | `25.20%` |

### Открытые позиции в песочнице (5 / 5)
| # | Рынок | Кат. | Исход | Вход (Ask VWAP) | Текущий Bid | Оценка бота | Размер ($) | Нереализ. PnL | Источник |
| :- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| #288 | Will Ethereum dip to $1,500 November 16-22? | Crypto | **NO** | `0.906` | `0.949` | `98.5%` | `$3.31` | `$+0.16` | https://www.binance.com/en/tra |
| #290 | Will Anthropic close below its IPO price by November 23 | Macro | **NO** | `0.750` | `0.820` | `84.0%` | `$3.28` | `$+0.31` | https://www.nasdaq.com/market- |
| #297 | Will India win? | Other | **YES** | `0.570` | `0.570` | `68.7%` | `$1.53` | `$+0.00` | https://www.espncricinfo.com/ |
| #298 | Will Anthropic close below its IPO price by November 25 | Macro | **NO** | `0.540` | `0.540` | `60.0%` | `$2.66` | `$+0.00` | https://www.nasdaq.com/market- |
| #301 | Will Bitcoin dip to $58,000 November 16-22? | Crypto | **YES** | `0.510` | `0.460` | `55.8%` | `$1.69` | `$-0.17` | https://www.binance.com/en/tra |

### Доходность по замороженным категориям (Песочница)
| Категория | Сделок | PnL | Win Rate |
| :--- | :--- | :--- | :--- |
| **Crypto** | `257` | `-$0.15` | `57%` |
| **Geopolitics** | `8` | `+$1.02` | `62%` |
| **Macro** | `8` | `+$0.84` | `62%` |
| **Other** | `19` | `-$1.30` | `42%` |
| **Weather** | `4` | `-$1.35` | `0%` |

## 🔍 Последние проверенные кандидаты и фильтр стакана CLOB
| Рынок | Кат. | Сторона | Оценка бота | Цена Ask | Перекос (Edge) | Проскальзывание CLOB | Решение |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Spread: Manchester United FC (-1.5) | Sports | NO | `95.0%` | `92.0%` | `+3.0 п.п.` | `1.00%` | EXECUTED BUY #230 ($1.00 @ 0.9200) |
| SMU vs. Notre Dame | Sports | NO | `94.0%` | `91.0%` | `+3.0 п.п.` | `1.00%` | EXECUTED BUY #229 ($1.00 @ 0.9100) |
| UFC Fight Night: Brian Ortega vs. Dan Hooker (Ligh | Sports | NO | `95.0%` | `99.0%` | `-4.0 п.п.` | `1.00%` | REJECTED: Edge -4.0 pp < 2.5 pp threshold (P_est=95.0% vs AskVWAP=99.0%) |
| UFC Fight Night: Jared Cannonier vs. Ikram Alisker | Sports | NO | `98.5%` | `93.0%` | `+5.5 п.п.` | `2.00%` | REJECTED: Contract price $0.930 outside sweet spot [$0.70, $0.92] |
| Will Real Madrid CF vs. RC Celta de Vigo end in a  | Sports | NO | `96.5%` | `90.0%` | `+6.5 п.п.` | `1.00%` | EXECUTED BUY #228 ($1.00 @ 0.9000) |
| UFC Fight Night: Jake Matthews vs. Tahir Abdullaye | Sports | NO | `95.0%` | `100.0%` | `-5.0 п.п.` | `100.00%` | REJECTED: Edge -5.0 pp < 2.5 pp threshold (P_est=95.0% vs AskVWAP=100.0%) |
| San Diego State vs. Boise State | Sports | NO | `94.0%` | `91.0%` | `+3.0 п.п.` | `1.00%` | EXECUTED BUY #227 ($1.00 @ 0.9100) |
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
