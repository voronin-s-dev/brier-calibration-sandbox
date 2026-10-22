# 📊 Отчёт симулятора Polymarket (Устав Grok Bot — Демо-счёт)
**Обновлено:** `2026-10-22 00:44:42 UTC`

## 💰 Состояние виртуального портфеля
| Показатель | Значение | Правило устава |
| :--- | :--- | :--- |
| **Стартовый капитал** | `$50.00 USDC` | Не добавлять деньги |
| **Текущий баланс (Equity)** | **`$26.93 USDC`** (`-23.07$` / `-46.14%`) | Cash + Mark-to-Market по CLOB Bid |
| **Свободный кэш / В сделках** | `$17.14` / `$9.79 USDC` | До 8 открытых позиций, макс 8% банка |
| **Цель окупаемости подписки** | `$-23.07 / $60.00` (`0.0%`) | Цель: +$60.00 в месяц |
| **Просадка от пика (Текущая / Макс)** | `3.98%` / `6.31%` (Пик: `$28.05`) | Стоп-кран при просадке 40% |
| **Закрытых сделок / Win Rate** | `37` / `29.7%` | Brier Score: `0.3669` |

## 📂 Открытые позиции (4 / 8)
| # | Рынок | Кат. | Исход | Вход (Ask VWAP) | Текущий Bid | Оценка бота | Размер ($) | Нереализ. PnL | Источник |
| :- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| #35 | Will Bitcoin dip to $80,000 in October? | Crypto | **YES** | `0.610` | `0.320` | `99.5%` | `$1.11` | `$-0.53` | Kraken BTCUSDT 1m/1h Spot Klin |
| #36 | US x Iran ceasefire continues through October 22? | Geopolitics | **YES** | `0.953` | `0.908` | `94.6%` | `$3.30` | `$-0.16` | Official NFL data feed |
| #38 | Will the Bank of Russia decrease the key rate after the | Other | **NO** | `0.900` | `0.800` | `97.0%` | `$3.30` | `$-0.37` | https://www.cbr.ru/eng/dkp/cal |
| #41 | Will Bitcoin reach $85,000 on October 21? | Crypto | **NO** | `0.910` | `0.880` | `70.9%` | `$3.24` | `$-0.11` | https://www.binance.com/en/tra |

## 🔍 Последние проверенные кандидаты и фильтр стакана CLOB
| Рынок | Кат. | Сторона | Оценка бота | Цена Ask | Перекос (Edge) | Проскальзывание CLOB | Решение |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Will Luiz Inácio Lula da Silva win the second roun | Geopolitics | YES | `28.2%` | `18.0%` | `+10.2 п.п.` | `1.00%` | REJECTED: Win probability 28.2% < 92% minimum (no underdog lottery bets) |
| Will Aleksandar Vučić be the next Prime Minister o | Geopolitics | YES | `69.8%` | `65.1%` | `+4.8 п.п.` | `1.50%` | REJECTED: Win probability 69.8% < 92% minimum (no underdog lottery bets) |
| Suns vs. Trail Blazers | Sports | NO | `62.4%` | `58.0%` | `+4.4 п.п.` | `1.00%` | REJECTED: Win probability 62.4% < 92% minimum (no underdog lottery bets) |
| Warriors vs. Lakers | Sports | NO | `73.0%` | `68.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Win probability 73.0% < 92% minimum (no underdog lottery bets) |
| Will Flávio Bolsonaro win the second round of the  | Geopolitics | YES | `37.0%` | `32.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Win probability 37.0% < 92% minimum (no underdog lottery bets) |
| Will Aleksandar Vučić – United Serbia win the most | Geopolitics | YES | `73.0%` | `68.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Win probability 73.0% < 92% minimum (no underdog lottery bets) |
| Spread: Clippers (-5.5) | Sports | NO | `56.1%` | `52.0%` | `+4.1 п.п.` | `1.00%` | REJECTED: Win probability 56.1% < 92% minimum (no underdog lottery bets) |
| Spread: Clippers (-4.5) | Sports | NO | `97.5%` | `48.0%` | `+49.5 п.п.` | `1.00%` | REJECTED: Contract price $0.480 outside sweet spot [$0.84, $0.96] |
| Exact Score: Celtic FC 2 - 2 RC Celta de Vigo? | Sports | NO | `98.5%` | `94.0%` | `+4.5 п.п.` | `1.88%` | REJECTED: Max open positions (4) reached |
| Will Bitcoin dip to $78,000 October 19-25? | Crypto | YES | `13.7%` | `3.8%` | `+9.9 п.п.` | `0.60%` | REJECTED: Win probability 13.7% < 92% minimum (no underdog lottery bets) |
| Will NDP win the most seats in the 2026 British Co | Geopolitics | YES | `16.0%` | `11.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Win probability 16.0% < 92% minimum (no underdog lottery bets) |
| Will the price of Bitcoin be above $82,000 on Octo | Crypto | NO | `20.1%` | `11.0%` | `+9.1 п.п.` | `2.00%` | REJECTED: Win probability 20.1% < 92% minimum (no underdog lottery bets) |
| Will Conservative win the most seats in the 2026 B | Geopolitics | NO | `17.3%` | `11.0%` | `+6.3 п.п.` | `1.00%` | REJECTED: Win probability 17.3% < 92% minimum (no underdog lottery bets) |
| Will Bitcoin dip to $80,000 October 19-25? | Crypto | YES | `29.6%` | `11.0%` | `+18.6 п.п.` | `1.00%` | REJECTED: Win probability 29.6% < 92% minimum (no underdog lottery bets) |
| Will Bitcoin reach $90,000 October 19-25? | Crypto | YES | `18.6%` | `4.8%` | `+13.8 п.п.` | `0.10%` | REJECTED: Win probability 18.6% < 92% minimum (no underdog lottery bets) |
| Will Bitcoin reach $88,000 October 19-25? | Crypto | YES | `35.5%` | `15.0%` | `+20.5 п.п.` | `1.00%` | REJECTED: Win probability 35.5% < 92% minimum (no underdog lottery bets) |
| US x Iran ceasefire continues through October 24? | Geopolitics | NO | `23.5%` | `15.0%` | `+8.5 п.п.` | `1.00%` | REJECTED: Win probability 23.5% < 92% minimum (no underdog lottery bets) |
| Suns vs. Trail Blazers | Sports | NO | `62.4%` | `58.0%` | `+4.4 п.п.` | `1.00%` | REJECTED: Win probability 62.4% < 92% minimum (no underdog lottery bets) |
