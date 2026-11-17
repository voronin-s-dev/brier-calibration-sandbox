# Graph Report - Polymarket-Sim  (2026-11-17)

## Corpus Check
- 34 files · ~122,574 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 6 file(s) not represented in the graph (top: (none) 4, .db 1, .ini 1)

## Summary
- 425 nodes · 1107 edges · 21 communities (15 shown, 6 thin omitted)
- Extraction: 77% EXTRACTED · 23% INFERRED · 0% AMBIGUOUS · INFERRED: 255 edges (avg confidence: 0.9)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `a34d2e49`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- .evaluate_and_execute_shadow_candidates
- SimDatabase
- TestRiskManagementV2
- GrokCharterPaperTrader
- AutoGovernor
- CryptoOracle
- 🧠 Реестр авто-доработок и полуавтоматических решений (Auto-Governor)
- 📊 Отчёт симулятора Polymarket (Устав Grok Bot — Демо-счёт)
- README.md
- Polymarket Simulation and Agentic Market Architecture
- .monitor_and_manage_shadow_positions
- .test_reports_cadence_stale_warning
- TestShadowTrader
- Acceptance Gates: Polymarket Simulation Daily Audit & Auto-Refinement
- Спецификация: Risk Management & Budget Protection v2
- trader.py
- Разбор 2026-11-07: ложное утверждение об остановке симулятора из-за локального статуса
- run_sim.py
- Разбор 2026-11-03: Стагнация капитала, фиктивная альфа оракула и паралич слотов

## God Nodes (most connected - your core abstractions)
1. `SimDatabase` - 74 edges
2. `GrokCharterPaperTrader` - 55 edges
3. `TestRiskManagementV2` - 50 edges
4. `MarketInfo` - 47 edges
5. `AutoGovernor` - 30 edges
6. `generate_reports()` - 22 edges
7. `main()` - 22 edges
8. `EvaluationResult` - 21 edges
9. `send_telegram_alert()` - 20 edges
10. `WeatherOracle` - 16 edges

## Surprising Connections (you probably didn't know these)
- `Лестница исправления AAR (Fix Ladder)` --references--> `AutoGovernor`  [INFERRED]
  .agents/aar/checks-map.md → auto_governor.py
- `Shadow Portfolio (Sandbox) Implementation Plan` --references--> `AutoGovernor`  [INFERRED]
  docs/superpowers/plans/2026-10-28-shadow-portfolio.md → auto_governor.py
- `3. Реализация (How)` --references--> `AutoGovernor`  [INFERRED]
  .specs/archive/2026-10-25_risk_management_v2.md → auto_governor.py
- `Global Constraints` --references--> `simulate_clob_sell_shares()`  [INFERRED]
  docs/superpowers/plans/2026-10-28-shadow-portfolio.md → polymarket_api.py
- `Исправления` --references--> `main()`  [INFERRED]
  .agents/aar/runs/2026-11-10-shadow-missing-attribute-time-exit-aar.md → run_sim.py

## Import Cycles
- None detected.

## Communities (21 total, 6 thin omitted)

### Community 1 - "SimDatabase"
Cohesion: 0.06
Nodes (15): generate_reports(), SimDatabase, Review Focus, Task 1: Shadow Portfolio Database Schema & Access Layer, Task 3: Auto-Governor Tier 2 Shadow Category Unfreeze Rule, Task 4: Reporting & Dashboard Integration, Task 5: End-to-End Simulation & Verification, print_console_summary() (+7 more)

### Community 2 - "TestRiskManagementV2"
Cohesion: 0.05
Nodes (13): Матрица проверок риск-менеджмента (tests_risk.py), Исправления, calibrate_probability(), EvaluationResult, HighConvictionFactOracle, is_esports_market(), NewsAndOrderbookOracle, MarketInfo (+5 more)

### Community 4 - "AutoGovernor"
Cohesion: 0.12
Nodes (10): Карта проверок проекта (Checks Map): Polymarket-Sim, Когда направление обязательно, Лестница исправления AAR (Fix Ladder), Направления проверок, Ведомость, Исправления, Первопричина (Root Cause), Разбор 2026-11-10: троекратное дублирование уведомления об одобрении доработки #22 в Telegram (+2 more)

### Community 6 - "🧠 Реестр авто-доработок и полуавтоматических решений (Auto-Governor)"
Cohesion: 0.29
Nodes (6): 🛠️ История применённых авто-фиксов и одобренных правок (21), 🟡 Ожидают твоего решения (Полуавтоматический режим: 1), ⚪ Отклонённые и утратившие актуальность предложения (12), Предложение #34: Разморозка категории Crypto: стабильный плюс в песочнице ($+6.78) (`TIER_2_CALIBRATION`), 🧠 Реестр авто-доработок и полуавтоматических решений (Auto-Governor), ⚙️ Текущие активные параметры риск-менеджмента

### Community 7 - "📊 Отчёт симулятора Polymarket (Устав Grok Bot — Демо-счёт)"
Cohesion: 0.25
Nodes (7): Доходность по замороженным категориям (Песочница), 📂 Открытые позиции (1 / 8), Открытые позиции в песочнице (3 / 5), 📊 Отчёт симулятора Polymarket (Устав Grok Bot — Демо-счёт), 🔍 Последние проверенные кандидаты и фильтр стакана CLOB, 💰 Состояние виртуального портфеля, 🧪 Теневая песочница (Shadow Sandbox)

