import pandas as pd

def latest_login(logins: pd.DataFrame) -> pd.DataFrame:
    
    result = logins[logins['time_stamp'].dt.year==2020]
    result = result.groupby('user_id', as_index=False).agg(last_stamp=('time_stamp','max'))

    return result