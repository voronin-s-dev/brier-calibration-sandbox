# 📊 Отчёт симулятора Polymarket (Устав Grok Bot — Демо-счёт)
**Обновлено:** `2026-10-20 06:48:41 UTC`

## 💰 Состояние виртуального портфеля
| Показатель | Значение | Правило устава |
| :--- | :--- | :--- |
| **Стартовый капитал** | `$50.00 USDC` | Не добавлять деньги |
| **Текущий баланс (Equity)** | **`$27.80 USDC`** (`-22.20$` / `-44.40%`) | Cash + Mark-to-Market по CLOB Bid |
| **Свободный кэш / В сделках** | `$26.54` / `$1.26 USDC` | До 8 открытых позиций, макс 8% банка |
| **Цель окупаемости подписки** | `$-22.20 / $60.00` (`0.0%`) | Цель: +$60.00 в месяц |
| **Просадка от пика (Текущая / Макс)** | `0.89%` / `1.48%` (Пик: `$28.05`) | Стоп-кран при просадке 40% |
| **Закрытых сделок / Win Rate** | `34` / `23.5%` | Brier Score: `0.4280` |

## 📂 Открытые позиции (1 / 8)
| # | Рынок | Кат. | Исход | Вход (Ask VWAP) | Текущий Bid | Оценка бота | Размер ($) | Нереализ. PnL | Источник |
| :- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| #35 | Will Bitcoin dip to $80,000 in October? | Crypto | **YES** | `0.610` | `0.690` | `78.3%` | `$1.11` | `$+0.15` | Kraken BTCUSDT 1m/1h Spot Klin |

## 🔍 Последние проверенные кандидаты и фильтр стакана CLOB
| Рынок | Кат. | Сторона | Оценка бота | Цена Ask | Перекос (Edge) | Проскальзывание CLOB | Решение |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| US x Iran ceasefire continues through October 22? | Geopolitics | NO | `17.6%` | `8.3%` | `+9.3 п.п.` | `0.80%` | REJECTED: Win probability 17.6% < 55% minimum (no underdog lottery bets) |
| Will the highest temperature in New York City be b | Weather | NO | `79.3%` | `59.0%` | `+20.3 п.п.` | `2.00%` | REJECTED: Narrow weather bracket NO bet prohibited (airport METAR microclimate tail risk) |
| Will the price of Bitcoin be above $78,000 on Octo | Crypto | NO | `15.0%` | `8.0%` | `+7.0 п.п.` | `3.00%` | REJECTED: Edge +7.0 pp < 8 pp threshold (P_est=15.0% vs AskVWAP=8.0%) |
| Will Bitcoin dip to $76,000 October 19-25? | Crypto | YES | `22.6%` | `11.0%` | `+11.6 п.п.` | `1.00%` | REJECTED: Win probability 22.6% < 55% minimum (no underdog lottery bets) |
| Will the price of Bitcoin be above $78,000 on Octo | Crypto | NO | `11.3%` | `5.0%` | `+6.3 п.п.` | `0.40%` | REJECTED: Edge +6.3 pp < 8 pp threshold (P_est=11.3% vs AskVWAP=5.0%) |
| Will Bitcoin reach $85,000 in October? | Crypto | YES | `63.0%` | `53.0%` | `+10.0 п.п.` | `2.00%` | REJECTED: Duplicate underlying event (crypto:bitcoin:nodate) |
| Will the price of Bitcoin be above $76,000 on Octo | Crypto | NO | `10.6%` | `5.2%` | `+5.4 п.п.` | `2.40%` | REJECTED: Edge +5.4 pp < 8 pp threshold (P_est=10.6% vs AskVWAP=5.2%) |
| Will Bitcoin dip to $75,000 in October? | Crypto | YES | `31.5%` | `20.0%` | `+11.5 п.п.` | `1.00%` | REJECTED: Win probability 31.5% < 55% minimum (no underdog lottery bets) |
| Will Bitcoin reach $95,000 in October? | Crypto | YES | `8.5%` | `2.5%` | `+6.0 п.п.` | `0.30%` | REJECTED: Edge +6.0 pp < 8 pp threshold (P_est=8.5% vs AskVWAP=2.5%) |
| Will Bitcoin reach $92,500 in October? | Crypto | YES | `15.2%` | `7.0%` | `+8.2 п.п.` | `1.00%` | REJECTED: Win probability 15.2% < 55% minimum (no underdog lottery bets) |
| Will the price of Bitcoin be above $84,000 on Octo | Crypto | YES | `16.1%` | `10.0%` | `+6.1 п.п.` | `1.00%` | REJECTED: Edge +6.1 pp < 8 pp threshold (P_est=16.1% vs AskVWAP=10.0%) |
| Will Bitcoin dip to $77,500 in October? | Crypto | YES | `51.7%` | `38.0%` | `+13.7 п.п.` | `1.00%` | REJECTED: Win probability 51.7% < 55% minimum (no underdog lottery bets) |
| Will Bitcoin dip to $79,000 on October 20? | Crypto | YES | `14.8%` | `4.3%` | `+10.5 п.п.` | `0.70%` | REJECTED: Win probability 14.8% < 55% minimum (no underdog lottery bets) |
| Will the price of Bitcoin be above $80,000 on Octo | Crypto | NO | `22.1%` | `12.0%` | `+10.1 п.п.` | `1.00%` | REJECTED: Win probability 22.1% < 55% minimum (no underdog lottery bets) |
| Will Bitcoin dip to $74,000 October 19-25? | Crypto | YES | `10.7%` | `4.2%` | `+6.5 п.п.` | `0.88%` | REJECTED: Edge +6.5 pp < 8 pp threshold (P_est=10.7% vs AskVWAP=4.2%) |
| Will the price of Bitcoin be above $78,000 on Octo | Crypto | NO | `6.1%` | `1.6%` | `+4.5 п.п.` | `0.50%` | REJECTED: Edge +4.5 pp < 8 pp threshold (P_est=6.1% vs AskVWAP=1.6%) |
| Will Bitcoin reach $85,000 on October 20? | Crypto | YES | `9.7%` | `3.4%` | `+6.2 п.п.` | `0.40%` | REJECTED: Edge +6.2 pp < 8 pp threshold (P_est=9.7% vs AskVWAP=3.4%) |
| Will Bitcoin reach $90,000 October 19-25? | Crypto | YES | `11.2%` | `3.9%` | `+7.3 п.п.` | `1.28%` | REJECTED: Edge +7.3 pp < 8 pp threshold (P_est=11.2% vs AskVWAP=3.9%) |
