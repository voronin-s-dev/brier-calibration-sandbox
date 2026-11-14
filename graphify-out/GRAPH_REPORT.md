# Graph Report - Polymarket-Sim  (2026-11-13)

## Corpus Check
- 34 files · ~87,661 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 6 file(s) not represented in the graph (top: (none) 4, .db 1, .ini 1)

## Summary
- 417 nodes · 1077 edges · 29 communities (19 shown, 10 thin omitted)
- Extraction: 77% EXTRACTED · 23% INFERRED · 0% AMBIGUOUS · INFERRED: 246 edges (avg confidence: 0.9)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `dbe56183`
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
- http_tls.py
- TestRiskManagementV2
- .monitor_and_manage_shadow_positions
- Acceptance Gates: Polymarket Simulation Daily Audit & Auto-Refinement
- .test_reports_cadence_stale_warning
- .test_mature_consensus_oracle_strict_threshold
- extract_event_key
- Разбор 2026-11-07: ложное утверждение об остановке симулятора из-за локального статуса
- Разбор 2026-11-11: преждевременная отправка дневного дайджеста в 02:00 ночи сразу после смены даты по UTC
- oracles.py
- 3. Реализация (How)
- Карта проверок проекта (Checks Map): Polymarket-Sim
- HighConvictionFactOracle
- Разбор 2026-11-03: Стагнация капитала, фиктивная альфа оракула и паралич слотов
- .test_multi_category_filter_partitioning

## God Nodes (most connected - your core abstractions)
1. `SimDatabase` - 71 edges
2. `GrokCharterPaperTrader` - 53 edges
3. `TestRiskManagementV2` - 48 edges
4. `MarketInfo` - 46 edges
5. `AutoGovernor` - 30 edges
6. `generate_reports()` - 22 edges
7. `EvaluationResult` - 20 edges
8. `main()` - 20 edges
9. `send_telegram_alert()` - 18 edges
10. `WeatherOracle` - 16 edges

## Surprising Connections (you probably didn't know these)
- `Лестница исправления AAR (Fix Ladder)` --references--> `AutoGovernor`  [INFERRED]
  .agents/aar/checks-map.md → auto_governor.py
- `Global Constraints` --references--> `simulate_clob_sell_shares()`  [INFERRED]
  docs/superpowers/plans/2026-10-28-shadow-portfolio.md → polymarket_api.py
- `Ведомость` --references--> `check_and_send_daily_digest()`  [INFERRED]
  .agents/aar/runs/2026-11-11-daily-digest-midnight-early-trigger-aar.md → telegram_notify.py
- `3. Реализация (How)` --references--> `AutoGovernor`  [INFERRED]
  .specs/archive/2026-10-25_risk_management_v2.md → auto_governor.py
- `Task 2: Shadow Market Evaluation & Position Lifecycle in `trader.py`` --references--> `simulate_clob_sell_shares()`  [INFERRED]
  docs/superpowers/plans/2026-10-28-shadow-portfolio.md → polymarket_api.py

## Import Cycles
- None detected.

## Communities (29 total, 10 thin omitted)

### Community 1 - "SimDatabase"
Cohesion: 0.06
Nodes (17): generate_reports(), SimDatabase, Review Focus, Task 1: Shadow Portfolio Database Schema & Access Layer, Task 2: Shadow Market Evaluation & Position Lifecycle in `trader.py`, Task 3: Auto-Governor Tier 2 Shadow Category Unfreeze Rule, Task 4: Reporting & Dashboard Integration, Task 5: End-to-End Simulation & Verification (+9 more)

### Community 2 - "MarketInfo"
Cohesion: 0.15
Nodes (4): EvaluationResult, is_esports_market(), NewsAndOrderbookOracle, MarketInfo

### Community 3 - "polymarket_api.py"
Cohesion: 0.14
Nodes (9): classify_market_category(), extract_resolution_source(), fetch_active_markets(), fetch_clob_book(), fetch_market_by_id(), OrderBookSimulation, parse_market_dict(), simulate_clob_buy_and_exit_check() (+1 more)

