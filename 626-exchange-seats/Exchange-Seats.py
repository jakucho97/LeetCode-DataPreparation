import pandas as pd

def exchange_seats(seat: pd.DataFrame) -> pd.DataFrame:
    
    df = seat
    for i in range(0,len(df)-1,2):
        df.iloc[i,0], df.iloc[i+1,0] = df.iloc[i+1,0],df.iloc[i,0]

    return df.sort_values(by='id')