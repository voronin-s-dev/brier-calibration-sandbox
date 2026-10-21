# 📊 Отчёт симулятора Polymarket (Устав Grok Bot — Демо-счёт)
**Обновлено:** `2026-10-21 13:27:56 UTC`

## 💰 Состояние виртуального портфеля
| Показатель | Значение | Правило устава |
| :--- | :--- | :--- |
| **Стартовый капитал** | `$50.00 USDC` | Не добавлять деньги |
| **Текущий баланс (Equity)** | **`$27.35 USDC`** (`-22.65$` / `-45.29%`) | Cash + Mark-to-Market по CLOB Bid |
| **Свободный кэш / В сделках** | `$16.80` / `$10.55 USDC` | До 8 открытых позиций, макс 8% банка |
| **Цель окупаемости подписки** | `$-22.65 / $60.00` (`0.0%`) | Цель: +$60.00 в месяц |
| **Просадка от пика (Текущая / Макс)** | `2.48%` / `2.56%` (Пик: `$28.05`) | Стоп-кран при просадке 40% |
| **Закрытых сделок / Win Rate** | `35` / `25.7%` | Brier Score: `0.4280` |

## 📂 Открытые позиции (4 / 8)
| # | Рынок | Кат. | Исход | Вход (Ask VWAP) | Текущий Bid | Оценка бота | Размер ($) | Нереализ. PnL | Источник |
| :- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| #35 | Will Bitcoin dip to $80,000 in October? | Crypto | **YES** | `0.610` | `0.390` | `99.5%` | `$1.11` | `$-0.40` | Kraken BTCUSDT 1m/1h Spot Klin |
| #36 | US x Iran ceasefire continues through October 22? | Geopolitics | **YES** | `0.953` | `0.963` | `98.0%` | `$3.30` | `$+0.03` | Official NFL data feed |
| #38 | Will the Bank of Russia decrease the key rate after the | Other | **NO** | `0.900` | `0.890` | `97.0%` | `$3.30` | `$-0.04` | https://www.cbr.ru/eng/dkp/cal |
| #39 | Spread: Arsenal FC (-2.5) | Sports | **NO** | `0.964` | `0.948` | `98.4%` | `$3.30` | `$-0.05` | https://www.uefa.com/ |

## 🔍 Последние проверенные кандидаты и фильтр стакана CLOB
| Рынок | Кат. | Сторона | Оценка бота | Цена Ask | Перекос (Edge) | Проскальзывание CLOB | Решение |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Will the price of Bitcoin be above $80,000 on Octo | Crypto | NO | `11.0%` | `3.9%` | `+7.1 п.п.` | `0.42%` | REJECTED: Win probability 11.0% < 92% minimum (no underdog lottery bets) |
| Will NDP win the most seats in the 2026 British Co | Geopolitics | YES | `16.5%` | `12.0%` | `+4.5 п.п.` | `2.00%` | REJECTED: Win probability 16.5% < 92% minimum (no underdog lottery bets) |
| Will Elon Musk post 280-299 tweets from October 16 | Geopolitics | YES | `12.6%` | `7.0%` | `+5.6 п.п.` | `1.00%` | REJECTED: Win probability 12.6% < 92% minimum (no underdog lottery bets) |
| Will Bitcoin reach $92,000 October 19-25? | Crypto | YES | `8.6%` | `2.7%` | `+5.9 п.п.` | `0.50%` | REJECTED: Win probability 8.6% < 92% minimum (no underdog lottery bets) |
| Will Bitcoin dip to $76,000 October 19-25? | Crypto | YES | `8.3%` | `2.6%` | `+5.7 п.п.` | `0.10%` | REJECTED: Win probability 8.3% < 92% minimum (no underdog lottery bets) |
| Will Bitcoin dip to $82,000 on October 21? | Crypto | YES | `29.0%` | `13.0%` | `+16.1 п.п.` | `1.00%` | REJECTED: Win probability 29.0% < 92% minimum (no underdog lottery bets) |
| Will Аndrey Gyurov win the next Bulgarian presiden | Geopolitics | NO | `95.9%` | `91.0%` | `+4.9 п.п.` | `2.00%` | REJECTED: Max open positions (4) reached |
| Will Bitcoin reach $88,000 October 19-25? | Crypto | YES | `33.0%` | `15.0%` | `+18.0 п.п.` | `1.00%` | REJECTED: Win probability 33.0% < 92% minimum (no underdog lottery bets) |
| Will Elon Musk post 260-279 tweets from October 16 | Geopolitics | YES | `19.1%` | `15.0%` | `+4.1 п.п.` | `2.00%` | REJECTED: Win probability 19.1% < 92% minimum (no underdog lottery bets) |
| Will Bitcoin reach $90,000 October 19-25? | Crypto | YES | `17.5%` | `5.7%` | `+11.8 п.п.` | `0.37%` | REJECTED: Win probability 17.5% < 92% minimum (no underdog lottery bets) |
| US x Iran ceasefire continues through October 24? | Geopolitics | YES | `96.0%` | `91.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Duplicate underlying event (geopolitics:us x iran ceasefire continues through oc) |
| Will Bitcoin dip to $80,000 October 19-25? | Crypto | YES | `37.1%` | `15.0%` | `+22.1 п.п.` | `1.00%` | REJECTED: Win probability 37.1% < 92% minimum (no underdog lottery bets) |
| Will the price of Bitcoin be above $80,000 on Octo | Crypto | NO | `11.0%` | `4.0%` | `+7.0 п.п.` | `0.50%` | REJECTED: Win probability 11.0% < 92% minimum (no underdog lottery bets) |
| Will NDP win the most seats in the 2026 British Co | Geopolitics | YES | `16.5%` | `12.0%` | `+4.5 п.п.` | `2.00%` | REJECTED: Win probability 16.5% < 92% minimum (no underdog lottery bets) |
| Will Elon Musk post 280-299 tweets from October 16 | Geopolitics | YES | `12.5%` | `7.0%` | `+5.5 п.п.` | `1.00%` | REJECTED: Win probability 12.5% < 92% minimum (no underdog lottery bets) |
| Will Bitcoin reach $92,000 October 19-25? | Crypto | YES | `8.7%` | `3.0%` | `+5.7 п.п.` | `0.79%` | REJECTED: Win probability 8.7% < 92% minimum (no underdog lottery bets) |
| Will Conservative win the most seats in the 2026 B | Geopolitics | NO | `17.2%` | `12.0%` | `+5.2 п.п.` | `2.56%` | REJECTED: Win probability 17.2% < 92% minimum (no underdog lottery bets) |
| Ethereum Up or Down on October 21? | Crypto | YES | `95.5%` | `91.0%` | `+4.5 п.п.` | `1.00%` | REJECTED: Max open positions (4) reached |
