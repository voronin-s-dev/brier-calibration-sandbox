# 📊 Отчёт симулятора Polymarket (Устав Grok Bot — Демо-счёт)
**Обновлено:** `2026-10-25 16:44:05 UTC`

## 💰 Состояние виртуального портфеля
| Показатель | Значение | Правило устава |
| :--- | :--- | :--- |
| **Стартовый капитал** | `$50.00 USDC` | Не добавлять деньги |
| **Текущий баланс (Equity)** | **`$31.38 USDC`** (`-18.62$` / `-37.25%`) | Cash + Mark-to-Market по CLOB Bid |
| **Свободный кэш / В сделках** | `$16.39` / `$14.99 USDC` | До 8 открытых позиций, макс 8% банка |
| **Цель окупаемости подписки** | `$-18.62 / $60.00` (`0.0%`) | Цель: +$60.00 в месяц |
| **Просадка от пика (Текущая / Макс)** | `0.00%` / `6.31%` (Пик: `$31.38`) | Стоп-кран при просадке 40% |
| **Закрытых сделок / Win Rate** | `51` / `47.1%` | Brier Score: `0.2418` |

## 📂 Открытые позиции (4 / 8)
| # | Рынок | Кат. | Исход | Вход (Ask VWAP) | Текущий Bid | Оценка бота | Размер ($) | Нереализ. PnL | Источник |
| :- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| #51 | Will there be no change in Fed interest rates after the | Macro | **YES** | `0.940` | `0.940` | `96.5%` | `$3.67` | `$+0.00` | https://www.federalreserve.gov |
| #52 | Will the Fed increase interest rates by 25 bps after th | Macro | **NO** | `0.960` | `0.940` | `98.0%` | `$3.70` | `$-0.08` | https://www.federalreserve.gov |
| #53 | Will Flávio Bolsonaro win the second round of the 2026  | Geopolitics | **NO** | `0.939` | `0.969` | `98.5%` | `$3.71` | `$+0.12` | the margin of victory between  |
| #55 | Will Bitcoin dip to $78,000 October 19-25? | Crypto | **NO** | `0.948` | `0.977` | `98.5%` | `$3.75` | `$+0.11` | https://www.binance.com/en/tra |

## 🔍 Последние проверенные кандидаты и фильтр стакана CLOB
| Рынок | Кат. | Сторона | Оценка бота | Цена Ask | Перекос (Edge) | Проскальзывание CLOB | Решение |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Exact Score: FC Barcelona 3 - 2 Real Madrid CF? | Other | NO | `98.5%` | `93.9%` | `+4.6 п.п.` | `0.20%` | REJECTED: Max open positions (4) reached |
| Will Bitcoin reach $83,000 on October 25? | Crypto | YES | `8.5%` | `2.9%` | `+5.5 п.п.` | `0.34%` | REJECTED: Win probability 8.5% < 92% minimum (no underdog lottery bets) |
| Will the price of Bitcoin be above $84,000 on Octo | Crypto | YES | `15.5%` | `10.0%` | `+5.5 п.п.` | `3.00%` | REJECTED: Win probability 15.5% < 92% minimum (no underdog lottery bets) |
| Will Bitcoin reach $82,000 on October 25? | Crypto | YES | `27.9%` | `14.0%` | `+13.9 п.п.` | `1.00%` | REJECTED: Win probability 27.9% < 92% minimum (no underdog lottery bets) |
| Will Luiz Inácio Lula da Silva win the second roun | Geopolitics | NO | `91.0%` | `86.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Win probability 91.0% < 92% minimum (no underdog lottery bets) |
| Will the price of Bitcoin be above $76,000 on Octo | Crypto | NO | `9.8%` | `5.4%` | `+4.4 п.п.` | `1.68%` | REJECTED: Win probability 9.8% < 92% minimum (no underdog lottery bets) |
| Spread: Chiefs (-14.5) | Sports | YES | `15.7%` | `11.0%` | `+4.7 п.п.` | `1.00%` | REJECTED: Win probability 15.7% < 92% minimum (no underdog lottery bets) |
| Will Iliana Iotova win the 2026 Bulgarian presiden | Geopolitics | NO | `98.5%` | `91.0%` | `+7.5 п.п.` | `36.00%` | REJECTED: CLOB round-trip slippage 36.00% > 2.0% limit |
| Will Bitcoin dip to $79,000 on October 25? | Crypto | YES | `26.6%` | `11.0%` | `+15.6 п.п.` | `1.00%` | REJECTED: Win probability 26.6% < 92% minimum (no underdog lottery bets) |
| Will Ilija Srdanović be the next prime minister of | Geopolitics | NO | `94.0%` | `89.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Max open positions (4) reached |
| Will the price of Bitcoin be above $78,000 on Octo | Crypto | NO | `23.3%` | `15.3%` | `+8.0 п.п.` | `0.60%` | REJECTED: Win probability 23.3% < 92% minimum (no underdog lottery bets) |
| Will Bitcoin reach $82,000 October 19-25? | Crypto | YES | `27.4%` | `13.0%` | `+14.3 п.п.` | `1.00%` | REJECTED: Win probability 27.4% < 92% minimum (no underdog lottery bets) |
| Will Luiz Inácio Lula da Silva win the second roun | Geopolitics | YES | `21.4%` | `16.0%` | `+5.4 п.п.` | `1.00%` | REJECTED: Win probability 21.4% < 92% minimum (no underdog lottery bets) |
| Will Lamine Yamal win the 2026 Ballon d'Or? | Other | YES | `17.3%` | `12.2%` | `+5.1 п.п.` | `0.62%` | REJECTED: Win probability 17.3% < 92% minimum (no underdog lottery bets) |
| Spread: FC Barcelona (-3.5) | Sports | NO | `97.5%` | `88.0%` | `+9.5 п.п.` | `1.00%` | REJECTED: Max open positions (4) reached |
| Will the price of Bitcoin be above $84,000 on Octo | Crypto | YES | `14.7%` | `10.0%` | `+4.7 п.п.` | `3.00%` | REJECTED: Win probability 14.7% < 92% minimum (no underdog lottery bets) |
| Will the price of Bitcoin be between $78,000 and $ | Crypto | YES | `32.2%` | `14.6%` | `+17.6 п.п.` | `3.10%` | REJECTED: Win probability 32.2% < 92% minimum (no underdog lottery bets) |
| Will the price of Bitcoin be above $76,000 on Octo | Crypto | NO | `11.8%` | `7.0%` | `+4.8 п.п.` | `2.30%` | REJECTED: Win probability 11.8% < 92% minimum (no underdog lottery bets) |
