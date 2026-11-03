# Public scientific methods and boundary

This release candidate includes an **author-controlled, reviewed code-only** subset from the private research workspace. Its original Git history and all licensed market data remain private.

| Module | Content | Limit |
|---|---|---|
| `gbm_inference.py` | Physical-measure GBM likelihood and random-walk Metropolis posterior in drift/log-volatility | Requires user-supplied return history |
| `sigma_quadrature.py` | Marginalize Gaussian drift and integrate volatility-posterior density over a grid | Grid approximation; not a closed-form arithmetic Asian value |
| `asian_pricing.py` | Risk-neutral arithmetic Asian option Monte Carlo, geometric control variate | Lognormal constant-volatility approximation |
| `average_price_option.py` | Partially fixed arithmetic average, supplied futures curve and shared one-factor Brownian risk | Requires authorized fixing/curve inputs and assumes perfect instantaneous factor correlation |
| `synthetic.py` | Independent spot-GBM instructional baseline | Not paper replication |

The physical measure `P` is for the statistical model of historical returns, while risk-neutral `Q` is used for option valuation. Physical drift is not fed into the risk-neutral futures model.

The public experiment compares

```
PI = E[C(sigma) | D]
PM = C(E[sigma | D])
Delta = PI - PM
```

using entirely synthetic returns and fixing curves. Its tests check invariants, not vendor settlement marks or the unpublished empirical claims. In particular, the private manuscript's ten-million-history experiments, 2,381 contract-date observations, implied-volatility timing and date-level price errors are **not** independently reproduced here.

See [data_contract.md](data_contract.md) and [release_manifest.md](release_manifest.md).
