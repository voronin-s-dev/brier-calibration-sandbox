# Graph Report - Polymarket-Sim  (2026-11-12)

## Corpus Check
- 34 files · ~87,009 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 6 file(s) not represented in the graph (top: (none) 4, .db 1, .ini 1)

## Summary
- 409 nodes · 1050 edges · 16 communities (14 shown, 2 thin omitted)
- Extraction: 77% EXTRACTED · 23% INFERRED · 0% AMBIGUOUS · INFERRED: 240 edges (avg confidence: 0.9)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `bb447b41`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- GrokCharterPaperTrader
- SimDatabase
- MarketInfo
- polymarket_api.py
- AutoGovernor
- CryptoOracle
- 🧠 Реестр авто-доработок и полуавтоматических решений (Auto-Governor)
- 📊 Отчёт симулятора Polymarket (Устав Grok Bot — Демо-счёт)
- README.md
- Polymarket Simulation and Agentic Market Architecture
- telegram_notify.py
- Матрица проверок риск-менеджмента (tests_risk.py)
- Acceptance Gates: Polymarket Simulation Daily Audit & Auto-Refinement
- .test_reports_cadence_stale_warning
- test_e2e_shadow.py
- Разбор 2026-11-07: ложное утверждение об остановке симулятора из-за локального статуса

## God Nodes (most connected - your core abstractions)
1. `SimDatabase` - 69 edges
2. `GrokCharterPaperTrader` - 51 edges
3. `MarketInfo` - 44 edges
4. `TestRiskManagementV2` - 44 edges
5. `AutoGovernor` - 30 edges
6. `generate_reports()` - 22 edges
7. `main()` - 20 edges
8. `EvaluationResult` - 19 edges
9. `send_telegram_alert()` - 18 edges
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

## Communities (16 total, 2 thin omitted)

### Community 0 - "GrokCharterPaperTrader"
Cohesion: 0.06
Nodes (11): Ведомость, Исправления, Разбор 2026-11-10: сбой циклов из-за отсутствующего поля MIN_HOURS_TO_CLOSE_EXIT при появлении теневых позиций, Чем доказано, что ловится, Global Constraints, Shadow Portfolio (Sandbox) Implementation Plan, Task 2: Shadow Market Evaluation & Position Lifecycle in `trader.py`, simulate_clob_sell_shares() (+3 more)

### Community 1 - "SimDatabase"
Cohesion: 0.07
Nodes (11): generate_reports(), SimDatabase, Review Focus, Task 1: Shadow Portfolio Database Schema & Access Layer, Task 3: Auto-Governor Tier 2 Shadow Category Unfreeze Rule, Task 4: Reporting & Dashboard Integration, Task 5: End-to-End Simulation & Verification, print_console_summary() (+3 more)

### Community 2 - "MarketInfo"
Cohesion: 0.07
Nodes (12): calibrate_probability(), EvaluationResult, HighConvictionFactOracle, is_esports_market(), NewsAndOrderbookOracle, norm_cdf(), WeatherOracle, MarketInfo (+4 more)

### Community 3 - "polymarket_api.py"
Cohesion: 0.09
Nodes (11): fetch_polymarket_json(), fetch_standard_url(), resolve_secure_ip(), classify_market_category(), extract_resolution_source(), fetch_active_markets(), fetch_clob_book(), fetch_market_by_id() (+3 more)

### Community 4 - "AutoGovernor"
Cohesion: 0.16
Nodes (3): AutoGovernor, git_sync_snapshot(), main()

### Community 6 - "🧠 Реестр авто-доработок и полуавтоматических решений (Auto-Governor)"
Cohesion: 0.33
Nodes (5): 🛠️ История применённых авто-фиксов и одобренных правок (19), 🟡 Ожидают твоего решения (Полуавтоматический режим: 0), ⚪ Отклонённые и утратившие актуальность предложения (4), 🧠 Реестр авто-доработок и полуавтоматических решений (Auto-Governor), ⚙️ Текущие активные параметры риск-менеджмента

### Community 7 - "📊 Отчёт симулятора Polymarket (Устав Grok Bot — Демо-счёт)"
Cohesion: 0.25
Nodes (7): Доходность по замороженным категориям (Песочница), 📂 Открытые позиции (7 / 8), Открытые позиции в песочнице (3 / 5), 📊 Отчёт симулятора Polymarket (Устав Grok Bot — Демо-счёт), 🔍 Последние проверенные кандидаты и фильтр стакана CLOB, 💰 Состояние виртуального портфеля, 🧪 Теневая песочница (Shadow Sandbox)

