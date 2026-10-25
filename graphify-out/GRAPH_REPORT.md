# Graph Report - Polymarket-Sim  (2026-10-25)

## Corpus Check
- 15 files · ~35,585 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 3 file(s) not represented in the graph (top: (none) 2, .db 1)

## Summary
- 196 nodes · 492 edges · 9 communities (8 shown, 1 thin omitted)
- Extraction: 87% EXTRACTED · 13% INFERRED · 0% AMBIGUOUS · INFERRED: 64 edges (avg confidence: 0.89)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `cd42b26f`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- oracles.py
- SimDatabase
- send_telegram_alert
- trader.py
- AutoGovernor
- GrokCharterPaperTrader
- 🧠 Реестр авто-доработок и полуавтоматических решений (Auto-Governor)
- 📊 Отчёт симулятора Polymarket (Устав Grok Bot — Демо-счёт)
- README.md

## God Nodes (most connected - your core abstractions)
1. `SimDatabase` - 36 edges
2. `GrokCharterPaperTrader` - 26 edges
3. `AutoGovernor` - 23 edges
4. `MarketInfo` - 22 edges
5. `main()` - 18 edges
6. `TestRiskManagementV2` - 17 edges
7. `fetch_polymarket_json()` - 13 edges
8. `WeatherOracle` - 13 edges
9. `send_telegram_alert()` - 12 edges
10. `generate_reports()` - 11 edges

## Surprising Connections (you probably didn't know these)
- `AutoGovernor` --uses--> `SimDatabase`  [INFERRED]
  auto_governor.py → database.py
- `AutoGovernor` --uses--> `WeatherOracle`  [INFERRED]
  auto_governor.py → oracles.py
- `AutoGovernor` --uses--> `MarketInfo`  [INFERRED]
  auto_governor.py → polymarket_api.py
- `TestRiskManagementV2` --uses--> `AutoGovernor`  [INFERRED]
  tests_risk.py → auto_governor.py
- `GrokCharterPaperTrader` --uses--> `AutoGovernor`  [INFERRED]
  trader.py → auto_governor.py

## Import Cycles
- None detected.

## Communities (9 total, 1 thin omitted)

### Community 0 - "oracles.py"
Cohesion: 0.11
Nodes (6): calibrate_probability(), CryptoOracle, EvaluationResult, NewsAndOrderbookOracle, norm_cdf(), MarketInfo

### Community 1 - "SimDatabase"
Cohesion: 0.13
Nodes (4): generate_reports(), SimDatabase, print_console_summary(), TestRiskManagementV2

### Community 2 - "send_telegram_alert"
Cohesion: 0.21
Nodes (4): _load_env_fallback(), send_telegram_alert(), load_token_from_env(), trigger_workflow()

### Community 3 - "trader.py"
Cohesion: 0.09
Nodes (11): fetch_polymarket_json(), fetch_standard_url(), classify_market_category(), extract_resolution_source(), fetch_active_markets(), fetch_clob_book(), fetch_market_by_id(), OrderBookSimulation (+3 more)

### Community 4 - "AutoGovernor"
Cohesion: 0.17
Nodes (3): AutoGovernor, git_sync_snapshot(), main()

### Community 5 - "GrokCharterPaperTrader"
Cohesion: 0.10
Nodes (4): HighConvictionFactOracle, WeatherOracle, extract_event_key(), GrokCharterPaperTrader

### Community 6 - "🧠 Реестр авто-доработок и полуавтоматических решений (Auto-Governor)"
Cohesion: 0.40
Nodes (4): 🛠️ История применённых авто-фиксов и одобренных правок (1), 🟡 Ожидают твоего решения (Полуавтоматический режим: 0), 🧠 Реестр авто-доработок и полуавтоматических решений (Auto-Governor), ⚙️ Текущие активные параметры риск-менеджмента

### Community 7 - "📊 Отчёт симулятора Polymarket (Устав Grok Bot — Демо-счёт)"
Cohesion: 0.40
Nodes (4): 📂 Открытые позиции (7 / 8), 📊 Отчёт симулятора Polymarket (Устав Grok Bot — Демо-счёт), 🔍 Последние проверенные кандидаты и фильтр стакана CLOB, 💰 Состояние виртуального портфеля

## Knowledge Gaps
- **1 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `SimDatabase` connect `SimDatabase` to `oracles.py`, `trader.py`, `AutoGovernor`, `GrokCharterPaperTrader`?**
  _High betweenness centrality (0.190) - this node is a cross-community bridge._
- **Are the 5 inferred relationships involving `SimDatabase` (e.g. with `AutoGovernor` and `generate_reports()`) actually correct?**
  _`SimDatabase` has 5 INFERRED edges - model-reasoned connections that need verification._
- **Should `oracles.py` be split into smaller, more focused modules?**
  _Cohesion score 0.1051693404634581 - nodes in this community are weakly interconnected._
- **Why does `GrokCharterPaperTrader` connect `GrokCharterPaperTrader` to `oracles.py`, `SimDatabase`, `trader.py`, `AutoGovernor`?**
  _High betweenness centrality (0.104) - this node is a cross-community bridge._
- **Are the 11 inferred relationships involving `GrokCharterPaperTrader` (e.g. with `print_console_summary()` and `TestRiskManagementV2`) actually correct?**
  _`GrokCharterPaperTrader` has 11 INFERRED edges - model-reasoned connections that need verification._
- **Should `SimDatabase` be split into smaller, more focused modules?**
  _Cohesion score 0.12550607287449392 - nodes in this community are weakly interconnected._
- **Why does `AutoGovernor` connect `AutoGovernor` to `oracles.py`, `SimDatabase`, `trader.py`, `GrokCharterPaperTrader`?**
  _High betweenness centrality (0.103) - this node is a cross-community bridge._