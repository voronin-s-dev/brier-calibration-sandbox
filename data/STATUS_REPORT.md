# 📊 Отчёт симулятора Polymarket (Устав Grok Bot — Демо-счёт)
**Обновлено:** `2026-10-21 22:05:55 UTC`

## 💰 Состояние виртуального портфеля
| Показатель | Значение | Правило устава |
| :--- | :--- | :--- |
| **Стартовый капитал** | `$50.00 USDC` | Не добавлять деньги |
| **Текущий баланс (Equity)** | **`$26.85 USDC`** (`-23.15$` / `-46.31%`) | Cash + Mark-to-Market по CLOB Bid |
| **Свободный кэш / В сделках** | `$17.03` / `$9.81 USDC` | До 8 открытых позиций, макс 8% банка |
| **Цель окупаемости подписки** | `$-23.15 / $60.00` (`0.0%`) | Цель: +$60.00 в месяц |
| **Просадка от пика (Текущая / Макс)** | `4.28%` / `6.31%` (Пик: `$28.05`) | Стоп-кран при просадке 40% |
| **Закрытых сделок / Win Rate** | `36` / `27.8%` | Brier Score: `0.3669` |

## 📂 Открытые позиции (4 / 8)
| # | Рынок | Кат. | Исход | Вход (Ask VWAP) | Текущий Bid | Оценка бота | Размер ($) | Нереализ. PnL | Источник |
| :- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| #35 | Will Bitcoin dip to $80,000 in October? | Crypto | **YES** | `0.610` | `0.280` | `99.5%` | `$1.11` | `$-0.60` | Kraken BTCUSDT 1m/1h Spot Klin |
| #36 | US x Iran ceasefire continues through October 22? | Geopolitics | **YES** | `0.953` | `0.881` | `98.0%` | `$3.30` | `$-0.25` | Official NFL data feed |
| #38 | Will the Bank of Russia decrease the key rate after the | Other | **NO** | `0.900` | `0.830` | `97.0%` | `$3.30` | `$-0.26` | https://www.cbr.ru/eng/dkp/cal |
| #40 | Will Bitcoin reach $86,000 on October 21? | Crypto | **NO** | `0.941` | `0.947` | `97.8%` | `$3.19` | `$+0.02` | https://www.binance.com/en/tra |

## 🔍 Последние проверенные кандидаты и фильтр стакана CLOB
| Рынок | Кат. | Сторона | Оценка бота | Цена Ask | Перекос (Edge) | Проскальзывание CLOB | Решение |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Spread: Wizards (-4.5) | Sports | NO | `97.5%` | `52.0%` | `+45.5 п.п.` | `1.00%` | REJECTED: Contract price $0.520 outside sweet spot [$0.84, $0.96] |
| Spread: Pacers (-3.5) | Sports | NO | `97.5%` | `53.0%` | `+44.5 п.п.` | `1.00%` | REJECTED: Contract price $0.530 outside sweet spot [$0.84, $0.96] |
| Spread: Clippers (-4.5) | Sports | NO | `97.5%` | `49.0%` | `+48.5 п.п.` | `2.00%` | REJECTED: Contract price $0.490 outside sweet spot [$0.84, $0.96] |
| Hawks vs. Magic | Sports | NO | `60.1%` | `56.0%` | `+4.1 п.п.` | `1.00%` | REJECTED: Win probability 60.1% < 92% minimum (no underdog lottery bets) |
| Hornets vs. Nets | Sports | YES | `57.9%` | `53.0%` | `+4.9 п.п.` | `1.00%` | REJECTED: Win probability 57.9% < 92% minimum (no underdog lottery bets) |
| Will Bitcoin dip to $78,000 October 19-25? | Crypto | YES | `11.2%` | `3.0%` | `+8.2 п.п.` | `0.40%` | REJECTED: Win probability 11.2% < 92% minimum (no underdog lottery bets) |
| Will the highest temperature in Tokyo be 26°C on O | Weather | NO | `12.3%` | `6.6%` | `+5.7 п.п.` | `2.58%` | REJECTED: Win probability 12.3% < 92% minimum (no underdog lottery bets) |
| Will the price of Bitcoin be above $82,000 on Octo | Crypto | NO | `15.5%` | `7.0%` | `+8.5 п.п.` | `1.00%` | REJECTED: Win probability 15.5% < 92% minimum (no underdog lottery bets) |
| Exact Score: Celtic FC 2 - 2 RC Celta de Vigo? | Sports | NO | `98.5%` | `94.0%` | `+4.5 п.п.` | `1.00%` | REJECTED: Max open positions (4) reached |
| Will NDP win the most seats in the 2026 British Co | Geopolitics | YES | `16.0%` | `11.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Win probability 16.0% < 92% minimum (no underdog lottery bets) |
| Will Bitcoin reach $92,000 October 19-25? | Crypto | YES | `11.6%` | `2.7%` | `+8.9 п.п.` | `0.80%` | REJECTED: Win probability 11.6% < 92% minimum (no underdog lottery bets) |
| Will Conservative win the most seats in the 2026 B | Geopolitics | NO | `22.2%` | `11.0%` | `+11.2 п.п.` | `1.00%` | REJECTED: Win probability 22.2% < 92% minimum (no underdog lottery bets) |
| Will the price of Bitcoin be above $86,000 on Octo | Crypto | YES | `22.9%` | `11.8%` | `+11.1 п.п.` | `0.70%` | REJECTED: Win probability 22.9% < 92% minimum (no underdog lottery bets) |
| Will Bitcoin dip to $80,000 October 19-25? | Crypto | YES | `25.1%` | `9.0%` | `+16.1 п.п.` | `1.00%` | REJECTED: Win probability 25.1% < 92% minimum (no underdog lottery bets) |
| Will Bitcoin reach $90,000 October 19-25? | Crypto | YES | `23.3%` | `6.7%` | `+16.6 п.п.` | `0.40%` | REJECTED: Win probability 23.3% < 92% minimum (no underdog lottery bets) |
| Spread: Clippers (-4.5) | Sports | NO | `97.5%` | `49.0%` | `+48.5 п.п.` | `2.00%` | REJECTED: Contract price $0.490 outside sweet spot [$0.84, $0.96] |
| Hawks vs. Magic | Sports | NO | `60.3%` | `56.0%` | `+4.3 п.п.` | `1.00%` | REJECTED: Win probability 60.3% < 92% minimum (no underdog lottery bets) |
| Hornets vs. Nets | Sports | YES | `58.1%` | `53.0%` | `+5.1 п.п.` | `1.00%` | REJECTED: Win probability 58.1% < 92% minimum (no underdog lottery bets) |
