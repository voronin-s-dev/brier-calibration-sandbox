# 📊 Отчёт симулятора Polymarket (Устав Grok Bot — Демо-счёт)
**Обновлено:** `2026-10-23 12:17:28 UTC`

## 💰 Состояние виртуального портфеля
| Показатель | Значение | Правило устава |
| :--- | :--- | :--- |
| **Стартовый капитал** | `$50.00 USDC` | Не добавлять деньги |
| **Текущий баланс (Equity)** | **`$29.70 USDC`** (`-20.30$` / `-40.61%`) | Cash + Mark-to-Market по CLOB Bid |
| **Свободный кэш / В сделках** | `$18.04` / `$11.66 USDC` | До 8 открытых позиций, макс 8% банка |
| **Цель окупаемости подписки** | `$-20.30 / $60.00` (`0.0%`) | Цель: +$60.00 в месяц |
| **Просадка от пика (Текущая / Макс)** | `0.37%` / `6.31%` (Пик: `$29.81`) | Стоп-кран при просадке 40% |
| **Закрытых сделок / Win Rate** | `44` / `40.9%` | Brier Score: `0.2860` |

## 📂 Открытые позиции (4 / 8)
| # | Рынок | Кат. | Исход | Вход (Ask VWAP) | Текущий Bid | Оценка бота | Размер ($) | Нереализ. PnL | Источник |
| :- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| #35 | Will Bitcoin dip to $80,000 in October? | Crypto | **YES** | `0.610` | `0.680` | `99.5%` | `$1.11` | `$+0.13` | Kraken BTCUSDT 1m/1h Spot Klin |
| #45 | US x Iran ceasefire continues through October 24? | Geopolitics | **YES** | `0.920` | `0.930` | `97.0%` | `$3.41` | `$+0.04` | Official NFL data feed |
| #47 | Israel x Iran ceasefire continues through October 24? | Geopolitics | **YES** | `0.950` | `0.930` | `97.0%` | `$3.57` | `$-0.08` | the totality of information av |
| #48 | Will the price of Bitcoin be above $80,000 on October 2 | Crypto | **YES** | `0.949` | `0.925` | `97.3%` | `$3.57` | `$-0.09` | https://www.binance.com/en/tra |

## 🔍 Последние проверенные кандидаты и фильтр стакана CLOB
| Рынок | Кат. | Сторона | Оценка бота | Цена Ask | Перекос (Edge) | Проскальзывание CLOB | Решение |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Dota 2: salamit vs Nemiga Gaming - Game 2 Winner | Sports | YES | `1.5%` | `100.0%` | `-98.5 п.п.` | `100.00%` | REJECTED: Edge -98.5 pp < 2 pp threshold (P_est=1.5% vs AskVWAP=100.0%) |
| Will Liverpool FC win on 2026-10-25? | Sports | YES | `51.0%` | `46.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Win probability 51.0% < 92% minimum (no underdog lottery bets) |
| Will Aleksandar Vučić – United Serbia win the most | Geopolitics | YES | `78.6%` | `70.0%` | `+8.6 п.п.` | `1.00%` | REJECTED: Win probability 78.6% < 92% minimum (no underdog lottery bets) |
| Will Harry Kane win the 2026 Ballon d'Or? | Other | YES | `82.0%` | `76.5%` | `+5.5 п.п.` | `0.10%` | REJECTED: Win probability 82.0% < 92% minimum (no underdog lottery bets) |
| Dota 2: Team Liquid vs GamerLegion - Game 1 Winner | Sports | YES | `1.5%` | `100.0%` | `-98.5 п.п.` | `100.00%` | REJECTED: Edge -98.5 pp < 2 pp threshold (P_est=1.5% vs AskVWAP=100.0%) |
| Will the price of Ethereum be above $2,300 on Octo | Crypto | NO | `10.0%` | `4.6%` | `+5.4 п.п.` | `0.70%` | REJECTED: Win probability 10.0% < 92% minimum (no underdog lottery bets) |
| Will Lorne Doerkson be the next Premier of British | Other | YES | `97.0%` | `92.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Max open positions (4) reached |
| Will Bitcoin reach $84,000 on October 23? | Crypto | YES | `15.8%` | `5.0%` | `+10.8 п.п.` | `1.00%` | REJECTED: Win probability 15.8% < 92% minimum (no underdog lottery bets) |
| Will the price of Ethereum be above $2,300 on Octo | Crypto | NO | `16.3%` | `7.0%` | `+9.3 п.п.` | `1.30%` | REJECTED: Win probability 16.3% < 92% minimum (no underdog lottery bets) |
| Israel x Iran ceasefire continues through October  | Geopolitics | NO | `21.2%` | `11.0%` | `+10.2 п.п.` | `2.00%` | REJECTED: Win probability 21.2% < 92% minimum (no underdog lottery bets) |
| Will Borussia Mönchengladbach win on 2026-10-23? | Sports | YES | `18.0%` | `13.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Win probability 18.0% < 92% minimum (no underdog lottery bets) |
| Will Russia target Kyiv on October 23, 2026? | Other | NO | `20.1%` | `15.4%` | `+4.7 п.п.` | `2.38%` | REJECTED: Win probability 20.1% < 92% minimum (no underdog lottery bets) |
| Will Ethereum dip to $2,300 October 19-25? | Crypto | YES | `36.0%` | `18.0%` | `+18.0 п.п.` | `2.00%` | REJECTED: Win probability 36.0% < 92% minimum (no underdog lottery bets) |
| Will Bitcoin reach $86,000 October 19-25? | Crypto | YES | `18.8%` | `3.1%` | `+15.7 п.п.` | `0.10%` | REJECTED: Win probability 18.8% < 92% minimum (no underdog lottery bets) |
| Spread: Manchester City FC (-3.5) | Sports | NO | `97.5%` | `93.0%` | `+4.5 п.п.` | `1.00%` | REJECTED: Max open positions (4) reached |
| Will Bitcoin dip to $78,000 October 19-25? | Crypto | YES | `24.9%` | `7.0%` | `+17.9 п.п.` | `0.20%` | REJECTED: Win probability 24.9% < 92% minimum (no underdog lottery bets) |
| Will the price of Bitcoin be above $80,000 on Octo | Crypto | NO | `21.9%` | `12.0%` | `+9.9 п.п.` | `1.10%` | REJECTED: Win probability 21.9% < 92% minimum (no underdog lottery bets) |
| Will Bitcoin dip to $76,000 October 19-25? | Crypto | YES | `8.9%` | `2.5%` | `+6.4 п.п.` | `0.30%` | REJECTED: Win probability 8.9% < 92% minimum (no underdog lottery bets) |
