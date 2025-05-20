import pandas as pd

def find_customers(customer: pd.DataFrame, product: pd.DataFrame) -> pd.DataFrame:
    
    result = customer.groupby('customer_id', as_index=False).agg(set)
    
    result = result[result['product_key'] == set(product['product_key'])]

    return result[['customer_id']]