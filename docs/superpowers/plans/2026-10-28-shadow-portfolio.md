# Shadow Portfolio (Sandbox) Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build an isolated Shadow Portfolio (Sandbox) that simulates paper-trading on disabled categories (Crypto, Weather, Macro) with virtual capital ($50 USDC), CLOB execution, and full lifecycle monitoring, supplying empirical accuracy metrics to Auto-Governor for safe category unfreezing.

**Architecture:** Dedicated SQLite tables (`shadow_positions`, `shadow_portfolio_state`) in `data/polymarket_sim.db` physically isolate phantom trades from the active bankroll. `GrokCharterPaperTrader` branches market evaluation into active vs. shadow candidates, managing phantom entries/exits in the 10-minute cycle without altering real cash. `AutoGovernor` gains Tier 2 logic to propose category unfreezing when shadow performance stabilizes, while `dashboard_gen.py` renders a dedicated sandbox section in reports.

**Tech Stack:** Python 3.12, SQLite3 (`sqlite3`), Polymarket Gamma & CLOB APIs, `pytest`, `unittest`.

**Spec:** `C:\Users\voron\.gemini\antigravity\brain\fc98a803-ebd8-4703-a5dd-5a4d12f1c91a\shadow_portfolio_design.md`

## Global Constraints

- **Python Version:** 3.12 (`C:\Users\voron\AppData\Local\Programs\Python\Python312\python.exe`).
- **Database Safety:** Zero cross-contamination between `positions`/`portfolio_state` and `shadow_positions`/`shadow_portfolio_state`. Real balance and real PnL must never change due to shadow operations.
- **Telegram Alert Hygiene:** Shadow trades and shadow closures must NEVER trigger public Telegram alerts to avoid confusion.
- **CLOB Execution Fidelity:** Shadow trades must use honest CLOB book simulation (`simulate_clob_buy_shares`, `simulate_clob_sell_shares`), respecting slippage and liquidity rules.
- **ASD-STE100 Rules:** System comments and documentation must follow clear, concise, active voice standards.

## Review Focus

1. **Table Isolation Leak:** A query in `recalculate_portfolio()` or `get_open_positions()` accidentally includes shadow rows. (Prevented by physically separate tables `shadow_positions` and `shadow_portfolio_state`).
2. **Double Evaluation Overhead:** Scanning 50 shadow markets wastes API rate limits. (Constraint: limit shadow candidate evaluation to top 10 non-active markets per cycle).
3. **Shadow Bankruptcy:** Shadow bankroll drops below $1.00; shadow sizing must respect virtual cash and cap open positions to 5.
4. **Auto-Governor False Unfreeze:** A category with only 1 lucky winning trade triggers an unfreeze proposal. (Constraint: require >= 5 closed shadow trades, PnL >= +$1.50, and Win Rate >= 60%).
5. **Report Rendering on Empty Shadow DB:** `dashboard_gen.py` must render gracefully with 0 shadow trades without `ZeroDivisionError`.

---

### Task 1: Shadow Portfolio Database Schema & Access Layer

**Files:**
- Modify: `database.py:30-150`, `database.py:400-490`
- Test: `test_shadow_portfolio.py`

**Interfaces:**
- Consumes: `SimDatabase._connect()`
- Produces:
  - `SimDatabase.get_shadow_portfolio() -> Dict[str, Any]`
  - `SimDatabase.recalculate_shadow_portfolio() -> Dict[str, Any]`
  - `SimDatabase.get_open_shadow_positions() -> List[Dict[str, Any]]`
  - `SimDatabase.get_all_shadow_positions(limit: int = 100) -> List[Dict[str, Any]]`
  - `SimDatabase.open_shadow_position(...) -> int`
  - `SimDatabase.close_shadow_position(...) -> float`
  - `SimDatabase.get_shadow_category_stats() -> Dict[str, Dict[str, float]]`

- [ ] **Step 1: Write the failing unit tests for shadow database operations**

