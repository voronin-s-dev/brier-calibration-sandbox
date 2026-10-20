# 📊 Отчёт симулятора Polymarket (Устав Grok Bot — Демо-счёт)
**Обновлено:** `2026-10-20 18:27:52 UTC`

## 💰 Состояние виртуального портфеля
| Показатель | Значение | Правило устава |
| :--- | :--- | :--- |
| **Стартовый капитал** | `$50.00 USDC` | Не добавлять деньги |
| **Текущий баланс (Equity)** | **`$27.45 USDC`** (`-22.55$` / `-45.10%`) | Cash + Mark-to-Market по CLOB Bid |
| **Свободный кэш / В сделках** | `$16.64` / `$10.81 USDC` | До 8 открытых позиций, макс 8% банка |
| **Цель окупаемости подписки** | `$-22.55 / $60.00` (`0.0%`) | Цель: +$60.00 в месяц |
| **Просадка от пика (Текущая / Макс)** | `2.14%` / `2.14%` (Пик: `$28.05`) | Стоп-кран при просадке 40% |
| **Закрытых сделок / Win Rate** | `34` / `23.5%` | Brier Score: `0.4280` |

## 📂 Открытые позиции (4 / 8)
| # | Рынок | Кат. | Исход | Вход (Ask VWAP) | Текущий Bid | Оценка бота | Размер ($) | Нереализ. PnL | Источник |
| :- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| #35 | Will Bitcoin dip to $80,000 in October? | Crypto | **YES** | `0.610` | `0.540` | `99.5%` | `$1.11` | `$-0.13` | Kraken BTCUSDT 1m/1h Spot Klin |
| #36 | US x Iran ceasefire continues through October 22? | Geopolitics | **YES** | `0.953` | `0.952` | `98.0%` | `$3.30` | `$-0.00` | Official NFL data feed |
| #37 | Will Bitcoin dip to $81,000 on October 20? | Crypto | **NO** | `0.940` | `0.930` | `98.0%` | `$3.30` | `$-0.04` | https://www.binance.com/en/tra |
| #38 | Will the Bank of Russia decrease the key rate after the | Other | **NO** | `0.900` | `0.890` | `97.0%` | `$3.30` | `$-0.04` | https://www.cbr.ru/eng/dkp/cal |

## 🔍 Последние проверенные кандидаты и фильтр стакана CLOB
| Рынок | Кат. | Сторона | Оценка бота | Цена Ask | Перекос (Edge) | Проскальзывание CLOB | Решение |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Spread: Steelers (-3.5) | Sports | NO | `97.5%` | `52.0%` | `+45.5 п.п.` | `2.00%` | REJECTED: Contract price $0.520 outside sweet spot [$0.84, $0.96] |
| Counter-Strike: Nice Try vs aimclub (BO3) - Stake  | Sports | YES | `94.7%` | `90.0%` | `+4.7 п.п.` | `2.00%` | REJECTED: Max open positions (4) reached |
| LoL: Vitality Rising Bees vs G2 HEL - Game 2 Winne | Sports | NO | `1.5%` | `100.0%` | `-98.5 п.п.` | `100.00%` | REJECTED: Edge -98.5 pp < 2 pp threshold (P_est=1.5% vs AskVWAP=100.0%) |
| Will Elon Musk post <40 tweets from October 19 to  | Geopolitics | YES | `1.5%` | `100.0%` | `-98.5 п.п.` | `100.00%` | REJECTED: Edge -98.5 pp < 2 pp threshold (P_est=1.5% vs AskVWAP=100.0%) |
| Counter-Strike: Damajuana vs your end - Map 1 Winn | Sports | NO | `1.5%` | `100.0%` | `-98.5 п.п.` | `100.00%` | REJECTED: Edge -98.5 pp < 2 pp threshold (P_est=1.5% vs AskVWAP=100.0%) |
| Counter-Strike: Wingman vs Revise (BO3) - Exort Fi | Sports | NO | `1.5%` | `100.0%` | `-98.5 п.п.` | `100.00%` | REJECTED: Edge -98.5 pp < 2 pp threshold (P_est=1.5% vs AskVWAP=100.0%) |
| Counter-Strike: Luminosity vs Nexus (BO3) - Dracul | Sports | YES | `1.5%` | `100.0%` | `-98.5 п.п.` | `100.00%` | REJECTED: Edge -98.5 pp < 2 pp threshold (P_est=1.5% vs AskVWAP=100.0%) |
| Wild vs. Oilers | Sports | YES | `51.0%` | `46.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Win probability 51.0% < 92% minimum (no underdog lottery bets) |
| Counter-Strike: JiJieHao vs Iberian Soul (BO3) - D | Sports | NO | `1.5%` | `100.0%` | `-98.5 п.п.` | `100.00%` | REJECTED: Edge -98.5 pp < 2 pp threshold (P_est=1.5% vs AskVWAP=100.0%) |
| Will the price of Bitcoin be above $88,000 on Octo | Crypto | YES | `6.6%` | `2.3%` | `+4.3 п.п.` | `0.20%` | REJECTED: Win probability 6.6% < 92% minimum (no underdog lottery bets) |
| Will the price of Ethereum be above $2,300 on Octo | Crypto | NO | `8.6%` | `4.2%` | `+4.4 п.п.` | `0.26%` | REJECTED: Win probability 8.6% < 92% minimum (no underdog lottery bets) |
| Will the price of Bitcoin be above $86,000 on Octo | Crypto | YES | `10.8%` | `3.3%` | `+7.4 п.п.` | `0.10%` | REJECTED: Win probability 10.8% < 92% minimum (no underdog lottery bets) |
| Will the price of Bitcoin be above $80,000 on Octo | Crypto | NO | `17.6%` | `7.7%` | `+9.9 п.п.` | `1.71%` | REJECTED: Win probability 17.6% < 92% minimum (no underdog lottery bets) |
| Will the price of Ethereum be above $2,500 on Octo | Crypto | YES | `18.2%` | `10.0%` | `+8.2 п.п.` | `1.00%` | REJECTED: Win probability 18.2% < 92% minimum (no underdog lottery bets) |
| Will the Bank of Russia decrease the key rate afte | Other | NO | `97.0%` | `90.0%` | `+7.0 п.п.` | `1.00%` | EXECUTED BUY #38 ($3.30 @ 0.9000) |
| Will the price of Bitcoin be above $84,000 on Octo | Crypto | YES | `21.1%` | `12.0%` | `+9.1 п.п.` | `2.00%` | REJECTED: Win probability 21.1% < 92% minimum (no underdog lottery bets) |
| Will "Grand Theft Auto VI Launch Trailer" get betw | Other | NO | `90.1%` | `86.0%` | `+4.1 п.п.` | `1.00%` | REJECTED: Win probability 90.1% < 92% minimum (no underdog lottery bets) |
| Will Bitcoin dip to $81,000 on October 20? | Crypto | NO | `98.0%` | `94.0%` | `+4.0 п.п.` | `1.00%` | EXECUTED BUY #37 ($3.30 @ 0.9400) |
