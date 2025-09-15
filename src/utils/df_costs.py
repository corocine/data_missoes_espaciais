import pandas as pd


def generate_df_costs(df: pd.DataFrame):
    """
    Prepares and filters a DataFrame with mission cost details.

    This function selects specific columns related to costs, removes 
    records without price data, and sorts the result by the highest price. 
    The goal is to prepare a clean table for display or analysis.

    Args:
        df (pd.DataFrame): The input DataFrame. Expected to contain the 
                           columns 'Empresa', 'Missao', 'Preco', 
                           'RegiaoLancamento', 'AnoLancamento', and 'StatusMissao'.

    Returns:
        dict or None: A dictionary containing the processed DataFrame and 
                      its length, or None if the input DataFrame is empty.
                      The dictionary contains the following keys:
                        - 'df_costs' (pd.DataFrame): The cleaned and sorted cost table.
                        - 'df_len' (int): The number of records in the final table.
"""
    if df.empty:
        return None
    
    
    df_costs = df[['Empresa', 'Missao', 'Preco', 'RegiaoLancamento', 'AnoLancamento', 'StatusMissao']].sort_values(by='Preco', ascending=False)
    df_costs = df_costs.dropna(subset=['Preco'])
    df_costs.groupby('Missao')['Preco'].sum()
    df_len = len(df_costs)
    
    result = {
        'df_costs': df_costs,
        'df_len': df_len
    }
    
    return result