import pandas as pd
from pathlib import Path
import streamlit as st

BASE_DIR = Path.cwd()
db_path = BASE_DIR / 'data' / "space_missions.parquet"


@st.cache_data
def load_data():
    
    df = pd.read_parquet(db_path)
    return df
    

