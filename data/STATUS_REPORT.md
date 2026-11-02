# 📊 Отчёт симулятора Polymarket (Устав Grok Bot — Демо-счёт)
**Обновлено:** `2026-11-02 09:52:41 UTC`

## 💰 Состояние виртуального портфеля
| Показатель | Значение | Правило устава |
| :--- | :--- | :--- |
| **Стартовый капитал** | `$50.00 USDC` | Не добавлять деньги |
| **Текущий баланс (Equity)** | **`$27.68 USDC`** (`-22.32$` / `-44.63%`) | Cash + Mark-to-Market по CLOB Bid |
| **Свободный кэш / В сделках** | `$22.50` / `$5.18 USDC` | До 8 открытых позиций, макс 8% банка |
| **Цель окупаемости подписки** | `$-22.32 / $60.00` (`0.0%`) | Цель: +$60.00 в месяц |
| **Просадка от пика (Текущая / Макс)** | `21.61%` / `24.45%` (Пик: `$35.32`) | Стоп-кран при просадке 40% |
| **Закрытых сделок / Win Rate** | `86` / `64.0%` | Brier Score: `0.2194` |

## 📂 Открытые позиции (3 / 8)
| # | Рынок | Кат. | Исход | Вход (Ask VWAP) | Текущий Bid | Оценка бота | Размер ($) | Нереализ. PnL | Источник |
| :- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| #88 | Kings vs. Mavericks | Sports | **NO** | `0.800` | `0.780` | `82.0%` | `$1.09` | `$-0.03` | https://www.nba.com/ |
| #89 | Nets vs. Knicks | Sports | **NO** | `0.890` | `0.880` | `92.0%` | `$2.21` | `$-0.02` | https://www.nba.com/ |
| #90 | Bulls vs. 76ers | Sports | **NO** | `0.830` | `0.820` | `86.0%` | `$1.96` | `$-0.02` | https://www.nba.com/ |

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
| Spread: Bears (-3.5) | Sports | NO | `97.5%` | `74.0%` | `+23.5 п.п.` | `1.00%` | REJECTED: Contract price $0.740 outside sweet spot [$0.76, $0.89] |
| Bulls vs. 76ers | Sports | NO | `86.0%` | `83.0%` | `+3.0 п.п.` | `1.00%` | EXECUTED BUY #90 ($1.96 @ 0.8300) |
| Spread: Seahawks (-3.5) | Sports | NO | `97.5%` | `53.0%` | `+44.5 п.п.` | `1.00%` | REJECTED: Contract price $0.530 outside sweet spot [$0.76, $0.89] |
| Counter-Strike: FURIA vs FaZe - Map 1 Winner | Sports | YES | `1.5%` | `100.0%` | `-98.5 п.п.` | `100.00%` | REJECTED: Edge -98.5 pp < 2 pp threshold (P_est=1.5% vs AskVWAP=100.0%) |
| Map Handicap: FURIA (-1.5) vs FaZe (+1.5) | Sports | YES | `1.5%` | `100.0%` | `-98.5 п.п.` | `100.00%` | REJECTED: Edge -98.5 pp < 2 pp threshold (P_est=1.5% vs AskVWAP=100.0%) |
| Counter-Strike: 9z vs BetBoom Team (BO3) - IEM Bei | Sports | YES | `1.5%` | `7.0%` | `-5.5 п.п.` | `1.00%` | REJECTED: Edge -5.5 pp < 2 pp threshold (P_est=1.5% vs AskVWAP=7.0%) |
| Spread: Bears (-3.5) | Sports | NO | `97.5%` | `74.0%` | `+23.5 п.п.` | `1.00%` | REJECTED: Contract price $0.740 outside sweet spot [$0.76, $0.89] |
| Spread: Seahawks (-3.5) | Sports | NO | `97.5%` | `54.0%` | `+43.5 п.п.` | `1.00%` | REJECTED: Contract price $0.540 outside sweet spot [$0.76, $0.89] |
| Spread: Bears (-3.5) | Sports | NO | `97.5%` | `74.0%` | `+23.5 п.п.` | `1.00%` | REJECTED: Contract price $0.740 outside sweet spot [$0.76, $0.89] |
| Spread: Seahawks (-3.5) | Sports | NO | `97.5%` | `54.0%` | `+43.5 п.п.` | `1.00%` | REJECTED: Contract price $0.540 outside sweet spot [$0.76, $0.89] |
| Spread: Bears (-3.5) | Sports | NO | `97.5%` | `74.0%` | `+23.5 п.п.` | `1.00%` | REJECTED: Contract price $0.740 outside sweet spot [$0.76, $0.89] |
| Spread: Seahawks (-3.5) | Sports | NO | `97.5%` | `54.0%` | `+43.5 п.п.` | `1.00%` | REJECTED: Contract price $0.540 outside sweet spot [$0.76, $0.89] |
| Nets vs. Knicks | Sports | NO | `92.0%` | `89.0%` | `+3.0 п.п.` | `1.00%` | EXECUTED BUY #89 ($2.21 @ 0.8900) |
| Spread: Lakers (-4.5) | Sports | NO | `97.5%` | `56.0%` | `+41.5 п.п.` | `1.00%` | REJECTED: Contract price $0.560 outside sweet spot [$0.76, $0.89] |
| Spread: Seahawks (-3.5) | Sports | NO | `97.5%` | `54.0%` | `+43.5 п.п.` | `1.00%` | REJECTED: Contract price $0.540 outside sweet spot [$0.76, $0.89] |
| Kings vs. Mavericks | Sports | NO | `82.0%` | `80.0%` | `+2.0 п.п.` | `1.00%` | EXECUTED BUY #88 ($1.09 @ 0.8000) |
| Counter-Strike: 100 Thieves vs Wildcard - Map 2 Wi | Sports | NO | `1.5%` | `100.0%` | `-98.5 п.п.` | `100.00%` | REJECTED: Edge -98.5 pp < 2 pp threshold (P_est=1.5% vs AskVWAP=100.0%) |
| Counter-Strike: BESTIA vs BARCA (BO3) - FiReSPORTS | Sports | NO | `1.5%` | `100.0%` | `-98.5 п.п.` | `100.00%` | REJECTED: Edge -98.5 pp < 2 pp threshold (P_est=1.5% vs AskVWAP=100.0%) |
