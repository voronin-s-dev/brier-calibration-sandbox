# Graph Report - Polymarket-Sim  (2026-11-18)

## Corpus Check
- 34 files · ~125,197 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 6 file(s) not represented in the graph (top: (none) 4, .db 1, .ini 1)

## Summary
- 434 nodes · 1139 edges · 22 communities (16 shown, 6 thin omitted)
- Extraction: 77% EXTRACTED · 23% INFERRED · 0% AMBIGUOUS · INFERRED: 265 edges (avg confidence: 0.89)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `c72586a3`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- Матрица проверок риск-менеджмента (tests_risk.py)
- SimDatabase
- MarketInfo
- SimDatabase
- AutoGovernor
- extract_event_key
- 🧠 Реестр авто-доработок и полуавтоматических решений (Auto-Governor)
- 📊 Отчёт симулятора Polymarket (Устав Grok Bot — Демо-счёт)
- README.md
- Polymarket Simulation and Agentic Market Architecture
- .test_e2e_dual_track_execution
- .test_reports_cadence_stale_warning
- Карта проверок проекта (Checks Map): Polymarket-Sim
- Acceptance Gates: Polymarket Simulation Daily Audit & Auto-Refinement
- Спецификация: Risk Management & Budget Protection v2
- trader.py
- Разбор 2026-11-07: ложное утверждение об остановке симулятора из-за локального статуса
- run_sim.py
- .test_shadow_candidate_funnel_not_starved

## God Nodes (most connected - your core abstractions)
1. `SimDatabase` - 78 edges
2. `GrokCharterPaperTrader` - 57 edges
3. `TestRiskManagementV2` - 55 edges
4. `MarketInfo` - 50 edges
5. `AutoGovernor` - 30 edges
6. `generate_reports()` - 22 edges
7. `EvaluationResult` - 22 edges
8. `main()` - 22 edges
9. `send_telegram_alert()` - 20 edges
10. `WeatherOracle` - 16 edges

## Surprising Connections (you probably didn't know these)
- `Лестница исправления AAR (Fix Ladder)` --references--> `AutoGovernor`  [INFERRED]
  .agents/aar/checks-map.md → auto_governor.py
- `Global Constraints` --references--> `simulate_clob_sell_shares()`  [INFERRED]
  docs/superpowers/plans/2026-10-28-shadow-portfolio.md → polymarket_api.py
- `3. Реализация (How)` --references--> `AutoGovernor`  [INFERRED]
  .specs/archive/2026-10-25_risk_management_v2.md → auto_governor.py
- `Task 1: Shadow Portfolio Database Schema & Access Layer` --references--> `SimDatabase`  [INFERRED]
  docs/superpowers/plans/2026-10-28-shadow-portfolio.md → database.py
- `Task 2: Shadow Market Evaluation & Position Lifecycle in `trader.py`` --references--> `simulate_clob_sell_shares()`  [INFERRED]
  docs/superpowers/plans/2026-10-28-shadow-portfolio.md → polymarket_api.py

## Import Cycles
- None detected.

## Communities (22 total, 6 thin omitted)

### Community 1 - "SimDatabase"
Cohesion: 0.06
Nodes (14): Ведомость, Исправления, Разбор 2026-11-10: сбой циклов из-за отсутствующего поля MIN_HOURS_TO_CLOSE_EXIT при появлении теневых позиций, Чем доказано, что ловится, generate_reports(), Review Focus, Task 1: Shadow Portfolio Database Schema & Access Layer, Task 2: Shadow Market Evaluation & Position Lifecycle in `trader.py` (+6 more)

### Community 2 - "MarketInfo"
Cohesion: 0.06
Nodes (11): calibrate_probability(), CryptoOracle, HighConvictionFactOracle, is_esports_market(), NewsAndOrderbookOracle, norm_cdf(), WeatherOracle, MarketInfo (+3 more)

### Community 3 - "SimDatabase"
Cohesion: 0.07
Nodes (7): SimDatabase, EvaluationResult, print_console_summary(), TestE2EShadowPortfolio, TestShadowTrader, TestRiskManagementV2, GrokCharterPaperTrader

### Community 4 - "AutoGovernor"
Cohesion: 0.12
Nodes (7): Ведомость, Исправления, Первопричина (Root Cause), Разбор 2026-11-10: троекратное дублирование уведомления об одобрении доработки #22 в Telegram, AutoGovernor, Global Constraints, Shadow Portfolio (Sandbox) Implementation Plan

### Community 6 - "🧠 Реестр авто-доработок и полуавтоматических решений (Auto-Governor)"
Cohesion: 0.29
Nodes (6): 🛠️ История применённых авто-фиксов и одобренных правок (22), 🟡 Ожидают твоего решения (Полуавтоматический режим: 1), ⚪ Отклонённые и утратившие актуальность предложения (12), Предложение #34: Разморозка категории Crypto: стабильный плюс в песочнице ($+6.78) (`TIER_2_CALIBRATION`), 🧠 Реестр авто-доработок и полуавтоматических решений (Auto-Governor), ⚙️ Текущие активные параметры риск-менеджмента

### Community 7 - "📊 Отчёт симулятора Polymarket (Устав Grok Bot — Демо-счёт)"
Cohesion: 0.29
Nodes (6): Доходность по замороженным категориям (Песочница), 📂 Открытые позиции (5 / 8), 📊 Отчёт симулятора Polymarket (Устав Grok Bot — Демо-счёт), 🔍 Последние проверенные кандидаты и фильтр стакана CLOB, 💰 Состояние виртуального портфеля, 🧪 Теневая песочница (Shadow Sandbox)

