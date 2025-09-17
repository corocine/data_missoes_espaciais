import pandas as pd
import plotly.express as px
import streamlit as st
from src.utils.variables import CATEGORIES_COLORS

def launches_choropleth_map(df: pd.DataFrame):
    if df.empty:
        st.info("Nenhum dado disponível para o mapa.")
        st.stop()
        
    st.subheader("Mapa Global de Lançamentos Espaciais")
    launches_by_country = df.groupby('RegiaoLancamento')['Missao'].size().reset_index() 
    
    fig = px.choropleth(
        data_frame=launches_by_country,
        locations='RegiaoLancamento',          
        locationmode='country names',
        color='Missao', 
        hover_name='RegiaoLancamento', 
        color_continuous_scale='Blues',
    )
    
    fig.update_layout(
        geo=dict(showframe=False, showcoastlines=False),
        margin={"r":0,"t":40,"l":0,"b":0}
    )
    
    fig.update_traces(
        hovertemplate="<b>%{location}</b><br><b>Nº de Lançamentos:</b> %{z}<extra></extra>"
    )
    
    
    st.plotly_chart(fig, use_container_width=True)