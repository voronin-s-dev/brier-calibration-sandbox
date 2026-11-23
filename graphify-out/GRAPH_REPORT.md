# Graph Report - Polymarket-Sim  (2026-11-23)

## Corpus Check
- 34 files · ~165,664 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 6 file(s) not represented in the graph (top: (none) 4, .db 1, .ini 1)

## Summary
- 464 nodes · 1198 edges · 29 communities (16 shown, 13 thin omitted)
- Extraction: 77% EXTRACTED · 23% INFERRED · 0% AMBIGUOUS · INFERRED: 272 edges (avg confidence: 0.89)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `48146b9c`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- CryptoOracle
- SimDatabase
- WeatherOracle
- TestShadowTrader
- Разбор 2026-11-11: преждевременная отправка дневного дайджеста в 02:00 ночи сразу после смены даты по UTC
- AutoGovernor
- 🧠 Реестр авто-доработок и полуавтоматических решений (Auto-Governor)
- 📊 Отчёт симулятора Polymarket (Устав Grok Bot — Демо-счёт)
- README.md
- Polymarket Simulation and Agentic Market Architecture
- MarketInfo
- .test_reports_cadence_stale_warning
- NewsAndOrderbookOracle
- Acceptance Gates: Polymarket Simulation Daily Audit & Auto-Refinement
- extract_event_key
- Разбор 2026-11-07: ложное утверждение об остановке симулятора из-за локального статуса
- GrokCharterPaperTrader
- .test_e2e_dual_track_execution
- Спецификация: Risk Management & Budget Protection v2
- trader.py
- Разбор 2026-11-03: Стагнация капитала, фиктивная альфа оракула и паралич слотов
- TestRiskManagementV2
- .test_multi_category_filter_partitioning

## God Nodes (most connected - your core abstractions)
1. `SimDatabase` - 80 edges
2. `TestRiskManagementV2` - 66 edges
3. `GrokCharterPaperTrader` - 61 edges
4. `MarketInfo` - 52 edges
5. `AutoGovernor` - 30 edges
6. `generate_reports()` - 22 edges
7. `EvaluationResult` - 22 edges
8. `main()` - 22 edges
9. `send_telegram_alert()` - 20 edges
10. `WeatherOracle` - 18 edges

## Surprising Connections (you probably didn't know these)
- `Global Constraints` --references--> `simulate_clob_sell_shares()`  [INFERRED]
  docs/superpowers/plans/2026-10-28-shadow-portfolio.md → polymarket_api.py
- `Лестница исправления AAR (Fix Ladder)` --references--> `AutoGovernor`  [INFERRED]
  .agents/aar/checks-map.md → auto_governor.py
- `3. Реализация (How)` --references--> `AutoGovernor`  [INFERRED]
  .specs/archive/2026-10-25_risk_management_v2.md → auto_governor.py
- `Task 2: Shadow Market Evaluation & Position Lifecycle in `trader.py`` --references--> `simulate_clob_sell_shares()`  [INFERRED]
  docs/superpowers/plans/2026-10-28-shadow-portfolio.md → polymarket_api.py
- `Исправления` --references--> `main()`  [INFERRED]
  .agents/aar/runs/2026-11-10-shadow-missing-attribute-time-exit-aar.md → run_sim.py

## Import Cycles
- None detected.

## Communities (29 total, 13 thin omitted)

### Community 1 - "SimDatabase"
Cohesion: 0.06
Nodes (11): generate_reports(), SimDatabase, Review Focus, Task 1: Shadow Portfolio Database Schema & Access Layer, Task 3: Auto-Governor Tier 2 Shadow Category Unfreeze Rule, Task 4: Reporting & Dashboard Integration, Task 5: End-to-End Simulation & Verification, print_console_summary() (+3 more)

