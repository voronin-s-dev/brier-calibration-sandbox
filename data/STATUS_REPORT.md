# 📊 Отчёт симулятора Polymarket (Устав Grok Bot — Демо-счёт)
**Обновлено:** `2026-10-23 01:42:31 UTC`

## 💰 Состояние виртуального портфеля
| Показатель | Значение | Правило устава |
| :--- | :--- | :--- |
| **Стартовый капитал** | `$50.00 USDC` | Не добавлять деньги |
| **Текущий баланс (Equity)** | **`$28.85 USDC`** (`-21.15$` / `-42.31%`) | Cash + Mark-to-Market по CLOB Bid |
| **Свободный кэш / В сделках** | `$17.69` / `$11.15 USDC` | До 8 открытых позиций, макс 8% банка |
| **Цель окупаемости подписки** | `$-21.15 / $60.00` (`0.0%`) | Цель: +$60.00 в месяц |
| **Просадка от пика (Текущая / Макс)** | `0.15%` / `6.31%` (Пик: `$28.89`) | Стоп-кран при просадке 40% |
| **Закрытых сделок / Win Rate** | `41` / `36.6%` | Brier Score: `0.3214` |

## 📂 Открытые позиции (4 / 8)
| # | Рынок | Кат. | Исход | Вход (Ask VWAP) | Текущий Bid | Оценка бота | Размер ($) | Нереализ. PnL | Источник |
| :- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| #35 | Will Bitcoin dip to $80,000 in October? | Crypto | **YES** | `0.610` | `0.700` | `99.5%` | `$1.11` | `$+0.16` | Kraken BTCUSDT 1m/1h Spot Klin |
| #38 | Will the Bank of Russia decrease the key rate after the | Other | **NO** | `0.900` | `0.800` | `97.0%` | `$3.30` | `$-0.37` | https://www.cbr.ru/eng/dkp/cal |
| #44 | Will Bitcoin dip to $80,000 on October 22? | Crypto | **NO** | `0.917` | `0.964` | `98.5%` | `$3.40` | `$+0.17` | https://www.binance.com/en/tra |
| #45 | US x Iran ceasefire continues through October 24? | Geopolitics | **YES** | `0.920` | `0.910` | `95.0%` | `$3.41` | `$-0.04` | Official NFL data feed |

## 🔍 Последние проверенные кандидаты и фильтр стакана CLOB
| Рынок | Кат. | Сторона | Оценка бота | Цена Ask | Перекос (Edge) | Проскальзывание CLOB | Решение |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Will Flavio Bolsonaro win the most votes in the se | Geopolitics | NO | `35.0%` | `31.0%` | `+4.0 п.п.` | `2.00%` | REJECTED: Win probability 35.0% < 92% minimum (no underdog lottery bets) |
| Will Aleksandar Vučić be the next Prime Minister o | Geopolitics | YES | `75.8%` | `70.6%` | `+5.2 п.п.` | `0.49%` | REJECTED: Win probability 75.8% < 92% minimum (no underdog lottery bets) |
| Will Brighton & Hove Albion FC win on 2026-10-25? | Sports | YES | `36.0%` | `31.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Win probability 36.0% < 92% minimum (no underdog lottery bets) |
| Will Elon Musk post 240-259 tweets from October 16 | Geopolitics | YES | `1.5%` | `100.0%` | `-98.5 п.п.` | `100.00%` | REJECTED: Edge -98.5 pp < 2 pp threshold (P_est=1.5% vs AskVWAP=100.0%) |
| Will Aleksandar Vučić – United Serbia win the most | Geopolitics | YES | `74.0%` | `69.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Win probability 74.0% < 92% minimum (no underdog lottery bets) |
| Will Harry Kane win the 2026 Ballon d'Or? | Other | YES | `86.9%` | `75.0%` | `+11.9 п.п.` | `0.10%` | REJECTED: Win probability 86.9% < 92% minimum (no underdog lottery bets) |
| Will the price of Bitcoin be above $76,000 on Octo | Crypto | NO | `10.6%` | `4.8%` | `+5.8 п.п.` | `2.28%` | REJECTED: Win probability 10.6% < 92% minimum (no underdog lottery bets) |
| Will the price of Ethereum be above $2,300 on Octo | Crypto | NO | `16.8%` | `8.9%` | `+7.9 п.п.` | `1.15%` | REJECTED: Win probability 16.8% < 92% minimum (no underdog lottery bets) |
| Will Ethereum reach $2,600 October 19-25? | Crypto | YES | `11.4%` | `4.6%` | `+6.8 п.п.` | `0.60%` | REJECTED: Win probability 11.4% < 92% minimum (no underdog lottery bets) |
| Will the price of Ethereum be above $2,500 on Octo | Crypto | YES | `10.8%` | `4.8%` | `+6.0 п.п.` | `0.59%` | REJECTED: Win probability 10.8% < 92% minimum (no underdog lottery bets) |
| Will Ethereum dip to $2,200 October 19-25? | Crypto | YES | `13.4%` | `5.6%` | `+7.8 п.п.` | `0.99%` | REJECTED: Win probability 13.4% < 92% minimum (no underdog lottery bets) |
| Will Bitcoin reach $86,000 October 19-25? | Crypto | YES | `19.7%` | `4.8%` | `+14.9 п.п.` | `0.80%` | REJECTED: Win probability 19.7% < 92% minimum (no underdog lottery bets) |
| Will Bitcoin dip to $78,000 October 19-25? | Crypto | YES | `32.2%` | `13.1%` | `+19.1 п.п.` | `0.81%` | REJECTED: Win probability 32.2% < 92% minimum (no underdog lottery bets) |
| Will Iliana Iotova win the next Bulgarian presiden | Geopolitics | NO | `17.8%` | `13.0%` | `+4.8 п.п.` | `1.00%` | REJECTED: Win probability 17.8% < 92% minimum (no underdog lottery bets) |
| Will Аndrey Gyurov win the next Bulgarian presiden | Geopolitics | NO | `94.4%` | `89.0%` | `+5.4 п.п.` | `1.00%` | REJECTED: Max open positions (4) reached |
| Will Bitcoin dip to $76,000 October 19-25? | Crypto | YES | `12.8%` | `3.9%` | `+8.9 п.п.` | `0.40%` | REJECTED: Win probability 12.8% < 92% minimum (no underdog lottery bets) |
| Will the price of Bitcoin be above $80,000 on Octo | Crypto | NO | `19.8%` | `12.8%` | `+7.0 п.п.` | `2.18%` | REJECTED: Win probability 19.8% < 92% minimum (no underdog lottery bets) |
| Will Flavio Bolsonaro win the most votes in the se | Geopolitics | NO | `35.0%` | `31.0%` | `+4.0 п.п.` | `2.00%` | REJECTED: Win probability 35.0% < 92% minimum (no underdog lottery bets) |