### Community 9 - "Polymarket Simulation and Agentic Market Architecture"
Cohesion: 0.40
Nodes (4): 1. Multi-Agent Role Decomposition, 2. Scraping and Resource Optimization (Obscura Integration), 3. Simulation Verification (Unlazy Integration), Polymarket Simulation and Agentic Market Architecture

### Community 10 - "telegram_notify.py"
Cohesion: 0.08
Nodes (15): Ведомость, Исправления, Первопричина (Root Cause), Разбор 2026-11-10: троекратное дублирование уведомления об одобрении доработки #22 в Telegram, Ведомость, Исправления, Первопричина (Root Cause), Разбор 2026-11-11: преждевременная отправка дневного дайджеста в 02:00 ночи сразу после смены даты по UTC (+7 more)

### Community 12 - "Матрица проверок риск-менеджмента (tests_risk.py)"
Cohesion: 0.06
Nodes (16): Карта проверок проекта (Checks Map): Polymarket-Sim, Когда направление обязательно, Лестница исправления AAR (Fix Ladder), Матрица проверок риск-менеджмента (tests_risk.py), Направления проверок, Ведомость, Исправления, Разбор 2026-11-03: Стагнация капитала, фиктивная альфа оракула и паралич слотов (+8 more)

### Community 14 - "Acceptance Gates: Polymarket Simulation Daily Audit & Auto-Refinement"
Cohesion: 0.33
Nodes (5): Acceptance Gates: Polymarket Simulation Daily Audit & Auto-Refinement, Gate 1: Unit & Behavior Risk Tests, Gate 2: Full Test Suite, Gate 3: Auto-Governor & Status Inspection, Gate 4: Knowledge Graph Synchronization

### Community 15 - ".test_reports_cadence_stale_warning"
Cohesion: 0.38
Nodes (4): Ведомость, Исправления, Разбор 2026-11-07: подмена 10-минутного мониторинга уставного бота задержкой бесплатного GitHub Actions, Чем доказано, что ловится

### Community 17 - "test_e2e_shadow.py"
Cohesion: 0.12
Nodes (4): make_market(), TestE2EShadowPortfolio, side_effect_buy(), side_effect_eval()

### Community 19 - "Разбор 2026-11-07: ложное утверждение об остановке симулятора из-за локального статуса"
Cohesion: 0.40
Nodes (4): Ведомость, Исправления, Разбор 2026-11-07: ложное утверждение об остановке симулятора из-за локального статуса, Чем доказано, что ловится

## Knowledge Gaps
- **2 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `SimDatabase` connect `SimDatabase` to `GrokCharterPaperTrader`, `MarketInfo`, `AutoGovernor`, `Матрица проверок риск-менеджмента (tests_risk.py)`, `test_e2e_shadow.py`?**
  _High betweenness centrality (0.209) - this node is a cross-community bridge._
- **Are the 11 inferred relationships involving `SimDatabase` (e.g. with `AutoGovernor` and `generate_reports()`) actually correct?**
  _`SimDatabase` has 11 INFERRED edges - model-reasoned connections that need verification._
- **Should `GrokCharterPaperTrader` be split into smaller, more focused modules?**
  _Cohesion score 0.05974025974025974 - nodes in this community are weakly interconnected._
- **Why does `TestRiskManagementV2` connect `MarketInfo` to `GrokCharterPaperTrader`, `SimDatabase`, `AutoGovernor`, `telegram_notify.py`, `Матрица проверок риск-менеджмента (tests_risk.py)`?**
  _High betweenness centrality (0.131) - this node is a cross-community bridge._
- **Are the 17 inferred relationships involving `GrokCharterPaperTrader` (e.g. with `Исправления` and `Shadow Portfolio (Sandbox) Implementation Plan`) actually correct?**
  _`GrokCharterPaperTrader` has 17 INFERRED edges - model-reasoned connections that need verification._
- **Should `SimDatabase` be split into smaller, more focused modules?**
  _Cohesion score 0.06660006660006661 - nodes in this community are weakly interconnected._
- **Why does `GrokCharterPaperTrader` connect `GrokCharterPaperTrader` to `SimDatabase`, `MarketInfo`, `polymarket_api.py`, `AutoGovernor`, `CryptoOracle`, `Матрица проверок риск-менеджмента (tests_risk.py)`, `test_e2e_shadow.py`?**
  _High betweenness centrality (0.121) - this node is a cross-community bridge._