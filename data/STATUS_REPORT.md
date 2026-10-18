# 📊 Отчёт симулятора Polymarket (Устав Grok Bot — Демо-счёт)
**Обновлено:** `2026-10-18 20:29:42 UTC`

## 💰 Состояние виртуального портфеля
| Показатель | Значение | Правило устава |
| :--- | :--- | :--- |
| **Стартовый капитал** | `$50.00 USDC` | Не добавлять деньги |
| **Текущий баланс (Equity)** | **`$28.05 USDC`** (`-21.95$` / `-43.90%`) | Cash + Mark-to-Market по CLOB Bid |
| **Свободный кэш / В сделках** | `$26.91` / `$1.14 USDC` | До 8 открытых позиций, макс 8% банка |
| **Цель окупаемости подписки** | `$-21.95 / $60.00` (`0.0%`) | Цель: +$60.00 в месяц |
| **Просадка от пика (Текущая / Макс)** | `0.00%` / `0.17%` (Пик: `$28.05`) | Стоп-кран при просадке 40% |
| **Закрытых сделок / Win Rate** | `33` / `24.2%` | Brier Score: `0.4280` |

## 📂 Открытые позиции (1 / 8)
| # | Рынок | Кат. | Исход | Вход (Ask VWAP) | Текущий Bid | Оценка бота | Размер ($) | Нереализ. PnL | Источник |
| :- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| #34 | Will Bitcoin dip to $77,500 in October? | Crypto | **YES** | `0.480` | `0.490` | `62.1%` | `$1.12` | `$+0.02` | Binance BTCUSDT 1m/1h Spot Kli |

## 🔍 Последние проверенные кандидаты и фильтр стакана CLOB
| Рынок | Кат. | Сторона | Оценка бота | Цена Ask | Перекос (Edge) | Проскальзывание CLOB | Решение |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Will the highest temperature in Beijing be 20°C on | Weather | NO | `84.3%` | `75.0%` | `+9.3 п.п.` | `3.00%` | REJECTED: Narrow weather bracket NO bet prohibited (airport METAR microclimate tail risk) |
| Will the highest temperature in Wuhan be 17°C on O | Weather | NO | `86.4%` | `45.0%` | `+41.4 п.п.` | `3.00%` | REJECTED: Narrow weather bracket NO bet prohibited (airport METAR microclimate tail risk) |
| Will the price of Bitcoin be above $78,000 on Octo | Crypto | NO | `19.2%` | `12.4%` | `+6.9 п.п.` | `1.20%` | REJECTED: Edge +6.8 pp < 8 pp threshold (P_est=19.2% vs AskVWAP=12.4%) |
| Will the price of Bitcoin be above $78,000 on Octo | Crypto | NO | `14.2%` | `8.5%` | `+5.7 п.п.` | `0.90%` | REJECTED: Edge +5.7 pp < 8 pp threshold (P_est=14.2% vs AskVWAP=8.5%) |
| Will Ethereum reach $2,600 in October? | Crypto | YES | `36.3%` | `30.0%` | `+6.3 п.п.` | `2.00%` | REJECTED: Edge +6.3 pp < 8 pp threshold (P_est=36.3% vs AskVWAP=30.0%) |
| Will Bitcoin dip to $70,000 in October? | Crypto | YES | `13.0%` | `9.0%` | `+4.0 п.п.` | `1.00%` | REJECTED: Edge +4.0 pp < 8 pp threshold (P_est=13.0% vs AskVWAP=9.0%) |
| Will Bitcoin reach $92,500 in October? | Crypto | YES | `14.5%` | `7.0%` | `+7.5 п.п.` | `1.00%` | REJECTED: Edge +7.5 pp < 8 pp threshold (P_est=14.5% vs AskVWAP=7.0%) |
| Will Ethereum dip to $2,200 in October? | Crypto | YES | `56.7%` | `50.0%` | `+6.7 п.п.` | `1.00%` | REJECTED: Edge +6.7 pp < 8 pp threshold (P_est=56.7% vs AskVWAP=50.0%) |
| Will Bitcoin dip to $75,000 in October? | Crypto | YES | `40.2%` | `29.0%` | `+11.2 п.п.` | `1.00%` | REJECTED: Win probability 40.2% < 55% minimum (no underdog lottery bets) |
| Will Bitcoin reach $87,500 in October? | Crypto | YES | `37.2%` | `24.0%` | `+13.2 п.п.` | `1.00%` | REJECTED: Win probability 37.2% < 55% minimum (no underdog lottery bets) |
| Will the price of Bitcoin be above $72,000 on Octo | Crypto | NO | `0.5%` | `100.0%` | `-99.5 п.п.` | `100.00%` | REJECTED: Edge -99.5 pp < 8 pp threshold (P_est=0.5% vs AskVWAP=100.0%) |
| Will Bitcoin reach $82,500 in October? | Crypto | YES | `81.5%` | `77.0%` | `+4.5 п.п.` | `1.00%` | REJECTED: Edge +4.5 pp < 8 pp threshold (P_est=81.5% vs AskVWAP=77.0%) |
| Will the price of Bitcoin be above $80,000 on Octo | Crypto | NO | `31.8%` | `26.0%` | `+5.8 п.п.` | `1.00%` | REJECTED: Edge +5.8 pp < 8 pp threshold (P_est=31.8% vs AskVWAP=26.0%) |
| Will Bitcoin reach $95,000 in October? | Crypto | YES | `8.3%` | `2.7%` | `+5.6 п.п.` | `0.28%` | REJECTED: Edge +5.6 pp < 8 pp threshold (P_est=8.3% vs AskVWAP=2.7%) |
| Will the highest temperature in Beijing be 20°C on | Weather | NO | `82.2%` | `73.0%` | `+9.2 п.п.` | `3.00%` | REJECTED: Narrow weather bracket NO bet prohibited (airport METAR microclimate tail risk) |
| Will the highest temperature in Paris be 14°C on O | Weather | NO | `76.4%` | `67.0%` | `+9.4 п.п.` | `1.00%` | REJECTED: Narrow weather bracket NO bet prohibited (airport METAR microclimate tail risk) |
| Will the highest temperature in Wuhan be 17°C on O | Weather | NO | `85.6%` | `44.0%` | `+41.6 п.п.` | `2.00%` | REJECTED: Narrow weather bracket NO bet prohibited (airport METAR microclimate tail risk) |
| Will Bitcoin reach $92,500 in October? | Crypto | YES | `15.2%` | `7.0%` | `+8.2 п.п.` | `1.00%` | REJECTED: Win probability 15.2% < 55% minimum (no underdog lottery bets) |
