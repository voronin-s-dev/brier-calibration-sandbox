# Graph Report - Polymarket-Sim  (2026-11-18)

## Corpus Check
- 34 files · ~128,979 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 6 file(s) not represented in the graph (top: (none) 4, .db 1, .ini 1)

## Summary
- 440 nodes · 1151 edges · 23 communities (16 shown, 7 thin omitted)
- Extraction: 77% EXTRACTED · 23% INFERRED · 0% AMBIGUOUS · INFERRED: 269 edges (avg confidence: 0.89)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `72c5605c`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- Матрица проверок риск-менеджмента (tests_risk.py)
- SimDatabase
- GrokCharterPaperTrader
- .monitor_and_manage_shadow_positions
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
- check_and_send_daily_digest
- .test_shadow_candidate_funnel_not_starved

## God Nodes (most connected - your core abstractions)
1. `SimDatabase` - 78 edges
2. `GrokCharterPaperTrader` - 58 edges
3. `TestRiskManagementV2` - 56 edges
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
- `Task 2: Shadow Market Evaluation & Position Lifecycle in `trader.py`` --references--> `simulate_clob_sell_shares()`  [INFERRED]
  docs/superpowers/plans/2026-10-28-shadow-portfolio.md → polymarket_api.py
- `Исправления` --references--> `main()`  [INFERRED]
  .agents/aar/runs/2026-11-10-shadow-missing-attribute-time-exit-aar.md → run_sim.py

## Import Cycles
- None detected.

## Communities (23 total, 7 thin omitted)

### Community 1 - "SimDatabase"
Cohesion: 0.05
Nodes (14): generate_reports(), SimDatabase, Review Focus, Task 1: Shadow Portfolio Database Schema & Access Layer, Task 2: Shadow Market Evaluation & Position Lifecycle in `trader.py`, Task 4: Reporting & Dashboard Integration, Task 5: End-to-End Simulation & Verification, print_console_summary() (+6 more)

### Community 2 - "GrokCharterPaperTrader"
Cohesion: 0.05
Nodes (12): CryptoOracle, EvaluationResult, HighConvictionFactOracle, is_esports_market(), NewsAndOrderbookOracle, WeatherOracle, MarketInfo, TestRiskManagementV2 (+4 more)

### Community 3 - ".monitor_and_manage_shadow_positions"
Cohesion: 0.31
Nodes (4): Ведомость, Исправления, Разбор 2026-11-10: сбой циклов из-за отсутствующего поля MIN_HOURS_TO_CLOSE_EXIT при появлении теневых позиций, Чем доказано, что ловится

### Community 4 - "AutoGovernor"
Cohesion: 0.08
Nodes (14): Ведомость, Исправления, Первопричина (Root Cause), Разбор 2026-11-10: троекратное дублирование уведомления об одобрении доработки #22 в Telegram, AutoGovernor, Global Constraints, Shadow Portfolio (Sandbox) Implementation Plan, Task 3: Auto-Governor Tier 2 Shadow Category Unfreeze Rule (+6 more)

### Community 6 - "🧠 Реестр авто-доработок и полуавтоматических решений (Auto-Governor)"
Cohesion: 0.29
Nodes (6): 🛠️ История применённых авто-фиксов и одобренных правок (22), 🟡 Ожидают твоего решения (Полуавтоматический режим: 1), ⚪ Отклонённые и утратившие актуальность предложения (12), Предложение #34: Разморозка категории Crypto: стабильный плюс в песочнице ($+6.78) (`TIER_2_CALIBRATION`), 🧠 Реестр авто-доработок и полуавтоматических решений (Auto-Governor), ⚙️ Текущие активные параметры риск-менеджмента

### Community 7 - "📊 Отчёт симулятора Polymarket (Устав Grok Bot — Демо-счёт)"
Cohesion: 0.29
Nodes (6): Доходность по замороженным категориям (Песочница), 📂 Открытые позиции (3 / 8), 📊 Отчёт симулятора Polymarket (Устав Grok Bot — Демо-счёт), 🔍 Последние проверенные кандидаты и фильтр стакана CLOB, 💰 Состояние виртуального портфеля, 🧪 Теневая песочница (Shadow Sandbox)

