import pandas as pd
from pathlib import Path

BASE_DIR = Path.cwd()
db_path = BASE_DIR / 'data' / "space_missions.csv"

df = pd.read_csv(db_path,  encoding='latin-1')
    
df['Company'] = df['Company'].astype('category')
df['Rocket'] = df['Rocket'].astype('category')
df['Mission'] = df['Mission'].astype('category')
df['RocketStatus'] = df['RocketStatus'].astype('category')
df['MissionStatus'] = df['MissionStatus'].astype('category')
df['Company'] = df['Company'].astype('category')
df['Country'] = df['Location'].str.split(',').str[-1].str.strip()
df['Country'] = df['Country'].astype('category')
df['Price'] = df['Price'].str.replace(',', '', regex=False)
df['Price'] = df['Price'].astype(float)
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
df['Year'] = df['Date'].dt.year
df['Date'] = df['Date'].dt.date
df['Time'] = pd.to_datetime(df['Time'], errors='coerce')
df['Time'] = df['Time'].dt.time

columns_translated = {
    'Company': 'Empresa',
    'Location': 'Localizacao',
    'Date': 'Data',
    'Time': 'Hora',
    'Rocket': 'Foguete',
    'Mission': 'Missao',
    'RocketStatus': 'StatusFoguete',
    'Price': 'Preco',
    'MissionStatus': 'StatusMissao',
    'Country': 'RegiaoLancamento',
    'Year': 'AnoLancamento'
}

df.rename(columns=columns_translated, inplace=True) 

output_dir = BASE_DIR / 'data'
output_dir.mkdir(parents=True, exist_ok=True)
df.to_parquet(output_dir / 'space_missions.parquet')