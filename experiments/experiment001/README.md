# experiment001 — Posterior integration versus posterior-mean plug-in

This **synthetic-only** demonstration uses publicly released Gaussian GBM posterior inference, one-dimensional volatility quadrature and a one-factor, partially fixed average-price option pricer. It does **not** reproduce the manuscript's ten-million-history simulation or empirical results.

Scientific question: How different are `PI = E[C(sigma)|D]` and `PM = C(E[sigma|D])` under the same return model and synthetic fixing curve?

After installing the editable project, run:

```bash
python -m experiments.experiment001.run --seed 2026 --pricing-paths 1024
python -m experiments.experiment001.run --seed 2026 --pricing-paths 1024 --output results/experiment001/summary.json
```

The second command preserves the output locally. Commit it **after review**, with the exact source commit and environment. To test numerical stability, compare denser volatility grids and larger path counts; do not interpret the sign as universal. Scientific claims about markets require licensed original observations and independently verified timing/measurement choices. **Next:** record a reviewer-approved numerical output and check quadrature/Monte Carlo convergence.
