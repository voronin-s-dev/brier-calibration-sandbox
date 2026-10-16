# 📊 Отчёт симулятора Polymarket (Устав Grok Bot — Демо-счёт)
**Обновлено:** `2026-10-16 05:44:30 UTC`

## 💰 Состояние виртуального портфеля
| Показатель | Значение | Правило устава |
| :--- | :--- | :--- |
| **Стартовый капитал** | `$50.00 USDC` | Не добавлять деньги |
| **Текущий баланс (Equity)** | **`$34.83 USDC`** (`-15.17$` / `-30.34%`) | Cash + Mark-to-Market по CLOB Bid |
| **Свободный кэш / В сделках** | `$33.08` / `$1.75 USDC` | До 8 открытых позиций, макс 8% банка |
| **Цель окупаемости подписки** | `$-15.17 / $60.00` (`0.0%`) | Цель: +$60.00 в месяц |
| **Просадка от пика (Текущая / Макс)** | `35.20%` / `35.20%` (Пик: `$53.75`) | Стоп-кран при просадке 40% |
| **Закрытых сделок / Win Rate** | `20` / `30.0%` | Brier Score: `0.3143` |

## 📂 Открытые позиции (2 / 8)
| # | Рынок | Кат. | Исход | Вход (Ask VWAP) | Текущий Bid | Оценка бота | Размер ($) | Нереализ. PnL | Источник |
| :- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| #20 | Will the highest temperature in Houston be between 78-7 | Weather | **NO** | `0.680` | `0.470` | `74.2%` | `$1.45` | `$-0.45` | Auto-Meteo Houston (US) |
| #22 | Will the price of Bitcoin be above $80,000 on October 1 | Crypto | **NO** | `0.080` | `0.060` | `12.0%` | `$1.00` | `$-0.25` | https://www.binance.com/en/tra |

## 🔍 Последние проверенные кандидаты и фильтр стакана CLOB
| Рынок | Кат. | Сторона | Оценка бота | Цена Ask | Перекос (Edge) | Проскальзывание CLOB | Решение |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Wuhan Tennis Open: Elina Svitolina vs Sonay Kartal | Sports | NO | `60.0%` | `66.0%` | `-6.0 п.п.` | `1.00%` | REJECTED: Edge -6.0 pp < 5 pp threshold (P_est=60.0% vs AskVWAP=66.0%) |
| Will the highest temperature in Seoul (Incheon) be | Weather | NO | `81.3%` | `57.0%` | `+24.3 п.п.` | `3.00%` | REJECTED: CLOB round-trip slippage 3.00% > 2.5% limit |
| Will the price of Bitcoin be above $82,000 on Octo | Crypto | NO | `52.0%` | `47.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Duplicate underlying event (crypto:bitcoin:october 17) |
| Will the price of Bitcoin be above $80,000 on Octo | Crypto | NO | `14.0%` | `9.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Calculated 0.25x Kelly bet $0.48 below $1.00 min or > cash $33.08 |
| Will the price of Ethereum be above $2,300 on Octo | Crypto | NO | `10.0%` | `6.0%` | `+4.0 п.п.` | `3.00%` | REJECTED: Edge +4.0 pp < 5 pp threshold (P_est=10.0% vs AskVWAP=6.0%) |
| Will the price of Ethereum be above $2,300 on Octo | Crypto | NO | `16.2%` | `9.0%` | `+7.2 п.п.` | `3.00%` | REJECTED: CLOB round-trip slippage 3.00% > 2.5% limit |
| Will the price of Bitcoin be above $82,000 on Octo | Crypto | NO | `52.0%` | `48.0%` | `+4.0 п.п.` | `3.00%` | REJECTED: Edge +4.0 pp < 5 pp threshold (P_est=52.0% vs AskVWAP=48.0%) |
| Will the price of Bitcoin be above $84,000 on Octo | Crypto | YES | `33.5%` | `29.0%` | `+4.5 п.п.` | `2.00%` | REJECTED: Edge +4.5 pp < 5 pp threshold (P_est=33.5% vs AskVWAP=29.0%) |
| Will the price of Bitcoin be above $82,000 on Octo | Crypto | NO | `43.0%` | `38.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Edge +5.0 pp < 5 pp threshold (P_est=43.0% vs AskVWAP=38.0%) |
| Will the price of Bitcoin be above $80,000 on Octo | Crypto | NO | `11.0%` | `6.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Duplicate underlying event (crypto:bitcoin:october 16) |
| Will the price of Bitcoin be above $80,000 on Octo | Crypto | NO | `16.9%` | `8.0%` | `+8.9 п.п.` | `1.00%` | EXECUTED BUY #22 ($1.00 @ 0.0800) |
| Will the price of Bitcoin be above $82,000 on Octo | Crypto | NO | `42.0%` | `37.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Edge +5.0 pp < 5 pp threshold (P_est=42.0% vs AskVWAP=37.0%) |
| Will the price of Ethereum be above $2,400 on Octo | Crypto | NO | `22.5%` | `18.0%` | `+4.5 п.п.` | `2.00%` | REJECTED: Edge +4.5 pp < 5 pp threshold (P_est=22.5% vs AskVWAP=18.0%) |
| Ethereum Up or Down on October 16? | Crypto | YES | `55.0%` | `51.0%` | `+4.0 п.п.` | `3.00%` | REJECTED: Edge +4.0 pp < 5 pp threshold (P_est=55.0% vs AskVWAP=51.0%) |
| Will the price of Bitcoin be above $80,000 on Octo | Crypto | NO | `11.0%` | `6.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Duplicate underlying event (crypto:bitcoin:october 16) |
| Will the price of Bitcoin be above $80,000 on Octo | Crypto | NO | `13.0%` | `8.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Calculated 0.25x Kelly bet $0.49 below $1.00 min or > cash $32.20 |
| Will the price of Bitcoin be above $82,000 on Octo | Crypto | NO | `39.0%` | `34.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Edge +5.0 pp < 5 pp threshold (P_est=39.0% vs AskVWAP=34.0%) |
| Ethereum Up or Down on October 16? | Crypto | YES | `57.5%` | `53.0%` | `+4.5 п.п.` | `2.00%` | REJECTED: Edge +4.5 pp < 5 pp threshold (P_est=57.5% vs AskVWAP=53.0%) |
