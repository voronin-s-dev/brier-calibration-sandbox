# Graph Report - Polymarket-Sim  (2026-11-10)

## Corpus Check
- 29 files · ~73,183 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 6 file(s) not represented in the graph (top: (none) 4, .db 1, .ini 1)

## Summary
- 361 nodes · 942 edges · 20 communities (15 shown, 5 thin omitted)
- Extraction: 77% EXTRACTED · 23% INFERRED · 0% AMBIGUOUS · INFERRED: 215 edges (avg confidence: 0.9)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `335693a3`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- GrokCharterPaperTrader
- SimDatabase
- oracles.py
- trader.py
- AutoGovernor
- Матрица проверок риск-менеджмента (tests_risk.py)
- 🧠 Реестр авто-доработок и полуавтоматических решений (Auto-Governor)
- 📊 Отчёт симулятора Polymarket (Устав Grok Bot — Демо-счёт)
- README.md
- Polymarket Simulation and Agentic Market Architecture
- .test_e2e_dual_track_execution
- Спецификация: Risk Management & Budget Protection v2
- polymarket_api.py
- TestShadowTrader
- .test_shadow_position_active_time_exit
- .test_reports_cadence_stale_warning
- Shadow Portfolio (Sandbox) Implementation Plan
- Разбор 2026-11-07: ложное утверждение об остановке симулятора из-за локального статуса

## God Nodes (most connected - your core abstractions)
1. `SimDatabase` - 65 edges
2. `GrokCharterPaperTrader` - 46 edges
3. `MarketInfo` - 35 edges
4. `AutoGovernor` - 30 edges
5. `TestRiskManagementV2` - 28 edges
6. `generate_reports()` - 22 edges
7. `main()` - 20 edges
8. `EvaluationResult` - 19 edges
9. `Task 1: Shadow Portfolio Database Schema & Access Layer` - 15 edges
10. `fetch_polymarket_json()` - 14 edges

## Surprising Connections (you probably didn't know these)
- `Global Constraints` --references--> `simulate_clob_sell_shares()`  [INFERRED]
  docs/superpowers/plans/2026-10-28-shadow-portfolio.md → polymarket_api.py
- `Лестница исправления AAR (Fix Ladder)` --references--> `AutoGovernor`  [INFERRED]
  .agents/aar/checks-map.md → auto_governor.py
- `Shadow Portfolio (Sandbox) Implementation Plan` --references--> `AutoGovernor`  [INFERRED]
  docs/superpowers/plans/2026-10-28-shadow-portfolio.md → auto_governor.py
- `3. Реализация (How)` --references--> `AutoGovernor`  [INFERRED]
  .specs/archive/2026-10-25_risk_management_v2.md → auto_governor.py
- `Task 2: Shadow Market Evaluation & Position Lifecycle in `trader.py`` --references--> `simulate_clob_sell_shares()`  [INFERRED]
  docs/superpowers/plans/2026-10-28-shadow-portfolio.md → polymarket_api.py

## Import Cycles
- None detected.

## Communities (20 total, 5 thin omitted)

### Community 0 - "GrokCharterPaperTrader"
Cohesion: 0.16
Nodes (3): Task 2: Shadow Market Evaluation & Position Lifecycle in `trader.py`, 3. Реализация (How), GrokCharterPaperTrader

### Community 1 - "SimDatabase"
Cohesion: 0.08
Nodes (11): generate_reports(), SimDatabase, Review Focus, Task 1: Shadow Portfolio Database Schema & Access Layer, Task 3: Auto-Governor Tier 2 Shadow Category Unfreeze Rule, Task 4: Reporting & Dashboard Integration, Task 5: End-to-End Simulation & Verification, print_console_summary() (+3 more)

### Community 2 - "oracles.py"
Cohesion: 0.07
Nodes (7): fetch_polymarket_json(), fetch_standard_url(), resolve_secure_ip(), CryptoOracle, NewsAndOrderbookOracle, norm_cdf(), WeatherOracle

### Community 3 - "trader.py"
Cohesion: 0.08
Nodes (9): git_sync_snapshot(), check_and_send_daily_digest(), _load_env_fallback(), notify_position_closed(), _plural_deals(), send_telegram_alert(), extract_event_key(), load_token_from_env() (+1 more)

### Community 4 - "AutoGovernor"
Cohesion: 0.14
Nodes (6): Карта проверок проекта (Checks Map): Polymarket-Sim, Когда направление обязательно, Лестница исправления AAR (Fix Ladder), Направления проверок, AutoGovernor, main()

### Community 5 - "Матрица проверок риск-менеджмента (tests_risk.py)"
Cohesion: 0.07
Nodes (14): Матрица проверок риск-менеджмента (tests_risk.py), Ведомость, Исправления, Разбор 2026-11-03: Стагнация капитала, фиктивная альфа оракула и паралич слотов, Чем доказано, что ловится, calibrate_probability(), EvaluationResult, HighConvictionFactOracle (+6 more)

