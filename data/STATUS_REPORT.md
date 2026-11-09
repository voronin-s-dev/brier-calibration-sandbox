# 📊 Отчёт симулятора Polymarket (Устав Grok Bot — Демо-счёт)
**Обновлено:** `2026-11-09 01:19:22 UTC`

## 💰 Состояние виртуального портфеля
| Показатель | Значение | Правило устава |
| :--- | :--- | :--- |
| **Стартовый капитал** | `$50.00 USDC` | Не добавлять деньги |
| **Текущий баланс (Equity)** | **`$37.97 USDC`** (`-12.03$` / `-24.06%`) | Cash + Mark-to-Market по CLOB Bid |
| **Свободный кэш / В сделках** | `$26.19` / `$11.78 USDC` | До 8 открытых позиций, макс 8% банка |
| **Цель окупаемости подписки** | `$-12.03 / $60.00` (`0.0%`) | Цель: +$60.00 в месяц |
| **Просадка от пика (Текущая / Макс)** | `0.09%` / `24.45%` (Пик: `$38.00`) | Стоп-кран при просадке 40% |
| **Закрытых сделок / Win Rate** | `96` / `84.4%` | Brier Score: `0.1849` |

## 📂 Открытые позиции (4 / 8)
| # | Рынок | Кат. | Исход | Вход (Ask VWAP) | Текущий Bid | Оценка бота | Размер ($) | Нереализ. PnL | Источник |
| :- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| #115 | Will FC RFS win on 2026-11-08? | Sports | **NO** | `0.919` | `0.953` | `98.5%` | `$2.68` | `$+0.10` | https://www.virsliga.lv/ |
| #121 | Spread: Buccaneers (-3.5) | Sports | **NO** | `0.810` | `0.810` | `97.5%` | `$2.83` | `$-0.00` | https://www.nfl.com/scores |
| #123 | LoL: Bilibili Gaming vs T1 (BO5) - Worlds Playoffs | Sports | **YES** | `0.900` | `0.940` | `98.0%` | `$3.03` | `$+0.13` | https://gol.gg/esports/home |
| #124 | Games Total: O/U 4.5 | Sports | **NO** | `0.900` | `0.890` | `94.0%` | `$3.04` | `$-0.03` | https://gol.gg/esports/home |

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
| Spread: Rockets (-4.5) | Sports | NO | `97.5%` | `42.1%` | `+55.4 п.п.` | `14.15%` | REJECTED: Contract price $0.421 outside sweet spot [$0.76, $0.92] |
| Spread: Bills (-4.5) | Sports | NO | `97.5%` | `57.0%` | `+40.5 п.п.` | `1.00%` | REJECTED: Contract price $0.570 outside sweet spot [$0.76, $0.92] |
| Spread: Bills (-3.5) | Sports | NO | `97.5%` | `55.0%` | `+42.5 п.п.` | `1.00%` | REJECTED: Contract price $0.550 outside sweet spot [$0.76, $0.92] |
| Call of Duty: Paris Gentle Mates vs Cloud9 New Yor | Sports | NO | `1.5%` | `100.0%` | `-98.5 п.п.` | `100.00%` | REJECTED: Edge -98.5 pp < 2 pp threshold (P_est=1.5% vs AskVWAP=100.0%) |
| Games Total: O/U 3.5 | Sports | NO | `1.5%` | `100.0%` | `-98.5 п.п.` | `100.00%` | REJECTED: Edge -98.5 pp < 2 pp threshold (P_est=1.5% vs AskVWAP=100.0%) |
| Game Handicap: BLG (-2.5) vs T1 (+2.5) | Sports | YES | `1.5%` | `100.0%` | `-98.5 п.п.` | `100.00%` | REJECTED: Edge -98.5 pp < 2 pp threshold (P_est=1.5% vs AskVWAP=100.0%) |
| LoL: Bilibili Gaming vs T1 - Game 3 Winner | Sports | NO | `1.5%` | `100.0%` | `-98.5 п.п.` | `100.00%` | REJECTED: Edge -98.5 pp < 2 pp threshold (P_est=1.5% vs AskVWAP=100.0%) |
| LoL: Bilibili Gaming vs T1 - Game 2 Winner | Sports | YES | `1.5%` | `100.0%` | `-98.5 п.п.` | `100.00%` | REJECTED: Edge -98.5 pp < 2 pp threshold (P_est=1.5% vs AskVWAP=100.0%) |
| Games Total: O/U 4.5 | Sports | NO | `94.0%` | `90.0%` | `+4.0 п.п.` | `1.00%` | EXECUTED BUY #124 ($3.04 @ 0.9000) |
| Spread: Rockets (-4.5) | Sports | NO | `97.5%` | `42.1%` | `+55.4 п.п.` | `13.42%` | REJECTED: Contract price $0.421 outside sweet spot [$0.76, $0.92] |
| Spread: Bills (-4.5) | Sports | NO | `97.5%` | `57.0%` | `+40.5 п.п.` | `1.00%` | REJECTED: Contract price $0.570 outside sweet spot [$0.76, $0.92] |
| Spread: Pelicans (-3.5) | Sports | NO | `97.5%` | `57.0%` | `+40.5 п.п.` | `1.00%` | REJECTED: Contract price $0.570 outside sweet spot [$0.76, $0.92] |
| Spread: Bills (-3.5) | Sports | NO | `97.5%` | `55.0%` | `+42.5 п.п.` | `1.00%` | REJECTED: Contract price $0.550 outside sweet spot [$0.76, $0.92] |
| Call of Duty: Paris Gentle Mates vs Cloud9 New Yor | Sports | NO | `1.5%` | `100.0%` | `-98.5 п.п.` | `100.00%` | REJECTED: Edge -98.5 pp < 2 pp threshold (P_est=1.5% vs AskVWAP=100.0%) |
| Games Total: O/U 3.5 | Sports | NO | `1.5%` | `100.0%` | `-98.5 п.п.` | `100.00%` | REJECTED: Edge -98.5 pp < 2 pp threshold (P_est=1.5% vs AskVWAP=100.0%) |
| Game Handicap: BLG (-2.5) vs T1 (+2.5) | Sports | YES | `1.5%` | `100.0%` | `-98.5 п.п.` | `100.00%` | REJECTED: Edge -98.5 pp < 2 pp threshold (P_est=1.5% vs AskVWAP=100.0%) |
| LoL: Bilibili Gaming vs T1 - Game 3 Winner | Sports | NO | `1.5%` | `100.0%` | `-98.5 п.п.` | `100.00%` | REJECTED: Edge -98.5 pp < 2 pp threshold (P_est=1.5% vs AskVWAP=100.0%) |
| LoL: Bilibili Gaming vs T1 - Game 2 Winner | Sports | YES | `1.5%` | `100.0%` | `-98.5 п.п.` | `100.00%` | REJECTED: Edge -98.5 pp < 2 pp threshold (P_est=1.5% vs AskVWAP=100.0%) |
