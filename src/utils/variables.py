from pathlib import Path

BASE_DIR = Path.cwd()
LOGO_DIR = BASE_DIR / 'data' / 'logo.ico'
PARQUET_PATH = BASE_DIR / 'data' / "space_missions.parquet"
CSV_DIR = BASE_DIR / 'data' / 'space_missions.csv'


PRIMARY_COLOR    = "#4A148C"
SECONDARY_COLOR  = "#6A1B9A"
TERTIARY_COLOR   = "#8E24AA"
QUATERNARY_COLOR = "#AB47BC"
QUINARY_COLOR    = "#CE93D8"
SENARY_COLOR     = "#F3E5F5"

SCALE_COLOR_MAP = 'Purples'

CATEGORIES_COLORS = [
    PRIMARY_COLOR,
    SECONDARY_COLOR,
    TERTIARY_COLOR,
    QUATERNARY_COLOR,
    QUINARY_COLOR,
    SENARY_COLOR
]