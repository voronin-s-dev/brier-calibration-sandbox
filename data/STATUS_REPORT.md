# 📊 Отчёт симулятора Polymarket (Устав Grok Bot — Демо-счёт)
**Обновлено:** `2026-10-18 16:27:22 UTC`

## 💰 Состояние виртуального портфеля
| Показатель | Значение | Правило устава |
| :--- | :--- | :--- |
| **Стартовый капитал** | `$50.00 USDC` | Не добавлять деньги |
| **Текущий баланс (Equity)** | **`$28.00 USDC`** (`-22.00$` / `-44.00%`) | Cash + Mark-to-Market по CLOB Bid |
| **Свободный кэш / В сделках** | `$26.91` / `$1.10 USDC` | До 8 открытых позиций, макс 8% банка |
| **Цель окупаемости подписки** | `$-22.00 / $60.00` (`0.0%`) | Цель: +$60.00 в месяц |
| **Просадка от пика (Текущая / Макс)** | `0.08%` / `0.08%` (Пик: `$28.03`) | Стоп-кран при просадке 40% |
| **Закрытых сделок / Win Rate** | `33` / `24.2%` | Brier Score: `0.4280` |

## 📂 Открытые позиции (1 / 8)
| # | Рынок | Кат. | Исход | Вход (Ask VWAP) | Текущий Bid | Оценка бота | Размер ($) | Нереализ. PnL | Источник |
| :- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| #34 | Will Bitcoin dip to $77,500 in October? | Crypto | **YES** | `0.480` | `0.470` | `59.3%` | `$1.12` | `$-0.02` | Binance BTCUSDT 1m/1h Spot Kli |

## 🔍 Последние проверенные кандидаты и фильтр стакана CLOB
| Рынок | Кат. | Сторона | Оценка бота | Цена Ask | Перекос (Edge) | Проскальзывание CLOB | Решение |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Tampa Bay Rays vs. Cleveland Guardians | Sports | YES | `60.0%` | `55.0%` | `+5.0 п.п.` | `1.00%` | REJECTED: Edge +5.0 pp < 8 pp threshold (P_est=60.0% vs AskVWAP=55.0%) |
| Will Bitcoin reach $85,000 in October? | Crypto | YES | `60.0%` | `48.0%` | `+12.0 п.п.` | `1.00%` | REJECTED: Duplicate underlying event (crypto:bitcoin:nodate) |
| Will the highest temperature in Paris be 14°C on O | Weather | NO | `76.6%` | `69.0%` | `+7.6 п.п.` | `3.00%` | REJECTED: Edge +7.6 pp < 8 pp threshold (P_est=76.6% vs AskVWAP=69.0%) |
| Will the highest temperature in Beijing be 19°C on | Weather | NO | `71.5%` | `56.0%` | `+15.5 п.п.` | `2.00%` | REJECTED: Narrow weather bracket NO bet prohibited (airport METAR microclimate tail risk) |
| Will Bitcoin reach $92,500 in October? | Crypto | YES | `15.8%` | `7.0%` | `+8.8 п.п.` | `1.00%` | REJECTED: Win probability 15.8% < 55% minimum (no underdog lottery bets) |
| Will the highest temperature in Lucknow be 32°C on | Weather | NO | `88.3%` | `83.0%` | `+5.3 п.п.` | `1.00%` | REJECTED: Edge +5.3 pp < 8 pp threshold (P_est=88.3% vs AskVWAP=83.0%) |
| Will the price of Bitcoin be above $86,000 on Octo | Crypto | YES | `13.9%` | `8.0%` | `+5.9 п.п.` | `2.00%` | REJECTED: Edge +5.9 pp < 8 pp threshold (P_est=13.9% vs AskVWAP=8.0%) |
| Will Bitcoin dip to $75,000 in October? | Crypto | YES | `38.2%` | `28.0%` | `+10.2 п.п.` | `1.00%` | REJECTED: Win probability 38.2% < 55% minimum (no underdog lottery bets) |
| Will Bitcoin dip to $72,500 in October? | Crypto | YES | `22.1%` | `14.0%` | `+8.1 п.п.` | `1.00%` | REJECTED: Win probability 22.1% < 55% minimum (no underdog lottery bets) |
| Will the price of Ethereum be above $2,300 on Octo | Crypto | NO | `24.4%` | `20.1%` | `+4.3 п.п.` | `1.00%` | REJECTED: Edge +4.3 pp < 8 pp threshold (P_est=24.4% vs AskVWAP=20.1%) |
| Will Ethereum dip to $2,200 in October? | Crypto | YES | `51.3%` | `46.0%` | `+5.3 п.п.` | `1.00%` | REJECTED: Edge +5.3 pp < 8 pp threshold (P_est=51.3% vs AskVWAP=46.0%) |
| Will Bitcoin dip to $77,500 in October? | Crypto | YES | `59.3%` | `48.0%` | `+11.3 п.п.` | `1.00%` | EXECUTED BUY #34 ($1.12 @ 0.4800) |
| Will Bitcoin reach $90,000 in October? | Crypto | YES | `25.7%` | `15.0%` | `+10.7 п.п.` | `1.00%` | REJECTED: Win probability 25.7% < 55% minimum (no underdog lottery bets) |
| Will Bitcoin reach $87,500 in October? | Crypto | YES | `39.6%` | `26.0%` | `+13.6 п.п.` | `1.00%` | REJECTED: Win probability 39.6% < 55% minimum (no underdog lottery bets) |
| Will the price of Bitcoin be above $80,000 on Octo | Crypto | NO | `26.5%` | `20.0%` | `+6.5 п.п.` | `1.00%` | REJECTED: Edge +6.5 pp < 8 pp threshold (P_est=26.5% vs AskVWAP=20.0%) |
| Will Bitcoin reach $82,500 in October? | Crypto | YES | `85.7%` | `81.0%` | `+4.7 п.п.` | `1.00%` | REJECTED: Edge +4.7 pp < 8 pp threshold (P_est=85.7% vs AskVWAP=81.0%) |
| Will Bitcoin reach $95,000 in October? | Crypto | YES | `9.4%` | `3.3%` | `+6.1 п.п.` | `0.31%` | REJECTED: Edge +6.1 pp < 8 pp threshold (P_est=9.4% vs AskVWAP=3.3%) |
| Will the price of Bitcoin be above $88,000 on Octo | Crypto | YES | `2.0%` | `100.0%` | `-98.0 п.п.` | `100.00%` | REJECTED: Edge -98.0 pp < 8 pp threshold (P_est=2.0% vs AskVWAP=100.0%) |
