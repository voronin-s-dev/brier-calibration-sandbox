# 📊 Отчёт симулятора Polymarket (Устав Grok Bot — Демо-счёт)
**Обновлено:** `2026-11-08 21:01:15 UTC`

## 💰 Состояние виртуального портфеля
| Показатель | Значение | Правило устава |
| :--- | :--- | :--- |
| **Стартовый капитал** | `$50.00 USDC` | Не добавлять деньги |
| **Текущий баланс (Equity)** | **`$35.96 USDC`** (`-14.04$` / `-28.09%`) | Cash + Mark-to-Market по CLOB Bid |
| **Свободный кэш / В сделках** | `$22.41` / `$13.55 USDC` | До 8 открытых позиций, макс 8% банка |
| **Цель окупаемости подписки** | `$-14.04 / $60.00` (`0.0%`) | Цель: +$60.00 в месяц |
| **Просадка от пика (Текущая / Макс)** | `0.84%` / `24.45%` (Пик: `$36.26`) | Стоп-кран при просадке 40% |
| **Закрытых сделок / Win Rate** | `95` / `81.1%` | Brier Score: `0.1849` |

## 📂 Открытые позиции (5 / 8)
| # | Рынок | Кат. | Исход | Вход (Ask VWAP) | Текущий Bid | Оценка бота | Размер ($) | Нереализ. PnL | Источник |
| :- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| #100 | Spread: Colts (-3.5) | Sports | **NO** | `0.840` | `0.750` | `97.5%` | `$2.42` | `$-0.26` | https://www.nfl.com/scores |
| #107 | Spread: Commanders (-3.5) | Sports | **NO** | `0.790` | `0.981` | `97.5%` | `$2.56` | `$+0.62` | https://www.nfl.com/scores |
| #114 | Spread: Chargers (-3.5) | Sports | **NO** | `0.810` | `0.790` | `97.5%` | `$2.68` | `$-0.07` | https://www.nfl.com/scores |
| #115 | Will FC RFS win on 2026-11-08? | Sports | **NO** | `0.919` | `0.971` | `98.5%` | `$2.68` | `$+0.15` | https://www.virsliga.lv/ |
| #121 | Spread: Buccaneers (-3.5) | Sports | **NO** | `0.810` | `0.790` | `97.5%` | `$2.83` | `$-0.07` | https://www.nfl.com/scores |

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
| Dota 2: Yakult Brothers vs PuckChamp (BO3) - Dream | Sports | YES | `1.5%` | `100.0%` | `-98.5 п.п.` | `100.00%` | REJECTED: Edge -98.5 pp < 2 pp threshold (P_est=1.5% vs AskVWAP=100.0%) |
| Dota 2: Amaru Gaming vs Inner Circle - Game 1 Winn | Sports | YES | `1.5%` | `100.0%` | `-98.5 п.п.` | `100.00%` | REJECTED: Edge -98.5 pp < 2 pp threshold (P_est=1.5% vs AskVWAP=100.0%) |
| Spread: Pistons (-3.5) | Sports | NO | `97.5%` | `39.0%` | `+58.5 п.п.` | `1.00%` | REJECTED: Contract price $0.390 outside sweet spot [$0.76, $0.92] |
| Dota 2: Yakult Brothers vs PuckChamp - Game 2 Winn | Sports | YES | `1.5%` | `100.0%` | `-98.5 п.п.` | `100.00%` | REJECTED: Edge -98.5 pp < 2 pp threshold (P_est=1.5% vs AskVWAP=100.0%) |
| Spread: Pistons (-4.5) | Sports | NO | `97.5%` | `41.0%` | `+56.5 п.п.` | `1.00%` | REJECTED: Contract price $0.410 outside sweet spot [$0.76, $0.92] |
| Dota 2: Nemiga Gaming vs Spirit Academy (BO3) - As | Sports | NO | `1.5%` | `100.0%` | `-98.5 п.п.` | `100.00%` | REJECTED: Edge -98.5 pp < 2 pp threshold (P_est=1.5% vs AskVWAP=100.0%) |
| Dota 2: HULIGANI vs InterActive Philippines - Game | Sports | YES | `1.5%` | `100.0%` | `-98.5 п.п.` | `100.00%` | REJECTED: Edge -98.5 pp < 2 pp threshold (P_est=1.5% vs AskVWAP=100.0%) |
| Dota 2: Froglings vs Ka4kanarskie cyxariki - Game  | Sports | NO | `1.5%` | `100.0%` | `-98.5 п.п.` | `100.00%` | REJECTED: Edge -98.5 pp < 2 pp threshold (P_est=1.5% vs AskVWAP=100.0%) |
| Dota 2: Yakult Brothers vs PuckChamp (BO3) - Dream | Sports | YES | `1.5%` | `100.0%` | `-98.5 п.п.` | `100.00%` | REJECTED: Edge -98.5 pp < 2 pp threshold (P_est=1.5% vs AskVWAP=100.0%) |
| Counter-Strike: OG vs 9INE - Map 2 Winner | Sports | NO | `1.5%` | `100.0%` | `-98.5 п.п.` | `100.00%` | REJECTED: Edge -98.5 pp < 2 pp threshold (P_est=1.5% vs AskVWAP=100.0%) |
| Dota 2: Amaru Gaming vs Inner Circle - Game 1 Winn | Sports | YES | `1.5%` | `100.0%` | `-98.5 п.п.` | `100.00%` | REJECTED: Edge -98.5 pp < 2 pp threshold (P_est=1.5% vs AskVWAP=100.0%) |
| Dota 2: Yakult Brothers vs PuckChamp - Game 2 Winn | Sports | YES | `1.5%` | `100.0%` | `-98.5 п.п.` | `100.00%` | REJECTED: Edge -98.5 pp < 2 pp threshold (P_est=1.5% vs AskVWAP=100.0%) |
| Spread: Pistons (-3.5) | Sports | NO | `97.5%` | `39.0%` | `+58.5 п.п.` | `1.00%` | REJECTED: Contract price $0.390 outside sweet spot [$0.76, $0.92] |
| Spread: Pistons (-4.5) | Sports | NO | `97.5%` | `41.0%` | `+56.5 п.п.` | `1.00%` | REJECTED: Contract price $0.410 outside sweet spot [$0.76, $0.92] |
| Dota 2: HULIGANI vs InterActive Philippines - Game | Sports | YES | `1.5%` | `100.0%` | `-98.5 п.п.` | `100.00%` | REJECTED: Edge -98.5 pp < 2 pp threshold (P_est=1.5% vs AskVWAP=100.0%) |
| Dota 2: Froglings vs Ka4kanarskie cyxariki - Game  | Sports | NO | `1.5%` | `100.0%` | `-98.5 п.п.` | `100.00%` | REJECTED: Edge -98.5 pp < 2 pp threshold (P_est=1.5% vs AskVWAP=100.0%) |
| Counter-Strike: OG vs 9INE - Map 2 Winner | Sports | NO | `1.5%` | `100.0%` | `-98.5 п.п.` | `100.00%` | REJECTED: Edge -98.5 pp < 2 pp threshold (P_est=1.5% vs AskVWAP=100.0%) |
| Dota 2: Yakult Brothers vs PuckChamp - Game 1 Winn | Sports | YES | `1.5%` | `100.0%` | `-98.5 п.п.` | `100.00%` | REJECTED: Edge -98.5 pp < 2 pp threshold (P_est=1.5% vs AskVWAP=100.0%) |
