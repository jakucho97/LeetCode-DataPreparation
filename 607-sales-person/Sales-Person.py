import pandas as pd

def sales_person(sales_person: pd.DataFrame, company: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    
    merged = orders.merge(company, how='left', on=['com_id'])
    merged = merged[merged['name']=='RED']

    return sales_person[~sales_person['sales_id'].isin(merged['sales_id'])][['name']]