### Community 3 - "TestShadowTrader"
Cohesion: 0.16
Nodes (6): Ведомость, Исправления, Разбор 2026-11-10: сбой циклов из-за отсутствующего поля MIN_HOURS_TO_CLOSE_EXIT при появлении теневых позиций, Чем доказано, что ловится, make_market_info(), TestShadowTrader

### Community 4 - "Разбор 2026-11-11: преждевременная отправка дневного дайджеста в 02:00 ночи сразу после смены даты по UTC"
Cohesion: 0.22
Nodes (6): Ведомость, Исправления, Первопричина (Root Cause), Разбор 2026-11-11: преждевременная отправка дневного дайджеста в 02:00 ночи сразу после смены даты по UTC, check_and_send_daily_digest(), _plural_deals()

### Community 5 - "AutoGovernor"
Cohesion: 0.08
Nodes (13): Карта проверок проекта (Checks Map): Polymarket-Sim, Когда направление обязательно, Лестница исправления AAR (Fix Ladder), Направления проверок, Ведомость, Исправления, Первопричина (Root Cause), Разбор 2026-11-10: троекратное дублирование уведомления об одобрении доработки #22 в Telegram (+5 more)

### Community 6 - "🧠 Реестр авто-доработок и полуавтоматических решений (Auto-Governor)"
Cohesion: 0.25
Nodes (7): 🛠️ История применённых авто-фиксов и одобренных правок (25), 🟡 Ожидают твоего решения (Полуавтоматический режим: 1), ⚪ Отклонённые и утратившие актуальность предложения (12), Предложение #34: Разморозка категории Crypto: стабильный плюс в песочнице ($+6.78) (`TIER_2_CALIBRATION`), 🧠 Реестр авто-доработок и полуавтоматических решений (Auto-Governor), 🧪 Результаты теневой песочницы (Shadow Sandbox), ⚙️ Текущие активные параметры риск-менеджмента

### Community 7 - "📊 Отчёт симулятора Polymarket (Устав Grok Bot — Демо-счёт)"
Cohesion: 0.25
Nodes (7): Доходность по замороженным категориям (Песочница), 📂 Открытые позиции (0 / 8), Открытые позиции в песочнице (4 / 5), 📊 Отчёт симулятора Polymarket (Устав Grok Bot — Демо-счёт), 🔍 Последние проверенные кандидаты и фильтр стакана CLOB, 💰 Состояние виртуального портфеля, 🧪 Теневая песочница (Shadow Sandbox)

### Community 9 - "Polymarket Simulation and Agentic Market Architecture"
Cohesion: 0.40
Nodes (4): 1. Multi-Agent Role Decomposition, 2. Scraping and Resource Optimization (Obscura Integration), 3. Simulation Verification (Unlazy Integration), Polymarket Simulation and Agentic Market Architecture

### Community 10 - "MarketInfo"
Cohesion: 0.14
Nodes (6): calibrate_probability(), EvaluationResult, HighConvictionFactOracle, is_esports_market(), MarketInfo, _mk()

### Community 12 - ".test_reports_cadence_stale_warning"
Cohesion: 0.38
Nodes (4): Ведомость, Исправления, Разбор 2026-11-07: подмена 10-минутного мониторинга уставного бота задержкой бесплатного GitHub Actions, Чем доказано, что ловится

### Community 14 - "Acceptance Gates: Polymarket Simulation Daily Audit & Auto-Refinement"
Cohesion: 0.33
Nodes (5): Acceptance Gates: Polymarket Simulation Daily Audit & Auto-Refinement, Gate 1: Unit & Behavior Risk Tests, Gate 2: Full Test Suite, Gate 3: Auto-Governor & Status Inspection, Gate 4: Knowledge Graph Synchronization

### Community 19 - "Разбор 2026-11-07: ложное утверждение об остановке симулятора из-за локального статуса"
Cohesion: 0.40
Nodes (4): Ведомость, Исправления, Разбор 2026-11-07: ложное утверждение об остановке симулятора из-за локального статуса, Чем доказано, что ловится

