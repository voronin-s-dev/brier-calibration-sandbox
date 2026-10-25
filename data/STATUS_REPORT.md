# 📊 Отчёт симулятора Polymarket (Устав Grok Bot — Демо-счёт)
**Обновлено:** `2026-10-25 01:42:40 UTC`

## 💰 Состояние виртуального портфеля
| Показатель | Значение | Правило устава |
| :--- | :--- | :--- |
| **Стартовый капитал** | `$50.00 USDC` | Не добавлять деньги |
| **Текущий баланс (Equity)** | **`$31.27 USDC`** (`-18.73$` / `-37.46%`) | Cash + Mark-to-Market по CLOB Bid |
| **Свободный кэш / В сделках** | `$16.39` / `$14.88 USDC` | До 8 открытых позиций, макс 8% банка |
| **Цель окупаемости подписки** | `$-18.73 / $60.00` (`0.0%`) | Цель: +$60.00 в месяц |
| **Просадка от пика (Текущая / Макс)** | `0.00%` / `6.31%` (Пик: `$31.27`) | Стоп-кран при просадке 40% |
| **Закрытых сделок / Win Rate** | `51` / `47.1%` | Brier Score: `0.2418` |

## 📂 Открытые позиции (4 / 8)
| # | Рынок | Кат. | Исход | Вход (Ask VWAP) | Текущий Bid | Оценка бота | Размер ($) | Нереализ. PnL | Источник |
| :- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| #51 | Will there be no change in Fed interest rates after the | Macro | **YES** | `0.940` | `0.940` | `96.5%` | `$3.67` | `$+0.00` | https://www.federalreserve.gov |
| #52 | Will the Fed increase interest rates by 25 bps after th | Macro | **NO** | `0.960` | `0.950` | `98.0%` | `$3.70` | `$-0.04` | https://www.federalreserve.gov |
| #53 | Will Flávio Bolsonaro win the second round of the 2026  | Geopolitics | **NO** | `0.939` | `0.950` | `98.5%` | `$3.71` | `$+0.04` | the margin of victory between  |
| #55 | Will Bitcoin dip to $78,000 October 19-25? | Crypto | **NO** | `0.948` | `0.959` | `98.5%` | `$3.75` | `$+0.04` | https://www.binance.com/en/tra |

## 🔍 Последние проверенные кандидаты и фильтр стакана CLOB
| Рынок | Кат. | Сторона | Оценка бота | Цена Ask | Перекос (Edge) | Проскальзывание CLOB | Решение |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Spread: Ravens (-3.5) | Sports | NO | `97.5%` | `71.0%` | `+26.5 п.п.` | `1.00%` | REJECTED: Contract price $0.710 outside sweet spot [$0.84, $0.96] |
| Bengals vs. Ravens | Sports | NO | `47.0%` | `42.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Win probability 47.0% < 92% minimum (no underdog lottery bets) |
| Will Harry Kane win the 2026 Ballon d'Or? | Other | YES | `83.1%` | `70.4%` | `+12.7 п.п.` | `0.10%` | REJECTED: Win probability 83.1% < 92% minimum (no underdog lottery bets) |
| Will Aleksandar Vučić – United Serbia win the most | Geopolitics | YES | `78.3%` | `72.0%` | `+6.3 п.п.` | `1.00%` | REJECTED: Win probability 78.3% < 92% minimum (no underdog lottery bets) |
| LoL: Team Liquid vs Bilibili Gaming (BO1) - Worlds | Sports | YES | `1.5%` | `100.0%` | `-98.5 п.п.` | `100.00%` | REJECTED: Edge -98.5 pp < 2 pp threshold (P_est=1.5% vs AskVWAP=100.0%) |
| Will the price of Bitcoin be between $80,000 and $ | Crypto | NO | `46.2%` | `15.0%` | `+31.2 п.п.` | `1.00%` | REJECTED: Win probability 46.2% < 92% minimum (no underdog lottery bets) |
| Will Luiz Inácio Lula da Silva win the second roun | Geopolitics | YES | `20.5%` | `14.0%` | `+6.5 п.п.` | `2.00%` | REJECTED: Win probability 20.5% < 92% minimum (no underdog lottery bets) |
| Will Flavio Bolsonaro win the most votes in the se | Geopolitics | NO | `92.1%` | `88.0%` | `+4.1 п.п.` | `1.00%` | REJECTED: Max open positions (4) reached |
| Will Naftali Bennett be the next Prime Minister of | Geopolitics | YES | `24.9%` | `14.0%` | `+10.9 п.п.` | `1.00%` | REJECTED: Win probability 24.9% < 92% minimum (no underdog lottery bets) |
| Will the price of Bitcoin be above $80,000 on Octo | Crypto | NO | `29.1%` | `10.5%` | `+18.6 п.п.` | `0.40%` | REJECTED: Win probability 29.1% < 92% minimum (no underdog lottery bets) |
| Will Аndrey Gyurov win the next Bulgarian presiden | Geopolitics | YES | `19.6%` | `13.0%` | `+6.6 п.п.` | `1.00%` | REJECTED: Win probability 19.6% < 92% minimum (no underdog lottery bets) |
| Israel x Iran ceasefire continues through October  | Geopolitics | YES | `97.0%` | `92.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Max open positions (4) reached |
| Will FC Barcelona vs. Real Madrid CF end in a draw | Sports | NO | `91.7%` | `85.0%` | `+6.7 п.п.` | `1.00%` | REJECTED: Win probability 91.7% < 92% minimum (no underdog lottery bets) |
| Will Luiz Inácio Lula da Silva win the second roun | Geopolitics | YES | `23.4%` | `16.0%` | `+7.4 п.п.` | `1.00%` | REJECTED: Win probability 23.4% < 92% minimum (no underdog lottery bets) |
| Will Lamine Yamal win the 2026 Ballon d'Or? | Other | YES | `24.8%` | `13.6%` | `+11.2 п.п.` | `0.34%` | REJECTED: Win probability 24.8% < 92% minimum (no underdog lottery bets) |
| Spread: Ravens (-3.5) | Sports | NO | `97.5%` | `71.0%` | `+26.5 п.п.` | `1.00%` | REJECTED: Contract price $0.710 outside sweet spot [$0.84, $0.96] |
| Bengals vs. Ravens | Sports | NO | `46.0%` | `41.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Win probability 46.0% < 92% minimum (no underdog lottery bets) |
| Will Harry Kane win the 2026 Ballon d'Or? | Other | YES | `83.0%` | `70.5%` | `+12.5 п.п.` | `0.10%` | REJECTED: Win probability 83.0% < 92% minimum (no underdog lottery bets) |
