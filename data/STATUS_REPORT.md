# 📊 Отчёт симулятора Polymarket (Устав Grok Bot — Демо-счёт)
**Обновлено:** `2026-10-20 12:18:33 UTC`

## 💰 Состояние виртуального портфеля
| Показатель | Значение | Правило устава |
| :--- | :--- | :--- |
| **Стартовый капитал** | `$50.00 USDC` | Не добавлять деньги |
| **Текущий баланс (Equity)** | **`$27.87 USDC`** (`-22.13$` / `-44.26%`) | Cash + Mark-to-Market по CLOB Bid |
| **Свободный кэш / В сделках** | `$26.54` / `$1.33 USDC` | До 8 открытых позиций, макс 8% банка |
| **Цель окупаемости подписки** | `$-22.13 / $60.00` (`0.0%`) | Цель: +$60.00 в месяц |
| **Просадка от пика (Текущая / Макс)** | `0.64%` / `1.48%` (Пик: `$28.05`) | Стоп-кран при просадке 40% |
| **Закрытых сделок / Win Rate** | `34` / `23.5%` | Brier Score: `0.4280` |

## 📂 Открытые позиции (1 / 8)
| # | Рынок | Кат. | Исход | Вход (Ask VWAP) | Текущий Bid | Оценка бота | Размер ($) | Нереализ. PnL | Источник |
| :- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| #35 | Will Bitcoin dip to $80,000 in October? | Crypto | **YES** | `0.610` | `0.730` | `82.1%` | `$1.11` | `$+0.22` | Kraken BTCUSDT 1m/1h Spot Klin |

## 🔍 Последние проверенные кандидаты и фильтр стакана CLOB
| Рынок | Кат. | Сторона | Оценка бота | Цена Ask | Перекос (Edge) | Проскальзывание CLOB | Решение |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| US x Iran ceasefire continues through October 31? | Geopolitics | NO | `28.5%` | `22.0%` | `+6.5 п.п.` | `1.00%` | REJECTED: Edge +6.5 pp < 8 pp threshold (P_est=28.5% vs AskVWAP=22.0%) |
| US x Iran ceasefire continues through October 22? | Geopolitics | NO | `11.5%` | `7.3%` | `+4.1 п.п.` | `0.23%` | REJECTED: Edge +4.1 pp < 8 pp threshold (P_est=11.5% vs AskVWAP=7.3%) |
| Will the highest temperature in Lucknow be 30°C on | Weather | NO | `75.9%` | `65.0%` | `+10.9 п.п.` | `3.00%` | REJECTED: Narrow weather bracket NO bet prohibited (airport METAR microclimate tail risk) |
| Will the price of Bitcoin be above $78,000 on Octo | Crypto | NO | `12.2%` | `5.7%` | `+6.5 п.п.` | `0.40%` | REJECTED: Edge +6.5 pp < 8 pp threshold (P_est=12.2% vs AskVWAP=5.7%) |
| Will the highest temperature in Seoul (Incheon) be | Weather | NO | `73.8%` | `48.0%` | `+25.8 п.п.` | `2.00%` | REJECTED: Narrow weather bracket NO bet prohibited (airport METAR microclimate tail risk) |
| Will the price of Bitcoin be above $80,000 on Octo | Crypto | NO | `25.1%` | `17.0%` | `+8.1 п.п.` | `1.00%` | REJECTED: Win probability 25.1% < 55% minimum (no underdog lottery bets) |
| Will Bitcoin reach $84,000 on October 20? | Crypto | YES | `12.2%` | `5.0%` | `+7.2 п.п.` | `1.00%` | REJECTED: Edge +7.2 pp < 8 pp threshold (P_est=12.2% vs AskVWAP=5.0%) |
| Will Bitcoin dip to $80,000 on October 20? | Crypto | YES | `36.6%` | `20.0%` | `+16.6 п.п.` | `1.00%` | REJECTED: Win probability 36.6% < 55% minimum (no underdog lottery bets) |
| Will Bitcoin reach $92,500 in October? | Crypto | YES | `13.4%` | `5.0%` | `+8.4 п.п.` | `1.00%` | REJECTED: Win probability 13.4% < 55% minimum (no underdog lottery bets) |
| Will Bitcoin dip to $74,000 October 19-25? | Crypto | YES | `11.3%` | `4.2%` | `+7.1 п.п.` | `0.38%` | REJECTED: Edge +7.1 pp < 8 pp threshold (P_est=11.3% vs AskVWAP=4.2%) |
| Will Bitcoin dip to $79,000 on October 20? | Crypto | YES | `14.5%` | `6.6%` | `+7.9 п.п.` | `0.40%` | REJECTED: Edge +7.9 pp < 8 pp threshold (P_est=14.5% vs AskVWAP=6.6%) |
| Will Bitcoin dip to $77,500 in October? | Crypto | YES | `54.2%` | `41.0%` | `+13.2 п.п.` | `1.00%` | REJECTED: Win probability 54.2% < 55% minimum (no underdog lottery bets) |
| Will Bitcoin reach $90,000 October 19-25? | Crypto | YES | `9.4%` | `2.7%` | `+6.7 п.п.` | `0.20%` | REJECTED: Edge +6.7 pp < 8 pp threshold (P_est=9.4% vs AskVWAP=2.7%) |
| Will Bitcoin reach $90,000 in October? | Crypto | YES | `23.6%` | `13.0%` | `+10.6 п.п.` | `1.00%` | REJECTED: Win probability 23.6% < 55% minimum (no underdog lottery bets) |
| Will the price of Bitcoin be above $84,000 on Octo | Crypto | YES | `11.4%` | `6.0%` | `+5.4 п.п.` | `1.00%` | REJECTED: Edge +5.4 pp < 8 pp threshold (P_est=11.4% vs AskVWAP=6.0%) |
| Will Bitcoin reach $87,500 in October? | Crypto | YES | `38.1%` | `25.0%` | `+13.2 п.п.` | `1.00%` | REJECTED: Win probability 38.1% < 55% minimum (no underdog lottery bets) |
| US x Iran ceasefire continues through October 31? | Geopolitics | NO | `28.5%` | `22.0%` | `+6.5 п.п.` | `1.00%` | REJECTED: Edge +6.5 pp < 8 pp threshold (P_est=28.5% vs AskVWAP=22.0%) |
| Will the highest temperature in Lucknow be 30°C on | Weather | NO | `76.0%` | `65.0%` | `+11.0 п.п.` | `3.00%` | REJECTED: Narrow weather bracket NO bet prohibited (airport METAR microclimate tail risk) |
