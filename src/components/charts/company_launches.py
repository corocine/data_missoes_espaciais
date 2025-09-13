import pandas as pd
import plotly.express as px
import streamlit as st
from src.utils.variables import CATEGORIES_COLORS


def company_launches_chart(df: pd.DataFrame):
    
    if df.empty:
        st.info("Nenhum dado disponível para exibição.")
        st.stop()
    
    st.subheader('Número de missões por empresa')
    
    companies = df.groupby('Empresa')['Missao'].size().nlargest(8).reset_index()   
    
    fig = px.pie(
        companies,
        names='Empresa',
        values='Missao',
        color='Empresa',
        color_discrete_sequence=CATEGORIES_COLORS,
        labels={'Empresa': 'Empresa', 'Missao': 'Número de missões'},
        )
    
    st.plotly_chart(fig, use_container_width=True)
    