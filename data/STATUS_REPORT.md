# 📊 Отчёт симулятора Polymarket (Устав Grok Bot — Демо-счёт)
**Обновлено:** `2026-10-24 12:29:55 UTC`

## 💰 Состояние виртуального портфеля
| Показатель | Значение | Правило устава |
| :--- | :--- | :--- |
| **Стартовый капитал** | `$50.00 USDC` | Не добавлять деньги |
| **Текущий баланс (Equity)** | **`$30.54 USDC`** (`-19.46$` / `-38.91%`) | Cash + Mark-to-Market по CLOB Bid |
| **Свободный кэш / В сделках** | `$18.14` / `$12.41 USDC` | До 8 открытых позиций, макс 8% банка |
| **Цель окупаемости подписки** | `$-19.46 / $60.00` (`0.0%`) | Цель: +$60.00 в месяц |
| **Просадка от пика (Текущая / Макс)** | `0.23%` / `6.31%` (Пик: `$30.61`) | Стоп-кран при просадке 40% |
| **Закрытых сделок / Win Rate** | `47` / `42.6%` | Brier Score: `0.2574` |

## 📂 Открытые позиции (4 / 8)
| # | Рынок | Кат. | Исход | Вход (Ask VWAP) | Текущий Bid | Оценка бота | Размер ($) | Нереализ. PnL | Источник |
| :- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| #35 | Will Bitcoin dip to $80,000 in October? | Crypto | **YES** | `0.610` | `0.810` | `99.5%` | `$1.11` | `$+0.36` | Kraken BTCUSDT 1m/1h Spot Klin |
| #45 | US x Iran ceasefire continues through October 24? | Geopolitics | **YES** | `0.920` | `0.978` | `98.0%` | `$3.41` | `$+0.21` | Official NFL data feed |
| #47 | Israel x Iran ceasefire continues through October 24? | Geopolitics | **YES** | `0.950` | `0.979` | `98.0%` | `$3.57` | `$+0.11` | the totality of information av |
| #51 | Will there be no change in Fed interest rates after the | Macro | **YES** | `0.940` | `0.930` | `96.5%` | `$3.67` | `$-0.04` | https://www.federalreserve.gov |

## 🔍 Последние проверенные кандидаты и фильтр стакана CLOB
| Рынок | Кат. | Сторона | Оценка бота | Цена Ask | Перекос (Edge) | Проскальзывание CLOB | Решение |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Will the price of Bitcoin be above $82,000 on Octo | Crypto | YES | `21.3%` | `8.0%` | `+13.3 п.п.` | `1.00%` | REJECTED: Win probability 21.3% < 92% minimum (no underdog lottery bets) |
| Exact Score: Chelsea FC 0 - 0 Tottenham Hotspur FC | Other | YES | `9.3%` | `4.8%` | `+4.5 п.п.` | `0.34%` | REJECTED: Win probability 9.3% < 92% minimum (no underdog lottery bets) |
| Will the price of Bitcoin be above $78,000 on Octo | Crypto | NO | `17.9%` | `5.1%` | `+12.8 п.п.` | `0.60%` | REJECTED: Win probability 17.9% < 92% minimum (no underdog lottery bets) |
| Will Ilija Srdanović be the next prime minister of | Geopolitics | NO | `98.0%` | `89.0%` | `+9.0 п.п.` | `2.00%` | REJECTED: Category cap reached (2/2 in Geopolitics) |
| Will the price of Ethereum be above $2,400 on Octo | Crypto | YES | `8.1%` | `3.9%` | `+4.2 п.п.` | `1.19%` | REJECTED: Win probability 8.1% < 92% minimum (no underdog lottery bets) |
| Will Iliana Iotova win the 2026 Bulgarian presiden | Geopolitics | YES | `23.9%` | `13.0%` | `+10.9 п.п.` | `1.00%` | REJECTED: Win probability 23.9% < 92% minimum (no underdog lottery bets) |
| Will FC Barcelona vs. Real Madrid CF end in a draw | Sports | NO | `96.2%` | `85.0%` | `+11.2 п.п.` | `1.00%` | REJECTED: Max open positions (4) reached |
| Israel x Iran ceasefire continues through October  | Geopolitics | NO | `15.7%` | `11.0%` | `+4.7 п.п.` | `1.00%` | REJECTED: Win probability 15.7% < 92% minimum (no underdog lottery bets) |
| Will Аndrey Gyurov win the next Bulgarian presiden | Geopolitics | YES | `19.4%` | `13.0%` | `+6.4 п.п.` | `1.00%` | REJECTED: Win probability 19.4% < 92% minimum (no underdog lottery bets) |
| Will the Fed increase interest rates by 25 bps aft | Macro | NO | `98.0%` | `94.0%` | `+4.0 п.п.` | `1.00%` | REJECTED: Max open positions (4) reached |
| Will the price of Bitcoin be above $82,000 on Octo | Crypto | YES | `21.1%` | `7.0%` | `+14.1 п.п.` | `1.00%` | REJECTED: Win probability 21.1% < 92% minimum (no underdog lottery bets) |
| Exact Score: Chelsea FC 0 - 0 Tottenham Hotspur FC | Other | YES | `9.5%` | `4.8%` | `+4.7 п.п.` | `0.34%` | REJECTED: Win probability 9.5% < 92% minimum (no underdog lottery bets) |
| Will the price of Bitcoin be above $78,000 on Octo | Crypto | NO | `18.0%` | `5.1%` | `+12.9 п.п.` | `0.40%` | REJECTED: Win probability 18.0% < 92% minimum (no underdog lottery bets) |
| Will Ilija Srdanović be the next prime minister of | Geopolitics | NO | `98.0%` | `89.0%` | `+9.0 п.п.` | `2.00%` | REJECTED: Category cap reached (2/2 in Geopolitics) |
| Will the price of Ethereum be above $2,400 on Octo | Crypto | YES | `8.4%` | `3.8%` | `+4.6 п.п.` | `0.96%` | REJECTED: Win probability 8.4% < 92% minimum (no underdog lottery bets) |
| Will Iliana Iotova win the 2026 Bulgarian presiden | Geopolitics | YES | `23.5%` | `13.0%` | `+10.5 п.п.` | `1.00%` | REJECTED: Win probability 23.5% < 92% minimum (no underdog lottery bets) |
| Will Bitcoin reach $82,000 on October 24? | Crypto | NO | `96.0%` | `91.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Max open positions (4) reached |
| Will FC Barcelona vs. Real Madrid CF end in a draw | Sports | NO | `90.7%` | `85.0%` | `+5.7 п.п.` | `1.00%` | REJECTED: Win probability 90.7% < 92% minimum (no underdog lottery bets) |
