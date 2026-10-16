# 📊 Отчёт симулятора Polymarket (Устав Grok Bot — Демо-счёт)
**Обновлено:** `2026-10-16 16:36:57 UTC`

## 💰 Состояние виртуального портфеля
| Показатель | Значение | Правило устава |
| :--- | :--- | :--- |
| **Стартовый капитал** | `$50.00 USDC` | Не добавлять деньги |
| **Текущий баланс (Equity)** | **`$32.55 USDC`** (`-17.45$` / `-34.90%`) | Cash + Mark-to-Market по CLOB Bid |
| **Свободный кэш / В сделках** | `$31.24` / `$1.32 USDC` | До 8 открытых позиций, макс 8% банка |
| **Цель окупаемости подписки** | `$-17.45 / $60.00` (`0.0%`) | Цель: +$60.00 в месяц |
| **Просадка от пика (Текущая / Макс)** | `39.44%` / `39.57%` (Пик: `$53.75`) | Стоп-кран при просадке 40% |
| **Закрытых сделок / Win Rate** | `29` / `27.6%` | Brier Score: `0.3143` |

## 📂 Открытые позиции (1 / 8)
| # | Рынок | Кат. | Исход | Вход (Ask VWAP) | Текущий Bid | Оценка бота | Размер ($) | Нереализ. PnL | Источник |
| :- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| #26 | Will the highest temperature in Seoul (Incheon) be 25°C | Weather | **NO** | `0.570` | `0.560` | `81.9%` | `$1.34` | `$-0.02` | METAR RKSI (Seoul Incheon) |

## 🔍 Последние проверенные кандидаты и фильтр стакана CLOB
| Рынок | Кат. | Сторона | Оценка бота | Цена Ask | Перекос (Edge) | Проскальзывание CLOB | Решение |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Will Fulham FC win on 2026-10-17? | Sports | YES | `62.0%` | `57.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Edge +5.0 pp < 8 pp threshold (P_est=62.0% vs AskVWAP=57.0%) |
| Israel x Iran ceasefire continues through October  | Geopolitics | NO | `11.2%` | `7.0%` | `+4.2 п.п.` | `1.00%` | REJECTED: Edge +4.2 pp < 8 pp threshold (P_est=11.2% vs AskVWAP=7.0%) |
| Will the Fed increase interest rates by 25 bps aft | Macro | YES | `18.0%` | `13.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Edge +5.0 pp < 8 pp threshold (P_est=18.0% vs AskVWAP=13.0%) |
| Will the highest temperature in Seoul (Incheon) be | Weather | NO | `87.4%` | `55.0%` | `+32.4 п.п.` | `2.00%` | REJECTED: Duplicate underlying event (weather:seoul (incheon):october 17) |
| Will the price of Bitcoin be above $80,000 on Octo | Crypto | NO | `32.6%` | `24.0%` | `+8.6 п.п.` | `2.00%` | REJECTED: Win probability 32.6% < 55% minimum (no underdog lottery bets) |
| Will the highest temperature in Amsterdam be 14°C  | Weather | NO | `70.6%` | `49.0%` | `+21.6 п.п.` | `3.00%` | REJECTED: CLOB round-trip slippage 3.00% > 2.0% limit |
| Will the price of Bitcoin be above $82,000 on Octo | Crypto | YES | `37.7%` | `29.0%` | `+8.7 п.п.` | `2.00%` | REJECTED: Win probability 37.7% < 55% minimum (no underdog lottery bets) |
| Will Bitcoin dip to $80,000 October 12-18? | Crypto | YES | `53.5%` | `27.0%` | `+26.5 п.п.` | `4.00%` | REJECTED: Win probability 53.5% < 55% minimum (no underdog lottery bets) |
| Will the price of Bitcoin be above $80,000 on Octo | Crypto | NO | `29.6%` | `18.0%` | `+11.6 п.п.` | `1.00%` | REJECTED: Win probability 29.6% < 55% minimum (no underdog lottery bets) |
| Will Bitcoin reach $84,000 October 12-18? | Crypto | YES | `37.1%` | `8.0%` | `+29.1 п.п.` | `1.00%` | REJECTED: Win probability 37.1% < 55% minimum (no underdog lottery bets) |
| Will Bitcoin reach $88,000 October 12-18? | Crypto | YES | `6.1%` | `0.7%` | `+5.3 п.п.` | `0.24%` | REJECTED: Edge +5.4 pp < 8 pp threshold (P_est=6.1% vs AskVWAP=0.7%) |
| Will Ethereum reach $2,600 October 12-18? | Crypto | YES | `15.9%` | `2.2%` | `+13.7 п.п.` | `1.52%` | REJECTED: Win probability 15.9% < 55% minimum (no underdog lottery bets) |
| Will the price of Bitcoin be above $86,000 on Octo | Crypto | YES | `6.3%` | `0.8%` | `+5.5 п.п.` | `0.48%` | REJECTED: Edge +5.5 pp < 8 pp threshold (P_est=6.3% vs AskVWAP=0.8%) |
| Will the price of Bitcoin be above $88,000 on Octo | Crypto | YES | `9.4%` | `3.5%` | `+5.9 п.п.` | `1.90%` | REJECTED: Edge +5.9 pp < 8 pp threshold (P_est=9.4% vs AskVWAP=3.5%) |
| Will the price of Ethereum be above $2,400 on Octo | Crypto | NO | `24.7%` | `12.5%` | `+12.2 п.п.` | `1.70%` | REJECTED: Win probability 24.7% < 55% minimum (no underdog lottery bets) |
| Will Bitcoin reach $86,000 October 12-18? | Crypto | YES | `16.0%` | `1.2%` | `+14.8 п.п.` | `0.20%` | REJECTED: Win probability 16.0% < 55% minimum (no underdog lottery bets) |
| Will the price of Bitcoin be above $90,000 on Octo | Crypto | YES | `2.0%` | `100.0%` | `-98.0 п.п.` | `100.00%` | REJECTED: Edge -98.0 pp < 8 pp threshold (P_est=2.0% vs AskVWAP=100.0%) |
| Will the price of Bitcoin be above $80,000 on Octo | Crypto | NO | `34.9%` | `28.0%` | `+6.9 п.п.` | `3.00%` | REJECTED: Edge +6.9 pp < 8 pp threshold (P_est=34.9% vs AskVWAP=28.0%) |
