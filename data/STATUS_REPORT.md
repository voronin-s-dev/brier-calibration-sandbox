# 📊 Отчёт симулятора Polymarket (Устав Grok Bot — Демо-счёт)
**Обновлено:** `2026-10-31 18:02:49 UTC`

## 💰 Состояние виртуального портфеля
| Показатель | Значение | Правило устава |
| :--- | :--- | :--- |
| **Стартовый капитал** | `$50.00 USDC` | Не добавлять деньги |
| **Текущий баланс (Equity)** | **`$27.15 USDC`** (`-22.85$` / `-45.70%`) | Cash + Mark-to-Market по CLOB Bid |
| **Свободный кэш / В сделках** | `$19.17` / `$7.98 USDC` | До 8 открытых позиций, макс 8% банка |
| **Цель окупаемости подписки** | `$-22.85 / $60.00` (`0.0%`) | Цель: +$60.00 в месяц |
| **Просадка от пика (Текущая / Макс)** | `23.12%` / `24.45%` (Пик: `$35.32`) | Стоп-кран при просадке 40% |
| **Закрытых сделок / Win Rate** | `79` / `62.0%` | Brier Score: `0.2333` |

## 📂 Открытые позиции (3 / 8)
| # | Рынок | Кат. | Исход | Вход (Ask VWAP) | Текущий Bid | Оценка бота | Размер ($) | Нереализ. PnL | Источник |
| :- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| #75 | Will FC Barcelona win on 2026-10-31? | Sports | **YES** | `0.890` | `0.880` | `92.0%` | `$3.78` | `$-0.04` | https://www.laliga.com/ |
| #81 | Timberwolves vs. Spurs | Sports | **NO** | `0.850` | `0.830` | `87.0%` | `$2.15` | `$-0.05` | https://www.nba.com/ |
| #83 | FC Porto vs. Estoril Praia: O/U 5.5 | Sports | **NO** | `0.880` | `0.870` | `91.0%` | `$2.17` | `$-0.02` | https://www.ligaportugal.pt/ |

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
| Counter-Strike: FOKUS vs BakS eSports - Map 2 Winn | Sports | NO | `1.5%` | `100.0%` | `-98.5 п.п.` | `100.00%` | REJECTED: Edge -98.5 pp < 2 pp threshold (P_est=1.5% vs AskVWAP=100.0%) |
| Spread: Rockets (-3.5) | Sports | NO | `97.5%` | `54.0%` | `+43.5 п.п.` | `1.00%` | REJECTED: Contract price $0.540 outside sweet spot [$0.76, $0.89] |
| Dota 2: World Squad vs CIS Squad (BO1) - PARI Univ | Sports | YES | `1.5%` | `100.0%` | `-98.5 п.п.` | `100.00%` | REJECTED: Edge -98.5 pp < 2 pp threshold (P_est=1.5% vs AskVWAP=100.0%) |
| LoL: Karmine Corp vs Movistar KOI - Game 1 Winner | Sports | NO | `1.5%` | `100.0%` | `-98.5 п.п.` | `100.00%` | REJECTED: Edge -98.5 pp < 2 pp threshold (P_est=1.5% vs AskVWAP=100.0%) |
| Counter-Strike: FOKUS vs BakS eSports - Map 2 Winn | Sports | NO | `1.5%` | `100.0%` | `-98.5 п.п.` | `100.00%` | REJECTED: Edge -98.5 pp < 2 pp threshold (P_est=1.5% vs AskVWAP=100.0%) |
| Spread: Rockets (-3.5) | Sports | NO | `97.5%` | `54.0%` | `+43.5 п.п.` | `1.00%` | REJECTED: Contract price $0.540 outside sweet spot [$0.76, $0.89] |
| Dota 2: World Squad vs CIS Squad (BO1) - PARI Univ | Sports | YES | `1.5%` | `100.0%` | `-98.5 п.п.` | `100.00%` | REJECTED: Edge -98.5 pp < 2 pp threshold (P_est=1.5% vs AskVWAP=100.0%) |
| LoL: Karmine Corp vs Movistar KOI - Game 1 Winner | Sports | YES | `86.0%` | `100.0%` | `-14.0 п.п.` | `100.00%` | REJECTED: Edge -14.0 pp < 2 pp threshold (P_est=86.0% vs AskVWAP=100.0%) |
| Will FC Porto vs. Estoril Praia end in a draw? | Sports | NO | `96.5%` | `89.0%` | `+7.5 п.п.` | `1.00%` | REJECTED: Category cap reached (3/3 in Sports) |
| FC Porto vs. Estoril Praia: O/U 5.5 | Sports | NO | `91.0%` | `88.0%` | `+3.0 п.п.` | `1.00%` | EXECUTED BUY #83 ($2.17 @ 0.8800) |
| Map Handicap: FURIA (-2.5) vs Nemiga (+2.5) | Sports | YES | `1.5%` | `100.0%` | `-98.5 п.п.` | `100.00%` | REJECTED: Edge -98.5 pp < 2 pp threshold (P_est=1.5% vs AskVWAP=100.0%) |
| Counter-Strike: Nemiga vs FURIA - Map 3 Winner | Sports | YES | `1.5%` | `100.0%` | `-98.5 п.п.` | `100.00%` | REJECTED: Edge -98.5 pp < 2 pp threshold (P_est=1.5% vs AskVWAP=100.0%) |
| Dota 2: Team Yandex vs GamerLegion - Game 1 Winner | Sports | YES | `94.5%` | `99.0%` | `-4.5 п.п.` | `2.00%` | REJECTED: Edge -4.5 pp < 2 pp threshold (P_est=94.5% vs AskVWAP=99.0%) |
| Map Handicap: FURIA (-2.5) vs Nemiga (+2.5) | Sports | YES | `1.5%` | `100.0%` | `-98.5 п.п.` | `100.00%` | REJECTED: Edge -98.5 pp < 2 pp threshold (P_est=1.5% vs AskVWAP=100.0%) |
| Counter-Strike: Nemiga vs FURIA - Map 3 Winner | Sports | YES | `1.5%` | `100.0%` | `-98.5 п.п.` | `100.00%` | REJECTED: Edge -98.5 pp < 2 pp threshold (P_est=1.5% vs AskVWAP=100.0%) |
| Counter-Strike: 1WIN vs 5star (BO3) - Moscow Cyber | Sports | YES | `90.5%` | `80.0%` | `+10.5 п.п.` | `1.00%` | REJECTED: Category cap reached (3/3 in Sports) |
| Dota 2: Team Yandex vs GamerLegion - Game 1 Winner | Sports | YES | `93.0%` | `88.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Duplicate underlying event (sports:dota 2: team yandex vs gamerlegion :nodate) |
| Map Handicap: FURIA (-2.5) vs Nemiga (+2.5) | Sports | YES | `1.5%` | `100.0%` | `-98.5 п.п.` | `100.00%` | REJECTED: Edge -98.5 pp < 2 pp threshold (P_est=1.5% vs AskVWAP=100.0%) |
