# 📊 Отчёт симулятора Polymarket (Устав Grok Bot — Демо-счёт)
**Обновлено:** `2026-11-24 21:10:20 UTC`

## 💰 Состояние виртуального портфеля
| Показатель | Значение | Правило устава |
| :--- | :--- | :--- |
| **Стартовый капитал** | `$50.00 USDC` | Не добавлять деньги |
| **Текущий баланс (Equity)** | **`$25.19 USDC`** (`-24.81$` / `-49.61%`) | Cash + Mark-to-Market по CLOB Bid |
| **Свободный кэш / В сделках** | `$22.24` / `$2.96 USDC` | До 8 открытых позиций, макс 8% банка |
| **Цель окупаемости подписки** | `$-24.81 / $60.00` (`0.0%`) | Цель: +$60.00 в месяц |
| **Просадка от пика (Текущая / Макс)** | `35.88%` / `37.84%` (Пик: `$39.29`) | Стоп-кран при просадке 40% |
| **Закрытых сделок / Win Rate** | `233` / `64.4%` | Brier Score: `0.2280` |

## 📂 Открытые позиции (3 / 8)
| # | Рынок | Кат. | Исход | Вход (Ask VWAP) | Текущий Bid | Оценка бота | Размер ($) | Нереализ. PnL | Источник |
| :- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| #235 | Will ŠK Slovan Bratislava win on 2026-11-24? | Sports | **NO** | `0.920` | `0.950` | `98.0%` | `$1.00` | `$+0.03` | https://www.uefa.com/ |
| #236 | Will AEK win on 2026-11-24? | Sports | **NO** | `0.920` | `0.890` | `94.0%` | `$1.00` | `$-0.03` | https://www.uefa.com/ |
| #237 | Will SSC Napoli win on 2026-11-24? | Sports | **NO** | `0.910` | `0.870` | `94.0%` | `$1.00` | `$-0.04` | https://www.uefa.com/ |

## 🧪 Теневая песочница (Shadow Sandbox)
| Показатель | Значение |
| :--- | :--- |
| **Виртуальный баланс (Equity)** | **`$43.85 USDC`** |
| **Свободный кэш / В сделках** | `$39.40` / `$4.44 USDC` |
| **Открытых позиций** | `2 / 5` |
| **Текущая просадка** | `33.55%` |

### Открытые позиции в песочнице (2 / 5)
| # | Рынок | Кат. | Исход | Вход (Ask VWAP) | Текущий Bid | Оценка бота | Размер ($) | Нереализ. PnL | Источник |
| :- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| #396 | Will the price of Bitcoin be above $62,000 on November  | Crypto | **NO** | `0.860` | `0.900` | `93.5%` | `$1.80` | `$+0.08` | https://www.binance.com/en/tra |
| #402 | Will Bitcoin dip to $59,000 on November 24? | Crypto | **YES** | `0.380` | `0.370` | `53.6%` | `$2.63` | `$-0.07` | https://www.binance.com/en/tra |

### Доходность по замороженным категориям (Песочница)
| Категория | Сделок | PnL | Win Rate |
| :--- | :--- | :--- | :--- |
| **Crypto** | `346` | `-$5.50` | `54%` |
| **Geopolitics** | `8` | `+$1.02` | `62%` |
| **Macro** | `20` | `+$1.97` | `65%` |
| **Other** | `21` | `-$2.29` | `38%` |
| **Weather** | `5` | `-$1.37` | `0%` |

