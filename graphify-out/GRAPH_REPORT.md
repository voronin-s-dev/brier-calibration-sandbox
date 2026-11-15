# Graph Report - Polymarket-Sim  (2026-11-15)

## Corpus Check
- 34 files · ~104,783 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 7 file(s) not represented in the graph (top: (none) 5, .db 1, .ini 1)

## Summary
- 421 nodes · 1092 edges · 17 communities (16 shown, 1 thin omitted)
- Extraction: 77% EXTRACTED · 23% INFERRED · 0% AMBIGUOUS · INFERRED: 250 edges (avg confidence: 0.9)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `1077cc59`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- GrokCharterPaperTrader
- SimDatabase
- TestRiskManagementV2
- .test_e2e_dual_track_execution
- AutoGovernor
- http_tls.py
- 🧠 Реестр авто-доработок и полуавтоматических решений (Auto-Governor)
- 📊 Отчёт симулятора Polymarket (Устав Grok Bot — Демо-счёт)
- README.md
- Polymarket Simulation and Agentic Market Architecture
- .monitor_and_manage_shadow_positions
- Acceptance Gates: Polymarket Simulation Daily Audit & Auto-Refinement
- trader.py
- Разбор 2026-11-07: ложное утверждение об остановке симулятора из-за локального статуса
- Разбор 2026-11-11: преждевременная отправка дневного дайджеста в 02:00 ночи сразу после смены даты по UTC
- 3. Реализация (How)
- Разбор 2026-11-03: Стагнация капитала, фиктивная альфа оракула и паралич слотов

## God Nodes (most connected - your core abstractions)
1. `SimDatabase` - 72 edges
2. `GrokCharterPaperTrader` - 53 edges
3. `TestRiskManagementV2` - 48 edges
4. `MarketInfo` - 46 edges
5. `AutoGovernor` - 30 edges
6. `generate_reports()` - 22 edges
7. `main()` - 22 edges
8. `EvaluationResult` - 20 edges
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

## Communities (17 total, 1 thin omitted)

### Community 0 - "GrokCharterPaperTrader"
Cohesion: 0.06
Nodes (10): Global Constraints, Shadow Portfolio (Sandbox) Implementation Plan, Task 2: Shadow Market Evaluation & Position Lifecycle in `trader.py`, fetch_clob_book(), fetch_market_by_id(), simulate_clob_buy_and_exit_check(), simulate_clob_sell_shares(), 3. Реализация (How) (+2 more)

### Community 1 - "SimDatabase"
Cohesion: 0.05
Nodes (14): Ведомость, Исправления, Разбор 2026-11-07: подмена 10-минутного мониторинга уставного бота задержкой бесплатного GitHub Actions, Чем доказано, что ловится, generate_reports(), SimDatabase, Review Focus, Task 1: Shadow Portfolio Database Schema & Access Layer (+6 more)

### Community 2 - "TestRiskManagementV2"
Cohesion: 0.06
Nodes (14): Матрица проверок риск-менеджмента (tests_risk.py), Исправления, calibrate_probability(), EvaluationResult, HighConvictionFactOracle, is_esports_market(), NewsAndOrderbookOracle, norm_cdf() (+6 more)

### Community 3 - ".test_e2e_dual_track_execution"
Cohesion: 0.25
Nodes (4): make_market(), TestE2EShadowPortfolio, side_effect_buy(), side_effect_eval()

### Community 4 - "AutoGovernor"
Cohesion: 0.09
Nodes (15): Карта проверок проекта (Checks Map): Polymarket-Sim, Когда направление обязательно, Лестница исправления AAR (Fix Ladder), Направления проверок, Ведомость, Исправления, Первопричина (Root Cause), Разбор 2026-11-10: троекратное дублирование уведомления об одобрении доработки #22 в Telegram (+7 more)

### Community 5 - "http_tls.py"
Cohesion: 0.11
Nodes (5): fetch_polymarket_json(), fetch_standard_url(), resolve_secure_ip(), CryptoOracle, trigger_workflow()

### Community 6 - "🧠 Реестр авто-доработок и полуавтоматических решений (Auto-Governor)"
Cohesion: 0.29
Nodes (6): 🛠️ История применённых авто-фиксов и одобренных правок (20), 🟡 Ожидают твоего решения (Полуавтоматический режим: 0), ⚪ Отклонённые и утратившие актуальность предложения (5), 🧠 Реестр авто-доработок и полуавтоматических решений (Auto-Governor), 🧪 Результаты теневой песочницы (Shadow Sandbox), ⚙️ Текущие активные параметры риск-менеджмента

### Community 7 - "📊 Отчёт симулятора Polymarket (Устав Grok Bot — Демо-счёт)"
Cohesion: 0.25
Nodes (7): Доходность по замороженным категориям (Песочница), 📂 Открытые позиции (4 / 8), Открытые позиции в песочнице (4 / 5), 📊 Отчёт симулятора Polymarket (Устав Grok Bot — Демо-счёт), 🔍 Последние проверенные кандидаты и фильтр стакана CLOB, 💰 Состояние виртуального портфеля, 🧪 Теневая песочница (Shadow Sandbox)

