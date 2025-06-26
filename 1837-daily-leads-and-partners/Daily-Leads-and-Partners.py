import pandas as pd

def daily_leads_and_partners(daily_sales: pd.DataFrame) -> pd.DataFrame:
    result = daily_sales.groupby(by=['date_id','make_name'], as_index=False).nunique().rename(columns={'lead_id':'unique_leads','partner_id':'unique_partners'})

    return result