import pandas as pd
import plotly.express as px
import streamlit as st
from src.utils.variables import CATEGORIES_COLORS

def rockets_launches_by_country_chart(df: pd.DataFrame):
    
    if df.empty:
        st.info("Nenhum dado disponível para exibição.")
        st.stop()
    
    st.subheader('Número de foguetes por região de lançamento')
    
    rockets = df.groupby('RegiaoLancamento')['Foguete'].size().nlargest(10).reset_index()
    
    fig = px.bar(
        rockets,
        x='RegiaoLancamento',
        y='Foguete',
        color='Foguete',
        color_continuous_scale=CATEGORIES_COLORS[::-1],
        labels={'RegiaoLancamento': 'Região de lançamento', 'Foguete': 'Número de foguetes'}, 
    )
    fig.update_traces(
        hovertemplate="<br><b>Região de Lançamento</b>: %{x}<br><b>Nº Foguetes</b>: %{y:,.0f}<br><extra></extra>"
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    