# 📊 Отчёт симулятора Polymarket (Устав Grok Bot — Демо-счёт)
**Обновлено:** `2026-10-22 15:51:43 UTC`

## 💰 Состояние виртуального портфеля
| Показатель | Значение | Правило устава |
| :--- | :--- | :--- |
| **Стартовый капитал** | `$50.00 USDC` | Не добавлять деньги |
| **Текущий баланс (Equity)** | **`$28.29 USDC`** (`-21.71$` / `-43.42%`) | Cash + Mark-to-Market по CLOB Bid |
| **Свободный кэш / В сделках** | `$17.52` / `$10.77 USDC` | До 8 открытых позиций, макс 8% банка |
| **Цель окупаемости подписки** | `$-21.71 / $60.00` (`0.0%`) | Цель: +$60.00 в месяц |
| **Просадка от пика (Текущая / Макс)** | `0.13%` / `6.31%` (Пик: `$28.32`) | Стоп-кран при просадке 40% |
| **Закрытых сделок / Win Rate** | `39` / `33.3%` | Brier Score: `0.3214` |

## 📂 Открытые позиции (4 / 8)
| # | Рынок | Кат. | Исход | Вход (Ask VWAP) | Текущий Bid | Оценка бота | Размер ($) | Нереализ. PnL | Источник |
| :- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| #35 | Will Bitcoin dip to $80,000 in October? | Crypto | **YES** | `0.610` | `0.690` | `99.5%` | `$1.11` | `$+0.15` | Kraken BTCUSDT 1m/1h Spot Klin |
| #36 | US x Iran ceasefire continues through October 22? | Geopolitics | **YES** | `0.953` | `0.963` | `98.0%` | `$3.30` | `$+0.03` | Official NFL data feed |
| #38 | Will the Bank of Russia decrease the key rate after the | Other | **NO** | `0.900` | `0.770` | `97.0%` | `$3.30` | `$-0.48` | https://www.cbr.ru/eng/dkp/cal |
| #43 | AFC Bournemouth vs. AC Milan: O/U 0.5 | Sports | **YES** | `0.950` | `0.940` | `98.0%` | `$3.39` | `$-0.04` | https://www.uefa.com/ |

## 🔍 Последние проверенные кандидаты и фильтр стакана CLOB
| Рынок | Кат. | Сторона | Оценка бота | Цена Ask | Перекос (Edge) | Проскальзывание CLOB | Решение |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Counter-Strike: BC.Game Esports vs FaZe - Map 2 Wi | Sports | NO | `1.5%` | `100.0%` | `-98.5 п.п.` | `100.00%` | REJECTED: Edge -98.5 pp < 2 pp threshold (P_est=1.5% vs AskVWAP=100.0%) |
| Will Liverpool FC win on 2026-10-25? | Sports | YES | `51.0%` | `46.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Win probability 51.0% < 92% minimum (no underdog lottery bets) |
| Will Lamine Yamal win the 2026 Ballon d'Or? | Other | YES | `28.7%` | `16.6%` | `+12.2 п.п.` | `0.10%` | REJECTED: Win probability 28.7% < 92% minimum (no underdog lottery bets) |
| LoL: Galions vs Solary - Game 4 Winner | Sports | YES | `1.5%` | `100.0%` | `-98.5 п.п.` | `100.00%` | REJECTED: Edge -98.5 pp < 2 pp threshold (P_est=1.5% vs AskVWAP=100.0%) |
| LoL: Galions vs Solary - Game 2 Winner | Sports | YES | `1.5%` | `100.0%` | `-98.5 п.п.` | `100.00%` | REJECTED: Edge -98.5 pp < 2 pp threshold (P_est=1.5% vs AskVWAP=100.0%) |
| Counter-Strike: BC.Game Esports vs FaZe (BO3) - Dr | Sports | NO | `1.5%` | `100.0%` | `-98.5 п.п.` | `100.00%` | REJECTED: Edge -98.5 pp < 2 pp threshold (P_est=1.5% vs AskVWAP=100.0%) |
| LoL: Galions vs Solary - Game 3 Winner | Sports | NO | `1.5%` | `100.0%` | `-98.5 п.п.` | `100.00%` | REJECTED: Edge -98.5 pp < 2 pp threshold (P_est=1.5% vs AskVWAP=100.0%) |
| Dota 2: Team Liquid vs 1win - Game 1 Winner | Sports | NO | `1.5%` | `100.0%` | `-98.5 п.п.` | `100.00%` | REJECTED: Edge -98.5 pp < 2 pp threshold (P_est=1.5% vs AskVWAP=100.0%) |
| Will the price of Ethereum be above $2,500 on Octo | Crypto | YES | `13.8%` | `8.0%` | `+5.8 п.п.` | `3.00%` | REJECTED: Win probability 13.8% < 92% minimum (no underdog lottery bets) |
| Will Flavio Bolsonaro win the most votes in the se | Geopolitics | NO | `91.0%` | `87.0%` | `+4.0 п.п.` | `2.00%` | REJECTED: Win probability 91.0% < 92% minimum (no underdog lottery bets) |
| Torino FC vs. AC Monza: O/U 0.5 | Sports | NO | `11.3%` | `7.0%` | `+4.3 п.п.` | `1.00%` | REJECTED: Win probability 11.3% < 92% minimum (no underdog lottery bets) |
| Will Bitcoin reach $83,000 on October 22? | Crypto | YES | `26.5%` | `14.4%` | `+12.1 п.п.` | `0.40%` | REJECTED: Win probability 26.5% < 92% minimum (no underdog lottery bets) |
| Will Ethereum dip to $2,200 October 19-25? | Crypto | YES | `14.6%` | `5.9%` | `+8.7 п.п.` | `0.50%` | REJECTED: Win probability 14.6% < 92% minimum (no underdog lottery bets) |
| Will Bitcoin reach $86,000 October 19-25? | Crypto | YES | `22.8%` | `7.0%` | `+15.8 п.п.` | `1.26%` | REJECTED: Win probability 22.8% < 92% minimum (no underdog lottery bets) |
| Will Bitcoin reach $88,000 October 19-25? | Crypto | YES | `10.2%` | `2.6%` | `+7.6 п.п.` | `0.10%` | REJECTED: Win probability 10.2% < 92% minimum (no underdog lottery bets) |
| Will Bitcoin dip to $76,000 October 19-25? | Crypto | YES | `14.8%` | `4.3%` | `+10.4 п.п.` | `0.58%` | REJECTED: Win probability 14.8% < 92% minimum (no underdog lottery bets) |
| Will Kylian Mbappé win the 2026 Ballon d'Or? | Other | YES | `14.4%` | `5.5%` | `+8.9 п.п.` | `0.30%` | REJECTED: Win probability 14.4% < 92% minimum (no underdog lottery bets) |
| US x Iran ceasefire continues through October 24? | Geopolitics | NO | `18.3%` | `13.0%` | `+5.3 п.п.` | `1.00%` | REJECTED: Win probability 18.3% < 92% minimum (no underdog lottery bets) |
