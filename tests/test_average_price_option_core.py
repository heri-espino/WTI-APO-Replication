"""Independent synthetic tests of the fixing-aware WTI-like baseline."""
import numpy as np
import pytest
from wti_apo_replication.average_price_option import (
    expected_average_level, wti_average_price_option_mc,
    wti_apo_cross_section_mc, posterior_wti_apo_prices,
)

def state():
    return dict(realized_fixings=np.array([99.,101.]),
                forward_fixings=np.array([100.,102.,101.]),
                fixing_times=np.array([2.,4.,7.])/252,
                rate=0.03, time_to_expiry=7./252,
                sigma=0.25, n_paths=4096, seed=2026)

def test_fully_realized_intrinsic_exact():
    est=wti_average_price_option_mc(
        realized_fixings=np.array([90.,100.,110.]),
        forward_fixings=np.array([]),fixing_times=np.array([]),
        strike=95.,sigma=0.3,rate=0.,time_to_expiry=0.,
        n_paths=64,seed=1)
    assert est.price == pytest.approx(5.0)
    assert est.standard_error == pytest.approx(0.0)

def test_expected_average_and_strike_ordering():
    s=state()
    assert expected_average_level(s["realized_fixings"],s["forward_fixings"]) == pytest.approx(100.6)
    est=wti_apo_cross_section_mc(strikes=np.array([98.,103.]),
                                option_types=["call","call"],**s)
    assert est.prices[0]>est.prices[1]
    assert np.all(np.isfinite(est.prices))

def test_call_put_matched_path_parity():
    s=state()
    call=wti_average_price_option_mc(strike=101.,option_type="call",**s)
    put=wti_average_price_option_mc(strike=101.,option_type="put",**s)
    assert abs(call.price-put.price) < 0.15

def test_common_seed_posterior_prices():
    s=state()
    s.pop("sigma")
    s.pop("n_paths")
    samples=np.array([0.15,0.3,0.45])
    prices=posterior_wti_apo_prices(samples,strike=101.,n_paths=2048,**s)
    assert prices.shape==(3,)
    assert np.all(np.isfinite(prices))
