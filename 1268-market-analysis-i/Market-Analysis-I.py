import pandas as pd

def market_analysis(users: pd.DataFrame, orders: pd.DataFrame, items: pd.DataFrame) -> pd.DataFrame:
    
    grouped = orders[orders['order_date'].dt.year==2019].groupby('buyer_id', as_index=False).size()

    result = users.merge(grouped,how='left',left_on=['user_id'], right_on=['buyer_id']).fillna(0)[['user_id','join_date','size']]
    
    return result.rename(columns={'user_id':'buyer_id','size':'orders_in_2019'})