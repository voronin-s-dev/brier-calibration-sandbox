# Graph Report - Polymarket-Sim  (2026-10-25)

## Corpus Check
- 15 files · ~36,079 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 3 file(s) not represented in the graph (top: (none) 2, .db 1)

## Summary
- 202 nodes · 506 edges · 11 communities (7 shown, 4 thin omitted)
- Extraction: 87% EXTRACTED · 13% INFERRED · 0% AMBIGUOUS · INFERRED: 64 edges (avg confidence: 0.89)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `5cd822aa`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- oracles.py
- SimDatabase
- send_telegram_alert
- trader.py
- AutoGovernor
- 🧠 Реестр авто-доработок и полуавтоматических решений (Auto-Governor)
- 📊 Отчёт симулятора Polymarket (Устав Grok Bot — Демо-счёт)
- README.md
- http_tls.py
- extract_event_key

## God Nodes (most connected - your core abstractions)
1. `SimDatabase` - 36 edges
2. `GrokCharterPaperTrader` - 26 edges
3. `AutoGovernor` - 23 edges
4. `MarketInfo` - 22 edges
5. `main()` - 18 edges
6. `TestRiskManagementV2` - 17 edges
7. `fetch_polymarket_json()` - 13 edges
8. `WeatherOracle` - 13 edges
9. `generate_reports()` - 11 edges
10. `fetch_standard_url()` - 11 edges

## Surprising Connections (you probably didn't know these)
- `AutoGovernor` --uses--> `SimDatabase`  [INFERRED]
  auto_governor.py → database.py
- `AutoGovernor` --uses--> `MarketInfo`  [INFERRED]
  auto_governor.py → polymarket_api.py
- `TestRiskManagementV2` --uses--> `AutoGovernor`  [INFERRED]
  tests_risk.py → auto_governor.py
- `GrokCharterPaperTrader` --uses--> `AutoGovernor`  [INFERRED]
  trader.py → auto_governor.py
- `GrokCharterPaperTrader` --uses--> `SimDatabase`  [INFERRED]
  trader.py → database.py

## Import Cycles
- None detected.

## Communities (11 total, 4 thin omitted)

### Community 0 - "oracles.py"
Cohesion: 0.09
Nodes (8): calibrate_probability(), CryptoOracle, EvaluationResult, HighConvictionFactOracle, NewsAndOrderbookOracle, norm_cdf(), MarketInfo, GrokCharterPaperTrader

### Community 1 - "SimDatabase"
Cohesion: 0.13
Nodes (4): generate_reports(), SimDatabase, print_console_summary(), TestRiskManagementV2

### Community 2 - "send_telegram_alert"
Cohesion: 0.18
Nodes (3): git_sync_snapshot(), load_token_from_env(), trigger_workflow()

### Community 3 - "trader.py"
Cohesion: 0.09
Nodes (14): classify_market_category(), extract_resolution_source(), fetch_active_markets(), fetch_clob_book(), fetch_market_by_id(), OrderBookSimulation, parse_market_dict(), simulate_clob_buy_and_exit_check() (+6 more)

### Community 4 - "AutoGovernor"
Cohesion: 0.16
Nodes (3): AutoGovernor, WeatherOracle, main()

### Community 6 - "🧠 Реестр авто-доработок и полуавтоматических решений (Auto-Governor)"
Cohesion: 0.40
Nodes (4): 🛠️ История применённых авто-фиксов и одобренных правок (1), 🟡 Ожидают твоего решения (Полуавтоматический режим: 0), 🧠 Реестр авто-доработок и полуавтоматических решений (Auto-Governor), ⚙️ Текущие активные параметры риск-менеджмента

### Community 7 - "📊 Отчёт симулятора Polymarket (Устав Grok Bot — Демо-счёт)"
Cohesion: 0.40
Nodes (4): 📂 Открытые позиции (7 / 8), 📊 Отчёт симулятора Polymarket (Устав Grok Bot — Демо-счёт), 🔍 Последние проверенные кандидаты и фильтр стакана CLOB, 💰 Состояние виртуального портфеля

## Knowledge Gaps
- **4 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `SimDatabase` connect `SimDatabase` to `oracles.py`, `send_telegram_alert`, `trader.py`, `AutoGovernor`?**
  _High betweenness centrality (0.186) - this node is a cross-community bridge._
- **Are the 5 inferred relationships involving `SimDatabase` (e.g. with `AutoGovernor` and `generate_reports()`) actually correct?**
  _`SimDatabase` has 5 INFERRED edges - model-reasoned connections that need verification._
- **Should `oracles.py` be split into smaller, more focused modules?**
  _Cohesion score 0.08773784355179703 - nodes in this community are weakly interconnected._
- **Why does `GrokCharterPaperTrader` connect `oracles.py` to `SimDatabase`, `send_telegram_alert`, `trader.py`, `AutoGovernor`, `.compute_kelly_sizing`?**
  _High betweenness centrality (0.100) - this node is a cross-community bridge._
- **Are the 11 inferred relationships involving `GrokCharterPaperTrader` (e.g. with `print_console_summary()` and `TestRiskManagementV2`) actually correct?**
  _`GrokCharterPaperTrader` has 11 INFERRED edges - model-reasoned connections that need verification._
- **Should `SimDatabase` be split into smaller, more focused modules?**
  _Cohesion score 0.12550607287449392 - nodes in this community are weakly interconnected._
- **Why does `AutoGovernor` connect `AutoGovernor` to `oracles.py`, `SimDatabase`, `send_telegram_alert`, `trader.py`?**
  _High betweenness centrality (0.100) - this node is a cross-community bridge._