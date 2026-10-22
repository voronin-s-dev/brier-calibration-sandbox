# 📊 Отчёт симулятора Polymarket (Устав Grok Bot — Демо-счёт)
**Обновлено:** `2026-10-22 19:33:55 UTC`

## 💰 Состояние виртуального портфеля
| Показатель | Значение | Правило устава |
| :--- | :--- | :--- |
| **Стартовый капитал** | `$50.00 USDC` | Не добавлять деньги |
| **Текущий баланс (Equity)** | **`$28.40 USDC`** (`-21.60$` / `-43.21%`) | Cash + Mark-to-Market по CLOB Bid |
| **Свободный кэш / В сделках** | `$17.69` / `$10.70 USDC` | До 8 открытых позиций, макс 8% банка |
| **Цель окупаемости подписки** | `$-21.60 / $60.00` (`0.0%`) | Цель: +$60.00 в месяц |
| **Просадка от пика (Текущая / Макс)** | `0.31%` / `6.31%` (Пик: `$28.49`) | Стоп-кран при просадке 40% |
| **Закрытых сделок / Win Rate** | `41` / `36.6%` | Brier Score: `0.3214` |

## 📂 Открытые позиции (4 / 8)
| # | Рынок | Кат. | Исход | Вход (Ask VWAP) | Текущий Bid | Оценка бота | Размер ($) | Нереализ. PnL | Источник |
| :- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| #35 | Will Bitcoin dip to $80,000 in October? | Crypto | **YES** | `0.610` | `0.710` | `99.5%` | `$1.11` | `$+0.18` | Kraken BTCUSDT 1m/1h Spot Klin |
| #38 | Will the Bank of Russia decrease the key rate after the | Other | **NO** | `0.900` | `0.730` | `97.0%` | `$3.30` | `$-0.62` | https://www.cbr.ru/eng/dkp/cal |
| #44 | Will Bitcoin dip to $80,000 on October 22? | Crypto | **NO** | `0.917` | `0.907` | `94.6%` | `$3.40` | `$-0.04` | https://www.binance.com/en/tra |
| #45 | US x Iran ceasefire continues through October 24? | Geopolitics | **YES** | `0.920` | `0.910` | `95.0%` | `$3.41` | `$-0.04` | Official NFL data feed |

## 🔍 Последние проверенные кандидаты и фильтр стакана CLOB
| Рынок | Кат. | Сторона | Оценка бота | Цена Ask | Перекос (Edge) | Проскальзывание CLOB | Решение |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Will Brighton & Hove Albion FC win on 2026-10-25? | Sports | YES | `36.0%` | `31.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Win probability 36.0% < 92% minimum (no underdog lottery bets) |
| Will Aleksandar Vučić – United Serbia win the most | Geopolitics | YES | `76.0%` | `71.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Win probability 76.0% < 92% minimum (no underdog lottery bets) |
| Spread: 76ers (-3.5) | Sports | NO | `97.5%` | `54.0%` | `+43.5 п.п.` | `1.00%` | REJECTED: Contract price $0.540 outside sweet spot [$0.84, $0.96] |
| Will Harry Kane win the 2026 Ballon d'Or? | Other | YES | `87.8%` | `76.3%` | `+11.5 п.п.` | `0.10%` | REJECTED: Win probability 87.8% < 92% minimum (no underdog lottery bets) |
| Will Lamine Yamal win the 2026 Ballon d'Or? | Other | YES | `27.6%` | `17.4%` | `+10.2 п.п.` | `0.40%` | REJECTED: Win probability 27.6% < 92% minimum (no underdog lottery bets) |
| Nuggets vs. Thunder | Sports | NO | `79.0%` | `74.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Win probability 79.0% < 92% minimum (no underdog lottery bets) |
| Spread: Bears (-3.5) | Sports | NO | `97.5%` | `57.0%` | `+40.5 п.п.` | `1.00%` | REJECTED: Contract price $0.570 outside sweet spot [$0.84, $0.96] |
| Will Estudiantes de La Plata win on 2026-10-22? | Sports | NO | `98.0%` | `93.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Max open positions (4) reached |
| Will the price of Ethereum be above $2,500 on Octo | Crypto | YES | `12.2%` | `7.3%` | `+4.9 п.п.` | `3.48%` | REJECTED: Win probability 12.2% < 92% minimum (no underdog lottery bets) |
| Will Iliana Iotova win the 2026 Bulgarian presiden | Geopolitics | YES | `12.7%` | `7.8%` | `+5.0 п.п.` | `3.95%` | REJECTED: Win probability 12.7% < 92% minimum (no underdog lottery bets) |
| Will Ethereum dip to $2,200 October 19-25? | Crypto | YES | `15.0%` | `7.5%` | `+7.5 п.п.` | `1.09%` | REJECTED: Win probability 15.0% < 92% minimum (no underdog lottery bets) |
| Will Bitcoin reach $86,000 October 19-25? | Crypto | YES | `21.3%` | `6.0%` | `+15.3 п.п.` | `2.00%` | REJECTED: Win probability 21.3% < 92% minimum (no underdog lottery bets) |
| Will Bitcoin dip to $78,000 October 19-25? | Crypto | YES | `33.7%` | `13.5%` | `+20.2 п.п.` | `0.66%` | REJECTED: Win probability 33.7% < 92% minimum (no underdog lottery bets) |
| Will Аndrey Gyurov win the next Bulgarian presiden | Geopolitics | NO | `94.1%` | `88.0%` | `+6.1 п.п.` | `1.00%` | REJECTED: Max open positions (4) reached |
| Will Bitcoin dip to $76,000 October 19-25? | Crypto | YES | `14.5%` | `4.9%` | `+9.6 п.п.` | `1.07%` | REJECTED: Win probability 14.5% < 92% minimum (no underdog lottery bets) |
| Will the price of Bitcoin be above $80,000 on Octo | Crypto | NO | `23.1%` | `15.0%` | `+8.1 п.п.` | `2.30%` | REJECTED: Win probability 23.1% < 92% minimum (no underdog lottery bets) |
| US x Iran ceasefire continues through October 24? | Geopolitics | YES | `95.0%` | `92.0%` | `+3.0 п.п.` | `1.00%` | EXECUTED BUY #45 ($3.41 @ 0.9200) |
| Will Brighton & Hove Albion FC win on 2026-10-25? | Sports | YES | `36.0%` | `31.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Win probability 36.0% < 92% minimum (no underdog lottery bets) |
