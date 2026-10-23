# 📊 Отчёт симулятора Polymarket (Устав Grok Bot — Демо-счёт)
**Обновлено:** `2026-10-23 06:45:14 UTC`

## 💰 Состояние виртуального портфеля
| Показатель | Значение | Правило устава |
| :--- | :--- | :--- |
| **Стартовый капитал** | `$50.00 USDC` | Не добавлять деньги |
| **Текущий баланс (Equity)** | **`$28.71 USDC`** (`-21.29$` / `-42.59%`) | Cash + Mark-to-Market по CLOB Bid |
| **Свободный кэш / В сделках** | `$17.96` / `$10.75 USDC` | До 8 открытых позиций, макс 8% банка |
| **Цель окупаемости подписки** | `$-21.29 / $60.00` (`0.0%`) | Цель: +$60.00 в месяц |
| **Просадка от пика (Текущая / Макс)** | `0.64%` / `6.31%` (Пик: `$28.89`) | Стоп-кран при просадке 40% |
| **Закрытых сделок / Win Rate** | `42` / `38.1%` | Brier Score: `0.2860` |

## 📂 Открытые позиции (4 / 8)
| # | Рынок | Кат. | Исход | Вход (Ask VWAP) | Текущий Bid | Оценка бота | Размер ($) | Нереализ. PnL | Источник |
| :- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| #35 | Will Bitcoin dip to $80,000 in October? | Crypto | **YES** | `0.610` | `0.620` | `99.5%` | `$1.11` | `$+0.02` | Kraken BTCUSDT 1m/1h Spot Klin |
| #38 | Will the Bank of Russia decrease the key rate after the | Other | **NO** | `0.900` | `0.760` | `97.0%` | `$3.30` | `$-0.51` | https://www.cbr.ru/eng/dkp/cal |
| #45 | US x Iran ceasefire continues through October 24? | Geopolitics | **YES** | `0.920` | `0.920` | `96.0%` | `$3.41` | `$-0.00` | Official NFL data feed |
| #46 | Will the price of Bitcoin be above $84,000 on October 2 | Crypto | **NO** | `0.959` | `0.954` | `98.5%` | `$3.44` | `$-0.02` | https://www.binance.com/en/tra |

## 🔍 Последние проверенные кандидаты и фильтр стакана CLOB
| Рынок | Кат. | Сторона | Оценка бота | Цена Ask | Перекос (Edge) | Проскальзывание CLOB | Решение |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Will Harry Kane win the 2026 Ballon d'Or? | Other | YES | `86.7%` | `77.0%` | `+9.7 п.п.` | `0.20%` | REJECTED: Win probability 86.7% < 92% minimum (no underdog lottery bets) |
| Will Benjamin Netanyahu be the next Prime Minister | Geopolitics | NO | `77.0%` | `72.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Win probability 77.0% < 92% minimum (no underdog lottery bets) |
| Spread: Manchester City FC (-3.5) | Sports | NO | `97.5%` | `93.0%` | `+4.5 п.п.` | `1.00%` | REJECTED: Max open positions (4) reached |
| Will Bitcoin dip to $79,000 on October 23? | Crypto | YES | `15.1%` | `4.2%` | `+10.9 п.п.` | `0.25%` | REJECTED: Win probability 15.1% < 92% minimum (no underdog lottery bets) |
| Will Bitcoin reach $85,000 on October 23? | Crypto | YES | `10.5%` | `3.4%` | `+7.1 п.п.` | `0.70%` | REJECTED: Win probability 10.5% < 92% minimum (no underdog lottery bets) |
| Will the price of Bitcoin be above $76,000 on Octo | Crypto | NO | `8.9%` | `4.2%` | `+4.7 п.п.` | `1.60%` | REJECTED: Win probability 8.9% < 92% minimum (no underdog lottery bets) |
| Will Bitcoin dip to $80,000 on October 23? | Crypto | YES | `34.2%` | `15.0%` | `+19.1 п.п.` | `1.00%` | REJECTED: Win probability 34.2% < 92% minimum (no underdog lottery bets) |
| Will Ethereum reach $2,600 October 19-25? | Crypto | YES | `12.5%` | `3.5%` | `+9.0 п.п.` | `0.20%` | REJECTED: Win probability 12.5% < 92% minimum (no underdog lottery bets) |
| Will the price of Ethereum be above $2,500 on Octo | Crypto | YES | `12.2%` | `6.0%` | `+6.2 п.п.` | `1.20%` | REJECTED: Win probability 12.2% < 92% minimum (no underdog lottery bets) |
| Will the price of Ethereum be above $2,300 on Octo | Crypto | NO | `11.5%` | `5.3%` | `+6.2 п.п.` | `0.61%` | REJECTED: Win probability 11.5% < 92% minimum (no underdog lottery bets) |
| Will Likud win 30-34 seats in the 2026 Israeli leg | Geopolitics | NO | `97.4%` | `93.0%` | `+4.4 п.п.` | `1.00%` | REJECTED: Max open positions (4) reached |
| Will Ethereum dip to $2,200 October 19-25? | Crypto | YES | `9.5%` | `3.3%` | `+6.2 п.п.` | `0.28%` | REJECTED: Win probability 9.5% < 92% minimum (no underdog lottery bets) |
| Will Naftali Bennett be the next Prime Minister of | Geopolitics | YES | `21.5%` | `16.0%` | `+5.5 п.п.` | `1.00%` | REJECTED: Win probability 21.5% < 92% minimum (no underdog lottery bets) |
| Will Bitcoin dip to $78,000 October 19-25? | Crypto | YES | `25.1%` | `6.2%` | `+18.9 п.п.` | `0.10%` | REJECTED: Win probability 25.1% < 92% minimum (no underdog lottery bets) |
| Will Bitcoin reach $86,000 October 19-25? | Crypto | YES | `21.9%` | `5.0%` | `+16.9 п.п.` | `0.10%` | REJECTED: Win probability 21.9% < 92% minimum (no underdog lottery bets) |
| Will Bitcoin reach $88,000 October 19-25? | Crypto | YES | `9.1%` | `2.4%` | `+6.7 п.п.` | `0.40%` | REJECTED: Win probability 9.1% < 92% minimum (no underdog lottery bets) |
| Will Iliana Iotova win the next Bulgarian presiden | Geopolitics | NO | `19.1%` | `13.0%` | `+6.1 п.п.` | `1.00%` | REJECTED: Win probability 19.1% < 92% minimum (no underdog lottery bets) |
| Will Brighton & Hove Albion FC win on 2026-10-25? | Sports | YES | `36.0%` | `31.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Win probability 36.0% < 92% minimum (no underdog lottery bets) |
