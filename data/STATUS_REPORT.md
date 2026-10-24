# 📊 Отчёт симулятора Polymarket (Устав Grok Bot — Демо-счёт)
**Обновлено:** `2026-10-24 23:35:55 UTC`

## 💰 Состояние виртуального портфеля
| Показатель | Значение | Правило устава |
| :--- | :--- | :--- |
| **Стартовый капитал** | `$50.00 USDC` | Не добавлять деньги |
| **Текущий баланс (Equity)** | **`$31.22 USDC`** (`-18.78$` / `-37.57%`) | Cash + Mark-to-Market по CLOB Bid |
| **Свободный кэш / В сделках** | `$16.39` / `$14.83 USDC` | До 8 открытых позиций, макс 8% банка |
| **Цель окупаемости подписки** | `$-18.78 / $60.00` (`0.0%`) | Цель: +$60.00 в месяц |
| **Просадка от пика (Текущая / Макс)** | `0.04%` / `6.31%` (Пик: `$31.23`) | Стоп-кран при просадке 40% |
| **Закрытых сделок / Win Rate** | `51` / `47.1%` | Brier Score: `0.2418` |

## 📂 Открытые позиции (4 / 8)
| # | Рынок | Кат. | Исход | Вход (Ask VWAP) | Текущий Bid | Оценка бота | Размер ($) | Нереализ. PnL | Источник |
| :- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| #51 | Will there be no change in Fed interest rates after the | Macro | **YES** | `0.940` | `0.940` | `96.5%` | `$3.67` | `$+0.00` | https://www.federalreserve.gov |
| #52 | Will the Fed increase interest rates by 25 bps after th | Macro | **NO** | `0.960` | `0.950` | `98.0%` | `$3.70` | `$-0.04` | https://www.federalreserve.gov |
| #53 | Will Flávio Bolsonaro win the second round of the 2026  | Geopolitics | **NO** | `0.939` | `0.951` | `98.5%` | `$3.71` | `$+0.05` | the margin of victory between  |
| #55 | Will Bitcoin dip to $78,000 October 19-25? | Crypto | **NO** | `0.948` | `0.945` | `97.5%` | `$3.75` | `$-0.01` | https://www.binance.com/en/tra |

## 🔍 Последние проверенные кандидаты и фильтр стакана CLOB
| Рынок | Кат. | Сторона | Оценка бота | Цена Ask | Перекос (Edge) | Проскальзывание CLOB | Решение |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Will Likud win the most seats in the 2026 Israeli  | Geopolitics | YES | `35.4%` | `29.0%` | `+6.4 п.п.` | `1.00%` | REJECTED: Win probability 35.4% < 92% minimum (no underdog lottery bets) |
| Steelers vs. Saints: O/U 44.5 | Sports | NO | `57.1%` | `53.0%` | `+4.2 п.п.` | `1.00%` | REJECTED: Win probability 57.1% < 92% minimum (no underdog lottery bets) |
| Will Harry Kane win the 2026 Ballon d'Or? | Other | YES | `80.0%` | `71.0%` | `+9.0 п.п.` | `0.10%` | REJECTED: Win probability 80.0% < 92% minimum (no underdog lottery bets) |
| Will Aleksandar Vučić – United Serbia win the most | Geopolitics | YES | `77.1%` | `72.0%` | `+5.1 п.п.` | `1.00%` | REJECTED: Win probability 77.1% < 92% minimum (no underdog lottery bets) |
| Will Kylian Mbappé win the 2026 Ballon d'Or? | Other | YES | `27.9%` | `16.3%` | `+11.6 п.п.` | `0.20%` | REJECTED: Win probability 27.9% < 92% minimum (no underdog lottery bets) |
| LoL: Hanwha Life Esports vs Gen.G (BO1) - Worlds G | Sports | YES | `1.5%` | `100.0%` | `-98.5 п.п.` | `100.00%` | REJECTED: Edge -98.5 pp < 2 pp threshold (P_est=1.5% vs AskVWAP=100.0%) |
| Will Israel election happen as scheduled? | Geopolitics | YES | `98.0%` | `93.7%` | `+4.3 п.п.` | `0.10%` | REJECTED: Max open positions (4) reached |
| Will the price of Bitcoin be above $82,000 on Octo | Crypto | NO | `98.5%` | `92.9%` | `+5.6 п.п.` | `1.50%` | REJECTED: Max open positions (4) reached |
| Will Naftali Bennett be the next Prime Minister of | Geopolitics | YES | `25.0%` | `14.0%` | `+11.0 п.п.` | `1.00%` | REJECTED: Win probability 25.0% < 92% minimum (no underdog lottery bets) |
| Will the price of Ethereum be above $2,300 on Octo | Crypto | NO | `17.2%` | `6.6%` | `+10.6 п.п.` | `0.80%` | REJECTED: Win probability 17.2% < 92% minimum (no underdog lottery bets) |
| Will Аndrey Gyurov win the next Bulgarian presiden | Geopolitics | YES | `19.7%` | `13.0%` | `+6.7 п.п.` | `1.00%` | REJECTED: Win probability 19.7% < 92% minimum (no underdog lottery bets) |
| Will FC Barcelona vs. Real Madrid CF end in a draw | Sports | NO | `89.9%` | `85.0%` | `+4.9 п.п.` | `1.00%` | REJECTED: Win probability 89.9% < 92% minimum (no underdog lottery bets) |
| Will Bitcoin dip to $78,000 October 19-25? | Crypto | NO | `97.5%` | `94.8%` | `+2.6 п.п.` | `0.30%` | EXECUTED BUY #55 ($3.75 @ 0.9480) |
| Will Luiz Inácio Lula da Silva win the second roun | Geopolitics | YES | `22.7%` | `15.0%` | `+7.7 п.п.` | `1.00%` | REJECTED: Win probability 22.7% < 92% minimum (no underdog lottery bets) |
| Will Harry Kane win the 2026 Ballon d'Or? | Other | YES | `83.4%` | `70.7%` | `+12.7 п.п.` | `0.10%` | REJECTED: Win probability 83.4% < 92% minimum (no underdog lottery bets) |
| Will Aleksandar Vučić – United Serbia win the most | Geopolitics | YES | `74.2%` | `70.0%` | `+4.2 п.п.` | `1.00%` | REJECTED: Win probability 74.2% < 92% minimum (no underdog lottery bets) |
| Dota 2: Astra Invicta vs LEGION (BO3) - PARI Unive | Sports | YES | `1.5%` | `100.0%` | `-98.5 п.п.` | `100.00%` | REJECTED: Edge -98.5 pp < 2 pp threshold (P_est=1.5% vs AskVWAP=100.0%) |
| UFC 333: Alexander Volkanovski vs. Movsar Evloev ( | Sports | NO | `1.5%` | `100.0%` | `-98.5 п.п.` | `100.00%` | REJECTED: Edge -98.5 pp < 2 pp threshold (P_est=1.5% vs AskVWAP=100.0%) |
