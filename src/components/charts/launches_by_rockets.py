import pandas as pd
import plotly.express as px
import streamlit as st
from src.utils.variables import SCALE_COLOR_MAP 

def top_rockets_by_mission_chart(df: pd.DataFrame):
    if df.empty:
        st.info("Nenhum dado disponível para exibição.")
        st.stop()

    st.subheader("Top 10 Foguetes por Número de Missões Realizadas")
    
    rocket_counts = (
        df.groupby('Foguete')
        .size()
        .reset_index(name='TotalMissoes')
    )

    rocket_info = (
        df.groupby('Foguete')
        .agg({
            'RegiaoLancamento': lambda x: x.mode()[0] if not x.mode().empty else None,
            'AnoLancamento': 'max'
        })
        .reset_index()
    )

    data_to_plot = (
        rocket_counts
        .merge(rocket_info, on='Foguete', how='left')
        .nlargest(10, 'TotalMissoes')
    )
    
    fig_top_rockets_by_mission = px.bar(
    data_frame=data_to_plot.sort_values(by='TotalMissoes', ascending=True),
    x='TotalMissoes',
    y='Foguete',
    orientation='h',
    color='TotalMissoes',
    color_continuous_scale=SCALE_COLOR_MAP,
    text='TotalMissoes',
    labels={'TotalMissoes': 'Número de Missões', 'Foguete': 'Modelo do Foguete'},
    custom_data=['RegiaoLancamento', 'AnoLancamento']
)

    fig_top_rockets_by_mission.update_traces(
        textposition='inside',
        hovertemplate='<b>%{y}</b><br>Nº de Missões: %{x}<br>'
                    'Região: %{customdata[0]}<br>'
                    'Ano do último Lançamento: %{customdata[1]}<extra></extra>'
    )

    st.plotly_chart(fig_top_rockets_by_mission, use_container_width=True, key="fig_top_rockets_by_mission")