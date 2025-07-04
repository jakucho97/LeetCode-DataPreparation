import pandas as pd

round2 = lambda x: round(x + 1e-9, 2)

def queries_stats(queries: pd.DataFrame) -> pd.DataFrame:

    queries['quality'] = queries['rating'] / queries['position'] + 1e-10
    queries['poor_query_percentage'] = (queries['rating']<3)*100

    result = queries.groupby('query_name', as_index=False).agg({'quality':'mean','poor_query_percentage':'mean'}).round(2)

    return result