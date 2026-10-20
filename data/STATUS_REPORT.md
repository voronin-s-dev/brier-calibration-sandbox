# 📊 Отчёт симулятора Polymarket (Устав Grok Bot — Демо-счёт)
**Обновлено:** `2026-10-20 16:48:05 UTC`

## 💰 Состояние виртуального портфеля
| Показатель | Значение | Правило устава |
| :--- | :--- | :--- |
| **Стартовый капитал** | `$50.00 USDC` | Не добавлять деньги |
| **Текущий баланс (Equity)** | **`$27.52 USDC`** (`-22.48$` / `-44.95%`) | Cash + Mark-to-Market по CLOB Bid |
| **Свободный кэш / В сделках** | `$26.54` / `$0.98 USDC` | До 8 открытых позиций, макс 8% банка |
| **Цель окупаемости подписки** | `$-22.48 / $60.00` (`0.0%`) | Цель: +$60.00 в месяц |
| **Просадка от пика (Текущая / Макс)** | `1.87%` / `1.87%` (Пик: `$28.05`) | Стоп-кран при просадке 40% |
| **Закрытых сделок / Win Rate** | `34` / `23.5%` | Brier Score: `0.4280` |

## 📂 Открытые позиции (1 / 8)
| # | Рынок | Кат. | Исход | Вход (Ask VWAP) | Текущий Bid | Оценка бота | Размер ($) | Нереализ. PnL | Источник |
| :- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| #35 | Will Bitcoin dip to $80,000 in October? | Crypto | **YES** | `0.610` | `0.540` | `68.0%` | `$1.11` | `$-0.13` | Kraken BTCUSDT 1m/1h Spot Klin |

## 🔍 Последние проверенные кандидаты и фильтр стакана CLOB
| Рынок | Кат. | Сторона | Оценка бота | Цена Ask | Перекос (Edge) | Проскальзывание CLOB | Решение |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Will Bitcoin dip to $75,000 in October? | Crypto | YES | `25.0%` | `15.0%` | `+10.0 п.п.` | `1.00%` | REJECTED: Win probability 25.0% < 55% minimum (no underdog lottery bets) |
| Will the highest temperature in New York City be b | Weather | YES | `25.0%` | `14.4%` | `+10.6 п.п.` | `2.42%` | REJECTED: Win probability 25.0% < 55% minimum (no underdog lottery bets) |
| Will Bitcoin reach $88,000 October 19-25? | Crypto | YES | `25.8%` | `10.0%` | `+15.8 п.п.` | `1.60%` | REJECTED: Win probability 25.8% < 55% minimum (no underdog lottery bets) |
| Will the highest temperature in Seoul (Incheon) be | Weather | YES | `7.7%` | `2.0%` | `+5.7 п.п.` | `1.05%` | REJECTED: Edge +5.7 pp < 8 pp threshold (P_est=7.7% vs AskVWAP=2.0%) |
| Will the highest temperature in Seoul (Incheon) be | Weather | NO | `67.5%` | `24.0%` | `+43.5 п.п.` | `10.00%` | REJECTED: Narrow weather bracket NO bet prohibited (airport METAR microclimate tail risk) |
| Will the highest temperature in Istanbul be 15°C o | Weather | NO | `86.1%` | `44.1%` | `+41.9 п.п.` | `6.10%` | REJECTED: CLOB round-trip slippage 6.10% > 2.0% limit |
| Will Bitcoin reach $95,000 in October? | Crypto | YES | `10.2%` | `3.3%` | `+6.9 п.п.` | `0.50%` | REJECTED: Edge +6.9 pp < 8 pp threshold (P_est=10.2% vs AskVWAP=3.3%) |
| Will Ethereum reach $2,800 in October? | Crypto | YES | `20.4%` | `15.0%` | `+5.4 п.п.` | `1.00%` | REJECTED: Edge +5.4 pp < 8 pp threshold (P_est=20.4% vs AskVWAP=15.0%) |
| Will the highest temperature in Chengdu be 20°C on | Weather | YES | `21.9%` | `6.2%` | `+15.7 п.п.` | `3.08%` | REJECTED: Win probability 21.9% < 55% minimum (no underdog lottery bets) |
| Will Bitcoin reach $84,000 October 19-25? | Crypto | YES | `75.1%` | `69.0%` | `+6.1 п.п.` | `2.00%` | REJECTED: Edge +6.1 pp < 8 pp threshold (P_est=75.1% vs AskVWAP=69.0%) |
| Will Bitcoin reach $92,500 in October? | Crypto | YES | `18.1%` | `8.0%` | `+10.1 п.п.` | `1.00%` | REJECTED: Win probability 18.1% < 55% minimum (no underdog lottery bets) |
| Will Ethereum dip to $2,300 in October? | Crypto | YES | `53.3%` | `43.0%` | `+10.3 п.п.` | `1.00%` | REJECTED: Win probability 53.3% < 55% minimum (no underdog lottery bets) |
| Will Bitcoin reach $92,000 October 19-25? | Crypto | YES | `7.2%` | `1.9%` | `+5.3 п.п.` | `0.30%` | REJECTED: Edge +5.3 pp < 8 pp threshold (P_est=7.2% vs AskVWAP=1.9%) |
| Will Bitcoin dip to $77,500 in October? | Crypto | YES | `42.7%` | `28.0%` | `+14.7 п.п.` | `1.00%` | REJECTED: Win probability 42.7% < 55% minimum (no underdog lottery bets) |
| Will Bitcoin dip to $76,000 October 19-25? | Crypto | YES | `14.9%` | `4.9%` | `+10.0 п.п.` | `0.20%` | REJECTED: Win probability 14.9% < 55% minimum (no underdog lottery bets) |
| Will Bitcoin reach $90,000 in October? | Crypto | YES | `29.5%` | `16.0%` | `+13.5 п.п.` | `1.00%` | REJECTED: Win probability 29.5% < 55% minimum (no underdog lottery bets) |
| Will the price of Bitcoin be above $80,000 on Octo | Crypto | NO | `8.8%` | `2.6%` | `+6.2 п.п.` | `0.80%` | REJECTED: Edge +6.2 pp < 8 pp threshold (P_est=8.8% vs AskVWAP=2.6%) |
| Will Bitcoin dip to $74,000 October 19-25? | Crypto | YES | `6.5%` | `1.9%` | `+4.6 п.п.` | `0.10%` | REJECTED: Edge +4.6 pp < 8 pp threshold (P_est=6.5% vs AskVWAP=1.9%) |
