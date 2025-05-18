import pandas as pd

def largest_orders(orders: pd.DataFrame) -> pd.DataFrame:
    
    orders = orders.groupby('customer_number', as_index=False).size()
    orders = orders[orders['size']==orders['size'].max()]

    return orders[['customer_number']]