### Community 9 - "Polymarket Simulation and Agentic Market Architecture"
Cohesion: 0.40
Nodes (4): 1. Multi-Agent Role Decomposition, 2. Scraping and Resource Optimization (Obscura Integration), 3. Simulation Verification (Unlazy Integration), Polymarket Simulation and Agentic Market Architecture

### Community 11 - ".test_e2e_dual_track_execution"
Cohesion: 0.33
Nodes (3): make_market(), side_effect_buy(), side_effect_eval()

### Community 12 - ".test_reports_cadence_stale_warning"
Cohesion: 0.24
Nodes (5): Ведомость, Исправления, Разбор 2026-11-07: подмена 10-минутного мониторинга уставного бота задержкой бесплатного GitHub Actions, Чем доказано, что ловится, TestShadowReports

### Community 13 - "Карта проверок проекта (Checks Map): Polymarket-Sim"
Cohesion: 0.40
Nodes (4): Карта проверок проекта (Checks Map): Polymarket-Sim, Когда направление обязательно, Лестница исправления AAR (Fix Ladder), Направления проверок

### Community 14 - "Acceptance Gates: Polymarket Simulation Daily Audit & Auto-Refinement"
Cohesion: 0.33
Nodes (5): Acceptance Gates: Polymarket Simulation Daily Audit & Auto-Refinement, Gate 1: Unit & Behavior Risk Tests, Gate 2: Full Test Suite, Gate 3: Auto-Governor & Status Inspection, Gate 4: Knowledge Graph Synchronization

### Community 15 - "Спецификация: Risk Management & Budget Protection v2"
Cohesion: 0.33
Nodes (5): 1. Зачем (Why), 2. Требования (Requirements), 3. Реализация (How), 4. Чеклист верификации, Спецификация: Risk Management & Budget Protection v2

### Community 17 - "trader.py"
Cohesion: 0.07
Nodes (12): fetch_polymarket_json(), fetch_standard_url(), resolve_secure_ip(), classify_market_category(), extract_resolution_source(), fetch_active_markets(), fetch_clob_book(), fetch_market_by_id() (+4 more)

### Community 19 - "Разбор 2026-11-07: ложное утверждение об остановке симулятора из-за локального статуса"
Cohesion: 0.40
Nodes (4): Ведомость, Исправления, Разбор 2026-11-07: ложное утверждение об остановке симулятора из-за локального статуса, Чем доказано, что ловится

### Community 20 - "run_sim.py"
Cohesion: 0.09
Nodes (13): Ведомость, Исправления, Первопричина (Root Cause), Разбор 2026-11-11: преждевременная отправка дневного дайджеста в 02:00 ночи сразу после смены даты по UTC, git_sync_snapshot(), main(), check_and_send_daily_digest(), _load_env_fallback() (+5 more)

### Community 26 - ".test_shadow_candidate_funnel_not_starved"
Cohesion: 0.20
Nodes (5): Ведомость, Исправления, Разбор 2026-11-03: Стагнация капитала, фиктивная альфа оракула и паралич слотов, Чем доказано, что ловится, _mk()

## Knowledge Gaps
- **6 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `SimDatabase` connect `SimDatabase` to `SimDatabase`, `MarketInfo`, `AutoGovernor`, `.test_reports_cadence_stale_warning`, `trader.py`, `run_sim.py`, `.test_shadow_candidate_funnel_not_starved`?**
  _High betweenness centrality (0.216) - this node is a cross-community bridge._
- **Are the 11 inferred relationships involving `SimDatabase` (e.g. with `AutoGovernor` and `generate_reports()`) actually correct?**
  _`SimDatabase` has 11 INFERRED edges - model-reasoned connections that need verification._
- **Should `SimDatabase` be split into smaller, more focused modules?**
  _Cohesion score 0.05543859649122807 - nodes in this community are weakly interconnected._
- **Why does `TestRiskManagementV2` connect `SimDatabase` to `Матрица проверок риск-менеджмента (tests_risk.py)`, `SimDatabase`, `MarketInfo`, `AutoGovernor`, `extract_event_key`, `.run_cycle`, `.test_dynamic_risk_cap_for_ceiling_contracts`, `trader.py`, `run_sim.py`, `.test_shadow_candidate_funnel_not_starved`?**
  _High betweenness centrality (0.148) - this node is a cross-community bridge._
- **Are the 17 inferred relationships involving `GrokCharterPaperTrader` (e.g. with `Исправления` and `Shadow Portfolio (Sandbox) Implementation Plan`) actually correct?**
  _`GrokCharterPaperTrader` has 17 INFERRED edges - model-reasoned connections that need verification._
- **Should `MarketInfo` be split into smaller, more focused modules?**
  _Cohesion score 0.06168831168831169 - nodes in this community are weakly interconnected._
- **Why does `GrokCharterPaperTrader` connect `SimDatabase` to `Матрица проверок риск-менеджмента (tests_risk.py)`, `SimDatabase`, `MarketInfo`, `AutoGovernor`, `.run_cycle`, `Спецификация: Risk Management & Budget Protection v2`, `.test_dynamic_risk_cap_for_ceiling_contracts`, `trader.py`, `.partition_markets`, `run_sim.py`, `.test_shadow_candidate_funnel_not_starved`?**
  _High betweenness centrality (0.115) - this node is a cross-community bridge._