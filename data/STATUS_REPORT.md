# 📊 Отчёт симулятора Polymarket (Устав Grok Bot — Демо-счёт)
**Обновлено:** `2026-11-08 15:19:39 UTC`

## 💰 Состояние виртуального портфеля
| Показатель | Значение | Правило устава |
| :--- | :--- | :--- |
| **Стартовый капитал** | `$50.00 USDC` | Не добавлять деньги |
| **Текущий баланс (Equity)** | **`$33.96 USDC`** (`-16.04$` / `-32.08%`) | Cash + Mark-to-Market по CLOB Bid |
| **Свободный кэш / В сделках** | `$18.40` / `$15.56 USDC` | До 8 открытых позиций, макс 8% банка |
| **Цель окупаемости подписки** | `$-16.04 / $60.00` (`0.0%`) | Цель: +$60.00 в месяц |
| **Просадка от пика (Текущая / Макс)** | `3.84%` / `24.45%` (Пик: `$35.32`) | Стоп-кран при просадке 40% |
| **Закрытых сделок / Win Rate** | `94` / `78.7%` | Brier Score: `0.1849` |

## 📂 Открытые позиции (6 / 8)
| # | Рынок | Кат. | Исход | Вход (Ask VWAP) | Текущий Bid | Оценка бота | Размер ($) | Нереализ. PnL | Источник |
| :- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| #100 | Spread: Colts (-3.5) | Sports | **NO** | `0.840` | `0.790` | `97.5%` | `$2.42` | `$-0.14` | https://www.nfl.com/scores |
| #107 | Spread: Commanders (-3.5) | Sports | **NO** | `0.790` | `0.780` | `97.5%` | `$2.56` | `$-0.03` | https://www.nfl.com/scores |
| #110 | Spread: Dolphins (-3.5) | Sports | **NO** | `0.840` | `0.830` | `97.5%` | `$2.58` | `$-0.03` | https://www.nfl.com/scores |
| #114 | Spread: Chargers (-3.5) | Sports | **NO** | `0.810` | `0.790` | `97.5%` | `$2.68` | `$-0.07` | https://www.nfl.com/scores |
| #115 | Will FC RFS win on 2026-11-08? | Sports | **NO** | `0.919` | `0.958` | `98.5%` | `$2.68` | `$+0.11` | https://www.virsliga.lv/ |
| #117 | Brighton & Hove Albion FC vs. Brentford FC: O/U 5.5 | Sports | **NO** | `0.910` | `0.940` | `97.0%` | `$2.71` | `$+0.09` | https://www.premierleague.com/ |

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
| Dota 2: Froglings vs potn9ki - Game 1 Winner | Sports | NO | `1.5%` | `100.0%` | `-98.5 п.п.` | `100.00%` | REJECTED: Edge -98.5 pp < 2 pp threshold (P_est=1.5% vs AskVWAP=100.0%) |
| Spread: Eagles (-3.5) | Sports | NO | `97.5%` | `72.0%` | `+25.5 п.п.` | `1.00%` | REJECTED: Contract price $0.720 outside sweet spot [$0.76, $0.92] |
| Spread: 49ers (-3.5) | Sports | NO | `97.5%` | `29.0%` | `+68.5 п.п.` | `1.00%` | REJECTED: Contract price $0.290 outside sweet spot [$0.76, $0.92] |
| Counter-Strike: Prestige vs KUUSAMO.gg - Map 2 Win | Sports | NO | `1.5%` | `100.0%` | `-98.5 п.п.` | `100.00%` | REJECTED: Edge -98.5 pp < 2 pp threshold (P_est=1.5% vs AskVWAP=100.0%) |
| Spread: Rams (-4.5) | Sports | NO | `97.5%` | `51.0%` | `+46.5 п.п.` | `1.00%` | REJECTED: Contract price $0.510 outside sweet spot [$0.76, $0.92] |
| Spread: Giants (-3.5) | Sports | NO | `97.5%` | `57.0%` | `+40.5 п.п.` | `1.00%` | REJECTED: Contract price $0.570 outside sweet spot [$0.76, $0.92] |
| Dota 2: Xipto Esports vs Nemiga Gaming - Game 1 Wi | Sports | NO | `1.5%` | `100.0%` | `-98.5 п.п.` | `100.00%` | REJECTED: Edge -98.5 pp < 2 pp threshold (P_est=1.5% vs AskVWAP=100.0%) |
| Dota 2: HULIGANI vs Yellow Submarine - Game 2 Winn | Sports | NO | `1.5%` | `100.0%` | `-98.5 п.п.` | `100.00%` | REJECTED: Edge -98.5 pp < 2 pp threshold (P_est=1.5% vs AskVWAP=100.0%) |
| Dota 2: Power Rangers vs Team Synapse - Game 1 Win | Sports | NO | `1.5%` | `100.0%` | `-98.5 п.п.` | `100.00%` | REJECTED: Edge -98.5 pp < 2 pp threshold (P_est=1.5% vs AskVWAP=100.0%) |
| Spread: Saints (-3.5) | Sports | NO | `97.5%` | `50.0%` | `+47.5 п.п.` | `1.00%` | REJECTED: Contract price $0.500 outside sweet spot [$0.76, $0.92] |
| Dota 2: Froglings vs potn9ki - Game 1 Winner | Sports | NO | `1.5%` | `100.0%` | `-98.5 п.п.` | `100.00%` | REJECTED: Edge -98.5 pp < 2 pp threshold (P_est=1.5% vs AskVWAP=100.0%) |
| Spread: Eagles (-3.5) | Sports | NO | `97.5%` | `72.0%` | `+25.5 п.п.` | `1.00%` | REJECTED: Contract price $0.720 outside sweet spot [$0.76, $0.92] |
| Spread: 49ers (-3.5) | Sports | NO | `97.5%` | `29.0%` | `+68.5 п.п.` | `1.00%` | REJECTED: Contract price $0.290 outside sweet spot [$0.76, $0.92] |
| Counter-Strike: Prestige vs KUUSAMO.gg - Map 2 Win | Sports | NO | `1.5%` | `100.0%` | `-98.5 п.п.` | `100.00%` | REJECTED: Edge -98.5 pp < 2 pp threshold (P_est=1.5% vs AskVWAP=100.0%) |
| Spread: Rams (-4.5) | Sports | NO | `97.5%` | `51.0%` | `+46.5 п.п.` | `1.00%` | REJECTED: Contract price $0.510 outside sweet spot [$0.76, $0.92] |
| Dota 2: Xipto Esports vs Nemiga Gaming - Game 1 Wi | Sports | NO | `1.5%` | `100.0%` | `-98.5 п.п.` | `100.00%` | REJECTED: Edge -98.5 pp < 2 pp threshold (P_est=1.5% vs AskVWAP=100.0%) |
| Spread: Giants (-3.5) | Sports | NO | `97.5%` | `57.0%` | `+40.5 п.п.` | `1.00%` | REJECTED: Contract price $0.570 outside sweet spot [$0.76, $0.92] |
| Dota 2: Power Rangers vs Team Synapse - Game 1 Win | Sports | NO | `1.5%` | `100.0%` | `-98.5 п.п.` | `100.00%` | REJECTED: Edge -98.5 pp < 2 pp threshold (P_est=1.5% vs AskVWAP=100.0%) |
