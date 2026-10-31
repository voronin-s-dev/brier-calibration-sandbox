# 📊 Отчёт симулятора Polymarket (Устав Grok Bot — Демо-счёт)
**Обновлено:** `2026-10-31 13:51:48 UTC`

## 💰 Состояние виртуального портфеля
| Показатель | Значение | Правило устава |
| :--- | :--- | :--- |
| **Стартовый капитал** | `$50.00 USDC` | Не добавлять деньги |
| **Текущий баланс (Equity)** | **`$26.90 USDC`** (`-23.10$` / `-46.20%`) | Cash + Mark-to-Market по CLOB Bid |
| **Свободный кэш / В сделках** | `$18.87` / `$8.04 USDC` | До 8 открытых позиций, макс 8% банка |
| **Цель окупаемости подписки** | `$-23.10 / $60.00` (`0.0%`) | Цель: +$60.00 в месяц |
| **Просадка от пика (Текущая / Макс)** | `23.83%` / `24.45%` (Пик: `$35.32`) | Стоп-кран при просадке 40% |
| **Закрытых сделок / Win Rate** | `78` / `61.5%` | Brier Score: `0.2435` |

## 📂 Открытые позиции (3 / 8)
| # | Рынок | Кат. | Исход | Вход (Ask VWAP) | Текущий Bid | Оценка бота | Размер ($) | Нереализ. PnL | Источник |
| :- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| #75 | Will FC Barcelona win on 2026-10-31? | Sports | **YES** | `0.890` | `0.880` | `92.0%` | `$3.78` | `$-0.04` | https://www.laliga.com/ |
| #81 | Timberwolves vs. Spurs | Sports | **NO** | `0.850` | `0.810` | `86.0%` | `$2.15` | `$-0.10` | https://www.nba.com/ |
| #82 | Dota 2: Team Yandex vs GamerLegion (BO3) - PARI Univers | Sports | **YES** | `0.870` | `0.910` | `93.0%` | `$2.15` | `$+0.10` | https://www.dotabuff.com |

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
| Map Handicap: FURIA (-2.5) vs Nemiga (+2.5) | Sports | YES | `1.5%` | `100.0%` | `-98.5 п.п.` | `100.00%` | REJECTED: Edge -98.5 pp < 2 pp threshold (P_est=1.5% vs AskVWAP=100.0%) |
| Counter-Strike: Nemiga vs FURIA - Map 3 Winner | Sports | YES | `1.5%` | `100.0%` | `-98.5 п.п.` | `100.00%` | REJECTED: Edge -98.5 pp < 2 pp threshold (P_est=1.5% vs AskVWAP=100.0%) |
| Dota 2: Team Yandex vs GamerLegion - Game 1 Winner | Sports | YES | `94.5%` | `99.0%` | `-4.5 п.п.` | `2.00%` | REJECTED: Edge -4.5 pp < 2 pp threshold (P_est=94.5% vs AskVWAP=99.0%) |
| Map Handicap: FURIA (-2.5) vs Nemiga (+2.5) | Sports | YES | `1.5%` | `100.0%` | `-98.5 п.п.` | `100.00%` | REJECTED: Edge -98.5 pp < 2 pp threshold (P_est=1.5% vs AskVWAP=100.0%) |
| Counter-Strike: Nemiga vs FURIA - Map 3 Winner | Sports | YES | `1.5%` | `100.0%` | `-98.5 п.п.` | `100.00%` | REJECTED: Edge -98.5 pp < 2 pp threshold (P_est=1.5% vs AskVWAP=100.0%) |
| Counter-Strike: 1WIN vs 5star (BO3) - Moscow Cyber | Sports | YES | `90.5%` | `80.0%` | `+10.5 п.п.` | `1.00%` | REJECTED: Category cap reached (3/3 in Sports) |
| Dota 2: Team Yandex vs GamerLegion - Game 1 Winner | Sports | YES | `93.0%` | `88.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Duplicate underlying event (sports:dota 2: team yandex vs gamerlegion :nodate) |
| Map Handicap: FURIA (-2.5) vs Nemiga (+2.5) | Sports | YES | `1.5%` | `100.0%` | `-98.5 п.п.` | `100.00%` | REJECTED: Edge -98.5 pp < 2 pp threshold (P_est=1.5% vs AskVWAP=100.0%) |
| Counter-Strike: Nemiga vs FURIA - Map 3 Winner | Sports | YES | `1.5%` | `100.0%` | `-98.5 п.п.` | `100.00%` | REJECTED: Edge -98.5 pp < 2 pp threshold (P_est=1.5% vs AskVWAP=100.0%) |
| Spread: Hawks (-3.5) | Sports | NO | `97.5%` | `47.0%` | `+50.5 п.п.` | `1.00%` | REJECTED: Contract price $0.470 outside sweet spot [$0.76, $0.89] |
| Spread: Oregon (-3.5) | Sports | NO | `97.5%` | `48.0%` | `+49.5 п.п.` | `1.00%` | REJECTED: Contract price $0.480 outside sweet spot [$0.76, $0.89] |
| Dota 2: Team Yandex vs GamerLegion (BO3) - PARI Un | Sports | YES | `90.0%` | `87.0%` | `+3.0 п.п.` | `1.00%` | EXECUTED BUY #82 ($2.15 @ 0.8700) |
| Timberwolves vs. Spurs | Sports | NO | `88.0%` | `85.0%` | `+3.0 п.п.` | `1.00%` | EXECUTED BUY #81 ($2.15 @ 0.8500) |
| Spread: Steelers (-3.5) | Sports | NO | `97.5%` | `52.0%` | `+45.5 п.п.` | `1.00%` | REJECTED: Contract price $0.520 outside sweet spot [$0.76, $0.89] |
| Counter-Strike: NRG vs Procyon Gaming (BO3) - FiRe | Sports | NO | `1.5%` | `100.0%` | `-98.5 п.п.` | `100.00%` | REJECTED: Edge -98.5 pp < 2 pp threshold (P_est=1.5% vs AskVWAP=100.0%) |
| Spread: Steelers (-3.5) | Sports | NO | `97.5%` | `52.0%` | `+45.5 п.п.` | `1.00%` | REJECTED: Contract price $0.520 outside sweet spot [$0.76, $0.89] |
| Spread: Broncos (-3.5) | Sports | NO | `97.5%` | `66.0%` | `+31.5 п.п.` | `1.00%` | REJECTED: Contract price $0.660 outside sweet spot [$0.76, $0.89] |
| Counter-Strike: NRG vs Procyon Gaming (BO3) - FiRe | Sports | NO | `1.5%` | `100.0%` | `-98.5 п.п.` | `100.00%` | REJECTED: Edge -98.5 pp < 2 pp threshold (P_est=1.5% vs AskVWAP=100.0%) |
