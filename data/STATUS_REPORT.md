# 📊 Отчёт симулятора Polymarket (Устав Grok Bot — Демо-счёт)
**Обновлено:** `2026-10-23 20:27:57 UTC`

## 💰 Состояние виртуального портфеля
| Показатель | Значение | Правило устава |
| :--- | :--- | :--- |
| **Стартовый капитал** | `$50.00 USDC` | Не добавлять деньги |
| **Текущий баланс (Equity)** | **`$29.85 USDC`** (`-20.15$` / `-40.30%`) | Cash + Mark-to-Market по CLOB Bid |
| **Свободный кэш / В сделках** | `$18.24` / `$11.61 USDC` | До 8 открытых позиций, макс 8% банка |
| **Цель окупаемости подписки** | `$-20.15 / $60.00` (`0.0%`) | Цель: +$60.00 в месяц |
| **Просадка от пика (Текущая / Макс)** | `0.25%` / `6.31%` (Пик: `$29.92`) | Стоп-кран при просадке 40% |
| **Закрытых сделок / Win Rate** | `45` / `42.2%` | Brier Score: `0.2574` |

## 📂 Открытые позиции (4 / 8)
| # | Рынок | Кат. | Исход | Вход (Ask VWAP) | Текущий Bid | Оценка бота | Размер ($) | Нереализ. PnL | Источник |
| :- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| #35 | Will Bitcoin dip to $80,000 in October? | Crypto | **YES** | `0.610` | `0.680` | `99.5%` | `$1.11` | `$+0.13` | Kraken BTCUSDT 1m/1h Spot Klin |
| #45 | US x Iran ceasefire continues through October 24? | Geopolitics | **YES** | `0.920` | `0.900` | `94.0%` | `$3.41` | `$-0.07` | Official NFL data feed |
| #47 | Israel x Iran ceasefire continues through October 24? | Geopolitics | **YES** | `0.950` | `0.940` | `98.0%` | `$3.57` | `$-0.04` | the totality of information av |
| #49 | Will Bitcoin dip to $80,000 on October 23? | Crypto | **NO** | `0.960` | `0.945` | `98.5%` | `$3.56` | `$-0.06` | https://www.binance.com/en/tra |

## 🔍 Последние проверенные кандидаты и фильтр стакана CLOB
| Рынок | Кат. | Сторона | Оценка бота | Цена Ask | Перекос (Edge) | Проскальзывание CLOB | Решение |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Hawks vs. Hornets | Sports | NO | `48.3%` | `44.0%` | `+4.3 п.п.` | `1.00%` | REJECTED: Win probability 48.3% < 92% minimum (no underdog lottery bets) |
| Spread: Celtics (-2.5) | Sports | YES | `57.5%` | `52.0%` | `+5.5 п.п.` | `1.00%` | REJECTED: Win probability 57.5% < 92% minimum (no underdog lottery bets) |
| Spread: Hawks (-2.5) | Sports | NO | `54.7%` | `50.0%` | `+4.7 п.п.` | `1.00%` | REJECTED: Win probability 54.7% < 92% minimum (no underdog lottery bets) |
| Will Harry Kane win the 2026 Ballon d'Or? | Other | YES | `81.8%` | `76.4%` | `+5.5 п.п.` | `0.10%` | REJECTED: Win probability 81.8% < 92% minimum (no underdog lottery bets) |
| Timberwolves vs. Magic | Sports | NO | `62.2%` | `52.0%` | `+10.2 п.п.` | `1.00%` | REJECTED: Win probability 62.2% < 92% minimum (no underdog lottery bets) |
| Knicks vs. Celtics | Sports | NO | `61.8%` | `57.0%` | `+4.8 п.п.` | `1.00%` | REJECTED: Win probability 61.8% < 92% minimum (no underdog lottery bets) |
| LoL: Bilibili Gaming vs Movistar KOI (BO1) - World | Sports | YES | `1.5%` | `100.0%` | `-98.5 п.п.` | `100.00%` | REJECTED: Edge -98.5 pp < 2 pp threshold (P_est=1.5% vs AskVWAP=100.0%) |
| Will the price of Bitcoin be between $78,000 and $ | Crypto | YES | `17.1%` | `2.4%` | `+14.7 п.п.` | `1.00%` | REJECTED: Win probability 17.1% < 92% minimum (no underdog lottery bets) |
| Will Iliana Iotova win the 2026 Bulgarian presiden | Geopolitics | YES | `22.3%` | `15.0%` | `+7.3 п.п.` | `3.00%` | REJECTED: Win probability 22.3% < 92% minimum (no underdog lottery bets) |
| Will Dejan Šoškić be the next Prime Minister of Se | Geopolitics | YES | `18.2%` | `13.2%` | `+5.0 п.п.` | `1.70%` | REJECTED: Win probability 18.2% < 92% minimum (no underdog lottery bets) |
| Will the price of Bitcoin be above $82,000 on Octo | Crypto | YES | `29.2%` | `14.0%` | `+15.2 п.п.` | `1.00%` | REJECTED: Win probability 29.2% < 92% minimum (no underdog lottery bets) |
| Will Ethereum dip to $2,300 October 19-25? | Crypto | YES | `35.1%` | `11.0%` | `+24.1 п.п.` | `1.00%` | REJECTED: Win probability 35.1% < 92% minimum (no underdog lottery bets) |
| Will FC Barcelona vs. Real Madrid CF end in a draw | Sports | NO | `95.8%` | `85.0%` | `+10.8 п.п.` | `1.00%` | REJECTED: Max open positions (4) reached |
| Will Аndrey Gyurov win the next Bulgarian presiden | Geopolitics | YES | `19.0%` | `15.0%` | `+4.0 п.п.` | `1.00%` | REJECTED: Win probability 19.0% < 92% minimum (no underdog lottery bets) |
| Will Ilija Srdanović be the next prime minister of | Geopolitics | YES | `21.6%` | `14.0%` | `+7.6 п.п.` | `2.00%` | REJECTED: Win probability 21.6% < 92% minimum (no underdog lottery bets) |
| Will Bitcoin dip to $78,000 October 19-25? | Crypto | YES | `26.1%` | `5.2%` | `+20.9 п.п.` | `0.29%` | REJECTED: Win probability 26.1% < 92% minimum (no underdog lottery bets) |
| Spread: Manchester City FC (-3.5) | Sports | NO | `97.5%` | `93.0%` | `+4.5 п.п.` | `1.00%` | REJECTED: Max open positions (4) reached |
| Counter-Strike: Brute vs BakS eSports (BO3) - CCT  | Sports | YES | `98.5%` | `90.4%` | `+8.1 п.п.` | `0.60%` | REJECTED: Max open positions (4) reached |
