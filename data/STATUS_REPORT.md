# 📊 Отчёт симулятора Polymarket (Устав Grok Bot — Демо-счёт)
**Обновлено:** `2026-10-20 16:57:14 UTC`

## 💰 Состояние виртуального портфеля
| Показатель | Значение | Правило устава |
| :--- | :--- | :--- |
| **Стартовый капитал** | `$50.00 USDC` | Не добавлять деньги |
| **Текущий баланс (Equity)** | **`$27.51 USDC`** (`-22.49$` / `-44.99%`) | Cash + Mark-to-Market по CLOB Bid |
| **Свободный кэш / В сделках** | `$26.54` / `$0.96 USDC` | До 8 открытых позиций, макс 8% банка |
| **Цель окупаемости подписки** | `$-22.49 / $60.00` (`0.0%`) | Цель: +$60.00 в месяц |
| **Просадка от пика (Текущая / Макс)** | `1.93%` / `1.93%` (Пик: `$28.05`) | Стоп-кран при просадке 40% |
| **Закрытых сделок / Win Rate** | `34` / `23.5%` | Brier Score: `0.4280` |

## 📂 Открытые позиции (1 / 8)
| # | Рынок | Кат. | Исход | Вход (Ask VWAP) | Текущий Bid | Оценка бота | Размер ($) | Нереализ. PnL | Источник |
| :- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| #35 | Will Bitcoin dip to $80,000 in October? | Crypto | **YES** | `0.610` | `0.530` | `67.1%` | `$1.11` | `$-0.15` | Kraken BTCUSDT 1m/1h Spot Klin |

## 🔍 Последние проверенные кандидаты и фильтр стакана CLOB
| Рынок | Кат. | Сторона | Оценка бота | Цена Ask | Перекос (Edge) | Проскальзывание CLOB | Решение |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Will the highest temperature in Seoul (Incheon) be | Weather | YES | `23.1%` | `12.0%` | `+11.1 п.п.` | `4.00%` | REJECTED: Win probability 23.1% < 55% minimum (no underdog lottery bets) |
| Will Bitcoin dip to $75,000 in October? | Crypto | YES | `24.7%` | `14.0%` | `+10.7 п.п.` | `1.00%` | REJECTED: Win probability 24.7% < 55% minimum (no underdog lottery bets) |
| Will Bitcoin reach $88,000 October 19-25? | Crypto | YES | `25.8%` | `10.0%` | `+15.8 п.п.` | `1.00%` | REJECTED: Win probability 25.8% < 55% minimum (no underdog lottery bets) |
| Will the highest temperature in New York City be b | Weather | YES | `25.0%` | `14.4%` | `+10.6 п.п.` | `2.42%` | REJECTED: Win probability 25.0% < 55% minimum (no underdog lottery bets) |
| Will the price of Bitcoin be above $90,000 on Octo | Crypto | YES | `2.0%` | `100.0%` | `-98.0 п.п.` | `100.00%` | REJECTED: Edge -98.0 pp < 8 pp threshold (P_est=2.0% vs AskVWAP=100.0%) |
| Will the price of Bitcoin be above $84,000 on Octo | Crypto | YES | `30.9%` | `26.0%` | `+4.9 п.п.` | `1.00%` | REJECTED: Edge +4.9 pp < 8 pp threshold (P_est=30.9% vs AskVWAP=26.0%) |
| Will the price of Bitcoin be above $80,000 on Octo | Crypto | NO | `16.5%` | `7.0%` | `+9.5 п.п.` | `1.00%` | REJECTED: Win probability 16.5% < 55% minimum (no underdog lottery bets) |
| Will the highest temperature in Istanbul be 15°C o | Weather | NO | `86.7%` | `49.3%` | `+37.4 п.п.` | `15.60%` | REJECTED: CLOB round-trip slippage 15.60% > 2.0% limit |
| Will the highest temperature in Seoul (Incheon) be | Weather | YES | `7.7%` | `2.1%` | `+5.6 п.п.` | `0.96%` | REJECTED: Edge +5.6 pp < 8 pp threshold (P_est=7.7% vs AskVWAP=2.1%) |
| Will the price of Ethereum be above $2,500 on Octo | Crypto | YES | `23.2%` | `18.0%` | `+5.2 п.п.` | `1.00%` | REJECTED: Edge +5.2 pp < 8 pp threshold (P_est=23.2% vs AskVWAP=18.0%) |
| Will Ethereum reach $2,800 in October? | Crypto | YES | `20.5%` | `15.0%` | `+5.5 п.п.` | `1.00%` | REJECTED: Edge +5.5 pp < 8 pp threshold (P_est=20.5% vs AskVWAP=15.0%) |
| Will Bitcoin reach $95,000 in October? | Crypto | YES | `10.3%` | `3.0%` | `+7.3 п.п.` | `0.10%` | REJECTED: Edge +7.3 pp < 8 pp threshold (P_est=10.3% vs AskVWAP=3.0%) |
| Will the highest temperature in Chengdu be 20°C on | Weather | YES | `22.8%` | `2.2%` | `+20.6 п.п.` | `0.82%` | REJECTED: Win probability 22.8% < 55% minimum (no underdog lottery bets) |
| Will Bitcoin reach $84,000 October 19-25? | Crypto | YES | `76.6%` | `69.0%` | `+7.6 п.п.` | `1.00%` | REJECTED: Edge +7.6 pp < 8 pp threshold (P_est=76.6% vs AskVWAP=69.0%) |
| Will Bitcoin reach $92,500 in October? | Crypto | YES | `18.0%` | `8.0%` | `+10.0 п.п.` | `1.00%` | REJECTED: Win probability 18.0% < 55% minimum (no underdog lottery bets) |
| Will Ethereum dip to $2,300 in October? | Crypto | YES | `52.7%` | `44.0%` | `+8.7 п.п.` | `2.00%` | REJECTED: Win probability 52.7% < 55% minimum (no underdog lottery bets) |
| Will Bitcoin reach $92,000 October 19-25? | Crypto | YES | `7.2%` | `1.9%` | `+5.3 п.п.` | `0.40%` | REJECTED: Edge +5.3 pp < 8 pp threshold (P_est=7.2% vs AskVWAP=1.9%) |
| Will Bitcoin dip to $77,500 in October? | Crypto | YES | `42.1%` | `27.0%` | `+15.1 п.п.` | `1.00%` | REJECTED: Win probability 42.1% < 55% minimum (no underdog lottery bets) |
