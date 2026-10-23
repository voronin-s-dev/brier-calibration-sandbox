# 📊 Отчёт симулятора Polymarket (Устав Grok Bot — Демо-счёт)
**Обновлено:** `2026-10-23 01:23:47 UTC`

## 💰 Состояние виртуального портфеля
| Показатель | Значение | Правило устава |
| :--- | :--- | :--- |
| **Стартовый капитал** | `$50.00 USDC` | Не добавлять деньги |
| **Текущий баланс (Equity)** | **`$28.82 USDC`** (`-21.18$` / `-42.35%`) | Cash + Mark-to-Market по CLOB Bid |
| **Свободный кэш / В сделках** | `$17.69` / `$11.13 USDC` | До 8 открытых позиций, макс 8% банка |
| **Цель окупаемости подписки** | `$-21.18 / $60.00` (`0.0%`) | Цель: +$60.00 в месяц |
| **Просадка от пика (Текущая / Макс)** | `0.00%` / `6.31%` (Пик: `$28.82`) | Стоп-кран при просадке 40% |
| **Закрытых сделок / Win Rate** | `41` / `36.6%` | Brier Score: `0.3214` |

## 📂 Открытые позиции (4 / 8)
| # | Рынок | Кат. | Исход | Вход (Ask VWAP) | Текущий Bid | Оценка бота | Размер ($) | Нереализ. PnL | Источник |
| :- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| #35 | Will Bitcoin dip to $80,000 in October? | Crypto | **YES** | `0.610` | `0.700` | `99.5%` | `$1.11` | `$+0.16` | Kraken BTCUSDT 1m/1h Spot Klin |
| #38 | Will the Bank of Russia decrease the key rate after the | Other | **NO** | `0.900` | `0.810` | `97.0%` | `$3.30` | `$-0.33` | https://www.cbr.ru/eng/dkp/cal |
| #44 | Will Bitcoin dip to $80,000 on October 22? | Crypto | **NO** | `0.917` | `0.948` | `98.2%` | `$3.40` | `$+0.11` | https://www.binance.com/en/tra |
| #45 | US x Iran ceasefire continues through October 24? | Geopolitics | **YES** | `0.920` | `0.910` | `95.0%` | `$3.41` | `$-0.04` | Official NFL data feed |

## 🔍 Последние проверенные кандидаты и фильтр стакана CLOB
| Рынок | Кат. | Сторона | Оценка бота | Цена Ask | Перекос (Edge) | Проскальзывание CLOB | Решение |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Will Aleksandar Vučić be the next Prime Minister o | Geopolitics | YES | `75.8%` | `70.6%` | `+5.2 п.п.` | `0.49%` | REJECTED: Win probability 75.8% < 92% minimum (no underdog lottery bets) |
| Will Brighton & Hove Albion FC win on 2026-10-25? | Sports | YES | `36.0%` | `31.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Win probability 36.0% < 92% minimum (no underdog lottery bets) |
| Will Aleksandar Vučić – United Serbia win the most | Geopolitics | YES | `74.0%` | `69.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Win probability 74.0% < 92% minimum (no underdog lottery bets) |
| Will Harry Kane win the 2026 Ballon d'Or? | Other | YES | `86.3%` | `75.0%` | `+11.3 п.п.` | `0.10%` | REJECTED: Win probability 86.3% < 92% minimum (no underdog lottery bets) |
| Will the price of Bitcoin be above $76,000 on Octo | Crypto | NO | `10.6%` | `4.8%` | `+5.9 п.п.` | `2.28%` | REJECTED: Win probability 10.6% < 92% minimum (no underdog lottery bets) |
| Will the price of Ethereum be above $2,300 on Octo | Crypto | NO | `16.8%` | `10.6%` | `+6.2 п.п.` | `2.50%` | REJECTED: Win probability 16.8% < 92% minimum (no underdog lottery bets) |
| Will Ethereum reach $2,600 October 19-25? | Crypto | YES | `11.6%` | `4.1%` | `+7.5 п.п.` | `0.70%` | REJECTED: Win probability 11.6% < 92% minimum (no underdog lottery bets) |
| Will the price of Ethereum be above $2,500 on Octo | Crypto | YES | `10.9%` | `4.3%` | `+6.6 п.п.` | `0.70%` | REJECTED: Win probability 10.9% < 92% minimum (no underdog lottery bets) |
| Will Ethereum dip to $2,200 October 19-25? | Crypto | YES | `13.4%` | `6.3%` | `+7.1 п.п.` | `1.09%` | REJECTED: Win probability 13.4% < 92% minimum (no underdog lottery bets) |
| Will Bitcoin dip to $78,000 October 19-25? | Crypto | YES | `32.0%` | `12.4%` | `+19.6 п.п.` | `0.40%` | REJECTED: Win probability 32.0% < 92% minimum (no underdog lottery bets) |
| Will Bitcoin reach $86,000 October 19-25? | Crypto | YES | `19.8%` | `4.4%` | `+15.4 п.п.` | `0.50%` | REJECTED: Win probability 19.8% < 92% minimum (no underdog lottery bets) |
| Will Bitcoin dip to $76,000 October 19-25? | Crypto | YES | `12.9%` | `3.9%` | `+9.0 п.п.` | `0.30%` | REJECTED: Win probability 12.9% < 92% minimum (no underdog lottery bets) |
| Will the price of Bitcoin be above $80,000 on Octo | Crypto | NO | `19.7%` | `11.7%` | `+8.0 п.п.` | `1.10%` | REJECTED: Win probability 19.7% < 92% minimum (no underdog lottery bets) |
| Will Aleksandar Vučić be the next Prime Minister o | Geopolitics | YES | `76.5%` | `71.9%` | `+4.7 п.п.` | `1.70%` | REJECTED: Win probability 76.5% < 92% minimum (no underdog lottery bets) |
| Will Brighton & Hove Albion FC win on 2026-10-25? | Sports | YES | `36.0%` | `31.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Win probability 36.0% < 92% minimum (no underdog lottery bets) |
| Patriots vs. Bears | Sports | YES | `46.0%` | `41.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Win probability 46.0% < 92% minimum (no underdog lottery bets) |
| Will Harry Kane win the 2026 Ballon d'Or? | Other | YES | `82.3%` | `76.9%` | `+5.5 п.п.` | `0.10%` | REJECTED: Win probability 82.3% < 92% minimum (no underdog lottery bets) |
| Will Aleksandar Vučić – United Serbia win the most | Geopolitics | YES | `75.0%` | `70.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Win probability 75.0% < 92% minimum (no underdog lottery bets) |