### Community 9 - "Polymarket Simulation and Agentic Market Architecture"
Cohesion: 0.40
Nodes (4): 1. Multi-Agent Role Decomposition, 2. Scraping and Resource Optimization (Obscura Integration), 3. Simulation Verification (Unlazy Integration), Polymarket Simulation and Agentic Market Architecture

### Community 11 - ".monitor_and_manage_shadow_positions"
Cohesion: 0.29
Nodes (4): Global Constraints, Shadow Portfolio (Sandbox) Implementation Plan, Task 2: Shadow Market Evaluation & Position Lifecycle in `trader.py`, simulate_clob_sell_shares()

### Community 12 - ".test_reports_cadence_stale_warning"
Cohesion: 0.38
Nodes (4): Ведомость, Исправления, Разбор 2026-11-07: подмена 10-минутного мониторинга уставного бота задержкой бесплатного GitHub Actions, Чем доказано, что ловится

### Community 13 - "TestShadowTrader"
Cohesion: 0.14
Nodes (6): Ведомость, Исправления, Разбор 2026-11-10: сбой циклов из-за отсутствующего поля MIN_HOURS_TO_CLOSE_EXIT при появлении теневых позиций, Чем доказано, что ловится, make_market_info(), TestShadowTrader

### Community 14 - "Acceptance Gates: Polymarket Simulation Daily Audit & Auto-Refinement"
Cohesion: 0.33
Nodes (5): Acceptance Gates: Polymarket Simulation Daily Audit & Auto-Refinement, Gate 1: Unit & Behavior Risk Tests, Gate 2: Full Test Suite, Gate 3: Auto-Governor & Status Inspection, Gate 4: Knowledge Graph Synchronization

### Community 15 - "Спецификация: Risk Management & Budget Protection v2"
Cohesion: 0.40
Nodes (4): 1. Зачем (Why), 2. Требования (Requirements), 4. Чеклист верификации, Спецификация: Risk Management & Budget Protection v2

### Community 17 - "trader.py"
Cohesion: 0.07
Nodes (11): norm_cdf(), WeatherOracle, classify_market_category(), extract_resolution_source(), fetch_active_markets(), fetch_clob_book(), fetch_market_by_id(), OrderBookSimulation (+3 more)

### Community 19 - "Разбор 2026-11-07: ложное утверждение об остановке симулятора из-за локального статуса"
Cohesion: 0.40
Nodes (4): Ведомость, Исправления, Разбор 2026-11-07: ложное утверждение об остановке симулятора из-за локального статуса, Чем доказано, что ловится

### Community 20 - "run_sim.py"
Cohesion: 0.07
Nodes (15): Ведомость, Исправления, Первопричина (Root Cause), Разбор 2026-11-11: преждевременная отправка дневного дайджеста в 02:00 ночи сразу после смены даты по UTC, fetch_polymarket_json(), fetch_standard_url(), resolve_secure_ip(), git_sync_snapshot() (+7 more)

### Community 26 - "Разбор 2026-11-03: Стагнация капитала, фиктивная альфа оракула и паралич слотов"
Cohesion: 0.50
Nodes (3): Ведомость, Разбор 2026-11-03: Стагнация капитала, фиктивная альфа оракула и паралич слотов, Чем доказано, что ловится

## Knowledge Gaps
- **6 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `SimDatabase` connect `SimDatabase` to `TestRiskManagementV2`, `GrokCharterPaperTrader`, `AutoGovernor`, `.run_cycle`, `TestShadowTrader`, `trader.py`, `run_sim.py`?**
  _High betweenness centrality (0.208) - this node is a cross-community bridge._
- **Are the 11 inferred relationships involving `SimDatabase` (e.g. with `AutoGovernor` and `generate_reports()`) actually correct?**
  _`SimDatabase` has 11 INFERRED edges - model-reasoned connections that need verification._
- **Should `.evaluate_and_execute_shadow_candidates` be split into smaller, more focused modules?**
  _Cohesion score 0.14285714285714285 - nodes in this community are weakly interconnected._
- **Why does `TestRiskManagementV2` connect `TestRiskManagementV2` to `.evaluate_and_execute_shadow_candidates`, `SimDatabase`, `GrokCharterPaperTrader`, `AutoGovernor`, `.run_cycle`, `.test_dynamic_risk_cap_for_ceiling_contracts`, `trader.py`, `run_sim.py`?**
  _High betweenness centrality (0.138) - this node is a cross-community bridge._
- **Are the 17 inferred relationships involving `GrokCharterPaperTrader` (e.g. with `Исправления` and `Shadow Portfolio (Sandbox) Implementation Plan`) actually correct?**
  _`GrokCharterPaperTrader` has 17 INFERRED edges - model-reasoned connections that need verification._
- **Should `SimDatabase` be split into smaller, more focused modules?**
  _Cohesion score 0.060240963855421686 - nodes in this community are weakly interconnected._
- **Why does `GrokCharterPaperTrader` connect `GrokCharterPaperTrader` to `.evaluate_and_execute_shadow_candidates`, `SimDatabase`, `TestRiskManagementV2`, `AutoGovernor`, `CryptoOracle`, `.run_cycle`, `.monitor_and_manage_shadow_positions`, `TestShadowTrader`, `.test_dynamic_risk_cap_for_ceiling_contracts`, `trader.py`, `run_sim.py`?**
  _High betweenness centrality (0.119) - this node is a cross-community bridge._