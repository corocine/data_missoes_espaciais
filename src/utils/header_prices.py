import pandas as pd

def header_prices(df: pd.DataFrame):
    """
    Calculates and formats statistics about the availability of price data.

    This function analyzes the 'Preco' column of a DataFrame to determine
    how many records contain valid cost data and what percentage this 
    represents of the total. It returns this information in a structured 
    dictionary.

    Args:
        df (pd.DataFrame): The input DataFrame. Expected to contain 
                           a column named 'Preco'.

    Returns:
        dict or None: A dictionary containing price statistics, or None 
                      if the input DataFrame is empty.
                      The dictionary contains the following keys:
                        - 'records_with_price' (int): Number of records with price.
                        - 'total_records' (int): Total number of records.
                        - 'available_percentage' (float): Percentage of available price data.
                        - 'message' (str): A formatted message for use in tooltips.
"""
    
    if df.empty:
        return None
    
    records_with_price = df['Preco'].count()
    total_records = len(df)
    available_percentage = (records_with_price / total_records) * 100
    message = f"""
            Este valor corresponde à soma dos custos de apenas {records_with_price} missões
            ({available_percentage:.1f}% do total), que possuem dados de preço disponíveis. 
            O gasto total real de todas as missões é consideravelmente maior.
            """
    result = {
        
        'records_with_price': records_with_price,
        'total_records': total_records,
        'available_percentage': available_percentage,
        'message': message
        
    }
    
    return result