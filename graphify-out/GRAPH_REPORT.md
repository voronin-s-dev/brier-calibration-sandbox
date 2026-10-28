# Graph Report - Polymarket-Sim  (2026-10-28)

## Corpus Check
- 25 files · ~46,920 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 6 file(s) not represented in the graph (top: (none) 5, .db 1)

## Summary
- 300 nodes · 801 edges · 12 communities (9 shown, 3 thin omitted)
- Extraction: 79% EXTRACTED · 21% INFERRED · 0% AMBIGUOUS · INFERRED: 170 edges (avg confidence: 0.9)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `d1bc725d`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- GrokCharterPaperTrader
- SimDatabase
- CryptoOracle
- trader.py
- AutoGovernor
- .compute_kelly_sizing
- 🧠 Реестр авто-доработок и полуавтоматических решений (Auto-Governor)
- 📊 Отчёт симулятора Polymarket (Устав Grok Bot — Демо-счёт)
- README.md
- http_tls.py
- .test_e2e_dual_track_execution
- progress.md

## God Nodes (most connected - your core abstractions)
1. `SimDatabase` - 60 edges
2. `GrokCharterPaperTrader` - 39 edges
3. `AutoGovernor` - 30 edges
4. `MarketInfo` - 28 edges
5. `generate_reports()` - 21 edges
6. `main()` - 18 edges
7. `TestRiskManagementV2` - 18 edges
8. `EvaluationResult` - 17 edges
9. `Task 1: Shadow Portfolio Database Schema & Access Layer` - 15 edges
10. `fetch_polymarket_json()` - 13 edges

## Surprising Connections (you probably didn't know these)
- `Лестница исправления AAR (Fix Ladder)` --references--> `AutoGovernor`  [INFERRED]
  .agents/aar/checks-map.md → auto_governor.py
- `Global Constraints` --references--> `simulate_clob_sell_shares()`  [INFERRED]
  docs/superpowers/plans/2026-10-28-shadow-portfolio.md → polymarket_api.py
- `3. Реализация (How)` --references--> `AutoGovernor`  [INFERRED]
  .specs/archive/2026-10-25_risk_management_v2.md → auto_governor.py
- `Task 2: Shadow Market Evaluation & Position Lifecycle in `trader.py`` --references--> `send_telegram_alert()`  [INFERRED]
  docs/superpowers/plans/2026-10-28-shadow-portfolio.md → telegram_notify.py
- `3. Реализация (How)` --references--> `extract_event_key()`  [INFERRED]
  .specs/archive/2026-10-25_risk_management_v2.md → trader.py

## Import Cycles
- None detected.

## Communities (12 total, 3 thin omitted)

### Community 0 - "GrokCharterPaperTrader"
Cohesion: 0.07
Nodes (13): Task 2: Shadow Market Evaluation & Position Lifecycle in `trader.py`, calibrate_probability(), EvaluationResult, HighConvictionFactOracle, NewsAndOrderbookOracle, norm_cdf(), WeatherOracle, fetch_market_by_id() (+5 more)

### Community 1 - "SimDatabase"
Cohesion: 0.08
Nodes (11): generate_reports(), SimDatabase, Review Focus, Task 1: Shadow Portfolio Database Schema & Access Layer, Task 3: Auto-Governor Tier 2 Shadow Category Unfreeze Rule, Task 4: Reporting & Dashboard Integration, Task 5: End-to-End Simulation & Verification, print_console_summary() (+3 more)

### Community 3 - "trader.py"
Cohesion: 0.09
Nodes (8): classify_market_category(), extract_resolution_source(), fetch_active_markets(), fetch_clob_book(), OrderBookSimulation, parse_market_dict(), simulate_clob_buy_and_exit_check(), extract_event_key()

### Community 4 - "AutoGovernor"
Cohesion: 0.14
Nodes (5): AutoGovernor, Global Constraints, Shadow Portfolio (Sandbox) Implementation Plan, git_sync_snapshot(), main()

