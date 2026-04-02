import pandas as pd
from src.project_utils import clean_column_name, clean_columns


def test_clean_column_name():
    assert clean_column_name("A&E Attendances Type 1") == "aande_attendances_type_1"


def test_clean_columns():
    df = pd.DataFrame(columns=["A&E Attendances Type 1", "Other Emergency Admissions"])
    cleaned = clean_columns(df)
    assert "aande_attendances_type_1" in cleaned.columns
    assert "other_emergency_admissions" in cleaned.columns
