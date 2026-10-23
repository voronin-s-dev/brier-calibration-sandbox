# 📊 Отчёт симулятора Polymarket (Устав Grok Bot — Демо-счёт)
**Обновлено:** `2026-10-23 23:43:05 UTC`

## 💰 Состояние виртуального портфеля
| Показатель | Значение | Правило устава |
| :--- | :--- | :--- |
| **Стартовый капитал** | `$50.00 USDC` | Не добавлять деньги |
| **Текущий баланс (Equity)** | **`$29.86 USDC`** (`-20.14$` / `-40.28%`) | Cash + Mark-to-Market по CLOB Bid |
| **Свободный кэш / В сделках** | `$18.04` / `$11.82 USDC` | До 8 открытых позиций, макс 8% банка |
| **Цель окупаемости подписки** | `$-20.14 / $60.00` (`0.0%`) | Цель: +$60.00 в месяц |
| **Просадка от пика (Текущая / Макс)** | `0.91%` / `6.31%` (Пик: `$30.14`) | Стоп-кран при просадке 40% |
| **Закрытых сделок / Win Rate** | `46` / `41.3%` | Brier Score: `0.2574` |

## 📂 Открытые позиции (4 / 8)
| # | Рынок | Кат. | Исход | Вход (Ask VWAP) | Текущий Bid | Оценка бота | Размер ($) | Нереализ. PnL | Источник |
| :- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| #35 | Will Bitcoin dip to $80,000 in October? | Crypto | **YES** | `0.610` | `0.750` | `99.5%` | `$1.11` | `$+0.25` | Kraken BTCUSDT 1m/1h Spot Klin |
| #45 | US x Iran ceasefire continues through October 24? | Geopolitics | **YES** | `0.920` | `0.920` | `96.0%` | `$3.41` | `$-0.00` | Official NFL data feed |
| #47 | Israel x Iran ceasefire continues through October 24? | Geopolitics | **YES** | `0.950` | `0.930` | `97.5%` | `$3.57` | `$-0.08` | the totality of information av |
| #50 | Spread: Manchester City FC (-3.5) | Sports | **NO** | `0.940` | `0.930` | `97.5%` | `$3.59` | `$-0.04` | https://www.premierleague.com/ |

## 🔍 Последние проверенные кандидаты и фильтр стакана CLOB
| Рынок | Кат. | Сторона | Оценка бота | Цена Ask | Перекос (Edge) | Проскальзывание CLOB | Решение |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Will Harry Kane win the 2026 Ballon d'Or? | Other | YES | `85.7%` | `76.8%` | `+8.9 п.п.` | `0.10%` | REJECTED: Win probability 85.7% < 92% minimum (no underdog lottery bets) |
| Grizzlies vs. Warriors | Sports | YES | `44.6%` | `40.0%` | `+4.6 п.п.` | `1.00%` | REJECTED: Win probability 44.6% < 92% minimum (no underdog lottery bets) |
| LoL: LOS vs T1 (BO1) - Worlds Group Stage | Sports | YES | `1.5%` | `100.0%` | `-98.5 п.п.` | `100.00%` | REJECTED: Edge -98.5 pp < 2 pp threshold (P_est=1.5% vs AskVWAP=100.0%) |
| Will the price of Ethereum be above $2,300 on Octo | Crypto | NO | `18.9%` | `7.2%` | `+11.7 п.п.` | `1.80%` | REJECTED: Win probability 18.9% < 92% minimum (no underdog lottery bets) |
| Will Ethereum dip to $2,200 October 19-25? | Crypto | YES | `9.4%` | `3.0%` | `+6.4 п.п.` | `0.27%` | REJECTED: Win probability 9.4% < 92% minimum (no underdog lottery bets) |
| Will Bitcoin reach $84,000 October 19-25? | Crypto | YES | `26.8%` | `3.2%` | `+23.6 п.п.` | `0.70%` | REJECTED: Win probability 26.8% < 92% minimum (no underdog lottery bets) |
| Will the price of Bitcoin be between $80,000 and $ | Crypto | NO | `46.8%` | `12.8%` | `+34.0 п.п.` | `1.82%` | REJECTED: Win probability 46.8% < 92% minimum (no underdog lottery bets) |
| Will the price of Bitcoin be between $78,000 and $ | Crypto | YES | `21.7%` | `7.9%` | `+13.8 п.п.` | `2.10%` | REJECTED: Win probability 21.7% < 92% minimum (no underdog lottery bets) |
| Will the price of Bitcoin be above $80,000 on Octo | Crypto | NO | `33.0%` | `16.1%` | `+16.9 п.п.` | `1.00%` | REJECTED: Win probability 33.0% < 92% minimum (no underdog lottery bets) |
| Will Ethereum reach $2,500 October 19-25? | Crypto | YES | `23.3%` | `6.9%` | `+16.4 п.п.` | `2.06%` | REJECTED: Win probability 23.3% < 92% minimum (no underdog lottery bets) |
| Will Iliana Iotova win the 2026 Bulgarian presiden | Geopolitics | YES | `24.5%` | `15.0%` | `+9.5 п.п.` | `2.01%` | REJECTED: Win probability 24.5% < 92% minimum (no underdog lottery bets) |
| Will FC Barcelona vs. Real Madrid CF end in a draw | Sports | NO | `96.2%` | `85.0%` | `+11.2 п.п.` | `1.00%` | REJECTED: Max open positions (4) reached |
| Will Ilija Srdanović be the next prime minister of | Geopolitics | YES | `22.3%` | `14.0%` | `+8.3 п.п.` | `2.00%` | REJECTED: Win probability 22.3% < 92% minimum (no underdog lottery bets) |
| Will Bitcoin dip to $76,000 October 19-25? | Crypto | YES | `10.2%` | `2.9%` | `+7.3 п.п.` | `0.10%` | REJECTED: Win probability 10.2% < 92% minimum (no underdog lottery bets) |
| Israel x Iran ceasefire continues through October  | Geopolitics | NO | `21.3%` | `13.0%` | `+8.3 п.п.` | `2.00%` | REJECTED: Win probability 21.3% < 92% minimum (no underdog lottery bets) |
| Will Ethereum dip to $2,350 on October 23? | Crypto | YES | `99.5%` | `15.0%` | `+84.5 п.п.` | `5.00%` | REJECTED: Contract price $0.150 outside sweet spot [$0.84, $0.96] |
| Will Аndrey Gyurov win the next Bulgarian presiden | Geopolitics | YES | `19.2%` | `13.0%` | `+6.2 п.п.` | `1.00%` | REJECTED: Win probability 19.2% < 92% minimum (no underdog lottery bets) |
| Counter-Strike: paiN vs Imperial (BO3) - Circuit X | Sports | NO | `96.2%` | `91.0%` | `+5.1 п.п.` | `1.00%` | REJECTED: Max open positions (4) reached |