### Community 5 - ".compute_kelly_sizing"
Cohesion: 0.10
Nodes (9): Карта проверок проекта (Checks Map): Polymarket-Sim, Лестница исправления AAR (Fix Ladder), Матрица проверок риск-менеджмента (tests_risk.py), 1. Зачем (Why), 2. Требования (Requirements), 3. Реализация (How), 4. Чеклист верификации, Спецификация: Risk Management & Budget Protection v2 (+1 more)

### Community 6 - "🧠 Реестр авто-доработок и полуавтоматических решений (Auto-Governor)"
Cohesion: 0.33
Nodes (5): 🛠️ История применённых авто-фиксов и одобренных правок (18), 🟡 Ожидают твоего решения (Полуавтоматический режим: 1), Предложение #19: Калибровка Brier Score (0.227): снизить вес оракула до 0.53 (`TIER_2_CALIBRATION`), 🧠 Реестр авто-доработок и полуавтоматических решений (Auto-Governor), ⚙️ Текущие активные параметры риск-менеджмента

### Community 7 - "📊 Отчёт симулятора Polymarket (Устав Grok Bot — Демо-счёт)"
Cohesion: 0.29
Nodes (6): Доходность по замороженным категориям (Песочница), 📂 Открытые позиции (4 / 8), 📊 Отчёт симулятора Polymarket (Устав Grok Bot — Демо-счёт), 🔍 Последние проверенные кандидаты и фильтр стакана CLOB, 💰 Состояние виртуального портфеля, 🧪 Теневая песочница (Shadow Sandbox)

### Community 9 - "http_tls.py"
Cohesion: 0.11
Nodes (9): fetch_polymarket_json(), fetch_standard_url(), check_and_send_daily_digest(), _load_env_fallback(), notify_position_closed(), _plural_deals(), send_telegram_alert(), load_token_from_env() (+1 more)

### Community 12 - ".test_e2e_dual_track_execution"
Cohesion: 0.22
Nodes (4): make_market(), TestE2EShadowPortfolio, side_effect_buy(), side_effect_eval()

## Knowledge Gaps
- **3 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `SimDatabase` connect `SimDatabase` to `GrokCharterPaperTrader`, `trader.py`, `AutoGovernor`, `.compute_kelly_sizing`, `.test_e2e_dual_track_execution`?**
  _High betweenness centrality (0.246) - this node is a cross-community bridge._
- **Are the 11 inferred relationships involving `SimDatabase` (e.g. with `AutoGovernor` and `generate_reports()`) actually correct?**
  _`SimDatabase` has 11 INFERRED edges - model-reasoned connections that need verification._
- **Should `GrokCharterPaperTrader` be split into smaller, more focused modules?**
  _Cohesion score 0.06666666666666667 - nodes in this community are weakly interconnected._
- **Why does `GrokCharterPaperTrader` connect `GrokCharterPaperTrader` to `SimDatabase`, `CryptoOracle`, `trader.py`, `AutoGovernor`, `.compute_kelly_sizing`, `.test_e2e_dual_track_execution`?**
  _High betweenness centrality (0.130) - this node is a cross-community bridge._
- **Are the 16 inferred relationships involving `GrokCharterPaperTrader` (e.g. with `Shadow Portfolio (Sandbox) Implementation Plan` and `Task 2: Shadow Market Evaluation & Position Lifecycle in `trader.py``) actually correct?**
  _`GrokCharterPaperTrader` has 16 INFERRED edges - model-reasoned connections that need verification._
- **Should `SimDatabase` be split into smaller, more focused modules?**
  _Cohesion score 0.0761904761904762 - nodes in this community are weakly interconnected._
- **Why does `AutoGovernor` connect `AutoGovernor` to `GrokCharterPaperTrader`, `SimDatabase`, `trader.py`, `.compute_kelly_sizing`?**
  _High betweenness centrality (0.110) - this node is a cross-community bridge._