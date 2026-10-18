# 📊 Отчёт симулятора Polymarket (Устав Grok Bot — Демо-счёт)
**Обновлено:** `2026-10-18 22:33:09 UTC`

## 💰 Состояние виртуального портфеля
| Показатель | Значение | Правило устава |
| :--- | :--- | :--- |
| **Стартовый капитал** | `$50.00 USDC` | Не добавлять деньги |
| **Текущий баланс (Equity)** | **`$27.89 USDC`** (`-22.11$` / `-44.23%`) | Cash + Mark-to-Market по CLOB Bid |
| **Свободный кэш / В сделках** | `$26.91` / `$0.98 USDC` | До 8 открытых позиций, макс 8% банка |
| **Цель окупаемости подписки** | `$-22.11 / $60.00` (`0.0%`) | Цель: +$60.00 в месяц |
| **Просадка от пика (Текущая / Макс)** | `0.58%` / `0.58%` (Пик: `$28.05`) | Стоп-кран при просадке 40% |
| **Закрытых сделок / Win Rate** | `33` / `24.2%` | Brier Score: `0.4280` |

## 📂 Открытые позиции (1 / 8)
| # | Рынок | Кат. | Исход | Вход (Ask VWAP) | Текущий Bid | Оценка бота | Размер ($) | Нереализ. PnL | Источник |
| :- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| #34 | Will Bitcoin dip to $77,500 in October? | Crypto | **YES** | `0.480` | `0.420` | `55.8%` | `$1.12` | `$-0.14` | Binance BTCUSDT 1m/1h Spot Kli |

## 🔍 Последние проверенные кандидаты и фильтр стакана CLOB
| Рынок | Кат. | Сторона | Оценка бота | Цена Ask | Перекос (Edge) | Проскальзывание CLOB | Решение |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Will the price of Bitcoin be above $78,000 on Octo | Crypto | NO | `14.7%` | `8.1%` | `+6.6 п.п.` | `0.20%` | REJECTED: Edge +6.6 pp < 8 pp threshold (P_est=14.7% vs AskVWAP=8.1%) |
| Will the price of Ethereum be above $2,700 on Octo | Crypto | YES | `2.0%` | `100.0%` | `-98.0 п.п.` | `100.00%` | REJECTED: Edge -98.0 pp < 8 pp threshold (P_est=2.0% vs AskVWAP=100.0%) |
| Will the price of Bitcoin be above $84,000 on Octo | Crypto | YES | `16.8%` | `11.0%` | `+5.8 п.п.` | `1.00%` | REJECTED: Edge +5.8 pp < 8 pp threshold (P_est=16.8% vs AskVWAP=11.0%) |
| Will Ethereum reach $2,600 in October? | Crypto | YES | `44.0%` | `38.0%` | `+6.0 п.п.` | `1.00%` | REJECTED: Edge +6.0 pp < 8 pp threshold (P_est=44.0% vs AskVWAP=38.0%) |
| Will the price of Bitcoin be above $86,000 on Octo | Crypto | YES | `14.7%` | `9.0%` | `+5.7 п.п.` | `2.00%` | REJECTED: Edge +5.7 pp < 8 pp threshold (P_est=14.7% vs AskVWAP=9.0%) |
| Will Bitcoin dip to $80,000 in October? | Crypto | YES | `82.2%` | `75.0%` | `+7.2 п.п.` | `1.00%` | REJECTED: Edge +7.2 pp < 8 pp threshold (P_est=82.2% vs AskVWAP=75.0%) |
| Will the price of Bitcoin be above $90,000 on Octo | Crypto | YES | `2.0%` | `100.0%` | `-98.0 п.п.` | `100.00%` | REJECTED: Edge -98.0 pp < 8 pp threshold (P_est=2.0% vs AskVWAP=100.0%) |
| Will Ethereum dip to $2,200 in October? | Crypto | YES | `47.4%` | `41.0%` | `+6.4 п.п.` | `1.00%` | REJECTED: Edge +6.4 pp < 8 pp threshold (P_est=47.4% vs AskVWAP=41.0%) |
| Will Bitcoin reach $92,500 in October? | Crypto | YES | `16.7%` | `9.0%` | `+7.7 п.п.` | `1.00%` | REJECTED: Edge +7.7 pp < 8 pp threshold (P_est=16.7% vs AskVWAP=9.0%) |
| Will Bitcoin reach $90,000 in October? | Crypto | YES | `27.1%` | `17.0%` | `+10.1 п.п.` | `1.00%` | REJECTED: Win probability 27.1% < 55% minimum (no underdog lottery bets) |
| Will Bitcoin dip to $75,000 in October? | Crypto | YES | `35.6%` | `25.0%` | `+10.7 п.п.` | `1.00%` | REJECTED: Win probability 35.6% < 55% minimum (no underdog lottery bets) |
| Will Bitcoin reach $87,500 in October? | Crypto | YES | `41.6%` | `29.0%` | `+12.6 п.п.` | `1.00%` | REJECTED: Win probability 41.6% < 55% minimum (no underdog lottery bets) |
| Will the price of Bitcoin be above $72,000 on Octo | Crypto | NO | `0.5%` | `100.0%` | `-99.5 п.п.` | `100.00%` | REJECTED: Edge -99.5 pp < 8 pp threshold (P_est=0.5% vs AskVWAP=100.0%) |
| Will the price of Bitcoin be above $80,000 on Octo | Crypto | NO | `19.8%` | `14.0%` | `+5.8 п.п.` | `1.00%` | REJECTED: Edge +5.8 pp < 8 pp threshold (P_est=19.8% vs AskVWAP=14.0%) |
| Will Bitcoin reach $95,000 in October? | Crypto | YES | `9.7%` | `3.6%` | `+6.1 п.п.` | `0.31%` | REJECTED: Edge +6.1 pp < 8 pp threshold (P_est=9.7% vs AskVWAP=3.6%) |
| Will the price of Bitcoin be above $78,000 on Octo | Crypto | NO | `19.2%` | `12.7%` | `+6.5 п.п.` | `1.50%` | REJECTED: Edge +6.5 pp < 8 pp threshold (P_est=19.2% vs AskVWAP=12.7%) |
| Will the highest temperature in Wuhan be 17°C on O | Weather | NO | `86.2%` | `43.9%` | `+42.4 п.п.` | `1.88%` | REJECTED: Narrow weather bracket NO bet prohibited (airport METAR microclimate tail risk) |
| Will Ethereum reach $2,600 in October? | Crypto | YES | `36.1%` | `29.0%` | `+7.1 п.п.` | `1.00%` | REJECTED: Edge +7.1 pp < 8 pp threshold (P_est=36.1% vs AskVWAP=29.0%) |
