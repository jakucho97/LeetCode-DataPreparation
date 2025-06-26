import pandas as pd

def users_percentage(users: pd.DataFrame, register: pd.DataFrame) -> pd.DataFrame:
    
    grouped = register.groupby('contest_id', as_index=False).size()
    grouped['percentage']=((grouped['size']/len(users))*100).round(2)

    return grouped[['contest_id','percentage']].sort_values(by=['percentage','contest_id'], ascending=[False,True])