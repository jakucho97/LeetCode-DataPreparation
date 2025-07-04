import pandas as pd

def human_traffic(stadium: pd.DataFrame) -> pd.DataFrame:
    check=[]
    for i in range(0,len(stadium)-2):
        consecutive=[]
        for j in range(0,3):
            if stadium['people'].iloc[i+j]>=100:
                consecutive.append(int(stadium['id'].iloc[i+j]))
        if len(consecutive)==3:
            i=i
            for x in consecutive:
                check.append(x)

    result = stadium[stadium['id'].isin(check)]

    return result