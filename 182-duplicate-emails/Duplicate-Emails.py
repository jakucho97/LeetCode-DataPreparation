import pandas as pd

def duplicate_emails(person: pd.DataFrame) -> pd.DataFrame:
    
    result = person[person['email'].duplicated()==True].drop_duplicates(subset=['email'])
    return result[['email']]