### Community 4 - "AutoGovernor"
Cohesion: 0.07
Nodes (10): Ведомость, Исправления, Первопричина (Root Cause), Разбор 2026-11-10: троекратное дублирование уведомления об одобрении доработки #22 в Telegram, AutoGovernor, Global Constraints, Shadow Portfolio (Sandbox) Implementation Plan, WeatherOracle (+2 more)

### Community 6 - "🧠 Реестр авто-доработок и полуавтоматических решений (Auto-Governor)"
Cohesion: 0.33
Nodes (5): 🛠️ История применённых авто-фиксов и одобренных правок (19), 🟡 Ожидают твоего решения (Полуавтоматический режим: 0), ⚪ Отклонённые и утратившие актуальность предложения (4), 🧠 Реестр авто-доработок и полуавтоматических решений (Auto-Governor), ⚙️ Текущие активные параметры риск-менеджмента

### Community 7 - "📊 Отчёт симулятора Polymarket (Устав Grok Bot — Демо-счёт)"
Cohesion: 0.25
Nodes (7): Доходность по замороженным категориям (Песочница), 📂 Открытые позиции (1 / 8), Открытые позиции в песочнице (3 / 5), 📊 Отчёт симулятора Polymarket (Устав Grok Bot — Демо-счёт), 🔍 Последние проверенные кандидаты и фильтр стакана CLOB, 💰 Состояние виртуального портфеля, 🧪 Теневая песочница (Shadow Sandbox)

### Community 9 - "Polymarket Simulation and Agentic Market Architecture"
Cohesion: 0.40
Nodes (4): 1. Multi-Agent Role Decomposition, 2. Scraping and Resource Optimization (Obscura Integration), 3. Simulation Verification (Unlazy Integration), Polymarket Simulation and Agentic Market Architecture

### Community 10 - "telegram_notify.py"
Cohesion: 0.13
Nodes (7): check_and_send_daily_digest(), _load_env_fallback(), notify_position_closed(), _plural_deals(), send_telegram_alert(), load_token_from_env(), trigger_workflow()

### Community 11 - "http_tls.py"
Cohesion: 0.23
Nodes (3): fetch_polymarket_json(), fetch_standard_url(), resolve_secure_ip()

### Community 12 - "TestRiskManagementV2"
Cohesion: 0.11
Nodes (3): Матрица проверок риск-менеджмента (tests_risk.py), calibrate_probability(), TestRiskManagementV2

### Community 13 - ".monitor_and_manage_shadow_positions"
Cohesion: 0.18
Nodes (5): Ведомость, Исправления, Разбор 2026-11-10: сбой циклов из-за отсутствующего поля MIN_HOURS_TO_CLOSE_EXIT при появлении теневых позиций, Чем доказано, что ловится, TestShadowTrader

### Community 14 - "Acceptance Gates: Polymarket Simulation Daily Audit & Auto-Refinement"
Cohesion: 0.33
Nodes (5): Acceptance Gates: Polymarket Simulation Daily Audit & Auto-Refinement, Gate 1: Unit & Behavior Risk Tests, Gate 2: Full Test Suite, Gate 3: Auto-Governor & Status Inspection, Gate 4: Knowledge Graph Synchronization

### Community 15 - ".test_reports_cadence_stale_warning"
Cohesion: 0.38
Nodes (4): Ведомость, Исправления, Разбор 2026-11-07: подмена 10-минутного мониторинга уставного бота задержкой бесплатного GitHub Actions, Чем доказано, что ловится

### Community 16 - ".test_mature_consensus_oracle_strict_threshold"
Cohesion: 0.22
Nodes (3): Исправления, _mk(), _mk()

### Community 19 - "Разбор 2026-11-07: ложное утверждение об остановке симулятора из-за локального статуса"
Cohesion: 0.40
Nodes (4): Ведомость, Исправления, Разбор 2026-11-07: ложное утверждение об остановке симулятора из-за локального статуса, Чем доказано, что ловится

