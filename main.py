import streamlit as st 
from src.utils.variables import LOGO_DIR
from src.utils.load_data import load_data
from src.components.filters import show_filters
from src.components.filters import show_record_count
from src.components.metrics import show_metrics
from src.components.charts.rockets_launches_by_country_chart import rockets_launches_by_country_chart
from src.components.charts.status_mission_chart import status_mission_chart
from src.components.charts.company_launches import company_launches_chart
from src.components.charts.launches_by_year import launches_by_year
from src.components.charts.mission_costs import mission_costs
from src.components.charts.launches_map import launches_choropleth_map
from src.utils.header_prices import header_prices
from src.components.charts.launches_by_rockets import top_rockets_by_mission_chart

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
    
    st.title('Histórico de missões espaciais')
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
    
    
    st.markdown("<h2 style='text-align: center; padding-bottom: 50px;;'>Qual a origem dos lançamentos?</h2>", unsafe_allow_html=True)
    
    col3, col4 = st.columns(2)
    
    with col3:
        launches_choropleth_map(df_filtred)
        
    with col4:
        rockets_launches_by_country_chart(df_filtred)
        
    
    launches_by_year(df_filtred)
    
    top_rockets_by_mission_chart(df_filtred)
    
    st.markdown('---')
    
    st.markdown("<h2 style='text-align: center; padding-bottom: 50px;;'>Qual a taxa de sucesso das missões e quais empresas realizam o serviço?</h2>", unsafe_allow_html=True)
    col1, col2 = st.columns(2)
        
    with col1:
        status_mission_chart(df_filtred)
    
    with col2:
        company_launches_chart(df_filtred)
        
    st.markdown('---')
    
    price_records = header_prices(df)
    
    if price_records is None:
        st.info("Nenhum dado disponível para exibição.")
        st.stop()
        
    price_records_message = price_records['message']
    
    st.markdown("<h2 style='text-align: center;;'>Distribuição dos Custos por Missão</h2>", unsafe_allow_html=True )
    st.info(price_records_message)
    mission_costs(df_filtred)
    
    st.markdown('---')
    
   
    
    st.dataframe(df_filtred)
    
if __name__ == '__main__':
    main()
   
