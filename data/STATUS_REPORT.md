# 📊 Отчёт симулятора Polymarket (Устав Grok Bot — Демо-счёт)
**Обновлено:** `2026-10-18 18:18:24 UTC`

## 💰 Состояние виртуального портфеля
| Показатель | Значение | Правило устава |
| :--- | :--- | :--- |
| **Стартовый капитал** | `$50.00 USDC` | Не добавлять деньги |
| **Текущий баланс (Equity)** | **`$27.98 USDC`** (`-22.02$` / `-44.04%`) | Cash + Mark-to-Market по CLOB Bid |
| **Свободный кэш / В сделках** | `$26.91` / `$1.07 USDC` | До 8 открытых позиций, макс 8% банка |
| **Цель окупаемости подписки** | `$-22.02 / $60.00` (`0.0%`) | Цель: +$60.00 в месяц |
| **Просадка от пика (Текущая / Макс)** | `0.17%` / `0.17%` (Пик: `$28.03`) | Стоп-кран при просадке 40% |
| **Закрытых сделок / Win Rate** | `33` / `24.2%` | Brier Score: `0.4280` |

## 📂 Открытые позиции (1 / 8)
| # | Рынок | Кат. | Исход | Вход (Ask VWAP) | Текущий Bid | Оценка бота | Размер ($) | Нереализ. PnL | Источник |
| :- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| #34 | Will Bitcoin dip to $77,500 in October? | Crypto | **YES** | `0.480` | `0.460` | `59.6%` | `$1.12` | `$-0.05` | Binance BTCUSDT 1m/1h Spot Kli |

## 🔍 Последние проверенные кандидаты и фильтр стакана CLOB
| Рынок | Кат. | Сторона | Оценка бота | Цена Ask | Перекос (Edge) | Проскальзывание CLOB | Решение |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Will the highest temperature in Beijing be 20°C on | Weather | NO | `82.2%` | `73.0%` | `+9.2 п.п.` | `3.00%` | REJECTED: Narrow weather bracket NO bet prohibited (airport METAR microclimate tail risk) |
| Will the highest temperature in Paris be 14°C on O | Weather | NO | `76.4%` | `67.0%` | `+9.4 п.п.` | `1.00%` | REJECTED: Narrow weather bracket NO bet prohibited (airport METAR microclimate tail risk) |
| Will the highest temperature in Wuhan be 17°C on O | Weather | NO | `85.6%` | `44.0%` | `+41.6 п.п.` | `2.00%` | REJECTED: Narrow weather bracket NO bet prohibited (airport METAR microclimate tail risk) |
| Will Bitcoin reach $92,500 in October? | Crypto | YES | `15.2%` | `7.0%` | `+8.2 п.п.` | `1.00%` | REJECTED: Win probability 15.2% < 55% minimum (no underdog lottery bets) |
| Will the price of Bitcoin be above $84,000 on Octo | Crypto | YES | `14.8%` | `10.0%` | `+4.8 п.п.` | `1.00%` | REJECTED: Edge +4.8 pp < 8 pp threshold (P_est=14.8% vs AskVWAP=10.0%) |
| Will Bitcoin dip to $80,000 in October? | Crypto | YES | `86.4%` | `81.0%` | `+5.3 п.п.` | `1.00%` | REJECTED: Edge +5.3 pp < 8 pp threshold (P_est=86.4% vs AskVWAP=81.0%) |
| Will Ethereum reach $2,600 in October? | Crypto | YES | `40.6%` | `34.0%` | `+6.6 п.п.` | `2.00%` | REJECTED: Edge +6.6 pp < 8 pp threshold (P_est=40.6% vs AskVWAP=34.0%) |
| Will the price of Bitcoin be above $86,000 on Octo | Crypto | YES | `13.1%` | `7.0%` | `+6.1 п.п.` | `2.00%` | REJECTED: Edge +6.1 pp < 8 pp threshold (P_est=13.1% vs AskVWAP=7.0%) |
| Will Ethereum dip to $2,200 in October? | Crypto | YES | `51.7%` | `47.0%` | `+4.7 п.п.` | `1.00%` | REJECTED: Edge +4.7 pp < 8 pp threshold (P_est=51.7% vs AskVWAP=47.0%) |
| Will Bitcoin dip to $75,000 in October? | Crypto | YES | `38.2%` | `26.0%` | `+12.2 п.п.` | `1.00%` | REJECTED: Win probability 38.2% < 55% minimum (no underdog lottery bets) |
| Will Bitcoin reach $90,000 in October? | Crypto | YES | `25.3%` | `15.0%` | `+10.3 п.п.` | `1.00%` | REJECTED: Win probability 25.3% < 55% minimum (no underdog lottery bets) |
| Will Bitcoin reach $87,500 in October? | Crypto | YES | `39.1%` | `26.0%` | `+13.1 п.п.` | `1.00%` | REJECTED: Win probability 39.1% < 55% minimum (no underdog lottery bets) |
| Will the price of Bitcoin be above $72,000 on Octo | Crypto | NO | `0.5%` | `100.0%` | `-99.5 п.п.` | `100.00%` | REJECTED: Edge -99.5 pp < 8 pp threshold (P_est=0.5% vs AskVWAP=100.0%) |
| Will the price of Bitcoin be above $80,000 on Octo | Crypto | NO | `27.6%` | `22.0%` | `+5.6 п.п.` | `1.00%` | REJECTED: Edge +5.6 pp < 8 pp threshold (P_est=27.6% vs AskVWAP=22.0%) |
| Will Bitcoin reach $95,000 in October? | Crypto | YES | `9.0%` | `2.7%` | `+6.3 п.п.` | `0.20%` | REJECTED: Edge +6.3 pp < 8 pp threshold (P_est=9.0% vs AskVWAP=2.7%) |
| Will the highest temperature in Paris be 14°C on O | Weather | NO | `76.4%` | `67.0%` | `+9.4 п.п.` | `1.00%` | REJECTED: Narrow weather bracket NO bet prohibited (airport METAR microclimate tail risk) |
| Will the highest temperature in Wuhan be 17°C on O | Weather | NO | `85.6%` | `44.0%` | `+41.6 п.п.` | `2.00%` | REJECTED: Narrow weather bracket NO bet prohibited (airport METAR microclimate tail risk) |
| Will Bitcoin reach $92,500 in October? | Crypto | YES | `15.2%` | `7.0%` | `+8.2 п.п.` | `1.00%` | REJECTED: Win probability 15.2% < 55% minimum (no underdog lottery bets) |
