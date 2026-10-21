# 📊 Отчёт симулятора Polymarket (Устав Grok Bot — Демо-счёт)
**Обновлено:** `2026-10-21 18:22:46 UTC`

## 💰 Состояние виртуального портфеля
| Показатель | Значение | Правило устава |
| :--- | :--- | :--- |
| **Стартовый капитал** | `$50.00 USDC` | Не добавлять деньги |
| **Текущий баланс (Equity)** | **`$26.69 USDC`** (`-23.31$` / `-46.62%`) | Cash + Mark-to-Market по CLOB Bid |
| **Свободный кэш / В сделках** | `$16.80` / `$9.89 USDC` | До 8 открытых позиций, макс 8% банка |
| **Цель окупаемости подписки** | `$-23.31 / $60.00` (`0.0%`) | Цель: +$60.00 в месяц |
| **Просадка от пика (Текущая / Макс)** | `4.85%` / `4.90%` (Пик: `$28.05`) | Стоп-кран при просадке 40% |
| **Закрытых сделок / Win Rate** | `35` / `25.7%` | Brier Score: `0.4280` |

## 📂 Открытые позиции (4 / 8)
| # | Рынок | Кат. | Исход | Вход (Ask VWAP) | Текущий Bid | Оценка бота | Размер ($) | Нереализ. PnL | Источник |
| :- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| #35 | Will Bitcoin dip to $80,000 in October? | Crypto | **YES** | `0.610` | `0.280` | `99.5%` | `$1.11` | `$-0.60` | Kraken BTCUSDT 1m/1h Spot Klin |
| #36 | US x Iran ceasefire continues through October 22? | Geopolitics | **YES** | `0.953` | `0.979` | `98.0%` | `$3.30` | `$+0.09` | Official NFL data feed |
| #38 | Will the Bank of Russia decrease the key rate after the | Other | **NO** | `0.900` | `0.750` | `97.0%` | `$3.30` | `$-0.55` | https://www.cbr.ru/eng/dkp/cal |
| #39 | Spread: Arsenal FC (-2.5) | Sports | **NO** | `0.964` | `0.946` | `98.2%` | `$3.30` | `$-0.06` | https://www.uefa.com/ |

## 🔍 Последние проверенные кандидаты и фильтр стакана CLOB
| Рынок | Кат. | Сторона | Оценка бота | Цена Ask | Перекос (Edge) | Проскальзывание CLOB | Решение |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Valorant: CGN Esports vs Joblife (BO3) - Project B | Sports | NO | `1.5%` | `100.0%` | `-98.5 п.п.` | `100.00%` | REJECTED: Edge -98.5 pp < 2 pp threshold (P_est=1.5% vs AskVWAP=100.0%) |
| Spread: Pacers (-3.5) | Sports | NO | `97.5%` | `51.0%` | `+46.5 п.п.` | `1.00%` | REJECTED: Contract price $0.510 outside sweet spot [$0.84, $0.96] |
| Dota 2: salamit vs HULIGANI - Game 2 Winner | Sports | YES | `1.5%` | `100.0%` | `-98.5 п.п.` | `100.00%` | REJECTED: Edge -98.5 pp < 2 pp threshold (P_est=1.5% vs AskVWAP=100.0%) |
| Spread: Clippers (-4.5) | Sports | NO | `97.5%` | `48.0%` | `+49.5 п.п.` | `1.00%` | REJECTED: Contract price $0.480 outside sweet spot [$0.84, $0.96] |
| Hornets vs. Nets | Sports | NO | `54.0%` | `49.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Win probability 54.0% < 92% minimum (no underdog lottery bets) |
| Will the highest temperature in Tokyo be 26°C on O | Weather | NO | `12.3%` | `8.0%` | `+4.3 п.п.` | `4.00%` | REJECTED: Win probability 12.3% < 92% minimum (no underdog lottery bets) |
| Exact Score: Celtic FC 2 - 2 RC Celta de Vigo? | Sports | NO | `98.5%` | `94.0%` | `+4.5 п.п.` | `1.00%` | REJECTED: Max open positions (4) reached |
| Will NDP win the most seats in the 2026 British Co | Geopolitics | YES | `16.5%` | `12.0%` | `+4.5 п.п.` | `2.00%` | REJECTED: Win probability 16.5% < 92% minimum (no underdog lottery bets) |
| Will Bitcoin reach $92,000 October 19-25? | Crypto | YES | `11.8%` | `3.3%` | `+8.5 п.п.` | `0.70%` | REJECTED: Win probability 11.8% < 92% minimum (no underdog lottery bets) |
| Will voter turnout in the second round of the 2026 | Geopolitics | YES | `21.0%` | `16.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Win probability 21.0% < 92% minimum (no underdog lottery bets) |
| Will Conservative win the most seats in the 2026 B | Geopolitics | NO | `15.5%` | `11.0%` | `+4.5 п.п.` | `1.00%` | REJECTED: Win probability 15.5% < 92% minimum (no underdog lottery bets) |
| Will the price of Bitcoin be above $86,000 on Octo | Crypto | YES | `23.5%` | `14.0%` | `+9.5 п.п.` | `0.80%` | REJECTED: Win probability 23.5% < 92% minimum (no underdog lottery bets) |
| Will Bitcoin dip to $80,000 October 19-25? | Crypto | YES | `26.6%` | `9.0%` | `+17.6 п.п.` | `1.83%` | REJECTED: Win probability 26.6% < 92% minimum (no underdog lottery bets) |
| Will Bitcoin reach $90,000 October 19-25? | Crypto | YES | `23.5%` | `7.8%` | `+15.7 п.п.` | `0.40%` | REJECTED: Win probability 23.5% < 92% minimum (no underdog lottery bets) |
| Will Iliana Iotova win the 2026 Bulgarian presiden | Geopolitics | NO | `97.5%` | `92.9%` | `+4.6 п.п.` | `0.50%` | REJECTED: Max open positions (4) reached |
| Will "Grand Theft Auto VI Launch Trailer" get betw | Other | NO | `22.3%` | `11.7%` | `+10.7 п.п.` | `1.85%` | REJECTED: Win probability 22.3% < 92% minimum (no underdog lottery bets) |
| Spread: Pacers (-3.5) | Sports | NO | `97.5%` | `51.0%` | `+46.5 п.п.` | `1.00%` | REJECTED: Contract price $0.510 outside sweet spot [$0.84, $0.96] |
| Dota 2: salamit vs HULIGANI - Game 2 Winner | Sports | YES | `1.5%` | `100.0%` | `-98.5 п.п.` | `100.00%` | REJECTED: Edge -98.5 pp < 2 pp threshold (P_est=1.5% vs AskVWAP=100.0%) |