Create `test_shadow_portfolio.py` with tests verifying:
1. `test_shadow_schema_initialization`: `shadow_portfolio_state` starts with $50.0 cash and equity.
2. `test_real_and_shadow_isolation`: Opening a shadow position does not alter `cash_usdc` or `locked_usdc` in `portfolio_state`.
3. `test_shadow_position_lifecycle`: Opening and closing a shadow position properly updates `shadow_portfolio_state` cash, equity, and realized PnL.
4. `test_shadow_category_stats`: Closed shadow trades aggregate count, PnL, and wins per category correctly.

- [ ] **Step 2: Run test to verify it fails**

Run: `& "C:\Users\voron\AppData\Local\Programs\Python\Python312\python.exe" -m pytest test_shadow_portfolio.py -v`
Expected: FAIL (missing methods in `SimDatabase`)

- [ ] **Step 3: Implement shadow schema and methods in `database.py`**

1. In `SimDatabase._init_schema()`, add `CREATE TABLE IF NOT EXISTS shadow_portfolio_state` and `CREATE TABLE IF NOT EXISTS shadow_positions` as specified in the design doc.
2. Ensure row 1 of `shadow_portfolio_state` is inserted if not present (`initial_capital=50.0, cash_usdc=50.0, locked_usdc=0.0, total_equity=50.0`).
3. Implement `get_shadow_portfolio()`, `recalculate_shadow_portfolio()`, `get_open_shadow_positions()`, `get_all_shadow_positions()`, `open_shadow_position()`, `close_shadow_position()`, and `get_shadow_category_stats()`.

- [ ] **Step 4: Run test to verify it passes**

Run: `& "C:\Users\voron\AppData\Local\Programs\Python\Python312\python.exe" -m pytest test_shadow_portfolio.py -v`
Expected: PASS

- [ ] **Step 5: Run full existing test suite to ensure no regressions**

Run: `& "C:\Users\voron\AppData\Local\Programs\Python\Python312\python.exe" -m pytest tests_risk.py -v`
Expected: 11 passed

- [ ] **Step 6: Commit**

```bash
git add database.py test_shadow_portfolio.py
git commit -m "feat(database): add shadow portfolio and shadow positions schema and methods"
```

---

### Task 2: Shadow Market Evaluation & Position Lifecycle in `trader.py`

**Files:**
- Modify: `trader.py:345-440`, `trader.py:180-260`, `trader.py:580-645`
- Test: `test_shadow_trader.py`

**Interfaces:**
- Consumes:
  - `SimDatabase.get_shadow_portfolio()`
  - `SimDatabase.open_shadow_position()`
  - `SimDatabase.close_shadow_position()`
  - `polymarket_api.simulate_clob_buy_shares()`
  - `polymarket_api.simulate_clob_sell_shares()`
- Produces:
  - `GrokCharterPaperTrader.evaluate_and_execute_shadow_candidates(shadow_markets: List[MarketInfo], open_shadow_market_ids: Set[str]) -> int`
  - `GrokCharterPaperTrader.monitor_and_manage_shadow_positions() -> int`

- [ ] **Step 1: Write the failing unit tests for shadow trading lifecycle**

Create `test_shadow_trader.py`:
1. `test_shadow_candidate_partitioning`: Markets matching `active_category_filter` go to real candidate queue; non-matching markets go to shadow candidate queue (capped at 10).
2. `test_shadow_trade_execution`: Shadow candidate meeting Edge >= 8% and Slippage <= 2% opens a position in `shadow_positions` using shadow cash without modifying real portfolio.
3. `test_shadow_position_monitoring_and_exit`: An open shadow position is checked against CLOB bids, exiting on TP (+12%) or Stop-Loss (35%) or settlement.

- [ ] **Step 2: Run test to verify it fails**

Run: `& "C:\Users\voron\AppData\Local\Programs\Python\Python312\python.exe" -m pytest test_shadow_trader.py -v`
Expected: FAIL (missing shadow methods in `GrokCharterPaperTrader`)

- [ ] **Step 3: Implement shadow candidate handling and monitoring in `trader.py`**

