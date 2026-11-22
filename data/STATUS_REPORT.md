# 📊 Отчёт симулятора Polymarket (Устав Grok Bot — Демо-счёт)
**Обновлено:** `2026-11-22 21:26:53 UTC`

## 💰 Состояние виртуального портфеля
| Показатель | Значение | Правило устава |
| :--- | :--- | :--- |
| **Стартовый капитал** | `$50.00 USDC` | Не добавлять деньги |
| **Текущий баланс (Equity)** | **`$25.08 USDC`** (`-24.92$` / `-49.85%`) | Cash + Mark-to-Market по CLOB Bid |
| **Свободный кэш / В сделках** | `$25.08` / `$0.00 USDC` | До 8 открытых позиций, макс 8% банка |
| **Цель окупаемости подписки** | `$-24.92 / $60.00` (`0.0%`) | Цель: +$60.00 в месяц |
| **Просадка от пика (Текущая / Макс)** | `36.18%` / `37.84%` (Пик: `$39.29`) | Стоп-кран при просадке 40% |
| **Закрытых сделок / Win Rate** | `232` / `64.2%` | Brier Score: `0.2280` |

## 📂 Открытые позиции (0 / 8)
*Нет активных позиций.*

## 🧪 Теневая песочница (Shadow Sandbox)
| Показатель | Значение |
| :--- | :--- |
| **Виртуальный баланс (Equity)** | **`$49.31 USDC`** |
| **Свободный кэш / В сделках** | `$37.25` / `$12.06 USDC` |
| **Открытых позиций** | `5 / 5` |
| **Текущая просадка** | `25.28%` |

### Открытые позиции в песочнице (5 / 5)
| # | Рынок | Кат. | Исход | Вход (Ask VWAP) | Текущий Bid | Оценка бота | Размер ($) | Нереализ. PnL | Источник |
| :- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| #311 | Will the price of Bitcoin be above $62,000 on November  | Crypto | **NO** | `0.678` | `0.675` | `74.9%` | `$1.16` | `$-0.01` | https://www.binance.com/en/tra |
| #322 | Will Bitcoin dip to $58,000 on November 22? | Crypto | **NO** | `0.910` | `0.930` | `97.0%` | `$2.98` | `$+0.07` | https://www.binance.com/en/tra |
| #326 | Will Ethereum reach $1,800 November 16-22? | Crypto | **NO** | `0.902` | `0.895` | `96.2%` | `$2.97` | `$-0.02` | https://www.binance.com/en/tra |
| #327 | Will Bitcoin dip to $58,000 November 16-22? | Crypto | **NO** | `0.880` | `0.930` | `96.0%` | `$2.96` | `$+0.17` | https://www.binance.com/en/tra |
| #328 | Will Anthropic close below its IPO price by November 25 | Macro | **NO** | `0.630` | `0.630` | `67.5%` | `$1.78` | `$+0.00` | https://www.nasdaq.com/market- |

### Доходность по замороженным категориям (Песочница)
| Категория | Сделок | PnL | Win Rate |
| :--- | :--- | :--- | :--- |
| **Crypto** | `280` | `-$0.61` | `56%` |
| **Geopolitics** | `8` | `+$1.02` | `62%` |
| **Macro** | `10` | `+$1.72` | `70%` |
| **Other** | `20` | `-$1.65` | `40%` |
| **Weather** | `5` | `-$1.37` | `0%` |

## 🔍 Последние проверенные кандидаты и фильтр стакана CLOB
| Рынок | Кат. | Сторона | Оценка бота | Цена Ask | Перекос (Edge) | Проскальзывание CLOB | Решение |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
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
| UFC Fight Night: Jared Cannonier vs. Ikram Alisker | Sports | NO | `98.5%` | `93.0%` | `+5.5 п.п.` | `2.00%` | REJECTED: Contract price $0.930 outside sweet spot [$0.70, $0.92] |
| Will Real Madrid CF vs. RC Celta de Vigo end in a  | Sports | NO | `96.5%` | `90.0%` | `+6.5 п.п.` | `1.00%` | EXECUTED BUY #228 ($1.00 @ 0.9000) |
| UFC Fight Night: Jake Matthews vs. Tahir Abdullaye | Sports | NO | `95.0%` | `100.0%` | `-5.0 п.п.` | `100.00%` | REJECTED: Edge -5.0 pp < 2.5 pp threshold (P_est=95.0% vs AskVWAP=100.0%) |
| San Diego State vs. Boise State | Sports | NO | `94.0%` | `91.0%` | `+3.0 п.п.` | `1.00%` | EXECUTED BUY #227 ($1.00 @ 0.9100) |
