# 📊 Отчёт симулятора Polymarket (Устав Grok Bot — Демо-счёт)
**Обновлено:** `2026-10-16 00:59:03 UTC`

## 💰 Состояние виртуального портфеля
| Показатель | Значение | Правило устава |
| :--- | :--- | :--- |
| **Стартовый капитал** | `$50.00 USDC` | Не добавлять деньги |
| **Текущий баланс (Equity)** | **`$35.62 USDC`** (`-14.38$` / `-28.75%`) | Cash + Mark-to-Market по CLOB Bid |
| **Свободный кэш / В сделках** | `$32.65` / `$2.97 USDC` | До 8 открытых позиций, макс 8% банка |
| **Цель окупаемости подписки** | `$-14.38 / $60.00` (`0.0%`) | Цель: +$60.00 в месяц |
| **Просадка от пика (Текущая / Макс)** | `33.72%` / `33.74%` (Пик: `$53.75`) | Стоп-кран при просадке 40% |
| **Закрытых сделок / Win Rate** | `19` / `31.6%` | Brier Score: `0.3143` |

## 📂 Открытые позиции (3 / 8)
| # | Рынок | Кат. | Исход | Вход (Ask VWAP) | Текущий Bid | Оценка бота | Размер ($) | Нереализ. PnL | Источник |
| :- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| #20 | Will the highest temperature in Houston be between 78-7 | Weather | **NO** | `0.680` | `0.560` | `79.2%` | `$1.45` | `$-0.26` | Auto-Meteo Houston (US) |
| #21 | Will the price of Bitcoin be above $84,000 on October 1 | Crypto | **YES** | `0.138` | `0.096` | `26.3%` | `$1.30` | `$-0.40` | https://www.binance.com/en/tra |
| #22 | Will the price of Bitcoin be above $80,000 on October 1 | Crypto | **NO** | `0.080` | `0.070` | `13.0%` | `$1.00` | `$-0.12` | https://www.binance.com/en/tra |

## 🔍 Последние проверенные кандидаты и фильтр стакана CLOB
| Рынок | Кат. | Сторона | Оценка бота | Цена Ask | Перекос (Edge) | Проскальзывание CLOB | Решение |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
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
| Will the price of Bitcoin be above $80,000 on Octo | Crypto | NO | `10.0%` | `5.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Duplicate underlying event (crypto:bitcoin:october 16) |
| Will the price of Ethereum be above $2,300 on Octo | Crypto | NO | `13.0%` | `9.0%` | `+4.0 п.п.` | `3.00%` | REJECTED: Edge +4.0 pp < 5 pp threshold (P_est=13.0% vs AskVWAP=9.0%) |
| Will the price of Bitcoin be above $80,000 on Octo | Crypto | NO | `12.0%` | `7.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Edge +5.0 pp < 5 pp threshold (P_est=12.0% vs AskVWAP=7.0%) |
| Will the price of Bitcoin be above $82,000 on Octo | Crypto | NO | `36.0%` | `31.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Edge +5.0 pp < 5 pp threshold (P_est=36.0% vs AskVWAP=31.0%) |
| Will the price of Ethereum be above $2,400 on Octo | Crypto | NO | `17.0%` | `12.5%` | `+4.5 п.п.` | `1.50%` | REJECTED: Edge +4.5 pp < 5 pp threshold (P_est=17.0% vs AskVWAP=12.5%) |
| Ethereum Up or Down on October 16? | Crypto | YES | `71.0%` | `66.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Edge +5.0 pp < 5 pp threshold (P_est=71.0% vs AskVWAP=66.0%) |
| Will the price of Bitcoin be above $80,000 on Octo | Crypto | NO | `10.0%` | `5.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Duplicate underlying event (crypto:bitcoin:october 16) |
| Will the highest temperature in Wellington be 9°C  | Weather | YES | `19.9%` | `100.0%` | `-80.1 п.п.` | `100.00%` | REJECTED: Edge -80.1 pp < 5 pp threshold (P_est=19.9% vs AskVWAP=100.0%) |
