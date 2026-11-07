# 📊 Отчёт симулятора Polymarket (Устав Grok Bot — Демо-счёт)
**Обновлено:** `2026-11-07 23:31:03 UTC`

## 💰 Состояние виртуального портфеля
| Показатель | Значение | Правило устава |
| :--- | :--- | :--- |
| **Стартовый капитал** | `$50.00 USDC` | Не добавлять деньги |
| **Текущий баланс (Equity)** | **`$32.03 USDC`** (`-17.97$` / `-35.94%`) | Cash + Mark-to-Market по CLOB Bid |
| **Свободный кэш / В сделках** | `$19.46` / `$12.57 USDC` | До 8 открытых позиций, макс 8% банка |
| **Цель окупаемости подписки** | `$-17.97 / $60.00` (`0.0%`) | Цель: +$60.00 в месяц |
| **Просадка от пика (Текущая / Макс)** | `9.30%` / `24.45%` (Пик: `$35.32`) | Стоп-кран при просадке 40% |
| **Закрытых сделок / Win Rate** | `95` / `72.6%` | Brier Score: `0.1892` |

## 📂 Открытые позиции (5 / 8)
| # | Рынок | Кат. | Исход | Вход (Ask VWAP) | Текущий Bid | Оценка бота | Размер ($) | Нереализ. PnL | Источник |
| :- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| #100 | Spread: Colts (-3.5) | Sports | **NO** | `0.840` | `0.790` | `97.5%` | `$2.42` | `$-0.14` | https://www.nfl.com/scores |
| #106 | LoL: Invictus Gaming vs Gen.G (BO5) - Worlds Playoffs | Sports | **NO** | `0.910` | `0.958` | `98.5%` | `$2.56` | `$+0.14` | https://gol.gg/esports/home |
| #107 | Spread: Commanders (-3.5) | Sports | **NO** | `0.790` | `0.780` | `97.5%` | `$2.56` | `$-0.03` | https://www.nfl.com/scores |
| #108 | Games Total: O/U 4.5 | Sports | **NO** | `0.920` | `0.910` | `94.0%` | `$2.57` | `$-0.03` | https://gol.gg/esports/home |
| #109 | Dota 2: Yakult Brothers vs CyberHero (BO3) - DreamLeagu | Sports | **NO** | `0.920` | `0.910` | `95.0%` | `$2.56` | `$-0.03` | https://www.dotabuff.com |

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
| Spread: Giants (-3.5) | Sports | NO | `97.5%` | `55.0%` | `+42.5 п.п.` | `1.00%` | REJECTED: Contract price $0.550 outside sweet spot [$0.76, $0.92] |
| Spread: UNLV (-3.5) | Sports | NO | `97.5%` | `52.0%` | `+45.5 п.п.` | `1.00%` | REJECTED: Contract price $0.520 outside sweet spot [$0.76, $0.92] |
| Dota 2: Yakult Brothers vs CyberHero - Game 1 Winn | Sports | YES | `1.5%` | `100.0%` | `-98.5 п.п.` | `100.00%` | REJECTED: Edge -98.5 pp < 2 pp threshold (P_est=1.5% vs AskVWAP=100.0%) |
| UFC Fight Night: Andre Petroski vs. Mantas Kondrat | Sports | NO | `1.5%` | `100.0%` | `-98.5 п.п.` | `100.00%` | REJECTED: Edge -98.5 pp < 2 pp threshold (P_est=1.5% vs AskVWAP=100.0%) |
| LoL: Invictus Gaming vs Gen.G - Game 1 Winner | Sports | YES | `1.5%` | `100.0%` | `-98.5 п.п.` | `100.00%` | REJECTED: Edge -98.5 pp < 2 pp threshold (P_est=1.5% vs AskVWAP=100.0%) |
| Dota 2: Yakult Brothers vs CyberHero (BO3) - Dream | Sports | NO | `95.0%` | `92.0%` | `+3.0 п.п.` | `1.00%` | EXECUTED BUY #109 ($2.56 @ 0.9200) |
| Games Total: O/U 4.5 | Sports | NO | `94.0%` | `92.0%` | `+2.0 п.п.` | `1.00%` | EXECUTED BUY #108 ($2.57 @ 0.9200) |
| Dota 2: Yakult Brothers vs CyberHero - Game 1 Winn | Sports | YES | `1.5%` | `100.0%` | `-98.5 п.п.` | `100.00%` | REJECTED: Edge -98.5 pp < 2 pp threshold (P_est=1.5% vs AskVWAP=100.0%) |
| Spread: UNLV (-3.5) | Sports | NO | `97.5%` | `52.0%` | `+45.5 п.п.` | `1.00%` | REJECTED: Contract price $0.520 outside sweet spot [$0.76, $0.92] |
| UFC Fight Night: Andre Petroski vs. Mantas Kondrat | Sports | NO | `1.5%` | `100.0%` | `-98.5 п.п.` | `100.00%` | REJECTED: Edge -98.5 pp < 2 pp threshold (P_est=1.5% vs AskVWAP=100.0%) |
| Dota 2: PlayTime vs HULIGANI - Game 1 Winner | Sports | YES | `1.5%` | `100.0%` | `-98.5 п.п.` | `100.00%` | REJECTED: Edge -98.5 pp < 2 pp threshold (P_est=1.5% vs AskVWAP=100.0%) |
| Dota 2: Yakult Brothers vs Amaru Gaming (BO3) - Dr | Sports | YES | `1.5%` | `100.0%` | `-98.5 п.п.` | `100.00%` | REJECTED: Edge -98.5 pp < 2 pp threshold (P_est=1.5% vs AskVWAP=100.0%) |
| LoL: Invictus Gaming vs Gen.G - Game 1 Winner | Sports | YES | `1.5%` | `100.0%` | `-98.5 п.п.` | `100.00%` | REJECTED: Edge -98.5 pp < 2 pp threshold (P_est=1.5% vs AskVWAP=100.0%) |
| Spread: Giants (-3.5) | Sports | NO | `97.5%` | `55.0%` | `+42.5 п.п.` | `1.00%` | REJECTED: Contract price $0.550 outside sweet spot [$0.76, $0.92] |
| UFC Fight Night: Wellington Turman vs. Seokhyeon K | Sports | YES | `1.5%` | `100.0%` | `-98.5 п.п.` | `100.00%` | REJECTED: Edge -98.5 pp < 2 pp threshold (P_est=1.5% vs AskVWAP=100.0%) |
| UFC Fight Night: Andre Petroski vs. Mantas Kondrat | Sports | NO | `1.5%` | `100.0%` | `-98.5 п.п.` | `100.00%` | REJECTED: Edge -98.5 pp < 2 pp threshold (P_est=1.5% vs AskVWAP=100.0%) |
| Dota 2: PlayTime vs HULIGANI - Game 1 Winner | Sports | YES | `1.5%` | `100.0%` | `-98.5 п.п.` | `100.00%` | REJECTED: Edge -98.5 pp < 2 pp threshold (P_est=1.5% vs AskVWAP=100.0%) |
| Dota 2: Yakult Brothers vs Amaru Gaming (BO3) - Dr | Sports | YES | `1.5%` | `100.0%` | `-98.5 п.п.` | `100.00%` | REJECTED: Edge -98.5 pp < 2 pp threshold (P_est=1.5% vs AskVWAP=100.0%) |
