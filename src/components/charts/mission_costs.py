import pandas as pd
import plotly.express as px
import streamlit as st
from src.utils.header_prices import header_prices
from src.utils.df_costs import generate_df_costs
from src.utils.variables import CATEGORIES_COLORS, PRIMARY_COLOR, SECONDARY_COLOR



def mission_costs(df: pd.DataFrame):
    
    if df.empty:
        st.info("Nenhum dado disponível para exibição.")
        st.stop()
    
    col1, col2 = st.columns([0.5, 0.5])
    
    with col1:
          
        st.subheader("Top missões com maiores orçamentos")
        
        df_costs = generate_df_costs(df)
        
        if df_costs is None:
            st.info("Nenhum dado disponível para exibição.")
            st.stop()
        
        df = df_costs['df_costs']
        
        df_top_10_costs = df.nlargest(10, 'Preco')

        fig_top_10_costs = px.funnel(
            df_top_10_costs,
            x='Preco',
            y='Missao',
            color='StatusMissao',
            color_discrete_sequence=CATEGORIES_COLORS,
            custom_data=['RegiaoLancamento', 'AnoLancamento', 'StatusMissao']
            )
        
        fig_top_10_costs.update_traces(
            textinfo='value', 
            hovertemplate='<b>%{customdata[0]}</b><br><b>Status da Missão:</b> %{customdata[2]}<br>Ano de Lançamento: %{customdata[1]}<br><extra></extra>'
        )
        
            
        st.plotly_chart(fig_top_10_costs, use_container_width=True, key='fig_top_10_costs')
        
    
    with col2:
        st.subheader("Top missões com menores orçamentos")  

        df_costs = generate_df_costs(df)
        
        if df_costs is None:
            st.info("Nenhum dado disponível para exibição.")
            st.stop()
        
        df = df_costs['df_costs']
        
        df_top_10_costs_nsmallest = df.nsmallest(10, 'Preco')

        fig_top_10_costs_nsmallest = px.funnel(
            df_top_10_costs_nsmallest,
            x='Preco',
            y='Missao',
            color='StatusMissao',
            color_discrete_sequence=[SECONDARY_COLOR, PRIMARY_COLOR],
            custom_data=['RegiaoLancamento', 'AnoLancamento', 'StatusMissao']
            )
        
        fig_top_10_costs_nsmallest.update_traces(
            textinfo='value', 
            hovertemplate='<b>%{customdata[0]}</b><br><b>Status da Missão:</b> %{customdata[2]}<br>Ano de Lançamento: %{customdata[1]}<br><extra></extra>'
        )
            
        st.plotly_chart(fig_top_10_costs_nsmallest, use_container_width=True, key='fig_top_10_costs_nsmallest')