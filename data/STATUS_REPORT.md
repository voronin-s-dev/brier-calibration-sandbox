# 📊 Отчёт симулятора Polymarket (Устав Grok Bot — Демо-счёт)
**Обновлено:** `2026-10-13 19:26:31 UTC`

## 💰 Состояние виртуального портфеля
| Показатель | Значение | Правило устава |
| :--- | :--- | :--- |
| **Стартовый капитал** | `$50.00 USDC` | Не добавлять деньги |
| **Текущий баланс (Equity)** | **`$41.88 USDC`** (`-8.12$` / `-16.25%`) | Cash + Mark-to-Market по CLOB Bid |
| **Свободный кэш / В сделках** | `$36.81` / `$5.07 USDC` | До 8 открытых позиций, макс 8% банка |
| **Цель окупаемости подписки** | `$-8.12 / $60.00` (`0.0%`) | Цель: +$60.00 в месяц |
| **Просадка от пика (Текущая / Макс)** | `22.09%` / `22.81%` (Пик: `$53.75`) | Стоп-кран при просадке 40% |
| **Закрытых сделок / Win Rate** | `12` / `33.3%` | Brier Score: `0.3143` |

## 📂 Открытые позиции (2 / 8)
| # | Рынок | Кат. | Исход | Вход (Ask VWAP) | Текущий Bid | Оценка бота | Размер ($) | Нереализ. PnL | Источник |
| :- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| #9 | Will Bitcoin dip to $80,000 October 12-18? | Crypto | **YES** | `0.300` | `0.280` | `36.1%` | `$3.07` | `$-0.20` | Binance BTCUSDT 1m/1h Spot Kli |
| #13 | Will Ethereum reach $2,700 October 12-18? | Crypto | **YES** | `0.130` | `0.123` | `23.4%` | `$2.33` | `$-0.13` | Binance ETHUSDT 1m/1h Spot Kli |

## 🔍 Последние проверенные кандидаты и фильтр стакана CLOB
| Рынок | Кат. | Сторона | Оценка бота | Цена Ask | Перекос (Edge) | Проскальзывание CLOB | Решение |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Bitcoin Up or Down on October 14? | Crypto | YES | `44.0%` | `39.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Edge +5.0 pp < 8 pp threshold (P_est=44.0% vs AskVWAP=39.0%) |
| Will the highest temperature in Cape Town be 19°C  | Weather | NO | `78.3%` | `71.0%` | `+7.3 п.п.` | `2.00%` | REJECTED: Edge +7.3 pp < 8 pp threshold (P_est=78.3% vs AskVWAP=71.0%) |
| Will the highest temperature in Manila be 33°C on  | Weather | NO | `72.2%` | `64.0%` | `+8.1 п.п.` | `3.04%` | REJECTED: CLOB round-trip slippage 3.04% > 2.0% limit |
| Will the price of Bitcoin be above $80,000 on Octo | Crypto | NO | `11.5%` | `7.0%` | `+4.5 п.п.` | `2.00%` | REJECTED: Edge +4.5 pp < 8 pp threshold (P_est=11.5% vs AskVWAP=7.0%) |
| Will the price of Bitcoin be above $80,000 on Octo | Crypto | NO | `17.0%` | `12.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Edge +5.0 pp < 8 pp threshold (P_est=17.0% vs AskVWAP=12.0%) |
| Will the price of Ethereum be above $2,400 on Octo | Crypto | YES | `92.5%` | `88.0%` | `+4.5 п.п.` | `2.00%` | REJECTED: Edge +4.5 pp < 8 pp threshold (P_est=92.5% vs AskVWAP=88.0%) |
| Will the price of Bitcoin be above $84,000 on Octo | Crypto | YES | `39.0%` | `34.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Edge +5.0 pp < 8 pp threshold (P_est=39.0% vs AskVWAP=34.0%) |
| Bitcoin Up or Down on October 14? | Crypto | YES | `44.0%` | `39.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Edge +5.0 pp < 8 pp threshold (P_est=44.0% vs AskVWAP=39.0%) |
| Will the highest temperature in Cape Town be 19°C  | Weather | NO | `78.3%` | `71.0%` | `+7.3 п.п.` | `2.00%` | REJECTED: Edge +7.3 pp < 8 pp threshold (P_est=78.3% vs AskVWAP=71.0%) |
| Will the highest temperature in Manila be 33°C on  | Weather | NO | `72.2%` | `64.0%` | `+8.1 п.п.` | `3.04%` | REJECTED: CLOB round-trip slippage 3.04% > 2.0% limit |
| Will the price of Bitcoin be above $80,000 on Octo | Crypto | NO | `11.5%` | `7.0%` | `+4.5 п.п.` | `2.00%` | REJECTED: Edge +4.5 pp < 8 pp threshold (P_est=11.5% vs AskVWAP=7.0%) |
| Will the price of Bitcoin be above $80,000 on Octo | Crypto | NO | `17.0%` | `12.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Edge +5.0 pp < 8 pp threshold (P_est=17.0% vs AskVWAP=12.0%) |
| Will the price of Ethereum be above $2,400 on Octo | Crypto | YES | `92.5%` | `88.0%` | `+4.5 п.п.` | `2.00%` | REJECTED: Edge +4.5 pp < 8 pp threshold (P_est=92.5% vs AskVWAP=88.0%) |
| Will the price of Bitcoin be above $84,000 on Octo | Crypto | YES | `39.0%` | `34.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Edge +5.0 pp < 8 pp threshold (P_est=39.0% vs AskVWAP=34.0%) |
| Will Bitcoin dip to $82,000 on October 13? | Crypto | NO | `96.7%` | `85.0%` | `+11.7 п.п.` | `1.00%` | EXECUTED BUY #14 ($3.34 @ 0.8500) |
| Will Ethereum reach $2,800 October 12-18? | Crypto | YES | `8.2%` | `3.5%` | `+4.7 п.п.` | `0.12%` | REJECTED: Edge +4.7 pp < 8 pp threshold (P_est=8.2% vs AskVWAP=3.5%) |
| Bitcoin Up or Down on October 14? | Crypto | YES | `46.0%` | `41.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Edge +5.0 pp < 8 pp threshold (P_est=46.0% vs AskVWAP=41.0%) |
| Will the price of Bitcoin be above $74,000 on Octo | Crypto | NO | `0.5%` | `100.0%` | `-99.5 п.п.` | `100.00%` | REJECTED: Edge -99.5 pp < 8 pp threshold (P_est=0.5% vs AskVWAP=100.0%) |
