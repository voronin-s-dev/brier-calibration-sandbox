# 📊 Отчёт симулятора Polymarket (Устав Grok Bot — Демо-счёт)
**Обновлено:** `2026-10-22 10:51:13 UTC`

## 💰 Состояние виртуального портфеля
| Показатель | Значение | Правило устава |
| :--- | :--- | :--- |
| **Стартовый капитал** | `$50.00 USDC` | Не добавлять деньги |
| **Текущий баланс (Equity)** | **`$28.10 USDC`** (`-21.90$` / `-43.79%`) | Cash + Mark-to-Market по CLOB Bid |
| **Свободный кэш / В сделках** | `$17.34` / `$10.76 USDC` | До 8 открытых позиций, макс 8% банка |
| **Цель окупаемости подписки** | `$-21.90 / $60.00` (`0.0%`) | Цель: +$60.00 в месяц |
| **Просадка от пика (Текущая / Макс)** | `0.55%` / `6.31%` (Пик: `$28.26`) | Стоп-кран при просадке 40% |
| **Закрытых сделок / Win Rate** | `38` / `31.6%` | Brier Score: `0.3214` |

## 📂 Открытые позиции (4 / 8)
| # | Рынок | Кат. | Исход | Вход (Ask VWAP) | Текущий Bid | Оценка бота | Размер ($) | Нереализ. PnL | Источник |
| :- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| #35 | Will Bitcoin dip to $80,000 in October? | Crypto | **YES** | `0.610` | `0.610` | `99.5%` | `$1.11` | `$+0.00` | Kraken BTCUSDT 1m/1h Spot Klin |
| #36 | US x Iran ceasefire continues through October 22? | Geopolitics | **YES** | `0.953` | `0.950` | `98.0%` | `$3.30` | `$-0.01` | Official NFL data feed |
| #38 | Will the Bank of Russia decrease the key rate after the | Other | **NO** | `0.900` | `0.790` | `97.0%` | `$3.30` | `$-0.40` | https://www.cbr.ru/eng/dkp/cal |
| #42 | Bitcoin Up or Down on October 22? | Crypto | **NO** | `0.940` | `0.970` | `98.5%` | `$3.36` | `$+0.11` | https://www.binance.com/en/tra |

## 🔍 Последние проверенные кандидаты и фильтр стакана CLOB
| Рынок | Кат. | Сторона | Оценка бота | Цена Ask | Перекос (Edge) | Проскальзывание CLOB | Решение |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Will Aleksandar Vučić – United Serbia win the most | Geopolitics | YES | `73.0%` | `68.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Win probability 73.0% < 92% minimum (no underdog lottery bets) |
| Will Lamine Yamal win the 2026 Ballon d'Or? | Other | YES | `28.9%` | `17.1%` | `+11.8 п.п.` | `0.16%` | REJECTED: Win probability 28.9% < 92% minimum (no underdog lottery bets) |
| Will the price of Ethereum be above $2,300 on Octo | Crypto | NO | `15.3%` | `9.0%` | `+6.3 п.п.` | `2.90%` | REJECTED: Win probability 15.3% < 92% minimum (no underdog lottery bets) |
| Will NDP win the most seats in the 2026 British Co | Geopolitics | YES | `19.0%` | `15.0%` | `+4.0 п.п.` | `3.00%` | REJECTED: Win probability 19.0% < 92% minimum (no underdog lottery bets) |
| Will Ethereum reach $2,600 October 19-25? | Crypto | YES | `18.4%` | `5.0%` | `+13.4 п.п.` | `1.39%` | REJECTED: Win probability 18.4% < 92% minimum (no underdog lottery bets) |
| Will the price of Bitcoin be above $84,000 on Octo | Crypto | YES | `18.2%` | `10.0%` | `+8.2 п.п.` | `1.00%` | REJECTED: Win probability 18.2% < 92% minimum (no underdog lottery bets) |
| Will the price of Ethereum be above $2,500 on Octo | Crypto | YES | `18.7%` | `11.0%` | `+7.7 п.п.` | `3.00%` | REJECTED: Win probability 18.7% < 92% minimum (no underdog lottery bets) |
| Exact Score: Celtic FC 2 - 2 RC Celta de Vigo? | Sports | NO | `98.5%` | `94.0%` | `+4.5 п.п.` | `1.00%` | REJECTED: Max open positions (4) reached |
| Will Ethereum dip to $2,200 October 19-25? | Crypto | YES | `12.4%` | `4.8%` | `+7.7 п.п.` | `0.59%` | REJECTED: Win probability 12.4% < 92% minimum (no underdog lottery bets) |
| Will Bitcoin reach $88,000 October 19-25? | Crypto | YES | `14.3%` | `2.9%` | `+11.4 п.п.` | `0.10%` | REJECTED: Win probability 14.3% < 92% minimum (no underdog lottery bets) |
| Will Bitcoin dip to $76,000 October 19-25? | Crypto | YES | `12.3%` | `3.8%` | `+8.5 п.п.` | `0.10%` | REJECTED: Win probability 12.3% < 92% minimum (no underdog lottery bets) |
| Will Bitcoin dip to $78,000 October 19-25? | Crypto | YES | `28.7%` | `11.2%` | `+17.5 п.п.` | `0.10%` | REJECTED: Win probability 28.7% < 92% minimum (no underdog lottery bets) |
| Will Bitcoin reach $86,000 October 19-25? | Crypto | YES | `29.9%` | `10.0%` | `+19.9 п.п.` | `1.82%` | REJECTED: Win probability 29.9% < 92% minimum (no underdog lottery bets) |
| Will Bitcoin dip to $80,000 on October 22? | Crypto | YES | `25.0%` | `14.6%` | `+10.4 п.п.` | `0.94%` | REJECTED: Win probability 25.0% < 92% minimum (no underdog lottery bets) |
| Will the price of Bitcoin be above $80,000 on Octo | Crypto | NO | `18.9%` | `12.6%` | `+6.3 п.п.` | `0.90%` | REJECTED: Win probability 18.9% < 92% minimum (no underdog lottery bets) |
| Will Kylian Mbappé win the 2026 Ballon d'Or? | Other | YES | `9.6%` | `4.1%` | `+5.5 п.п.` | `0.10%` | REJECTED: Win probability 9.6% < 92% minimum (no underdog lottery bets) |
| Will Harry Kane win the 2026 Ballon d'Or? | Other | YES | `85.8%` | `76.3%` | `+9.5 п.п.` | `0.10%` | REJECTED: Win probability 85.8% < 92% minimum (no underdog lottery bets) |
| Will Lamine Yamal win the 2026 Ballon d'Or? | Other | YES | `28.9%` | `17.1%` | `+11.8 п.п.` | `0.60%` | REJECTED: Win probability 28.9% < 92% minimum (no underdog lottery bets) |