### Community 9 - "Polymarket Simulation and Agentic Market Architecture"
Cohesion: 0.40
Nodes (4): 1. Multi-Agent Role Decomposition, 2. Scraping and Resource Optimization (Obscura Integration), 3. Simulation Verification (Unlazy Integration), Polymarket Simulation and Agentic Market Architecture

### Community 13 - ".monitor_and_manage_shadow_positions"
Cohesion: 0.14
Nodes (6): Ведомость, Исправления, Разбор 2026-11-10: сбой циклов из-за отсутствующего поля MIN_HOURS_TO_CLOSE_EXIT при появлении теневых позиций, Чем доказано, что ловится, make_market_info(), TestShadowTrader

### Community 14 - "Acceptance Gates: Polymarket Simulation Daily Audit & Auto-Refinement"
Cohesion: 0.33
Nodes (5): Acceptance Gates: Polymarket Simulation Daily Audit & Auto-Refinement, Gate 1: Unit & Behavior Risk Tests, Gate 2: Full Test Suite, Gate 3: Auto-Governor & Status Inspection, Gate 4: Knowledge Graph Synchronization

### Community 17 - "trader.py"
Cohesion: 0.09
Nodes (7): WeatherOracle, classify_market_category(), extract_resolution_source(), fetch_active_markets(), OrderBookSimulation, parse_market_dict(), parse_canonical_date_or_range()

### Community 19 - "Разбор 2026-11-07: ложное утверждение об остановке симулятора из-за локального статуса"
Cohesion: 0.40
Nodes (4): Ведомость, Исправления, Разбор 2026-11-07: ложное утверждение об остановке симулятора из-за локального статуса, Чем доказано, что ловится

### Community 20 - "Разбор 2026-11-11: преждевременная отправка дневного дайджеста в 02:00 ночи сразу после смены даты по UTC"
Cohesion: 0.14
Nodes (7): Ведомость, Исправления, Первопричина (Root Cause), Разбор 2026-11-11: преждевременная отправка дневного дайджеста в 02:00 ночи сразу после смены даты по UTC, check_and_send_daily_digest(), notify_position_closed(), _plural_deals()

### Community 22 - "3. Реализация (How)"
Cohesion: 0.40
Nodes (4): 1. Зачем (Why), 2. Требования (Requirements), 4. Чеклист верификации, Спецификация: Risk Management & Budget Protection v2

### Community 26 - "Разбор 2026-11-03: Стагнация капитала, фиктивная альфа оракула и паралич слотов"
Cohesion: 0.50
Nodes (3): Ведомость, Разбор 2026-11-03: Стагнация капитала, фиктивная альфа оракула и паралич слотов, Чем доказано, что ловится

## Knowledge Gaps
- **1 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `SimDatabase` connect `SimDatabase` to `GrokCharterPaperTrader`, `TestRiskManagementV2`, `.test_e2e_dual_track_execution`, `AutoGovernor`, `.monitor_and_manage_shadow_positions`, `trader.py`?**
  _High betweenness centrality (0.207) - this node is a cross-community bridge._
- **Are the 11 inferred relationships involving `SimDatabase` (e.g. with `AutoGovernor` and `generate_reports()`) actually correct?**
  _`SimDatabase` has 11 INFERRED edges - model-reasoned connections that need verification._
- **Should `GrokCharterPaperTrader` be split into smaller, more focused modules?**
  _Cohesion score 0.06095791001451379 - nodes in this community are weakly interconnected._
- **Why does `TestRiskManagementV2` connect `TestRiskManagementV2` to `GrokCharterPaperTrader`, `SimDatabase`, `AutoGovernor`, `trader.py`, `Разбор 2026-11-11: преждевременная отправка дневного дайджеста в 02:00 ночи сразу после смены даты по UTC`?**
  _High betweenness centrality (0.137) - this node is a cross-community bridge._
- **Are the 17 inferred relationships involving `GrokCharterPaperTrader` (e.g. with `Исправления` and `Shadow Portfolio (Sandbox) Implementation Plan`) actually correct?**
  _`GrokCharterPaperTrader` has 17 INFERRED edges - model-reasoned connections that need verification._
- **Should `SimDatabase` be split into smaller, more focused modules?**
  _Cohesion score 0.05307709906199954 - nodes in this community are weakly interconnected._
- **Why does `GrokCharterPaperTrader` connect `GrokCharterPaperTrader` to `SimDatabase`, `TestRiskManagementV2`, `.test_e2e_dual_track_execution`, `AutoGovernor`, `http_tls.py`, `.monitor_and_manage_shadow_positions`, `trader.py`?**
  _High betweenness centrality (0.117) - this node is a cross-community bridge._