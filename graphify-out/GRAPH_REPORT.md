# Graph Report - Polymarket-Sim  (2026-11-10)

## Corpus Check
- 29 files · ~68,855 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 6 file(s) not represented in the graph (top: (none) 4, .db 1, .ini 1)

## Summary
- 354 nodes · 927 edges · 14 communities (12 shown, 2 thin omitted)
- Extraction: 77% EXTRACTED · 23% INFERRED · 0% AMBIGUOUS · INFERRED: 214 edges (avg confidence: 0.9)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `c26f7067`
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
- oracles.py
- .test_shadow_position_active_time_exit
- .test_reports_cadence_stale_warning
- Разбор 2026-11-07: ложное утверждение об остановке симулятора из-за локального статуса

## God Nodes (most connected - your core abstractions)
1. `SimDatabase` - 64 edges
2. `GrokCharterPaperTrader` - 44 edges
3. `MarketInfo` - 34 edges
4. `AutoGovernor` - 30 edges
5. `TestRiskManagementV2` - 26 edges
6. `generate_reports()` - 22 edges
7. `EvaluationResult` - 19 edges
8. `main()` - 19 edges
9. `Task 1: Shadow Portfolio Database Schema & Access Layer` - 15 edges
10. `fetch_polymarket_json()` - 14 edges

## Surprising Connections (you probably didn't know these)
- `Лестница исправления AAR (Fix Ladder)` --references--> `AutoGovernor`  [INFERRED]
  .agents/aar/checks-map.md → auto_governor.py
- `Global Constraints` --references--> `simulate_clob_sell_shares()`  [INFERRED]
  docs/superpowers/plans/2026-10-28-shadow-portfolio.md → polymarket_api.py
- `3. Реализация (How)` --references--> `AutoGovernor`  [INFERRED]
  .specs/archive/2026-10-25_risk_management_v2.md → auto_governor.py
- `Исправления` --references--> `main()`  [INFERRED]
  .agents/aar/runs/2026-11-10-shadow-missing-attribute-time-exit-aar.md → run_sim.py
- `Task 2: Shadow Market Evaluation & Position Lifecycle in `trader.py`` --references--> `send_telegram_alert()`  [INFERRED]
  docs/superpowers/plans/2026-10-28-shadow-portfolio.md → telegram_notify.py

## Import Cycles
- None detected.

## Communities (14 total, 2 thin omitted)

### Community 0 - "GrokCharterPaperTrader"
Cohesion: 0.06
Nodes (15): Task 2: Shadow Market Evaluation & Position Lifecycle in `trader.py`, EvaluationResult, fetch_clob_book(), MarketInfo, OrderBookSimulation, simulate_clob_buy_and_exit_check(), simulate_clob_sell_shares(), make_market() (+7 more)

### Community 1 - "SimDatabase"
Cohesion: 0.08
Nodes (11): generate_reports(), SimDatabase, Review Focus, Task 1: Shadow Portfolio Database Schema & Access Layer, Task 3: Auto-Governor Tier 2 Shadow Category Unfreeze Rule, Task 4: Reporting & Dashboard Integration, Task 5: End-to-End Simulation & Verification, print_console_summary() (+3 more)

### Community 3 - "trader.py"
Cohesion: 0.08
Nodes (8): git_sync_snapshot(), check_and_send_daily_digest(), _load_env_fallback(), notify_position_closed(), _plural_deals(), send_telegram_alert(), load_token_from_env(), trigger_workflow()

### Community 4 - "AutoGovernor"
Cohesion: 0.15
Nodes (5): AutoGovernor, Global Constraints, Shadow Portfolio (Sandbox) Implementation Plan, WeatherOracle, main()

### Community 5 - "Матрица проверок риск-менеджмента (tests_risk.py)"
Cohesion: 0.05
Nodes (20): Карта проверок проекта (Checks Map): Polymarket-Sim, Когда направление обязательно, Лестница исправления AAR (Fix Ladder), Матрица проверок риск-менеджмента (tests_risk.py), Направления проверок, Ведомость, Исправления, Разбор 2026-11-03: Стагнация капитала, фиктивная альфа оракула и паралич слотов (+12 more)

