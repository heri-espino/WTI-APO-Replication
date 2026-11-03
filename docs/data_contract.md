# Input contract for separately licensed market-data reproduction

**No market observations are included here.** To evaluate the methods against real WTI APO marks, readers must obtain authorized data independently and construct:

- `realized_fixings`: already known first-nearby CL settlements by valuation date
- `forward_fixings`: valuation-date futures levels corresponding to remaining fixing dates and a documented contract-roll schedule
- `fixing_times`: remaining dates in year fractions, ordered consistently with forwards
- `strike`, `option_type`, discount rate/factor, and annualized volatility estimated from information available by the declared cutoff
- For historical GBM inference, a specified return history and sampling interval; remove returns spanning a contract roll where necessary

Validation requires recording vendor product and query vintage, source-field interpretation, eligible contracts/dates, missingness, provenance hashes, time cutoff, model configuration, seeds, units, outputs, and a rights review for any derived publication figure or table.

This is a numerical **interface contract**, not evidence that the historical pipeline or vendor timestamps were validated for release.
