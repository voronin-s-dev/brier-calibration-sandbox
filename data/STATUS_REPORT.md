# 📊 Отчёт симулятора Polymarket (Устав Grok Bot — Демо-счёт)
**Обновлено:** `2026-10-22 05:27:33 UTC`

## 💰 Состояние виртуального портфеля
| Показатель | Значение | Правило устава |
| :--- | :--- | :--- |
| **Стартовый капитал** | `$50.00 USDC` | Не добавлять деньги |
| **Текущий баланс (Equity)** | **`$28.00 USDC`** (`-22.00$` / `-43.99%`) | Cash + Mark-to-Market по CLOB Bid |
| **Свободный кэш / В сделках** | `$17.34` / `$10.66 USDC` | До 8 открытых позиций, макс 8% банка |
| **Цель окупаемости подписки** | `$-22.00 / $60.00` (`0.0%`) | Цель: +$60.00 в месяц |
| **Просадка от пика (Текущая / Макс)** | `0.16%` / `6.31%` (Пик: `$28.05`) | Стоп-кран при просадке 40% |
| **Закрытых сделок / Win Rate** | `38` / `31.6%` | Brier Score: `0.3214` |

## 📂 Открытые позиции (4 / 8)
| # | Рынок | Кат. | Исход | Вход (Ask VWAP) | Текущий Bid | Оценка бота | Размер ($) | Нереализ. PnL | Источник |
| :- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| #35 | Will Bitcoin dip to $80,000 in October? | Crypto | **YES** | `0.610` | `0.490` | `99.5%` | `$1.11` | `$-0.22` | Kraken BTCUSDT 1m/1h Spot Klin |
| #36 | US x Iran ceasefire continues through October 22? | Geopolitics | **YES** | `0.953` | `0.941` | `97.8%` | `$3.30` | `$-0.04` | Official NFL data feed |
| #38 | Will the Bank of Russia decrease the key rate after the | Other | **NO** | `0.900` | `0.860` | `97.0%` | `$3.30` | `$-0.15` | https://www.cbr.ru/eng/dkp/cal |
| #42 | Bitcoin Up or Down on October 22? | Crypto | **NO** | `0.940` | `0.940` | `98.0%` | `$3.36` | `$+0.00` | https://www.binance.com/en/tra |

## 🔍 Последние проверенные кандидаты и фильтр стакана CLOB
| Рынок | Кат. | Сторона | Оценка бота | Цена Ask | Перекос (Edge) | Проскальзывание CLOB | Решение |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Will Elon Musk post 200-219 tweets from October 16 | Geopolitics | YES | `1.5%` | `100.0%` | `-98.5 п.п.` | `100.00%` | REJECTED: Edge -98.5 pp < 2 pp threshold (P_est=1.5% vs AskVWAP=100.0%) |
| Will Lamine Yamal win the 2026 Ballon d'Or? | Other | YES | `22.1%` | `16.6%` | `+5.5 п.п.` | `0.10%` | REJECTED: Win probability 22.1% < 92% minimum (no underdog lottery bets) |
| Will NDP win the most seats in the 2026 British Co | Geopolitics | YES | `17.5%` | `13.0%` | `+4.5 п.п.` | `2.00%` | REJECTED: Win probability 17.5% < 92% minimum (no underdog lottery bets) |
| Will the price of Bitcoin be above $86,000 on Octo | Crypto | YES | `9.4%` | `4.0%` | `+5.4 п.п.` | `1.10%` | REJECTED: Win probability 9.4% < 92% minimum (no underdog lottery bets) |
| Will Ethereum dip to $2,300 October 19-25? | Crypto | YES | `31.1%` | `13.0%` | `+18.1 п.п.` | `1.00%` | REJECTED: Win probability 31.1% < 92% minimum (no underdog lottery bets) |
| Exact Score: Celtic FC 0 - 0 RC Celta de Vigo? | Sports | YES | `11.0%` | `7.0%` | `+4.0 п.п.` | `2.00%` | REJECTED: Win probability 11.0% < 92% minimum (no underdog lottery bets) |
| Will Bitcoin dip to $80,000 on October 22? | Crypto | YES | `17.3%` | `4.5%` | `+12.8 п.п.` | `0.56%` | REJECTED: Win probability 17.3% < 92% minimum (no underdog lottery bets) |
| Will the price of Bitcoin be above $78,000 on Octo | Crypto | NO | `13.3%` | `5.6%` | `+7.7 п.п.` | `2.38%` | REJECTED: Win probability 13.3% < 92% minimum (no underdog lottery bets) |
| Will Ethereum reach $2,600 October 19-25? | Crypto | YES | `27.1%` | `12.0%` | `+15.1 п.п.` | `1.00%` | REJECTED: Win probability 27.1% < 92% minimum (no underdog lottery bets) |
| Exact Score: Celtic FC 2 - 2 RC Celta de Vigo? | Sports | NO | `98.5%` | `94.0%` | `+4.5 п.п.` | `2.00%` | REJECTED: Max open positions (4) reached |
| Will Iliana Iotova win the 2026 Bulgarian presiden | Geopolitics | YES | `11.4%` | `4.9%` | `+6.5 п.п.` | `0.10%` | REJECTED: Win probability 11.4% < 92% minimum (no underdog lottery bets) |
| Will Ethereum dip to $2,200 October 19-25? | Crypto | YES | `9.8%` | `5.1%` | `+4.7 п.п.` | `1.49%` | REJECTED: Win probability 9.8% < 92% minimum (no underdog lottery bets) |
| Will Bitcoin dip to $76,000 October 19-25? | Crypto | YES | `9.9%` | `3.4%` | `+6.5 п.п.` | `0.50%` | REJECTED: Win probability 9.9% < 92% minimum (no underdog lottery bets) |
| Will Bitcoin dip to $78,000 October 19-25? | Crypto | YES | `23.2%` | `8.0%` | `+15.2 п.п.` | `1.09%` | REJECTED: Win probability 23.2% < 92% minimum (no underdog lottery bets) |
| Will the price of Bitcoin be above $84,000 on Octo | Crypto | YES | `17.3%` | `13.0%` | `+4.3 п.п.` | `2.00%` | REJECTED: Win probability 17.3% < 92% minimum (no underdog lottery bets) |
| Will Bitcoin reach $88,000 October 19-25? | Crypto | YES | `20.4%` | `6.0%` | `+14.4 п.п.` | `1.00%` | REJECTED: Win probability 20.4% < 92% minimum (no underdog lottery bets) |
| Will the Bank of Russia make no change to the key  | Other | NO | `18.2%` | `14.0%` | `+4.2 п.п.` | `2.00%` | REJECTED: Win probability 18.2% < 92% minimum (no underdog lottery bets) |
| Will the price of Ethereum be above $2,400 on Octo | Crypto | NO | `20.8%` | `12.2%` | `+8.6 п.п.` | `4.40%` | REJECTED: Win probability 20.8% < 92% minimum (no underdog lottery bets) |
