# 📊 Отчёт симулятора Polymarket (Устав Grok Bot — Демо-счёт)
**Обновлено:** `2026-10-20 17:06:22 UTC`

## 💰 Состояние виртуального портфеля
| Показатель | Значение | Правило устава |
| :--- | :--- | :--- |
| **Стартовый капитал** | `$50.00 USDC` | Не добавлять деньги |
| **Текущий баланс (Equity)** | **`$27.52 USDC`** (`-22.48$` / `-44.95%`) | Cash + Mark-to-Market по CLOB Bid |
| **Свободный кэш / В сделках** | `$26.54` / `$0.98 USDC` | До 8 открытых позиций, макс 8% банка |
| **Цель окупаемости подписки** | `$-22.48 / $60.00` (`0.0%`) | Цель: +$60.00 в месяц |
| **Просадка от пика (Текущая / Макс)** | `1.87%` / `1.93%` (Пик: `$28.05`) | Стоп-кран при просадке 40% |
| **Закрытых сделок / Win Rate** | `34` / `23.5%` | Brier Score: `0.4280` |

## 📂 Открытые позиции (1 / 8)
| # | Рынок | Кат. | Исход | Вход (Ask VWAP) | Текущий Bid | Оценка бота | Размер ($) | Нереализ. PnL | Источник |
| :- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| #35 | Will Bitcoin dip to $80,000 in October? | Crypto | **YES** | `0.610` | `0.540` | `67.3%` | `$1.11` | `$-0.13` | Kraken BTCUSDT 1m/1h Spot Klin |

## 🔍 Последние проверенные кандидаты и фильтр стакана CLOB
| Рынок | Кат. | Сторона | Оценка бота | Цена Ask | Перекос (Edge) | Проскальзывание CLOB | Решение |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| US x Iran ceasefire continues through October 22? | Geopolitics | NO | `10.2%` | `5.8%` | `+4.4 п.п.` | `0.40%` | REJECTED: Edge +4.4 pp < 8 pp threshold (P_est=10.2% vs AskVWAP=5.8%) |
| Will the highest temperature in Seoul (Incheon) be | Weather | YES | `23.0%` | `12.0%` | `+11.0 п.п.` | `3.00%` | REJECTED: Win probability 23.0% < 55% minimum (no underdog lottery bets) |
| Will Bitcoin dip to $75,000 in October? | Crypto | YES | `24.7%` | `14.0%` | `+10.7 п.п.` | `1.00%` | REJECTED: Win probability 24.7% < 55% minimum (no underdog lottery bets) |
| Will Bitcoin reach $88,000 October 19-25? | Crypto | YES | `25.8%` | `10.0%` | `+15.8 п.п.` | `1.00%` | REJECTED: Win probability 25.8% < 55% minimum (no underdog lottery bets) |
| Will the highest temperature in New York City be b | Weather | YES | `25.0%` | `14.4%` | `+10.6 п.п.` | `2.42%` | REJECTED: Win probability 25.0% < 55% minimum (no underdog lottery bets) |
| Will the price of Bitcoin be above $90,000 on Octo | Crypto | YES | `2.0%` | `100.0%` | `-98.0 п.п.` | `100.00%` | REJECTED: Edge -98.0 pp < 8 pp threshold (P_est=2.0% vs AskVWAP=100.0%) |
| Will the price of Bitcoin be above $84,000 on Octo | Crypto | YES | `30.4%` | `25.0%` | `+5.4 п.п.` | `1.00%` | REJECTED: Edge +5.4 pp < 8 pp threshold (P_est=30.4% vs AskVWAP=25.0%) |
| Will the price of Bitcoin be above $80,000 on Octo | Crypto | NO | `16.4%` | `7.0%` | `+9.4 п.п.` | `1.00%` | REJECTED: Win probability 16.4% < 55% minimum (no underdog lottery bets) |
| Will the highest temperature in Istanbul be 15°C o | Weather | NO | `87.8%` | `43.7%` | `+44.1 п.п.` | `11.10%` | REJECTED: CLOB round-trip slippage 11.10% > 2.0% limit |
| Will the highest temperature in Seoul (Incheon) be | Weather | YES | `7.7%` | `3.6%` | `+4.1 п.п.` | `2.30%` | REJECTED: Edge +4.1 pp < 8 pp threshold (P_est=7.7% vs AskVWAP=3.6%) |
| Will the price of Ethereum be above $2,500 on Octo | Crypto | YES | `22.8%` | `18.0%` | `+4.8 п.п.` | `2.00%` | REJECTED: Edge +4.8 pp < 8 pp threshold (P_est=22.8% vs AskVWAP=18.0%) |
| Will Ethereum reach $2,800 in October? | Crypto | YES | `20.5%` | `15.0%` | `+5.5 п.п.` | `1.00%` | REJECTED: Edge +5.5 pp < 8 pp threshold (P_est=20.5% vs AskVWAP=15.0%) |
| Will Bitcoin reach $95,000 in October? | Crypto | YES | `10.2%` | `3.1%` | `+7.1 п.п.` | `0.10%` | REJECTED: Edge +7.1 pp < 8 pp threshold (P_est=10.2% vs AskVWAP=3.1%) |
| Will the highest temperature in Chengdu be 20°C on | Weather | YES | `21.7%` | `4.8%` | `+17.0 п.п.` | `2.68%` | REJECTED: Win probability 21.7% < 55% minimum (no underdog lottery bets) |
| Will Bitcoin reach $84,000 October 19-25? | Crypto | YES | `75.7%` | `68.0%` | `+7.7 п.п.` | `1.00%` | REJECTED: Edge +7.7 pp < 8 pp threshold (P_est=75.7% vs AskVWAP=68.0%) |
| Will the price of Bitcoin be above $78,000 on Octo | Crypto | NO | `5.3%` | `1.3%` | `+4.0 п.п.` | `0.30%` | REJECTED: Edge +4.0 pp < 8 pp threshold (P_est=5.3% vs AskVWAP=1.3%) |
| Will Bitcoin reach $92,500 in October? | Crypto | YES | `18.0%` | `8.0%` | `+10.0 п.п.` | `1.00%` | REJECTED: Win probability 18.0% < 55% minimum (no underdog lottery bets) |
| Will Ethereum dip to $2,300 in October? | Crypto | YES | `53.0%` | `44.0%` | `+9.0 п.п.` | `1.00%` | REJECTED: Win probability 53.0% < 55% minimum (no underdog lottery bets) |
