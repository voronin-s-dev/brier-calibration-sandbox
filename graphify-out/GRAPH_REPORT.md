# Graph Report - Polymarket-Sim  (2026-11-09)

## Corpus Check
- 30 files · ~64,490 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 5 file(s) not represented in the graph (top: (none) 4, .db 1)

## Summary
- 345 nodes · 873 edges · 21 communities (17 shown, 4 thin omitted)
- Extraction: 78% EXTRACTED · 22% INFERRED · 0% AMBIGUOUS · INFERRED: 190 edges (avg confidence: 0.9)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `479b1427`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- GrokCharterPaperTrader
- SimDatabase
- WeatherOracle
- trader.py
- AutoGovernor
- TestRiskManagementV2
- 🧠 Реестр авто-доработок и полуавтоматических решений (Auto-Governor)
- 📊 Отчёт симулятора Polymarket (Устав Grok Bot — Демо-счёт)
- README.md
- Polymarket Simulation and Agentic Market Architecture
- .test_shadow_candidate_funnel_not_starved
- MarketInfo
- Daily Focus: 2026-11-09
- .test_e2e_dual_track_execution
- progress.md
- .test_reports_cadence_stale_warning
- CryptoOracle
- NewsAndOrderbookOracle
- Карта проверок проекта (Checks Map): Polymarket-Sim
- Разбор 2026-11-07: ложное утверждение об остановке симулятора из-за локального статуса
- Спецификация: Risk Management & Budget Protection v2

## God Nodes (most connected - your core abstractions)
1. `SimDatabase` - 61 edges
2. `GrokCharterPaperTrader` - 40 edges
3. `AutoGovernor` - 30 edges
4. `MarketInfo` - 30 edges
5. `generate_reports()` - 22 edges
6. `TestRiskManagementV2` - 22 edges
7. `main()` - 18 edges
8. `EvaluationResult` - 17 edges
9. `Task 1: Shadow Portfolio Database Schema & Access Layer` - 15 edges
10. `fetch_polymarket_json()` - 13 edges

## Surprising Connections (you probably didn't know these)
- `Лестница исправления AAR (Fix Ladder)` --references--> `AutoGovernor`  [INFERRED]
  .agents/aar/checks-map.md → auto_governor.py
- `Shadow Portfolio (Sandbox) Implementation Plan` --references--> `AutoGovernor`  [INFERRED]
  docs/superpowers/plans/2026-10-28-shadow-portfolio.md → auto_governor.py
- `3. Реализация (How)` --references--> `AutoGovernor`  [INFERRED]
  .specs/archive/2026-10-25_risk_management_v2.md → auto_governor.py
- `Global Constraints` --references--> `simulate_clob_sell_shares()`  [INFERRED]
  docs/superpowers/plans/2026-10-28-shadow-portfolio.md → polymarket_api.py
- `Task 2: Shadow Market Evaluation & Position Lifecycle in `trader.py`` --references--> `send_telegram_alert()`  [INFERRED]
  docs/superpowers/plans/2026-10-28-shadow-portfolio.md → telegram_notify.py

## Import Cycles
- None detected.

## Communities (21 total, 4 thin omitted)

### Community 0 - "GrokCharterPaperTrader"
Cohesion: 0.07
Nodes (9): Global Constraints, Shadow Portfolio (Sandbox) Implementation Plan, Task 2: Shadow Market Evaluation & Position Lifecycle in `trader.py`, fetch_clob_book(), simulate_clob_buy_and_exit_check(), simulate_clob_sell_shares(), make_market_info(), TestShadowTrader (+1 more)

### Community 1 - "SimDatabase"
Cohesion: 0.08
Nodes (11): generate_reports(), SimDatabase, Review Focus, Task 1: Shadow Portfolio Database Schema & Access Layer, Task 3: Auto-Governor Tier 2 Shadow Category Unfreeze Rule, Task 4: Reporting & Dashboard Integration, Task 5: End-to-End Simulation & Verification, print_console_summary() (+3 more)

### Community 2 - "WeatherOracle"
Cohesion: 0.19
Nodes (4): calibrate_probability(), EvaluationResult, norm_cdf(), WeatherOracle

### Community 3 - "trader.py"
Cohesion: 0.07
Nodes (12): fetch_polymarket_json(), fetch_standard_url(), classify_market_category(), extract_resolution_source(), fetch_active_markets(), OrderBookSimulation, parse_market_dict(), check_and_send_daily_digest() (+4 more)

### Community 4 - "AutoGovernor"
Cohesion: 0.11
Nodes (5): AutoGovernor, git_sync_snapshot(), main(), load_token_from_env(), trigger_workflow()

### Community 5 - "TestRiskManagementV2"
Cohesion: 0.18
Nodes (4): Матрица проверок риск-менеджмента (tests_risk.py), 3. Реализация (How), TestRiskManagementV2, extract_event_key()

### Community 6 - "🧠 Реестр авто-доработок и полуавтоматических решений (Auto-Governor)"
Cohesion: 0.33
Nodes (5): 🛠️ История применённых авто-фиксов и одобренных правок (18), 🟡 Ожидают твоего решения (Полуавтоматический режим: 0), ⚪ Отклонённые и утратившие актуальность предложения (2), 🧠 Реестр авто-доработок и полуавтоматических решений (Auto-Governor), ⚙️ Текущие активные параметры риск-менеджмента

