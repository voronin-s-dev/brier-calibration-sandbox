# 📊 Отчёт симулятора Polymarket (Устав Grok Bot — Демо-счёт)
**Обновлено:** `2026-10-24 19:06:07 UTC`

## 💰 Состояние виртуального портфеля
| Показатель | Значение | Правило устава |
| :--- | :--- | :--- |
| **Стартовый капитал** | `$50.00 USDC` | Не добавлять деньги |
| **Текущий баланс (Equity)** | **`$30.87 USDC`** (`-19.13$` / `-38.25%`) | Cash + Mark-to-Market по CLOB Bid |
| **Свободный кэш / В сделках** | `$16.32` / `$14.56 USDC` | До 8 открытых позиций, макс 8% банка |
| **Цель окупаемости подписки** | `$-19.13 / $60.00` (`0.0%`) | Цель: +$60.00 в месяц |
| **Просадка от пика (Текущая / Макс)** | `0.27%` / `6.31%` (Пик: `$30.96`) | Стоп-кран при просадке 40% |
| **Закрытых сделок / Win Rate** | `50` / `46.0%` | Brier Score: `0.2418` |

## 📂 Открытые позиции (4 / 8)
| # | Рынок | Кат. | Исход | Вход (Ask VWAP) | Текущий Bid | Оценка бота | Размер ($) | Нереализ. PnL | Источник |
| :- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| #51 | Will there be no change in Fed interest rates after the | Macro | **YES** | `0.940` | `0.940` | `96.5%` | `$3.67` | `$+0.00` | https://www.federalreserve.gov |
| #52 | Will the Fed increase interest rates by 25 bps after th | Macro | **NO** | `0.960` | `0.940` | `98.0%` | `$3.70` | `$-0.08` | https://www.federalreserve.gov |
| #53 | Will Flávio Bolsonaro win the second round of the 2026  | Geopolitics | **NO** | `0.939` | `0.936` | `97.1%` | `$3.71` | `$-0.01` | the margin of victory between  |
| #54 | Will Bitcoin dip to $79,000 on October 24? | Crypto | **NO** | `0.934` | `0.925` | `97.5%` | `$3.60` | `$-0.03` | https://www.binance.com/en/tra |

## 🔍 Последние проверенные кандидаты и фильтр стакана CLOB
| Рынок | Кат. | Сторона | Оценка бота | Цена Ask | Перекос (Edge) | Проскальзывание CLOB | Решение |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| UFC 333: Aaron Pico vs. Losene Keita (Featherweigh | Sports | NO | `1.5%` | `100.0%` | `-98.5 п.п.` | `100.00%` | REJECTED: Edge -98.5 pp < 2 pp threshold (P_est=1.5% vs AskVWAP=100.0%) |
| LoL: G2 Esports vs LOS (BO1) - Worlds Group Stage | Sports | NO | `23.0%` | `18.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Win probability 23.0% < 92% minimum (no underdog lottery bets) |
| LoL: CTBC Flying Oyster vs Movistar KOI (BO1) - Wo | Sports | YES | `1.5%` | `100.0%` | `-98.5 п.п.` | `100.00%` | REJECTED: Edge -98.5 pp < 2 pp threshold (P_est=1.5% vs AskVWAP=100.0%) |
| Will Lula win the most votes in the second round o | Geopolitics | NO | `21.5%` | `13.0%` | `+8.5 п.п.` | `2.00%` | REJECTED: Win probability 21.5% < 92% minimum (no underdog lottery bets) |
| Will Naftali Bennett be the next Prime Minister of | Geopolitics | YES | `20.0%` | `15.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Win probability 20.0% < 92% minimum (no underdog lottery bets) |
| Will Movsar Evloev win by KO or TKO? | Sports | NO | `94.2%` | `89.0%` | `+5.2 п.п.` | `4.00%` | REJECTED: CLOB round-trip slippage 4.00% > 2.0% limit |
| Will Flavio Bolsonaro win the most votes in the se | Geopolitics | NO | `96.2%` | `88.0%` | `+8.2 п.п.` | `1.00%` | REJECTED: Max open positions (4) reached |
| Will Аndrey Gyurov win the next Bulgarian presiden | Geopolitics | YES | `19.4%` | `13.0%` | `+6.4 п.п.` | `1.00%` | REJECTED: Win probability 19.4% < 92% minimum (no underdog lottery bets) |
| Will FC Barcelona vs. Real Madrid CF end in a draw | Sports | NO | `90.6%` | `85.0%` | `+5.6 п.п.` | `1.00%` | REJECTED: Win probability 90.6% < 92% minimum (no underdog lottery bets) |
| Will Bitcoin dip to $78,000 October 19-25? | Crypto | YES | `29.1%` | `11.2%` | `+17.9 п.п.` | `0.20%` | REJECTED: Win probability 29.1% < 92% minimum (no underdog lottery bets) |
| Dota 2: Astra Invicta vs LEGION - Game 2 Winner | Sports | YES | `96.5%` | `92.0%` | `+4.5 п.п.` | `2.00%` | REJECTED: Max open positions (4) reached |
| US x Iran ceasefire continues through October 28? | Geopolitics | NO | `18.7%` | `12.0%` | `+6.7 п.п.` | `1.00%` | REJECTED: Win probability 18.7% < 92% minimum (no underdog lottery bets) |
| LoL: G2 Esports vs LOS (BO1) - Worlds Group Stage | Sports | NO | `25.6%` | `17.0%` | `+8.6 п.п.` | `1.00%` | REJECTED: Win probability 25.6% < 92% minimum (no underdog lottery bets) |
| LoL: CTBC Flying Oyster vs Movistar KOI (BO1) - Wo | Sports | YES | `1.5%` | `100.0%` | `-98.5 п.п.` | `100.00%` | REJECTED: Edge -98.5 pp < 2 pp threshold (P_est=1.5% vs AskVWAP=100.0%) |
| Will Lula win the most votes in the second round o | Geopolitics | NO | `21.6%` | `13.0%` | `+8.6 п.п.` | `2.00%` | REJECTED: Win probability 21.6% < 92% minimum (no underdog lottery bets) |
| Will Naftali Bennett be the next Prime Minister of | Geopolitics | YES | `23.4%` | `15.0%` | `+8.4 п.п.` | `1.00%` | REJECTED: Win probability 23.4% < 92% minimum (no underdog lottery bets) |
| Will Movsar Evloev win by KO or TKO? | Sports | NO | `94.2%` | `89.0%` | `+5.2 п.п.` | `4.00%` | REJECTED: CLOB round-trip slippage 4.00% > 2.0% limit |
| Will Flavio Bolsonaro win the most votes in the se | Geopolitics | NO | `95.8%` | `88.0%` | `+7.8 п.п.` | `1.00%` | REJECTED: Max open positions (4) reached |
