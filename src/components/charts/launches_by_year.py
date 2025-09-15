import pandas as pd
import plotly.express as px
import streamlit as st

def launches_by_year(df: pd.DataFrame):
    
    if df.empty:
        st.info("Nenhum dado disponível para exibição.")
        st.stop()

    st.subheader('Número de Lançamentos por Ano e Região')
    
    launches_by_year_and_region = df.groupby(['AnoLancamento', 'RegiaoLancamento']).size().reset_index(name='Numero de Lancamentos')
    
    top_5_regions = df['RegiaoLancamento'].value_counts().nlargest(5).index
    
    data_to_plot = launches_by_year_and_region[launches_by_year_and_region['RegiaoLancamento'].isin(top_5_regions)]

    fig_launches_by_year = px.line(
        data_frame=data_to_plot,        
        x='AnoLancamento',                 
        y='Numero de Lancamentos',    
        color='RegiaoLancamento',         
        markers=True,              
        labels={                        
            'AnoLancamento': 'Ano', 
            'Numero de Lancamentos': 'Número de Lançamentos', 
            'RegiaoLancamento': 'Região'
        },
    )
    
    fig_launches_by_year.update_layout(
        legend_title_text='Região de Lançamento'
    )
    
    st.plotly_chart(fig_launches_by_year, use_container_width=True, key="fig_launches_by_year")