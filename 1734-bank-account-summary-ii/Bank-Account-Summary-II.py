import pandas as pd

def account_summary(users: pd.DataFrame, transactions: pd.DataFrame) -> pd.DataFrame:
    
    result = transactions.groupby('account', as_index=False)['amount'].sum()
    result = result[result['amount']>10000].merge(users, on='account').rename(columns={'amount':'BALANCE','name':'NAME'})

    return result[['NAME','BALANCE']]