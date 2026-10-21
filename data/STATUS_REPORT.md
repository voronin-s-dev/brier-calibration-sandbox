# 📊 Отчёт симулятора Polymarket (Устав Grok Bot — Демо-счёт)
**Обновлено:** `2026-10-21 18:13:26 UTC`

## 💰 Состояние виртуального портфеля
| Показатель | Значение | Правило устава |
| :--- | :--- | :--- |
| **Стартовый капитал** | `$50.00 USDC` | Не добавлять деньги |
| **Текущий баланс (Equity)** | **`$26.89 USDC`** (`-23.11$` / `-46.21%`) | Cash + Mark-to-Market по CLOB Bid |
| **Свободный кэш / В сделках** | `$16.80` / `$10.09 USDC` | До 8 открытых позиций, макс 8% банка |
| **Цель окупаемости подписки** | `$-23.11 / $60.00` (`0.0%`) | Цель: +$60.00 в месяц |
| **Просадка от пика (Текущая / Макс)** | `4.12%` / `4.12%` (Пик: `$28.05`) | Стоп-кран при просадке 40% |
| **Закрытых сделок / Win Rate** | `35` / `25.7%` | Brier Score: `0.4280` |

## 📂 Открытые позиции (4 / 8)
| # | Рынок | Кат. | Исход | Вход (Ask VWAP) | Текущий Bid | Оценка бота | Размер ($) | Нереализ. PnL | Источник |
| :- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| #35 | Will Bitcoin dip to $80,000 in October? | Crypto | **YES** | `0.610` | `0.280` | `99.5%` | `$1.11` | `$-0.60` | Kraken BTCUSDT 1m/1h Spot Klin |
| #36 | US x Iran ceasefire continues through October 22? | Geopolitics | **YES** | `0.953` | `0.979` | `98.0%` | `$3.30` | `$+0.09` | Official NFL data feed |
| #38 | Will the Bank of Russia decrease the key rate after the | Other | **NO** | `0.900` | `0.810` | `97.0%` | `$3.30` | `$-0.33` | https://www.cbr.ru/eng/dkp/cal |
| #39 | Spread: Arsenal FC (-2.5) | Sports | **NO** | `0.964` | `0.942` | `97.8%` | `$3.30` | `$-0.08` | https://www.uefa.com/ |

## 🔍 Последние проверенные кандидаты и фильтр стакана CLOB
| Рынок | Кат. | Сторона | Оценка бота | Цена Ask | Перекос (Edge) | Проскальзывание CLOB | Решение |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Spread: Pacers (-3.5) | Sports | NO | `97.5%` | `51.0%` | `+46.5 п.п.` | `1.00%` | REJECTED: Contract price $0.510 outside sweet spot [$0.84, $0.96] |
| Dota 2: salamit vs HULIGANI - Game 2 Winner | Sports | YES | `1.5%` | `100.0%` | `-98.5 п.п.` | `100.00%` | REJECTED: Edge -98.5 pp < 2 pp threshold (P_est=1.5% vs AskVWAP=100.0%) |
| Spread: Clippers (-4.5) | Sports | NO | `97.5%` | `48.0%` | `+49.5 п.п.` | `1.00%` | REJECTED: Contract price $0.480 outside sweet spot [$0.84, $0.96] |
| Will the highest temperature in Tokyo be 26°C on O | Weather | NO | `13.1%` | `8.0%` | `+5.1 п.п.` | `4.00%` | REJECTED: Win probability 13.1% < 92% minimum (no underdog lottery bets) |
| Exact Score: Celtic FC 2 - 2 RC Celta de Vigo? | Sports | NO | `98.5%` | `94.0%` | `+4.5 п.п.` | `1.00%` | REJECTED: Max open positions (4) reached |
| Will NDP win the most seats in the 2026 British Co | Geopolitics | YES | `16.5%` | `12.0%` | `+4.5 п.п.` | `2.00%` | REJECTED: Win probability 16.5% < 92% minimum (no underdog lottery bets) |
| Will Bitcoin reach $92,000 October 19-25? | Crypto | YES | `11.8%` | `3.1%` | `+8.8 п.п.` | `0.40%` | REJECTED: Win probability 11.8% < 92% minimum (no underdog lottery bets) |
| Will voter turnout in the second round of the 2026 | Geopolitics | YES | `21.0%` | `16.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Win probability 21.0% < 92% minimum (no underdog lottery bets) |
| Will Conservative win the most seats in the 2026 B | Geopolitics | NO | `17.2%` | `11.0%` | `+6.2 п.п.` | `1.00%` | REJECTED: Win probability 17.2% < 92% minimum (no underdog lottery bets) |
| Will the price of Bitcoin be above $86,000 on Octo | Crypto | YES | `23.5%` | `13.5%` | `+10.0 п.п.` | `0.50%` | REJECTED: Win probability 23.5% < 92% minimum (no underdog lottery bets) |
| Will Bitcoin dip to $80,000 October 19-25? | Crypto | YES | `26.6%` | `9.0%` | `+17.6 п.п.` | `1.00%` | REJECTED: Win probability 26.6% < 92% minimum (no underdog lottery bets) |
| Will Bitcoin reach $90,000 October 19-25? | Crypto | YES | `23.5%` | `8.1%` | `+15.4 п.п.` | `0.40%` | REJECTED: Win probability 23.5% < 92% minimum (no underdog lottery bets) |
| Will Iliana Iotova win the 2026 Bulgarian presiden | Geopolitics | NO | `97.8%` | `92.9%` | `+4.9 п.п.` | `0.50%` | REJECTED: Max open positions (4) reached |
| Counter-Strike: Lavked vs Spirit Academy (BO3) - C | Sports | NO | `93.5%` | `89.0%` | `+4.5 п.п.` | `3.00%` | REJECTED: CLOB round-trip slippage 3.00% > 2.0% limit |
| Will the price of Bitcoin be above $80,000 on Octo | Crypto | NO | `11.0%` | `3.9%` | `+7.1 п.п.` | `0.42%` | REJECTED: Win probability 11.0% < 92% minimum (no underdog lottery bets) |
| Will NDP win the most seats in the 2026 British Co | Geopolitics | YES | `16.5%` | `12.0%` | `+4.5 п.п.` | `2.00%` | REJECTED: Win probability 16.5% < 92% minimum (no underdog lottery bets) |
| Will Elon Musk post 280-299 tweets from October 16 | Geopolitics | YES | `12.6%` | `7.0%` | `+5.6 п.п.` | `1.00%` | REJECTED: Win probability 12.6% < 92% minimum (no underdog lottery bets) |
| Will Bitcoin reach $92,000 October 19-25? | Crypto | YES | `8.6%` | `2.7%` | `+5.9 п.п.` | `0.50%` | REJECTED: Win probability 8.6% < 92% minimum (no underdog lottery bets) |