1. In `run_cycle()`:
   - Partition scanned markets: `active_candidates` (where `category.upper() == cat_filter.upper()`) and `shadow_candidates` (where `category.upper() != cat_filter.upper()`).
   - If `cat_filter == "ALL"`, `shadow_candidates` is empty (all are active).
   - Cap `shadow_candidates` to top 10 by volume/priority to conserve API calls.
2. Implement `evaluate_and_execute_shadow_candidates()`:
   - Check open shadow position count (max 5).
   - Evaluate probability with existing oracles.
   - Sizing: half-Kelly on `shadow_portfolio["total_equity"]`, max 6% ($3 cap), min bet $1.00.
   - CLOB buy simulation on shadow cash.
   - Log to `trades.txt` with `[SHADOW EXEC]` prefix.
3. Implement `monitor_and_manage_shadow_positions()`:
   - Check resolution and CLOB sell bids for open shadow positions.
   - Close positions meeting TP (+12%), Stop-Loss (35%), probability shift, or expiration.
   - Log to `trades.txt` with `[SHADOW RESOLVED]` / `[SHADOW EXIT]` prefix.
   - DO NOT invoke `send_telegram_alert` for shadow events.

- [ ] **Step 4: Run test to verify it passes**

Run: `& "C:\Users\voron\AppData\Local\Programs\Python\Python312\python.exe" -m pytest test_shadow_trader.py -v`
Expected: PASS

- [ ] **Step 5: Run risk management test suite**

Run: `& "C:\Users\voron\AppData\Local\Programs\Python\Python312\python.exe" -m pytest tests_risk.py -v`
Expected: 11 passed

- [ ] **Step 6: Commit**

```bash
git add trader.py test_shadow_trader.py
git commit -m "feat(trader): implement dual-track shadow evaluation and position monitoring"
```

---

### Task 3: Auto-Governor Tier 2 Shadow Category Unfreeze Rule

**Files:**
- Modify: `auto_governor.py:390-460`, `auto_governor.py:550-630`
- Test: `test_shadow_governor.py`

**Interfaces:**
- Consumes:
  - `SimDatabase.get_shadow_category_stats()`
  - `SimDatabase.get_portfolio()`
- Produces:
  - Auto-Governor Tier 2 `tier2_shadow_category_unfreeze_<cat>_<batch>` event generation when shadow category satisfies criteria: `count >= 5`, `pnl >= +1.50`, `win_rate >= 0.60`.

- [ ] **Step 1: Write failing unit test for shadow unfreeze proposal**

Create `test_shadow_governor.py`:
1. `test_shadow_category_unfreeze_proposal`: When `active_category_filter != 'ALL'` and shadow `Crypto` has 5 closed trades with PnL = +$2.50, `AutoGovernor.evaluate_portfolio_and_rules()` triggers a `SEMI_AUTO` event proposing to unfreeze or rotate to `ALL`.
2. `test_unfreeze_requires_minimum_trades`: If shadow `Crypto` has only 2 trades (even if positive PnL), no unfreeze proposal is triggered.

- [ ] **Step 2: Run test to verify it fails**

Run: `& "C:\Users\voron\AppData\Local\Programs\Python\Python312\python.exe" -m pytest test_shadow_governor.py -v`
Expected: FAIL

- [ ] **Step 3: Implement shadow unfreeze rule in `auto_governor.py`**

1. In `AutoGovernor.evaluate_portfolio_and_rules()`, check if `active_cat != 'ALL'`:
   - Query `self.db.get_shadow_category_stats()`.
   - For any disabled category with `st["count"] >= 5`, `st["pnl"] >= 1.50`, and `win_rate >= 0.60`:
     - Construct rule key: `f"tier2_shadow_unfreeze_{c.lower()}_{int(st['count'])}"`
     - If not already recorded, create `SEMI_AUTO` governance event:
       - Title: `f"Разморозка категории {c}: стабильный плюс в песочнице"`
       - Action: `{"active_category_filter": "ALL"}` (or adding category to allowed pool)
       - Send Telegram decision alert.
2. In `generate_governance_report()`, include a summary table of shadow category performance.

