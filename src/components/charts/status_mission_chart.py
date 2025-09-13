import pandas as pd
import plotly.express as px
import streamlit as st
from src.utils.variables import CATEGORIES_COLORS

def status_mission_chart(df: pd.DataFrame):
    
    if df.empty:
        st.info("Nenhum dado disponível para exibição.")
        st.stop()
    
    st.subheader('Status da Missão por Região de Lançamento')
    df_chart = df.copy()
    df_chart['quantidade'] = 1 
    df_chart['StatusMissao'] = df_chart['StatusMissao'].astype(str)
    df_chart['RegiaoLancamento'] = df_chart['RegiaoLancamento'].astype(str)
    
    fig_sunburst = px.sunburst(
                df_chart,
                path=['StatusMissao', 'RegiaoLancamento'], 
                values='quantidade',
                
                color='StatusMissao',
                color_discrete_sequence=CATEGORIES_COLORS
            )
             
    fig_sunburst.update_traces(
        textinfo='label+percent parent', 
        hovertemplate='<b>%{label}</b><br>Nº de Missões: %{value}<br>Percentual do Anel Anterior: %{percentParent:.1%}<extra></extra>'
    )
            
    fig_sunburst.update_layout(
        margin=dict(t=5, l=5, r=5, b=5)
    )
            
    st.plotly_chart(fig_sunburst, use_container_width=True)
