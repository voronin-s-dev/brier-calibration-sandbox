# 📊 Отчёт симулятора Polymarket (Устав Grok Bot — Демо-счёт)
**Обновлено:** `2026-10-20 06:30:15 UTC`

## 💰 Состояние виртуального портфеля
| Показатель | Значение | Правило устава |
| :--- | :--- | :--- |
| **Стартовый капитал** | `$50.00 USDC` | Не добавлять деньги |
| **Текущий баланс (Equity)** | **`$27.82 USDC`** (`-22.18$` / `-44.37%`) | Cash + Mark-to-Market по CLOB Bid |
| **Свободный кэш / В сделках** | `$26.54` / `$1.27 USDC` | До 8 открытых позиций, макс 8% банка |
| **Цель окупаемости подписки** | `$-22.18 / $60.00` (`0.0%`) | Цель: +$60.00 в месяц |
| **Просадка от пика (Текущая / Макс)** | `0.83%` / `1.48%` (Пик: `$28.05`) | Стоп-кран при просадке 40% |
| **Закрытых сделок / Win Rate** | `34` / `23.5%` | Brier Score: `0.4280` |

## 📂 Открытые позиции (1 / 8)
| # | Рынок | Кат. | Исход | Вход (Ask VWAP) | Текущий Bid | Оценка бота | Размер ($) | Нереализ. PnL | Источник |
| :- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| #35 | Will Bitcoin dip to $80,000 in October? | Crypto | **YES** | `0.610` | `0.700` | `78.9%` | `$1.11` | `$+0.16` | Kraken BTCUSDT 1m/1h Spot Klin |

## 🔍 Последние проверенные кандидаты и фильтр стакана CLOB
| Рынок | Кат. | Сторона | Оценка бота | Цена Ask | Перекос (Edge) | Проскальзывание CLOB | Решение |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| US x Iran ceasefire continues through October 22? | Geopolitics | NO | `18.4%` | `8.1%` | `+10.3 п.п.` | `0.59%` | REJECTED: Win probability 18.4% < 55% minimum (no underdog lottery bets) |
| Will the price of Ethereum be above $2,300 on Octo | Crypto | NO | `13.3%` | `9.0%` | `+4.3 п.п.` | `2.00%` | REJECTED: Edge +4.3 pp < 8 pp threshold (P_est=13.3% vs AskVWAP=9.0%) |
| Will the highest temperature in New York City be b | Weather | NO | `79.5%` | `59.0%` | `+20.5 п.п.` | `2.00%` | REJECTED: Narrow weather bracket NO bet prohibited (airport METAR microclimate tail risk) |
| Will the price of Bitcoin be above $78,000 on Octo | Crypto | NO | `15.3%` | `8.0%` | `+7.3 п.п.` | `2.00%` | REJECTED: Edge +7.3 pp < 8 pp threshold (P_est=15.3% vs AskVWAP=8.0%) |
| Will Bitcoin dip to $76,000 October 19-25? | Crypto | YES | `22.6%` | `11.0%` | `+11.6 п.п.` | `1.00%` | REJECTED: Win probability 22.6% < 55% minimum (no underdog lottery bets) |
| Will the price of Bitcoin be above $78,000 on Octo | Crypto | NO | `11.4%` | `5.0%` | `+6.4 п.п.` | `0.50%` | REJECTED: Edge +6.4 pp < 8 pp threshold (P_est=11.4% vs AskVWAP=5.0%) |
| Will Bitcoin reach $85,000 in October? | Crypto | YES | `62.4%` | `52.0%` | `+10.4 п.п.` | `1.00%` | REJECTED: Duplicate underlying event (crypto:bitcoin:nodate) |
| Will the price of Bitcoin be above $76,000 on Octo | Crypto | NO | `10.7%` | `4.6%` | `+6.1 п.п.` | `1.10%` | REJECTED: Edge +6.1 pp < 8 pp threshold (P_est=10.7% vs AskVWAP=4.6%) |
| Will Bitcoin dip to $75,000 in October? | Crypto | YES | `31.8%` | `20.0%` | `+11.8 п.п.` | `1.00%` | REJECTED: Win probability 31.8% < 55% minimum (no underdog lottery bets) |
| Will Bitcoin reach $95,000 in October? | Crypto | YES | `8.5%` | `2.6%` | `+5.9 п.п.` | `0.30%` | REJECTED: Edge +5.9 pp < 8 pp threshold (P_est=8.5% vs AskVWAP=2.6%) |
| Will Bitcoin reach $92,500 in October? | Crypto | YES | `15.2%` | `7.0%` | `+8.2 п.п.` | `1.00%` | REJECTED: Win probability 15.2% < 55% minimum (no underdog lottery bets) |
| Will the price of Bitcoin be above $84,000 on Octo | Crypto | YES | `16.0%` | `10.0%` | `+6.0 п.п.` | `1.00%` | REJECTED: Edge +6.0 pp < 8 pp threshold (P_est=16.0% vs AskVWAP=10.0%) |
| Will Bitcoin dip to $77,500 in October? | Crypto | YES | `51.7%` | `38.0%` | `+13.7 п.п.` | `1.00%` | REJECTED: Win probability 51.7% < 55% minimum (no underdog lottery bets) |
| Will Bitcoin dip to $79,000 on October 20? | Crypto | YES | `15.1%` | `4.6%` | `+10.5 п.п.` | `0.60%` | REJECTED: Win probability 15.1% < 55% minimum (no underdog lottery bets) |
| Will the price of Bitcoin be above $80,000 on Octo | Crypto | NO | `22.6%` | `13.0%` | `+9.6 п.п.` | `1.00%` | REJECTED: Win probability 22.6% < 55% minimum (no underdog lottery bets) |
| Will the price of Bitcoin be above $78,000 on Octo | Crypto | NO | `6.1%` | `2.1%` | `+4.0 п.п.` | `0.40%` | REJECTED: Edge +4.0 pp < 8 pp threshold (P_est=6.1% vs AskVWAP=2.1%) |
| Will Bitcoin dip to $74,000 October 19-25? | Crypto | YES | `10.8%` | `4.4%` | `+6.4 п.п.` | `0.98%` | REJECTED: Edge +6.4 pp < 8 pp threshold (P_est=10.8% vs AskVWAP=4.4%) |
| Will Bitcoin reach $85,000 on October 20? | Crypto | YES | `9.7%` | `3.4%` | `+6.3 п.п.` | `0.50%` | REJECTED: Edge +6.3 pp < 8 pp threshold (P_est=9.7% vs AskVWAP=3.4%) |
