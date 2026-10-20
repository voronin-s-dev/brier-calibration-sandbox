# 📊 Отчёт симулятора Polymarket (Устав Grok Bot — Демо-счёт)
**Обновлено:** `2026-10-20 23:20:02 UTC`

## 💰 Состояние виртуального портфеля
| Показатель | Значение | Правило устава |
| :--- | :--- | :--- |
| **Стартовый капитал** | `$50.00 USDC` | Не добавлять деньги |
| **Текущий баланс (Equity)** | **`$27.47 USDC`** (`-22.53$` / `-45.07%`) | Cash + Mark-to-Market по CLOB Bid |
| **Свободный кэш / В сделках** | `$16.64` / `$10.82 USDC` | До 8 открытых позиций, макс 8% банка |
| **Цель окупаемости подписки** | `$-22.53 / $60.00` (`0.0%`) | Цель: +$60.00 в месяц |
| **Просадка от пика (Текущая / Макс)** | `2.07%` / `2.15%` (Пик: `$28.05`) | Стоп-кран при просадке 40% |
| **Закрытых сделок / Win Rate** | `34` / `23.5%` | Brier Score: `0.4280` |

## 📂 Открытые позиции (4 / 8)
| # | Рынок | Кат. | Исход | Вход (Ask VWAP) | Текущий Bid | Оценка бота | Размер ($) | Нереализ. PnL | Источник |
| :- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| #35 | Will Bitcoin dip to $80,000 in October? | Crypto | **YES** | `0.610` | `0.480` | `99.5%` | `$1.11` | `$-0.24` | Kraken BTCUSDT 1m/1h Spot Klin |
| #36 | US x Iran ceasefire continues through October 22? | Geopolitics | **YES** | `0.953` | `0.947` | `98.0%` | `$3.30` | `$-0.02` | Official NFL data feed |
| #37 | Will Bitcoin dip to $81,000 on October 20? | Crypto | **NO** | `0.940` | `0.971` | `98.5%` | `$3.30` | `$+0.11` | https://www.binance.com/en/tra |
| #38 | Will the Bank of Russia decrease the key rate after the | Other | **NO** | `0.900` | `0.890` | `97.0%` | `$3.30` | `$-0.04` | https://www.cbr.ru/eng/dkp/cal |

## 🔍 Последние проверенные кандидаты и фильтр стакана CLOB
| Рынок | Кат. | Сторона | Оценка бота | Цена Ask | Перекос (Edge) | Проскальзывание CLOB | Решение |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Will Bitcoin reach $87,000 on October 20? | Crypto | YES | `1.5%` | `100.0%` | `-98.5 п.п.` | `100.00%` | REJECTED: Edge -98.5 pp < 2 pp threshold (P_est=1.5% vs AskVWAP=100.0%) |
| Spread: Lions (-3.5) | Sports | NO | `97.5%` | `53.0%` | `+44.5 п.п.` | `1.00%` | REJECTED: Contract price $0.530 outside sweet spot [$0.84, $0.96] |
| Spread: Rams (-3.5) | Sports | NO | `97.5%` | `49.0%` | `+48.5 п.п.` | `1.00%` | REJECTED: Contract price $0.490 outside sweet spot [$0.84, $0.96] |
| Will Bitcoin dip to $79,000 on October 20? | Crypto | YES | `1.5%` | `100.0%` | `-98.5 п.п.` | `100.00%` | REJECTED: Edge -98.5 pp < 2 pp threshold (P_est=1.5% vs AskVWAP=100.0%) |
| Spread: Steelers (-3.5) | Sports | NO | `97.5%` | `53.0%` | `+44.5 п.п.` | `1.00%` | REJECTED: Contract price $0.530 outside sweet spot [$0.84, $0.96] |
| Hawks vs. Magic | Sports | NO | `63.0%` | `58.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Win probability 63.0% < 92% minimum (no underdog lottery bets) |
| Counter-Strike: QUINTESSÊNCIA vs Los Niños (BO3) - | Sports | NO | `1.5%` | `100.0%` | `-98.5 п.п.` | `100.00%` | REJECTED: Edge -98.5 pp < 2 pp threshold (P_est=1.5% vs AskVWAP=100.0%) |
| Will FC Bayern München win on 2026-10-21? | Sports | YES | `56.7%` | `48.0%` | `+8.7 п.п.` | `1.00%` | REJECTED: Win probability 56.7% < 92% minimum (no underdog lottery bets) |
| Will David Eby be the next Premier of British Colu | Other | NO | `92.7%` | `85.0%` | `+7.7 п.п.` | `2.00%` | REJECTED: Max open positions (4) reached |
| Will the price of Ethereum be above $2,400 on Octo | Crypto | NO | `21.0%` | `12.0%` | `+9.0 п.п.` | `1.00%` | REJECTED: Win probability 21.0% < 92% minimum (no underdog lottery bets) |
| Will the price of Bitcoin be above $80,000 on Octo | Crypto | NO | `13.5%` | `4.0%` | `+9.5 п.п.` | `0.10%` | REJECTED: Win probability 13.5% < 92% minimum (no underdog lottery bets) |
| Will the price of Bitcoin be above $86,000 on Octo | Crypto | YES | `11.8%` | `3.9%` | `+7.9 п.п.` | `0.37%` | REJECTED: Win probability 11.8% < 92% minimum (no underdog lottery bets) |
| Will the price of Bitcoin be above $82,000 on Octo | Crypto | NO | `28.4%` | `16.0%` | `+12.4 п.п.` | `1.00%` | REJECTED: Win probability 28.4% < 92% minimum (no underdog lottery bets) |
| Will RB Leipzig win on 2026-10-21? | Sports | YES | `14.0%` | `9.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Win probability 14.0% < 92% minimum (no underdog lottery bets) |
| Will the price of Ethereum be above $2,500 on Octo | Crypto | YES | `18.9%` | `12.0%` | `+6.9 п.п.` | `1.00%` | REJECTED: Win probability 18.9% < 92% minimum (no underdog lottery bets) |
| US x Iran ceasefire continues through October 24? | Geopolitics | NO | `17.0%` | `12.0%` | `+5.0 п.п.` | `2.00%` | REJECTED: Win probability 17.0% < 92% minimum (no underdog lottery bets) |
| Will the price of Bitcoin be above $84,000 on Octo | Crypto | YES | `24.3%` | `16.0%` | `+8.3 п.п.` | `1.00%` | REJECTED: Win probability 24.3% < 92% minimum (no underdog lottery bets) |
| Will "Grand Theft Auto VI Launch Trailer" get betw | Other | NO | `20.7%` | `16.1%` | `+4.6 п.п.` | `1.80%` | REJECTED: Win probability 20.7% < 92% minimum (no underdog lottery bets) |
