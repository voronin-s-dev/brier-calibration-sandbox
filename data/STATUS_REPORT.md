# 📊 Отчёт симулятора Polymarket (Устав Grok Bot — Демо-счёт)
**Обновлено:** `2026-10-23 17:15:20 UTC`

## 💰 Состояние виртуального портфеля
| Показатель | Значение | Правило устава |
| :--- | :--- | :--- |
| **Стартовый капитал** | `$50.00 USDC` | Не добавлять деньги |
| **Текущий баланс (Equity)** | **`$29.67 USDC`** (`-20.33$` / `-40.67%`) | Cash + Mark-to-Market по CLOB Bid |
| **Свободный кэш / В сделках** | `$18.24` / `$11.43 USDC` | До 8 открытых позиций, макс 8% банка |
| **Цель окупаемости подписки** | `$-20.33 / $60.00` (`0.0%`) | Цель: +$60.00 в месяц |
| **Просадка от пика (Текущая / Макс)** | `0.47%` / `6.31%` (Пик: `$29.81`) | Стоп-кран при просадке 40% |
| **Закрытых сделок / Win Rate** | `45` / `42.2%` | Brier Score: `0.2574` |

## 📂 Открытые позиции (4 / 8)
| # | Рынок | Кат. | Исход | Вход (Ask VWAP) | Текущий Bid | Оценка бота | Размер ($) | Нереализ. PnL | Источник |
| :- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| #35 | Will Bitcoin dip to $80,000 in October? | Crypto | **YES** | `0.610` | `0.630` | `99.5%` | `$1.11` | `$+0.04` | Kraken BTCUSDT 1m/1h Spot Klin |
| #45 | US x Iran ceasefire continues through October 24? | Geopolitics | **YES** | `0.920` | `0.870` | `93.0%` | `$3.41` | `$-0.19` | Official NFL data feed |
| #47 | Israel x Iran ceasefire continues through October 24? | Geopolitics | **YES** | `0.950` | `0.930` | `97.0%` | `$3.57` | `$-0.08` | the totality of information av |
| #49 | Will Bitcoin dip to $80,000 on October 23? | Crypto | **NO** | `0.960` | `0.960` | `98.5%` | `$3.56` | `$-0.00` | https://www.binance.com/en/tra |

## 🔍 Последние проверенные кандидаты и фильтр стакана CLOB
| Рынок | Кат. | Сторона | Оценка бота | Цена Ask | Перекос (Edge) | Проскальзывание CLOB | Решение |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| LoL: Hanwha Life Esports vs Top Esports (BO1) - Wo | Sports | YES | `82.0%` | `77.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Win probability 82.0% < 92% minimum (no underdog lottery bets) |
| Will Aleksandar Vučić – United Serbia win the most | Geopolitics | YES | `76.5%` | `72.0%` | `+4.5 п.п.` | `2.00%` | REJECTED: Win probability 76.5% < 92% minimum (no underdog lottery bets) |
| Will Harry Kane win the 2026 Ballon d'Or? | Other | YES | `86.2%` | `76.1%` | `+10.1 п.п.` | `0.30%` | REJECTED: Win probability 86.2% < 92% minimum (no underdog lottery bets) |
| Counter-Strike: JiJieHao vs Eternal Fire (BO3) - D | Sports | NO | `87.6%` | `83.0%` | `+4.7 п.п.` | `1.00%` | REJECTED: Win probability 87.6% < 92% minimum (no underdog lottery bets) |
| Knicks vs. Celtics | Sports | NO | `60.7%` | `56.0%` | `+4.7 п.п.` | `1.00%` | REJECTED: Win probability 60.7% < 92% minimum (no underdog lottery bets) |
| Dota 2: BetBoom Team vs Astra Invicta - Game 2 Win | Sports | YES | `1.5%` | `100.0%` | `-98.5 п.п.` | `100.00%` | REJECTED: Edge -98.5 pp < 2 pp threshold (P_est=1.5% vs AskVWAP=100.0%) |
| Exact Score: Chelsea FC 0 - 0 Tottenham Hotspur FC | Other | YES | `9.0%` | `4.2%` | `+4.8 п.п.` | `0.20%` | REJECTED: Win probability 9.0% < 92% minimum (no underdog lottery bets) |
| Will Ethereum dip to $2,200 October 19-25? | Crypto | YES | `6.9%` | `2.4%` | `+4.5 п.п.` | `0.40%` | REJECTED: Win probability 6.9% < 92% minimum (no underdog lottery bets) |
| Will Dejan Šoškić be the next Prime Minister of Se | Geopolitics | YES | `19.9%` | `14.8%` | `+5.1 п.п.` | `1.90%` | REJECTED: Win probability 19.9% < 92% minimum (no underdog lottery bets) |
| Will Ethereum dip to $2,300 October 19-25? | Crypto | YES | `31.1%` | `8.0%` | `+23.1 п.п.` | `2.00%` | REJECTED: Win probability 31.1% < 92% minimum (no underdog lottery bets) |
| Will Bitcoin reach $83,000 on October 23? | Crypto | NO | `98.0%` | `93.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Duplicate underlying event (crypto:bitcoin:october 23) |
| Israel x Iran ceasefire continues through October  | Geopolitics | NO | `18.0%` | `13.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Win probability 18.0% < 92% minimum (no underdog lottery bets) |
| Will Bitcoin dip to $78,000 October 19-25? | Crypto | YES | `22.8%` | `3.8%` | `+19.0 п.п.` | `0.74%` | REJECTED: Win probability 22.8% < 92% minimum (no underdog lottery bets) |
| Will Borussia Mönchengladbach win on 2026-10-23? | Sports | YES | `17.0%` | `12.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Win probability 17.0% < 92% minimum (no underdog lottery bets) |
| Will Bitcoin reach $86,000 October 19-25? | Crypto | YES | `17.5%` | `2.9%` | `+14.6 п.п.` | `0.27%` | REJECTED: Win probability 17.5% < 92% minimum (no underdog lottery bets) |
| Will Ilija Srdanović be the next prime minister of | Geopolitics | YES | `18.5%` | `14.0%` | `+4.5 п.п.` | `2.00%` | REJECTED: Win probability 18.5% < 92% minimum (no underdog lottery bets) |
| Will Iliana Iotova win the next Bulgarian presiden | Geopolitics | NO | `19.6%` | `13.0%` | `+6.6 п.п.` | `1.00%` | REJECTED: Win probability 19.6% < 92% minimum (no underdog lottery bets) |
| Will Kylian Mbappé win the 2026 Ballon d'Or? | Other | YES | `19.1%` | `7.6%` | `+11.5 п.п.` | `0.50%` | REJECTED: Win probability 19.1% < 92% minimum (no underdog lottery bets) |
