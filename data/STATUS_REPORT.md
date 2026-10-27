# 📊 Отчёт симулятора Polymarket (Устав Grok Bot — Демо-счёт)
**Обновлено:** `2026-10-27 00:53:36 UTC`

## 💰 Состояние виртуального портфеля
| Показатель | Значение | Правило устава |
| :--- | :--- | :--- |
| **Стартовый капитал** | `$50.00 USDC` | Не добавлять деньги |
| **Текущий баланс (Equity)** | **`$35.26 USDC`** (`-14.74$` / `-29.49%`) | Cash + Mark-to-Market по CLOB Bid |
| **Свободный кэш / В сделках** | `$18.09` / `$17.17 USDC` | До 8 открытых позиций, макс 8% банка |
| **Цель окупаемости подписки** | `$-14.74 / $60.00` (`0.0%`) | Цель: +$60.00 в месяц |
| **Просадка от пика (Текущая / Макс)** | `0.00%` / `6.31%` (Пик: `$35.26`) | Стоп-кран при просадке 40% |
| **Закрытых сделок / Win Rate** | `64` / `57.8%` | Brier Score: `0.1778` |

## 📂 Открытые позиции (4 / 8)
| # | Рынок | Кат. | Исход | Вход (Ask VWAP) | Текущий Bid | Оценка бота | Размер ($) | Нереализ. PnL | Источник |
| :- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| #51 | Will there be no change in Fed interest rates after the | Macro | **YES** | `0.940` | `0.934` | `96.5%` | `$3.67` | `$-0.02` | https://www.federalreserve.gov |
| #52 | Will the Fed increase interest rates by 25 bps after th | Macro | **NO** | `0.960` | `0.930` | `98.0%` | `$3.70` | `$-0.12` | https://www.federalreserve.gov |
| #59 | Israel x Iran ceasefire continues through October 27? | Geopolitics | **YES** | `0.940` | `0.974` | `98.0%` | `$4.69` | `$+0.17` | the totality of information av |
| #66 | Pacers vs. Bucks: O/U 212.5 | Sports | **YES** | `0.960` | `0.964` | `98.5%` | `$5.06` | `$+0.02` | https://www.nba.com/ |

## 🔍 Последние проверенные кандидаты и фильтр стакана CLOB
| Рынок | Кат. | Сторона | Оценка бота | Цена Ask | Перекос (Edge) | Проскальзывание CLOB | Решение |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Will Liverpool FC win on 2026-10-28? | Sports | YES | `48.0%` | `43.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Win probability 48.0% < 92% minimum (no underdog lottery bets) |
| Counter-Strike: Spirit vs MOUZ (BO3) - PGL Masters | Sports | YES | `61.0%` | `56.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Win probability 61.0% < 92% minimum (no underdog lottery bets) |
| Counter-Strike: Astralis vs fnatic (BO3) - Stake R | Sports | NO | `49.2%` | `44.0%` | `+5.2 п.п.` | `1.00%` | REJECTED: Win probability 49.2% < 92% minimum (no underdog lottery bets) |
| Spread: Nuggets (-6.5) | Sports | YES | `60.0%` | `54.0%` | `+6.0 п.п.` | `1.00%` | REJECTED: Win probability 60.0% < 92% minimum (no underdog lottery bets) |
| Map Handicap: VIT (-1.5) vs Natus Vincere (+1.5) | Sports | NO | `62.4%` | `58.0%` | `+4.4 п.п.` | `1.94%` | REJECTED: Win probability 62.4% < 92% minimum (no underdog lottery bets) |
| Will FC Internazionale Milano win on 2026-10-28? | Sports | YES | `78.0%` | `73.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Win probability 78.0% < 92% minimum (no underdog lottery bets) |
| Spread: Packers (-4.5) | Sports | NO | `97.5%` | `54.0%` | `+43.5 п.п.` | `1.00%` | REJECTED: Contract price $0.540 outside sweet spot [$0.84, $0.96] |
| Map Handicap: ICE (-1.5) vs Team Nemesis (+1.5) | Sports | YES | `56.3%` | `52.0%` | `+4.3 п.п.` | `3.00%` | REJECTED: Win probability 56.3% < 92% minimum (no underdog lottery bets) |
| Counter-Strike: MIBR vs Eternal Fire (BO3) - Stake | Sports | YES | `69.1%` | `64.0%` | `+5.1 п.п.` | `1.00%` | REJECTED: Win probability 69.1% < 92% minimum (no underdog lottery bets) |
| Counter-Strike: TheMongolz vs Legacy (BO3) - PGL M | Sports | YES | `49.0%` | `44.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Win probability 49.0% < 92% minimum (no underdog lottery bets) |
| Spread: Nuggets (-8.5) | Sports | YES | `51.9%` | `46.0%` | `+5.9 п.п.` | `1.00%` | REJECTED: Win probability 51.9% < 92% minimum (no underdog lottery bets) |
| Will the Milwaukee Brewers win the 2026 World Seri | Sports | YES | `93.4%` | `84.7%` | `+8.7 п.п.` | `3.30%` | REJECTED: CLOB round-trip slippage 3.30% > 2.0% limit |
| Counter-Strike: Envy vs GamerLegion (BO3) - Tesla  | Sports | YES | `65.4%` | `60.0%` | `+5.4 п.п.` | `1.00%` | REJECTED: Win probability 65.4% < 92% minimum (no underdog lottery bets) |
| Counter-Strike: B8 vs K27 (BO3) - Tesla Cup Group  | Sports | YES | `70.9%` | `65.0%` | `+5.9 п.п.` | `1.00%` | REJECTED: Win probability 70.9% < 92% minimum (no underdog lottery bets) |
| Counter-Strike: Inner Circle Esports vs Team Nemes | Sports | YES | `80.2%` | `75.0%` | `+5.2 п.п.` | `2.00%` | REJECTED: Win probability 80.2% < 92% minimum (no underdog lottery bets) |
| Spread: Nuggets (-7.5) | Sports | YES | `55.3%` | `50.0%` | `+5.3 п.п.` | `1.00%` | REJECTED: Win probability 55.3% < 92% minimum (no underdog lottery bets) |
| Warriors vs. Nuggets | Sports | NO | `80.8%` | `72.0%` | `+8.8 п.п.` | `1.00%` | REJECTED: Win probability 80.8% < 92% minimum (no underdog lottery bets) |
| Counter-Strike: Spirit vs MOUZ (BO3) - PGL Masters | Sports | YES | `61.0%` | `56.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Win probability 61.0% < 92% minimum (no underdog lottery bets) |
