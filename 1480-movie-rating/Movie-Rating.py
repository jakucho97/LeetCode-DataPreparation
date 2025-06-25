import pandas as pd

def movie_rating(movies: pd.DataFrame, users: pd.DataFrame, movie_rating: pd.DataFrame) -> pd.DataFrame:
    
    best_raters = movie_rating.groupby('user_id', as_index=False).size()
    best_raters = best_raters.merge(users, how='left', on='user_id').sort_values(by=['size','name'], ascending=[False, True]).head(1)

    best_movie = movie_rating[(movie_rating['created_at'].dt.month==2) & (movie_rating['created_at'].dt.year==2020)]
    best_movie = best_movie.groupby('movie_id', as_index=False)['rating'].mean()
    best_movie = best_movie.merge(movies, how='left', on='movie_id').sort_values(by=['rating','title'], ascending=[False,True]).head(1)

    result = pd.DataFrame({'results':[best_movie.iloc[0,2],best_raters.iloc[0,2]]})

    return result