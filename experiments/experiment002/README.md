# experiment002 — Synthetic PI–PM mechanism map (manual only)

**Purpose:** Preserve the author-controlled synthetic mechanism-map implementation used to investigate the response of posterior-integrated and plug-in Asian-option values to historical sample size, true volatility, moneyness, maturity, and fixing fraction.

**Scope:** The source in `run.py` is the actual Gaussian-sigma-quadrature mechanism-map algorithm transferred from the private research workspace, not a new reconstruction of its numerical findings. It uses **synthetic histories only**, no Barchart or Databento records. The full historical output/checkpoint directory and figures are not part of this public release candidate; **the published-scale numbers have not been reproduced in this public repo**.

**Inspect available CLI modes:**

```bash
python -m experiments.experiment002.run --help
```

**Small manual execution** (may create checkpoint and summary outputs; do not commit outputs until reviewed):

```bash
python -m experiments.experiment002.run --preset quick --backend numpy
```

The production-scale preset is computationally expensive and must be **manual only**. Never run it automatically on every push or PR. The original configuration, seeds and checkpoints must be audited before claiming exact reproduction of any 10-million-history reported result.

**Why:** PI – PM differences depend on the posterior variance of volatility and option-price curvature. This code implements a full factorial synthetic phase-map calculation with marginal sigma quadrature and Curran pricing.

**Validation:** Public CI only imports its CLI and runs fast core unit tests. It does not run even the quick numerical experiment automatically. Compare independent quadrature, vectorization, grid refinement and original checkpoint provenance before release.

**Next:** Run an approved small configuration manually and version its complete, rights-cleared output and verification manifest. For the full experiment, reproduce the exact original configuration and output, including cost/seed documentation, without exposing private system paths.
