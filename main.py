import streamlit as st 
from src.utils.variables import LOGO_DIR
from src.utils.load_data import load_data
from src.components.filters import show_filters
from src.components.filters import show_record_count

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
    
    df = load_data()
    
    if df is None:
        st.info("Nenhum dado disponível para exibição.")
        st.stop()
        
    df_filtred = show_filters(df)
        
    if df_filtred.empty:
        st.warning("Nenhum dado encontrado com os filtros selecionados.")
        st.stop()
        
    show_record_count(df_filtred)

    st.dataframe(df_filtred)
    
    
if __name__ == '__main__':
    main()