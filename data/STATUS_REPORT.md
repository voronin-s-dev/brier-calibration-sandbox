# 📊 Отчёт симулятора Polymarket (Устав Grok Bot — Демо-счёт)
**Обновлено:** `2026-10-21 07:45:41 UTC`

## 💰 Состояние виртуального портфеля
| Показатель | Значение | Правило устава |
| :--- | :--- | :--- |
| **Стартовый капитал** | `$50.00 USDC` | Не добавлять деньги |
| **Текущий баланс (Equity)** | **`$27.51 USDC`** (`-22.49$` / `-44.98%`) | Cash + Mark-to-Market по CLOB Bid |
| **Свободный кэш / В сделках** | `$16.80` / `$10.71 USDC` | До 8 открытых позиций, макс 8% банка |
| **Цель окупаемости подписки** | `$-22.49 / $60.00` (`0.0%`) | Цель: +$60.00 в месяц |
| **Просадка от пика (Текущая / Макс)** | `1.91%` / `2.16%` (Пик: `$28.05`) | Стоп-кран при просадке 40% |
| **Закрытых сделок / Win Rate** | `35` / `25.7%` | Brier Score: `0.4280` |

## 📂 Открытые позиции (4 / 8)
| # | Рынок | Кат. | Исход | Вход (Ask VWAP) | Текущий Bid | Оценка бота | Размер ($) | Нереализ. PnL | Источник |
| :- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| #35 | Will Bitcoin dip to $80,000 in October? | Crypto | **YES** | `0.610` | `0.490` | `99.5%` | `$1.11` | `$-0.22` | Kraken BTCUSDT 1m/1h Spot Klin |
| #36 | US x Iran ceasefire continues through October 22? | Geopolitics | **YES** | `0.953` | `0.960` | `98.0%` | `$3.30` | `$+0.02` | Official NFL data feed |
| #38 | Will the Bank of Russia decrease the key rate after the | Other | **NO** | `0.900` | `0.880` | `97.0%` | `$3.30` | `$-0.07` | https://www.cbr.ru/eng/dkp/cal |
| #39 | Spread: Arsenal FC (-2.5) | Sports | **NO** | `0.964` | `0.955` | `98.5%` | `$3.30` | `$-0.03` | https://www.uefa.com/ |

## 🔍 Последние проверенные кандидаты и фильтр стакана CLOB
| Рынок | Кат. | Сторона | Оценка бота | Цена Ask | Перекос (Edge) | Проскальзывание CLOB | Решение |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Will FC Bayern München win on 2026-10-21? | Sports | YES | `51.0%` | `46.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Win probability 51.0% < 92% minimum (no underdog lottery bets) |
| Will LASK Linz win on 2026-10-21? | Sports | YES | `13.0%` | `8.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Win probability 13.0% < 92% minimum (no underdog lottery bets) |
| Will the price of Bitcoin be above $80,000 on Octo | Crypto | NO | `17.8%` | `8.0%` | `+9.8 п.п.` | `1.00%` | REJECTED: Win probability 17.8% < 92% minimum (no underdog lottery bets) |
| Will Bitcoin dip to $78,000 October 19-25? | Crypto | YES | `26.6%` | `10.0%` | `+16.6 п.п.` | `1.00%` | REJECTED: Win probability 26.6% < 92% minimum (no underdog lottery bets) |
| Will Bitcoin reach $88,000 October 19-25? | Crypto | YES | `26.1%` | `11.0%` | `+15.1 п.п.` | `1.00%` | REJECTED: Win probability 26.1% < 92% minimum (no underdog lottery bets) |
| Will Bitcoin dip to $80,000 on October 21? | Crypto | YES | `13.7%` | `3.0%` | `+10.7 п.п.` | `0.50%` | REJECTED: Win probability 13.7% < 92% minimum (no underdog lottery bets) |
| FC Bayern München vs. Arsenal FC: O/U 0.5 | Sports | NO | `15.6%` | `4.3%` | `+11.2 п.п.` | `0.51%` | REJECTED: Win probability 15.6% < 92% minimum (no underdog lottery bets) |
| Will the price of Bitcoin be above $86,000 on Octo | Crypto | YES | `9.4%` | `4.2%` | `+5.2 п.п.` | `0.50%` | REJECTED: Win probability 9.4% < 92% minimum (no underdog lottery bets) |
| Will NDP win the most seats in the 2026 British Co | Geopolitics | YES | `16.0%` | `11.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Win probability 16.0% < 92% minimum (no underdog lottery bets) |
| Will Bitcoin reach $90,000 October 19-25? | Crypto | YES | `13.7%` | `4.9%` | `+8.8 п.п.` | `0.50%` | REJECTED: Win probability 13.7% < 92% minimum (no underdog lottery bets) |
| Will Elon Musk post 280-299 tweets from October 16 | Geopolitics | YES | `12.6%` | `8.0%` | `+4.6 п.п.` | `2.00%` | REJECTED: Win probability 12.6% < 92% minimum (no underdog lottery bets) |
| Will Bitcoin dip to $76,000 October 19-25? | Crypto | YES | `12.5%` | `3.2%` | `+9.3 п.п.` | `0.10%` | REJECTED: Win probability 12.5% < 92% minimum (no underdog lottery bets) |
| Will Аndrey Gyurov win the next Bulgarian presiden | Geopolitics | NO | `94.9%` | `89.0%` | `+5.9 п.п.` | `2.00%` | REJECTED: Max open positions (4) reached |
| Will the price of Bitcoin be above $82,000 on Octo | Crypto | NO | `23.5%` | `11.8%` | `+11.8 п.п.` | `1.76%` | REJECTED: Win probability 23.5% < 92% minimum (no underdog lottery bets) |
| Will FC Bayern München win on 2026-10-21? | Sports | YES | `51.0%` | `46.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Win probability 51.0% < 92% minimum (no underdog lottery bets) |
| Will the price of Bitcoin be above $80,000 on Octo | Crypto | NO | `17.8%` | `7.0%` | `+10.8 п.п.` | `1.00%` | REJECTED: Win probability 17.8% < 92% minimum (no underdog lottery bets) |
| Will LASK Linz win on 2026-10-21? | Sports | YES | `13.0%` | `8.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Win probability 13.0% < 92% minimum (no underdog lottery bets) |
| Will Bitcoin dip to $78,000 October 19-25? | Crypto | YES | `26.8%` | `9.0%` | `+17.8 п.п.` | `1.00%` | REJECTED: Win probability 26.8% < 92% minimum (no underdog lottery bets) |
