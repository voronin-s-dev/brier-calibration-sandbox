# 📊 Отчёт симулятора Polymarket (Устав Grok Bot — Демо-счёт)
**Обновлено:** `2026-10-21 21:56:33 UTC`

## 💰 Состояние виртуального портфеля
| Показатель | Значение | Правило устава |
| :--- | :--- | :--- |
| **Стартовый капитал** | `$50.00 USDC` | Не добавлять деньги |
| **Текущий баланс (Equity)** | **`$26.58 USDC`** (`-23.42$` / `-46.84%`) | Cash + Mark-to-Market по CLOB Bid |
| **Свободный кэш / В сделках** | `$17.03` / `$9.55 USDC` | До 8 открытых позиций, макс 8% банка |
| **Цель окупаемости подписки** | `$-23.42 / $60.00` (`0.0%`) | Цель: +$60.00 в месяц |
| **Просадка от пика (Текущая / Макс)** | `5.23%` / `6.31%` (Пик: `$28.05`) | Стоп-кран при просадке 40% |
| **Закрытых сделок / Win Rate** | `36` / `27.8%` | Brier Score: `0.3669` |

## 📂 Открытые позиции (4 / 8)
| # | Рынок | Кат. | Исход | Вход (Ask VWAP) | Текущий Bid | Оценка бота | Размер ($) | Нереализ. PnL | Источник |
| :- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| #35 | Will Bitcoin dip to $80,000 in October? | Crypto | **YES** | `0.610` | `0.270` | `99.5%` | `$1.11` | `$-0.62` | Kraken BTCUSDT 1m/1h Spot Klin |
| #36 | US x Iran ceasefire continues through October 22? | Geopolitics | **YES** | `0.953` | `0.834` | `98.0%` | `$3.30` | `$-0.41` | Official NFL data feed |
| #38 | Will the Bank of Russia decrease the key rate after the | Other | **NO** | `0.900` | `0.820` | `97.0%` | `$3.30` | `$-0.29` | https://www.cbr.ru/eng/dkp/cal |
| #40 | Will Bitcoin reach $86,000 on October 21? | Crypto | **NO** | `0.941` | `0.933` | `96.9%` | `$3.19` | `$-0.03` | https://www.binance.com/en/tra |

## 🔍 Последние проверенные кандидаты и фильтр стакана CLOB
| Рынок | Кат. | Сторона | Оценка бота | Цена Ask | Перекос (Edge) | Проскальзывание CLOB | Решение |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Spread: Clippers (-4.5) | Sports | NO | `97.5%` | `49.0%` | `+48.5 п.п.` | `2.00%` | REJECTED: Contract price $0.490 outside sweet spot [$0.84, $0.96] |
| Hawks vs. Magic | Sports | NO | `60.3%` | `56.0%` | `+4.3 п.п.` | `1.00%` | REJECTED: Win probability 60.3% < 92% minimum (no underdog lottery bets) |
| Hornets vs. Nets | Sports | YES | `58.1%` | `53.0%` | `+5.1 п.п.` | `1.00%` | REJECTED: Win probability 58.1% < 92% minimum (no underdog lottery bets) |
| Will Bitcoin dip to $78,000 October 19-25? | Crypto | YES | `11.3%` | `2.8%` | `+8.5 п.п.` | `0.53%` | REJECTED: Win probability 11.3% < 92% minimum (no underdog lottery bets) |
| Will the highest temperature in Tokyo be 26°C on O | Weather | NO | `12.1%` | `6.0%` | `+6.1 п.п.` | `2.00%` | REJECTED: Win probability 12.1% < 92% minimum (no underdog lottery bets) |
| Will the price of Bitcoin be above $82,000 on Octo | Crypto | NO | `15.7%` | `8.0%` | `+7.7 п.п.` | `2.00%` | REJECTED: Win probability 15.7% < 92% minimum (no underdog lottery bets) |
| Exact Score: Celtic FC 2 - 2 RC Celta de Vigo? | Sports | NO | `98.5%` | `94.0%` | `+4.5 п.п.` | `1.00%` | REJECTED: Max open positions (4) reached |
| Will NDP win the most seats in the 2026 British Co | Geopolitics | YES | `15.5%` | `11.0%` | `+4.5 п.п.` | `2.00%` | REJECTED: Win probability 15.5% < 92% minimum (no underdog lottery bets) |
| Will Bitcoin reach $92,000 October 19-25? | Crypto | YES | `11.7%` | `2.8%` | `+8.9 п.п.` | `0.79%` | REJECTED: Win probability 11.7% < 92% minimum (no underdog lottery bets) |
| Will Conservative win the most seats in the 2026 B | Geopolitics | NO | `21.2%` | `10.0%` | `+11.2 п.п.` | `2.00%` | REJECTED: Win probability 21.2% < 92% minimum (no underdog lottery bets) |
| Will the price of Bitcoin be above $86,000 on Octo | Crypto | YES | `23.5%` | `13.6%` | `+9.9 п.п.` | `0.10%` | REJECTED: Win probability 23.5% < 92% minimum (no underdog lottery bets) |
| Will Bitcoin dip to $80,000 October 19-25? | Crypto | YES | `25.0%` | `9.0%` | `+16.0 п.п.` | `1.00%` | REJECTED: Win probability 25.0% < 92% minimum (no underdog lottery bets) |
| Will Bitcoin reach $90,000 October 19-25? | Crypto | YES | `23.5%` | `7.2%` | `+16.3 п.п.` | `0.50%` | REJECTED: Win probability 23.5% < 92% minimum (no underdog lottery bets) |
| Counter-Strike: FaZe vs Heroic - Map 2 Winner | Sports | NO | `98.5%` | `85.8%` | `+12.7 п.п.` | `2.70%` | REJECTED: CLOB round-trip slippage 2.70% > 2.0% limit |
| Will Bitcoin reach $86,000 on October 21? | Crypto | NO | `96.9%` | `94.1%` | `+2.8 п.п.` | `0.80%` | EXECUTED BUY #40 ($3.19 @ 0.9410) |
| Will Flávio Bolsonaro win the second round of the  | Geopolitics | YES | `38.0%` | `33.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Win probability 38.0% < 92% minimum (no underdog lottery bets) |
| Valorant: CGN Esports vs Joblife (BO3) - Project B | Sports | NO | `1.5%` | `100.0%` | `-98.5 п.п.` | `100.00%` | REJECTED: Edge -98.5 pp < 2 pp threshold (P_est=1.5% vs AskVWAP=100.0%) |
| Spread: Pacers (-3.5) | Sports | NO | `97.5%` | `51.0%` | `+46.5 п.п.` | `1.00%` | REJECTED: Contract price $0.510 outside sweet spot [$0.84, $0.96] |