- [ ] **Step 4: Run test to verify it passes**

Run: `& "C:\Users\voron\AppData\Local\Programs\Python\Python312\python.exe" -m pytest test_shadow_governor.py -v`
Expected: PASS

- [ ] **Step 5: Commit**

```bash
git add auto_governor.py test_shadow_governor.py
git commit -m "feat(governor): add Tier 2 shadow category recovery audit and unfreeze proposals"
```

---

### Task 4: Reporting & Dashboard Integration

**Files:**
- Modify: `dashboard_gen.py:20-120`, `dashboard_gen.py:180-290`
- Test: `test_shadow_reports.py`

**Interfaces:**
- Consumes:
  - `SimDatabase.get_shadow_portfolio()`
  - `SimDatabase.get_all_shadow_positions()`
  - `SimDatabase.get_shadow_category_stats()`
- Produces:
  - Updated `STATUS_REPORT.md` containing `## 🧪 Теневая песочница (Shadow Sandbox)`
  - Updated `dashboard.html` containing a dedicated visual card for the Shadow Portfolio.

- [ ] **Step 1: Write failing unit test for shadow reporting**

Create `test_shadow_reports.py`:
1. `test_reports_include_shadow_section`: Call `generate_reports(db, html_path, md_path)` and assert that `STATUS_REPORT.md` and `dashboard.html` contain the Shadow Sandbox header, shadow equity, and shadow PnL breakdown.
2. `test_reports_zero_division_guard`: Verify report generation succeeds without errors when 0 shadow positions exist.

- [ ] **Step 2: Run test to verify it fails**

Run: `& "C:\Users\voron\AppData\Local\Programs\Python\Python312\python.exe" -m pytest test_shadow_reports.py -v`
Expected: FAIL

- [ ] **Step 3: Implement shadow reporting in `dashboard_gen.py`**

1. In `generate_reports()`, query `db.get_shadow_portfolio()`, `db.get_all_shadow_positions(limit=50)`, and `db.get_shadow_category_stats()`.
2. Format a dedicated Markdown section in `STATUS_REPORT.md`:
   - Shadow Virtual Equity, Cash, Locked, Current Drawdown.
   - Category performance table for shadow trades (Crypto, Weather, etc.).
3. Add a corresponding visual grid card in `dashboard.html` with clean CSS styling matching the existing dashboard aesthetic.

- [ ] **Step 4: Run test to verify it passes**

Run: `& "C:\Users\voron\AppData\Local\Programs\Python\Python312\python.exe" -m pytest test_shadow_reports.py -v`
Expected: PASS

- [ ] **Step 5: Commit**

```bash
git add dashboard_gen.py test_shadow_reports.py
git commit -m "feat(dashboard): render dedicated Shadow Sandbox section in status report and HTML dashboard"
```

---

### Task 5: End-to-End Simulation & Verification

**Files:**
- Test: `test_e2e_shadow.py`
- Modify: `run_sim.py` (ensure `--status` and regular cycle display shadow stats)

- [ ] **Step 1: Write end-to-end integration test**

Create `test_e2e_shadow.py`:
1. Initialize test database with `active_category_filter = 'Sports'`.
2. Run a mocked cycle with both a Sports market and a Crypto market available.
3. Assert real position is created in `positions` and shadow position is created in `shadow_positions`.
4. Assert real cash reflects only the Sports trade; shadow cash reflects only the Crypto trade.
5. Generate reports and verify both files exist and are populated.

- [ ] **Step 2: Run all test suites across the repository**

Run: `& "C:\Users\voron\AppData\Local\Programs\Python\Python312\python.exe" -m pytest test_shadow_portfolio.py test_shadow_trader.py test_shadow_governor.py test_shadow_reports.py test_e2e_shadow.py tests_risk.py -v`
Expected: ALL PASS

- [ ] **Step 3: Run code graph update**

Run: `graphify update .`

- [ ] **Step 4: Commit**

```bash
git add test_e2e_shadow.py run_sim.py
git commit -m "chore(test): add e2e integration test for shadow portfolio and update code graph"
```
