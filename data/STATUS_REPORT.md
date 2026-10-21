# 📊 Отчёт симулятора Polymarket (Устав Grok Bot — Демо-счёт)
**Обновлено:** `2026-10-21 18:32:07 UTC`

## 💰 Состояние виртуального портфеля
| Показатель | Значение | Правило устава |
| :--- | :--- | :--- |
| **Стартовый капитал** | `$50.00 USDC` | Не добавлять деньги |
| **Текущий баланс (Equity)** | **`$26.71 USDC`** (`-23.29$` / `-46.57%`) | Cash + Mark-to-Market по CLOB Bid |
| **Свободный кэш / В сделках** | `$16.80` / `$9.91 USDC` | До 8 открытых позиций, макс 8% банка |
| **Цель окупаемости подписки** | `$-23.29 / $60.00` (`0.0%`) | Цель: +$60.00 в месяц |
| **Просадка от пика (Текущая / Макс)** | `4.76%` / `5.15%` (Пик: `$28.05`) | Стоп-кран при просадке 40% |
| **Закрытых сделок / Win Rate** | `35` / `25.7%` | Brier Score: `0.4280` |

## 📂 Открытые позиции (4 / 8)
| # | Рынок | Кат. | Исход | Вход (Ask VWAP) | Текущий Bid | Оценка бота | Размер ($) | Нереализ. PnL | Источник |
| :- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| #35 | Will Bitcoin dip to $80,000 in October? | Crypto | **YES** | `0.610` | `0.270` | `99.5%` | `$1.11` | `$-0.62` | Kraken BTCUSDT 1m/1h Spot Klin |
| #36 | US x Iran ceasefire continues through October 22? | Geopolitics | **YES** | `0.953` | `0.960` | `98.0%` | `$3.30` | `$+0.02` | Official NFL data feed |
| #38 | Will the Bank of Russia decrease the key rate after the | Other | **NO** | `0.900` | `0.780` | `97.0%` | `$3.30` | `$-0.44` | https://www.cbr.ru/eng/dkp/cal |
| #39 | Spread: Arsenal FC (-2.5) | Sports | **NO** | `0.964` | `0.946` | `98.4%` | `$3.30` | `$-0.06` | https://www.uefa.com/ |

## 🔍 Последние проверенные кандидаты и фильтр стакана CLOB
| Рынок | Кат. | Сторона | Оценка бота | Цена Ask | Перекос (Edge) | Проскальзывание CLOB | Решение |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Will Flávio Bolsonaro win the second round of the  | Geopolitics | YES | `38.0%` | `33.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Win probability 38.0% < 92% minimum (no underdog lottery bets) |
| Valorant: CGN Esports vs Joblife (BO3) - Project B | Sports | NO | `1.5%` | `100.0%` | `-98.5 п.п.` | `100.00%` | REJECTED: Edge -98.5 pp < 2 pp threshold (P_est=1.5% vs AskVWAP=100.0%) |
| Spread: Pacers (-3.5) | Sports | NO | `97.5%` | `51.0%` | `+46.5 п.п.` | `1.00%` | REJECTED: Contract price $0.510 outside sweet spot [$0.84, $0.96] |
| Dota 2: salamit vs HULIGANI - Game 2 Winner | Sports | YES | `1.5%` | `100.0%` | `-98.5 п.п.` | `100.00%` | REJECTED: Edge -98.5 pp < 2 pp threshold (P_est=1.5% vs AskVWAP=100.0%) |
| Counter-Strike: TheMongolz vs PRIVATE (BO3) - 1win | Sports | YES | `62.9%` | `68.0%` | `-5.1 п.п.` | `1.00%` | REJECTED: Edge -5.1 pp < 2 pp threshold (P_est=62.9% vs AskVWAP=68.0%) |
| Spread: Clippers (-4.5) | Sports | NO | `97.5%` | `48.0%` | `+49.5 п.п.` | `1.00%` | REJECTED: Contract price $0.480 outside sweet spot [$0.84, $0.96] |
| Hornets vs. Nets | Sports | NO | `54.0%` | `49.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Win probability 54.0% < 92% minimum (no underdog lottery bets) |
| Will the highest temperature in Tokyo be 26°C on O | Weather | NO | `12.4%` | `8.0%` | `+4.4 п.п.` | `4.00%` | REJECTED: Win probability 12.4% < 92% minimum (no underdog lottery bets) |
| Exact Score: Celtic FC 2 - 2 RC Celta de Vigo? | Sports | NO | `98.5%` | `94.0%` | `+4.5 п.п.` | `1.00%` | REJECTED: Max open positions (4) reached |
| Will Bitcoin reach $92,000 October 19-25? | Crypto | YES | `11.8%` | `3.1%` | `+8.7 п.п.` | `0.50%` | REJECTED: Win probability 11.8% < 92% minimum (no underdog lottery bets) |
| Will voter turnout in the second round of the 2026 | Geopolitics | YES | `21.0%` | `16.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Win probability 21.0% < 92% minimum (no underdog lottery bets) |
| Will the price of Bitcoin be above $86,000 on Octo | Crypto | YES | `23.7%` | `15.3%` | `+8.4 п.п.` | `0.90%` | REJECTED: Win probability 23.7% < 92% minimum (no underdog lottery bets) |
| Will Bitcoin reach $90,000 October 19-25? | Crypto | YES | `23.5%` | `8.3%` | `+15.2 п.п.` | `0.60%` | REJECTED: Win probability 23.5% < 92% minimum (no underdog lottery bets) |
| Will Bitcoin dip to $80,000 October 19-25? | Crypto | YES | `26.3%` | `8.0%` | `+18.3 п.п.` | `1.00%` | REJECTED: Win probability 26.3% < 92% minimum (no underdog lottery bets) |
| Will "Grand Theft Auto VI Launch Trailer" get betw | Other | NO | `16.7%` | `12.4%` | `+4.3 п.п.` | `2.48%` | REJECTED: Win probability 16.7% < 92% minimum (no underdog lottery bets) |
| Valorant: CGN Esports vs Joblife (BO3) - Project B | Sports | NO | `1.5%` | `100.0%` | `-98.5 п.п.` | `100.00%` | REJECTED: Edge -98.5 pp < 2 pp threshold (P_est=1.5% vs AskVWAP=100.0%) |
| Spread: Pacers (-3.5) | Sports | NO | `97.5%` | `51.0%` | `+46.5 п.п.` | `1.00%` | REJECTED: Contract price $0.510 outside sweet spot [$0.84, $0.96] |
| Dota 2: salamit vs HULIGANI - Game 2 Winner | Sports | YES | `1.5%` | `100.0%` | `-98.5 п.п.` | `100.00%` | REJECTED: Edge -98.5 pp < 2 pp threshold (P_est=1.5% vs AskVWAP=100.0%) |
