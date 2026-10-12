# 📊 Отчёт симулятора Polymarket (Устав Grok Bot — Демо-счёт)
**Обновлено:** `2026-10-12 21:56:53 UTC`

## 💰 Состояние виртуального портфеля
| Показатель | Значение | Правило устава |
| :--- | :--- | :--- |
| **Стартовый капитал** | `$50.00 USDC` | Не добавлять деньги |
| **Текущий баланс (Equity)** | **`$49.10 USDC`** (`-0.90$` / `-1.80%`) | Cash + Mark-to-Market по CLOB Bid |
| **Свободный кэш / В сделках** | `$43.53` / `$5.57 USDC` | До 5 открытых позиций, макс 6% банка |
| **Цель окупаемости подписки** | `$-0.90 / $60.00` (`0.0%`) | Цель: +$60.00 в месяц |
| **Просадка от пика (Текущая / Макс)** | `1.80%` / `1.80%` (Пик: `$50.00`) | Стоп-кран при просадке 40% |
| **Закрытых сделок / Win Rate** | `4` / `0.0%` | Brier Score: `N/A (ожидание экспирации)` |

## 📂 Открытые позиции (2 / 5)
| # | Рынок | Кат. | Исход | Вход (Ask VWAP) | Текущий Bid | Оценка бота | Размер ($) | Нереализ. PnL | Источник |
| :- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| #4 | Will the highest temperature in Seoul (Incheon) be 21°C | Weather | **NO** | `0.380` | `0.350` | `62.4%` | `$2.99` | `$-0.24` | METAR RKSI (Seoul Incheon) |
| #6 | Will the highest temperature in Shanghai be 26°C on Oct | Weather | **NO** | `0.650` | `0.620` | `74.5%` | `$2.95` | `$-0.14` | METAR ZSPD (Shanghai Pudong) |

## 🔍 Последние проверенные кандидаты и фильтр стакана CLOB
| Рынок | Кат. | Сторона | Оценка бота | Цена Ask | Перекос (Edge) | Проскальзывание CLOB | Решение |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Will the highest temperature in Sao Paulo be 26°C  | Weather | NO | `83.0%` | `79.0%` | `+4.0 п.п.` | `3.00%` | REJECTED: Edge +4.0 pp < 8 pp threshold (P_est=83.0% vs AskVWAP=79.0%) |
| Will Bitcoin reach $87,000 on October 12? | Crypto | YES | `2.0%` | `100.0%` | `-98.0 п.п.` | `100.00%` | REJECTED: Edge -98.0 pp < 8 pp threshold (P_est=2.0% vs AskVWAP=100.0%) |
| Will the highest temperature in Shanghai be 27°C o | Weather | NO | `64.3%` | `46.0%` | `+18.3 п.п.` | `2.00%` | REJECTED: Duplicate underlying event (weather:shanghai:october 13) |
| Will the highest temperature in Shanghai be 26°C o | Weather | NO | `74.5%` | `65.0%` | `+9.5 п.п.` | `3.00%` | EXECUTED BUY #6 ($2.95 @ 0.6500) |
| Will Ethereum reach $2,700 on October 12? | Crypto | YES | `2.0%` | `100.0%` | `-98.0 п.п.` | `100.00%` | REJECTED: Edge -98.0 pp < 8 pp threshold (P_est=2.0% vs AskVWAP=100.0%) |
| Bitcoin Up or Down on October 13? | Crypto | YES | `47.5%` | `43.0%` | `+4.5 п.п.` | `2.00%` | REJECTED: Edge +4.5 pp < 8 pp threshold (P_est=47.5% vs AskVWAP=43.0%) |
| Will Ethereum reach $2,750 on October 12? | Crypto | YES | `2.0%` | `100.0%` | `-98.0 п.п.` | `100.00%` | REJECTED: Edge -98.0 pp < 8 pp threshold (P_est=2.0% vs AskVWAP=100.0%) |
| Will the highest temperature in Seoul (Incheon) be | Weather | YES | `9.8%` | `100.0%` | `-90.2 п.п.` | `100.00%` | REJECTED: Edge -90.2 pp < 8 pp threshold (P_est=9.8% vs AskVWAP=100.0%) |
| Will the highest temperature in Lucknow be 33°C on | Weather | NO | `99.5%` | `93.0%` | `+6.5 п.п.` | `8.00%` | REJECTED: Edge +6.5 pp < 8 pp threshold (P_est=99.5% vs AskVWAP=93.0%) |
| Will the highest temperature in Shenzhen be 31°C o | Weather | NO | `99.5%` | `77.0%` | `+22.5 п.п.` | `6.00%` | REJECTED: CLOB round-trip slippage 6.00% > 3.0% limit |
| Will the highest temperature in Shanghai be 27°C o | Weather | YES | `59.9%` | `54.2%` | `+5.7 п.п.` | `2.21%` | REJECTED: Edge +5.7 pp < 8 pp threshold (P_est=59.9% vs AskVWAP=54.2%) |
| Will the price of Bitcoin be above $84,000 on Octo | Crypto | YES | `33.0%` | `28.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Edge +5.0 pp < 8 pp threshold (P_est=33.0% vs AskVWAP=28.0%) |
| Will the highest temperature in Seoul (Incheon) be | Weather | YES | `1.6%` | `100.0%` | `-98.4 п.п.` | `100.00%` | REJECTED: Edge -98.4 pp < 8 pp threshold (P_est=1.6% vs AskVWAP=100.0%) |
| Will the price of Bitcoin be above $84,000 on Octo | Crypto | YES | `21.0%` | `16.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Edge +5.0 pp < 8 pp threshold (P_est=21.0% vs AskVWAP=16.0%) |
| Will Bitcoin reach $88,000 on October 12? | Crypto | YES | `0.5%` | `100.0%` | `-99.5 п.п.` | `100.00%` | REJECTED: Edge -99.5 pp < 8 pp threshold (P_est=0.5% vs AskVWAP=100.0%) |
| Will the highest temperature in Tokyo be 25°C on O | Weather | NO | `97.5%` | `62.0%` | `+35.5 п.п.` | `6.00%` | REJECTED: CLOB round-trip slippage 6.00% > 3.0% limit |
| Will the highest temperature in Lucknow be 33°C on | Weather | NO | `99.5%` | `93.0%` | `+6.5 п.п.` | `8.00%` | REJECTED: Edge +6.5 pp < 8 pp threshold (P_est=99.5% vs AskVWAP=93.0%) |
| Will the highest temperature in Shenzhen be 31°C o | Weather | NO | `99.5%` | `77.0%` | `+22.5 п.п.` | `6.00%` | REJECTED: CLOB round-trip slippage 6.00% > 3.0% limit |
