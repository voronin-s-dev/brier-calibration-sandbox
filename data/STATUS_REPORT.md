# 📊 Отчёт симулятора Polymarket (Устав Grok Bot — Демо-счёт)
**Обновлено:** `2026-10-29 18:23:45 UTC`

## 💰 Состояние виртуального портфеля
| Показатель | Значение | Правило устава |
| :--- | :--- | :--- |
| **Стартовый капитал** | `$50.00 USDC` | Не добавлять деньги |
| **Текущий баланс (Equity)** | **`$28.15 USDC`** (`-21.85$` / `-43.69%`) | Cash + Mark-to-Market по CLOB Bid |
| **Свободный кэш / В сделках** | `$21.16` / `$7.00 USDC` | До 8 открытых позиций, макс 8% банка |
| **Цель окупаемости подписки** | `$-21.85 / $60.00` (`0.0%`) | Цель: +$60.00 в месяц |
| **Просадка от пика (Текущая / Макс)** | `20.28%` / `24.45%` (Пик: `$35.32`) | Стоп-кран при просадке 40% |
| **Закрытых сделок / Win Rate** | `75` / `61.3%` | Brier Score: `0.2283` |

## 📂 Открытые позиции (3 / 8)
| # | Рынок | Кат. | Исход | Вход (Ask VWAP) | Текущий Bid | Оценка бота | Размер ($) | Нереализ. PnL | Источник |
| :- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| #75 | Will FC Barcelona win on 2026-10-31? | Sports | **YES** | `0.890` | `0.870` | `92.8%` | `$3.78` | `$-0.08` | https://www.laliga.com/ |
| #78 | LoL: Karmine Corp vs CTBC Flying Oyster (BO3) - Worlds  | Sports | **YES** | `0.800` | `0.810` | `85.0%` | `$1.69` | `$+0.02` | https://gol.gg/esports/home |
| #79 | LoL: Hanwha Life Esports vs G2 Esports (BO3) - Worlds G | Sports | **YES** | `0.790` | `0.780` | `82.0%` | `$1.61` | `$-0.02` | https://gol.gg/esports/home |

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
| Counter-Strike: Fortress vs DNK (BO3) - Exort Fies | Sports | YES | `1.5%` | `100.0%` | `-98.5 п.п.` | `100.00%` | REJECTED: Edge -98.5 pp < 2 pp threshold (P_est=1.5% vs AskVWAP=100.0%) |
| Spread: Packers (-4.5) | Sports | NO | `97.5%` | `55.0%` | `+42.5 п.п.` | `1.00%` | REJECTED: Contract price $0.550 outside sweet spot [$0.76, $0.89] |
| Spread: Packers (-3.5) | Sports | NO | `97.5%` | `50.0%` | `+47.5 п.п.` | `1.00%` | REJECTED: Contract price $0.500 outside sweet spot [$0.76, $0.89] |
| LoL: Hanwha Life Esports vs G2 Esports (BO3) - Wor | Sports | YES | `82.0%` | `79.0%` | `+3.0 п.п.` | `1.00%` | EXECUTED BUY #79 ($1.61 @ 0.7900) |
| Spread: Atlanta Dream (-3.5) | Sports | NO | `97.5%` | `45.0%` | `+52.5 п.п.` | `1.00%` | REJECTED: Contract price $0.450 outside sweet spot [$0.76, $0.89] |
| Counter-Strike: JiJieHao vs SAW Youngsters - Map 1 | Sports | YES | `1.5%` | `100.0%` | `-98.5 п.п.` | `100.00%` | REJECTED: Edge -98.5 pp < 2 pp threshold (P_est=1.5% vs AskVWAP=100.0%) |
| Spread: Packers (-3.5) | Sports | NO | `97.5%` | `50.0%` | `+47.5 п.п.` | `1.00%` | REJECTED: Contract price $0.500 outside sweet spot [$0.76, $0.89] |
| Spread: Packers (-4.5) | Sports | NO | `97.5%` | `54.0%` | `+43.5 п.п.` | `1.00%` | REJECTED: Contract price $0.540 outside sweet spot [$0.76, $0.89] |
| Counter-Strike: BIG vs Eternal Fire - Map 1 Winner | Sports | YES | `1.5%` | `100.0%` | `-98.5 п.п.` | `100.00%` | REJECTED: Edge -98.5 pp < 2 pp threshold (P_est=1.5% vs AskVWAP=100.0%) |
| Dota 2: Team Liquid vs Astra Invicta (BO3) - PARI  | Sports | NO | `1.5%` | `100.0%` | `-98.5 п.п.` | `100.00%` | REJECTED: Edge -98.5 pp < 2 pp threshold (P_est=1.5% vs AskVWAP=100.0%) |
| Map Handicap: VIT (-1.5) vs Natus Vincere (+1.5) | Sports | YES | `1.5%` | `100.0%` | `-98.5 п.п.` | `100.00%` | REJECTED: Edge -98.5 pp < 2 pp threshold (P_est=1.5% vs AskVWAP=100.0%) |
| Dota 2: Team Liquid vs Astra Invicta - Game 2 Winn | Sports | NO | `1.5%` | `100.0%` | `-98.5 п.п.` | `100.00%` | REJECTED: Edge -98.5 pp < 2 pp threshold (P_est=1.5% vs AskVWAP=100.0%) |
| Counter-Strike: FaZe vs GamerLegion - Map 1 Winner | Sports | NO | `93.0%` | `100.0%` | `-7.0 п.п.` | `100.00%` | REJECTED: Edge -7.0 pp < 2 pp threshold (P_est=93.0% vs AskVWAP=100.0%) |
| Spread: Broncos (-3.5) | Sports | NO | `97.5%` | `67.0%` | `+30.5 п.п.` | `1.00%` | REJECTED: Contract price $0.670 outside sweet spot [$0.76, $0.89] |
| Counter-Strike: JiJieHao vs SAW Youngsters - Map 1 | Sports | YES | `1.5%` | `100.0%` | `-98.5 п.п.` | `100.00%` | REJECTED: Edge -98.5 pp < 2 pp threshold (P_est=1.5% vs AskVWAP=100.0%) |
| Spread: Atlanta Dream (-3.5) | Sports | NO | `97.5%` | `46.0%` | `+51.5 п.п.` | `2.00%` | REJECTED: Contract price $0.460 outside sweet spot [$0.76, $0.89] |
| Spread: Packers (-3.5) | Sports | NO | `97.5%` | `50.0%` | `+47.5 п.п.` | `1.00%` | REJECTED: Contract price $0.500 outside sweet spot [$0.76, $0.89] |
| Counter-Strike: BIG vs Eternal Fire - Map 1 Winner | Sports | YES | `1.5%` | `100.0%` | `-98.5 п.п.` | `100.00%` | REJECTED: Edge -98.5 pp < 2 pp threshold (P_est=1.5% vs AskVWAP=100.0%) |
