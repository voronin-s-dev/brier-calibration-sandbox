# 📊 Отчёт симулятора Polymarket (Устав Grok Bot — Демо-счёт)
**Обновлено:** `2026-10-24 21:29:34 UTC`

## 💰 Состояние виртуального портфеля
| Показатель | Значение | Правило устава |
| :--- | :--- | :--- |
| **Стартовый капитал** | `$50.00 USDC` | Не добавлять деньги |
| **Текущий баланс (Equity)** | **`$30.98 USDC`** (`-19.02$` / `-38.03%`) | Cash + Mark-to-Market по CLOB Bid |
| **Свободный кэш / В сделках** | `$16.32` / `$14.67 USDC` | До 8 открытых позиций, макс 8% банка |
| **Цель окупаемости подписки** | `$-19.02 / $60.00` (`0.0%`) | Цель: +$60.00 в месяц |
| **Просадка от пика (Текущая / Макс)** | `0.00%` / `6.31%` (Пик: `$30.98`) | Стоп-кран при просадке 40% |
| **Закрытых сделок / Win Rate** | `50` / `46.0%` | Brier Score: `0.2418` |

## 📂 Открытые позиции (4 / 8)
| # | Рынок | Кат. | Исход | Вход (Ask VWAP) | Текущий Bid | Оценка бота | Размер ($) | Нереализ. PnL | Источник |
| :- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| #51 | Will there be no change in Fed interest rates after the | Macro | **YES** | `0.940` | `0.940` | `96.5%` | `$3.67` | `$+0.00` | https://www.federalreserve.gov |
| #52 | Will the Fed increase interest rates by 25 bps after th | Macro | **NO** | `0.960` | `0.940` | `98.0%` | `$3.70` | `$-0.08` | https://www.federalreserve.gov |
| #53 | Will Flávio Bolsonaro win the second round of the 2026  | Geopolitics | **NO** | `0.939` | `0.933` | `97.5%` | `$3.71` | `$-0.02` | the margin of victory between  |
| #54 | Will Bitcoin dip to $79,000 on October 24? | Crypto | **NO** | `0.934` | `0.957` | `98.5%` | `$3.60` | `$+0.09` | https://www.binance.com/en/tra |

## 🔍 Последние проверенные кандидаты и фильтр стакана CLOB
| Рынок | Кат. | Сторона | Оценка бота | Цена Ask | Перекос (Edge) | Проскальзывание CLOB | Решение |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Will Harry Kane win the 2026 Ballon d'Or? | Other | YES | `83.3%` | `70.7%` | `+12.6 п.п.` | `0.10%` | REJECTED: Win probability 83.3% < 92% minimum (no underdog lottery bets) |
| Dota 2: Astra Invicta vs LEGION (BO3) - PARI Unive | Sports | YES | `1.5%` | `100.0%` | `-98.5 п.п.` | `100.00%` | REJECTED: Edge -98.5 pp < 2 pp threshold (P_est=1.5% vs AskVWAP=100.0%) |
| Will Kylian Mbappé win the 2026 Ballon d'Or? | Other | YES | `32.5%` | `21.0%` | `+11.5 п.п.` | `0.70%` | REJECTED: Win probability 32.5% < 92% minimum (no underdog lottery bets) |
| UFC 333: Alexander Volkanovski vs. Movsar Evloev ( | Sports | NO | `1.5%` | `100.0%` | `-98.5 п.п.` | `100.00%` | REJECTED: Edge -98.5 pp < 2 pp threshold (P_est=1.5% vs AskVWAP=100.0%) |
| LoL: LYON vs Karmine Corp (BO1) - Worlds Group Sta | Sports | NO | `1.5%` | `100.0%` | `-98.5 п.п.` | `100.00%` | REJECTED: Edge -98.5 pp < 2 pp threshold (P_est=1.5% vs AskVWAP=100.0%) |
| Will Flavio Bolsonaro win the most votes in the se | Geopolitics | NO | `95.9%` | `88.0%` | `+7.9 п.п.` | `1.00%` | REJECTED: Max open positions (4) reached |
| Will Naftali Bennett be the next Prime Minister of | Geopolitics | YES | `22.8%` | `14.0%` | `+8.8 п.п.` | `1.00%` | REJECTED: Win probability 22.8% < 92% minimum (no underdog lottery bets) |
| Will Аndrey Gyurov win the next Bulgarian presiden | Geopolitics | YES | `19.7%` | `13.0%` | `+6.7 п.п.` | `1.00%` | REJECTED: Win probability 19.7% < 92% minimum (no underdog lottery bets) |
| Will FC Barcelona vs. Real Madrid CF end in a draw | Sports | NO | `90.1%` | `85.0%` | `+5.1 п.п.` | `1.00%` | REJECTED: Win probability 90.1% < 92% minimum (no underdog lottery bets) |
| Will Bitcoin dip to $78,000 October 19-25? | Crypto | YES | `28.2%` | `11.0%` | `+17.3 п.п.` | `0.18%` | REJECTED: Win probability 28.2% < 92% minimum (no underdog lottery bets) |
| Dota 2: Yellow Submarine vs Dawn Bulls - Game 2 Wi | Sports | NO | `1.5%` | `100.0%` | `-98.5 п.п.` | `100.00%` | REJECTED: Edge -98.5 pp < 2 pp threshold (P_est=1.5% vs AskVWAP=100.0%) |
| Will Harry Kane win the 2026 Ballon d'Or? | Other | YES | `83.3%` | `70.7%` | `+12.6 п.п.` | `0.10%` | REJECTED: Win probability 83.3% < 92% minimum (no underdog lottery bets) |
| UFC 333: Aaron Pico vs. Losene Keita (Featherweigh | Sports | NO | `1.5%` | `100.0%` | `-98.5 п.п.` | `100.00%` | REJECTED: Edge -98.5 pp < 2 pp threshold (P_est=1.5% vs AskVWAP=100.0%) |
| UFC 333: Merab Dvalishvili vs. Petr Yan (Bantamwei | Sports | YES | `47.1%` | `43.0%` | `+4.2 п.п.` | `1.00%` | REJECTED: Win probability 47.1% < 92% minimum (no underdog lottery bets) |
| Counter-Strike: G2 vs Natus Vincere - Map 2 Winner | Sports | YES | `1.5%` | `100.0%` | `-98.5 п.п.` | `100.00%` | REJECTED: Edge -98.5 pp < 2 pp threshold (P_est=1.5% vs AskVWAP=100.0%) |
| Counter-Strike: G2 vs Natus Vincere (BO3) - PGL Ma | Sports | YES | `1.5%` | `100.0%` | `-98.5 п.п.` | `100.00%` | REJECTED: Edge -98.5 pp < 2 pp threshold (P_est=1.5% vs AskVWAP=100.0%) |
| Will Kylian Mbappé win the 2026 Ballon d'Or? | Other | YES | `29.4%` | `20.3%` | `+9.1 п.п.` | `0.40%` | REJECTED: Win probability 29.4% < 92% minimum (no underdog lottery bets) |
| UFC 333: Alexander Volkov vs. Rizvan Kuniev (Heavy | Sports | NO | `1.5%` | `100.0%` | `-98.5 п.п.` | `100.00%` | REJECTED: Edge -98.5 pp < 2 pp threshold (P_est=1.5% vs AskVWAP=100.0%) |
