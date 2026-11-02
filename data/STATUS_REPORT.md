# 📊 Отчёт симулятора Polymarket (Устав Grok Bot — Демо-счёт)
**Обновлено:** `2026-11-02 02:37:53 UTC`

## 💰 Состояние виртуального портфеля
| Показатель | Значение | Правило устава |
| :--- | :--- | :--- |
| **Стартовый капитал** | `$50.00 USDC` | Не добавлять деньги |
| **Текущий баланс (Equity)** | **`$27.53 USDC`** (`-22.47$` / `-44.94%`) | Cash + Mark-to-Market по CLOB Bid |
| **Свободный кэш / В сделках** | `$22.05` / `$5.48 USDC` | До 8 открытых позиций, макс 8% банка |
| **Цель окупаемости подписки** | `$-22.47 / $60.00` (`0.0%`) | Цель: +$60.00 в месяц |
| **Просадка от пика (Текущая / Макс)** | `22.04%` / `24.45%` (Пик: `$35.32`) | Стоп-кран при просадке 40% |
| **Закрытых сделок / Win Rate** | `85` / `63.5%` | Brier Score: `0.2268` |

## 📂 Открытые позиции (3 / 8)
| # | Рынок | Кат. | Исход | Вход (Ask VWAP) | Текущий Bid | Оценка бота | Размер ($) | Нереализ. PnL | Источник |
| :- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| #86 | Spread: Commanders (-17.5) | Sports | **NO** | `0.830` | `0.927` | `97.7%` | `$2.00` | `$+0.23` | https://www.nfl.com/scores |
| #88 | Kings vs. Mavericks | Sports | **NO** | `0.800` | `0.780` | `82.0%` | `$1.09` | `$-0.03` | https://www.nba.com/ |
| #89 | Nets vs. Knicks | Sports | **NO** | `0.890` | `0.880` | `92.0%` | `$2.21` | `$-0.02` | https://www.nba.com/ |

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
| Counter-Strike: 100 Thieves vs Wildcard (BO3) - Fi | Sports | NO | `1.5%` | `100.0%` | `-98.5 п.п.` | `100.00%` | REJECTED: Edge -98.5 pp < 2 pp threshold (P_est=1.5% vs AskVWAP=100.0%) |
| Spread: Lakers (-3.5) | Sports | NO | `97.5%` | `52.0%` | `+45.5 п.п.` | `1.00%` | REJECTED: Contract price $0.520 outside sweet spot [$0.76, $0.89] |
| Counter-Strike: DENDELE CS vs Imperial - Map 2 Win | Sports | NO | `1.5%` | `100.0%` | `-98.5 п.п.` | `100.00%` | REJECTED: Edge -98.5 pp < 2 pp threshold (P_est=1.5% vs AskVWAP=100.0%) |
| Spread: Commanders (-4.5) | Sports | NO | `97.5%` | `47.0%` | `+50.5 п.п.` | `1.00%` | REJECTED: Contract price $0.470 outside sweet spot [$0.76, $0.89] |
| Valorant: Gentle Mates GC vs KRÜ Blaze (BO5) - VCT | Sports | YES | `1.5%` | `100.0%` | `-98.5 п.п.` | `100.00%` | REJECTED: Edge -98.5 pp < 2 pp threshold (P_est=1.5% vs AskVWAP=100.0%) |
| Spread: Lakers (-4.5) | Sports | NO | `97.5%` | `56.0%` | `+41.5 п.п.` | `1.00%` | REJECTED: Contract price $0.560 outside sweet spot [$0.76, $0.89] |
