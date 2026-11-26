# 📊 Отчёт симулятора Polymarket (Устав Grok Bot — Демо-счёт)
**Обновлено:** `2026-11-26 06:01:13 UTC`

## 💰 Состояние виртуального портфеля
| Показатель | Значение | Правило устава |
| :--- | :--- | :--- |
| **Стартовый капитал** | `$50.00 USDC` | Не добавлять деньги |
| **Текущий баланс (Equity)** | **`$24.57 USDC`** (`-25.43$` / `-50.85%`) | Cash + Mark-to-Market по CLOB Bid |
| **Свободный кэш / В сделках** | `$24.57` / `$0.00 USDC` | До 8 открытых позиций, макс 8% банка |
| **Цель окупаемости подписки** | `$-25.43 / $60.00` (`0.0%`) | Цель: +$60.00 в месяц |
| **Просадка от пика (Текущая / Макс)** | `37.46%` / `37.84%` (Пик: `$39.29`) | Стоп-кран при просадке 40% |
| **Закрытых сделок / Win Rate** | `239` / `64.4%` | Brier Score: `0.2280` |

## 📂 Открытые позиции (0 / 8)
*Нет активных позиций.*

## 🧪 Теневая песочница (Shadow Sandbox)
| Показатель | Значение |
| :--- | :--- |
| **Виртуальный баланс (Equity)** | **`$39.30 USDC`** |
| **Свободный кэш / В сделках** | `$39.30` / `$0.00 USDC` |
| **Открытых позиций** | `0 / 5` |
| **Текущая просадка** | `40.45%` |

### Доходность по замороженным категориям (Песочница)
| Категория | Сделок | PnL | Win Rate |
| :--- | :--- | :--- | :--- |
| **Crypto** | `393` | `-$10.12` | `53%` |
| **Geopolitics** | `8` | `+$1.02` | `62%` |
| **Macro** | `20` | `+$1.97` | `65%` |
| **Other** | `22` | `-$2.20` | `41%` |
| **Weather** | `5` | `-$1.37` | `0%` |

## 🔍 Последние проверенные кандидаты и фильтр стакана CLOB
| Рынок | Кат. | Сторона | Оценка бота | Цена Ask | Перекос (Edge) | Проскальзывание CLOB | Решение |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Exact Score: FC Internazionale Milano 3 - 1 VfB St | Sports | NO | `98.5%` | `92.0%` | `+6.5 п.п.` | `1.00%` | EXECUTED BUY #240 ($1.00 @ 0.9200) |
| Exact Score: Sabah FK 0 - 4 FC Barcelona? | Sports | NO | `98.5%` | `91.0%` | `+7.5 п.п.` | `1.00%` | EXECUTED BUY #239 ($1.00 @ 0.9100) |
| Exact Score: Sabah FK 0 - 3 FC Barcelona? | Sports | NO | `98.5%` | `91.0%` | `+7.5 п.п.` | `1.00%` | EXECUTED BUY #238 ($1.00 @ 0.9100) |
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
