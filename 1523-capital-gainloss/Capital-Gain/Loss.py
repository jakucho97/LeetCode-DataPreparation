import pandas as pd

def capital_gainloss(stocks: pd.DataFrame) -> pd.DataFrame:
    stocks['price'] = stocks['price'].where(stocks['operation']=='Sell', - stocks['price'])
    return stocks.groupby('stock_name', as_index=False).price.sum().rename(columns={"price":"capital_gain_loss"})