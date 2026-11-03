# Graph Report - Polymarket-Sim  (2026-11-03)

## Corpus Check
- 27 files · ~50,330 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 5 file(s) not represented in the graph (top: (none) 4, .db 1)

## Summary
- 321 nodes · 838 edges · 11 communities (9 shown, 2 thin omitted)
- Extraction: 79% EXTRACTED · 21% INFERRED · 0% AMBIGUOUS · INFERRED: 180 edges (avg confidence: 0.9)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `63dcb08e`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- GrokCharterPaperTrader
- SimDatabase
- WeatherOracle
- trader.py
- AutoGovernor
- .compute_kelly_sizing
- 🧠 Реестр авто-доработок и полуавтоматических решений (Auto-Governor)
- 📊 Отчёт симулятора Polymarket (Устав Grok Bot — Демо-счёт)
- README.md
- Polymarket Simulation and Agentic Market Architecture
- progress.md

## God Nodes (most connected - your core abstractions)
1. `SimDatabase` - 61 edges
2. `GrokCharterPaperTrader` - 40 edges
3. `AutoGovernor` - 30 edges
4. `MarketInfo` - 30 edges
5. `TestRiskManagementV2` - 22 edges
6. `generate_reports()` - 21 edges
7. `main()` - 18 edges
8. `EvaluationResult` - 17 edges
9. `Task 1: Shadow Portfolio Database Schema & Access Layer` - 15 edges
10. `fetch_polymarket_json()` - 13 edges

## Surprising Connections (you probably didn't know these)
- `Лестница исправления AAR (Fix Ladder)` --references--> `AutoGovernor`  [INFERRED]
  .agents/aar/checks-map.md → auto_governor.py
- `Global Constraints` --references--> `simulate_clob_sell_shares()`  [INFERRED]
  docs/superpowers/plans/2026-10-28-shadow-portfolio.md → polymarket_api.py
- `3. Реализация (How)` --references--> `AutoGovernor`  [INFERRED]
  .specs/archive/2026-10-25_risk_management_v2.md → auto_governor.py
- `Task 2: Shadow Market Evaluation & Position Lifecycle in `trader.py`` --references--> `simulate_clob_sell_shares()`  [INFERRED]
  docs/superpowers/plans/2026-10-28-shadow-portfolio.md → polymarket_api.py
- `Task 2: Shadow Market Evaluation & Position Lifecycle in `trader.py`` --references--> `send_telegram_alert()`  [INFERRED]
  docs/superpowers/plans/2026-10-28-shadow-portfolio.md → telegram_notify.py

## Import Cycles
- None detected.

## Communities (11 total, 2 thin omitted)

### Community 0 - "GrokCharterPaperTrader"
Cohesion: 0.06
Nodes (14): EvaluationResult, HighConvictionFactOracle, NewsAndOrderbookOracle, MarketInfo, OrderBookSimulation, make_market(), TestE2EShadowPortfolio, side_effect_buy() (+6 more)

### Community 1 - "SimDatabase"
Cohesion: 0.08
Nodes (12): generate_reports(), SimDatabase, Review Focus, Task 1: Shadow Portfolio Database Schema & Access Layer, Task 2: Shadow Market Evaluation & Position Lifecycle in `trader.py`, Task 3: Auto-Governor Tier 2 Shadow Category Unfreeze Rule, Task 4: Reporting & Dashboard Integration, Task 5: End-to-End Simulation & Verification (+4 more)

### Community 2 - "WeatherOracle"
Cohesion: 0.13
Nodes (4): calibrate_probability(), CryptoOracle, norm_cdf(), WeatherOracle

### Community 3 - "trader.py"
Cohesion: 0.06
Nodes (17): fetch_polymarket_json(), fetch_standard_url(), classify_market_category(), extract_resolution_source(), fetch_active_markets(), fetch_clob_book(), fetch_market_by_id(), parse_market_dict() (+9 more)

### Community 4 - "AutoGovernor"
Cohesion: 0.13
Nodes (5): AutoGovernor, Global Constraints, Shadow Portfolio (Sandbox) Implementation Plan, git_sync_snapshot(), main()

### Community 5 - ".compute_kelly_sizing"
Cohesion: 0.07
Nodes (16): Карта проверок проекта (Checks Map): Polymarket-Sim, Когда направление обязательно, Лестница исправления AAR (Fix Ladder), Матрица проверок риск-менеджмента (tests_risk.py), Направления проверок, Ведомость, Исправления, Разбор 2026-11-03: Стагнация капитала, фиктивная альфа оракула и паралич слотов (+8 more)

### Community 6 - "🧠 Реестр авто-доработок и полуавтоматических решений (Auto-Governor)"
Cohesion: 0.33
Nodes (5): 🛠️ История применённых авто-фиксов и одобренных правок (0), 🟡 Ожидают твоего решения (Полуавтоматический режим: 0), 🧠 Реестр авто-доработок и полуавтоматических решений (Auto-Governor), 🧪 Результаты теневой песочницы (Shadow Sandbox), ⚙️ Текущие активные параметры риск-менеджмента

### Community 7 - "📊 Отчёт симулятора Polymarket (Устав Grok Bot — Демо-счёт)"
Cohesion: 0.29
Nodes (6): Доходность по замороженным категориям (Песочница), 📂 Открытые позиции (2 / 8), 📊 Отчёт симулятора Polymarket (Устав Grok Bot — Демо-счёт), 🔍 Последние проверенные кандидаты и фильтр стакана CLOB, 💰 Состояние виртуального портфеля, 🧪 Теневая песочница (Shadow Sandbox)

### Community 9 - "Polymarket Simulation and Agentic Market Architecture"
Cohesion: 0.40
Nodes (4): 1. Multi-Agent Role Decomposition, 2. Scraping and Resource Optimization (Obscura Integration), 3. Simulation Verification (Unlazy Integration), Polymarket Simulation and Agentic Market Architecture

## Knowledge Gaps
- **2 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `SimDatabase` connect `SimDatabase` to `GrokCharterPaperTrader`, `trader.py`, `AutoGovernor`, `.compute_kelly_sizing`?**
  _High betweenness centrality (0.244) - this node is a cross-community bridge._
- **Are the 11 inferred relationships involving `SimDatabase` (e.g. with `AutoGovernor` and `generate_reports()`) actually correct?**
  _`SimDatabase` has 11 INFERRED edges - model-reasoned connections that need verification._
- **Should `GrokCharterPaperTrader` be split into smaller, more focused modules?**
  _Cohesion score 0.05829420970266041 - nodes in this community are weakly interconnected._
- **Why does `GrokCharterPaperTrader` connect `GrokCharterPaperTrader` to `SimDatabase`, `WeatherOracle`, `trader.py`, `AutoGovernor`, `.compute_kelly_sizing`?**
  _High betweenness centrality (0.130) - this node is a cross-community bridge._
- **Are the 16 inferred relationships involving `GrokCharterPaperTrader` (e.g. with `Shadow Portfolio (Sandbox) Implementation Plan` and `Task 2: Shadow Market Evaluation & Position Lifecycle in `trader.py``) actually correct?**
  _`GrokCharterPaperTrader` has 16 INFERRED edges - model-reasoned connections that need verification._
- **Should `SimDatabase` be split into smaller, more focused modules?**
  _Cohesion score 0.07525150905432595 - nodes in this community are weakly interconnected._
- **Why does `AutoGovernor` connect `AutoGovernor` to `GrokCharterPaperTrader`, `SimDatabase`, `WeatherOracle`, `trader.py`, `.compute_kelly_sizing`?**
  _High betweenness centrality (0.104) - this node is a cross-community bridge._