# Acceptance Gates: Polymarket Simulation Daily Audit & Auto-Refinement

## Gate 1: Unit & Behavior Risk Tests
- Command: `pytest tests_risk.py`
- Expected: Exit code 0, all tests pass (including new deduplication, OBI damping, esports guard, and sweet-spot TP tests).

## Gate 2: Full Test Suite
- Command: `pytest`
- Expected: Exit code 0, all test suites pass.

## Gate 3: Auto-Governor & Status Inspection
- Command: `py run_sim.py --status`
- Expected: Exit code 0, portfolio status and reports update properly.

## Gate 4: Knowledge Graph Synchronization
- Command: `graphify update .`
- Expected: Exit code 0, graphify knowledge graph updated without error.
