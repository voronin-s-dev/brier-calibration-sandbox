# 📊 Отчёт симулятора Polymarket (Устав Grok Bot — Демо-счёт)
**Обновлено:** `2026-10-21 07:36:23 UTC`

## 💰 Состояние виртуального портфеля
| Показатель | Значение | Правило устава |
| :--- | :--- | :--- |
| **Стартовый капитал** | `$50.00 USDC` | Не добавлять деньги |
| **Текущий баланс (Equity)** | **`$27.49 USDC`** (`-22.51$` / `-45.01%`) | Cash + Mark-to-Market по CLOB Bid |
| **Свободный кэш / В сделках** | `$16.80` / `$10.69 USDC` | До 8 открытых позиций, макс 8% банка |
| **Цель окупаемости подписки** | `$-22.51 / $60.00` (`0.0%`) | Цель: +$60.00 в месяц |
| **Просадка от пика (Текущая / Макс)** | `1.98%` / `2.16%` (Пик: `$28.05`) | Стоп-кран при просадке 40% |
| **Закрытых сделок / Win Rate** | `35` / `25.7%` | Brier Score: `0.4280` |

## 📂 Открытые позиции (4 / 8)
| # | Рынок | Кат. | Исход | Вход (Ask VWAP) | Текущий Bid | Оценка бота | Размер ($) | Нереализ. PnL | Источник |
| :- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| #35 | Will Bitcoin dip to $80,000 in October? | Crypto | **YES** | `0.610` | `0.480` | `99.5%` | `$1.11` | `$-0.24` | Kraken BTCUSDT 1m/1h Spot Klin |
| #36 | US x Iran ceasefire continues through October 22? | Geopolitics | **YES** | `0.953` | `0.960` | `98.0%` | `$3.30` | `$+0.02` | Official NFL data feed |
| #38 | Will the Bank of Russia decrease the key rate after the | Other | **NO** | `0.900` | `0.880` | `97.0%` | `$3.30` | `$-0.07` | https://www.cbr.ru/eng/dkp/cal |
| #39 | Spread: Arsenal FC (-2.5) | Sports | **NO** | `0.964` | `0.955` | `98.5%` | `$3.30` | `$-0.03` | https://www.uefa.com/ |

## 🔍 Последние проверенные кандидаты и фильтр стакана CLOB
| Рынок | Кат. | Сторона | Оценка бота | Цена Ask | Перекос (Edge) | Проскальзывание CLOB | Решение |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Will FC Bayern München win on 2026-10-21? | Sports | YES | `51.0%` | `46.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Win probability 51.0% < 92% minimum (no underdog lottery bets) |
| Will the price of Bitcoin be above $80,000 on Octo | Crypto | NO | `17.8%` | `7.0%` | `+10.8 п.п.` | `1.00%` | REJECTED: Win probability 17.8% < 92% minimum (no underdog lottery bets) |
| Will LASK Linz win on 2026-10-21? | Sports | YES | `13.0%` | `8.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Win probability 13.0% < 92% minimum (no underdog lottery bets) |
| Will Bitcoin dip to $78,000 October 19-25? | Crypto | YES | `26.8%` | `9.0%` | `+17.8 п.п.` | `1.00%` | REJECTED: Win probability 26.8% < 92% minimum (no underdog lottery bets) |
| Will Bitcoin reach $88,000 October 19-25? | Crypto | YES | `26.1%` | `11.0%` | `+15.1 п.п.` | `1.00%` | REJECTED: Win probability 26.1% < 92% minimum (no underdog lottery bets) |
| Will Bitcoin dip to $80,000 on October 21? | Crypto | YES | `13.7%` | `2.9%` | `+10.8 п.п.` | `0.24%` | REJECTED: Win probability 13.7% < 92% minimum (no underdog lottery bets) |
| FC Bayern München vs. Arsenal FC: O/U 0.5 | Sports | NO | `10.1%` | `4.3%` | `+5.8 п.п.` | `0.51%` | REJECTED: Win probability 10.1% < 92% minimum (no underdog lottery bets) |
| Will the price of Bitcoin be above $86,000 on Octo | Crypto | YES | `9.6%` | `4.4%` | `+5.1 п.п.` | `0.40%` | REJECTED: Win probability 9.6% < 92% minimum (no underdog lottery bets) |
| Will NDP win the most seats in the 2026 British Co | Geopolitics | YES | `16.0%` | `11.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Win probability 16.0% < 92% minimum (no underdog lottery bets) |
| Will Bitcoin reach $90,000 October 19-25? | Crypto | YES | `13.7%` | `5.0%` | `+8.7 п.п.` | `0.60%` | REJECTED: Win probability 13.7% < 92% minimum (no underdog lottery bets) |
| Will Elon Musk post 280-299 tweets from October 16 | Geopolitics | YES | `13.0%` | `8.0%` | `+5.0 п.п.` | `2.00%` | REJECTED: Win probability 13.0% < 92% minimum (no underdog lottery bets) |
| Will Bitcoin dip to $76,000 October 19-25? | Crypto | YES | `12.6%` | `3.3%` | `+9.3 п.п.` | `0.10%` | REJECTED: Win probability 12.6% < 92% minimum (no underdog lottery bets) |
| Will Iliana Iotova win the next Bulgarian presiden | Geopolitics | NO | `16.0%` | `12.0%` | `+4.0 п.п.` | `1.00%` | REJECTED: Win probability 16.0% < 92% minimum (no underdog lottery bets) |
| US x Iran ceasefire continues through October 24? | Geopolitics | YES | `96.0%` | `91.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Duplicate underlying event (geopolitics:us x iran ceasefire continues through oc) |
| Will FC Bayern München win on 2026-10-21? | Sports | YES | `51.0%` | `46.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Win probability 51.0% < 92% minimum (no underdog lottery bets) |
| Will the price of Bitcoin be above $80,000 on Octo | Crypto | NO | `18.4%` | `10.0%` | `+8.3 п.п.` | `1.00%` | REJECTED: Win probability 18.4% < 92% minimum (no underdog lottery bets) |
| Will LASK Linz win on 2026-10-21? | Sports | YES | `13.0%` | `8.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Win probability 13.0% < 92% minimum (no underdog lottery bets) |
| Will Bitcoin dip to $78,000 October 19-25? | Crypto | YES | `27.1%` | `12.0%` | `+15.1 п.п.` | `1.00%` | REJECTED: Win probability 27.1% < 92% minimum (no underdog lottery bets) |
