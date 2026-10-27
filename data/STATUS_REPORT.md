# 📊 Отчёт симулятора Polymarket (Устав Grok Bot — Демо-счёт)
**Обновлено:** `2026-10-27 12:37:06 UTC`

## 💰 Состояние виртуального портфеля
| Показатель | Значение | Правило устава |
| :--- | :--- | :--- |
| **Стартовый капитал** | `$50.00 USDC` | Не добавлять деньги |
| **Текущий баланс (Equity)** | **`$30.09 USDC`** (`-19.91$` / `-39.82%`) | Cash + Mark-to-Market по CLOB Bid |
| **Свободный кэш / В сделках** | `$9.91` / `$20.17 USDC` | До 8 открытых позиций, макс 8% банка |
| **Цель окупаемости подписки** | `$-19.91 / $60.00` (`0.0%`) | Цель: +$60.00 в месяц |
| **Просадка от пика (Текущая / Макс)** | `14.80%` / `14.94%` (Пик: `$35.32`) | Стоп-кран при просадке 40% |
| **Закрытых сделок / Win Rate** | `66` / `57.6%` | Brier Score: `0.2273` |

## 📂 Открытые позиции (5 / 8)
| # | Рынок | Кат. | Исход | Вход (Ask VWAP) | Текущий Bid | Оценка бота | Размер ($) | Нереализ. PnL | Источник |
| :- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| #51 | Will there be no change in Fed interest rates after the | Macro | **YES** | `0.940` | `0.933` | `96.5%` | `$3.67` | `$-0.03` | https://www.federalreserve.gov |
| #52 | Will the Fed increase interest rates by 25 bps after th | Macro | **NO** | `0.960` | `0.930` | `97.0%` | `$3.70` | `$-0.12` | https://www.federalreserve.gov |
| #70 | Kings vs. Spurs | Sports | **NO** | `0.930` | `0.920` | `96.0%` | `$4.54` | `$-0.05` | https://www.nba.com/ |
| #71 | Will Arsenal FC win on 2026-10-27? | Sports | **YES** | `0.900` | `0.890` | `95.0%` | `$4.53` | `$-0.05` | https://www.efl.com/ |
| #72 | Counter-Strike: FURIA vs TYLOO (BO3) - PGL Masters Buch | Sports | **YES** | `0.910` | `0.900` | `94.0%` | `$4.02` | `$-0.04` | https://hltv.org |

## 🔍 Последние проверенные кандидаты и фильтр стакана CLOB
| Рынок | Кат. | Сторона | Оценка бота | Цена Ask | Перекос (Edge) | Проскальзывание CLOB | Решение |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Counter-Strike: Prestige vs Bread Eaters Esports ( | Sports | NO | `1.5%` | `100.0%` | `-98.5 п.п.` | `100.00%` | REJECTED: Edge -98.5 pp < 2 pp threshold (P_est=1.5% vs AskVWAP=100.0%) |
| Counter-Strike: Luminosity vs HOTU (BO3) - Tesla C | Sports | NO | `50.0%` | `46.0%` | `+4.0 п.п.` | `1.00%` | REJECTED: Win probability 50.0% < 92% minimum (no underdog lottery bets) |
| Will SS Lazio win on 2026-10-27? | Sports | YES | `51.0%` | `46.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Win probability 51.0% < 92% minimum (no underdog lottery bets) |
| Map Handicap: ICE (-1.5) vs Team Nemesis (+1.5) | Sports | NO | `55.2%` | `49.0%` | `+6.2 п.п.` | `1.00%` | REJECTED: Win probability 55.2% < 92% minimum (no underdog lottery bets) |
| Dota 2: oveA vs Zero Tenacity - Game 2 Winner | Sports | YES | `1.5%` | `100.0%` | `-98.5 п.п.` | `100.00%` | REJECTED: Edge -98.5 pp < 2 pp threshold (P_est=1.5% vs AskVWAP=100.0%) |
| LoL: Top Esports vs Bilibili Gaming (BO3) - Worlds | Sports | NO | `81.0%` | `76.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Win probability 81.0% < 92% minimum (no underdog lottery bets) |
| Counter-Strike: Alliance vs FaZe - Map 2 Winner | Sports | YES | `1.5%` | `100.0%` | `-98.5 п.п.` | `100.00%` | REJECTED: Edge -98.5 pp < 2 pp threshold (P_est=1.5% vs AskVWAP=100.0%) |
| Counter-Strike: Alliance vs FaZe - Map 1 Winner | Sports | YES | `1.5%` | `100.0%` | `-98.5 п.п.` | `100.00%` | REJECTED: Edge -98.5 pp < 2 pp threshold (P_est=1.5% vs AskVWAP=100.0%) |
| Counter-Strike: Team Nemesis vs Brute (BO3) - NODW | Sports | YES | `1.5%` | `100.0%` | `-98.5 п.п.` | `100.00%` | REJECTED: Edge -98.5 pp < 2 pp threshold (P_est=1.5% vs AskVWAP=100.0%) |
| Spread: Knicks (-3.5) | Sports | NO | `97.5%` | `47.0%` | `+50.5 п.п.` | `1.00%` | REJECTED: Contract price $0.470 outside sweet spot [$0.84, $0.96] |
| Counter-Strike: Nemiga vs DENDELE CS - Map 2 Winne | Sports | NO | `1.5%` | `100.0%` | `-98.5 п.п.` | `100.00%` | REJECTED: Edge -98.5 pp < 2 pp threshold (P_est=1.5% vs AskVWAP=100.0%) |
| Counter-Strike: Spirit vs MOUZ (BO3) - PGL Masters | Sports | YES | `60.0%` | `55.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Win probability 60.0% < 92% minimum (no underdog lottery bets) |
| Counter-Strike: Inner Circle Esports vs Team Nemes | Sports | YES | `81.0%` | `76.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Win probability 81.0% < 92% minimum (no underdog lottery bets) |
| Counter-Strike: TheMongolz vs Legacy (BO3) - PGL M | Sports | YES | `49.0%` | `44.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Win probability 49.0% < 92% minimum (no underdog lottery bets) |
| Counter-Strike: magic vs BIG (BO3) - Stake Ranked  | Sports | YES | `58.9%` | `64.0%` | `-5.1 п.п.` | `2.00%` | REJECTED: Edge -5.1 pp < 2 pp threshold (P_est=58.9% vs AskVWAP=64.0%) |
| Counter-Strike: Alliance vs FaZe (BO3) - Tesla Cup | Sports | YES | `1.5%` | `100.0%` | `-98.5 п.п.` | `100.00%` | REJECTED: Edge -98.5 pp < 2 pp threshold (P_est=1.5% vs AskVWAP=100.0%) |
| Counter-Strike: Nemiga vs DENDELE CS (BO3) - PGL M | Sports | NO | `1.5%` | `100.0%` | `-98.5 п.п.` | `100.00%` | REJECTED: Edge -98.5 pp < 2 pp threshold (P_est=1.5% vs AskVWAP=100.0%) |
| Will Cagliari Calcio win on 2026-10-27? | Sports | YES | `14.0%` | `9.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Win probability 14.0% < 92% minimum (no underdog lottery bets) |
