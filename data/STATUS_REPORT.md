# 📊 Отчёт симулятора Polymarket (Устав Grok Bot — Демо-счёт)
**Обновлено:** `2026-10-13 09:38:55 UTC`

## 💰 Состояние виртуального портфеля
| Показатель | Значение | Правило устава |
| :--- | :--- | :--- |
| **Стартовый капитал** | `$50.00 USDC` | Не добавлять деньги |
| **Текущий баланс (Equity)** | **`$51.03 USDC`** (`+1.03$` / `+2.06%`) | Cash + Mark-to-Market по CLOB Bid |
| **Свободный кэш / В сделках** | `$44.86` / `$6.17 USDC` | До 5 открытых позиций, макс 6% банка |
| **Цель окупаемости подписки** | `$+1.03 / $60.00` (`1.7%`) | Цель: +$60.00 в месяц |
| **Просадка от пика (Текущая / Макс)** | `0.07%` / `2.43%` (Пик: `$51.07`) | Стоп-кран при просадке 40% |
| **Закрытых сделок / Win Rate** | `5` / `20.0%` | Brier Score: `N/A (ожидание экспирации)` |

## 📂 Открытые позиции (3 / 5)
| # | Рынок | Кат. | Исход | Вход (Ask VWAP) | Текущий Bid | Оценка бота | Размер ($) | Нереализ. PnL | Источник |
| :- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| #4 | Will the highest temperature in Seoul (Incheon) be 21°C | Weather | **NO** | `0.380` | `0.396` | `65.0%` | `$2.99` | `$+0.13` | METAR RKSI (Seoul Incheon) |
| #7 | Will the price of Bitcoin be above $84,000 on October 1 | Crypto | **YES** | `0.110` | `0.109` | `21.5%` | `$1.51` | `$-0.01` | https://www.binance.com/en/tra |
| #8 | Will the price of Bitcoin be above $80,000 on October 1 | Crypto | **NO** | `0.067` | `0.066` | `18.2%` | `$1.58` | `$-0.02` | https://www.binance.com/en/tra |

## 🔍 Последние проверенные кандидаты и фильтр стакана CLOB
| Рынок | Кат. | Сторона | Оценка бота | Цена Ask | Перекос (Edge) | Проскальзывание CLOB | Решение |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Will the highest temperature in Wellington be 18°C | Weather | YES | `17.2%` | `100.0%` | `-82.8 п.п.` | `100.00%` | REJECTED: Edge -82.8 pp < 8 pp threshold (P_est=17.2% vs AskVWAP=100.0%) |
| Will the highest temperature in Beijing be 20°C on | Weather | YES | `13.2%` | `100.0%` | `-86.8 п.п.` | `100.00%` | REJECTED: Edge -86.8 pp < 8 pp threshold (P_est=13.2% vs AskVWAP=100.0%) |
| Will the highest temperature in Shanghai be 27°C o | Weather | NO | `58.9%` | `35.0%` | `+23.9 п.п.` | `8.41%` | REJECTED: CLOB round-trip slippage 8.41% > 3.0% limit |
| Will the highest temperature in Wellington be 17°C | Weather | YES | `16.5%` | `100.0%` | `-83.5 п.п.` | `100.00%` | REJECTED: Edge -83.5 pp < 8 pp threshold (P_est=16.5% vs AskVWAP=100.0%) |
| Will the price of Bitcoin be above $84,000 on Octo | Crypto | YES | `34.0%` | `29.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Edge +5.0 pp < 8 pp threshold (P_est=34.0% vs AskVWAP=29.0%) |
| Will the price of Bitcoin be above $80,000 on Octo | Crypto | NO | `18.2%` | `6.7%` | `+11.5 п.п.` | `0.10%` | EXECUTED BUY #8 ($1.58 @ 0.0670) |
| Will the price of Ethereum be above $2,400 on Octo | Crypto | YES | `83.5%` | `79.0%` | `+4.5 п.п.` | `2.00%` | REJECTED: Edge +4.5 pp < 8 pp threshold (P_est=83.5% vs AskVWAP=79.0%) |
| Will the price of Bitcoin be above $84,000 on Octo | Crypto | YES | `29.0%` | `24.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Edge +5.0 pp < 8 pp threshold (P_est=29.0% vs AskVWAP=24.0%) |
| Will the highest temperature in Seoul (Incheon) be | Weather | YES | `9.8%` | `100.0%` | `-90.2 п.п.` | `100.00%` | REJECTED: Edge -90.2 pp < 8 pp threshold (P_est=9.8% vs AskVWAP=100.0%) |
| Capitals vs. Hurricanes | Weather | YES | `45.0%` | `40.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Edge +5.0 pp < 8 pp threshold (P_est=45.0% vs AskVWAP=40.0%) |
| Will the price of Bitcoin be above $84,000 on Octo | Crypto | YES | `21.5%` | `11.0%` | `+10.5 п.п.` | `0.10%` | EXECUTED BUY #7 ($1.51 @ 0.1100) |
| Will the highest temperature in Sao Paulo be 26°C  | Weather | NO | `83.0%` | `79.0%` | `+4.0 п.п.` | `3.00%` | REJECTED: Edge +4.0 pp < 8 pp threshold (P_est=83.0% vs AskVWAP=79.0%) |
| Will Bitcoin reach $87,000 on October 12? | Crypto | YES | `2.0%` | `100.0%` | `-98.0 п.п.` | `100.00%` | REJECTED: Edge -98.0 pp < 8 pp threshold (P_est=2.0% vs AskVWAP=100.0%) |
| Will the highest temperature in Shanghai be 27°C o | Weather | NO | `64.3%` | `46.0%` | `+18.3 п.п.` | `2.00%` | REJECTED: Duplicate underlying event (weather:shanghai:october 13) |
| Will the highest temperature in Shanghai be 26°C o | Weather | NO | `74.5%` | `65.0%` | `+9.5 п.п.` | `3.00%` | EXECUTED BUY #6 ($2.95 @ 0.6500) |
| Will Ethereum reach $2,700 on October 12? | Crypto | YES | `2.0%` | `100.0%` | `-98.0 п.п.` | `100.00%` | REJECTED: Edge -98.0 pp < 8 pp threshold (P_est=2.0% vs AskVWAP=100.0%) |
| Bitcoin Up or Down on October 13? | Crypto | YES | `47.5%` | `43.0%` | `+4.5 п.п.` | `2.00%` | REJECTED: Edge +4.5 pp < 8 pp threshold (P_est=47.5% vs AskVWAP=43.0%) |
| Will Ethereum reach $2,750 on October 12? | Crypto | YES | `2.0%` | `100.0%` | `-98.0 п.п.` | `100.00%` | REJECTED: Edge -98.0 pp < 8 pp threshold (P_est=2.0% vs AskVWAP=100.0%) |