### Community 6 - "🧠 Реестр авто-доработок и полуавтоматических решений (Auto-Governor)"
Cohesion: 0.33
Nodes (5): 🛠️ История применённых авто-фиксов и одобренных правок (19), 🟡 Ожидают твоего решения (Полуавтоматический режим: 0), ⚪ Отклонённые и утратившие актуальность предложения (3), 🧠 Реестр авто-доработок и полуавтоматических решений (Auto-Governor), ⚙️ Текущие активные параметры риск-менеджмента

### Community 7 - "📊 Отчёт симулятора Polymarket (Устав Grok Bot — Демо-счёт)"
Cohesion: 0.25
Nodes (7): Доходность по замороженным категориям (Песочница), 📂 Открытые позиции (1 / 8), Открытые позиции в песочнице (5 / 5), 📊 Отчёт симулятора Polymarket (Устав Grok Bot — Демо-счёт), 🔍 Последние проверенные кандидаты и фильтр стакана CLOB, 💰 Состояние виртуального портфеля, 🧪 Теневая песочница (Shadow Sandbox)

### Community 9 - "Polymarket Simulation and Agentic Market Architecture"
Cohesion: 0.40
Nodes (4): 1. Multi-Agent Role Decomposition, 2. Scraping and Resource Optimization (Obscura Integration), 3. Simulation Verification (Unlazy Integration), Polymarket Simulation and Agentic Market Architecture

### Community 10 - ".test_e2e_dual_track_execution"
Cohesion: 0.25
Nodes (4): make_market(), TestE2EShadowPortfolio, side_effect_buy(), side_effect_eval()

### Community 11 - "Спецификация: Risk Management & Budget Protection v2"
Cohesion: 0.40
Nodes (4): 1. Зачем (Why), 2. Требования (Requirements), 4. Чеклист верификации, Спецификация: Risk Management & Budget Protection v2

### Community 12 - "polymarket_api.py"
Cohesion: 0.14
Nodes (9): classify_market_category(), extract_resolution_source(), fetch_active_markets(), fetch_clob_book(), fetch_market_by_id(), OrderBookSimulation, parse_market_dict(), simulate_clob_buy_and_exit_check() (+1 more)

### Community 14 - ".test_shadow_position_active_time_exit"
Cohesion: 0.38
Nodes (4): Ведомость, Исправления, Разбор 2026-11-10: сбой циклов из-за отсутствующего поля MIN_HOURS_TO_CLOSE_EXIT при появлении теневых позиций, Чем доказано, что ловится

### Community 15 - ".test_reports_cadence_stale_warning"
Cohesion: 0.38
Nodes (4): Ведомость, Исправления, Разбор 2026-11-07: подмена 10-минутного мониторинга уставного бота задержкой бесплатного GitHub Actions, Чем доказано, что ловится

### Community 19 - "Разбор 2026-11-07: ложное утверждение об остановке симулятора из-за локального статуса"
Cohesion: 0.40
Nodes (4): Ведомость, Исправления, Разбор 2026-11-07: ложное утверждение об остановке симулятора из-за локального статуса, Чем доказано, что ловится

## Knowledge Gaps
- **5 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `SimDatabase` connect `SimDatabase` to `GrokCharterPaperTrader`, `trader.py`, `AutoGovernor`, `Матрица проверок риск-менеджмента (tests_risk.py)`, `.test_e2e_dual_track_execution`, `TestShadowTrader`?**
  _High betweenness centrality (0.231) - this node is a cross-community bridge._
- **Are the 11 inferred relationships involving `SimDatabase` (e.g. with `AutoGovernor` and `generate_reports()`) actually correct?**
  _`SimDatabase` has 11 INFERRED edges - model-reasoned connections that need verification._
- **Should `SimDatabase` be split into smaller, more focused modules?**
  _Cohesion score 0.07960199004975124 - nodes in this community are weakly interconnected._
- **Why does `GrokCharterPaperTrader` connect `GrokCharterPaperTrader` to `SimDatabase`, `oracles.py`, `trader.py`, `AutoGovernor`, `Матрица проверок риск-менеджмента (tests_risk.py)`, `.test_e2e_dual_track_execution`, `polymarket_api.py`, `TestShadowTrader`, `.test_shadow_position_active_time_exit`, `.test_dynamic_risk_cap_for_ceiling_contracts`, `.partition_markets`, `Shadow Portfolio (Sandbox) Implementation Plan`?**
  _High betweenness centrality (0.135) - this node is a cross-community bridge._
- **Are the 17 inferred relationships involving `GrokCharterPaperTrader` (e.g. with `Исправления` and `Shadow Portfolio (Sandbox) Implementation Plan`) actually correct?**
  _`GrokCharterPaperTrader` has 17 INFERRED edges - model-reasoned connections that need verification._
- **Should `oracles.py` be split into smaller, more focused modules?**
  _Cohesion score 0.07439024390243902 - nodes in this community are weakly interconnected._
- **Why does `AutoGovernor` connect `AutoGovernor` to `GrokCharterPaperTrader`, `SimDatabase`, `oracles.py`, `trader.py`, `Матрица проверок риск-менеджмента (tests_risk.py)`, `Shadow Portfolio (Sandbox) Implementation Plan`?**
  _High betweenness centrality (0.087) - this node is a cross-community bridge._