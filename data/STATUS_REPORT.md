# 📊 Отчёт симулятора Polymarket (Устав Grok Bot — Демо-счёт)
**Обновлено:** `2026-11-08 18:27:41 UTC`

## 💰 Состояние виртуального портфеля
| Показатель | Значение | Правило устава |
| :--- | :--- | :--- |
| **Стартовый капитал** | `$50.00 USDC` | Не добавлять деньги |
| **Текущий баланс (Equity)** | **`$34.12 USDC`** (`-15.88$` / `-31.76%`) | Cash + Mark-to-Market по CLOB Bid |
| **Свободный кэш / В сделках** | `$22.19` / `$11.93 USDC` | До 8 открытых позиций, макс 8% банка |
| **Цель окупаемости подписки** | `$-15.88 / $60.00` (`0.0%`) | Цель: +$60.00 в месяц |
| **Просадка от пика (Текущая / Макс)** | `3.38%` / `24.45%` (Пик: `$35.32`) | Стоп-кран при просадке 40% |
| **Закрытых сделок / Win Rate** | `95` / `80.0%` | Brier Score: `0.1849` |

## 📂 Открытые позиции (5 / 8)
| # | Рынок | Кат. | Исход | Вход (Ask VWAP) | Текущий Bid | Оценка бота | Размер ($) | Нереализ. PnL | Источник |
| :- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| #100 | Spread: Colts (-3.5) | Sports | **NO** | `0.840` | `0.690` | `97.5%` | `$2.42` | `$-0.43` | https://www.nfl.com/scores |
| #107 | Spread: Commanders (-3.5) | Sports | **NO** | `0.790` | `0.760` | `97.5%` | `$2.56` | `$-0.10` | https://www.nfl.com/scores |
| #110 | Spread: Dolphins (-3.5) | Sports | **NO** | `0.840` | `0.800` | `97.5%` | `$2.58` | `$-0.12` | https://www.nfl.com/scores |
| #114 | Spread: Chargers (-3.5) | Sports | **NO** | `0.810` | `0.790` | `97.5%` | `$2.68` | `$-0.07` | https://www.nfl.com/scores |
| #115 | Will FC RFS win on 2026-11-08? | Sports | **NO** | `0.919` | `0.825` | `98.4%` | `$2.68` | `$-0.27` | https://www.virsliga.lv/ |

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
| Spread: Pistons (-3.5) | Sports | NO | `97.5%` | `38.0%` | `+59.5 п.п.` | `1.00%` | REJECTED: Contract price $0.380 outside sweet spot [$0.76, $0.92] |
| Spread: 49ers (-3.5) | Sports | NO | `97.5%` | `29.0%` | `+68.5 п.п.` | `1.00%` | REJECTED: Contract price $0.290 outside sweet spot [$0.76, $0.92] |
| Spread: Pistons (-4.5) | Sports | NO | `97.5%` | `40.0%` | `+57.5 п.п.` | `2.00%` | REJECTED: Contract price $0.400 outside sweet spot [$0.76, $0.92] |
| Dota 2: Amaru Gaming vs CyberHero - Game 2 Winner | Sports | YES | `1.5%` | `100.0%` | `-98.5 п.п.` | `100.00%` | REJECTED: Edge -98.5 pp < 2 pp threshold (P_est=1.5% vs AskVWAP=100.0%) |
| Dota 2: Yakult Brothers vs Zero Tenacity - Game 2  | Sports | YES | `1.5%` | `100.0%` | `-98.5 п.п.` | `100.00%` | REJECTED: Edge -98.5 pp < 2 pp threshold (P_est=1.5% vs AskVWAP=100.0%) |
| Dota 2: Yakult Brothers vs Zero Tenacity (BO3) - D | Sports | YES | `1.5%` | `100.0%` | `-98.5 п.п.` | `100.00%` | REJECTED: Edge -98.5 pp < 2 pp threshold (P_est=1.5% vs AskVWAP=100.0%) |
| Counter-Strike: SAW Youngsters vs MASONIC (BO3) -  | Sports | YES | `1.5%` | `100.0%` | `-98.5 п.п.` | `100.00%` | REJECTED: Edge -98.5 pp < 2 pp threshold (P_est=1.5% vs AskVWAP=100.0%) |
| Spread: Patriots (-3.5) | Sports | NO | `97.5%` | `53.0%` | `+44.5 п.п.` | `1.00%` | REJECTED: Contract price $0.530 outside sweet spot [$0.76, $0.92] |
| Dota 2: PlayTime vs LEGION - Game 2 Winner | Sports | YES | `1.5%` | `100.0%` | `-98.5 п.п.` | `100.00%` | REJECTED: Edge -98.5 pp < 2 pp threshold (P_est=1.5% vs AskVWAP=100.0%) |
| Dota 2: PuckChamp vs Inner Circle - Game 2 Winner | Sports | NO | `95.0%` | `84.2%` | `+10.8 п.п.` | `3.60%` | REJECTED: CLOB round-trip slippage 3.60% > 2.0% limit |
| Spread: 49ers (-3.5) | Sports | NO | `97.5%` | `29.0%` | `+68.5 п.п.` | `1.00%` | REJECTED: Contract price $0.290 outside sweet spot [$0.76, $0.92] |
| Dota 2: PuckChamp vs Inner Circle - Game 2 Winner | Sports | NO | `97.9%` | `92.7%` | `+5.1 п.п.` | `3.20%` | REJECTED: Contract price $0.927 outside sweet spot [$0.76, $0.92] |
| Dota 2: Amaru Gaming vs CyberHero - Game 2 Winner | Sports | YES | `1.5%` | `100.0%` | `-98.5 п.п.` | `100.00%` | REJECTED: Edge -98.5 pp < 2 pp threshold (P_est=1.5% vs AskVWAP=100.0%) |
| Dota 2: Yakult Brothers vs Zero Tenacity - Game 2  | Sports | YES | `1.5%` | `100.0%` | `-98.5 п.п.` | `100.00%` | REJECTED: Edge -98.5 pp < 2 pp threshold (P_est=1.5% vs AskVWAP=100.0%) |
| Dota 2: Yakult Brothers vs Zero Tenacity (BO3) - D | Sports | YES | `1.5%` | `100.0%` | `-98.5 п.п.` | `100.00%` | REJECTED: Edge -98.5 pp < 2 pp threshold (P_est=1.5% vs AskVWAP=100.0%) |
| Counter-Strike: SAW Youngsters vs MASONIC (BO3) -  | Sports | YES | `1.5%` | `100.0%` | `-98.5 п.п.` | `100.00%` | REJECTED: Edge -98.5 pp < 2 pp threshold (P_est=1.5% vs AskVWAP=100.0%) |
| Spread: Patriots (-3.5) | Sports | NO | `97.5%` | `53.0%` | `+44.5 п.п.` | `1.00%` | REJECTED: Contract price $0.530 outside sweet spot [$0.76, $0.92] |
| Dota 2: PuckChamp vs Inner Circle - Game 1 Winner | Sports | YES | `1.5%` | `100.0%` | `-98.5 п.п.` | `100.00%` | REJECTED: Edge -98.5 pp < 2 pp threshold (P_est=1.5% vs AskVWAP=100.0%) |
