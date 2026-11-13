from pathlib import Path

import pandas as pd


def write_parquet(df: pd.DataFrame, path: Path) -> None:
    """Writing the project's tables as parquet files, each with a CSV twin.

    Save `df` as a parquet file and, beside it, a utf-8 CSV of the same name, creating their folder first.
    """
    path.parent.mkdir(parents=True, exist_ok=True)
    df.to_parquet(path, index=False) # the row numbers are not saved, the tables join on named columns
    df.to_csv(path.with_suffix(".csv"), index=False, encoding="utf-8")
