# 📊 Отчёт симулятора Polymarket (Устав Grok Bot — Демо-счёт)
**Обновлено:** `2026-10-23 20:18:31 UTC`

## 💰 Состояние виртуального портфеля
| Показатель | Значение | Правило устава |
| :--- | :--- | :--- |
| **Стартовый капитал** | `$50.00 USDC` | Не добавлять деньги |
| **Текущий баланс (Equity)** | **`$29.87 USDC`** (`-20.13$` / `-40.26%`) | Cash + Mark-to-Market по CLOB Bid |
| **Свободный кэш / В сделках** | `$18.24` / `$11.63 USDC` | До 8 открытых позиций, макс 8% банка |
| **Цель окупаемости подписки** | `$-20.13 / $60.00` (`0.0%`) | Цель: +$60.00 в месяц |
| **Просадка от пика (Текущая / Макс)** | `0.17%` / `6.31%` (Пик: `$29.92`) | Стоп-кран при просадке 40% |
| **Закрытых сделок / Win Rate** | `45` / `42.2%` | Brier Score: `0.2574` |

## 📂 Открытые позиции (4 / 8)
| # | Рынок | Кат. | Исход | Вход (Ask VWAP) | Текущий Bid | Оценка бота | Размер ($) | Нереализ. PnL | Источник |
| :- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| #35 | Will Bitcoin dip to $80,000 in October? | Crypto | **YES** | `0.610` | `0.690` | `99.5%` | `$1.11` | `$+0.15` | Kraken BTCUSDT 1m/1h Spot Klin |
| #45 | US x Iran ceasefire continues through October 24? | Geopolitics | **YES** | `0.920` | `0.900` | `93.5%` | `$3.41` | `$-0.07` | Official NFL data feed |
| #47 | Israel x Iran ceasefire continues through October 24? | Geopolitics | **YES** | `0.950` | `0.940` | `98.0%` | `$3.57` | `$-0.04` | the totality of information av |
| #49 | Will Bitcoin dip to $80,000 on October 23? | Crypto | **NO** | `0.960` | `0.946` | `98.5%` | `$3.56` | `$-0.05` | https://www.binance.com/en/tra |

## 🔍 Последние проверенные кандидаты и фильтр стакана CLOB
| Рынок | Кат. | Сторона | Оценка бота | Цена Ask | Перекос (Edge) | Проскальзывание CLOB | Решение |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Will Aleksandar Vučić – United Serbia win the most | Geopolitics | YES | `76.0%` | `71.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Win probability 76.0% < 92% minimum (no underdog lottery bets) |
| Counter-Strike: ex-RUSTEC vs Saint Sinners (BO3) - | Sports | NO | `1.5%` | `100.0%` | `-98.5 п.п.` | `100.00%` | REJECTED: Edge -98.5 pp < 2 pp threshold (P_est=1.5% vs AskVWAP=100.0%) |
| Spread: Timberwolves (-1.5) | Sports | NO | `60.5%` | `55.0%` | `+5.5 п.п.` | `1.00%` | REJECTED: Win probability 60.5% < 92% minimum (no underdog lottery bets) |
| Hawks vs. Hornets | Sports | NO | `48.4%` | `44.0%` | `+4.4 п.п.` | `1.00%` | REJECTED: Win probability 48.4% < 92% minimum (no underdog lottery bets) |
| Spread: Celtics (-2.5) | Sports | YES | `57.8%` | `52.0%` | `+5.8 п.п.` | `1.00%` | REJECTED: Win probability 57.8% < 92% minimum (no underdog lottery bets) |
| Spread: Hawks (-2.5) | Sports | NO | `54.9%` | `50.0%` | `+4.9 п.п.` | `1.00%` | REJECTED: Win probability 54.9% < 92% minimum (no underdog lottery bets) |
| Will Harry Kane win the 2026 Ballon d'Or? | Other | YES | `85.1%` | `76.4%` | `+8.7 п.п.` | `0.10%` | REJECTED: Win probability 85.1% < 92% minimum (no underdog lottery bets) |
| Timberwolves vs. Magic | Sports | NO | `62.3%` | `52.0%` | `+10.3 п.п.` | `1.00%` | REJECTED: Win probability 62.3% < 92% minimum (no underdog lottery bets) |
| Raptors vs. Wizards | Sports | NO | `31.3%` | `26.0%` | `+5.3 п.п.` | `1.00%` | REJECTED: Win probability 31.3% < 92% minimum (no underdog lottery bets) |
| LoL: Anyone's Legend vs Karmine Corp (BO1) - World | Sports | NO | `43.6%` | `39.0%` | `+4.6 п.п.` | `1.00%` | REJECTED: Win probability 43.6% < 92% minimum (no underdog lottery bets) |
| Knicks vs. Celtics | Sports | NO | `61.9%` | `57.0%` | `+4.9 п.п.` | `1.00%` | REJECTED: Win probability 61.9% < 92% minimum (no underdog lottery bets) |
| LoL: Bilibili Gaming vs Movistar KOI (BO1) - World | Sports | YES | `1.5%` | `100.0%` | `-98.5 п.п.` | `100.00%` | REJECTED: Edge -98.5 pp < 2 pp threshold (P_est=1.5% vs AskVWAP=100.0%) |
| Will Iliana Iotova win the 2026 Bulgarian presiden | Geopolitics | YES | `19.5%` | `15.0%` | `+4.5 п.п.` | `2.00%` | REJECTED: Win probability 19.5% < 92% minimum (no underdog lottery bets) |
| Will Dejan Šoškić be the next Prime Minister of Se | Geopolitics | YES | `17.2%` | `13.2%` | `+4.0 п.п.` | `1.70%` | REJECTED: Win probability 17.2% < 92% minimum (no underdog lottery bets) |
| Will the price of Bitcoin be above $82,000 on Octo | Crypto | YES | `29.5%` | `13.0%` | `+16.5 п.п.` | `1.00%` | REJECTED: Win probability 29.5% < 92% minimum (no underdog lottery bets) |
| Will Ethereum dip to $2,300 October 19-25? | Crypto | YES | `35.0%` | `12.0%` | `+23.1 п.п.` | `2.00%` | REJECTED: Win probability 35.0% < 92% minimum (no underdog lottery bets) |
| Will FC Barcelona vs. Real Madrid CF end in a draw | Sports | NO | `95.6%` | `85.0%` | `+10.6 п.п.` | `1.00%` | REJECTED: Max open positions (4) reached |
| Israel x Iran ceasefire continues through October  | Geopolitics | NO | `18.5%` | `14.0%` | `+4.5 п.п.` | `2.37%` | REJECTED: Win probability 18.5% < 92% minimum (no underdog lottery bets) |
