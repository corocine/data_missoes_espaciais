import streamlit as st
import pandas as pd
import humanize
from src.utils.header_prices import header_prices

def show_metrics(df: pd.DataFrame):
    
    total_price = int(df['Preco'].sum())
    humanize_value = humanize.intword(total_price).replace("billion", "bilhões").replace("million", "milhões")
    total_rockets = df['Foguete'].nunique()
    total_missions = f'{(df['Missao'].nunique()):,}'
    company_with_more_missions = df['Empresa'].value_counts().idxmax()
    top_period = df['AnoLancamento'].mode().iloc[0]
    
    price_records = header_prices(df)
    
    if price_records is None:
        st.info("Nenhum dado disponível para exibição.")
        st.stop()
        
    price_records_message = price_records['message']
    
    col1, col2, col3, col4, col5 = st.columns([0.2, 0.1, 0.1, 0.15, 0.2])
    
    with col1:
        st.metric('Gasto total', f'US${humanize_value}', help=price_records_message)
    with col2:
        st.metric('Foguetes utilizados', total_rockets)
    
    with col3:
        st.metric('Missões realizadas', f'{(total_missions).replace(",", ".")}')
    
    with col4:
        st.metric('Empresa com mais missões', company_with_more_missions)
    
    with col5:
        st.metric('Período com mais lançamentos', top_period)
    
    st.markdown('---')