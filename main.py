import streamlit as st 
from src.utils.variables import LOGO_DIR


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
if __name__ == '__main__':
    main()