# 📊 Отчёт симулятора Polymarket (Устав Grok Bot — Демо-счёт)
**Обновлено:** `2026-10-24 16:31:01 UTC`

## 💰 Состояние виртуального портфеля
| Показатель | Значение | Правило устава |
| :--- | :--- | :--- |
| **Стартовый капитал** | `$50.00 USDC` | Не добавлять деньги |
| **Текущий баланс (Equity)** | **`$30.85 USDC`** (`-19.15$` / `-38.31%`) | Cash + Mark-to-Market по CLOB Bid |
| **Свободный кэш / В сделках** | `$16.25` / `$14.59 USDC` | До 8 открытых позиций, макс 8% банка |
| **Цель окупаемости подписки** | `$-19.15 / $60.00` (`0.0%`) | Цель: +$60.00 в месяц |
| **Просадка от пика (Текущая / Макс)** | `0.14%` / `6.31%` (Пик: `$30.89`) | Стоп-кран при просадке 40% |
| **Закрытых сделок / Win Rate** | `48` / `43.8%` | Brier Score: `0.2418` |

## 📂 Открытые позиции (4 / 8)
| # | Рынок | Кат. | Исход | Вход (Ask VWAP) | Текущий Bid | Оценка бота | Размер ($) | Нереализ. PnL | Источник |
| :- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| #45 | US x Iran ceasefire continues through October 24? | Geopolitics | **YES** | `0.920` | `0.969` | `98.0%` | `$3.41` | `$+0.18` | Official NFL data feed |
| #47 | Israel x Iran ceasefire continues through October 24? | Geopolitics | **YES** | `0.950` | `0.976` | `98.0%` | `$3.57` | `$+0.10` | the totality of information av |
| #51 | Will there be no change in Fed interest rates after the | Macro | **YES** | `0.940` | `0.940` | `96.5%` | `$3.67` | `$+0.00` | https://www.federalreserve.gov |
| #52 | Will the Fed increase interest rates by 25 bps after th | Macro | **NO** | `0.960` | `0.950` | `98.0%` | `$3.70` | `$-0.04` | https://www.federalreserve.gov |

## 🔍 Последние проверенные кандидаты и фильтр стакана CLOB
| Рынок | Кат. | Сторона | Оценка бота | Цена Ask | Перекос (Edge) | Проскальзывание CLOB | Решение |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| UFC 333: Abubakar Vagaev vs. Jacob Malkoun (Middle | Sports | NO | `1.5%` | `100.0%` | `-98.5 п.п.` | `100.00%` | REJECTED: Edge -98.5 pp < 2 pp threshold (P_est=1.5% vs AskVWAP=100.0%) |
| Counter-Strike: Legacy vs Nemiga (BO3) - PGL Maste | Sports | YES | `1.5%` | `100.0%` | `-98.5 п.п.` | `100.00%` | REJECTED: Edge -98.5 pp < 2 pp threshold (P_est=1.5% vs AskVWAP=100.0%) |
| Counter-Strike: Vitality vs 9z (BO3) - PGL Masters | Sports | NO | `1.5%` | `100.0%` | `-98.5 п.п.` | `100.00%` | REJECTED: Edge -98.5 pp < 2 pp threshold (P_est=1.5% vs AskVWAP=100.0%) |
| Will Lula win the most votes in the second round o | Geopolitics | NO | `17.7%` | `13.0%` | `+4.7 п.п.` | `2.00%` | REJECTED: Win probability 17.7% < 92% minimum (no underdog lottery bets) |
| Will the price of Bitcoin be above $82,000 on Octo | Crypto | YES | `11.9%` | `3.4%` | `+8.5 п.п.` | `0.50%` | REJECTED: Win probability 11.9% < 92% minimum (no underdog lottery bets) |
| Will the price of Bitcoin be above $82,000 on Octo | Crypto | YES | `20.0%` | `13.0%` | `+7.0 п.п.` | `2.00%` | REJECTED: Win probability 20.0% < 92% minimum (no underdog lottery bets) |
| Will Naftali Bennett be the next Prime Minister of | Geopolitics | YES | `25.7%` | `15.0%` | `+10.7 п.п.` | `1.00%` | REJECTED: Win probability 25.7% < 92% minimum (no underdog lottery bets) |
| Michigan State vs. UCLA | Sports | NO | `92.0%` | `87.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Max open positions (4) reached |
| Counter-Strike: INOX Division vs Brute (BO3) - CCT | Sports | YES | `98.5%` | `92.0%` | `+6.5 п.п.` | `2.00%` | REJECTED: Max open positions (4) reached |
| Will Flavio Bolsonaro win the most votes in the se | Geopolitics | NO | `93.7%` | `88.0%` | `+5.7 п.п.` | `1.00%` | REJECTED: Category cap reached (2/2 in Geopolitics) |
| Will Bitcoin reach $82,000 October 19-25? | Crypto | YES | `33.3%` | `13.0%` | `+20.3 п.п.` | `2.00%` | REJECTED: Win probability 33.3% < 92% minimum (no underdog lottery bets) |
| Will Parma Calcio 1913 win on 2026-10-24? | Sports | YES | `17.0%` | `12.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Win probability 17.0% < 92% minimum (no underdog lottery bets) |
| Will the price of Bitcoin be above $78,000 on Octo | Crypto | YES | `94.1%` | `89.9%` | `+4.2 п.п.` | `0.10%` | REJECTED: Max open positions (4) reached |
| Will Аndrey Gyurov win the next Bulgarian presiden | Geopolitics | YES | `19.4%` | `13.0%` | `+6.4 п.п.` | `1.00%` | REJECTED: Win probability 19.4% < 92% minimum (no underdog lottery bets) |
| Will FC Barcelona vs. Real Madrid CF end in a draw | Sports | NO | `96.1%` | `85.0%` | `+11.1 п.п.` | `1.00%` | REJECTED: Max open positions (4) reached |
| Will Luiz Inácio Lula da Silva win the second roun | Geopolitics | YES | `21.1%` | `16.0%` | `+5.1 п.п.` | `1.00%` | REJECTED: Win probability 21.1% < 92% minimum (no underdog lottery bets) |
| US x Iran ceasefire continues through October 28? | Geopolitics | NO | `21.4%` | `15.0%` | `+6.4 п.п.` | `2.00%` | REJECTED: Win probability 21.4% < 92% minimum (no underdog lottery bets) |
| UFC 333: Colby Thicknesse vs. Asaf Chopurov (Banta | Sports | NO | `1.5%` | `100.0%` | `-98.5 п.п.` | `100.00%` | REJECTED: Edge -98.5 pp < 2 pp threshold (P_est=1.5% vs AskVWAP=100.0%) |
