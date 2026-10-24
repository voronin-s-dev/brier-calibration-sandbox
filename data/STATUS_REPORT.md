# 📊 Отчёт симулятора Polymarket (Устав Grok Bot — Демо-счёт)
**Обновлено:** `2026-10-24 21:48:12 UTC`

## 💰 Состояние виртуального портфеля
| Показатель | Значение | Правило устава |
| :--- | :--- | :--- |
| **Стартовый капитал** | `$50.00 USDC` | Не добавлять деньги |
| **Текущий баланс (Equity)** | **`$31.03 USDC`** (`-18.97$` / `-37.94%`) | Cash + Mark-to-Market по CLOB Bid |
| **Свободный кэш / В сделках** | `$16.32` / `$14.71 USDC` | До 8 открытых позиций, макс 8% банка |
| **Цель окупаемости подписки** | `$-18.97 / $60.00` (`0.0%`) | Цель: +$60.00 в месяц |
| **Просадка от пика (Текущая / Макс)** | `0.11%` / `6.31%` (Пик: `$31.06`) | Стоп-кран при просадке 40% |
| **Закрытых сделок / Win Rate** | `50` / `46.0%` | Brier Score: `0.2418` |

## 📂 Открытые позиции (4 / 8)
| # | Рынок | Кат. | Исход | Вход (Ask VWAP) | Текущий Bid | Оценка бота | Размер ($) | Нереализ. PnL | Источник |
| :- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| #51 | Will there be no change in Fed interest rates after the | Macro | **YES** | `0.940` | `0.940` | `96.5%` | `$3.67` | `$+0.00` | https://www.federalreserve.gov |
| #52 | Will the Fed increase interest rates by 25 bps after th | Macro | **NO** | `0.960` | `0.940` | `98.0%` | `$3.70` | `$-0.08` | https://www.federalreserve.gov |
| #53 | Will Flávio Bolsonaro win the second round of the 2026  | Geopolitics | **NO** | `0.939` | `0.948` | `98.5%` | `$3.71` | `$+0.04` | the margin of victory between  |
| #54 | Will Bitcoin dip to $79,000 on October 24? | Crypto | **NO** | `0.934` | `0.953` | `98.5%` | `$3.60` | `$+0.07` | https://www.binance.com/en/tra |

## 🔍 Последние проверенные кандидаты и фильтр стакана CLOB
| Рынок | Кат. | Сторона | Оценка бота | Цена Ask | Перекос (Edge) | Проскальзывание CLOB | Решение |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Will Harry Kane win the 2026 Ballon d'Or? | Other | YES | `83.4%` | `70.7%` | `+12.7 п.п.` | `0.10%` | REJECTED: Win probability 83.4% < 92% minimum (no underdog lottery bets) |
| Will Aleksandar Vučić – United Serbia win the most | Geopolitics | YES | `74.2%` | `70.0%` | `+4.2 п.п.` | `1.00%` | REJECTED: Win probability 74.2% < 92% minimum (no underdog lottery bets) |
| Dota 2: Astra Invicta vs LEGION (BO3) - PARI Unive | Sports | YES | `1.5%` | `100.0%` | `-98.5 п.п.` | `100.00%` | REJECTED: Edge -98.5 pp < 2 pp threshold (P_est=1.5% vs AskVWAP=100.0%) |
| UFC 333: Alexander Volkanovski vs. Movsar Evloev ( | Sports | NO | `1.5%` | `100.0%` | `-98.5 п.п.` | `100.00%` | REJECTED: Edge -98.5 pp < 2 pp threshold (P_est=1.5% vs AskVWAP=100.0%) |
| LoL: LYON vs Karmine Corp (BO1) - Worlds Group Sta | Sports | NO | `1.5%` | `100.0%` | `-98.5 п.п.` | `100.00%` | REJECTED: Edge -98.5 pp < 2 pp threshold (P_est=1.5% vs AskVWAP=100.0%) |
| Will Flavio Bolsonaro win the most votes in the se | Geopolitics | NO | `92.0%` | `88.0%` | `+4.0 п.п.` | `1.00%` | REJECTED: Max open positions (4) reached |
| Will Naftali Bennett be the next Prime Minister of | Geopolitics | YES | `22.7%` | `14.0%` | `+8.7 п.п.` | `1.00%` | REJECTED: Win probability 22.7% < 92% minimum (no underdog lottery bets) |
| Will Аndrey Gyurov win the next Bulgarian presiden | Geopolitics | YES | `19.6%` | `13.0%` | `+6.6 п.п.` | `1.00%` | REJECTED: Win probability 19.6% < 92% minimum (no underdog lottery bets) |
| Will FC Barcelona vs. Real Madrid CF end in a draw | Sports | NO | `90.2%` | `85.0%` | `+5.2 п.п.` | `1.00%` | REJECTED: Win probability 90.2% < 92% minimum (no underdog lottery bets) |
| Will Bitcoin dip to $78,000 October 19-25? | Crypto | YES | `27.9%` | `11.8%` | `+16.1 п.п.` | `0.20%` | REJECTED: Win probability 27.9% < 92% minimum (no underdog lottery bets) |
| Will Benjamin Netanyahu be the next Prime Minister | Geopolitics | NO | `78.0%` | `73.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Win probability 78.0% < 92% minimum (no underdog lottery bets) |
| Bengals vs. Ravens | Sports | NO | `47.0%` | `42.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Win probability 47.0% < 92% minimum (no underdog lottery bets) |
| Will Harry Kane win the 2026 Ballon d'Or? | Other | YES | `83.2%` | `70.7%` | `+12.6 п.п.` | `0.10%` | REJECTED: Win probability 83.2% < 92% minimum (no underdog lottery bets) |
| Dota 2: Astra Invicta vs LEGION (BO3) - PARI Unive | Sports | YES | `1.5%` | `100.0%` | `-98.5 п.п.` | `100.00%` | REJECTED: Edge -98.5 pp < 2 pp threshold (P_est=1.5% vs AskVWAP=100.0%) |
| UFC 333: Alexander Volkanovski vs. Movsar Evloev ( | Sports | NO | `1.5%` | `100.0%` | `-98.5 п.п.` | `100.00%` | REJECTED: Edge -98.5 pp < 2 pp threshold (P_est=1.5% vs AskVWAP=100.0%) |
| LoL: Invictus Gaming vs Team Secret Whales (BO1) - | Sports | YES | `79.5%` | `75.0%` | `+4.5 п.п.` | `1.00%` | REJECTED: Win probability 79.5% < 92% minimum (no underdog lottery bets) |
| LoL: LYON vs Karmine Corp (BO1) - Worlds Group Sta | Sports | NO | `1.5%` | `100.0%` | `-98.5 п.п.` | `100.00%` | REJECTED: Edge -98.5 pp < 2 pp threshold (P_est=1.5% vs AskVWAP=100.0%) |
| Will Flavio Bolsonaro win the most votes in the se | Geopolitics | NO | `94.0%` | `88.0%` | `+6.0 п.п.` | `1.00%` | REJECTED: Max open positions (4) reached |
