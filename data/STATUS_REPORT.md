# 📊 Отчёт симулятора Polymarket (Устав Grok Bot — Демо-счёт)
**Обновлено:** `2026-10-23 01:33:09 UTC`

## 💰 Состояние виртуального портфеля
| Показатель | Значение | Правило устава |
| :--- | :--- | :--- |
| **Стартовый капитал** | `$50.00 USDC` | Не добавлять деньги |
| **Текущий баланс (Equity)** | **`$28.89 USDC`** (`-21.11$` / `-42.22%`) | Cash + Mark-to-Market по CLOB Bid |
| **Свободный кэш / В сделках** | `$17.69` / `$11.20 USDC` | До 8 открытых позиций, макс 8% банка |
| **Цель окупаемости подписки** | `$-21.11 / $60.00` (`0.0%`) | Цель: +$60.00 в месяц |
| **Просадка от пика (Текущая / Макс)** | `0.00%` / `6.31%` (Пик: `$28.89`) | Стоп-кран при просадке 40% |
| **Закрытых сделок / Win Rate** | `41` / `36.6%` | Brier Score: `0.3214` |

## 📂 Открытые позиции (4 / 8)
| # | Рынок | Кат. | Исход | Вход (Ask VWAP) | Текущий Bid | Оценка бота | Размер ($) | Нереализ. PnL | Источник |
| :- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| #35 | Will Bitcoin dip to $80,000 in October? | Crypto | **YES** | `0.610` | `0.700` | `99.5%` | `$1.11` | `$+0.16` | Kraken BTCUSDT 1m/1h Spot Klin |
| #38 | Will the Bank of Russia decrease the key rate after the | Other | **NO** | `0.900` | `0.800` | `97.0%` | `$3.30` | `$-0.37` | https://www.cbr.ru/eng/dkp/cal |
| #44 | Will Bitcoin dip to $80,000 on October 22? | Crypto | **NO** | `0.917` | `0.976` | `98.5%` | `$3.40` | `$+0.22` | https://www.binance.com/en/tra |
| #45 | US x Iran ceasefire continues through October 24? | Geopolitics | **YES** | `0.920` | `0.910` | `95.0%` | `$3.41` | `$-0.04` | Official NFL data feed |

## 🔍 Последние проверенные кандидаты и фильтр стакана CLOB
| Рынок | Кат. | Сторона | Оценка бота | Цена Ask | Перекос (Edge) | Проскальзывание CLOB | Решение |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Will Flavio Bolsonaro win the most votes in the se | Geopolitics | NO | `35.0%` | `31.0%` | `+4.0 п.п.` | `2.00%` | REJECTED: Win probability 35.0% < 92% minimum (no underdog lottery bets) |
| Will Aleksandar Vučić be the next Prime Minister o | Geopolitics | YES | `75.8%` | `70.6%` | `+5.2 п.п.` | `0.49%` | REJECTED: Win probability 75.8% < 92% minimum (no underdog lottery bets) |
| Will Brighton & Hove Albion FC win on 2026-10-25? | Sports | YES | `36.0%` | `31.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Win probability 36.0% < 92% minimum (no underdog lottery bets) |
| Will Aleksandar Vučić – United Serbia win the most | Geopolitics | YES | `74.0%` | `69.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Win probability 74.0% < 92% minimum (no underdog lottery bets) |
| Will Harry Kane win the 2026 Ballon d'Or? | Other | YES | `87.5%` | `75.0%` | `+12.5 п.п.` | `0.10%` | REJECTED: Win probability 87.5% < 92% minimum (no underdog lottery bets) |
| Will the price of Bitcoin be above $76,000 on Octo | Crypto | NO | `10.6%` | `4.8%` | `+5.9 п.п.` | `2.26%` | REJECTED: Win probability 10.6% < 92% minimum (no underdog lottery bets) |
| Will the price of Ethereum be above $2,300 on Octo | Crypto | NO | `16.7%` | `10.5%` | `+6.2 п.п.` | `1.25%` | REJECTED: Win probability 16.7% < 92% minimum (no underdog lottery bets) |
| Will Ethereum reach $2,600 October 19-25? | Crypto | YES | `11.5%` | `3.9%` | `+7.6 п.п.` | `0.70%` | REJECTED: Win probability 11.5% < 92% minimum (no underdog lottery bets) |
| Will the price of Ethereum be above $2,500 on Octo | Crypto | YES | `10.9%` | `4.7%` | `+6.2 п.п.` | `1.16%` | REJECTED: Win probability 10.9% < 92% minimum (no underdog lottery bets) |
| Will the price of Bitcoin be above $80,000 on Octo | Crypto | NO | `28.1%` | `18.0%` | `+10.1 п.п.` | `1.80%` | REJECTED: Win probability 28.1% < 92% minimum (no underdog lottery bets) |
| Will Ethereum dip to $2,200 October 19-25? | Crypto | YES | `13.3%` | `7.0%` | `+6.3 п.п.` | `2.29%` | REJECTED: Win probability 13.3% < 92% minimum (no underdog lottery bets) |
| Will Bitcoin reach $86,000 October 19-25? | Crypto | YES | `19.8%` | `4.3%` | `+15.5 п.п.` | `0.50%` | REJECTED: Win probability 19.8% < 92% minimum (no underdog lottery bets) |
| Will Bitcoin dip to $78,000 October 19-25? | Crypto | YES | `31.7%` | `12.4%` | `+19.4 п.п.` | `0.56%` | REJECTED: Win probability 31.7% < 92% minimum (no underdog lottery bets) |
| Will Iliana Iotova win the next Bulgarian presiden | Geopolitics | NO | `17.7%` | `13.0%` | `+4.7 п.п.` | `1.00%` | REJECTED: Win probability 17.7% < 92% minimum (no underdog lottery bets) |
| Will Bitcoin reach $88,000 October 19-25? | Crypto | YES | `8.3%` | `2.6%` | `+5.8 п.п.` | `0.90%` | REJECTED: Win probability 8.3% < 92% minimum (no underdog lottery bets) |
| Will Аndrey Gyurov win the next Bulgarian presiden | Geopolitics | NO | `95.0%` | `89.0%` | `+6.0 п.п.` | `1.00%` | REJECTED: Max open positions (4) reached |
| Will Bitcoin dip to $76,000 October 19-25? | Crypto | YES | `12.8%` | `3.6%` | `+9.2 п.п.` | `0.10%` | REJECTED: Win probability 12.8% < 92% minimum (no underdog lottery bets) |
| Will the price of Bitcoin be above $80,000 on Octo | Crypto | NO | `19.1%` | `12.5%` | `+6.7 п.п.` | `1.17%` | REJECTED: Win probability 19.1% < 92% minimum (no underdog lottery bets) |
