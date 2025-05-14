import pandas as pd

def rising_temperature(weather: pd.DataFrame) -> pd.DataFrame:
    result = weather.sort_values(by='recordDate')

    return result[(result['recordDate'].diff().dt.days==1) & (result['temperature'].diff()>0)][['id']]