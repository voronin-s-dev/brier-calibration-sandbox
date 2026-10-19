# 📊 Отчёт симулятора Polymarket (Устав Grok Bot — Демо-счёт)
**Обновлено:** `2026-10-19 00:44:15 UTC`

## 💰 Состояние виртуального портфеля
| Показатель | Значение | Правило устава |
| :--- | :--- | :--- |
| **Стартовый капитал** | `$50.00 USDC` | Не добавлять деньги |
| **Текущий баланс (Equity)** | **`$27.72 USDC`** (`-22.28$` / `-44.56%`) | Cash + Mark-to-Market по CLOB Bid |
| **Свободный кэш / В сделках** | `$26.91` / `$0.82 USDC` | До 8 открытых позиций, макс 8% банка |
| **Цель окупаемости подписки** | `$-22.28 / $60.00` (`0.0%`) | Цель: +$60.00 в месяц |
| **Просадка от пика (Текущая / Макс)** | `1.16%` / `1.16%` (Пик: `$28.05`) | Стоп-кран при просадке 40% |
| **Закрытых сделок / Win Rate** | `33` / `24.2%` | Brier Score: `0.4280` |

## 📂 Открытые позиции (1 / 8)
| # | Рынок | Кат. | Исход | Вход (Ask VWAP) | Текущий Bid | Оценка бота | Размер ($) | Нереализ. PnL | Источник |
| :- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| #34 | Will Bitcoin dip to $77,500 in October? | Crypto | **YES** | `0.480` | `0.350` | `50.5%` | `$1.12` | `$-0.30` | Binance BTCUSDT 1m/1h Spot Kli |

## 🔍 Последние проверенные кандидаты и фильтр стакана CLOB
| Рынок | Кат. | Сторона | Оценка бота | Цена Ask | Перекос (Edge) | Проскальзывание CLOB | Решение |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Will the price of Bitcoin be above $88,000 on Octo | Crypto | YES | `9.3%` | `5.2%` | `+4.2 п.п.` | `0.60%` | REJECTED: Edge +4.2 pp < 8 pp threshold (P_est=9.3% vs AskVWAP=5.2%) |
| Will the price of Bitcoin be between $78,000 and $ | Crypto | YES | `9.3%` | `3.4%` | `+5.9 п.п.` | `0.25%` | REJECTED: Edge +5.9 pp < 8 pp threshold (P_est=9.3% vs AskVWAP=3.4%) |
| Will the price of Bitcoin be above $90,000 on Octo | Crypto | YES | `2.0%` | `100.0%` | `-98.0 п.п.` | `100.00%` | REJECTED: Edge -98.0 pp < 8 pp threshold (P_est=2.0% vs AskVWAP=100.0%) |
| Will Ethereum dip to $2,200 in October? | Crypto | YES | `42.2%` | `35.0%` | `+7.2 п.п.` | `1.00%` | REJECTED: Edge +7.2 pp < 8 pp threshold (P_est=42.2% vs AskVWAP=35.0%) |
| Will the price of Ethereum be above $2,400 on Octo | Crypto | NO | `45.1%` | `38.0%` | `+7.1 п.п.` | `2.00%` | REJECTED: Edge +7.2 pp < 8 pp threshold (P_est=45.1% vs AskVWAP=38.0%) |
| Will Bitcoin dip to $80,000 in October? | Crypto | YES | `75.5%` | `64.0%` | `+11.5 п.п.` | `1.00%` | REJECTED: Duplicate underlying event (crypto:bitcoin:nodate) |
| Will the price of Ethereum be above $2,300 on Octo | Crypto | NO | `12.7%` | `7.5%` | `+5.2 п.п.` | `0.40%` | REJECTED: Edge +5.2 pp < 8 pp threshold (P_est=12.7% vs AskVWAP=7.5%) |
| Will Bitcoin reach $90,000 in October? | Crypto | YES | `30.6%` | `21.0%` | `+9.6 п.п.` | `1.00%` | REJECTED: Win probability 30.6% < 55% minimum (no underdog lottery bets) |
| Will Bitcoin reach $92,500 in October? | Crypto | YES | `19.1%` | `11.0%` | `+8.1 п.п.` | `1.00%` | REJECTED: Win probability 19.1% < 55% minimum (no underdog lottery bets) |
| Will the price of Bitcoin be above $86,000 on Octo | Crypto | YES | `18.1%` | `13.0%` | `+5.1 п.п.` | `2.48%` | REJECTED: Edge +5.1 pp < 8 pp threshold (P_est=18.1% vs AskVWAP=13.0%) |
| Will Bitcoin dip to $75,000 in October? | Crypto | YES | `32.0%` | `22.0%` | `+10.1 п.п.` | `1.00%` | REJECTED: Win probability 32.0% < 55% minimum (no underdog lottery bets) |
| Will Bitcoin reach $87,500 in October? | Crypto | YES | `46.3%` | `36.0%` | `+10.3 п.п.` | `1.00%` | REJECTED: Win probability 46.3% < 55% minimum (no underdog lottery bets) |
| Will Bitcoin reach $95,000 in October? | Crypto | YES | `11.3%` | `4.9%` | `+6.4 п.п.` | `0.10%` | REJECTED: Edge +6.4 pp < 8 pp threshold (P_est=11.3% vs AskVWAP=4.9%) |
| Will the price of Bitcoin be above $72,000 on Octo | Crypto | NO | `0.5%` | `100.0%` | `-99.5 п.п.` | `100.00%` | REJECTED: Edge -99.5 pp < 8 pp threshold (P_est=0.5% vs AskVWAP=100.0%) |
| Will the price of Bitcoin be above $80,000 on Octo | Crypto | NO | `10.7%` | `6.0%` | `+4.7 п.п.` | `1.00%` | REJECTED: Edge +4.7 pp < 8 pp threshold (P_est=10.7% vs AskVWAP=6.0%) |
| Will Ethereum reach $2,600 in October? | Crypto | YES | `48.7%` | `43.0%` | `+5.7 п.п.` | `1.00%` | REJECTED: Edge +5.7 pp < 8 pp threshold (P_est=48.7% vs AskVWAP=43.0%) |
| Will the price of Bitcoin be above $88,000 on Octo | Crypto | YES | `9.4%` | `5.2%` | `+4.2 п.п.` | `0.60%` | REJECTED: Edge +4.2 pp < 8 pp threshold (P_est=9.4% vs AskVWAP=5.2%) |
| Will the price of Bitcoin be between $78,000 and $ | Crypto | YES | `9.4%` | `4.4%` | `+5.0 п.п.` | `0.30%` | REJECTED: Edge +5.0 pp < 8 pp threshold (P_est=9.4% vs AskVWAP=4.4%) |
