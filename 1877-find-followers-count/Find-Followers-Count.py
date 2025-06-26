import pandas as pd

def count_followers(followers: pd.DataFrame) -> pd.DataFrame:
    result= followers.groupby('user_id', as_index=False).size().rename(columns={'size':'followers_count'}).sort_values(by='user_id')

    return result