# 📊 Отчёт симулятора Polymarket (Устав Grok Bot — Демо-счёт)
**Обновлено:** `2026-11-09 09:19:28 UTC`

## 💰 Состояние виртуального портфеля
| Показатель | Значение | Правило устава |
| :--- | :--- | :--- |
| **Стартовый капитал** | `$50.00 USDC` | Не добавлять деньги |
| **Текущий баланс (Equity)** | **`$39.28 USDC`** (`-10.72$` / `-21.44%`) | Cash + Mark-to-Market по CLOB Bid |
| **Свободный кэш / В сделках** | `$36.42` / `$2.86 USDC` | До 8 открытых позиций, макс 8% банка |
| **Цель окупаемости подписки** | `$-10.72 / $60.00` (`0.0%`) | Цель: +$60.00 в месяц |
| **Просадка от пика (Текущая / Макс)** | `0.00%` / `24.45%` (Пик: `$39.28`) | Стоп-кран при просадке 40% |
| **Закрытых сделок / Win Rate** | `99` / `84.8%` | Brier Score: `0.1849` |

## 📂 Открытые позиции (1 / 8)
| # | Рынок | Кат. | Исход | Вход (Ask VWAP) | Текущий Bid | Оценка бота | Размер ($) | Нереализ. PnL | Источник |
| :- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| #115 | Will FC RFS win on 2026-11-08? | Sports | **NO** | `0.919` | `0.982` | `98.5%` | `$2.68` | `$+0.18` | https://www.virsliga.lv/ |

## 🧪 Теневая песочница (Shadow Sandbox)
| Показатель | Значение |
| :--- | :--- |
| **Виртуальный баланс (Equity)** | **`$50.00 USDC`** |
| **Свободный кэш / В сделках** | `$50.00` / `$0.00 USDC` |
| **Открытых позиций** | `0 / 5` |
| **Текущая просадка** | `0.00%` |

### Доходность по замороженным категориям (Песочница)
*Теневые сделки пока не закрыты (накапливается история).*

## 🔍 Последние проверенные кандидаты и фильтр стакана CLOB
| Рынок | Кат. | Сторона | Оценка бота | Цена Ask | Перекос (Edge) | Проскальзывание CLOB | Решение |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Spread: Rockets (-4.5) | Sports | NO | `97.5%` | `37.0%` | `+60.5 п.п.` | `2.00%` | REJECTED: Contract price $0.370 outside sweet spot [$0.76, $0.92] |
| Spread: Bills (-3.5) | Sports | NO | `97.5%` | `54.0%` | `+43.5 п.п.` | `1.00%` | REJECTED: Contract price $0.540 outside sweet spot [$0.76, $0.92] |
| Spread: Rockets (-4.5) | Sports | NO | `97.5%` | `37.0%` | `+60.5 п.п.` | `2.00%` | REJECTED: Contract price $0.370 outside sweet spot [$0.76, $0.92] |
| Spread: Bills (-3.5) | Sports | NO | `97.5%` | `54.0%` | `+43.5 п.п.` | `1.00%` | REJECTED: Contract price $0.540 outside sweet spot [$0.76, $0.92] |
| Spread: Rockets (-4.5) | Sports | NO | `97.5%` | `37.0%` | `+60.5 п.п.` | `2.00%` | REJECTED: Contract price $0.370 outside sweet spot [$0.76, $0.92] |
| Spread: Bills (-3.5) | Sports | NO | `97.5%` | `54.0%` | `+43.5 п.п.` | `1.00%` | REJECTED: Contract price $0.540 outside sweet spot [$0.76, $0.92] |
| Spread: Rockets (-4.5) | Sports | NO | `97.5%` | `37.0%` | `+60.5 п.п.` | `2.00%` | REJECTED: Contract price $0.370 outside sweet spot [$0.76, $0.92] |
| Spread: Bills (-3.5) | Sports | NO | `97.5%` | `54.0%` | `+43.5 п.п.` | `1.00%` | REJECTED: Contract price $0.540 outside sweet spot [$0.76, $0.92] |
| Spread: Rockets (-4.5) | Sports | NO | `97.5%` | `36.0%` | `+61.5 п.п.` | `1.00%` | REJECTED: Contract price $0.360 outside sweet spot [$0.76, $0.92] |
| Spread: Bills (-3.5) | Sports | NO | `97.5%` | `54.0%` | `+43.5 п.п.` | `1.00%` | REJECTED: Contract price $0.540 outside sweet spot [$0.76, $0.92] |
| Spread: Rockets (-4.5) | Sports | NO | `97.5%` | `36.0%` | `+61.5 п.п.` | `1.00%` | REJECTED: Contract price $0.360 outside sweet spot [$0.76, $0.92] |
| Spread: Bills (-3.5) | Sports | NO | `97.5%` | `54.0%` | `+43.5 п.п.` | `1.00%` | REJECTED: Contract price $0.540 outside sweet spot [$0.76, $0.92] |
| Spread: Rockets (-4.5) | Sports | NO | `97.5%` | `36.0%` | `+61.5 п.п.` | `1.00%` | REJECTED: Contract price $0.360 outside sweet spot [$0.76, $0.92] |
| Spread: Bills (-3.5) | Sports | NO | `97.5%` | `54.0%` | `+43.5 п.п.` | `1.00%` | REJECTED: Contract price $0.540 outside sweet spot [$0.76, $0.92] |
| Spread: Rockets (-4.5) | Sports | NO | `97.5%` | `36.0%` | `+61.5 п.п.` | `1.00%` | REJECTED: Contract price $0.360 outside sweet spot [$0.76, $0.92] |
| Spread: Bills (-3.5) | Sports | NO | `97.5%` | `54.0%` | `+43.5 п.п.` | `1.00%` | REJECTED: Contract price $0.540 outside sweet spot [$0.76, $0.92] |
| Spread: Rockets (-4.5) | Sports | NO | `97.5%` | `36.0%` | `+61.5 п.п.` | `1.00%` | REJECTED: Contract price $0.360 outside sweet spot [$0.76, $0.92] |
| Spread: Bills (-3.5) | Sports | NO | `97.5%` | `54.0%` | `+43.5 п.п.` | `1.00%` | REJECTED: Contract price $0.540 outside sweet spot [$0.76, $0.92] |
