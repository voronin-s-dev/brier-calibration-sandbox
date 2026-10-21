# 📊 Отчёт симулятора Polymarket (Устав Grok Bot — Демо-счёт)
**Обновлено:** `2026-10-21 01:56:34 UTC`

## 💰 Состояние виртуального портфеля
| Показатель | Значение | Правило устава |
| :--- | :--- | :--- |
| **Стартовый капитал** | `$50.00 USDC` | Не добавлять деньги |
| **Текущий баланс (Equity)** | **`$27.44 USDC`** (`-22.56$` / `-45.11%`) | Cash + Mark-to-Market по CLOB Bid |
| **Свободный кэш / В сделках** | `$16.80` / `$10.64 USDC` | До 8 открытых позиций, макс 8% банка |
| **Цель окупаемости подписки** | `$-22.56 / $60.00` (`0.0%`) | Цель: +$60.00 в месяц |
| **Просадка от пика (Текущая / Макс)** | `2.16%` / `2.16%` (Пик: `$28.05`) | Стоп-кран при просадке 40% |
| **Закрытых сделок / Win Rate** | `35` / `25.7%` | Brier Score: `0.4280` |

## 📂 Открытые позиции (4 / 8)
| # | Рынок | Кат. | Исход | Вход (Ask VWAP) | Текущий Bid | Оценка бота | Размер ($) | Нереализ. PnL | Источник |
| :- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| #35 | Will Bitcoin dip to $80,000 in October? | Crypto | **YES** | `0.610` | `0.490` | `99.5%` | `$1.11` | `$-0.22` | Kraken BTCUSDT 1m/1h Spot Klin |
| #36 | US x Iran ceasefire continues through October 22? | Geopolitics | **YES** | `0.953` | `0.948` | `98.0%` | `$3.30` | `$-0.02` | Official NFL data feed |
| #38 | Will the Bank of Russia decrease the key rate after the | Other | **NO** | `0.900` | `0.870` | `97.0%` | `$3.30` | `$-0.11` | https://www.cbr.ru/eng/dkp/cal |
| #39 | Spread: Arsenal FC (-2.5) | Sports | **NO** | `0.964` | `0.958` | `98.5%` | `$3.30` | `$-0.02` | https://www.uefa.com/ |

## 🔍 Последние проверенные кандидаты и фильтр стакана CLOB
| Рынок | Кат. | Сторона | Оценка бота | Цена Ask | Перекос (Edge) | Проскальзывание CLOB | Решение |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Will Bitcoin dip to $79,000 on October 20? | Crypto | YES | `1.5%` | `100.0%` | `-98.5 п.п.` | `100.00%` | REJECTED: Edge -98.5 pp < 2 pp threshold (P_est=1.5% vs AskVWAP=100.0%) |
| Will "Grand Theft Auto VI Launch Trailer" get betw | Other | NO | `22.7%` | `18.0%` | `+4.7 п.п.` | `1.60%` | REJECTED: Win probability 22.7% < 92% minimum (no underdog lottery bets) |
| Spread: Steelers (-3.5) | Sports | NO | `97.5%` | `53.0%` | `+44.5 п.п.` | `1.00%` | REJECTED: Contract price $0.530 outside sweet spot [$0.84, $0.96] |
| Will the price of Bitcoin be above $84,000 on Octo | Crypto | YES | `26.2%` | `21.0%` | `+5.2 п.п.` | `1.00%` | REJECTED: Win probability 26.2% < 92% minimum (no underdog lottery bets) |
| Counter-Strike: magic vs TheMongolz (BO3) - 1win P | Sports | NO | `59.4%` | `53.0%` | `+6.4 п.п.` | `1.00%` | REJECTED: Win probability 59.4% < 92% minimum (no underdog lottery bets) |
| Hawks vs. Magic | Sports | NO | `63.0%` | `58.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Win probability 63.0% < 92% minimum (no underdog lottery bets) |
| Will Bitcoin reach $86,000 on October 20? | Crypto | YES | `1.5%` | `100.0%` | `-98.5 п.п.` | `100.00%` | REJECTED: Edge -98.5 pp < 2 pp threshold (P_est=1.5% vs AskVWAP=100.0%) |
| Will Aleksandar Vučić – United Serbia win the most | Geopolitics | YES | `74.0%` | `69.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Win probability 74.0% < 92% minimum (no underdog lottery bets) |
| Will FC Bayern München win on 2026-10-21? | Sports | YES | `53.0%` | `48.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Win probability 53.0% < 92% minimum (no underdog lottery bets) |
| Will the price of Bitcoin be above $86,000 on Octo | Crypto | YES | `12.1%` | `5.1%` | `+7.0 п.п.` | `1.00%` | REJECTED: Win probability 12.1% < 92% minimum (no underdog lottery bets) |
| Will the price of Bitcoin be above $80,000 on Octo | Crypto | NO | `12.1%` | `4.0%` | `+8.1 п.п.` | `0.10%` | REJECTED: Win probability 12.1% < 92% minimum (no underdog lottery bets) |
| Will RB Leipzig win on 2026-10-21? | Sports | YES | `14.0%` | `9.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Win probability 14.0% < 92% minimum (no underdog lottery bets) |
| Will the price of Bitcoin be above $82,000 on Octo | Crypto | NO | `25.3%` | `14.0%` | `+11.3 п.п.` | `1.00%` | REJECTED: Win probability 25.3% < 92% minimum (no underdog lottery bets) |
| Spread: Arsenal FC (-2.5) | Sports | NO | `98.5%` | `96.4%` | `+2.1 п.п.` | `0.60%` | EXECUTED BUY #39 ($3.30 @ 0.9640) |
| Will "Grand Theft Auto VI Launch Trailer" get betw | Other | NO | `89.5%` | `85.0%` | `+4.5 п.п.` | `2.00%` | REJECTED: Win probability 89.5% < 92% minimum (no underdog lottery bets) |
| Will Bitcoin reach $87,000 on October 20? | Crypto | YES | `1.5%` | `100.0%` | `-98.5 п.п.` | `100.00%` | REJECTED: Edge -98.5 pp < 2 pp threshold (P_est=1.5% vs AskVWAP=100.0%) |
| Spread: Lions (-3.5) | Sports | NO | `97.5%` | `53.0%` | `+44.5 п.п.` | `1.00%` | REJECTED: Contract price $0.530 outside sweet spot [$0.84, $0.96] |
| Spread: Rams (-3.5) | Sports | NO | `97.5%` | `49.0%` | `+48.5 п.п.` | `1.00%` | REJECTED: Contract price $0.490 outside sweet spot [$0.84, $0.96] |
