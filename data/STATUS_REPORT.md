# 📊 Отчёт симулятора Polymarket (Устав Grok Bot — Демо-счёт)
**Обновлено:** `2026-10-22 15:33:01 UTC`

## 💰 Состояние виртуального портфеля
| Показатель | Значение | Правило устава |
| :--- | :--- | :--- |
| **Стартовый капитал** | `$50.00 USDC` | Не добавлять деньги |
| **Текущий баланс (Equity)** | **`$28.21 USDC`** (`-21.79$` / `-43.57%`) | Cash + Mark-to-Market по CLOB Bid |
| **Свободный кэш / В сделках** | `$17.52` / `$10.69 USDC` | До 8 открытых позиций, макс 8% банка |
| **Цель окупаемости подписки** | `$-21.79 / $60.00` (`0.0%`) | Цель: +$60.00 в месяц |
| **Просадка от пика (Текущая / Макс)** | `0.16%` / `6.31%` (Пик: `$28.26`) | Стоп-кран при просадке 40% |
| **Закрытых сделок / Win Rate** | `39` / `33.3%` | Brier Score: `0.3214` |

## 📂 Открытые позиции (4 / 8)
| # | Рынок | Кат. | Исход | Вход (Ask VWAP) | Текущий Bid | Оценка бота | Размер ($) | Нереализ. PnL | Источник |
| :- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| #35 | Will Bitcoin dip to $80,000 in October? | Crypto | **YES** | `0.610` | `0.680` | `99.5%` | `$1.11` | `$+0.13` | Kraken BTCUSDT 1m/1h Spot Klin |
| #36 | US x Iran ceasefire continues through October 22? | Geopolitics | **YES** | `0.953` | `0.947` | `98.0%` | `$3.30` | `$-0.02` | Official NFL data feed |
| #38 | Will the Bank of Russia decrease the key rate after the | Other | **NO** | `0.900` | `0.770` | `97.0%` | `$3.30` | `$-0.48` | https://www.cbr.ru/eng/dkp/cal |
| #43 | AFC Bournemouth vs. AC Milan: O/U 0.5 | Sports | **YES** | `0.950` | `0.940` | `98.0%` | `$3.39` | `$-0.04` | https://www.uefa.com/ |

## 🔍 Последние проверенные кандидаты и фильтр стакана CLOB
| Рынок | Кат. | Сторона | Оценка бота | Цена Ask | Перекос (Edge) | Проскальзывание CLOB | Решение |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Will Lamine Yamal win the 2026 Ballon d'Or? | Other | YES | `27.6%` | `16.6%` | `+11.0 п.п.` | `0.10%` | REJECTED: Win probability 27.6% < 92% minimum (no underdog lottery bets) |
| LoL: Galions vs Solary - Game 2 Winner | Sports | YES | `1.5%` | `100.0%` | `-98.5 п.п.` | `100.00%` | REJECTED: Edge -98.5 pp < 2 pp threshold (P_est=1.5% vs AskVWAP=100.0%) |
| LoL: Galions vs Solary - Game 3 Winner | Sports | NO | `1.5%` | `100.0%` | `-98.5 п.п.` | `100.00%` | REJECTED: Edge -98.5 pp < 2 pp threshold (P_est=1.5% vs AskVWAP=100.0%) |
| Will the price of Ethereum be above $2,500 on Octo | Crypto | YES | `14.3%` | `7.0%` | `+7.3 п.п.` | `2.00%` | REJECTED: Win probability 14.3% < 92% minimum (no underdog lottery bets) |
| Will Estudiantes de La Plata win on 2026-10-22? | Sports | NO | `98.0%` | `94.0%` | `+4.0 п.п.` | `1.00%` | REJECTED: Max open positions (4) reached |
| Will Lula win the most votes in the second round o | Geopolitics | YES | `92.0%` | `87.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Max open positions (4) reached |
| Torino FC vs. AC Monza: O/U 0.5 | Sports | NO | `11.4%` | `7.0%` | `+4.4 п.п.` | `1.00%` | REJECTED: Win probability 11.4% < 92% minimum (no underdog lottery bets) |
| Will Bitcoin reach $83,000 on October 22? | Crypto | YES | `27.3%` | `14.0%` | `+13.3 п.п.` | `0.80%` | REJECTED: Win probability 27.3% < 92% minimum (no underdog lottery bets) |
| Will Ethereum dip to $2,200 October 19-25? | Crypto | YES | `14.7%` | `6.2%` | `+8.5 п.п.` | `0.90%` | REJECTED: Win probability 14.7% < 92% minimum (no underdog lottery bets) |
| Counter-Strike: PARIVISION vs TheMongolz - Map 1 W | Sports | NO | `94.0%` | `83.0%` | `+11.0 п.п.` | `1.00%` | REJECTED: Contract price $0.830 outside sweet spot [$0.84, $0.96] |
| Will Bitcoin reach $88,000 October 19-25? | Crypto | YES | `10.3%` | `2.6%` | `+7.7 п.п.` | `0.10%` | REJECTED: Win probability 10.3% < 92% minimum (no underdog lottery bets) |
| Will Bitcoin reach $86,000 October 19-25? | Crypto | YES | `22.9%` | `7.0%` | `+15.9 п.п.` | `1.00%` | REJECTED: Win probability 22.9% < 92% minimum (no underdog lottery bets) |
| Will Bitcoin dip to $78,000 October 19-25? | Crypto | YES | `34.6%` | `16.5%` | `+18.1 п.п.` | `0.10%` | REJECTED: Win probability 34.6% < 92% minimum (no underdog lottery bets) |
| Will Bitcoin dip to $76,000 October 19-25? | Crypto | YES | `14.8%` | `4.3%` | `+10.5 п.п.` | `0.30%` | REJECTED: Win probability 14.8% < 92% minimum (no underdog lottery bets) |
| Will Bitcoin dip to $80,000 on October 22? | Crypto | YES | `32.7%` | `17.4%` | `+15.3 п.п.` | `2.07%` | REJECTED: Win probability 32.7% < 92% minimum (no underdog lottery bets) |
| Will the price of Bitcoin be above $80,000 on Octo | Crypto | NO | `24.3%` | `17.0%` | `+7.3 п.п.` | `0.50%` | REJECTED: Win probability 24.3% < 92% minimum (no underdog lottery bets) |
| AFC Bournemouth vs. AC Milan: O/U 0.5 | Sports | YES | `98.0%` | `95.0%` | `+3.0 п.п.` | `1.00%` | EXECUTED BUY #43 ($3.39 @ 0.9500) |
| Will Kylian Mbappé win the 2026 Ballon d'Or? | Other | YES | `10.9%` | `5.9%` | `+5.1 п.п.` | `0.75%` | REJECTED: Win probability 10.9% < 92% minimum (no underdog lottery bets) |
