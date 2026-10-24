# 📊 Отчёт симулятора Polymarket (Устав Grok Bot — Демо-счёт)
**Обновлено:** `2026-10-24 23:45:14 UTC`

## 💰 Состояние виртуального портфеля
| Показатель | Значение | Правило устава |
| :--- | :--- | :--- |
| **Стартовый капитал** | `$50.00 USDC` | Не добавлять деньги |
| **Текущий баланс (Equity)** | **`$31.22 USDC`** (`-18.78$` / `-37.55%`) | Cash + Mark-to-Market по CLOB Bid |
| **Свободный кэш / В сделках** | `$16.39` / `$14.83 USDC` | До 8 открытых позиций, макс 8% банка |
| **Цель окупаемости подписки** | `$-18.78 / $60.00` (`0.0%`) | Цель: +$60.00 в месяц |
| **Просадка от пика (Текущая / Макс)** | `0.01%` / `6.31%` (Пик: `$31.23`) | Стоп-кран при просадке 40% |
| **Закрытых сделок / Win Rate** | `51` / `47.1%` | Brier Score: `0.2418` |

## 📂 Открытые позиции (4 / 8)
| # | Рынок | Кат. | Исход | Вход (Ask VWAP) | Текущий Bid | Оценка бота | Размер ($) | Нереализ. PnL | Источник |
| :- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| #51 | Will there be no change in Fed interest rates after the | Macro | **YES** | `0.940` | `0.940` | `96.5%` | `$3.67` | `$+0.00` | https://www.federalreserve.gov |
| #52 | Will the Fed increase interest rates by 25 bps after th | Macro | **NO** | `0.960` | `0.950` | `98.0%` | `$3.70` | `$-0.04` | https://www.federalreserve.gov |
| #53 | Will Flávio Bolsonaro win the second round of the 2026  | Geopolitics | **NO** | `0.939` | `0.950` | `98.5%` | `$3.71` | `$+0.04` | the margin of victory between  |
| #55 | Will Bitcoin dip to $78,000 October 19-25? | Crypto | **NO** | `0.948` | `0.948` | `98.5%` | `$3.75` | `$+0.00` | https://www.binance.com/en/tra |

## 🔍 Последние проверенные кандидаты и фильтр стакана CLOB
| Рынок | Кат. | Сторона | Оценка бота | Цена Ask | Перекос (Edge) | Проскальзывание CLOB | Решение |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| LoL: Team Liquid vs Bilibili Gaming (BO1) - Worlds | Sports | YES | `30.0%` | `25.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Win probability 30.0% < 92% minimum (no underdog lottery bets) |
| Steelers vs. Saints: O/U 44.5 | Sports | NO | `57.6%` | `53.0%` | `+4.6 п.п.` | `1.00%` | REJECTED: Win probability 57.6% < 92% minimum (no underdog lottery bets) |
| Will Harry Kane win the 2026 Ballon d'Or? | Other | YES | `76.4%` | `71.0%` | `+5.5 п.п.` | `0.10%` | REJECTED: Win probability 76.4% < 92% minimum (no underdog lottery bets) |
| Will Aleksandar Vučić – United Serbia win the most | Geopolitics | YES | `77.7%` | `72.0%` | `+5.7 п.п.` | `1.00%` | REJECTED: Win probability 77.7% < 92% minimum (no underdog lottery bets) |
| Will Kylian Mbappé win the 2026 Ballon d'Or? | Other | YES | `26.9%` | `16.9%` | `+10.0 п.п.` | `0.10%` | REJECTED: Win probability 26.9% < 92% minimum (no underdog lottery bets) |
| LoL: Hanwha Life Esports vs Gen.G (BO1) - Worlds G | Sports | YES | `1.5%` | `100.0%` | `-98.5 п.п.` | `100.00%` | REJECTED: Edge -98.5 pp < 2 pp threshold (P_est=1.5% vs AskVWAP=100.0%) |
| Will Israel election happen as scheduled? | Geopolitics | YES | `98.0%` | `93.7%` | `+4.3 п.п.` | `0.10%` | REJECTED: Max open positions (4) reached |
| Will Ethereum reach $2,400 on October 24? | Crypto | YES | `14.7%` | `9.3%` | `+5.4 п.п.` | `6.26%` | REJECTED: Win probability 14.7% < 92% minimum (no underdog lottery bets) |
| Ethereum Up or Down on October 25? | Crypto | YES | `94.0%` | `90.0%` | `+4.0 п.п.` | `1.00%` | REJECTED: Max open positions (4) reached |
| Will Naftali Bennett be the next Prime Minister of | Geopolitics | YES | `24.7%` | `14.0%` | `+10.7 п.п.` | `1.00%` | REJECTED: Win probability 24.7% < 92% minimum (no underdog lottery bets) |
| Will the price of Bitcoin be above $80,000 on Octo | Crypto | NO | `29.2%` | `12.7%` | `+16.5 п.п.` | `0.30%` | REJECTED: Win probability 29.2% < 92% minimum (no underdog lottery bets) |
| Will Аndrey Gyurov win the next Bulgarian presiden | Geopolitics | YES | `19.6%` | `13.0%` | `+6.6 п.п.` | `1.00%` | REJECTED: Win probability 19.6% < 92% minimum (no underdog lottery bets) |
| Will FC Barcelona vs. Real Madrid CF end in a draw | Sports | NO | `89.6%` | `85.0%` | `+4.6 п.п.` | `1.00%` | REJECTED: Win probability 89.6% < 92% minimum (no underdog lottery bets) |
| Counter-Strike: BESTIA vs Imperial (BO3) - Circuit | Sports | NO | `95.0%` | `80.0%` | `+15.0 п.п.` | `1.00%` | REJECTED: Contract price $0.800 outside sweet spot [$0.84, $0.96] |
| Will Luiz Inácio Lula da Silva win the second roun | Geopolitics | YES | `23.1%` | `15.0%` | `+8.1 п.п.` | `1.00%` | REJECTED: Win probability 23.1% < 92% minimum (no underdog lottery bets) |
| Will Likud win the most seats in the 2026 Israeli  | Geopolitics | YES | `35.4%` | `29.0%` | `+6.4 п.п.` | `1.00%` | REJECTED: Win probability 35.4% < 92% minimum (no underdog lottery bets) |
| Steelers vs. Saints: O/U 44.5 | Sports | NO | `57.1%` | `53.0%` | `+4.2 п.п.` | `1.00%` | REJECTED: Win probability 57.1% < 92% minimum (no underdog lottery bets) |
| Will Harry Kane win the 2026 Ballon d'Or? | Other | YES | `80.0%` | `71.0%` | `+9.0 п.п.` | `0.10%` | REJECTED: Win probability 80.0% < 92% minimum (no underdog lottery bets) |
