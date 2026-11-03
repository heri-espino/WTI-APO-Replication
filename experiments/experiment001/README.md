# experiment001 — Synthetic posterior-integration check

**Purpose:** Demonstrate the numerical difference between posterior integration (PI) and posterior-mean plug-in pricing (PM) using only simulated Gaussian GBM returns and independently specified hypothetical futures levels. This is **not a reproduction of the paper's empirical results**.

**Method:** 63 simulated returns, root seed 2026, Gaussian physical-measure GBM posterior marginalized over drift, trapezoid sigma grid of 301 nodes, one-factor Curran arithmetic futures-option approximation with three already realized synthetic fixings and six remaining hypothetical futures levels.

**Run** from a clean installation:

```bash
python -m pip install -e ".[dev]"
python -m experiments.experiment001.run --seed 2026 --grid-points 301
python -m experiments.experiment001.run --output results/synthetic/experiment001.json
python -m pytest -q tests/test_experiment001.py
```

**Validation:** Fixed-seed exact reproducibility, normalized posterior weights, finite/nonnegative option prices, nonnegative variance and PI–PM accounting identity. The command optionally saves a JSON output under the allowed synthetic results directory; the public CI runs fast smoke checks.

**Findings:** Values and tolerances must be recorded only after executing the committed source. Do not substitute an unverified hand-written result, infer market implications, or claim 10-million-history reproduction.

**Next:** Compare sigma-grid refinement, add independent Monte Carlo checks of Curran's approximation, then verify the full manuscript configurations and sample-dependent outputs with separately licensed data. Publish only approved aggregate outputs.
