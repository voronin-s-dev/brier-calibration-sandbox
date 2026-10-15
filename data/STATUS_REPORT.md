# 📊 Отчёт симулятора Polymarket (Устав Grok Bot — Демо-счёт)
**Обновлено:** `2026-10-15 19:20:56 UTC`

## 💰 Состояние виртуального портфеля
| Показатель | Значение | Правило устава |
| :--- | :--- | :--- |
| **Стартовый капитал** | `$50.00 USDC` | Не добавлять деньги |
| **Текущий баланс (Equity)** | **`$36.03 USDC`** (`-13.97$` / `-27.94%`) | Cash + Mark-to-Market по CLOB Bid |
| **Свободный кэш / В сделках** | `$30.59` / `$5.44 USDC` | До 8 открытых позиций, макс 8% банка |
| **Цель окупаемости подписки** | `$-13.97 / $60.00` (`0.0%`) | Цель: +$60.00 в месяц |
| **Просадка от пика (Текущая / Макс)** | `32.96%` / `33.31%` (Пик: `$53.75`) | Стоп-кран при просадке 40% |
| **Закрытых сделок / Win Rate** | `17` / `23.5%` | Brier Score: `0.3143` |

## 📂 Открытые позиции (4 / 8)
| # | Рынок | Кат. | Исход | Вход (Ask VWAP) | Текущий Bid | Оценка бота | Размер ($) | Нереализ. PnL | Источник |
| :- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| #18 | Will Bitcoin reach $84,000 on October 15? | Crypto | **NO** | `0.891` | `0.902` | `97.8%` | `$1.45` | `$+0.02` | https://www.binance.com/en/tra |
| #19 | Will the price of Ethereum be above $2,500 on October 1 | Crypto | **NO** | `0.904` | `0.797` | `86.1%` | `$1.45` | `$-0.17` | https://www.binance.com/en/tra |
| #20 | Will the highest temperature in Houston be between 78-7 | Weather | **NO** | `0.680` | `0.580` | `81.6%` | `$1.45` | `$-0.21` | Auto-Meteo Houston (US) |
| #21 | Will the price of Bitcoin be above $84,000 on October 1 | Crypto | **YES** | `0.138` | `0.155` | `26.3%` | `$1.30` | `$+0.16` | https://www.binance.com/en/tra |

## 🔍 Последние проверенные кандидаты и фильтр стакана CLOB
| Рынок | Кат. | Сторона | Оценка бота | Цена Ask | Перекос (Edge) | Проскальзывание CLOB | Решение |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Will the price of Ethereum be above $2,400 on Octo | Crypto | NO | `18.0%` | `13.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Edge +5.0 pp < 5 pp threshold (P_est=18.0% vs AskVWAP=13.0%) |
| Will the price of Bitcoin be above $80,000 on Octo | Crypto | NO | `13.0%` | `8.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Calculated 0.25x Kelly bet $0.49 below $1.00 min or > cash $30.59 |
| Will the price of Bitcoin be above $82,000 on Octo | Crypto | NO | `37.0%` | `32.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Edge +5.0 pp < 5 pp threshold (P_est=37.0% vs AskVWAP=32.0%) |
| Will the price of Bitcoin be above $80,000 on Octo | Crypto | NO | `10.5%` | `6.0%` | `+4.5 п.п.` | `2.00%` | REJECTED: Edge +4.5 pp < 5 pp threshold (P_est=10.5% vs AskVWAP=6.0%) |
| Will the price of Ethereum be above $2,400 on Octo | Crypto | NO | `21.0%` | `16.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Edge +5.0 pp < 5 pp threshold (P_est=21.0% vs AskVWAP=16.0%) |
| Will the price of Bitcoin be above $80,000 on Octo | Crypto | NO | `29.0%` | `24.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Calculated 0.25x Kelly bet $0.59 below $1.00 min or > cash $30.59 |
| Will the price of Bitcoin be above $80,000 on Octo | Crypto | NO | `14.0%` | `9.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Calculated 0.25x Kelly bet $0.49 below $1.00 min or > cash $30.59 |
| Will the price of Bitcoin be above $82,000 on Octo | Crypto | NO | `40.0%` | `35.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Duplicate underlying event (crypto:bitcoin:october 16) |
| Will the price of Bitcoin be above $80,000 on Octo | Crypto | NO | `12.0%` | `7.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Edge +5.0 pp < 5 pp threshold (P_est=12.0% vs AskVWAP=7.0%) |
| Will the price of Bitcoin be above $80,000 on Octo | Crypto | NO | `29.5%` | `25.0%` | `+4.5 п.п.` | `2.00%` | REJECTED: Edge +4.5 pp < 5 pp threshold (P_est=29.5% vs AskVWAP=25.0%) |
| Will the price of Bitcoin be above $80,000 on Octo | Crypto | NO | `14.5%` | `10.0%` | `+4.5 п.п.` | `2.00%` | REJECTED: Edge +4.5 pp < 5 pp threshold (P_est=14.5% vs AskVWAP=10.0%) |
| Will Ethereum dip to $2,300 October 12-18? | Crypto | YES | `14.6%` | `9.6%` | `+5.0 п.п.` | `1.62%` | REJECTED: Calculated 0.25x Kelly bet $0.50 below $1.00 min or > cash $30.59 |
| Will the price of Bitcoin be above $82,000 on Octo | Crypto | NO | `40.0%` | `35.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Duplicate underlying event (crypto:bitcoin:october 16) |
| Will the price of Bitcoin be above $80,000 on Octo | Crypto | NO | `11.5%` | `7.0%` | `+4.5 п.п.` | `2.00%` | REJECTED: Edge +4.5 pp < 5 pp threshold (P_est=11.5% vs AskVWAP=7.0%) |
| Will the price of Bitcoin be above $84,000 on Octo | Crypto | YES | `26.3%` | `13.8%` | `+12.5 п.п.` | `0.30%` | EXECUTED BUY #21 ($1.30 @ 0.1380) |
| Will the highest temperature in Wellington be 10°C | Weather | NO | `71.6%` | `62.0%` | `+9.6 п.п.` | `3.00%` | REJECTED: CLOB round-trip slippage 3.00% > 2.5% limit |
| Will the highest temperature in Houston be between | Weather | NO | `82.6%` | `68.0%` | `+14.6 п.п.` | `2.00%` | EXECUTED BUY #20 ($1.45 @ 0.6800) |
| Will the highest temperature in Wellington be 9°C  | Weather | YES | `15.7%` | `100.0%` | `-84.3 п.п.` | `100.00%` | REJECTED: Edge -84.3 pp < 5 pp threshold (P_est=15.7% vs AskVWAP=100.0%) |
