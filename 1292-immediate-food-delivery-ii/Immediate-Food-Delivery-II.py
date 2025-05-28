import pandas as pd

def immediate_food_delivery(delivery: pd.DataFrame) -> pd.DataFrame:
    
    grouped = delivery.iloc[delivery.groupby('customer_id')['order_date'].idxmin()]
    grouped_immediate = grouped[grouped['order_date']==grouped['customer_pref_delivery_date']]

    return pd.DataFrame({'immediate_percentage':[round(((len(grouped_immediate)/len(grouped))*100),2)]})