# 📊 Отчёт симулятора Polymarket (Устав Grok Bot — Демо-счёт)
**Обновлено:** `2026-10-26 17:14:35 UTC`

## 💰 Состояние виртуального портфеля
| Показатель | Значение | Правило устава |
| :--- | :--- | :--- |
| **Стартовый капитал** | `$50.00 USDC` | Не добавлять деньги |
| **Текущий баланс (Equity)** | **`$33.63 USDC`** (`-16.37$` / `-32.74%`) | Cash + Mark-to-Market по CLOB Bid |
| **Свободный кэш / В сделках** | `$7.35` / `$26.28 USDC` | До 8 открытых позиций, макс 8% банка |
| **Цель окупаемости подписки** | `$-16.37 / $60.00` (`0.0%`) | Цель: +$60.00 в месяц |
| **Просадка от пика (Текущая / Макс)** | `0.69%` / `6.31%` (Пик: `$33.86`) | Стоп-кран при просадке 40% |
| **Закрытых сделок / Win Rate** | `60` / `55.0%` | Brier Score: `0.1778` |

## 📂 Открытые позиции (6 / 8)
| # | Рынок | Кат. | Исход | Вход (Ask VWAP) | Текущий Bid | Оценка бота | Размер ($) | Нереализ. PnL | Источник |
| :- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| #51 | Will there be no change in Fed interest rates after the | Macro | **YES** | `0.940` | `0.914` | `96.5%` | `$3.67` | `$-0.10` | https://www.federalreserve.gov |
| #52 | Will the Fed increase interest rates by 25 bps after th | Macro | **NO** | `0.960` | `0.910` | `87.0%` | `$3.70` | `$-0.19` | https://www.federalreserve.gov |
| #59 | Israel x Iran ceasefire continues through October 27? | Geopolitics | **YES** | `0.940` | `0.968` | `98.0%` | `$4.69` | `$+0.14` | the totality of information av |
| #64 | Spread: Olympique Lyonnais (-1.5) | Sports | **NO** | `0.965` | `0.968` | `98.5%` | `$5.01` | `$+0.02` | https://www.ligue1.com/ |
| #66 | Pacers vs. Bucks: O/U 212.5 | Sports | **YES** | `0.960` | `0.930` | `98.0%` | `$5.06` | `$-0.16` | https://www.nba.com/ |
| #67 | Will CD Santa Clara win on 2026-10-26? | Sports | **NO** | `0.910` | `0.900` | `94.0%` | `$4.50` | `$-0.05` | https://www.ligaportugal.pt/ |

## 🔍 Последние проверенные кандидаты и фильтр стакана CLOB
| Рынок | Кат. | Сторона | Оценка бота | Цена Ask | Перекос (Edge) | Проскальзывание CLOB | Решение |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Spread: Eagles (-3.5) | Sports | NO | `97.5%` | `79.0%` | `+18.5 п.п.` | `1.00%` | REJECTED: Contract price $0.790 outside sweet spot [$0.84, $0.96] |
| Dota 2: No Hoodwink vs Zero Tenacity (BO3) - Espor | Sports | YES | `1.5%` | `100.0%` | `-98.5 п.п.` | `100.00%` | REJECTED: Edge -98.5 pp < 2 pp threshold (P_est=1.5% vs AskVWAP=100.0%) |
| Paris Saint-Germain FC vs. Olympique Lyonnais: O/U | Sports | YES | `55.0%` | `50.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Win probability 55.0% < 92% minimum (no underdog lottery bets) |
| Counter-Strike: Inner Circle Esports vs Team Nemes | Sports | YES | `70.0%` | `64.0%` | `+6.0 п.п.` | `1.77%` | REJECTED: Win probability 70.0% < 92% minimum (no underdog lottery bets) |
| Spread: Cavaliers (-3.5) | Sports | NO | `97.5%` | `44.0%` | `+53.5 п.п.` | `1.00%` | REJECTED: Contract price $0.440 outside sweet spot [$0.84, $0.96] |
| Dota 2: Team Spirit vs PARIVISION (BO3) - PARI Uni | Sports | NO | `78.6%` | `74.0%` | `+4.6 п.п.` | `1.00%` | REJECTED: Win probability 78.6% < 92% minimum (no underdog lottery bets) |
| Spread: Cavaliers (-4.5) | Sports | NO | `97.5%` | `47.0%` | `+50.5 п.п.` | `1.00%` | REJECTED: Contract price $0.470 outside sweet spot [$0.84, $0.96] |
| Map Handicap: TS (-1.5) vs FURIA (+1.5) | Sports | YES | `1.5%` | `100.0%` | `-98.5 п.п.` | `100.00%` | REJECTED: Edge -98.5 pp < 2 pp threshold (P_est=1.5% vs AskVWAP=100.0%) |
| LoL: Karmine Corp vs Bilibili Gaming (BO1) - World | Sports | YES | `35.0%` | `30.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Win probability 35.0% < 92% minimum (no underdog lottery bets) |
| Spread: Cowboys (-4.5) | Sports | NO | `97.5%` | `52.0%` | `+45.5 п.п.` | `1.00%` | REJECTED: Contract price $0.520 outside sweet spot [$0.84, $0.96] |
| Grizzlies vs. Jazz | Sports | YES | `53.0%` | `48.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Win probability 53.0% < 92% minimum (no underdog lottery bets) |
| Warriors vs. Nuggets | Sports | NO | `76.0%` | `71.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Win probability 76.0% < 92% minimum (no underdog lottery bets) |
| Spread: Rockets (-4.5) | Sports | NO | `97.5%` | `49.0%` | `+48.5 п.п.` | `1.00%` | REJECTED: Contract price $0.490 outside sweet spot [$0.84, $0.96] |
| Counter-Strike: BetBoom Team vs Natus Vincere (BO3 | Sports | YES | `44.4%` | `40.0%` | `+4.4 п.п.` | `1.00%` | REJECTED: Win probability 44.4% < 92% minimum (no underdog lottery bets) |
| Cowboys vs. Eagles | Sports | NO | `39.0%` | `34.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Win probability 39.0% < 92% minimum (no underdog lottery bets) |
| Counter-Strike: Spirit vs FURIA (BO3) - PGL Master | Sports | NO | `1.5%` | `100.0%` | `-98.5 п.п.` | `100.00%` | REJECTED: Edge -98.5 pp < 2 pp threshold (P_est=1.5% vs AskVWAP=100.0%) |
| Paris Saint-Germain FC vs. Olympique Lyonnais: O/U | Sports | YES | `24.4%` | `16.1%` | `+8.3 п.п.` | `1.07%` | REJECTED: Win probability 24.4% < 92% minimum (no underdog lottery bets) |
| Paris Saint-Germain FC vs. Olympique Lyonnais: O/U | Sports | YES | `95.0%` | `90.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Category cap reached (3/3 in Sports) |
