# 📊 Отчёт симулятора Polymarket (Устав Grok Bot — Демо-счёт)
**Обновлено:** `2026-11-22 18:49:10 UTC`

## 💰 Состояние виртуального портфеля
| Показатель | Значение | Правило устава |
| :--- | :--- | :--- |
| **Стартовый капитал** | `$50.00 USDC` | Не добавлять деньги |
| **Текущий баланс (Equity)** | **`$24.96 USDC`** (`-25.04$` / `-50.07%`) | Cash + Mark-to-Market по CLOB Bid |
| **Свободный кэш / В сделках** | `$22.86` / `$2.10 USDC` | До 8 открытых позиций, макс 8% банка |
| **Цель окупаемости подписки** | `$-25.04 / $60.00` (`0.0%`) | Цель: +$60.00 в месяц |
| **Просадка от пика (Текущая / Макс)** | `36.47%` / `37.84%` (Пик: `$39.29`) | Стоп-кран при просадке 40% |
| **Закрытых сделок / Win Rate** | `230` / `63.9%` | Brier Score: `0.2280` |

## 📂 Открытые позиции (2 / 8)
| # | Рынок | Кат. | Исход | Вход (Ask VWAP) | Текущий Bid | Оценка бота | Размер ($) | Нереализ. PnL | Источник |
| :- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| #232 | Cardinals vs. Chiefs | Sports | **NO** | `0.920` | `0.970` | `98.5%` | `$1.00` | `$+0.05` | https://www.nfl.com/scores |
| #233 | Spread: Steelers (-3.5) | Sports | **NO** | `0.860` | `0.900` | `97.5%` | `$1.00` | `$+0.05` | https://www.nfl.com/scores |

## 🧪 Теневая песочница (Shadow Sandbox)
| Показатель | Значение |
| :--- | :--- |
| **Виртуальный баланс (Equity)** | **`$49.53 USDC`** |
| **Свободный кэш / В сделках** | `$38.16` / `$11.37 USDC` |
| **Открытых позиций** | `5 / 5` |
| **Текущая просадка** | `24.94%` |

### Открытые позиции в песочнице (5 / 5)
| # | Рынок | Кат. | Исход | Вход (Ask VWAP) | Текущий Bid | Оценка бота | Размер ($) | Нереализ. PnL | Источник |
| :- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| #311 | Will the price of Bitcoin be above $62,000 on November  | Crypto | **NO** | `0.678` | `0.732` | `77.6%` | `$1.16` | `$+0.09` | https://www.binance.com/en/tra |
| #322 | Will Bitcoin dip to $58,000 on November 22? | Crypto | **NO** | `0.910` | `0.900` | `92.7%` | `$2.98` | `$-0.03` | https://www.binance.com/en/tra |
| #324 | Will the price of Ethereum be above $1,700 on November  | Crypto | **NO** | `0.390` | `0.380` | `42.3%` | `$1.17` | `$-0.03` | https://www.binance.com/en/tra |
| #326 | Will Ethereum reach $1,800 November 16-22? | Crypto | **NO** | `0.902` | `0.932` | `96.8%` | `$2.97` | `$+0.10` | https://www.binance.com/en/tra |
| #327 | Will Bitcoin dip to $58,000 November 16-22? | Crypto | **NO** | `0.880` | `0.880` | `92.5%` | `$2.96` | `$+0.00` | https://www.binance.com/en/tra |

### Доходность по замороженным категориям (Песочница)
| Категория | Сделок | PnL | Win Rate |
| :--- | :--- | :--- | :--- |
| **Crypto** | `279` | `-$0.31` | `56%` |
| **Geopolitics** | `8` | `+$1.02` | `62%` |
| **Macro** | `10` | `+$1.72` | `70%` |
| **Other** | `20` | `-$1.65` | `40%` |
| **Weather** | `5` | `-$1.37` | `0%` |

## 🔍 Последние проверенные кандидаты и фильтр стакана CLOB
| Рынок | Кат. | Сторона | Оценка бота | Цена Ask | Перекос (Edge) | Проскальзывание CLOB | Решение |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Spread: Steelers (-4.5) | Sports | NO | `97.5%` | `93.0%` | `+4.5 п.п.` | `2.00%` | REJECTED: Contract price $0.930 outside sweet spot [$0.70, $0.92] |
| Spread: Steelers (-4.5) | Sports | NO | `97.5%` | `89.0%` | `+8.5 п.п.` | `1.00%` | REJECTED: Duplicate underlying event (sports:steelers:nodate) |
| Spread: Steelers (-3.5) | Sports | NO | `97.5%` | `86.0%` | `+11.5 п.п.` | `1.00%` | EXECUTED BUY #233 ($1.00 @ 0.8600) |
| Spread: Titans (-3.5) | Sports | NO | `97.5%` | `85.0%` | `+12.5 п.п.` | `1.00%` | REJECTED: Category cap reached (4/4 in Sports) |
| Cardinals vs. Chiefs | Sports | NO | `96.0%` | `92.0%` | `+4.0 п.п.` | `1.00%` | EXECUTED BUY #232 ($1.00 @ 0.9200) |
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
