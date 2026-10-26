# 📊 Отчёт симулятора Polymarket (Устав Grok Bot — Демо-счёт)
**Обновлено:** `2026-10-26 10:47:07 UTC`

## 💰 Состояние виртуального портфеля
| Показатель | Значение | Правило устава |
| :--- | :--- | :--- |
| **Стартовый капитал** | `$50.00 USDC` | Не добавлять деньги |
| **Текущий баланс (Equity)** | **`$33.86 USDC`** (`-16.14$` / `-32.27%`) | Cash + Mark-to-Market по CLOB Bid |
| **Свободный кэш / В сделках** | `$6.97` / `$26.89 USDC` | До 8 открытых позиций, макс 8% банка |
| **Цель окупаемости подписки** | `$-16.14 / $60.00` (`0.0%`) | Цель: +$60.00 в месяц |
| **Просадка от пика (Текущая / Макс)** | `0.00%` / `6.31%` (Пик: `$33.86`) | Стоп-кран при просадке 40% |
| **Закрытых сделок / Win Rate** | `59` / `54.2%` | Brier Score: `0.1905` |

## 📂 Открытые позиции (6 / 8)
| # | Рынок | Кат. | Исход | Вход (Ask VWAP) | Текущий Bid | Оценка бота | Размер ($) | Нереализ. PnL | Источник |
| :- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| #51 | Will there be no change in Fed interest rates after the | Macro | **YES** | `0.940` | `0.950` | `96.5%` | `$3.67` | `$+0.04` | https://www.federalreserve.gov |
| #52 | Will the Fed increase interest rates by 25 bps after th | Macro | **NO** | `0.960` | `0.950` | `98.0%` | `$3.70` | `$-0.04` | https://www.federalreserve.gov |
| #59 | Israel x Iran ceasefire continues through October 27? | Geopolitics | **YES** | `0.940` | `0.957` | `98.0%` | `$4.69` | `$+0.08` | the totality of information av |
| #61 | Will the price of Bitcoin be above $78,000 on October 2 | Crypto | **YES** | `0.940` | `0.980` | `98.5%` | `$4.58` | `$+0.19` | https://www.binance.com/en/tra |
| #64 | Spread: Olympique Lyonnais (-1.5) | Sports | **NO** | `0.965` | `0.966` | `98.5%` | `$5.01` | `$+0.01` | https://www.ligue1.com/ |
| #66 | Pacers vs. Bucks: O/U 212.5 | Sports | **YES** | `0.960` | `0.940` | `98.5%` | `$5.06` | `$-0.11` | https://www.nba.com/ |

## 🔍 Последние проверенные кандидаты и фильтр стакана CLOB
| Рынок | Кат. | Сторона | Оценка бота | Цена Ask | Перекос (Edge) | Проскальзывание CLOB | Решение |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Dota 2: OG vs GamerLegion - Game 2 Winner | Sports | YES | `60.2%` | `55.0%` | `+5.2 п.п.` | `1.00%` | REJECTED: Win probability 60.2% < 92% minimum (no underdog lottery bets) |
| Counter-Strike: 9z vs TYLOO - Map 1 Winner | Sports | YES | `82.3%` | `74.0%` | `+8.3 п.п.` | `1.00%` | REJECTED: Win probability 82.3% < 92% minimum (no underdog lottery bets) |
| Will AS Roma win on 2026-10-27? | Sports | YES | `78.0%` | `73.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Win probability 78.0% < 92% minimum (no underdog lottery bets) |
| Mavericks vs. Heat | Sports | NO | `80.0%` | `75.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Win probability 80.0% < 92% minimum (no underdog lottery bets) |
| Pacers vs. Bucks | Sports | NO | `45.0%` | `40.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Win probability 45.0% < 92% minimum (no underdog lottery bets) |
| Grizzlies vs. Jazz | Sports | YES | `54.0%` | `49.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Win probability 54.0% < 92% minimum (no underdog lottery bets) |
| Spread: Eagles (-3.5) | Sports | NO | `97.5%` | `80.0%` | `+17.5 п.п.` | `1.00%` | REJECTED: Contract price $0.800 outside sweet spot [$0.84, $0.96] |
| LoL: LOS vs Team Secret Whales (BO3) - Worlds Grou | Sports | NO | `71.0%` | `66.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Win probability 71.0% < 92% minimum (no underdog lottery bets) |
| Spread: Cowboys (-4.5) | Sports | NO | `97.5%` | `52.0%` | `+45.5 п.п.` | `1.00%` | REJECTED: Contract price $0.520 outside sweet spot [$0.84, $0.96] |
| Counter-Strike: Vitality vs FUT Esports - Map 1 Wi | Sports | YES | `68.5%` | `63.0%` | `+5.5 п.п.` | `1.00%` | REJECTED: Win probability 68.5% < 92% minimum (no underdog lottery bets) |
| LoL: Karmine Corp vs Bilibili Gaming (BO1) - World | Sports | YES | `35.0%` | `30.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Win probability 35.0% < 92% minimum (no underdog lottery bets) |
| Map Handicap: AUR (-1.5) vs Nemiga (+1.5) | Sports | NO | `1.5%` | `100.0%` | `-98.5 п.п.` | `100.00%` | REJECTED: Edge -98.5 pp < 2 pp threshold (P_est=1.5% vs AskVWAP=100.0%) |
| Counter-Strike: Vitality vs FUT Esports (BO3) - PG | Sports | YES | `78.0%` | `73.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Win probability 78.0% < 92% minimum (no underdog lottery bets) |
| Counter-Strike: Nemiga vs Aurora Gaming - Map 2 Wi | Sports | YES | `1.5%` | `100.0%` | `-98.5 п.п.` | `100.00%` | REJECTED: Edge -98.5 pp < 2 pp threshold (P_est=1.5% vs AskVWAP=100.0%) |
| Counter-Strike: Spirit vs FURIA (BO3) - PGL Master | Sports | YES | `69.0%` | `64.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Win probability 69.0% < 92% minimum (no underdog lottery bets) |
| Timberwolves vs. Cavaliers | Sports | YES | `46.0%` | `41.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Win probability 46.0% < 92% minimum (no underdog lottery bets) |
| Counter-Strike: Nemiga vs Aurora Gaming (BO3) - PG | Sports | YES | `1.5%` | `100.0%` | `-98.5 п.п.` | `100.00%` | REJECTED: Edge -98.5 pp < 2 pp threshold (P_est=1.5% vs AskVWAP=100.0%) |
| Dota 2: OG vs GamerLegion - Game 1 Winner | Sports | NO | `1.5%` | `100.0%` | `-98.5 п.п.` | `100.00%` | REJECTED: Edge -98.5 pp < 2 pp threshold (P_est=1.5% vs AskVWAP=100.0%) |
