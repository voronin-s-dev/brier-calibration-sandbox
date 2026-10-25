# 📊 Отчёт симулятора Polymarket (Устав Grok Bot — Демо-счёт)
**Обновлено:** `2026-10-25 16:53:21 UTC`

## 💰 Состояние виртуального портфеля
| Показатель | Значение | Правило устава |
| :--- | :--- | :--- |
| **Стартовый капитал** | `$50.00 USDC` | Не добавлять деньги |
| **Текущий баланс (Equity)** | **`$31.35 USDC`** (`-18.65$` / `-37.30%`) | Cash + Mark-to-Market по CLOB Bid |
| **Свободный кэш / В сделках** | `$16.39` / `$14.96 USDC` | До 8 открытых позиций, макс 8% банка |
| **Цель окупаемости подписки** | `$-18.65 / $60.00` (`0.0%`) | Цель: +$60.00 в месяц |
| **Просадка от пика (Текущая / Макс)** | `0.08%` / `6.31%` (Пик: `$31.38`) | Стоп-кран при просадке 40% |
| **Закрытых сделок / Win Rate** | `51` / `47.1%` | Brier Score: `0.2418` |

## 📂 Открытые позиции (4 / 8)
| # | Рынок | Кат. | Исход | Вход (Ask VWAP) | Текущий Bid | Оценка бота | Размер ($) | Нереализ. PnL | Источник |
| :- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| #51 | Will there be no change in Fed interest rates after the | Macro | **YES** | `0.940` | `0.940` | `96.5%` | `$3.67` | `$+0.00` | https://www.federalreserve.gov |
| #52 | Will the Fed increase interest rates by 25 bps after th | Macro | **NO** | `0.960` | `0.940` | `98.0%` | `$3.70` | `$-0.08` | https://www.federalreserve.gov |
| #53 | Will Flávio Bolsonaro win the second round of the 2026  | Geopolitics | **NO** | `0.939` | `0.962` | `98.5%` | `$3.71` | `$+0.09` | the margin of victory between  |
| #55 | Will Bitcoin dip to $78,000 October 19-25? | Crypto | **NO** | `0.948` | `0.978` | `98.5%` | `$3.75` | `$+0.12` | https://www.binance.com/en/tra |

## 🔍 Последние проверенные кандидаты и фильтр стакана CLOB
| Рынок | Кат. | Сторона | Оценка бота | Цена Ask | Перекос (Edge) | Проскальзывание CLOB | Решение |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Exact Score: FC Barcelona 3 - 2 Real Madrid CF? | Other | NO | `98.5%` | `93.9%` | `+4.6 п.п.` | `0.20%` | REJECTED: Max open positions (4) reached |
| Will Bitcoin reach $83,000 on October 25? | Crypto | YES | `8.3%` | `3.1%` | `+5.2 п.п.` | `0.45%` | REJECTED: Win probability 8.3% < 92% minimum (no underdog lottery bets) |
| Will the price of Bitcoin be above $84,000 on Octo | Crypto | YES | `15.3%` | `10.0%` | `+5.3 п.п.` | `2.00%` | REJECTED: Win probability 15.3% < 92% minimum (no underdog lottery bets) |
| Will Bitcoin reach $82,000 on October 25? | Crypto | YES | `27.6%` | `14.0%` | `+13.6 п.п.` | `1.00%` | REJECTED: Win probability 27.6% < 92% minimum (no underdog lottery bets) |
| Will the price of Bitcoin be above $76,000 on Octo | Crypto | NO | `9.8%` | `4.9%` | `+4.9 п.п.` | `1.16%` | REJECTED: Win probability 9.8% < 92% minimum (no underdog lottery bets) |
| Spread: Chiefs (-14.5) | Sports | YES | `15.6%` | `11.0%` | `+4.6 п.п.` | `1.00%` | REJECTED: Win probability 15.6% < 92% minimum (no underdog lottery bets) |
| Will Bitcoin dip to $79,000 on October 25? | Crypto | YES | `26.1%` | `11.0%` | `+15.1 п.п.` | `1.00%` | REJECTED: Win probability 26.1% < 92% minimum (no underdog lottery bets) |
| Will Ilija Srdanović be the next prime minister of | Geopolitics | NO | `94.0%` | `89.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Max open positions (4) reached |
| Will the price of Bitcoin be above $78,000 on Octo | Crypto | NO | `23.2%` | `15.2%` | `+8.0 п.п.` | `1.40%` | REJECTED: Win probability 23.2% < 92% minimum (no underdog lottery bets) |
| Will Bitcoin reach $82,000 October 19-25? | Crypto | YES | `27.6%` | `15.0%` | `+12.6 п.п.` | `1.00%` | REJECTED: Win probability 27.6% < 92% minimum (no underdog lottery bets) |
| Dota 2: Team Spirit vs Astra Invicta (BO3) - PARI  | Sports | YES | `90.5%` | `86.0%` | `+4.5 п.п.` | `3.00%` | REJECTED: Win probability 90.5% < 92% minimum (no underdog lottery bets) |
| Will Lamine Yamal win the 2026 Ballon d'Or? | Other | YES | `23.5%` | `11.9%` | `+11.6 п.п.` | `0.30%` | REJECTED: Win probability 23.5% < 92% minimum (no underdog lottery bets) |
| Spread: FC Barcelona (-3.5) | Sports | NO | `97.5%` | `90.0%` | `+7.5 п.п.` | `2.00%` | REJECTED: Max open positions (4) reached |
| Exact Score: FC Barcelona 3 - 2 Real Madrid CF? | Other | NO | `98.5%` | `93.9%` | `+4.6 п.п.` | `0.20%` | REJECTED: Max open positions (4) reached |
| Will Bitcoin reach $83,000 on October 25? | Crypto | YES | `8.5%` | `2.9%` | `+5.5 п.п.` | `0.34%` | REJECTED: Win probability 8.5% < 92% minimum (no underdog lottery bets) |
| Will the price of Bitcoin be above $84,000 on Octo | Crypto | YES | `15.5%` | `10.0%` | `+5.5 п.п.` | `3.00%` | REJECTED: Win probability 15.5% < 92% minimum (no underdog lottery bets) |
| Will Bitcoin reach $82,000 on October 25? | Crypto | YES | `27.9%` | `14.0%` | `+13.9 п.п.` | `1.00%` | REJECTED: Win probability 27.9% < 92% minimum (no underdog lottery bets) |
| Will Luiz Inácio Lula da Silva win the second roun | Geopolitics | NO | `91.0%` | `86.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Win probability 91.0% < 92% minimum (no underdog lottery bets) |
