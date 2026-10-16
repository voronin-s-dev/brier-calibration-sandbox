# 📊 Отчёт симулятора Polymarket (Устав Grok Bot — Демо-счёт)
**Обновлено:** `2026-10-16 06:03:02 UTC`

## 💰 Состояние виртуального портфеля
| Показатель | Значение | Правило устава |
| :--- | :--- | :--- |
| **Стартовый капитал** | `$50.00 USDC` | Не добавлять деньги |
| **Текущий баланс (Equity)** | **`$34.51 USDC`** (`-15.49$` / `-30.97%`) | Cash + Mark-to-Market по CLOB Bid |
| **Свободный кэш / В сделках** | `$32.89` / `$1.62 USDC` | До 8 открытых позиций, макс 8% банка |
| **Цель окупаемости подписки** | `$-15.49 / $60.00` (`0.0%`) | Цель: +$60.00 в месяц |
| **Просадка от пика (Текущая / Макс)** | `35.79%` / `35.79%` (Пик: `$53.75`) | Стоп-кран при просадке 40% |
| **Закрытых сделок / Win Rate** | `21` / `28.6%` | Brier Score: `0.3143` |

## 📂 Открытые позиции (2 / 8)
| # | Рынок | Кат. | Исход | Вход (Ask VWAP) | Текущий Bid | Оценка бота | Размер ($) | Нереализ. PnL | Источник |
| :- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| #22 | Will the price of Bitcoin be above $80,000 on October 1 | Crypto | **NO** | `0.080` | `0.060` | `12.5%` | `$1.00` | `$-0.25` | https://www.binance.com/en/tra |
| #23 | Will the price of Ethereum be above $2,300 on October 2 | Crypto | **NO** | `0.080` | `0.070` | `16.3%` | `$1.00` | `$-0.12` | https://www.binance.com/en/tra |

## 🔍 Последние проверенные кандидаты и фильтр стакана CLOB
| Рынок | Кат. | Сторона | Оценка бота | Цена Ask | Перекос (Edge) | Проскальзывание CLOB | Решение |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Wuhan Tennis Open: Elina Svitolina vs Sonay Kartal | Sports | YES | `57.0%` | `52.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Edge +5.0 pp < 5 pp threshold (P_est=57.0% vs AskVWAP=52.0%) |
| Will the highest temperature in Seoul (Incheon) be | Weather | NO | `81.5%` | `57.0%` | `+24.5 п.п.` | `3.00%` | REJECTED: CLOB round-trip slippage 3.00% > 2.5% limit |
| Will the price of Bitcoin be above $82,000 on Octo | Crypto | NO | `52.0%` | `47.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Duplicate underlying event (crypto:bitcoin:october 17) |
| Will the price of Bitcoin be above $80,000 on Octo | Crypto | NO | `14.0%` | `9.0%` | `+5.0 п.п.` | `1.05%` | REJECTED: Edge +5.0 pp < 5 pp threshold (P_est=14.0% vs AskVWAP=9.0%) |
| Will the price of Bitcoin be above $78,000 on Octo | Crypto | NO | `11.5%` | `5.0%` | `+6.5 п.п.` | `1.78%` | REJECTED: Calculated 0.25x Kelly bet $0.59 below $1.00 min or > cash $32.89 |
| Will the price of Ethereum be above $2,300 on Octo | Crypto | NO | `10.5%` | `6.0%` | `+4.5 п.п.` | `2.00%` | REJECTED: Edge +4.5 pp < 5 pp threshold (P_est=10.5% vs AskVWAP=6.0%) |
| Will the price of Ethereum be above $2,300 on Octo | Crypto | NO | `16.3%` | `8.0%` | `+8.3 п.п.` | `1.00%` | EXECUTED BUY #23 ($1.00 @ 0.0800) |
| Will the price of Bitcoin be above $80,000 on Octo | Crypto | NO | `28.5%` | `24.0%` | `+4.5 п.п.` | `2.00%` | REJECTED: Edge +4.5 pp < 5 pp threshold (P_est=28.5% vs AskVWAP=24.0%) |
| Will the price of Bitcoin be above $82,000 on Octo | Crypto | NO | `52.5%` | `48.0%` | `+4.5 п.п.` | `2.00%` | REJECTED: Edge +4.5 pp < 5 pp threshold (P_est=52.5% vs AskVWAP=48.0%) |
| Will the price of Bitcoin be above $84,000 on Octo | Crypto | YES | `33.5%` | `29.0%` | `+4.5 п.п.` | `2.00%` | REJECTED: Edge +4.5 pp < 5 pp threshold (P_est=33.5% vs AskVWAP=29.0%) |
| Wuhan Tennis Open: Elina Svitolina vs Sonay Kartal | Sports | YES | `31.0%` | `26.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Edge +5.0 pp < 5 pp threshold (P_est=31.0% vs AskVWAP=26.0%) |
| Will the highest temperature in Seoul (Incheon) be | Weather | NO | `81.5%` | `57.0%` | `+24.5 п.п.` | `3.00%` | REJECTED: CLOB round-trip slippage 3.00% > 2.5% limit |
| Will the price of Bitcoin be above $82,000 on Octo | Crypto | NO | `49.0%` | `44.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Edge +5.0 pp < 5 pp threshold (P_est=49.0% vs AskVWAP=44.0%) |
| Will the price of Bitcoin be above $80,000 on Octo | Crypto | NO | `13.0%` | `8.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Calculated 0.25x Kelly bet $0.47 below $1.00 min or > cash $33.08 |
| Will the price of Ethereum be above $2,300 on Octo | Crypto | NO | `10.0%` | `6.0%` | `+4.0 п.п.` | `3.00%` | REJECTED: Edge +4.0 pp < 5 pp threshold (P_est=10.0% vs AskVWAP=6.0%) |
| Will the price of Bitcoin be above $80,000 on Octo | Crypto | NO | `28.0%` | `24.0%` | `+4.0 п.п.` | `3.04%` | REJECTED: Edge +4.0 pp < 5 pp threshold (P_est=28.0% vs AskVWAP=24.0%) |
| Will the price of Bitcoin be above $84,000 on Octo | Crypto | YES | `34.5%` | `30.0%` | `+4.5 п.п.` | `2.00%` | REJECTED: Edge +4.5 pp < 5 pp threshold (P_est=34.5% vs AskVWAP=30.0%) |
| Wuhan Tennis Open: Elina Svitolina vs Sonay Kartal | Sports | NO | `60.0%` | `66.0%` | `-6.0 п.п.` | `1.00%` | REJECTED: Edge -6.0 pp < 5 pp threshold (P_est=60.0% vs AskVWAP=66.0%) |
