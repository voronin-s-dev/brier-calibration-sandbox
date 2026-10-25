# 📊 Отчёт симулятора Polymarket (Устав Grok Bot — Демо-счёт)
**Обновлено:** `2026-10-25 01:51:57 UTC`

## 💰 Состояние виртуального портфеля
| Показатель | Значение | Правило устава |
| :--- | :--- | :--- |
| **Стартовый капитал** | `$50.00 USDC` | Не добавлять деньги |
| **Текущий баланс (Equity)** | **`$31.23 USDC`** (`-18.77$` / `-37.53%`) | Cash + Mark-to-Market по CLOB Bid |
| **Свободный кэш / В сделках** | `$16.39` / `$14.84 USDC` | До 8 открытых позиций, макс 8% банка |
| **Цель окупаемости подписки** | `$-18.77 / $60.00` (`0.0%`) | Цель: +$60.00 в месяц |
| **Просадка от пика (Текущая / Макс)** | `0.11%` / `6.31%` (Пик: `$31.27`) | Стоп-кран при просадке 40% |
| **Закрытых сделок / Win Rate** | `51` / `47.1%` | Brier Score: `0.2418` |

## 📂 Открытые позиции (4 / 8)
| # | Рынок | Кат. | Исход | Вход (Ask VWAP) | Текущий Bid | Оценка бота | Размер ($) | Нереализ. PnL | Источник |
| :- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| #51 | Will there be no change in Fed interest rates after the | Macro | **YES** | `0.940` | `0.940` | `96.5%` | `$3.67` | `$+0.00` | https://www.federalreserve.gov |
| #52 | Will the Fed increase interest rates by 25 bps after th | Macro | **NO** | `0.960` | `0.950` | `98.0%` | `$3.70` | `$-0.04` | https://www.federalreserve.gov |
| #53 | Will Flávio Bolsonaro win the second round of the 2026  | Geopolitics | **NO** | `0.939` | `0.938` | `98.3%` | `$3.71` | `$-0.00` | the margin of victory between  |
| #55 | Will Bitcoin dip to $78,000 October 19-25? | Crypto | **NO** | `0.948` | `0.962` | `98.5%` | `$3.75` | `$+0.06` | https://www.binance.com/en/tra |

## 🔍 Последние проверенные кандидаты и фильтр стакана CLOB
| Рынок | Кат. | Сторона | Оценка бота | Цена Ask | Перекос (Edge) | Проскальзывание CLOB | Решение |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Bengals vs. Ravens | Sports | NO | `47.0%` | `42.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Win probability 47.0% < 92% minimum (no underdog lottery bets) |
| Will Harry Kane win the 2026 Ballon d'Or? | Other | YES | `83.2%` | `70.4%` | `+12.8 п.п.` | `0.10%` | REJECTED: Win probability 83.2% < 92% minimum (no underdog lottery bets) |
| Will Aleksandar Vučić – United Serbia win the most | Geopolitics | YES | `83.6%` | `72.0%` | `+11.6 п.п.` | `1.00%` | REJECTED: Win probability 83.6% < 92% minimum (no underdog lottery bets) |
| LoL: Team Liquid vs Bilibili Gaming (BO1) - Worlds | Sports | YES | `1.5%` | `100.0%` | `-98.5 п.п.` | `100.00%` | REJECTED: Edge -98.5 pp < 2 pp threshold (P_est=1.5% vs AskVWAP=100.0%) |
| Will Ilija Srdanović be the next prime minister of | Geopolitics | NO | `96.5%` | `92.0%` | `+4.5 п.п.` | `2.00%` | REJECTED: Max open positions (4) reached |
| Will the price of Bitcoin be between $80,000 and $ | Crypto | NO | `45.8%` | `14.0%` | `+31.8 п.п.` | `1.00%` | REJECTED: Win probability 45.8% < 92% minimum (no underdog lottery bets) |
| Will Luiz Inácio Lula da Silva win the second roun | Geopolitics | YES | `20.4%` | `13.0%` | `+7.4 п.п.` | `1.00%` | REJECTED: Win probability 20.4% < 92% minimum (no underdog lottery bets) |
| Will Flavio Bolsonaro win the most votes in the se | Geopolitics | NO | `94.8%` | `88.0%` | `+6.9 п.п.` | `1.00%` | REJECTED: Max open positions (4) reached |
| Will Naftali Bennett be the next Prime Minister of | Geopolitics | YES | `25.0%` | `14.0%` | `+11.0 п.п.` | `1.00%` | REJECTED: Win probability 25.0% < 92% minimum (no underdog lottery bets) |
| Will Аndrey Gyurov win the next Bulgarian presiden | Geopolitics | YES | `19.6%` | `13.0%` | `+6.6 п.п.` | `1.00%` | REJECTED: Win probability 19.6% < 92% minimum (no underdog lottery bets) |
| Will Luiz Inácio Lula da Silva win the second roun | Geopolitics | YES | `21.5%` | `15.0%` | `+6.5 п.п.` | `1.00%` | REJECTED: Win probability 21.5% < 92% minimum (no underdog lottery bets) |
| Spread: Ravens (-3.5) | Sports | NO | `97.5%` | `71.0%` | `+26.5 п.п.` | `1.00%` | REJECTED: Contract price $0.710 outside sweet spot [$0.84, $0.96] |
| Bengals vs. Ravens | Sports | NO | `47.0%` | `42.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Win probability 47.0% < 92% minimum (no underdog lottery bets) |
| Will Harry Kane win the 2026 Ballon d'Or? | Other | YES | `83.1%` | `70.4%` | `+12.7 п.п.` | `0.10%` | REJECTED: Win probability 83.1% < 92% minimum (no underdog lottery bets) |
| Will Aleksandar Vučić – United Serbia win the most | Geopolitics | YES | `78.3%` | `72.0%` | `+6.3 п.п.` | `1.00%` | REJECTED: Win probability 78.3% < 92% minimum (no underdog lottery bets) |
| LoL: Team Liquid vs Bilibili Gaming (BO1) - Worlds | Sports | YES | `1.5%` | `100.0%` | `-98.5 п.п.` | `100.00%` | REJECTED: Edge -98.5 pp < 2 pp threshold (P_est=1.5% vs AskVWAP=100.0%) |
| Will the price of Bitcoin be between $80,000 and $ | Crypto | NO | `46.2%` | `15.0%` | `+31.2 п.п.` | `1.00%` | REJECTED: Win probability 46.2% < 92% minimum (no underdog lottery bets) |
| Will Luiz Inácio Lula da Silva win the second roun | Geopolitics | YES | `20.5%` | `14.0%` | `+6.5 п.п.` | `2.00%` | REJECTED: Win probability 20.5% < 92% minimum (no underdog lottery bets) |
