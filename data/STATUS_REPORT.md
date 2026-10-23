# 📊 Отчёт симулятора Polymarket (Устав Grok Bot — Демо-счёт)
**Обновлено:** `2026-10-23 23:24:29 UTC`

## 💰 Состояние виртуального портфеля
| Показатель | Значение | Правило устава |
| :--- | :--- | :--- |
| **Стартовый капитал** | `$50.00 USDC` | Не добавлять деньги |
| **Текущий баланс (Equity)** | **`$29.90 USDC`** (`-20.10$` / `-40.21%`) | Cash + Mark-to-Market по CLOB Bid |
| **Свободный кэш / В сделках** | `$18.04` / `$11.86 USDC` | До 8 открытых позиций, макс 8% банка |
| **Цель окупаемости подписки** | `$-20.10 / $60.00` (`0.0%`) | Цель: +$60.00 в месяц |
| **Просадка от пика (Текущая / Макс)** | `0.79%` / `6.31%` (Пик: `$30.14`) | Стоп-кран при просадке 40% |
| **Закрытых сделок / Win Rate** | `46` / `41.3%` | Brier Score: `0.2574` |

## 📂 Открытые позиции (4 / 8)
| # | Рынок | Кат. | Исход | Вход (Ask VWAP) | Текущий Bid | Оценка бота | Размер ($) | Нереализ. PnL | Источник |
| :- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| #35 | Will Bitcoin dip to $80,000 in October? | Crypto | **YES** | `0.610` | `0.770` | `99.5%` | `$1.11` | `$+0.29` | Kraken BTCUSDT 1m/1h Spot Klin |
| #45 | US x Iran ceasefire continues through October 24? | Geopolitics | **YES** | `0.920` | `0.920` | `96.0%` | `$3.41` | `$-0.00` | Official NFL data feed |
| #47 | Israel x Iran ceasefire continues through October 24? | Geopolitics | **YES** | `0.950` | `0.930` | `98.0%` | `$3.57` | `$-0.08` | the totality of information av |
| #50 | Spread: Manchester City FC (-3.5) | Sports | **NO** | `0.940` | `0.930` | `97.5%` | `$3.59` | `$-0.04` | https://www.premierleague.com/ |

## 🔍 Последние проверенные кандидаты и фильтр стакана CLOB
| Рынок | Кат. | Сторона | Оценка бота | Цена Ask | Перекос (Edge) | Проскальзывание CLOB | Решение |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Will Harry Kane win the 2026 Ballon d'Or? | Other | YES | `88.6%` | `76.6%` | `+12.0 п.п.` | `0.10%` | REJECTED: Win probability 88.6% < 92% minimum (no underdog lottery bets) |
| LoL: Team Liquid vs CTBC Flying Oyster (BO1) - Wor | Sports | YES | `1.5%` | `100.0%` | `-98.5 п.п.` | `100.00%` | REJECTED: Edge -98.5 pp < 2 pp threshold (P_est=1.5% vs AskVWAP=100.0%) |
| Will the price of Ethereum be above $2,300 on Octo | Crypto | NO | `10.1%` | `3.6%` | `+6.5 п.п.` | `1.25%` | REJECTED: Win probability 10.1% < 92% minimum (no underdog lottery bets) |
| Will Flavio Bolsonaro win the most votes in the se | Geopolitics | YES | `17.5%` | `13.0%` | `+4.5 п.п.` | `2.00%` | REJECTED: Win probability 17.5% < 92% minimum (no underdog lottery bets) |
| Will the price of Ethereum be above $2,300 on Octo | Crypto | NO | `19.2%` | `7.5%` | `+11.7 п.п.` | `2.00%` | REJECTED: Win probability 19.2% < 92% minimum (no underdog lottery bets) |
| Will Bitcoin reach $84,000 October 19-25? | Crypto | YES | `27.1%` | `3.5%` | `+23.6 п.п.` | `0.34%` | REJECTED: Win probability 27.1% < 92% minimum (no underdog lottery bets) |
| Will Ethereum dip to $2,200 October 19-25? | Crypto | YES | `9.5%` | `3.1%` | `+6.4 п.п.` | `0.39%` | REJECTED: Win probability 9.5% < 92% minimum (no underdog lottery bets) |
| Will the price of Bitcoin be between $80,000 and $ | Crypto | NO | `47.9%` | `15.0%` | `+32.9 п.п.` | `1.16%` | REJECTED: Win probability 47.9% < 92% minimum (no underdog lottery bets) |
| Will the price of Bitcoin be between $78,000 and $ | Crypto | YES | `22.3%` | `9.7%` | `+12.6 п.п.` | `2.47%` | REJECTED: Win probability 22.3% < 92% minimum (no underdog lottery bets) |
| Will Ethereum reach $2,500 October 19-25? | Crypto | YES | `23.4%` | `7.4%` | `+16.0 п.п.` | `3.29%` | REJECTED: Win probability 23.4% < 92% minimum (no underdog lottery bets) |
| Will Iliana Iotova win the 2026 Bulgarian presiden | Geopolitics | YES | `22.6%` | `14.0%` | `+8.6 п.п.` | `2.00%` | REJECTED: Win probability 22.6% < 92% minimum (no underdog lottery bets) |
| Will FC Barcelona vs. Real Madrid CF end in a draw | Sports | NO | `96.2%` | `85.0%` | `+11.2 п.п.` | `1.00%` | REJECTED: Max open positions (4) reached |
| Will Ilija Srdanović be the next prime minister of | Geopolitics | YES | `18.0%` | `14.0%` | `+4.0 п.п.` | `2.00%` | REJECTED: Win probability 18.0% < 92% minimum (no underdog lottery bets) |
| Will Bitcoin dip to $76,000 October 19-25? | Crypto | YES | `10.4%` | `3.3%` | `+7.1 п.п.` | `0.39%` | REJECTED: Win probability 10.4% < 92% minimum (no underdog lottery bets) |
| Israel x Iran ceasefire continues through October  | Geopolitics | NO | `16.9%` | `12.4%` | `+4.5 п.п.` | `1.41%` | REJECTED: Win probability 16.9% < 92% minimum (no underdog lottery bets) |
| Spread: Manchester City FC (-3.5) | Sports | NO | `97.5%` | `94.0%` | `+3.5 п.п.` | `1.00%` | EXECUTED BUY #50 ($3.59 @ 0.9400) |
| Will Bitcoin dip to $78,000 October 19-25? | Crypto | YES | `30.2%` | `7.7%` | `+22.5 п.п.` | `0.19%` | REJECTED: Win probability 30.2% < 92% minimum (no underdog lottery bets) |
| Will Bitcoin dip to $80,000 on October 23? | Crypto | YES | `30.8%` | `8.7%` | `+22.1 п.п.` | `0.95%` | REJECTED: Win probability 30.8% < 92% minimum (no underdog lottery bets) |