### Community 7 - "📊 Отчёт симулятора Polymarket (Устав Grok Bot — Демо-счёт)"
Cohesion: 0.29
Nodes (6): Доходность по замороженным категориям (Песочница), 📂 Открытые позиции (0 / 8), 📊 Отчёт симулятора Polymarket (Устав Grok Bot — Демо-счёт), 🔍 Последние проверенные кандидаты и фильтр стакана CLOB, 💰 Состояние виртуального портфеля, 🧪 Теневая песочница (Shadow Sandbox)

### Community 9 - "Polymarket Simulation and Agentic Market Architecture"
Cohesion: 0.40
Nodes (4): 1. Multi-Agent Role Decomposition, 2. Scraping and Resource Optimization (Obscura Integration), 3. Simulation Verification (Unlazy Integration), Polymarket Simulation and Agentic Market Architecture

### Community 10 - ".test_shadow_candidate_funnel_not_starved"
Cohesion: 0.20
Nodes (5): Ведомость, Исправления, Разбор 2026-11-03: Стагнация капитала, фиктивная альфа оракула и паралич слотов, Чем доказано, что ловится, _mk()

### Community 11 - "MarketInfo"
Cohesion: 0.31
Nodes (4): HighConvictionFactOracle, fetch_market_by_id(), MarketInfo, _mk()

### Community 12 - "Daily Focus: 2026-11-09"
Cohesion: 0.25
Nodes (7): 1. [Harmonious-Thinker-Media] **Task 4.2:** Подготовить концепт персонального бота-ассистента для надиктовки постов Сергеем с авто-форматированием под V5., 2. [creator-core-engine & Harmonious-Thinker-Media] Тестирование генерации контента и саунд-дизайна (Earshot / FFmpeg), 3. [Инфраструктура и аудит] Проверка резервных копий и статуса скилов Antigravity, Daily Focus: 2026-11-09, Top-3 Приоритета на сегодня, Грабли и напоминания (Safeguards), Сводка активности по проектам

### Community 13 - ".test_e2e_dual_track_execution"
Cohesion: 0.25
Nodes (4): make_market(), TestE2EShadowPortfolio, side_effect_buy(), side_effect_eval()

### Community 15 - ".test_reports_cadence_stale_warning"
Cohesion: 0.38
Nodes (4): Ведомость, Исправления, Разбор 2026-11-07: подмена 10-минутного мониторинга уставного бота задержкой бесплатного GitHub Actions, Чем доказано, что ловится

### Community 18 - "Карта проверок проекта (Checks Map): Polymarket-Sim"
Cohesion: 0.40
Nodes (4): Карта проверок проекта (Checks Map): Polymarket-Sim, Когда направление обязательно, Лестница исправления AAR (Fix Ladder), Направления проверок

### Community 19 - "Разбор 2026-11-07: ложное утверждение об остановке симулятора из-за локального статуса"
Cohesion: 0.40
Nodes (4): Ведомость, Исправления, Разбор 2026-11-07: ложное утверждение об остановке симулятора из-за локального статуса, Чем доказано, что ловится

### Community 20 - "Спецификация: Risk Management & Budget Protection v2"
Cohesion: 0.40
Nodes (4): 1. Зачем (Why), 2. Требования (Requirements), 4. Чеклист верификации, Спецификация: Risk Management & Budget Protection v2

## Knowledge Gaps
- **4 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `SimDatabase` connect `SimDatabase` to `GrokCharterPaperTrader`, `trader.py`, `AutoGovernor`, `TestRiskManagementV2`, `.test_shadow_candidate_funnel_not_starved`, `.test_e2e_dual_track_execution`?**
  _High betweenness centrality (0.225) - this node is a cross-community bridge._
- **Are the 11 inferred relationships involving `SimDatabase` (e.g. with `AutoGovernor` and `generate_reports()`) actually correct?**
  _`SimDatabase` has 11 INFERRED edges - model-reasoned connections that need verification._
- **Should `GrokCharterPaperTrader` be split into smaller, more focused modules?**
  _Cohesion score 0.06775510204081632 - nodes in this community are weakly interconnected._
- **Why does `GrokCharterPaperTrader` connect `GrokCharterPaperTrader` to `SimDatabase`, `WeatherOracle`, `trader.py`, `AutoGovernor`, `TestRiskManagementV2`, `.test_shadow_candidate_funnel_not_starved`, `MarketInfo`, `.test_e2e_dual_track_execution`, `CryptoOracle`, `NewsAndOrderbookOracle`?**
  _High betweenness centrality (0.117) - this node is a cross-community bridge._
- **Are the 16 inferred relationships involving `GrokCharterPaperTrader` (e.g. with `Shadow Portfolio (Sandbox) Implementation Plan` and `Task 2: Shadow Market Evaluation & Position Lifecycle in `trader.py``) actually correct?**
  _`GrokCharterPaperTrader` has 16 INFERRED edges - model-reasoned connections that need verification._
- **Should `SimDatabase` be split into smaller, more focused modules?**
  _Cohesion score 0.07757885763000852 - nodes in this community are weakly interconnected._
- **Why does `AutoGovernor` connect `AutoGovernor` to `GrokCharterPaperTrader`, `SimDatabase`, `WeatherOracle`, `trader.py`, `TestRiskManagementV2`, `MarketInfo`, `Карта проверок проекта (Checks Map): Polymarket-Sim`?**
  _High betweenness centrality (0.093) - this node is a cross-community bridge._