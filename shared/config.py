import pandas as pd

WINDOW_START: pd.Timestamp = pd.Timestamp("2015-01-01")  # the project window
WINDOW_END: pd.Timestamp = pd.Timestamp("2021-12-31")

# the census's 13 age bands (DP05), each from its left edge up to below the next
AGE_EDGES: list[float] = [0, 5, 10, 15, 20, 25, 35, 45, 55, 60, 65, 75, 85, float("inf")]
AGE_BANDS: list[str] = ["under 5", "5-9", "10-14", "15-19", "20-24", "25-34", "35-44", "45-54", "55-59", "60-64", "65-74", "75-84", "85+"]

SEED: int = 42  # the project seed
