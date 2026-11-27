# Graph Report - Polymarket-Sim  (2026-11-27)

## Corpus Check
- 35 files · ~191,476 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 6 file(s) not represented in the graph (top: (none) 4, .db 1, .ini 1)

## Summary
- 509 nodes · 1313 edges · 26 communities (15 shown, 11 thin omitted)
- Extraction: 78% EXTRACTED · 22% INFERRED · 0% AMBIGUOUS · INFERRED: 287 edges (avg confidence: 0.89)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `f23fd9b6`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- Матрица проверок риск-менеджмента (tests_risk.py)
- SimDatabase
- extract_event_key
- Спецификация: Risk Management & Budget Protection v2
- SportsOddsOracle
- AutoGovernor
- 🧠 Реестр авто-доработок и полуавтоматических решений (Auto-Governor)
- 📊 Отчёт симулятора Polymarket (Устав Grok Bot — Демо-счёт)
- README.md
- Polymarket Simulation and Agentic Market Architecture
- MarketInfo
- GrokCharterPaperTrader
- .test_reports_cadence_stale_warning
- Разбор 2026-11-03: Стагнация капитала, фиктивная альфа оракула и паралич слотов
- Acceptance Gates: Polymarket Simulation Daily Audit & Auto-Refinement
- Разбор 2026-11-11: преждевременная отправка дневного дайджеста в 02:00 ночи сразу после смены даты по UTC
- Разбор 2026-11-07: ложное утверждение об остановке симулятора из-за локального статуса
- .compute_kelly_sizing
- trader.py
- .monitor_and_manage_shadow_positions
- TestRiskManagementV2

## God Nodes (most connected - your core abstractions)
1. `SimDatabase` - 82 edges
2. `TestRiskManagementV2` - 77 edges
3. `GrokCharterPaperTrader` - 64 edges
4. `MarketInfo` - 62 edges
5. `AutoGovernor` - 30 edges
6. `EvaluationResult` - 23 edges
7. `generate_reports()` - 22 edges
8. `main()` - 22 edges
9. `send_telegram_alert()` - 20 edges
10. `WeatherOracle` - 19 edges

## Surprising Connections (you probably didn't know these)
- `Global Constraints` --references--> `simulate_clob_sell_shares()`  [INFERRED]
  docs/superpowers/plans/2026-10-28-shadow-portfolio.md → polymarket_api.py
- `Ведомость` --references--> `check_and_send_daily_digest()`  [INFERRED]
  .agents/aar/runs/2026-11-11-daily-digest-midnight-early-trigger-aar.md → telegram_notify.py
- `Лестница исправления AAR (Fix Ladder)` --references--> `AutoGovernor`  [INFERRED]
  .agents/aar/checks-map.md → auto_governor.py
- `3. Реализация (How)` --references--> `AutoGovernor`  [INFERRED]
  .specs/archive/2026-10-25_risk_management_v2.md → auto_governor.py
- `Task 2: Shadow Market Evaluation & Position Lifecycle in `trader.py`` --references--> `simulate_clob_sell_shares()`  [INFERRED]
  docs/superpowers/plans/2026-10-28-shadow-portfolio.md → polymarket_api.py

## Import Cycles
- None detected.

## Communities (26 total, 11 thin omitted)

### Community 1 - "SimDatabase"
Cohesion: 0.05
Nodes (15): generate_reports(), SimDatabase, Review Focus, Task 1: Shadow Portfolio Database Schema & Access Layer, Task 2: Shadow Market Evaluation & Position Lifecycle in `trader.py`, Task 3: Auto-Governor Tier 2 Shadow Category Unfreeze Rule, Task 4: Reporting & Dashboard Integration, Task 5: End-to-End Simulation & Verification (+7 more)

### Community 2 - "extract_event_key"
Cohesion: 0.11
Nodes (3): TestHoldoutInvariants, extract_event_key(), parse_canonical_date_or_range()

### Community 3 - "Спецификация: Risk Management & Budget Protection v2"
Cohesion: 0.40
Nodes (4): 1. Зачем (Why), 2. Требования (Requirements), 4. Чеклист верификации, Спецификация: Risk Management & Budget Protection v2

### Community 5 - "AutoGovernor"
Cohesion: 0.07
Nodes (14): Карта проверок проекта (Checks Map): Polymarket-Sim, Когда направление обязательно, Лестница исправления AAR (Fix Ladder), Направления проверок, Ведомость, Исправления, Первопричина (Root Cause), Разбор 2026-11-10: троекратное дублирование уведомления об одобрении доработки #22 в Telegram (+6 more)

### Community 6 - "🧠 Реестр авто-доработок и полуавтоматических решений (Auto-Governor)"
Cohesion: 0.25
Nodes (7): 🛠️ История применённых авто-фиксов и одобренных правок (27), 🟡 Ожидают твоего решения (Полуавтоматический режим: 1), ⚪ Отклонённые и утратившие актуальность предложения (12), Предложение #34: Разморозка категории Crypto: стабильный плюс в песочнице ($+6.78) (`TIER_2_CALIBRATION`), 🧠 Реестр авто-доработок и полуавтоматических решений (Auto-Governor), 🧪 Результаты теневой песочницы (Shadow Sandbox), ⚙️ Текущие активные параметры риск-менеджмента

### Community 7 - "📊 Отчёт симулятора Polymarket (Устав Grok Bot — Демо-счёт)"
Cohesion: 0.29
Nodes (6): Доходность по замороженным категориям (Песочница), 📂 Открытые позиции (0 / 8), 📊 Отчёт симулятора Polymarket (Устав Grok Bot — Демо-счёт), 🔍 Последние проверенные кандидаты и фильтр стакана CLOB, 💰 Состояние виртуального портфеля, 🧪 Теневая песочница (Shadow Sandbox)

