import streamlit as st
import pandas as pd


def show_filters(df: pd.DataFrame):
    
    st.sidebar.markdown("<h1 style='text-align: center;'> Preferências </h1>", unsafe_allow_html=True)
    
    company = sorted(df['Empresa'].unique().tolist())
    country = sorted(df['RegiaoLancamento'].unique().tolist())
    rocket = sorted(df['Foguete'].unique().tolist())
    statusMission = sorted(df['StatusMissao'].unique().tolist())
    year = df['AnoLancamento'].unique().tolist()
    
    
    company_filter = st.sidebar.multiselect('Selecionar empresa', company, default=[])
    country_filter = st.sidebar.multiselect('Selecionar região de lançamento', country, default=[])
    rocket_filter = st.sidebar.multiselect('Selecionar foguete', rocket, default=[])
    statusMission_filter = st.sidebar.multiselect('Selecionar status da missão', statusMission, default=[])
    year_filter = st.sidebar.multiselect('Selecionar ano da missão', year, default=[])
    
    df_filtered = df.copy()
    
    if company_filter:
         df_filtered = df_filtered[df_filtered['Empresa'].isin(company_filter)]
    if country_filter:
        df_filtered = df_filtered[df_filtered['RegiaoLancamento'].isin(country_filter)]
    if rocket_filter:
        df_filtered = df_filtered[df_filtered['Foguete'].isin(rocket_filter)]
    if statusMission_filter:
        df_filtered = df_filtered[df_filtered['StatusMissao'].isin(statusMission_filter)]
    if year_filter:
        df_filtered = df_filtered[df_filtered['AnoLancamento'].isin(year_filter)]
    
    return df_filtered
    

def show_record_count(df_filtred): 
    """
    Displays the count of records found in the sidebar.

    Args:
        df_filtred (pd.DataFrame): The filtered DataFrame.
    """
    search_size = len(df_filtred)
    st.sidebar.write(f"Registros encontrados: {(search_size):,}")
    