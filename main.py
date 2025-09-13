import streamlit as st 
from src.utils.variables import LOGO_DIR
from src.utils.load_data import load_data
from src.components.filters import show_filters
from src.components.filters import show_record_count
from src.components.metrics import show_metrics
from src.components.charts.rockets_launches_by_country_chart import rockets_launches_by_country_chart
from src.components.charts.status_mission_chart import status_mission_chart
from src.components.charts.company_launches import company_launches_chart


def main():
    """
    Main function that orchestrates the creation and display of the dashboard.
    """
    st.set_page_config(
        page_title='Missões espaciais', 
        page_icon=LOGO_DIR,
        initial_sidebar_state='auto',
        layout='wide',
        menu_items= None               
    ) 
    
    st.title('Análise descritiva de missões espaciais')
    st.write('Essa análise detalha os lançamentos das missões espaciais realizadas no período de 1957 até 2022')
    
    df = load_data()
    
    if df is None:
        st.info("Nenhum dado disponível para exibição.")
        st.stop()
        
    df_filtred = show_filters(df)
        
    if df_filtred.empty:
        st.warning("Nenhum dado encontrado com os filtros selecionados.")
        st.stop()
        
    show_record_count(df_filtred)
    
    show_metrics(df_filtred)
    
    col1, col2 = st.columns([0.6, 0.4])
    
    with col1:
        status_mission_chart(df_filtred)
    
    with col2:
        company_launches_chart(df_filtred)
        
    st.markdown('---')
    
    rockets_launches_by_country_chart(df_filtred)
    
    
    
    st.markdown('---')
    st.dataframe(df_filtred)
    
    
if __name__ == '__main__':
    main()