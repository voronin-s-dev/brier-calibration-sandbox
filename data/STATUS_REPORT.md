# 📊 Отчёт симулятора Polymarket (Устав Grok Bot — Демо-счёт)
**Обновлено:** `2026-10-19 11:19:07 UTC`

## 💰 Состояние виртуального портфеля
| Показатель | Значение | Правило устава |
| :--- | :--- | :--- |
| **Стартовый капитал** | `$50.00 USDC` | Не добавлять деньги |
| **Текущий баланс (Equity)** | **`$27.74 USDC`** (`-22.26$` / `-44.51%`) | Cash + Mark-to-Market по CLOB Bid |
| **Свободный кэш / В сделках** | `$26.54` / `$1.20 USDC` | До 8 открытых позиций, макс 8% банка |
| **Цель окупаемости подписки** | `$-22.26 / $60.00` (`0.0%`) | Цель: +$60.00 в месяц |
| **Просадка от пика (Текущая / Макс)** | `1.09%` / `1.48%` (Пик: `$28.05`) | Стоп-кран при просадке 40% |
| **Закрытых сделок / Win Rate** | `34` / `23.5%` | Brier Score: `0.4280` |

## 📂 Открытые позиции (1 / 8)
| # | Рынок | Кат. | Исход | Вход (Ask VWAP) | Текущий Bid | Оценка бота | Размер ($) | Нереализ. PnL | Источник |
| :- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| #35 | Will Bitcoin dip to $80,000 in October? | Crypto | **YES** | `0.610` | `0.660` | `74.2%` | `$1.11` | `$+0.09` | Kraken BTCUSDT 1m/1h Spot Klin |

## 🔍 Последние проверенные кандидаты и фильтр стакана CLOB
| Рынок | Кат. | Сторона | Оценка бота | Цена Ask | Перекос (Edge) | Проскальзывание CLOB | Решение |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Will Ethereum reach $2,600 in October? | Crypto | YES | `50.5%` | `43.0%` | `+7.5 п.п.` | `1.00%` | REJECTED: Edge +7.5 pp < 8 pp threshold (P_est=50.5% vs AskVWAP=43.0%) |
| Will the price of Bitcoin be above $88,000 on Octo | Crypto | YES | `9.0%` | `4.9%` | `+4.1 п.п.` | `0.30%` | REJECTED: Edge +4.1 pp < 8 pp threshold (P_est=9.0% vs AskVWAP=4.9%) |
| Will the price of Bitcoin be above $80,000 on Octo | Crypto | NO | `21.6%` | `13.0%` | `+8.6 п.п.` | `1.00%` | REJECTED: Win probability 21.6% < 55% minimum (no underdog lottery bets) |
| Will Ethereum dip to $2,350 on October 19? | Crypto | YES | `25.6%` | `21.0%` | `+4.6 п.п.` | `3.00%` | REJECTED: Edge +4.6 pp < 8 pp threshold (P_est=25.6% vs AskVWAP=21.0%) |
| Will Ethereum dip to $2,200 in October? | Crypto | YES | `38.4%` | `32.0%` | `+6.4 п.п.` | `1.00%` | REJECTED: Edge +6.4 pp < 8 pp threshold (P_est=38.4% vs AskVWAP=32.0%) |
| Will the price of Bitcoin be above $84,000 on Octo | Crypto | YES | `20.4%` | `13.0%` | `+7.4 п.п.` | `1.00%` | REJECTED: Edge +7.4 pp < 8 pp threshold (P_est=20.4% vs AskVWAP=13.0%) |
| Will Solana dip to $100 in October? | Crypto | YES | `72.3%` | `68.0%` | `+4.3 п.п.` | `3.00%` | REJECTED: Edge +4.3 pp < 8 pp threshold (P_est=72.3% vs AskVWAP=68.0%) |
| Will Bitcoin reach $85,000 on October 19? | Crypto | YES | `11.5%` | `3.3%` | `+8.2 п.п.` | `0.30%` | REJECTED: Win probability 11.5% < 55% minimum (no underdog lottery bets) |
| Will the price of Bitcoin be above $78,000 on Octo | Crypto | NO | `8.0%` | `3.8%` | `+4.2 п.п.` | `0.20%` | REJECTED: Edge +4.2 pp < 8 pp threshold (P_est=8.0% vs AskVWAP=3.8%) |
| Will Bitcoin reach $90,000 in October? | Crypto | YES | `30.8%` | `20.0%` | `+10.8 п.п.` | `1.00%` | REJECTED: Win probability 30.8% < 55% minimum (no underdog lottery bets) |
| Will the price of Bitcoin be above $86,000 on Octo | Crypto | YES | `17.2%` | `11.0%` | `+6.2 п.п.` | `3.00%` | REJECTED: Edge +6.2 pp < 8 pp threshold (P_est=17.2% vs AskVWAP=11.0%) |
| Will Bitcoin reach $92,500 in October? | Crypto | YES | `18.9%` | `10.0%` | `+8.9 п.п.` | `1.00%` | REJECTED: Win probability 18.9% < 55% minimum (no underdog lottery bets) |
| Will the price of Ethereum be above $2,500 on Octo | Crypto | YES | `22.4%` | `18.0%` | `+4.5 п.п.` | `2.00%` | REJECTED: Edge +4.5 pp < 8 pp threshold (P_est=22.4% vs AskVWAP=18.0%) |
| Will the price of Bitcoin be above $80,000 on Octo | Crypto | NO | `15.2%` | `8.6%` | `+6.6 п.п.` | `0.80%` | REJECTED: Edge +6.6 pp < 8 pp threshold (P_est=15.2% vs AskVWAP=8.6%) |
| Will Bitcoin reach $87,500 in October? | Crypto | YES | `46.6%` | `33.0%` | `+13.6 п.п.` | `1.00%` | REJECTED: Win probability 46.6% < 55% minimum (no underdog lottery bets) |
| Will Bitcoin reach $85,000 in October? | Crypto | YES | `69.2%` | `60.0%` | `+9.2 п.п.` | `2.00%` | REJECTED: Duplicate underlying event (crypto:bitcoin:nodate) |
| Will Bitcoin dip to $81,000 on October 19? | Crypto | YES | `44.2%` | `29.0%` | `+15.2 п.п.` | `1.00%` | REJECTED: Win probability 44.2% < 55% minimum (no underdog lottery bets) |
| Will Bitcoin reach $95,000 in October? | Crypto | YES | `11.1%` | `4.4%` | `+6.7 п.п.` | `0.10%` | REJECTED: Edge +6.7 pp < 8 pp threshold (P_est=11.1% vs AskVWAP=4.4%) |