### Community 21 - ".test_e2e_dual_track_execution"
Cohesion: 0.25
Nodes (4): make_market(), TestE2EShadowPortfolio, side_effect_buy(), side_effect_eval()

### Community 22 - "Спецификация: Risk Management & Budget Protection v2"
Cohesion: 0.40
Nodes (4): 1. Зачем (Why), 2. Требования (Requirements), 4. Чеклист верификации, Спецификация: Risk Management & Budget Protection v2

### Community 23 - "trader.py"
Cohesion: 0.05
Nodes (19): fetch_polymarket_json(), fetch_standard_url(), resolve_secure_ip(), norm_cdf(), classify_market_category(), extract_resolution_source(), fetch_active_markets(), fetch_clob_book() (+11 more)

### Community 24 - "Разбор 2026-11-03: Стагнация капитала, фиктивная альфа оракула и паралич слотов"
Cohesion: 0.50
Nodes (3): Ведомость, Разбор 2026-11-03: Стагнация капитала, фиктивная альфа оракула и паралич слотов, Чем доказано, что ловится

### Community 26 - "TestRiskManagementV2"
Cohesion: 0.09
Nodes (5): Матрица проверок риск-менеджмента (tests_risk.py), Исправления, TestRiskManagementV2, _mk(), _mk()

## Knowledge Gaps
- **13 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `SimDatabase` connect `SimDatabase` to `TestShadowTrader`, `AutoGovernor`, `MarketInfo`, `.run_cycle`, `.open_position`, `GrokCharterPaperTrader`, `.test_e2e_dual_track_execution`, `trader.py`, `TestRiskManagementV2`, `.test_multi_category_filter_partitioning`?**
  _High betweenness centrality (0.209) - this node is a cross-community bridge._
- **Are the 11 inferred relationships involving `SimDatabase` (e.g. with `AutoGovernor` and `generate_reports()`) actually correct?**
  _`SimDatabase` has 11 INFERRED edges - model-reasoned connections that need verification._
- **Should `SimDatabase` be split into smaller, more focused modules?**
  _Cohesion score 0.058549931600547195 - nodes in this community are weakly interconnected._
- **Why does `TestRiskManagementV2` connect `TestRiskManagementV2` to `CryptoOracle`, `SimDatabase`, `WeatherOracle`, `Разбор 2026-11-11: преждевременная отправка дневного дайджеста в 02:00 ночи сразу после смены даты по UTC`, `AutoGovernor`, `MarketInfo`, `.run_cycle`, `NewsAndOrderbookOracle`, `extract_event_key`, `.open_position`, `.compute_kelly_sizing`, `.partition_markets`, `GrokCharterPaperTrader`, `trader.py`, `.is_social_mention_count_trap`, `.is_soccer_draw_trap`, `.test_multi_category_filter_partitioning`?**
  _High betweenness centrality (0.191) - this node is a cross-community bridge._
- **Are the 10 inferred relationships involving `TestRiskManagementV2` (e.g. with `AutoGovernor` and `SimDatabase`) actually correct?**
  _`TestRiskManagementV2` has 10 INFERRED edges - model-reasoned connections that need verification._
- **Should `AutoGovernor` be split into smaller, more focused modules?**
  _Cohesion score 0.08067226890756303 - nodes in this community are weakly interconnected._
- **Why does `GrokCharterPaperTrader` connect `GrokCharterPaperTrader` to `CryptoOracle`, `SimDatabase`, `WeatherOracle`, `TestShadowTrader`, `AutoGovernor`, `MarketInfo`, `.run_cycle`, `NewsAndOrderbookOracle`, `extract_event_key`, `.open_position`, `.compute_kelly_sizing`, `.partition_markets`, `.test_e2e_dual_track_execution`, `trader.py`, `.is_social_mention_count_trap`, `TestRiskManagementV2`, `.is_soccer_draw_trap`, `.test_multi_category_filter_partitioning`?**
  _High betweenness centrality (0.120) - this node is a cross-community bridge._