## 🔍 Последние проверенные кандидаты и фильтр стакана CLOB
| Рынок | Кат. | Сторона | Оценка бота | Цена Ask | Перекос (Edge) | Проскальзывание CLOB | Решение |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Will Elon Musk post <40 tweets from November 23 to | Geopolitics | NO | `96.2%` | `91.9%` | `+4.2 п.п.` | `0.50%` | REJECTED: Social Mention Count Guard: Tweet/post count bracket markets prohibited (burst variance trap) |
| Will SSC Napoli win on 2026-11-24? | Sports | NO | `94.0%` | `91.0%` | `+3.0 п.п.` | `1.00%` | EXECUTED BUY #237 ($1.00 @ 0.9100) |
| Will AEK win on 2026-11-24? | Sports | NO | `95.0%` | `92.0%` | `+3.0 п.п.` | `1.00%` | EXECUTED BUY #236 ($1.00 @ 0.9200) |
| Will Elon Musk post <40 tweets from November 23 to | Geopolitics | NO | `93.5%` | `89.1%` | `+4.5 п.п.` | `0.10%` | REJECTED: Social Mention Count Guard: Tweet/post count bracket markets prohibited (burst variance trap) |
| Will Elon Musk post <40 tweets from November 23 to | Geopolitics | NO | `94.5%` | `90.1%` | `+4.3 п.п.` | `1.50%` | REJECTED: Social Mention Count Guard: Tweet/post count bracket markets prohibited (burst variance trap) |
| Will ŠK Slovan Bratislava win on 2026-11-24? | Sports | NO | `95.0%` | `92.0%` | `+3.0 п.п.` | `1.00%` | EXECUTED BUY #235 ($1.00 @ 0.9200) |
| Spread: Commanders (-3.5) | Sports | NO | `97.5%` | `86.0%` | `+11.5 п.п.` | `1.00%` | EXECUTED BUY #234 ($1.00 @ 0.8600) |
| Will Elon Musk post 260-279 tweets from November 1 | Geopolitics | NO | `95.2%` | `91.1%` | `+4.1 п.п.` | `0.10%` | REJECTED: Social Mention Count Guard: Tweet/post count bracket markets prohibited (burst variance trap) |
| Will Elon Musk post 340-359 tweets from November 1 | Geopolitics | NO | `95.5%` | `89.4%` | `+6.1 п.п.` | `1.00%` | REJECTED: Social Mention Count Guard: Tweet/post count bracket markets prohibited (burst variance trap) |
| Will Elon Musk post 260-279 tweets from November 1 | Geopolitics | NO | `98.0%` | `93.5%` | `+4.5 п.п.` | `0.20%` | REJECTED: Contract price $0.935 outside sweet spot [$0.70, $0.92] |
| Spread: Steelers (-4.5) | Sports | NO | `97.5%` | `91.0%` | `+6.5 п.п.` | `1.00%` | REJECTED: Duplicate underlying event (sports:steelers:nodate) |
| Will Alexander Zverev win the 2026 Nitto ATP Final | Sports | NO | `94.0%` | `80.0%` | `+14.0 п.п.` | `13.90%` | REJECTED: Net EV edge +0.1 pp < 1.5 pp (Gross +14.0 pp - Slippage 13.90%) |
| Will Carlos Alcaraz win the 2026 Nitto ATP Finals? | Sports | YES | `93.8%` | `79.9%` | `+13.9 п.п.` | `8.30%` | REJECTED: CLOB round-trip slippage 8.30% > 2.0% limit |
| Spread: Steelers (-4.5) | Sports | NO | `97.5%` | `89.0%` | `+8.5 п.п.` | `1.00%` | REJECTED: Duplicate underlying event (sports:steelers:nodate) |
| Spread: Steelers (-4.5) | Sports | NO | `97.5%` | `93.0%` | `+4.5 п.п.` | `2.00%` | REJECTED: Contract price $0.930 outside sweet spot [$0.70, $0.92] |
| Spread: Steelers (-4.5) | Sports | NO | `97.5%` | `93.0%` | `+4.5 п.п.` | `2.00%` | REJECTED: Contract price $0.930 outside sweet spot [$0.70, $0.92] |
| Spread: Steelers (-4.5) | Sports | NO | `97.5%` | `89.0%` | `+8.5 п.п.` | `1.00%` | REJECTED: Duplicate underlying event (sports:steelers:nodate) |
| Spread: Steelers (-3.5) | Sports | NO | `97.5%` | `86.0%` | `+11.5 п.п.` | `1.00%` | EXECUTED BUY #233 ($1.00 @ 0.8600) |
