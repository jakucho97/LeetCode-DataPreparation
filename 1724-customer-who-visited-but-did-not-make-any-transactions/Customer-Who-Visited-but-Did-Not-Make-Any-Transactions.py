import pandas as pd

def find_customers(visits: pd.DataFrame, transactions: pd.DataFrame) -> pd.DataFrame:
    visits=visits.merge(transactions, how='left', on='visit_id')
    visits=visits[visits['transaction_id'].isnull()].groupby('customer_id', as_index=False).size().rename(columns={'size':'count_no_trans'})

    return visits