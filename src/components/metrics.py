import streamlit as st
import pandas as pd
import humanize


def show_metrics(df: pd.DataFrame):
    
    total_price = int(df['Preco'].sum())
    humanize_value = humanize.intword(total_price).replace("billion", "bilhões").replace("million", "milhões")
    total_rockets = df['Foguete'].nunique()
    total_missions = f'{(df['Missao'].nunique()):,}'
    company_with_more_missions = df['Empresa'].value_counts().idxmax()
    top_period = df['AnoLancamento'].mode().iloc[0]
    
    records_with_price = df['Preco'].count()
    total_records = len(df)
    available_percentage = (records_with_price / total_records) * 100
    
    
    col1, col2, col3, col4, col5 = st.columns([0.2, 0.1, 0.1, 0.15, 0.2])
    
    with col1:
        st.metric('Gasto total', f'US${humanize_value}', help= f"""
            Este valor é a soma dos custos de apenas {records_with_price} missões
            ({available_percentage:.1f}% do total), que são as que possuem dados de preço disponíveis.
            O gasto total real de todas as missões é consideravelmente maior.
            """,)
    with col2:
        st.metric('Foguetes utilizados', total_rockets)
    
    with col3:
        st.metric('Missões realizadas', f'{(total_missions).replace(",", ".")}')
    
    with col4:
        st.metric('Empresa com mais missões', company_with_more_missions)
    
    with col5:
        st.metric('Período com mais lançamentos', top_period)
    
    st.markdown('---')