### Community 9 - "Polymarket Simulation and Agentic Market Architecture"
Cohesion: 0.40
Nodes (4): 1. Multi-Agent Role Decomposition, 2. Scraping and Resource Optimization (Obscura Integration), 3. Simulation Verification (Unlazy Integration), Polymarket Simulation and Agentic Market Architecture

### Community 11 - ".test_e2e_dual_track_execution"
Cohesion: 0.33
Nodes (3): make_market(), side_effect_buy(), side_effect_eval()

### Community 12 - ".test_reports_cadence_stale_warning"
Cohesion: 0.38
Nodes (4): Ведомость, Исправления, Разбор 2026-11-07: подмена 10-минутного мониторинга уставного бота задержкой бесплатного GitHub Actions, Чем доказано, что ловится

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
Cohesion: 0.06
Nodes (14): fetch_polymarket_json(), fetch_standard_url(), resolve_secure_ip(), norm_cdf(), classify_market_category(), extract_resolution_source(), fetch_active_markets(), fetch_clob_book() (+6 more)

### Community 19 - "Разбор 2026-11-07: ложное утверждение об остановке симулятора из-за локального статуса"
Cohesion: 0.40
Nodes (4): Ведомость, Исправления, Разбор 2026-11-07: ложное утверждение об остановке симулятора из-за локального статуса, Чем доказано, что ловится

### Community 20 - "check_and_send_daily_digest"
Cohesion: 0.14
Nodes (7): Ведомость, Исправления, Первопричина (Root Cause), Разбор 2026-11-11: преждевременная отправка дневного дайджеста в 02:00 ночи сразу после смены даты по UTC, check_and_send_daily_digest(), notify_position_closed(), _plural_deals()

### Community 26 - ".test_shadow_candidate_funnel_not_starved"
Cohesion: 0.20
Nodes (5): Ведомость, Исправления, Разбор 2026-11-03: Стагнация капитала, фиктивная альфа оракула и паралич слотов, Чем доказано, что ловится, _mk()

## Knowledge Gaps
- **7 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `SimDatabase` connect `SimDatabase` to `trader.py`, `GrokCharterPaperTrader`, `.test_shadow_candidate_funnel_not_starved`, `AutoGovernor`?**
  _High betweenness centrality (0.214) - this node is a cross-community bridge._
- **Are the 11 inferred relationships involving `SimDatabase` (e.g. with `AutoGovernor` and `generate_reports()`) actually correct?**
  _`SimDatabase` has 11 INFERRED edges - model-reasoned connections that need verification._
- **Should `SimDatabase` be split into smaller, more focused modules?**
  _Cohesion score 0.05021929824561404 - nodes in this community are weakly interconnected._
- **Why does `TestRiskManagementV2` connect `GrokCharterPaperTrader` to `Матрица проверок риск-менеджмента (tests_risk.py)`, `SimDatabase`, `AutoGovernor`, `extract_event_key`, `.run_cycle`, `.test_dynamic_risk_cap_for_ceiling_contracts`, `trader.py`, `check_and_send_daily_digest`, `.is_social_mention_count_trap`, `.test_shadow_candidate_funnel_not_starved`?**
  _High betweenness centrality (0.153) - this node is a cross-community bridge._
- **Are the 17 inferred relationships involving `GrokCharterPaperTrader` (e.g. with `Исправления` and `Shadow Portfolio (Sandbox) Implementation Plan`) actually correct?**
  _`GrokCharterPaperTrader` has 17 INFERRED edges - model-reasoned connections that need verification._
- **Should `GrokCharterPaperTrader` be split into smaller, more focused modules?**
  _Cohesion score 0.05025712949976625 - nodes in this community are weakly interconnected._
- **Why does `GrokCharterPaperTrader` connect `GrokCharterPaperTrader` to `Матрица проверок риск-менеджмента (tests_risk.py)`, `SimDatabase`, `.monitor_and_manage_shadow_positions`, `AutoGovernor`, `.run_cycle`, `Спецификация: Risk Management & Budget Protection v2`, `.test_dynamic_risk_cap_for_ceiling_contracts`, `trader.py`, `.partition_markets`, `.is_social_mention_count_trap`, `.test_shadow_candidate_funnel_not_starved`?**
  _High betweenness centrality (0.119) - this node is a cross-community bridge._