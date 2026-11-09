# Graph Report - Polymarket-Sim  (2026-11-09)

## Corpus Check
- 28 files · ~63,360 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 6 file(s) not represented in the graph (top: (none) 4, .db 1, .ini 1)

## Summary
- 339 nodes · 878 edges · 13 communities (11 shown, 2 thin omitted)
- Extraction: 78% EXTRACTED · 22% INFERRED · 0% AMBIGUOUS · INFERRED: 192 edges (avg confidence: 0.9)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `2e81f986`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- GrokCharterPaperTrader
- SimDatabase
- CryptoOracle
- trader.py
- AutoGovernor
- Матрица проверок риск-менеджмента (tests_risk.py)
- 🧠 Реестр авто-доработок и полуавтоматических решений (Auto-Governor)
- 📊 Отчёт симулятора Polymarket (Устав Grok Bot — Демо-счёт)
- README.md
- Polymarket Simulation and Agentic Market Architecture
- http_tls.py
- .test_reports_cadence_stale_warning
- Разбор 2026-11-07: ложное утверждение об остановке симулятора из-за локального статуса

## God Nodes (most connected - your core abstractions)
1. `SimDatabase` - 62 edges
2. `GrokCharterPaperTrader` - 41 edges
3. `MarketInfo` - 32 edges
4. `AutoGovernor` - 30 edges
5. `TestRiskManagementV2` - 24 edges
6. `generate_reports()` - 22 edges
7. `EvaluationResult` - 18 edges
8. `main()` - 18 edges
9. `Task 1: Shadow Portfolio Database Schema & Access Layer` - 15 edges
10. `fetch_polymarket_json()` - 13 edges

## Surprising Connections (you probably didn't know these)
- `Лестница исправления AAR (Fix Ladder)` --references--> `AutoGovernor`  [INFERRED]
  .agents/aar/checks-map.md → auto_governor.py
- `Shadow Portfolio (Sandbox) Implementation Plan` --references--> `AutoGovernor`  [INFERRED]
  docs/superpowers/plans/2026-10-28-shadow-portfolio.md → auto_governor.py
- `3. Реализация (How)` --references--> `AutoGovernor`  [INFERRED]
  .specs/archive/2026-10-25_risk_management_v2.md → auto_governor.py
- `Global Constraints` --references--> `simulate_clob_sell_shares()`  [INFERRED]
  docs/superpowers/plans/2026-10-28-shadow-portfolio.md → polymarket_api.py
- `Task 2: Shadow Market Evaluation & Position Lifecycle in `trader.py`` --references--> `simulate_clob_sell_shares()`  [INFERRED]
  docs/superpowers/plans/2026-10-28-shadow-portfolio.md → polymarket_api.py

## Import Cycles
- None detected.

## Communities (13 total, 2 thin omitted)

### Community 0 - "GrokCharterPaperTrader"
Cohesion: 0.05
Nodes (17): Global Constraints, Shadow Portfolio (Sandbox) Implementation Plan, EvaluationResult, HighConvictionFactOracle, NewsAndOrderbookOracle, WeatherOracle, MarketInfo, simulate_clob_sell_shares() (+9 more)

### Community 1 - "SimDatabase"
Cohesion: 0.06
Nodes (12): generate_reports(), SimDatabase, Review Focus, Task 1: Shadow Portfolio Database Schema & Access Layer, Task 2: Shadow Market Evaluation & Position Lifecycle in `trader.py`, Task 4: Reporting & Dashboard Integration, Task 5: End-to-End Simulation & Verification, print_console_summary() (+4 more)

### Community 2 - "CryptoOracle"
Cohesion: 0.18
Nodes (3): calibrate_probability(), CryptoOracle, norm_cdf()

### Community 3 - "trader.py"
Cohesion: 0.07
Nodes (15): classify_market_category(), extract_resolution_source(), fetch_active_markets(), fetch_clob_book(), fetch_market_by_id(), OrderBookSimulation, parse_market_dict(), simulate_clob_buy_and_exit_check() (+7 more)

### Community 4 - "AutoGovernor"
Cohesion: 0.15
Nodes (4): AutoGovernor, Task 3: Auto-Governor Tier 2 Shadow Category Unfreeze Rule, git_sync_snapshot(), main()

