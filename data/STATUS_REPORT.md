# 📊 Отчёт симулятора Polymarket (Устав Grok Bot — Демо-счёт)
**Обновлено:** `2026-11-23 23:30:57 UTC`

## 💰 Состояние виртуального портфеля
| Показатель | Значение | Правило устава |
| :--- | :--- | :--- |
| **Стартовый капитал** | `$50.00 USDC` | Не добавлять деньги |
| **Текущий баланс (Equity)** | **`$25.05 USDC`** (`-24.95$` / `-49.89%`) | Cash + Mark-to-Market по CLOB Bid |
| **Свободный кэш / В сделках** | `$24.08` / `$0.98 USDC` | До 8 открытых позиций, макс 8% банка |
| **Цель окупаемости подписки** | `$-24.95 / $60.00` (`0.0%`) | Цель: +$60.00 в месяц |
| **Просадка от пика (Текущая / Макс)** | `36.24%` / `37.84%` (Пик: `$39.29`) | Стоп-кран при просадке 40% |
| **Закрытых сделок / Win Rate** | `232` / `64.2%` | Brier Score: `0.2280` |

## 📂 Открытые позиции (1 / 8)
| # | Рынок | Кат. | Исход | Вход (Ask VWAP) | Текущий Bid | Оценка бота | Размер ($) | Нереализ. PnL | Источник |
| :- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| #234 | Spread: Commanders (-3.5) | Sports | **NO** | `0.860` | `0.840` | `97.5%` | `$1.00` | `$-0.02` | https://www.nfl.com/scores |

## 🧪 Теневая песочница (Shadow Sandbox)
| Показатель | Значение |
| :--- | :--- |
| **Виртуальный баланс (Equity)** | **`$43.31 USDC`** |
| **Свободный кэш / В сделках** | `$38.09` / `$5.22 USDC` |
| **Открытых позиций** | `2 / 5` |
| **Текущая просадка** | `34.37%` |

### Открытые позиции в песочнице (2 / 5)
| # | Рынок | Кат. | Исход | Вход (Ask VWAP) | Текущий Bid | Оценка бота | Размер ($) | Нереализ. PnL | Источник |
| :- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| #362 | Will the price of Bitcoin be above $64,000 on November  | Crypto | **NO** | `0.913` | `0.895` | `95.0%` | `$2.57` | `$-0.05` | https://www.binance.com/en/tra |
| #364 | Will Bitcoin dip to $59,000 on November 23? | Crypto | **NO** | `0.903` | `0.961` | `98.5%` | `$2.54` | `$+0.16` | https://www.binance.com/en/tra |

### Доходность по замороженным категориям (Песочница)
| Категория | Сделок | PnL | Win Rate |
| :--- | :--- | :--- | :--- |
| **Crypto** | `314` | `-$5.82` | `54%` |
| **Geopolitics** | `8` | `+$1.02` | `62%` |
| **Macro** | `14` | `+$1.66` | `64%` |
| **Other** | `21` | `-$2.29` | `38%` |
| **Weather** | `5` | `-$1.37` | `0%` |

## 🔍 Последние проверенные кандидаты и фильтр стакана CLOB
| Рынок | Кат. | Сторона | Оценка бота | Цена Ask | Перекос (Edge) | Проскальзывание CLOB | Решение |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
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
| Spread: Titans (-3.5) | Sports | NO | `97.5%` | `85.0%` | `+12.5 п.п.` | `1.00%` | REJECTED: Category cap reached (4/4 in Sports) |
| Cardinals vs. Chiefs | Sports | NO | `96.0%` | `92.0%` | `+4.0 п.п.` | `1.00%` | EXECUTED BUY #232 ($1.00 @ 0.9200) |
| Will FC Barcelona vs. Villarreal CF end in a draw? | Sports | NO | `96.5%` | `90.0%` | `+6.5 п.п.` | `1.00%` | EXECUTED BUY #231 ($1.00 @ 0.9000) |
| Spread: Manchester United FC (-1.5) | Sports | NO | `95.0%` | `92.0%` | `+3.0 п.п.` | `1.00%` | EXECUTED BUY #230 ($1.00 @ 0.9200) |
| SMU vs. Notre Dame | Sports | NO | `94.0%` | `91.0%` | `+3.0 п.п.` | `1.00%` | EXECUTED BUY #229 ($1.00 @ 0.9100) |
| UFC Fight Night: Brian Ortega vs. Dan Hooker (Ligh | Sports | NO | `95.0%` | `99.0%` | `-4.0 п.п.` | `1.00%` | REJECTED: Edge -4.0 pp < 2.5 pp threshold (P_est=95.0% vs AskVWAP=99.0%) |
