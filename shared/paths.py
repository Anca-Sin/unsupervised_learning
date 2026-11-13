from pathlib import Path

PROJECT_ROOT: Path = Path(__file__).resolve().parents[1]  # the folder holding shared/ and notebooks/

DATA_DIR: Path = PROJECT_ROOT / "data"
RAW_DIR: Path = DATA_DIR / "0_raw"
MPV_RAW_DIR: Path = RAW_DIR / "1_1_mpv"
TIGER_RAW_DIR: Path = RAW_DIR / "1_2_tiger"
ACS_RAW_DIR: Path = RAW_DIR / "1_3_acs"

DATA_NOTEBOOKS_DIR: Path = DATA_DIR / "1_data_notebooks"
MPV_DIR: Path = DATA_NOTEBOOKS_DIR / "1_1_mpv"
MPV_HANDMADE_DIR: Path = MPV_DIR / "handmade"
TIGER_DIR: Path = DATA_NOTEBOOKS_DIR / "1_2_tiger"
ACS_DIR: Path = DATA_NOTEBOOKS_DIR / "1_3_acs"
ACS_HANDMADE_DIR: Path = ACS_DIR / "handmade"

JOIN_ROLES_DIR: Path = DATA_DIR / "2_join_and_roles"
JOIN_ROLES_HANDMADE_DIR: Path = JOIN_ROLES_DIR / "handmade"

OUTPUTS_DIR: Path = PROJECT_ROOT / "outputs"
