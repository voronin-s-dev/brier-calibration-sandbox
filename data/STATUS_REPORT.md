# 📊 Отчёт симулятора Polymarket (Устав Grok Bot — Демо-счёт)
**Обновлено:** `2026-10-20 12:00:04 UTC`

## 💰 Состояние виртуального портфеля
| Показатель | Значение | Правило устава |
| :--- | :--- | :--- |
| **Стартовый капитал** | `$50.00 USDC` | Не добавлять деньги |
| **Текущий баланс (Equity)** | **`$27.85 USDC`** (`-22.15$` / `-44.30%`) | Cash + Mark-to-Market по CLOB Bid |
| **Свободный кэш / В сделках** | `$26.54` / `$1.31 USDC` | До 8 открытых позиций, макс 8% банка |
| **Цель окупаемости подписки** | `$-22.15 / $60.00` (`0.0%`) | Цель: +$60.00 в месяц |
| **Просадка от пика (Текущая / Макс)** | `0.70%` / `1.48%` (Пик: `$28.05`) | Стоп-кран при просадке 40% |
| **Закрытых сделок / Win Rate** | `34` / `23.5%` | Brier Score: `0.4280` |

## 📂 Открытые позиции (1 / 8)
| # | Рынок | Кат. | Исход | Вход (Ask VWAP) | Текущий Bid | Оценка бота | Размер ($) | Нереализ. PnL | Источник |
| :- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| #35 | Will Bitcoin dip to $80,000 in October? | Crypto | **YES** | `0.610` | `0.720` | `81.5%` | `$1.11` | `$+0.20` | Kraken BTCUSDT 1m/1h Spot Klin |

## 🔍 Последние проверенные кандидаты и фильтр стакана CLOB
| Рынок | Кат. | Сторона | Оценка бота | Цена Ask | Перекос (Edge) | Проскальзывание CLOB | Решение |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| US x Iran ceasefire continues through October 31? | Geopolitics | NO | `28.5%` | `22.0%` | `+6.5 п.п.` | `1.00%` | REJECTED: Edge +6.5 pp < 8 pp threshold (P_est=28.5% vs AskVWAP=22.0%) |
| Will the price of Bitcoin be above $78,000 on Octo | Crypto | NO | `12.2%` | `5.8%` | `+6.4 п.п.` | `0.60%` | REJECTED: Edge +6.4 pp < 8 pp threshold (P_est=12.2% vs AskVWAP=5.8%) |
| Will the highest temperature in Seoul (Incheon) be | Weather | NO | `74.1%` | `48.0%` | `+26.1 п.п.` | `2.00%` | REJECTED: Narrow weather bracket NO bet prohibited (airport METAR microclimate tail risk) |
| Will the price of Bitcoin be above $80,000 on Octo | Crypto | NO | `24.6%` | `15.0%` | `+9.6 п.п.` | `1.00%` | REJECTED: Win probability 24.6% < 55% minimum (no underdog lottery bets) |
| Will Bitcoin reach $84,000 on October 20? | Crypto | YES | `12.7%` | `6.0%` | `+6.7 п.п.` | `2.00%` | REJECTED: Edge +6.7 pp < 8 pp threshold (P_est=12.7% vs AskVWAP=6.0%) |
| Will the highest temperature in New York City be b | Weather | NO | `83.6%` | `78.0%` | `+5.6 п.п.` | `1.00%` | REJECTED: Edge +5.6 pp < 8 pp threshold (P_est=83.6% vs AskVWAP=78.0%) |
| Will Bitcoin dip to $80,000 on October 20? | Crypto | YES | `36.0%` | `20.0%` | `+16.1 п.п.` | `1.04%` | REJECTED: Win probability 36.0% < 55% minimum (no underdog lottery bets) |
| Will Bitcoin reach $92,500 in October? | Crypto | YES | `13.4%` | `5.0%` | `+8.4 п.п.` | `1.00%` | REJECTED: Win probability 13.4% < 55% minimum (no underdog lottery bets) |
| Will Bitcoin dip to $74,000 October 19-25? | Crypto | YES | `11.3%` | `4.3%` | `+7.1 п.п.` | `0.58%` | REJECTED: Edge +7.1 pp < 8 pp threshold (P_est=11.3% vs AskVWAP=4.3%) |
| Will Bitcoin dip to $79,000 on October 20? | Crypto | YES | `14.1%` | `6.4%` | `+7.7 п.п.` | `0.30%` | REJECTED: Edge +7.7 pp < 8 pp threshold (P_est=14.1% vs AskVWAP=6.4%) |
| Will Bitcoin dip to $77,500 in October? | Crypto | YES | `53.9%` | `40.0%` | `+13.9 п.п.` | `1.00%` | REJECTED: Win probability 53.9% < 55% minimum (no underdog lottery bets) |
| Will Bitcoin reach $90,000 October 19-25? | Crypto | YES | `9.5%` | `3.4%` | `+6.1 п.п.` | `1.39%` | REJECTED: Edge +6.1 pp < 8 pp threshold (P_est=9.5% vs AskVWAP=3.4%) |
| Will Bitcoin reach $90,000 in October? | Crypto | YES | `23.6%` | `13.0%` | `+10.6 п.п.` | `1.00%` | REJECTED: Win probability 23.6% < 55% minimum (no underdog lottery bets) |
| Will the price of Bitcoin be above $84,000 on Octo | Crypto | YES | `11.8%` | `7.0%` | `+4.8 п.п.` | `1.00%` | REJECTED: Edge +4.8 pp < 8 pp threshold (P_est=11.8% vs AskVWAP=7.0%) |
| Will Bitcoin reach $87,500 in October? | Crypto | YES | `38.2%` | `25.0%` | `+13.2 п.п.` | `1.00%` | REJECTED: Win probability 38.2% < 55% minimum (no underdog lottery bets) |
| US x Iran ceasefire continues through October 22? | Geopolitics | NO | `17.6%` | `8.3%` | `+9.3 п.п.` | `0.80%` | REJECTED: Win probability 17.6% < 55% minimum (no underdog lottery bets) |
| Will the highest temperature in New York City be b | Weather | NO | `79.3%` | `59.0%` | `+20.3 п.п.` | `2.00%` | REJECTED: Narrow weather bracket NO bet prohibited (airport METAR microclimate tail risk) |
| Will the price of Bitcoin be above $78,000 on Octo | Crypto | NO | `15.0%` | `8.0%` | `+7.0 п.п.` | `3.00%` | REJECTED: Edge +7.0 pp < 8 pp threshold (P_est=15.0% vs AskVWAP=8.0%) |
