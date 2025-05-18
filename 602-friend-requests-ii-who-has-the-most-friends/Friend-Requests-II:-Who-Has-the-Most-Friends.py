import pandas as pd

def most_friends(request_accepted: pd.DataFrame) -> pd.DataFrame:

    accepted = request_accepted.rename(columns={'accepter_id':'id'})[['id']]
    requested = request_accepted.rename(columns={'requester_id':'id'})[['id']]

    result = pd.concat([accepted,requested]).groupby('id', as_index=False).size().rename(columns={'size':'num'})

    return result[result['num']==result['num'].max()]