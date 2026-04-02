from api.utils import prepare_input


def test_prepare_input():
    payload = {
        "year": 2026,
        "month": 2,
        "quarter": 1,
        "month_sin": 0.5,
        "month_cos": 0.8,
        "lag_1": 100.0,
        "lag_3": 100.0,
        "lag_6": 100.0,
        "lag_12": 100.0,
        "rolling_mean_3": 100.0,
        "rolling_mean_6": 100.0,
        "rolling_std_3": 10.0,
        "total_over_4hrs": 50.0,
        "total_emergency_admissions": 40.0,
        "total_booked_attendances": 20.0,
        "total_dta_waits": 5.0,
    }
    df = prepare_input(payload)
    assert df.shape == (1, 16)
