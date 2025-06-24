import pandas as pd

def restaurant_growth(customer: pd.DataFrame) -> pd.DataFrame:
    
    grouped = customer.groupby('visited_on', as_index=False).sum()

    grouped['average_amount']=grouped['amount'].rolling(7).mean().round(2)
    grouped = grouped.rename(columns={'amount':'single_amount'})
    grouped['amount']=grouped['single_amount'].rolling(7).sum().round(2)
    grouped=grouped[~grouped['average_amount'].isnull()]


    return grouped[['visited_on','amount','average_amount']]