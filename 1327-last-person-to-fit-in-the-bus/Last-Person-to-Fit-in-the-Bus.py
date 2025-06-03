import pandas as pd

def last_passenger(queue: pd.DataFrame) -> pd.DataFrame:
    
    queued = queue.sort_values(by=['turn'])
    queued['weight_sum'] = queued['weight'].cumsum()

    return queued[queued['weight_sum'] <= 1000].tail(1)[['person_name']]