### Community 6 - "🧠 Реестр авто-доработок и полуавтоматических решений (Auto-Governor)"
Cohesion: 0.29
Nodes (6): 🛠️ История применённых авто-фиксов и одобренных правок (18), 🟡 Ожидают твоего решения (Полуавтоматический режим: 0), ⚪ Отклонённые и утратившие актуальность предложения (2), 🧠 Реестр авто-доработок и полуавтоматических решений (Auto-Governor), 🧪 Результаты теневой песочницы (Shadow Sandbox), ⚙️ Текущие активные параметры риск-менеджмента

### Community 7 - "📊 Отчёт симулятора Polymarket (Устав Grok Bot — Демо-счёт)"
Cohesion: 0.29
Nodes (6): Доходность по замороженным категориям (Песочница), 📂 Открытые позиции (3 / 8), 📊 Отчёт симулятора Polymarket (Устав Grok Bot — Демо-счёт), 🔍 Последние проверенные кандидаты и фильтр стакана CLOB, 💰 Состояние виртуального портфеля, 🧪 Теневая песочница (Shadow Sandbox)

### Community 9 - "Polymarket Simulation and Agentic Market Architecture"
Cohesion: 0.40
Nodes (4): 1. Multi-Agent Role Decomposition, 2. Scraping and Resource Optimization (Obscura Integration), 3. Simulation Verification (Unlazy Integration), Polymarket Simulation and Agentic Market Architecture

### Community 10 - "oracles.py"
Cohesion: 0.10
Nodes (9): fetch_polymarket_json(), fetch_standard_url(), resolve_secure_ip(), norm_cdf(), classify_market_category(), extract_resolution_source(), fetch_active_markets(), fetch_market_by_id() (+1 more)

### Community 11 - ".test_shadow_position_active_time_exit"
Cohesion: 0.38
Nodes (4): Ведомость, Исправления, Разбор 2026-11-10: сбой циклов из-за отсутствующего поля MIN_HOURS_TO_CLOSE_EXIT при появлении теневых позиций, Чем доказано, что ловится

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

- **Why does `SimDatabase` connect `SimDatabase` to `GrokCharterPaperTrader`, `CryptoOracle`, `trader.py`, `AutoGovernor`, `Матрица проверок риск-менеджмента (tests_risk.py)`?**
  _High betweenness centrality (0.231) - this node is a cross-community bridge._
- **Are the 11 inferred relationships involving `SimDatabase` (e.g. with `AutoGovernor` and `generate_reports()`) actually correct?**
  _`SimDatabase` has 11 INFERRED edges - model-reasoned connections that need verification._
- **Should `GrokCharterPaperTrader` be split into smaller, more focused modules?**
  _Cohesion score 0.0594679186228482 - nodes in this community are weakly interconnected._
- **Why does `GrokCharterPaperTrader` connect `GrokCharterPaperTrader` to `SimDatabase`, `CryptoOracle`, `trader.py`, `AutoGovernor`, `Матрица проверок риск-менеджмента (tests_risk.py)`, `.test_shadow_position_active_time_exit`?**
  _High betweenness centrality (0.129) - this node is a cross-community bridge._
- **Are the 17 inferred relationships involving `GrokCharterPaperTrader` (e.g. with `Исправления` and `Shadow Portfolio (Sandbox) Implementation Plan`) actually correct?**
  _`GrokCharterPaperTrader` has 17 INFERRED edges - model-reasoned connections that need verification._
- **Should `SimDatabase` be split into smaller, more focused modules?**
  _Cohesion score 0.0781387181738367 - nodes in this community are weakly interconnected._
- **Why does `AutoGovernor` connect `AutoGovernor` to `GrokCharterPaperTrader`, `SimDatabase`, `trader.py`, `Матрица проверок риск-менеджмента (tests_risk.py)`?**
  _High betweenness centrality (0.089) - this node is a cross-community bridge._