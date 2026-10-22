# 📊 Отчёт симулятора Polymarket (Устав Grok Bot — Демо-счёт)
**Обновлено:** `2026-10-22 22:49:56 UTC`

## 💰 Состояние виртуального портфеля
| Показатель | Значение | Правило устава |
| :--- | :--- | :--- |
| **Стартовый капитал** | `$50.00 USDC` | Не добавлять деньги |
| **Текущий баланс (Equity)** | **`$28.71 USDC`** (`-21.29$` / `-42.58%`) | Cash + Mark-to-Market по CLOB Bid |
| **Свободный кэш / В сделках** | `$17.69` / `$11.02 USDC` | До 8 открытых позиций, макс 8% банка |
| **Цель окупаемости подписки** | `$-21.29 / $60.00` (`0.0%`) | Цель: +$60.00 в месяц |
| **Просадка от пика (Текущая / Макс)** | `0.22%` / `6.31%` (Пик: `$28.77`) | Стоп-кран при просадке 40% |
| **Закрытых сделок / Win Rate** | `41` / `36.6%` | Brier Score: `0.3214` |

## 📂 Открытые позиции (4 / 8)
| # | Рынок | Кат. | Исход | Вход (Ask VWAP) | Текущий Bid | Оценка бота | Размер ($) | Нереализ. PnL | Источник |
| :- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| #35 | Will Bitcoin dip to $80,000 in October? | Crypto | **YES** | `0.610` | `0.710` | `99.5%` | `$1.11` | `$+0.18` | Kraken BTCUSDT 1m/1h Spot Klin |
| #38 | Will the Bank of Russia decrease the key rate after the | Other | **NO** | `0.900` | `0.800` | `97.0%` | `$3.30` | `$-0.37` | https://www.cbr.ru/eng/dkp/cal |
| #44 | Will Bitcoin dip to $80,000 on October 22? | Crypto | **NO** | `0.917` | `0.922` | `96.0%` | `$3.40` | `$+0.02` | https://www.binance.com/en/tra |
| #45 | US x Iran ceasefire continues through October 24? | Geopolitics | **YES** | `0.920` | `0.910` | `95.0%` | `$3.41` | `$-0.04` | Official NFL data feed |

## 🔍 Последние проверенные кандидаты и фильтр стакана CLOB
| Рынок | Кат. | Сторона | Оценка бота | Цена Ask | Перекос (Edge) | Проскальзывание CLOB | Решение |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Spread: Thunder (-9.5) | Sports | YES | `49.9%` | `45.0%` | `+4.9 п.п.` | `1.00%` | REJECTED: Win probability 49.9% < 92% minimum (no underdog lottery bets) |
| Will Aleksandar Vučić be the next Prime Minister o | Geopolitics | YES | `83.7%` | `71.9%` | `+11.8 п.п.` | `1.80%` | REJECTED: Win probability 83.7% < 92% minimum (no underdog lottery bets) |
| Will Brighton & Hove Albion FC win on 2026-10-25? | Sports | YES | `36.0%` | `31.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Win probability 36.0% < 92% minimum (no underdog lottery bets) |
| Patriots vs. Bears | Sports | YES | `46.0%` | `41.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Win probability 46.0% < 92% minimum (no underdog lottery bets) |
| Will Harry Kane win the 2026 Ballon d'Or? | Other | YES | `81.5%` | `76.2%` | `+5.3 п.п.` | `0.40%` | REJECTED: Win probability 81.5% < 92% minimum (no underdog lottery bets) |
| Will Aleksandar Vučić – United Serbia win the most | Geopolitics | YES | `75.0%` | `70.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Win probability 75.0% < 92% minimum (no underdog lottery bets) |
| Will Lamine Yamal win the 2026 Ballon d'Or? | Other | YES | `21.8%` | `16.5%` | `+5.3 п.п.` | `0.40%` | REJECTED: Win probability 21.8% < 92% minimum (no underdog lottery bets) |
| Spread: Bears (-3.5) | Sports | NO | `97.5%` | `57.0%` | `+40.5 п.п.` | `1.00%` | REJECTED: Contract price $0.570 outside sweet spot [$0.84, $0.96] |
| Will the price of Ethereum be above $2,500 on Octo | Crypto | YES | `11.0%` | `6.7%` | `+4.3 п.п.` | `2.67%` | REJECTED: Win probability 11.0% < 92% minimum (no underdog lottery bets) |
| Will Estudiantes de La Plata win on 2026-10-22? | Sports | NO | `97.2%` | `89.0%` | `+8.2 п.п.` | `1.00%` | REJECTED: Max open positions (4) reached |
| Will Ethereum dip to $2,200 October 19-25? | Crypto | YES | `14.8%` | `7.2%` | `+7.6 п.п.` | `0.87%` | REJECTED: Win probability 14.8% < 92% minimum (no underdog lottery bets) |
| Will Bitcoin reach $86,000 October 19-25? | Crypto | YES | `20.1%` | `4.4%` | `+15.7 п.п.` | `0.70%` | REJECTED: Win probability 20.1% < 92% minimum (no underdog lottery bets) |
| Will Bitcoin dip to $78,000 October 19-25? | Crypto | YES | `33.3%` | `13.7%` | `+19.6 п.п.` | `0.39%` | REJECTED: Win probability 33.3% < 92% minimum (no underdog lottery bets) |
| Will Bitcoin dip to $76,000 October 19-25? | Crypto | YES | `13.7%` | `4.0%` | `+9.7 п.п.` | `0.40%` | REJECTED: Win probability 13.7% < 92% minimum (no underdog lottery bets) |
| Will the price of Bitcoin be above $80,000 on Octo | Crypto | NO | `22.1%` | `15.9%` | `+6.2 п.п.` | `1.20%` | REJECTED: Win probability 22.1% < 92% minimum (no underdog lottery bets) |
| Will Ilija Srdanović be the next prime minister of | Geopolitics | YES | `18.0%` | `13.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Win probability 18.0% < 92% minimum (no underdog lottery bets) |
| Will Kylian Mbappé win the 2026 Ballon d'Or? | Other | YES | `15.9%` | `6.4%` | `+9.5 п.п.` | `1.03%` | REJECTED: Win probability 15.9% < 92% minimum (no underdog lottery bets) |
| Spread: Thunder (-9.5) | Sports | YES | `49.9%` | `45.0%` | `+4.9 п.п.` | `1.00%` | REJECTED: Win probability 49.9% < 92% minimum (no underdog lottery bets) |