### Community 9 - "Polymarket Simulation and Agentic Market Architecture"
Cohesion: 0.33
Nodes (5): 1. Multi-Agent Role Decomposition, 2. Scraping and Resource Optimization (Obscura Integration), 3. Simulation Verification (Unlazy Integration), 4. Holdout Scenario Isolation (Judge Gate), Polymarket Simulation and Agentic Market Architecture

### Community 10 - "MarketInfo"
Cohesion: 0.05
Nodes (11): CryptoOracle, HighConvictionFactOracle, is_esports_market(), NewsAndOrderbookOracle, norm_cdf(), WeatherOracle, MarketInfo, _mk() (+3 more)

### Community 12 - ".test_reports_cadence_stale_warning"
Cohesion: 0.38
Nodes (4): Ведомость, Исправления, Разбор 2026-11-07: подмена 10-минутного мониторинга уставного бота задержкой бесплатного GitHub Actions, Чем доказано, что ловится

### Community 13 - "Разбор 2026-11-03: Стагнация капитала, фиктивная альфа оракула и паралич слотов"
Cohesion: 0.50
Nodes (3): Ведомость, Разбор 2026-11-03: Стагнация капитала, фиктивная альфа оракула и паралич слотов, Чем доказано, что ловится

### Community 14 - "Acceptance Gates: Polymarket Simulation Daily Audit & Auto-Refinement"
Cohesion: 0.29
Nodes (6): Acceptance Gates: Polymarket Simulation Daily Audit & Auto-Refinement, Gate 1: Unit & Behavior Risk Tests, Gate 2: Full Test Suite, Gate 3: Auto-Governor & Status Inspection, Gate 4: Knowledge Graph Synchronization, Gate 5: Holdout Scenario Isolation (Judge Gate)

### Community 17 - "Разбор 2026-11-11: преждевременная отправка дневного дайджеста в 02:00 ночи сразу после смены даты по UTC"
Cohesion: 0.29
Nodes (4): Ведомость, Исправления, Первопричина (Root Cause), Разбор 2026-11-11: преждевременная отправка дневного дайджеста в 02:00 ночи сразу после смены даты по UTC

### Community 19 - "Разбор 2026-11-07: ложное утверждение об остановке симулятора из-за локального статуса"
Cohesion: 0.40
Nodes (4): Ведомость, Исправления, Разбор 2026-11-07: ложное утверждение об остановке симулятора из-за локального статуса, Чем доказано, что ловится

### Community 23 - "trader.py"
Cohesion: 0.05
Nodes (20): fetch_polymarket_json(), fetch_standard_url(), resolve_secure_ip(), calibrate_probability(), classify_market_category(), extract_resolution_source(), fetch_active_markets(), fetch_clob_book() (+12 more)

### Community 24 - ".monitor_and_manage_shadow_positions"
Cohesion: 0.14
Nodes (6): Ведомость, Исправления, Разбор 2026-11-10: сбой циклов из-за отсутствующего поля MIN_HOURS_TO_CLOSE_EXIT при появлении теневых позиций, Чем доказано, что ловится, make_market_info(), TestShadowTrader

## Knowledge Gaps
- **11 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `TestRiskManagementV2` connect `TestRiskManagementV2` to `Матрица проверок риск-менеджмента (tests_risk.py)`, `SimDatabase`, `extract_event_key`, `.is_soccer_draw_trap`, `SportsOddsOracle`, `AutoGovernor`, `MarketInfo`, `GrokCharterPaperTrader`, `.open_position`, `Разбор 2026-11-11: преждевременная отправка дневного дайджеста в 02:00 ночи сразу после смены даты по UTC`, `.monitor_and_manage_open_positions`, `.compute_kelly_sizing`, `.run_cycle`, `trader.py`, `.is_social_mention_count_trap`?**
  _High betweenness centrality (0.211) - this node is a cross-community bridge._
- **Are the 11 inferred relationships involving `SimDatabase` (e.g. with `AutoGovernor` and `generate_reports()`) actually correct?**
  _`SimDatabase` has 11 INFERRED edges - model-reasoned connections that need verification._
- **Should `SimDatabase` be split into smaller, more focused modules?**
  _Cohesion score 0.05388151174668029 - nodes in this community are weakly interconnected._
- **Why does `SimDatabase` connect `SimDatabase` to `Матрица проверок риск-менеджмента (tests_risk.py)`, `AutoGovernor`, `MarketInfo`, `GrokCharterPaperTrader`, `.open_position`, `.monitor_and_manage_open_positions`, `.run_cycle`, `trader.py`, `.monitor_and_manage_shadow_positions`, `TestRiskManagementV2`?**
  _High betweenness centrality (0.194) - this node is a cross-community bridge._
- **Are the 11 inferred relationships involving `TestRiskManagementV2` (e.g. with `AutoGovernor` and `SimDatabase`) actually correct?**
  _`TestRiskManagementV2` has 11 INFERRED edges - model-reasoned connections that need verification._
- **Should `extract_event_key` be split into smaller, more focused modules?**
  _Cohesion score 0.1111111111111111 - nodes in this community are weakly interconnected._
- **Why does `GrokCharterPaperTrader` connect `GrokCharterPaperTrader` to `Матрица проверок риск-менеджмента (tests_risk.py)`, `SimDatabase`, `.is_soccer_draw_trap`, `SportsOddsOracle`, `AutoGovernor`, `MarketInfo`, `.open_position`, `.monitor_and_manage_open_positions`, `.compute_kelly_sizing`, `.run_cycle`, `trader.py`, `.monitor_and_manage_shadow_positions`, `TestRiskManagementV2`, `.is_social_mention_count_trap`?**
  _High betweenness centrality (0.118) - this node is a cross-community bridge._