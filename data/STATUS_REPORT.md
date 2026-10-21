# 📊 Отчёт симулятора Polymarket (Устав Grok Bot — Демо-счёт)
**Обновлено:** `2026-10-21 02:15:09 UTC`

## 💰 Состояние виртуального портфеля
| Показатель | Значение | Правило устава |
| :--- | :--- | :--- |
| **Стартовый капитал** | `$50.00 USDC` | Не добавлять деньги |
| **Текущий баланс (Equity)** | **`$27.50 USDC`** (`-22.50$` / `-45.00%`) | Cash + Mark-to-Market по CLOB Bid |
| **Свободный кэш / В сделках** | `$16.80` / `$10.70 USDC` | До 8 открытых позиций, макс 8% банка |
| **Цель окупаемости подписки** | `$-22.50 / $60.00` (`0.0%`) | Цель: +$60.00 в месяц |
| **Просадка от пика (Текущая / Макс)** | `1.95%` / `2.16%` (Пик: `$28.05`) | Стоп-кран при просадке 40% |
| **Закрытых сделок / Win Rate** | `35` / `25.7%` | Brier Score: `0.4280` |

## 📂 Открытые позиции (4 / 8)
| # | Рынок | Кат. | Исход | Вход (Ask VWAP) | Текущий Bid | Оценка бота | Размер ($) | Нереализ. PnL | Источник |
| :- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| #35 | Will Bitcoin dip to $80,000 in October? | Crypto | **YES** | `0.610` | `0.520` | `99.5%` | `$1.11` | `$-0.16` | Kraken BTCUSDT 1m/1h Spot Klin |
| #36 | US x Iran ceasefire continues through October 22? | Geopolitics | **YES** | `0.953` | `0.948` | `98.0%` | `$3.30` | `$-0.02` | Official NFL data feed |
| #38 | Will the Bank of Russia decrease the key rate after the | Other | **NO** | `0.900` | `0.870` | `97.0%` | `$3.30` | `$-0.11` | https://www.cbr.ru/eng/dkp/cal |
| #39 | Spread: Arsenal FC (-2.5) | Sports | **NO** | `0.964` | `0.959` | `98.5%` | `$3.30` | `$-0.02` | https://www.uefa.com/ |

## 🔍 Последние проверенные кандидаты и фильтр стакана CLOB
| Рынок | Кат. | Сторона | Оценка бота | Цена Ask | Перекос (Edge) | Проскальзывание CLOB | Решение |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| UFC 333: Merab Dvalishvili vs. Petr Yan (Bantamwei | Sports | YES | `46.0%` | `41.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Win probability 46.0% < 92% minimum (no underdog lottery bets) |
| Will Bitcoin dip to $79,000 on October 20? | Crypto | YES | `1.5%` | `100.0%` | `-98.5 п.п.` | `100.00%` | REJECTED: Edge -98.5 pp < 2 pp threshold (P_est=1.5% vs AskVWAP=100.0%) |
| Will "Grand Theft Auto VI Launch Trailer" get betw | Other | NO | `25.7%` | `17.9%` | `+7.8 п.п.` | `1.75%` | REJECTED: Win probability 25.7% < 92% minimum (no underdog lottery bets) |
| Spread: Steelers (-3.5) | Sports | NO | `97.5%` | `53.0%` | `+44.5 п.п.` | `1.00%` | REJECTED: Contract price $0.530 outside sweet spot [$0.84, $0.96] |
| Will the price of Bitcoin be above $84,000 on Octo | Crypto | YES | `24.5%` | `15.0%` | `+9.5 п.п.` | `1.00%` | REJECTED: Win probability 24.5% < 92% minimum (no underdog lottery bets) |
| Hawks vs. Magic | Sports | NO | `63.0%` | `58.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Win probability 63.0% < 92% minimum (no underdog lottery bets) |
| Will Bitcoin reach $86,000 on October 20? | Crypto | YES | `1.5%` | `100.0%` | `-98.5 п.п.` | `100.00%` | REJECTED: Edge -98.5 pp < 2 pp threshold (P_est=1.5% vs AskVWAP=100.0%) |
| Counter-Strike: magic vs TheMongolz (BO3) - 1win P | Sports | NO | `58.2%` | `53.0%` | `+5.2 п.п.` | `1.00%` | REJECTED: Win probability 58.2% < 92% minimum (no underdog lottery bets) |
| Will Aleksandar Vučić – United Serbia win the most | Geopolitics | YES | `74.0%` | `69.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Win probability 74.0% < 92% minimum (no underdog lottery bets) |
| Will FC Bayern München win on 2026-10-21? | Sports | YES | `53.0%` | `48.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Win probability 53.0% < 92% minimum (no underdog lottery bets) |
| Will the price of Bitcoin be above $88,000 on Octo | Crypto | YES | `7.1%` | `3.0%` | `+4.1 п.п.` | `1.51%` | REJECTED: Win probability 7.1% < 92% minimum (no underdog lottery bets) |
| Will the price of Bitcoin be above $86,000 on Octo | Crypto | YES | `11.8%` | `3.4%` | `+8.4 п.п.` | `0.24%` | REJECTED: Win probability 11.8% < 92% minimum (no underdog lottery bets) |
| Will the price of Bitcoin be above $80,000 on Octo | Crypto | NO | `12.3%` | `4.5%` | `+7.8 п.п.` | `0.10%` | REJECTED: Win probability 12.3% < 92% minimum (no underdog lottery bets) |
| Will RB Leipzig win on 2026-10-21? | Sports | YES | `14.0%` | `9.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Win probability 14.0% < 92% minimum (no underdog lottery bets) |
| Will the price of Bitcoin be above $82,000 on Octo | Crypto | NO | `25.7%` | `21.0%` | `+4.7 п.п.` | `1.00%` | REJECTED: Win probability 25.7% < 92% minimum (no underdog lottery bets) |
| Will the price of Ethereum be above $2,500 on Octo | Crypto | YES | `21.2%` | `12.0%` | `+9.2 п.п.` | `1.00%` | REJECTED: Win probability 21.2% < 92% minimum (no underdog lottery bets) |
| Will "Grand Theft Auto VI Launch Trailer" get betw | Other | NO | `89.5%` | `85.0%` | `+4.5 п.п.` | `2.00%` | REJECTED: Win probability 89.5% < 92% minimum (no underdog lottery bets) |
| UFC 333: Merab Dvalishvili vs. Petr Yan (Bantamwei | Sports | YES | `46.0%` | `41.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Win probability 46.0% < 92% minimum (no underdog lottery bets) |
