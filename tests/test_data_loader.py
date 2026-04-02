import pandas as pd
from pathlib import Path
from src.data_loader import list_csv_files


def test_list_csv_files(tmp_path: Path):
    file1 = tmp_path / "a.csv"
    file1.write_text("x\n1\n")
    files = list_csv_files(str(tmp_path))
    assert len(files) == 1
    assert files[0].name == "a.csv"