### Community 20 - "Разбор 2026-11-11: преждевременная отправка дневного дайджеста в 02:00 ночи сразу после смены даты по UTC"
Cohesion: 0.29
Nodes (4): Ведомость, Исправления, Первопричина (Root Cause), Разбор 2026-11-11: преждевременная отправка дневного дайджеста в 02:00 ночи сразу после смены даты по UTC

### Community 22 - "3. Реализация (How)"
Cohesion: 0.33
Nodes (5): 1. Зачем (Why), 2. Требования (Requirements), 3. Реализация (How), 4. Чеклист верификации, Спецификация: Risk Management & Budget Protection v2

### Community 24 - "Карта проверок проекта (Checks Map): Polymarket-Sim"
Cohesion: 0.40
Nodes (4): Карта проверок проекта (Checks Map): Polymarket-Sim, Когда направление обязательно, Лестница исправления AAR (Fix Ladder), Направления проверок

### Community 26 - "Разбор 2026-11-03: Стагнация капитала, фиктивная альфа оракула и паралич слотов"
Cohesion: 0.50
Nodes (3): Ведомость, Разбор 2026-11-03: Стагнация капитала, фиктивная альфа оракула и паралич слотов, Чем доказано, что ловится

## Knowledge Gaps
- **10 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `SimDatabase` connect `SimDatabase` to `GrokCharterPaperTrader`, `MarketInfo`, `polymarket_api.py`, `AutoGovernor`, `TestRiskManagementV2`, `.monitor_and_manage_shadow_positions`, `.test_mature_consensus_oracle_strict_threshold`, `test_e2e_shadow.py`, `.partition_markets`, `.test_shadow_take_profit_near_ceiling`, `.test_multi_category_filter_partitioning`?**
  _High betweenness centrality (0.207) - this node is a cross-community bridge._
- **Are the 11 inferred relationships involving `SimDatabase` (e.g. with `AutoGovernor` and `generate_reports()`) actually correct?**
  _`SimDatabase` has 11 INFERRED edges - model-reasoned connections that need verification._
- **Should `GrokCharterPaperTrader` be split into smaller, more focused modules?**
  _Cohesion score 0.14624505928853754 - nodes in this community are weakly interconnected._
- **Why does `TestRiskManagementV2` connect `TestRiskManagementV2` to `GrokCharterPaperTrader`, `SimDatabase`, `MarketInfo`, `polymarket_api.py`, `AutoGovernor`, `telegram_notify.py`, `.test_mature_consensus_oracle_strict_threshold`, `test_e2e_shadow.py`, `extract_event_key`, `Разбор 2026-11-11: преждевременная отправка дневного дайджеста в 02:00 ночи сразу после смены даты по UTC`, `.partition_markets`, `HighConvictionFactOracle`, `.test_shadow_take_profit_near_ceiling`, `.test_multi_category_filter_partitioning`?**
  _High betweenness centrality (0.139) - this node is a cross-community bridge._
- **Are the 17 inferred relationships involving `GrokCharterPaperTrader` (e.g. with `Исправления` and `Shadow Portfolio (Sandbox) Implementation Plan`) actually correct?**
  _`GrokCharterPaperTrader` has 17 INFERRED edges - model-reasoned connections that need verification._
- **Should `SimDatabase` be split into smaller, more focused modules?**
  _Cohesion score 0.058002735978112174 - nodes in this community are weakly interconnected._
- **Why does `GrokCharterPaperTrader` connect `GrokCharterPaperTrader` to `SimDatabase`, `MarketInfo`, `polymarket_api.py`, `AutoGovernor`, `CryptoOracle`, `TestRiskManagementV2`, `.monitor_and_manage_shadow_positions`, `.test_mature_consensus_oracle_strict_threshold`, `test_e2e_shadow.py`, `3. Реализация (How)`, `.partition_markets`, `HighConvictionFactOracle`, `.test_shadow_take_profit_near_ceiling`, `.test_multi_category_filter_partitioning`?**
  _High betweenness centrality (0.118) - this node is a cross-community bridge._