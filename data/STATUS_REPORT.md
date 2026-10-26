# 📊 Отчёт симулятора Polymarket (Устав Grok Bot — Демо-счёт)
**Обновлено:** `2026-10-26 04:35:55 UTC`

## 💰 Состояние виртуального портфеля
| Показатель | Значение | Правило устава |
| :--- | :--- | :--- |
| **Стартовый капитал** | `$50.00 USDC` | Не добавлять деньги |
| **Текущий баланс (Equity)** | **`$33.42 USDC`** (`-16.58$` / `-33.16%`) | Cash + Mark-to-Market по CLOB Bid |
| **Свободный кэш / В сделках** | `$8.72` / `$24.69 USDC` | До 8 открытых позиций, макс 8% банка |
| **Цель окупаемости подписки** | `$-16.58 / $60.00` (`0.0%`) | Цель: +$60.00 в месяц |
| **Просадка от пика (Текущая / Макс)** | `0.05%` / `6.31%` (Пик: `$33.43`) | Стоп-кран при просадке 40% |
| **Закрытых сделок / Win Rate** | `57` / `52.6%` | Brier Score: `0.1905` |

## 📂 Открытые позиции (6 / 8)
| # | Рынок | Кат. | Исход | Вход (Ask VWAP) | Текущий Bid | Оценка бота | Размер ($) | Нереализ. PnL | Источник |
| :- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| #51 | Will there be no change in Fed interest rates after the | Macro | **YES** | `0.940` | `0.940` | `96.5%` | `$3.67` | `$+0.00` | https://www.federalreserve.gov |
| #52 | Will the Fed increase interest rates by 25 bps after th | Macro | **NO** | `0.960` | `0.940` | `98.0%` | `$3.70` | `$-0.08` | https://www.federalreserve.gov |
| #59 | Israel x Iran ceasefire continues through October 27? | Geopolitics | **YES** | `0.940` | `0.954` | `98.0%` | `$4.69` | `$+0.07` | the totality of information av |
| #61 | Will the price of Bitcoin be above $78,000 on October 2 | Crypto | **YES** | `0.940` | `0.946` | `98.4%` | `$4.58` | `$+0.03` | https://www.binance.com/en/tra |
| #62 | Will Elon Musk post 115-139 tweets from October 24 to O | Geopolitics | **NO** | `0.929` | `0.976` | `96.9%` | `$2.89` | `$+0.15` | https://x.com/elonmusk |
| #64 | Spread: Olympique Lyonnais (-1.5) | Sports | **NO** | `0.965` | `0.962` | `98.5%` | `$5.01` | `$-0.02` | https://www.ligue1.com/ |

## 🔍 Последние проверенные кандидаты и фильтр стакана CLOB
| Рынок | Кат. | Сторона | Оценка бота | Цена Ask | Перекос (Edge) | Проскальзывание CLOB | Решение |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Will AC Milan win on 2026-10-28? | Sports | YES | `66.0%` | `61.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Win probability 66.0% < 92% minimum (no underdog lottery bets) |
| Cowboys vs. Eagles | Sports | YES | `73.0%` | `68.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Win probability 73.0% < 92% minimum (no underdog lottery bets) |
| Map Handicap: MOUZ (-1.5) vs TheMongolz (+1.5) | Sports | NO | `60.1%` | `54.0%` | `+6.1 п.п.` | `1.00%` | REJECTED: Win probability 60.1% < 92% minimum (no underdog lottery bets) |
| Counter-Strike: Spirit vs FURIA (BO3) - PGL Master | Sports | YES | `70.0%` | `65.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Win probability 70.0% < 92% minimum (no underdog lottery bets) |
| Counter-Strike: 9z vs TYLOO (BO3) - PGL Masters Bu | Sports | YES | `86.7%` | `76.0%` | `+10.7 п.п.` | `1.00%` | REJECTED: Win probability 86.7% < 92% minimum (no underdog lottery bets) |
| Hawks vs. Rockets | Sports | YES | `39.0%` | `34.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Win probability 39.0% < 92% minimum (no underdog lottery bets) |
| Counter-Strike: Ground Zero vs Off Chops - Map 1 W | Sports | YES | `1.5%` | `100.0%` | `-98.5 п.п.` | `100.00%` | REJECTED: Edge -98.5 pp < 2 pp threshold (P_est=1.5% vs AskVWAP=100.0%) |
| Pacers vs. Bucks | Sports | NO | `46.0%` | `41.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Win probability 46.0% < 92% minimum (no underdog lottery bets) |
| Counter-Strike: BetBoom Team vs Natus Vincere (BO3 | Sports | NO | `69.7%` | `64.0%` | `+5.7 п.п.` | `1.00%` | REJECTED: Win probability 69.7% < 92% minimum (no underdog lottery bets) |
| Map Handicap: G2 (-1.5) vs DENDELE CS (+1.5) | Sports | NO | `59.0%` | `55.0%` | `+4.0 п.п.` | `1.00%` | REJECTED: Win probability 59.0% < 92% minimum (no underdog lottery bets) |
| Will AS Roma win on 2026-10-27? | Sports | YES | `78.0%` | `73.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Win probability 78.0% < 92% minimum (no underdog lottery bets) |
| Warriors vs. Nuggets | Sports | YES | `33.0%` | `28.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Win probability 33.0% < 92% minimum (no underdog lottery bets) |
| Dota 2: OG vs GamerLegion (BO3) - PARI Universe Gr | Sports | NO | `48.2%` | `43.0%` | `+5.2 п.п.` | `1.00%` | REJECTED: Win probability 48.2% < 92% minimum (no underdog lottery bets) |
| Spread: Eagles (-3.5) | Sports | NO | `97.5%` | `80.0%` | `+17.5 п.п.` | `1.00%` | REJECTED: Contract price $0.800 outside sweet spot [$0.84, $0.96] |
| Counter-Strike: Vitality vs FUT Esports (BO3) - PG | Sports | YES | `80.0%` | `75.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Win probability 80.0% < 92% minimum (no underdog lottery bets) |
| LoL: Karmine Corp vs Bilibili Gaming (BO1) - World | Sports | YES | `38.4%` | `30.0%` | `+8.4 п.п.` | `1.00%` | REJECTED: Win probability 38.4% < 92% minimum (no underdog lottery bets) |
| Spread: Olympique Lyonnais (-1.5) | Sports | NO | `98.5%` | `96.5%` | `+2.0 п.п.` | `0.30%` | EXECUTED BUY #64 ($5.01 @ 0.9650) |
| Counter-Strike: Spirit vs FURIA (BO3) - PGL Master | Sports | YES | `70.0%` | `65.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Win probability 70.0% < 92% minimum (no underdog lottery bets) |
