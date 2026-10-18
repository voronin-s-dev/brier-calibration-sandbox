# 📊 Отчёт симулятора Polymarket (Устав Grok Bot — Демо-счёт)
**Обновлено:** `2026-10-18 22:51:23 UTC`

## 💰 Состояние виртуального портфеля
| Показатель | Значение | Правило устава |
| :--- | :--- | :--- |
| **Стартовый капитал** | `$50.00 USDC` | Не добавлять деньги |
| **Текущий баланс (Equity)** | **`$27.84 USDC`** (`-22.16$` / `-44.32%`) | Cash + Mark-to-Market по CLOB Bid |
| **Свободный кэш / В сделках** | `$26.91` / `$0.93 USDC` | До 8 открытых позиций, макс 8% банка |
| **Цель окупаемости подписки** | `$-22.16 / $60.00` (`0.0%`) | Цель: +$60.00 в месяц |
| **Просадка от пика (Текущая / Макс)** | `0.75%` / `0.75%` (Пик: `$28.05`) | Стоп-кран при просадке 40% |
| **Закрытых сделок / Win Rate** | `33` / `24.2%` | Brier Score: `0.4280` |

## 📂 Открытые позиции (1 / 8)
| # | Рынок | Кат. | Исход | Вход (Ask VWAP) | Текущий Bid | Оценка бота | Размер ($) | Нереализ. PnL | Источник |
| :- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| #34 | Will Bitcoin dip to $77,500 in October? | Crypto | **YES** | `0.480` | `0.400` | `55.4%` | `$1.12` | `$-0.19` | Binance BTCUSDT 1m/1h Spot Kli |

## 🔍 Последние проверенные кандидаты и фильтр стакана CLOB
| Рынок | Кат. | Сторона | Оценка бота | Цена Ask | Перекос (Edge) | Проскальзывание CLOB | Решение |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Will the price of Bitcoin be above $78,000 on Octo | Crypto | NO | `14.5%` | `7.3%` | `+7.2 п.п.` | `0.10%` | REJECTED: Edge +7.2 pp < 8 pp threshold (P_est=14.5% vs AskVWAP=7.3%) |
| Will the price of Ethereum be above $2,700 on Octo | Crypto | YES | `2.0%` | `100.0%` | `-98.0 п.п.` | `100.00%` | REJECTED: Edge -98.0 pp < 8 pp threshold (P_est=2.0% vs AskVWAP=100.0%) |
| Will the price of Bitcoin be above $84,000 on Octo | Crypto | YES | `17.1%` | `13.0%` | `+4.1 п.п.` | `1.00%` | REJECTED: Edge +4.1 pp < 8 pp threshold (P_est=17.1% vs AskVWAP=13.0%) |
| Will Ethereum reach $2,600 in October? | Crypto | YES | `44.3%` | `40.0%` | `+4.3 п.п.` | `1.00%` | REJECTED: Edge +4.3 pp < 8 pp threshold (P_est=44.3% vs AskVWAP=40.0%) |
| Will the price of Bitcoin be above $86,000 on Octo | Crypto | YES | `14.6%` | `9.3%` | `+5.4 п.п.` | `2.26%` | REJECTED: Edge +5.4 pp < 8 pp threshold (P_est=14.6% vs AskVWAP=9.3%) |
| Will Bitcoin dip to $80,000 in October? | Crypto | YES | `81.5%` | `73.0%` | `+8.5 п.п.` | `1.00%` | REJECTED: Duplicate underlying event (crypto:bitcoin:nodate) |
| Will the price of Bitcoin be above $90,000 on Octo | Crypto | YES | `2.0%` | `100.0%` | `-98.0 п.п.` | `100.00%` | REJECTED: Edge -98.0 pp < 8 pp threshold (P_est=2.0% vs AskVWAP=100.0%) |
| Will Ethereum dip to $2,200 in October? | Crypto | YES | `47.4%` | `40.0%` | `+7.4 п.п.` | `1.00%` | REJECTED: Edge +7.4 pp < 8 pp threshold (P_est=47.4% vs AskVWAP=40.0%) |
| Will the price of Ethereum be above $2,400 on Octo | Crypto | NO | `58.9%` | `53.0%` | `+5.9 п.п.` | `1.00%` | REJECTED: Edge +5.9 pp < 8 pp threshold (P_est=58.9% vs AskVWAP=53.0%) |
| Will the price of Ethereum be above $2,300 on Octo | Crypto | NO | `19.1%` | `14.0%` | `+5.1 п.п.` | `0.64%` | REJECTED: Edge +5.0 pp < 8 pp threshold (P_est=19.1% vs AskVWAP=14.0%) |
| Will Bitcoin reach $92,500 in October? | Crypto | YES | `16.7%` | `9.0%` | `+7.7 п.п.` | `1.00%` | REJECTED: Edge +7.7 pp < 8 pp threshold (P_est=16.7% vs AskVWAP=9.0%) |
| Will Bitcoin dip to $75,000 in October? | Crypto | YES | `35.3%` | `23.0%` | `+12.3 п.п.` | `1.00%` | REJECTED: Win probability 35.3% < 55% minimum (no underdog lottery bets) |
| Will Bitcoin reach $90,000 in October? | Crypto | YES | `27.1%` | `17.0%` | `+10.1 п.п.` | `1.00%` | REJECTED: Win probability 27.1% < 55% minimum (no underdog lottery bets) |
| Will Bitcoin reach $87,500 in October? | Crypto | YES | `41.9%` | `30.0%` | `+11.9 п.п.` | `1.00%` | REJECTED: Win probability 41.9% < 55% minimum (no underdog lottery bets) |
| Will the price of Bitcoin be above $72,000 on Octo | Crypto | NO | `0.5%` | `100.0%` | `-99.5 п.п.` | `100.00%` | REJECTED: Edge -99.5 pp < 8 pp threshold (P_est=0.5% vs AskVWAP=100.0%) |
| Will Bitcoin reach $95,000 in October? | Crypto | YES | `9.7%` | `3.8%` | `+5.9 п.п.` | `0.25%` | REJECTED: Edge +5.9 pp < 8 pp threshold (P_est=9.7% vs AskVWAP=3.8%) |
| Will the price of Bitcoin be above $80,000 on Octo | Crypto | NO | `19.1%` | `12.0%` | `+7.1 п.п.` | `1.00%` | REJECTED: Edge +7.1 pp < 8 pp threshold (P_est=19.1% vs AskVWAP=12.0%) |
| Will the price of Bitcoin be above $78,000 on Octo | Crypto | NO | `14.6%` | `7.9%` | `+6.7 п.п.` | `0.10%` | REJECTED: Edge +6.7 pp < 8 pp threshold (P_est=14.6% vs AskVWAP=7.9%) |
