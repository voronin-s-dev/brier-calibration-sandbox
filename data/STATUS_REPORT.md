# 📊 Отчёт симулятора Polymarket (Устав Grok Bot — Демо-счёт)
**Обновлено:** `2026-11-03 18:01:37 UTC`

## 💰 Состояние виртуального портфеля
| Показатель | Значение | Правило устава |
| :--- | :--- | :--- |
| **Стартовый капитал** | `$50.00 USDC` | Не добавлять деньги |
| **Текущий баланс (Equity)** | **`$27.67 USDC`** (`-22.33$` / `-44.67%`) | Cash + Mark-to-Market по CLOB Bid |
| **Свободный кэш / В сделках** | `$17.27` / `$10.39 USDC` | До 8 открытых позиций, макс 8% банка |
| **Цель окупаемости подписки** | `$-22.33 / $60.00` (`0.0%`) | Цель: +$60.00 в месяц |
| **Просадка от пика (Текущая / Макс)** | `21.66%` / `24.45%` (Пик: `$35.32`) | Стоп-кран при просадке 40% |
| **Закрытых сделок / Win Rate** | `90` / `64.4%` | Brier Score: `0.2274` |

## 📂 Открытые позиции (5 / 8)
| # | Рынок | Кат. | Исход | Вход (Ask VWAP) | Текущий Bid | Оценка бота | Размер ($) | Нереализ. PnL | Источник |
| :- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| #91 | Will Villarreal CF win on 2026-11-03? | Sports | **NO** | `0.800` | `0.790` | `83.0%` | `$1.66` | `$-0.02` | https://www.uefa.com/ |
| #93 | Will Aston Villa FC win on 2026-11-03? | Sports | **NO** | `0.910` | `0.890` | `94.0%` | `$2.22` | `$-0.05` | https://www.uefa.com/ |
| #94 | Spread: Villarreal CF (-1.5) | Sports | **NO** | `0.920` | `0.910` | `95.0%` | `$2.22` | `$-0.02` | https://www.uefa.com/ |
| #95 | LoL: Gen.G vs LYON (BO5) - Worlds Playoffs | Sports | **YES** | `0.920` | `0.910` | `95.0%` | `$2.22` | `$-0.02` | https://gol.gg/esports/home |
| #96 | Spread: FC Barcelona (-3.5) | Sports | **NO** | `0.800` | `0.790` | `97.5%` | `$2.22` | `$-0.03` | https://www.uefa.com/ |

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
| Counter-Strike: Walczaki vs SINQU (BO3) - NODWIN C | Sports | NO | `1.5%` | `100.0%` | `-98.5 п.п.` | `100.00%` | REJECTED: Edge -98.5 pp < 2 pp threshold (P_est=1.5% vs AskVWAP=100.0%) |
| Dota 2: Nemiga Gaming vs CyberHero (BO3) - EPL Mas | Sports | YES | `1.5%` | `100.0%` | `-98.5 п.п.` | `100.00%` | REJECTED: Edge -98.5 pp < 2 pp threshold (P_est=1.5% vs AskVWAP=100.0%) |
| Dota 2: Nemiga Gaming vs CyberHero (BO3) - EPL Mas | Sports | YES | `1.5%` | `100.0%` | `-98.5 п.п.` | `100.00%` | REJECTED: Edge -98.5 pp < 2 pp threshold (P_est=1.5% vs AskVWAP=100.0%) |
| Spread: FC Barcelona (-3.5) | Sports | NO | `97.5%` | `80.0%` | `+17.5 п.п.` | `1.00%` | EXECUTED BUY #96 ($2.22 @ 0.8000) |
| Dota 2: Nemiga Gaming vs CyberHero (BO3) - EPL Mas | Sports | YES | `1.5%` | `100.0%` | `-98.5 п.п.` | `100.00%` | REJECTED: Edge -98.5 pp < 2 pp threshold (P_est=1.5% vs AskVWAP=100.0%) |
| Counter-Strike: Falcons Force vs maybe - Map 1 Win | Sports | NO | `1.5%` | `100.0%` | `-98.5 п.п.` | `100.00%` | REJECTED: Edge -98.5 pp < 2 pp threshold (P_est=1.5% vs AskVWAP=100.0%) |
| Dota 2: rostikfacekid TEAM vs LenS Team - Game 2 W | Sports | YES | `1.5%` | `100.0%` | `-98.5 п.п.` | `100.00%` | REJECTED: Edge -98.5 pp < 2 pp threshold (P_est=1.5% vs AskVWAP=100.0%) |
| Dota 2: LEGION vs OG (BO3) - EPL Masters Playoffs | Sports | YES | `1.5%` | `100.0%` | `-98.5 п.п.` | `100.00%` | REJECTED: Edge -98.5 pp < 2 pp threshold (P_est=1.5% vs AskVWAP=100.0%) |
| Counter-Strike: Falcons Force vs maybe - Map 1 Win | Sports | NO | `1.5%` | `100.0%` | `-98.5 п.п.` | `100.00%` | REJECTED: Edge -98.5 pp < 2 pp threshold (P_est=1.5% vs AskVWAP=100.0%) |
| Dota 2: rostikfacekid TEAM vs LenS Team - Game 2 W | Sports | YES | `1.5%` | `100.0%` | `-98.5 п.п.` | `100.00%` | REJECTED: Edge -98.5 pp < 2 pp threshold (P_est=1.5% vs AskVWAP=100.0%) |
| Dota 2: LEGION vs OG (BO3) - EPL Masters Playoffs | Sports | YES | `1.5%` | `100.0%` | `-98.5 п.п.` | `100.00%` | REJECTED: Edge -98.5 pp < 2 pp threshold (P_est=1.5% vs AskVWAP=100.0%) |
| Counter-Strike: FURIA vs Natus Vincere (BO3) - IEM | Sports | NO | `1.5%` | `100.0%` | `-98.5 п.п.` | `100.00%` | REJECTED: Edge -98.5 pp < 2 pp threshold (P_est=1.5% vs AskVWAP=100.0%) |
| Counter-Strike: Falcons Force vs maybe - Map 1 Win | Sports | NO | `1.5%` | `100.0%` | `-98.5 п.п.` | `100.00%` | REJECTED: Edge -98.5 pp < 2 pp threshold (P_est=1.5% vs AskVWAP=100.0%) |
| Dota 2: rostikfacekid TEAM vs LenS Team - Game 2 W | Sports | YES | `1.5%` | `100.0%` | `-98.5 п.п.` | `100.00%` | REJECTED: Edge -98.5 pp < 2 pp threshold (P_est=1.5% vs AskVWAP=100.0%) |
| Dota 2: LEGION vs OG (BO3) - EPL Masters Playoffs | Sports | YES | `1.5%` | `100.0%` | `-98.5 п.п.` | `100.00%` | REJECTED: Edge -98.5 pp < 2 pp threshold (P_est=1.5% vs AskVWAP=100.0%) |
| Counter-Strike: FURIA vs Natus Vincere (BO3) - IEM | Sports | NO | `1.5%` | `100.0%` | `-98.5 п.п.` | `100.00%` | REJECTED: Edge -98.5 pp < 2 pp threshold (P_est=1.5% vs AskVWAP=100.0%) |
| LoL: Gen.G vs LYON (BO5) - Worlds Playoffs | Sports | YES | `95.0%` | `92.0%` | `+3.0 п.п.` | `1.00%` | EXECUTED BUY #95 ($2.22 @ 0.9200) |
| Spread: Villarreal CF (-1.5) | Sports | NO | `95.0%` | `92.0%` | `+3.0 п.п.` | `1.00%` | EXECUTED BUY #94 ($2.22 @ 0.9200) |
