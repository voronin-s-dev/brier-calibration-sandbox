# 📊 Отчёт симулятора Polymarket (Устав Grok Bot — Демо-счёт)
**Обновлено:** `2026-11-22 11:30:59 UTC`

## 💰 Состояние виртуального портфеля
| Показатель | Значение | Правило устава |
| :--- | :--- | :--- |
| **Стартовый капитал** | `$50.00 USDC` | Не добавлять деньги |
| **Текущий баланс (Equity)** | **`$24.59 USDC`** (`-25.41$` / `-50.82%`) | Cash + Mark-to-Market по CLOB Bid |
| **Свободный кэш / В сделках** | `$21.61` / `$2.98 USDC` | До 8 открытых позиций, макс 8% банка |
| **Цель окупаемости подписки** | `$-25.41 / $60.00` (`0.0%`) | Цель: +$60.00 в месяц |
| **Просадка от пика (Текущая / Макс)** | `37.42%` / `37.42%` (Пик: `$39.29`) | Стоп-кран при просадке 40% |
| **Закрытых сделок / Win Rate** | `227` / `63.4%` | Brier Score: `0.2280` |

## 📂 Открытые позиции (3 / 8)
| # | Рынок | Кат. | Исход | Вход (Ask VWAP) | Текущий Bid | Оценка бота | Размер ($) | Нереализ. PnL | Источник |
| :- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| #225 | Dolphins vs. Bills | Sports | **NO** | `0.920` | `0.910` | `95.0%` | `$1.00` | `$-0.01` | https://www.nfl.com/scores |
| #230 | Spread: Manchester United FC (-1.5) | Sports | **NO** | `0.920` | `0.920` | `96.0%` | `$1.00` | `$+0.00` | https://www.premierleague.com/ |
| #231 | Will FC Barcelona vs. Villarreal CF end in a draw? | Sports | **NO** | `0.900` | `0.890` | `96.5%` | `$1.00` | `$-0.01` | https://www.laliga.com/ |

## 🧪 Теневая песочница (Shadow Sandbox)
| Показатель | Значение |
| :--- | :--- |
| **Виртуальный баланс (Equity)** | **`$47.30 USDC`** |
| **Свободный кэш / В сделках** | `$39.23` / `$8.08 USDC` |
| **Открытых позиций** | `4 / 5` |
| **Текущая просадка** | `28.31%` |

### Открытые позиции в песочнице (4 / 5)
| # | Рынок | Кат. | Исход | Вход (Ask VWAP) | Текущий Bid | Оценка бота | Размер ($) | Нереализ. PnL | Источник |
| :- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| #307 | Hurricanes vs. Rangers | Weather | **YES** | `0.600` | `0.590` | `65.0%` | `$1.66` | `$-0.03` | https://www.nhl.com/scores |
| #310 | Will the price of Ethereum be above $1,700 on November  | Crypto | **NO** | `0.326` | `0.347` | `40.3%` | `$2.10` | `$+0.14` | https://www.binance.com/en/tra |
| #311 | Will the price of Bitcoin be above $62,000 on November  | Crypto | **NO** | `0.678` | `0.677` | `70.3%` | `$1.16` | `$-0.00` | https://www.binance.com/en/tra |
| #312 | Will the price of Bitcoin be above $62,000 on November  | Crypto | **NO** | `0.786` | `0.859` | `88.7%` | `$2.79` | `$+0.26` | https://www.binance.com/en/tra |

### Доходность по замороженным категориям (Песочница)
| Категория | Сделок | PnL | Win Rate |
| :--- | :--- | :--- | :--- |
| **Crypto** | `266` | `-$2.80` | `56%` |
| **Geopolitics** | `8` | `+$1.02` | `62%` |
| **Macro** | `10` | `+$1.72` | `70%` |
| **Other** | `20` | `-$1.65` | `40%` |
| **Weather** | `4` | `-$1.35` | `0%` |

## 🔍 Последние проверенные кандидаты и фильтр стакана CLOB
| Рынок | Кат. | Сторона | Оценка бота | Цена Ask | Перекос (Edge) | Проскальзывание CLOB | Решение |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Will FC Barcelona vs. Villarreal CF end in a draw? | Sports | NO | `96.5%` | `90.0%` | `+6.5 п.п.` | `1.00%` | EXECUTED BUY #231 ($1.00 @ 0.9000) |
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
