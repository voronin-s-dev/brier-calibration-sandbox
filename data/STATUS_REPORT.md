# 📊 Отчёт симулятора Polymarket (Устав Grok Bot — Демо-счёт)
**Обновлено:** `2026-10-26 10:28:05 UTC`

## 💰 Состояние виртуального портфеля
| Показатель | Значение | Правило устава |
| :--- | :--- | :--- |
| **Стартовый капитал** | `$50.00 USDC` | Не добавлять деньги |
| **Текущий баланс (Equity)** | **`$33.61 USDC`** (`-16.39$` / `-32.78%`) | Cash + Mark-to-Market по CLOB Bid |
| **Свободный кэш / В сделках** | `$1.69` / `$31.92 USDC` | До 8 открытых позиций, макс 8% банка |
| **Цель окупаемости подписки** | `$-16.39 / $60.00` (`0.0%`) | Цель: +$60.00 в месяц |
| **Просадка от пика (Текущая / Макс)** | `0.38%` / `6.31%` (Пик: `$33.74`) | Стоп-кран при просадке 40% |
| **Закрытых сделок / Win Rate** | `58` / `53.4%` | Brier Score: `0.1905` |

## 📂 Открытые позиции (7 / 8)
| # | Рынок | Кат. | Исход | Вход (Ask VWAP) | Текущий Bid | Оценка бота | Размер ($) | Нереализ. PnL | Источник |
| :- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| #51 | Will there be no change in Fed interest rates after the | Macro | **YES** | `0.940` | `0.951` | `96.5%` | `$3.67` | `$+0.04` | https://www.federalreserve.gov |
| #52 | Will the Fed increase interest rates by 25 bps after th | Macro | **NO** | `0.960` | `0.950` | `98.0%` | `$3.70` | `$-0.04` | https://www.federalreserve.gov |
| #59 | Israel x Iran ceasefire continues through October 27? | Geopolitics | **YES** | `0.940` | `0.958` | `98.0%` | `$4.69` | `$+0.09` | the totality of information av |
| #61 | Will the price of Bitcoin be above $78,000 on October 2 | Crypto | **YES** | `0.940` | `0.978` | `98.5%` | `$4.58` | `$+0.19` | https://www.binance.com/en/tra |
| #64 | Spread: Olympique Lyonnais (-1.5) | Sports | **NO** | `0.965` | `0.964` | `98.5%` | `$5.01` | `$-0.01` | https://www.ligue1.com/ |
| #65 | Counter-Strike: Nemiga vs Aurora Gaming (BO3) - PGL Mas | Sports | **NO** | `0.954` | `0.950` | `98.5%` | `$5.06` | `$-0.02` | https://hltv.org |
| #66 | Pacers vs. Bucks: O/U 212.5 | Sports | **YES** | `0.960` | `0.940` | `98.5%` | `$5.06` | `$-0.11` | https://www.nba.com/ |

## 🔍 Последние проверенные кандидаты и фильтр стакана CLOB
| Рынок | Кат. | Сторона | Оценка бота | Цена Ask | Перекос (Edge) | Проскальзывание CLOB | Решение |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Will AS Roma win on 2026-10-27? | Sports | YES | `78.0%` | `73.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Win probability 78.0% < 92% minimum (no underdog lottery bets) |
| Pacers vs. Bucks | Sports | NO | `45.0%` | `40.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Win probability 45.0% < 92% minimum (no underdog lottery bets) |
| Grizzlies vs. Jazz | Sports | YES | `54.0%` | `49.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Win probability 54.0% < 92% minimum (no underdog lottery bets) |
| Spread: Eagles (-3.5) | Sports | NO | `97.5%` | `80.0%` | `+17.5 п.п.` | `1.00%` | REJECTED: Contract price $0.800 outside sweet spot [$0.84, $0.96] |
| Map Handicap: MOUZ (-1.5) vs TheMongolz (+1.5) | Sports | NO | `1.5%` | `100.0%` | `-98.5 п.п.` | `100.00%` | REJECTED: Edge -98.5 pp < 2 pp threshold (P_est=1.5% vs AskVWAP=100.0%) |
| LoL: LOS vs Team Secret Whales (BO3) - Worlds Grou | Sports | NO | `71.0%` | `66.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Win probability 71.0% < 92% minimum (no underdog lottery bets) |
| Spread: Cowboys (-4.5) | Sports | NO | `97.5%` | `52.0%` | `+45.5 п.п.` | `1.00%` | REJECTED: Contract price $0.520 outside sweet spot [$0.84, $0.96] |
| LoL: Karmine Corp vs Bilibili Gaming (BO1) - World | Sports | YES | `35.0%` | `30.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Win probability 35.0% < 92% minimum (no underdog lottery bets) |
| Dota 2: OG vs GamerLegion (BO3) - PARI Universe Gr | Sports | NO | `27.9%` | `23.0%` | `+4.9 п.п.` | `1.00%` | REJECTED: Win probability 27.9% < 92% minimum (no underdog lottery bets) |
| Counter-Strike: Spirit vs FURIA (BO3) - PGL Master | Sports | YES | `69.0%` | `64.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Win probability 69.0% < 92% minimum (no underdog lottery bets) |
| Counter-Strike: TheMongolz vs MOUZ - Map 2 Winner | Sports | YES | `1.5%` | `100.0%` | `-98.5 п.п.` | `100.00%` | REJECTED: Edge -98.5 pp < 2 pp threshold (P_est=1.5% vs AskVWAP=100.0%) |
| Timberwolves vs. Cavaliers | Sports | YES | `46.0%` | `41.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Win probability 46.0% < 92% minimum (no underdog lottery bets) |
| Counter-Strike: TheMongolz vs MOUZ (BO3) - PGL Mas | Sports | YES | `1.5%` | `100.0%` | `-98.5 п.п.` | `100.00%` | REJECTED: Edge -98.5 pp < 2 pp threshold (P_est=1.5% vs AskVWAP=100.0%) |
| Dota 2: OG vs GamerLegion - Game 1 Winner | Sports | NO | `1.5%` | `100.0%` | `-98.5 п.п.` | `100.00%` | REJECTED: Edge -98.5 pp < 2 pp threshold (P_est=1.5% vs AskVWAP=100.0%) |
| Paris Saint-Germain FC vs. Olympique Lyonnais: O/U | Sports | YES | `20.5%` | `16.0%` | `+4.5 п.п.` | `2.00%` | REJECTED: Win probability 20.5% < 92% minimum (no underdog lottery bets) |
| Pacers vs. Bucks: O/U 212.5 | Sports | YES | `98.5%` | `96.0%` | `+2.5 п.п.` | `2.00%` | EXECUTED BUY #66 ($5.06 @ 0.9600) |
| Dota 2: Team Yandex vs Team Liquid (BO3) - PARI Un | Sports | NO | `21.9%` | `16.0%` | `+5.9 п.п.` | `1.00%` | REJECTED: Win probability 21.9% < 92% minimum (no underdog lottery bets) |
| Counter-Strike: Nemiga vs Aurora Gaming - Map 2 Wi | Sports | NO | `94.0%` | `87.0%` | `+7.0 п.п.` | `1.00%` | REJECTED: Duplicate underlying event (sports:counter-strike: nemiga vs aurora ga:nodate) |
