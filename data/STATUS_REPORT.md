# 📊 Отчёт симулятора Polymarket (Устав Grok Bot — Демо-счёт)
**Обновлено:** `2026-10-22 19:24:33 UTC`

## 💰 Состояние виртуального портфеля
| Показатель | Значение | Правило устава |
| :--- | :--- | :--- |
| **Стартовый капитал** | `$50.00 USDC` | Не добавлять деньги |
| **Текущий баланс (Equity)** | **`$28.44 USDC`** (`-21.56$` / `-43.11%`) | Cash + Mark-to-Market по CLOB Bid |
| **Свободный кэш / В сделках** | `$17.69` / `$10.76 USDC` | До 8 открытых позиций, макс 8% банка |
| **Цель окупаемости подписки** | `$-21.56 / $60.00` (`0.0%`) | Цель: +$60.00 в месяц |
| **Просадка от пика (Текущая / Макс)** | `0.08%` / `6.31%` (Пик: `$28.47`) | Стоп-кран при просадке 40% |
| **Закрытых сделок / Win Rate** | `40` / `35.0%` | Brier Score: `0.3214` |

## 📂 Открытые позиции (4 / 8)
| # | Рынок | Кат. | Исход | Вход (Ask VWAP) | Текущий Bid | Оценка бота | Размер ($) | Нереализ. PnL | Источник |
| :- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| #35 | Will Bitcoin dip to $80,000 in October? | Crypto | **YES** | `0.610` | `0.710` | `99.5%` | `$1.11` | `$+0.18` | Kraken BTCUSDT 1m/1h Spot Klin |
| #36 | US x Iran ceasefire continues through October 22? | Geopolitics | **YES** | `0.953` | `0.975` | `98.0%` | `$3.30` | `$+0.08` | Official NFL data feed |
| #38 | Will the Bank of Russia decrease the key rate after the | Other | **NO** | `0.900` | `0.740` | `97.0%` | `$3.30` | `$-0.59` | https://www.cbr.ru/eng/dkp/cal |
| #44 | Will Bitcoin dip to $80,000 on October 22? | Crypto | **NO** | `0.917` | `0.911` | `94.6%` | `$3.40` | `$-0.02` | https://www.binance.com/en/tra |

## 🔍 Последние проверенные кандидаты и фильтр стакана CLOB
| Рынок | Кат. | Сторона | Оценка бота | Цена Ask | Перекос (Edge) | Проскальзывание CLOB | Решение |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Will Brighton & Hove Albion FC win on 2026-10-25? | Sports | YES | `36.0%` | `31.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Win probability 36.0% < 92% minimum (no underdog lottery bets) |
| Will Aleksandar Vučić – United Serbia win the most | Geopolitics | YES | `76.0%` | `71.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Win probability 76.0% < 92% minimum (no underdog lottery bets) |
| Spread: 76ers (-3.5) | Sports | NO | `97.5%` | `54.0%` | `+43.5 п.п.` | `1.00%` | REJECTED: Contract price $0.540 outside sweet spot [$0.84, $0.96] |
| Will Harry Kane win the 2026 Ballon d'Or? | Other | YES | `87.5%` | `76.2%` | `+11.3 п.п.` | `0.10%` | REJECTED: Win probability 87.5% < 92% minimum (no underdog lottery bets) |
| Will Lamine Yamal win the 2026 Ballon d'Or? | Other | YES | `26.8%` | `17.6%` | `+9.2 п.п.` | `0.90%` | REJECTED: Win probability 26.8% < 92% minimum (no underdog lottery bets) |
| Spread: Bears (-3.5) | Sports | NO | `97.5%` | `57.0%` | `+40.5 п.п.` | `1.00%` | REJECTED: Contract price $0.570 outside sweet spot [$0.84, $0.96] |
| Will Estudiantes de La Plata win on 2026-10-22? | Sports | NO | `98.0%` | `93.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Max open positions (4) reached |
| Will the price of Ethereum be above $2,500 on Octo | Crypto | YES | `12.2%` | `6.2%` | `+5.9 п.п.` | `2.14%` | REJECTED: Win probability 12.2% < 92% minimum (no underdog lottery bets) |
| Will Ethereum dip to $2,200 October 19-25? | Crypto | YES | `15.1%` | `7.9%` | `+7.2 п.п.` | `1.69%` | REJECTED: Win probability 15.1% < 92% minimum (no underdog lottery bets) |
| Will Bitcoin reach $86,000 October 19-25? | Crypto | YES | `21.2%` | `6.0%` | `+15.2 п.п.` | `1.20%` | REJECTED: Win probability 21.2% < 92% minimum (no underdog lottery bets) |
| Will Bitcoin dip to $78,000 October 19-25? | Crypto | YES | `34.0%` | `14.4%` | `+19.6 п.п.` | `0.98%` | REJECTED: Win probability 34.0% < 92% minimum (no underdog lottery bets) |
| Will Аndrey Gyurov win the next Bulgarian presiden | Geopolitics | NO | `94.6%` | `88.0%` | `+6.6 п.п.` | `1.00%` | REJECTED: Max open positions (4) reached |
| Will Bitcoin dip to $76,000 October 19-25? | Crypto | YES | `14.5%` | `5.2%` | `+9.3 п.п.` | `1.09%` | REJECTED: Win probability 14.5% < 92% minimum (no underdog lottery bets) |
| Will Bitcoin dip to $80,000 on October 22? | Crypto | NO | `94.6%` | `91.8%` | `+2.8 п.п.` | `0.70%` | EXECUTED BUY #44 ($3.40 @ 0.9170) |
| Will the price of Bitcoin be above $80,000 on Octo | Crypto | NO | `23.4%` | `15.0%` | `+8.4 п.п.` | `0.87%` | REJECTED: Win probability 23.4% < 92% minimum (no underdog lottery bets) |
| Counter-Strike: BC.Game Esports vs FaZe - Map 2 Wi | Sports | NO | `1.5%` | `100.0%` | `-98.5 п.п.` | `100.00%` | REJECTED: Edge -98.5 pp < 2 pp threshold (P_est=1.5% vs AskVWAP=100.0%) |
| Will Liverpool FC win on 2026-10-25? | Sports | YES | `51.0%` | `46.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Win probability 51.0% < 92% minimum (no underdog lottery bets) |
| Will Lamine Yamal win the 2026 Ballon d'Or? | Other | YES | `28.7%` | `16.6%` | `+12.2 п.п.` | `0.10%` | REJECTED: Win probability 28.7% < 92% minimum (no underdog lottery bets) |