### Community 5 - "Матрица проверок риск-менеджмента (tests_risk.py)"
Cohesion: 0.07
Nodes (16): Карта проверок проекта (Checks Map): Polymarket-Sim, Когда направление обязательно, Лестница исправления AAR (Fix Ladder), Матрица проверок риск-менеджмента (tests_risk.py), Направления проверок, Ведомость, Исправления, Разбор 2026-11-03: Стагнация капитала, фиктивная альфа оракула и паралич слотов (+8 more)

### Community 6 - "🧠 Реестр авто-доработок и полуавтоматических решений (Auto-Governor)"
Cohesion: 0.40
Nodes (4): 🛠️ История применённых авто-фиксов и одобренных правок (0), 🟡 Ожидают твоего решения (Полуавтоматический режим: 0), 🧠 Реестр авто-доработок и полуавтоматических решений (Auto-Governor), ⚙️ Текущие активные параметры риск-менеджмента

### Community 7 - "📊 Отчёт симулятора Polymarket (Устав Grok Bot — Демо-счёт)"
Cohesion: 0.29
Nodes (6): Доходность по замороженным категориям (Песочница), 📂 Открытые позиции (0 / 8), 📊 Отчёт симулятора Polymarket (Устав Grok Bot — Демо-счёт), 🔍 Последние проверенные кандидаты и фильтр стакана CLOB, 💰 Состояние виртуального портфеля, 🧪 Теневая песочница (Shadow Sandbox)

### Community 9 - "Polymarket Simulation and Agentic Market Architecture"
Cohesion: 0.40
Nodes (4): 1. Multi-Agent Role Decomposition, 2. Scraping and Resource Optimization (Obscura Integration), 3. Simulation Verification (Unlazy Integration), Polymarket Simulation and Agentic Market Architecture

### Community 15 - ".test_reports_cadence_stale_warning"
Cohesion: 0.38
Nodes (4): Ведомость, Исправления, Разбор 2026-11-07: подмена 10-минутного мониторинга уставного бота задержкой бесплатного GitHub Actions, Чем доказано, что ловится

### Community 19 - "Разбор 2026-11-07: ложное утверждение об остановке симулятора из-за локального статуса"
Cohesion: 0.40
Nodes (4): Ведомость, Исправления, Разбор 2026-11-07: ложное утверждение об остановке симулятора из-за локального статуса, Чем доказано, что ловится

## Knowledge Gaps
- **2 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `SimDatabase` connect `SimDatabase` to `GrokCharterPaperTrader`, `trader.py`, `AutoGovernor`, `Матрица проверок риск-менеджмента (tests_risk.py)`?**
  _High betweenness centrality (0.240) - this node is a cross-community bridge._
- **Are the 11 inferred relationships involving `SimDatabase` (e.g. with `AutoGovernor` and `generate_reports()`) actually correct?**
  _`SimDatabase` has 11 INFERRED edges - model-reasoned connections that need verification._
- **Should `GrokCharterPaperTrader` be split into smaller, more focused modules?**
  _Cohesion score 0.05134575569358178 - nodes in this community are weakly interconnected._
- **Why does `GrokCharterPaperTrader` connect `GrokCharterPaperTrader` to `SimDatabase`, `CryptoOracle`, `trader.py`, `AutoGovernor`, `Матрица проверок риск-менеджмента (tests_risk.py)`?**
  _High betweenness centrality (0.124) - this node is a cross-community bridge._
- **Are the 16 inferred relationships involving `GrokCharterPaperTrader` (e.g. with `Shadow Portfolio (Sandbox) Implementation Plan` and `Task 2: Shadow Market Evaluation & Position Lifecycle in `trader.py``) actually correct?**
  _`GrokCharterPaperTrader` has 16 INFERRED edges - model-reasoned connections that need verification._
- **Should `SimDatabase` be split into smaller, more focused modules?**
  _Cohesion score 0.06413730803974707 - nodes in this community are weakly interconnected._
- **Why does `AutoGovernor` connect `AutoGovernor` to `GrokCharterPaperTrader`, `SimDatabase`, `trader.py`, `Матрица проверок риск-менеджмента (tests_risk.py)`?**
  _High betweenness centrality (0.098) - this node is a cross-community bridge._