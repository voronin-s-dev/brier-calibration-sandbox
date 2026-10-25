# 📊 Отчёт симулятора Polymarket (Устав Grok Bot — Демо-счёт)
**Обновлено:** `2026-10-25 22:18:07 UTC`

## 💰 Состояние виртуального портфеля
| Показатель | Значение | Правило устава |
| :--- | :--- | :--- |
| **Стартовый капитал** | `$50.00 USDC` | Не добавлять деньги |
| **Текущий баланс (Equity)** | **`$31.10 USDC`** (`-18.90$` / `-37.79%`) | Cash + Mark-to-Market по CLOB Bid |
| **Свободный кэш / В сделках** | `$0.00` / `$31.10 USDC` | До 8 открытых позиций, макс 8% банка |
| **Цель окупаемости подписки** | `$-18.90 / $60.00` (`0.0%`) | Цель: +$60.00 в месяц |
| **Просадка от пика (Текущая / Макс)** | `2.43%` / `6.31%` (Пик: `$31.88`) | Стоп-кран при просадке 40% |
| **Закрытых сделок / Win Rate** | `53` / `49.1%` | Brier Score: `0.2418` |

## 📂 Открытые позиции (8 / 8)
| # | Рынок | Кат. | Исход | Вход (Ask VWAP) | Текущий Bid | Оценка бота | Размер ($) | Нереализ. PnL | Источник |
| :- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| #51 | Will there be no change in Fed interest rates after the | Macro | **YES** | `0.940` | `0.930` | `96.5%` | `$3.67` | `$-0.04` | https://www.federalreserve.gov |
| #52 | Will the Fed increase interest rates by 25 bps after th | Macro | **NO** | `0.960` | `0.930` | `98.0%` | `$3.70` | `$-0.12` | https://www.federalreserve.gov |
| #55 | Will Bitcoin dip to $78,000 October 19-25? | Crypto | **NO** | `0.948` | `0.984` | `98.5%` | `$3.75` | `$+0.14` | https://www.binance.com/en/tra |
| #58 | LoL: Gen.G vs LYON (BO3) - Worlds Group Stage | Sports | **YES** | `0.920` | `0.770` | `71.2%` | `$4.69` | `$-0.76` | https://gol.gg/esports/home |
| #59 | Israel x Iran ceasefire continues through October 27? | Geopolitics | **YES** | `0.940` | `0.900` | `94.0%` | `$4.69` | `$-0.20` | the totality of information av |
| #60 | Clippers vs. Thunder | Sports | **NO** | `0.910` | `0.900` | `94.0%` | `$4.08` | `$-0.04` | https://www.nba.com/ |
| #61 | Will the price of Bitcoin be above $78,000 on October 2 | Crypto | **YES** | `0.940` | `0.958` | `98.5%` | `$4.58` | `$+0.09` | https://www.binance.com/en/tra |
| #62 | Will Elon Musk post 115-139 tweets from October 24 to O | Geopolitics | **NO** | `0.929` | `0.924` | `96.0%` | `$2.89` | `$-0.02` | https://x.com/elonmusk |

## 🔍 Последние проверенные кандидаты и фильтр стакана CLOB
| Рынок | Кат. | Сторона | Оценка бота | Цена Ask | Перекос (Edge) | Проскальзывание CLOB | Решение |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Will Harry Kane win the 2026 Ballon d'Or? | Other | YES | `78.5%` | `73.1%` | `+5.5 п.п.` | `0.10%` | REJECTED: Win probability 78.5% < 92% minimum (no underdog lottery bets) |
| Grizzlies vs. Kings | Sports | YES | `65.0%` | `60.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Win probability 65.0% < 92% minimum (no underdog lottery bets) |
| LoL: Gen.G vs LYON - Game 1 Winner | Sports | YES | `1.5%` | `100.0%` | `-98.5 п.п.` | `100.00%` | REJECTED: Edge -98.5 pp < 2 pp threshold (P_est=1.5% vs AskVWAP=100.0%) |
| Will the price of Bitcoin be above $84,000 on Octo | Crypto | YES | `12.7%` | `8.2%` | `+4.6 п.п.` | `2.18%` | REJECTED: Win probability 12.7% < 92% minimum (no underdog lottery bets) |
| Will the price of Bitcoin be above $76,000 on Octo | Crypto | NO | `10.3%` | `4.9%` | `+5.4 п.п.` | `0.90%` | REJECTED: Win probability 10.3% < 92% minimum (no underdog lottery bets) |
| Will the price of Bitcoin be above $78,000 on Octo | Crypto | NO | `24.2%` | `13.9%` | `+10.3 п.п.` | `0.10%` | REJECTED: Win probability 24.2% < 92% minimum (no underdog lottery bets) |
| Will Flávio Bolsonaro win the second round of the  | Geopolitics | NO | `93.8%` | `98.9%` | `-5.1 п.п.` | `14.20%` | REJECTED: Edge -5.1 pp < 2 pp threshold (P_est=93.8% vs AskVWAP=98.9%) |
| Will Bitcoin dip to $79,000 on October 25? | Crypto | YES | `22.9%` | `10.0%` | `+12.8 п.п.` | `2.00%` | REJECTED: Win probability 22.9% < 92% minimum (no underdog lottery bets) |
| Will Bitcoin reach $82,000 October 19-25? | Crypto | NO | `97.7%` | `92.8%` | `+4.9 п.п.` | `0.60%` | REJECTED: Duplicate underlying event (crypto:bitcoin:october 19) |
| US x Iran ceasefire continues through October 28? | Geopolitics | YES | `90.0%` | `85.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Win probability 90.0% < 92% minimum (no underdog lottery bets) |
| Will Lamine Yamal win the 2026 Ballon d'Or? | Other | YES | `24.6%` | `11.9%` | `+12.7 п.п.` | `0.30%` | REJECTED: Win probability 24.6% < 92% minimum (no underdog lottery bets) |
| Grizzlies vs. Kings | Sports | YES | `65.0%` | `60.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Win probability 65.0% < 92% minimum (no underdog lottery bets) |
| Raptors vs. Timberwolves | Sports | YES | `55.2%` | `51.0%` | `+4.2 п.п.` | `1.00%` | REJECTED: Win probability 55.2% < 92% minimum (no underdog lottery bets) |
| Will Benjamin Netanyahu be the next Prime Minister | Geopolitics | NO | `84.4%` | `76.0%` | `+8.4 п.п.` | `1.00%` | REJECTED: Win probability 84.4% < 92% minimum (no underdog lottery bets) |
| Pistons vs. 76ers | Sports | NO | `50.0%` | `45.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Win probability 50.0% < 92% minimum (no underdog lottery bets) |
| LoL: Gen.G vs LYON - Game 1 Winner | Sports | YES | `1.5%` | `100.0%` | `-98.5 п.п.` | `100.00%` | REJECTED: Edge -98.5 pp < 2 pp threshold (P_est=1.5% vs AskVWAP=100.0%) |
| Will the price of Bitcoin be above $84,000 on Octo | Crypto | YES | `12.8%` | `7.0%` | `+5.8 п.п.` | `1.00%` | REJECTED: Win probability 12.8% < 92% minimum (no underdog lottery bets) |
| Will the price of Bitcoin be above $82,000 on Octo | Crypto | YES | `15.4%` | `10.0%` | `+5.4 п.п.` | `1.00%` | REJECTED: Win probability 15.4% < 92% minimum (no underdog lottery bets) |
