# Licensed market-data input contracts

The public package contains **parsers and tests**, not commercial observations. The input files used by the private empirical study were obtained under third-party commercial licenses and cannot be redistributed through this repository.

## Barchart WTI Average Price Option histories

The public `bayesian_asian_options.barchart_apo` module parses contract filenames and daily option-price histories. A locally licensed export should provide, where available, daily `Time`, `Open`, `High`, `Low`, `Latest`, `Change`, `%Change`, `Volume`, and `Open Int` fields. The test suite creates tiny, hypothetical CSV files in a temporary directory; no third-party rows are committed.

The `Latest` field should be regarded as a **vendor end-of-day price proxy**, not as independently verified exchange settlement or executed transaction price. Expiry and symbol parsing rules are implemented in the module and checked with synthetic test filenames.

## Databento WTI futures-option snapshots

`bayesian_asian_options.databento_wti` normalizes definitions and selects candidate final settlement statistics from locally licensed input tables. Synthetic tests cover instrument IDs, timestamps, `stat_type`, `stat_flags`, `price`, and final-versus-intraday distinctions. It does **not** download market data or claim that every candidate statistic corresponds to an independently verified exchange settlement.

The actual vendor subscription, query, licensed dataset, schema version, timezone, retrieval timestamps and corrections must be documented by a data licensee. Credentials must remain outside version control.

## Reproduction limitations

- **No redistribution:** Do not submit raw market rows, extracts, row-level derived files, API tokens, subscription exports or paid vendor metadata as public pull requests.
- **Cutoff integrity:** Distinguish information available at the valuation date from prices or vendor updates published afterwards. An earlier date in a vendor record is not proof of its first publication time.
- **Pricing inputs:** Preserve actual first-nearby futures roll logic, known fixings, expiry conventions and discount factors in separately approved analysis scripts.
- **Rights:** Provider license terms may restrict even derived market aggregates; review each potential public result individually.
- **Validation:** The current adapter tests use only synthetic fixtures. They do not establish that every real vendor file and every manuscript empirical calculation has been independently reproduced.

For a full future reproduction, a researcher should obtain authorized Barchart and/or Databento access separately and execute a verified, publication-specific pipeline. That pipeline has not yet been released here.
