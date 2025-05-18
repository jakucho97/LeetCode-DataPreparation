import pandas as pd

def find_investments(insurance: pd.DataFrame) -> pd.DataFrame:
    
    location = insurance.drop_duplicates(subset=['lat','lon'], keep=False)
    value = insurance[insurance['tiv_2015'].duplicated(keep=False)]

    result = insurance[(insurance['pid'].isin(location['pid'])) & (insurance['pid'].isin(value['pid']))]

    return pd.DataFrame(result[['tiv_2016']].sum(), columns=['tiv_2016'])