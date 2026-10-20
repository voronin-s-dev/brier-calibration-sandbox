# 📊 Отчёт симулятора Polymarket (Устав Grok Bot — Демо-счёт)
**Обновлено:** `2026-10-20 20:36:13 UTC`

## 💰 Состояние виртуального портфеля
| Показатель | Значение | Правило устава |
| :--- | :--- | :--- |
| **Стартовый капитал** | `$50.00 USDC` | Не добавлять деньги |
| **Текущий баланс (Equity)** | **`$27.62 USDC`** (`-22.38$` / `-44.75%`) | Cash + Mark-to-Market по CLOB Bid |
| **Свободный кэш / В сделках** | `$16.64` / `$10.98 USDC` | До 8 открытых позиций, макс 8% банка |
| **Цель окупаемости подписки** | `$-22.38 / $60.00` (`0.0%`) | Цель: +$60.00 в месяц |
| **Просадка от пика (Текущая / Макс)** | `1.52%` / `2.15%` (Пик: `$28.05`) | Стоп-кран при просадке 40% |
| **Закрытых сделок / Win Rate** | `34` / `23.5%` | Brier Score: `0.4280` |

## 📂 Открытые позиции (4 / 8)
| # | Рынок | Кат. | Исход | Вход (Ask VWAP) | Текущий Bid | Оценка бота | Размер ($) | Нереализ. PnL | Источник |
| :- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| #35 | Will Bitcoin dip to $80,000 in October? | Crypto | **YES** | `0.610` | `0.530` | `99.5%` | `$1.11` | `$-0.15` | Kraken BTCUSDT 1m/1h Spot Klin |
| #36 | US x Iran ceasefire continues through October 22? | Geopolitics | **YES** | `0.953` | `0.946` | `98.0%` | `$3.30` | `$-0.02` | Official NFL data feed |
| #37 | Will Bitcoin dip to $81,000 on October 20? | Crypto | **NO** | `0.940` | `0.980` | `98.5%` | `$3.30` | `$+0.14` | https://www.binance.com/en/tra |
| #38 | Will the Bank of Russia decrease the key rate after the | Other | **NO** | `0.900` | `0.900` | `97.0%` | `$3.30` | `$+0.00` | https://www.cbr.ru/eng/dkp/cal |

## 🔍 Последние проверенные кандидаты и фильтр стакана CLOB
| Рынок | Кат. | Сторона | Оценка бота | Цена Ask | Перекос (Edge) | Проскальзывание CLOB | Решение |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Spread: Rams (-3.5) | Sports | NO | `97.5%` | `49.0%` | `+48.5 п.п.` | `1.00%` | REJECTED: Contract price $0.490 outside sweet spot [$0.84, $0.96] |
| Counter-Strike: K27 vs WW Team (BO3) - CIS LAN Cha | Sports | NO | `1.5%` | `100.0%` | `-98.5 п.п.` | `100.00%` | REJECTED: Edge -98.5 pp < 2 pp threshold (P_est=1.5% vs AskVWAP=100.0%) |
| Dota 2: TheBot$ vs Dawn Bulls - Game 2 Winner | Sports | YES | `1.5%` | `100.0%` | `-98.5 п.п.` | `100.00%` | REJECTED: Edge -98.5 pp < 2 pp threshold (P_est=1.5% vs AskVWAP=100.0%) |
| Spread: Steelers (-3.5) | Sports | NO | `97.5%` | `53.0%` | `+44.5 п.п.` | `1.00%` | REJECTED: Contract price $0.530 outside sweet spot [$0.84, $0.96] |
| Thunder vs. Spurs | Sports | NO | `53.8%` | `49.0%` | `+4.8 п.п.` | `1.00%` | REJECTED: Win probability 53.8% < 92% minimum (no underdog lottery bets) |
| Will FC Bayern München win on 2026-10-21? | Sports | YES | `53.0%` | `48.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Win probability 53.0% < 92% minimum (no underdog lottery bets) |
| 76ers vs. Knicks | Sports | NO | `66.7%` | `62.0%` | `+4.7 п.п.` | `1.00%` | REJECTED: Win probability 66.7% < 92% minimum (no underdog lottery bets) |
| Counter-Strike: fnatic vs PARIVISION (BO3) - 1win  | Sports | YES | `1.5%` | `100.0%` | `-98.5 п.п.` | `100.00%` | REJECTED: Edge -98.5 pp < 2 pp threshold (P_est=1.5% vs AskVWAP=100.0%) |
| Will the price of Ethereum be above $2,300 on Octo | Crypto | NO | `8.6%` | `4.0%` | `+4.6 п.п.` | `0.10%` | REJECTED: Win probability 8.6% < 92% minimum (no underdog lottery bets) |
| Will the price of Bitcoin be above $80,000 on Octo | Crypto | NO | `17.0%` | `6.0%` | `+10.9 п.п.` | `1.00%` | REJECTED: Win probability 17.0% < 92% minimum (no underdog lottery bets) |
| Will the price of Bitcoin be above $86,000 on Octo | Crypto | YES | `10.4%` | `3.5%` | `+7.0 п.п.` | `0.18%` | REJECTED: Win probability 10.4% < 92% minimum (no underdog lottery bets) |
| Will the price of Ethereum be above $2,500 on Octo | Crypto | YES | `16.2%` | `10.0%` | `+6.2 п.п.` | `1.00%` | REJECTED: Win probability 16.2% < 92% minimum (no underdog lottery bets) |
| US x Iran ceasefire continues through October 24? | Geopolitics | NO | `16.7%` | `12.0%` | `+4.7 п.п.` | `1.00%` | REJECTED: Win probability 16.7% < 92% minimum (no underdog lottery bets) |
| Will the price of Bitcoin be above $84,000 on Octo | Crypto | YES | `20.4%` | `12.0%` | `+8.4 п.п.` | `1.00%` | REJECTED: Win probability 20.4% < 92% minimum (no underdog lottery bets) |
| Will "Grand Theft Auto VI Launch Trailer" get betw | Other | NO | `17.6%` | `12.0%` | `+5.6 п.п.` | `1.67%` | REJECTED: Win probability 17.6% < 92% minimum (no underdog lottery bets) |
| Will "Grand Theft Auto VI Launch Trailer" get betw | Other | NO | `94.8%` | `90.0%` | `+4.8 п.п.` | `2.00%` | REJECTED: Max open positions (4) reached |
| Spread: Rams (-3.5) | Sports | NO | `97.5%` | `49.0%` | `+48.5 п.п.` | `1.00%` | REJECTED: Contract price $0.490 outside sweet spot [$0.84, $0.96] |
| Counter-Strike: Damajuana vs your end (BO3) - CCT  | Sports | YES | `1.5%` | `100.0%` | `-98.5 п.п.` | `100.00%` | REJECTED: Edge -98.5 pp < 2 pp threshold (P_est=1.5% vs AskVWAP=100.0%) |
