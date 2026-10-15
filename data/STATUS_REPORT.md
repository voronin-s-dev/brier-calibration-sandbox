# 📊 Отчёт симулятора Polymarket (Устав Grok Bot — Демо-счёт)
**Обновлено:** `2026-10-15 15:10:10 UTC`

## 💰 Состояние виртуального портфеля
| Показатель | Значение | Правило устава |
| :--- | :--- | :--- |
| **Стартовый капитал** | `$50.00 USDC` | Не добавлять деньги |
| **Текущий баланс (Equity)** | **`$36.15 USDC`** (`-13.85$` / `-27.70%`) | Cash + Mark-to-Market по CLOB Bid |
| **Свободный кэш / В сделках** | `$31.89` / `$4.26 USDC` | До 8 открытых позиций, макс 8% банка |
| **Цель окупаемости подписки** | `$-13.85 / $60.00` (`0.0%`) | Цель: +$60.00 в месяц |
| **Просадка от пика (Текущая / Макс)** | `32.74%` / `32.74%` (Пик: `$53.75`) | Стоп-кран при просадке 40% |
| **Закрытых сделок / Win Rate** | `17` / `23.5%` | Brier Score: `0.3143` |

## 📂 Открытые позиции (3 / 8)
| # | Рынок | Кат. | Исход | Вход (Ask VWAP) | Текущий Bid | Оценка бота | Размер ($) | Нереализ. PnL | Источник |
| :- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| #18 | Will Bitcoin reach $84,000 on October 15? | Crypto | **NO** | `0.891` | `0.867` | `94.5%` | `$1.45` | `$-0.04` | https://www.binance.com/en/tra |
| #19 | Will the price of Ethereum be above $2,500 on October 1 | Crypto | **NO** | `0.904` | `0.901` | `95.8%` | `$1.45` | `$-0.00` | https://www.binance.com/en/tra |
| #20 | Will the highest temperature in Houston be between 78-7 | Weather | **NO** | `0.680` | `0.660` | `82.6%` | `$1.45` | `$-0.04` | Auto-Meteo Houston (US) |

## 🔍 Последние проверенные кандидаты и фильтр стакана CLOB
| Рынок | Кат. | Сторона | Оценка бота | Цена Ask | Перекос (Edge) | Проскальзывание CLOB | Решение |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Will the highest temperature in Wellington be 10°C | Weather | NO | `71.6%` | `62.0%` | `+9.6 п.п.` | `3.00%` | REJECTED: CLOB round-trip slippage 3.00% > 2.5% limit |
| Will the highest temperature in Houston be between | Weather | NO | `82.6%` | `68.0%` | `+14.6 п.п.` | `2.00%` | EXECUTED BUY #20 ($1.45 @ 0.6800) |
| Will the highest temperature in Wellington be 9°C  | Weather | YES | `15.7%` | `100.0%` | `-84.3 п.п.` | `100.00%` | REJECTED: Edge -84.3 pp < 5 pp threshold (P_est=15.7% vs AskVWAP=100.0%) |
| Will the price of Bitcoin be above $80,000 on Octo | Crypto | NO | `18.0%` | `13.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Edge +5.0 pp < 5 pp threshold (P_est=18.0% vs AskVWAP=13.0%) |
| Will Bitcoin reach $83,000 on October 15? | Crypto | YES | `45.5%` | `53.0%` | `-7.5 п.п.` | `2.00%` | REJECTED: Edge -7.5 pp < 5 pp threshold (P_est=45.5% vs AskVWAP=53.0%) |
| Will the price of Bitcoin be above $80,000 on Octo | Crypto | NO | `15.0%` | `10.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Edge +5.0 pp < 5 pp threshold (P_est=15.0% vs AskVWAP=10.0%) |
| Will the price of Ethereum be above $2,500 on Octo | Crypto | NO | `95.8%` | `90.4%` | `+5.4 п.п.` | `0.30%` | EXECUTED BUY #19 ($1.45 @ 0.9040) |
| Will the highest temperature in Wellington be 10°C | Weather | NO | `71.7%` | `62.0%` | `+9.7 п.п.` | `3.00%` | REJECTED: CLOB round-trip slippage 3.00% > 2.5% limit |
| Will Bitcoin reach $84,000 on October 15? | Crypto | NO | `94.5%` | `89.1%` | `+5.4 п.п.` | `0.50%` | EXECUTED BUY #18 ($1.45 @ 0.8910) |
| Will the highest temperature in Wellington be 9°C  | Weather | YES | `15.6%` | `100.0%` | `-84.4 п.п.` | `100.00%` | REJECTED: Edge -84.4 pp < 5 pp threshold (P_est=15.6% vs AskVWAP=100.0%) |
| Will the price of Bitcoin be above $80,000 on Octo | Crypto | NO | `22.0%` | `17.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Edge +5.0 pp < 5 pp threshold (P_est=22.0% vs AskVWAP=17.0%) |
| Will the price of Bitcoin be above $80,000 on Octo | Crypto | NO | `19.0%` | `14.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Edge +5.0 pp < 5 pp threshold (P_est=19.0% vs AskVWAP=14.0%) |
| Will Bitcoin dip to $79,000 on October 15? | Crypto | NO | `98.0%` | `94.0%` | `+4.0 п.п.` | `1.00%` | REJECTED: Edge +4.0 pp < 5 pp threshold (P_est=98.0% vs AskVWAP=94.0%) |
| Will the highest temperature in Wellington be 10°C | Weather | NO | `71.9%` | `62.0%` | `+9.9 п.п.` | `3.00%` | REJECTED: CLOB round-trip slippage 3.00% > 2.5% limit |
| Will the highest temperature in Wellington be 9°C  | Weather | YES | `15.6%` | `100.0%` | `-84.4 п.п.` | `100.00%` | REJECTED: Edge -84.4 pp < 5 pp threshold (P_est=15.6% vs AskVWAP=100.0%) |
| Will the price of Bitcoin be above $80,000 on Octo | Crypto | NO | `25.5%` | `21.0%` | `+4.5 п.п.` | `2.00%` | REJECTED: Edge +4.5 pp < 5 pp threshold (P_est=25.5% vs AskVWAP=21.0%) |
| Will the price of Ethereum be above $2,300 on Octo | Crypto | NO | `17.2%` | `12.9%` | `+4.2 п.п.` | `2.50%` | REJECTED: Edge +4.3 pp < 5 pp threshold (P_est=17.2% vs AskVWAP=12.9%) |
| Will Bitcoin reach $83,000 on October 15? | Crypto | NO | `74.5%` | `70.0%` | `+4.5 п.п.` | `2.00%` | REJECTED: Edge +4.5 pp < 5 pp threshold (P_est=74.5% vs AskVWAP=70.0%) |
