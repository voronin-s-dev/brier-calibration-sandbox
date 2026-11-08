# 📊 Отчёт симулятора Polymarket (Устав Grok Bot — Демо-счёт)
**Обновлено:** `2026-11-08 20:10:18 UTC`

## 💰 Состояние виртуального портфеля
| Показатель | Значение | Правило устава |
| :--- | :--- | :--- |
| **Стартовый капитал** | `$50.00 USDC` | Не добавлять деньги |
| **Текущий баланс (Equity)** | **`$35.39 USDC`** (`-14.61$` / `-29.23%`) | Cash + Mark-to-Market по CLOB Bid |
| **Свободный кэш / В сделках** | `$19.36` / `$16.02 USDC` | До 8 открытых позиций, макс 8% банка |
| **Цель окупаемости подписки** | `$-14.61 / $60.00` (`0.0%`) | Цель: +$60.00 в месяц |
| **Просадка от пика (Текущая / Макс)** | `0.71%` / `24.45%` (Пик: `$35.64`) | Стоп-кран при просадке 40% |
| **Закрытых сделок / Win Rate** | `94` / `80.9%` | Brier Score: `0.1849` |

## 📂 Открытые позиции (6 / 8)
| # | Рынок | Кат. | Исход | Вход (Ask VWAP) | Текущий Bid | Оценка бота | Размер ($) | Нереализ. PnL | Источник |
| :- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| #100 | Spread: Colts (-3.5) | Sports | **NO** | `0.840` | `0.921` | `97.5%` | `$2.42` | `$+0.23` | https://www.nfl.com/scores |
| #107 | Spread: Commanders (-3.5) | Sports | **NO** | `0.790` | `0.750` | `97.5%` | `$2.56` | `$-0.13` | https://www.nfl.com/scores |
| #110 | Spread: Dolphins (-3.5) | Sports | **NO** | `0.840` | `0.962` | `97.5%` | `$2.58` | `$+0.37` | https://www.nfl.com/scores |
| #114 | Spread: Chargers (-3.5) | Sports | **NO** | `0.810` | `0.790` | `97.5%` | `$2.68` | `$-0.07` | https://www.nfl.com/scores |
| #115 | Will FC RFS win on 2026-11-08? | Sports | **NO** | `0.919` | `0.895` | `98.4%` | `$2.68` | `$-0.07` | https://www.virsliga.lv/ |
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
| Counter-Strike: OG vs 9INE - Map 2 Winner | Sports | NO | `1.5%` | `100.0%` | `-98.5 п.п.` | `100.00%` | REJECTED: Edge -98.5 pp < 2 pp threshold (P_est=1.5% vs AskVWAP=100.0%) |
| Dota 2: Yakult Brothers vs PuckChamp - Game 1 Winn | Sports | YES | `1.5%` | `100.0%` | `-98.5 п.п.` | `100.00%` | REJECTED: Edge -98.5 pp < 2 pp threshold (P_est=1.5% vs AskVWAP=100.0%) |
| Dota 2: Amaru Gaming vs Inner Circle - Game 1 Winn | Sports | YES | `1.5%` | `100.0%` | `-98.5 п.п.` | `100.00%` | REJECTED: Edge -98.5 pp < 2 pp threshold (P_est=1.5% vs AskVWAP=100.0%) |
| Spread: 49ers (-3.5) | Sports | NO | `97.5%` | `29.0%` | `+68.5 п.п.` | `1.00%` | REJECTED: Contract price $0.290 outside sweet spot [$0.76, $0.92] |
| Spread: Pistons (-3.5) | Sports | NO | `97.5%` | `38.0%` | `+59.5 п.п.` | `1.00%` | REJECTED: Contract price $0.380 outside sweet spot [$0.76, $0.92] |
| Spread: Pistons (-4.5) | Sports | NO | `97.5%` | `41.0%` | `+56.5 п.п.` | `1.00%` | REJECTED: Contract price $0.410 outside sweet spot [$0.76, $0.92] |
| Dota 2: HULIGANI vs InterActive Philippines - Game | Sports | YES | `1.5%` | `100.0%` | `-98.5 п.п.` | `100.00%` | REJECTED: Edge -98.5 pp < 2 pp threshold (P_est=1.5% vs AskVWAP=100.0%) |
| Dota 2: Nemiga Gaming vs Spirit Academy - Game 2 W | Sports | YES | `1.5%` | `100.0%` | `-98.5 п.п.` | `100.00%` | REJECTED: Edge -98.5 pp < 2 pp threshold (P_est=1.5% vs AskVWAP=100.0%) |
| Spread: Patriots (-3.5) | Sports | NO | `97.5%` | `53.0%` | `+44.5 п.п.` | `1.00%` | REJECTED: Contract price $0.530 outside sweet spot [$0.76, $0.92] |
| Dota 2: Froglings vs Ka4kanarskie cyxariki - Game  | Sports | NO | `1.5%` | `100.0%` | `-98.5 п.п.` | `100.00%` | REJECTED: Edge -98.5 pp < 2 pp threshold (P_est=1.5% vs AskVWAP=100.0%) |
| Counter-Strike: Ryvex vs Drama eSports (BO3) - CCT | Sports | YES | `97.5%` | `91.9%` | `+5.6 п.п.` | `2.90%` | REJECTED: CLOB round-trip slippage 2.90% > 2.0% limit |
| Spread: 49ers (-3.5) | Sports | NO | `97.5%` | `29.0%` | `+68.5 п.п.` | `1.00%` | REJECTED: Contract price $0.290 outside sweet spot [$0.76, $0.92] |
| Spread: Pistons (-3.5) | Sports | NO | `97.5%` | `38.0%` | `+59.5 п.п.` | `1.00%` | REJECTED: Contract price $0.380 outside sweet spot [$0.76, $0.92] |
| Spread: Pistons (-4.5) | Sports | NO | `97.5%` | `41.0%` | `+56.5 п.п.` | `1.00%` | REJECTED: Contract price $0.410 outside sweet spot [$0.76, $0.92] |
| Dota 2: Nemiga Gaming vs Spirit Academy - Game 2 W | Sports | YES | `1.5%` | `100.0%` | `-98.5 п.п.` | `100.00%` | REJECTED: Edge -98.5 pp < 2 pp threshold (P_est=1.5% vs AskVWAP=100.0%) |
| Dota 2: Froglings vs Ka4kanarskie cyxariki - Game  | Sports | YES | `98.5%` | `92.0%` | `+6.5 п.п.` | `2.00%` | REJECTED: Category cap reached (6/6 in Sports) |
| Spread: Patriots (-3.5) | Sports | NO | `97.5%` | `53.0%` | `+44.5 п.п.` | `1.00%` | REJECTED: Contract price $0.530 outside sweet spot [$0.76, $0.92] |
| Spread: Buccaneers (-3.5) | Sports | NO | `97.5%` | `81.0%` | `+16.5 п.п.` | `2.00%` | EXECUTED BUY #121 ($2.83 @ 0.8100) |
