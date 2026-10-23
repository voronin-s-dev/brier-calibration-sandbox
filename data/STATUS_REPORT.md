# 📊 Отчёт симулятора Polymarket (Устав Grok Bot — Демо-счёт)
**Обновлено:** `2026-10-23 17:05:55 UTC`

## 💰 Состояние виртуального портфеля
| Показатель | Значение | Правило устава |
| :--- | :--- | :--- |
| **Стартовый капитал** | `$50.00 USDC` | Не добавлять деньги |
| **Текущий баланс (Equity)** | **`$29.59 USDC`** (`-20.41$` / `-40.82%`) | Cash + Mark-to-Market по CLOB Bid |
| **Свободный кэш / В сделках** | `$18.24` / `$11.35 USDC` | До 8 открытых позиций, макс 8% банка |
| **Цель окупаемости подписки** | `$-20.41 / $60.00` (`0.0%`) | Цель: +$60.00 в месяц |
| **Просадка от пика (Текущая / Макс)** | `0.72%` / `6.31%` (Пик: `$29.81`) | Стоп-кран при просадке 40% |
| **Закрытых сделок / Win Rate** | `45` / `42.2%` | Brier Score: `0.2574` |

## 📂 Открытые позиции (4 / 8)
| # | Рынок | Кат. | Исход | Вход (Ask VWAP) | Текущий Bid | Оценка бота | Размер ($) | Нереализ. PnL | Источник |
| :- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| #35 | Will Bitcoin dip to $80,000 in October? | Crypto | **YES** | `0.610` | `0.630` | `99.5%` | `$1.11` | `$+0.04` | Kraken BTCUSDT 1m/1h Spot Klin |
| #45 | US x Iran ceasefire continues through October 24? | Geopolitics | **YES** | `0.920` | `0.860` | `74.3%` | `$3.41` | `$-0.22` | Official NFL data feed |
| #47 | Israel x Iran ceasefire continues through October 24? | Geopolitics | **YES** | `0.950` | `0.930` | `98.0%` | `$3.57` | `$-0.08` | the totality of information av |
| #49 | Will Bitcoin dip to $80,000 on October 23? | Crypto | **NO** | `0.960` | `0.950` | `98.5%` | `$3.56` | `$-0.04` | https://www.binance.com/en/tra |

## 🔍 Последние проверенные кандидаты и фильтр стакана CLOB
| Рынок | Кат. | Сторона | Оценка бота | Цена Ask | Перекос (Edge) | Проскальзывание CLOB | Решение |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| LoL: Hanwha Life Esports vs Top Esports (BO1) - Wo | Sports | YES | `82.0%` | `77.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Win probability 82.0% < 92% minimum (no underdog lottery bets) |
| Will Aleksandar Vučić – United Serbia win the most | Geopolitics | YES | `76.5%` | `72.0%` | `+4.5 п.п.` | `2.00%` | REJECTED: Win probability 76.5% < 92% minimum (no underdog lottery bets) |
| Counter-Strike: JiJieHao vs Eternal Fire (BO3) - D | Sports | NO | `67.0%` | `63.0%` | `+4.0 п.п.` | `1.00%` | REJECTED: Win probability 67.0% < 92% minimum (no underdog lottery bets) |
| Will Harry Kane win the 2026 Ballon d'Or? | Other | YES | `86.3%` | `76.0%` | `+10.3 п.п.` | `0.30%` | REJECTED: Win probability 86.3% < 92% minimum (no underdog lottery bets) |
| Knicks vs. Celtics | Sports | NO | `60.7%` | `56.0%` | `+4.7 п.п.` | `1.00%` | REJECTED: Win probability 60.7% < 92% minimum (no underdog lottery bets) |
| Dota 2: BetBoom Team vs Astra Invicta - Game 2 Win | Sports | YES | `1.5%` | `100.0%` | `-98.5 п.п.` | `100.00%` | REJECTED: Edge -98.5 pp < 2 pp threshold (P_est=1.5% vs AskVWAP=100.0%) |
| Exact Score: Chelsea FC 0 - 0 Tottenham Hotspur FC | Other | YES | `8.9%` | `4.2%` | `+4.7 п.п.` | `0.20%` | REJECTED: Win probability 8.9% < 92% minimum (no underdog lottery bets) |
| Will Ethereum dip to $2,200 October 19-25? | Crypto | YES | `7.0%` | `2.8%` | `+4.2 п.п.` | `0.98%` | REJECTED: Win probability 7.0% < 92% minimum (no underdog lottery bets) |
| Will Dejan Šoškić be the next Prime Minister of Se | Geopolitics | YES | `19.5%` | `14.8%` | `+4.7 п.п.` | `1.90%` | REJECTED: Win probability 19.5% < 92% minimum (no underdog lottery bets) |
| Will Ethereum dip to $2,300 October 19-25? | Crypto | YES | `31.4%` | `9.0%` | `+22.4 п.п.` | `2.00%` | REJECTED: Win probability 31.4% < 92% minimum (no underdog lottery bets) |
| Israel x Iran ceasefire continues through October  | Geopolitics | NO | `19.5%` | `15.1%` | `+4.4 п.п.` | `2.12%` | REJECTED: Win probability 19.5% < 92% minimum (no underdog lottery bets) |
| Will Borussia Mönchengladbach win on 2026-10-23? | Sports | YES | `17.0%` | `12.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Win probability 17.0% < 92% minimum (no underdog lottery bets) |
| Will Bitcoin dip to $78,000 October 19-25? | Crypto | YES | `22.8%` | `3.4%` | `+19.4 п.п.` | `0.30%` | REJECTED: Win probability 22.8% < 92% minimum (no underdog lottery bets) |
| Will Bitcoin reach $86,000 October 19-25? | Crypto | YES | `17.5%` | `2.9%` | `+14.6 п.п.` | `0.31%` | REJECTED: Win probability 17.5% < 92% minimum (no underdog lottery bets) |
| Will Ilija Srdanović be the next prime minister of | Geopolitics | YES | `18.5%` | `14.0%` | `+4.5 п.п.` | `2.00%` | REJECTED: Win probability 18.5% < 92% minimum (no underdog lottery bets) |
| Will Iliana Iotova win the next Bulgarian presiden | Geopolitics | NO | `19.5%` | `13.0%` | `+6.5 п.п.` | `1.00%` | REJECTED: Win probability 19.5% < 92% minimum (no underdog lottery bets) |
| Will Kylian Mbappé win the 2026 Ballon d'Or? | Other | YES | `17.8%` | `7.6%` | `+10.2 п.п.` | `0.35%` | REJECTED: Win probability 17.8% < 92% minimum (no underdog lottery bets) |
| Will Aleksandar Vučić – United Serbia win the most | Geopolitics | YES | `80.7%` | `72.0%` | `+8.7 п.п.` | `2.00%` | REJECTED: Win probability 80.7% < 92% minimum (no underdog lottery bets) |
