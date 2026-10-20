# 📊 Отчёт симулятора Polymarket (Устав Grok Bot — Демо-счёт)
**Обновлено:** `2026-10-20 01:12:14 UTC`

## 💰 Состояние виртуального портфеля
| Показатель | Значение | Правило устава |
| :--- | :--- | :--- |
| **Стартовый капитал** | `$50.00 USDC` | Не добавлять деньги |
| **Текущий баланс (Equity)** | **`$27.92 USDC`** (`-22.08$` / `-44.15%`) | Cash + Mark-to-Market по CLOB Bid |
| **Свободный кэш / В сделках** | `$26.54` / `$1.38 USDC` | До 8 открытых позиций, макс 8% банка |
| **Цель окупаемости подписки** | `$-22.08 / $60.00` (`0.0%`) | Цель: +$60.00 в месяц |
| **Просадка от пика (Текущая / Макс)** | `0.44%` / `1.48%` (Пик: `$28.05`) | Стоп-кран при просадке 40% |
| **Закрытых сделок / Win Rate** | `34` / `23.5%` | Brier Score: `0.4280` |

## 📂 Открытые позиции (1 / 8)
| # | Рынок | Кат. | Исход | Вход (Ask VWAP) | Текущий Bid | Оценка бота | Размер ($) | Нереализ. PnL | Источник |
| :- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| #35 | Will Bitcoin dip to $80,000 in October? | Crypto | **YES** | `0.610` | `0.760` | `83.2%` | `$1.11` | `$+0.27` | Kraken BTCUSDT 1m/1h Spot Klin |

## 🔍 Последние проверенные кандидаты и фильтр стакана CLOB
| Рынок | Кат. | Сторона | Оценка бота | Цена Ask | Перекос (Edge) | Проскальзывание CLOB | Решение |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Will Bitcoin dip to $76,000 October 19-25? | Crypto | YES | `27.0%` | `13.0%` | `+14.0 п.п.` | `1.00%` | REJECTED: Win probability 27.0% < 55% minimum (no underdog lottery bets) |
| Will the price of Bitcoin be between $78,000 and $ | Crypto | YES | `18.5%` | `11.5%` | `+7.0 п.п.` | `1.58%` | REJECTED: Edge +7.0 pp < 8 pp threshold (P_est=18.5% vs AskVWAP=11.5%) |
| Will the price of Bitcoin be above $76,000 on Octo | Crypto | NO | `12.9%` | `7.5%` | `+5.4 п.п.` | `3.40%` | REJECTED: Edge +5.4 pp < 8 pp threshold (P_est=12.9% vs AskVWAP=7.5%) |
| Will Solana dip to $100 in October? | Crypto | YES | `75.2%` | `71.0%` | `+4.2 п.п.` | `3.00%` | REJECTED: Edge +4.2 pp < 8 pp threshold (P_est=75.2% vs AskVWAP=71.0%) |
| Will the price of Bitcoin be above $80,000 on Octo | Crypto | NO | `29.1%` | `22.0%` | `+7.1 п.п.` | `1.00%` | REJECTED: Edge +7.1 pp < 8 pp threshold (P_est=29.1% vs AskVWAP=22.0%) |
| Will Bitcoin reach $92,500 in October? | Crypto | YES | `13.9%` | `6.0%` | `+7.9 п.п.` | `1.00%` | REJECTED: Edge +7.9 pp < 8 pp threshold (P_est=13.9% vs AskVWAP=6.0%) |
| Will Bitcoin reach $95,000 in October? | Crypto | YES | `7.8%` | `3.0%` | `+4.8 п.п.` | `0.10%` | REJECTED: Edge +4.8 pp < 8 pp threshold (P_est=7.8% vs AskVWAP=3.0%) |
| Will Bitcoin dip to $77,500 in October? | Crypto | YES | `55.5%` | `42.0%` | `+13.5 п.п.` | `1.00%` | REJECTED: Duplicate underlying event (crypto:bitcoin:nodate) |
| Will the price of Bitcoin be above $92,000 on Octo | Crypto | YES | `2.0%` | `100.0%` | `-98.0 п.п.` | `100.00%` | REJECTED: Edge -98.0 pp < 8 pp threshold (P_est=2.0% vs AskVWAP=100.0%) |
| Will the price of Bitcoin be above $78,000 on Octo | Crypto | NO | `9.9%` | `3.8%` | `+6.1 п.п.` | `0.44%` | REJECTED: Edge +6.1 pp < 8 pp threshold (P_est=9.9% vs AskVWAP=3.8%) |
| Will the price of Bitcoin be above $74,000 on Octo | Crypto | NO | `0.5%` | `100.0%` | `-99.5 п.п.` | `100.00%` | REJECTED: Edge -99.5 pp < 8 pp threshold (P_est=0.5% vs AskVWAP=100.0%) |
| Will Bitcoin dip to $75,000 in October? | Crypto | YES | `35.0%` | `22.0%` | `+13.0 п.п.` | `1.00%` | REJECTED: Win probability 35.0% < 55% minimum (no underdog lottery bets) |
| Will Bitcoin reach $85,000 in October? | Crypto | YES | `58.3%` | `48.0%` | `+10.3 п.п.` | `1.00%` | REJECTED: Duplicate underlying event (crypto:bitcoin:nodate) |
| Will the price of Bitcoin be above $88,000 on Octo | Crypto | YES | `2.0%` | `100.0%` | `-98.0 п.п.` | `100.00%` | REJECTED: Edge -98.0 pp < 8 pp threshold (P_est=2.0% vs AskVWAP=100.0%) |
| Will Bitcoin reach $90,000 in October? | Crypto | YES | `23.3%` | `13.0%` | `+10.3 п.п.` | `1.00%` | REJECTED: Win probability 23.3% < 55% minimum (no underdog lottery bets) |
| Will the price of Bitcoin be above $80,000 on Octo | Crypto | NO | `20.1%` | `13.0%` | `+7.1 п.п.` | `0.80%` | REJECTED: Edge +7.1 pp < 8 pp threshold (P_est=20.1% vs AskVWAP=13.0%) |
| Will Bitcoin reach $87,500 in October? | Crypto | YES | `38.1%` | `25.0%` | `+13.1 п.п.` | `1.00%` | REJECTED: Win probability 38.1% < 55% minimum (no underdog lottery bets) |
| Will the price of Bitcoin be between $78,000 and $ | Crypto | YES | `9.4%` | `3.0%` | `+6.4 п.п.` | `0.30%` | REJECTED: Edge +6.4 pp < 8 pp threshold (P_est=9.4% vs AskVWAP=3.0%) |
