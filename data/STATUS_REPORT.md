# 📊 Отчёт симулятора Polymarket (Устав Grok Bot — Демо-счёт)
**Обновлено:** `2026-10-23 11:58:45 UTC`

## 💰 Состояние виртуального портфеля
| Показатель | Значение | Правило устава |
| :--- | :--- | :--- |
| **Стартовый капитал** | `$50.00 USDC` | Не добавлять деньги |
| **Текущий баланс (Equity)** | **`$29.71 USDC`** (`-20.29$` / `-40.59%`) | Cash + Mark-to-Market по CLOB Bid |
| **Свободный кэш / В сделках** | `$18.05` / `$11.65 USDC` | До 8 открытых позиций, макс 8% банка |
| **Цель окупаемости подписки** | `$-20.29 / $60.00` (`0.0%`) | Цель: +$60.00 в месяц |
| **Просадка от пика (Текущая / Макс)** | `0.13%` / `6.31%` (Пик: `$29.74`) | Стоп-кран при просадке 40% |
| **Закрытых сделок / Win Rate** | `43` / `39.5%` | Brier Score: `0.2860` |

## 📂 Открытые позиции (4 / 8)
| # | Рынок | Кат. | Исход | Вход (Ask VWAP) | Текущий Bid | Оценка бота | Размер ($) | Нереализ. PnL | Источник |
| :- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| #35 | Will Bitcoin dip to $80,000 in October? | Crypto | **YES** | `0.610` | `0.650` | `99.5%` | `$1.11` | `$+0.07` | Kraken BTCUSDT 1m/1h Spot Klin |
| #45 | US x Iran ceasefire continues through October 24? | Geopolitics | **YES** | `0.920` | `0.930` | `97.0%` | `$3.41` | `$+0.04` | Official NFL data feed |
| #46 | Will the price of Bitcoin be above $84,000 on October 2 | Crypto | **NO** | `0.959` | `0.973` | `98.5%` | `$3.44` | `$+0.05` | https://www.binance.com/en/tra |
| #47 | Israel x Iran ceasefire continues through October 24? | Geopolitics | **YES** | `0.950` | `0.940` | `98.0%` | `$3.57` | `$-0.04` | the totality of information av |

## 🔍 Последние проверенные кандидаты и фильтр стакана CLOB
| Рынок | Кат. | Сторона | Оценка бота | Цена Ask | Перекос (Edge) | Проскальзывание CLOB | Решение |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Dota 2: salamit vs Nemiga Gaming - Game 2 Winner | Sports | YES | `1.5%` | `100.0%` | `-98.5 п.п.` | `100.00%` | REJECTED: Edge -98.5 pp < 2 pp threshold (P_est=1.5% vs AskVWAP=100.0%) |
| Will Liverpool FC win on 2026-10-25? | Sports | YES | `51.0%` | `46.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Win probability 51.0% < 92% minimum (no underdog lottery bets) |
| Will Aleksandar Vučić – United Serbia win the most | Geopolitics | YES | `78.8%` | `70.0%` | `+8.8 п.п.` | `1.00%` | REJECTED: Win probability 78.8% < 92% minimum (no underdog lottery bets) |
| Will Harry Kane win the 2026 Ballon d'Or? | Other | YES | `88.3%` | `76.5%` | `+11.8 п.п.` | `0.10%` | REJECTED: Win probability 88.3% < 92% minimum (no underdog lottery bets) |
| Will the price of Ethereum be above $2,300 on Octo | Crypto | NO | `9.9%` | `3.8%` | `+6.2 п.п.` | `0.45%` | REJECTED: Win probability 9.9% < 92% minimum (no underdog lottery bets) |
| Will Lorne Doerkson be the next Premier of British | Other | YES | `97.0%` | `92.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Max open positions (4) reached |
| Will Bitcoin reach $84,000 on October 23? | Crypto | YES | `16.4%` | `7.0%` | `+9.4 п.п.` | `1.00%` | REJECTED: Win probability 16.4% < 92% minimum (no underdog lottery bets) |
| Will Naftali Bennett be the next Prime Minister of | Geopolitics | YES | `20.0%` | `16.0%` | `+4.0 п.п.` | `1.00%` | REJECTED: Win probability 20.0% < 92% minimum (no underdog lottery bets) |
| Will the price of Ethereum be above $2,300 on Octo | Crypto | NO | `16.1%` | `5.8%` | `+10.3 п.п.` | `1.30%` | REJECTED: Win probability 16.1% < 92% minimum (no underdog lottery bets) |
| Israel x Iran ceasefire continues through October  | Geopolitics | NO | `21.3%` | `11.0%` | `+10.3 п.п.` | `2.00%` | REJECTED: Win probability 21.3% < 92% minimum (no underdog lottery bets) |
| Will Russia target Kyiv on October 23, 2026? | Other | NO | `20.0%` | `15.4%` | `+4.6 п.п.` | `2.38%` | REJECTED: Win probability 20.0% < 92% minimum (no underdog lottery bets) |
| Will Ethereum dip to $2,300 October 19-25? | Crypto | YES | `35.5%` | `14.0%` | `+21.6 п.п.` | `2.00%` | REJECTED: Win probability 35.5% < 92% minimum (no underdog lottery bets) |
| Will Bitcoin reach $86,000 October 19-25? | Crypto | YES | `18.9%` | `3.2%` | `+15.8 п.п.` | `0.30%` | REJECTED: Win probability 18.9% < 92% minimum (no underdog lottery bets) |
| Spread: Manchester City FC (-3.5) | Sports | NO | `97.5%` | `93.0%` | `+4.5 п.п.` | `1.00%` | REJECTED: Max open positions (4) reached |
| Will Bitcoin dip to $78,000 October 19-25? | Crypto | YES | `25.0%` | `6.1%` | `+18.9 п.п.` | `0.10%` | REJECTED: Win probability 25.0% < 92% minimum (no underdog lottery bets) |
| Will Ethereum reach $2,600 October 19-25? | Crypto | YES | `11.1%` | `3.4%` | `+7.7 п.п.` | `1.71%` | REJECTED: Win probability 11.1% < 92% minimum (no underdog lottery bets) |
| Will Bitcoin dip to $76,000 October 19-25? | Crypto | YES | `8.9%` | `2.1%` | `+6.8 п.п.` | `0.30%` | REJECTED: Win probability 8.9% < 92% minimum (no underdog lottery bets) |
| Israel x Iran ceasefire continues through October  | Geopolitics | YES | `98.0%` | `95.0%` | `+3.0 п.п.` | `1.00%` | EXECUTED BUY #47 ($3.57 @ 0.9500) |
