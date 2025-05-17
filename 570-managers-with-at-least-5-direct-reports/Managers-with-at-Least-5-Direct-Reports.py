import pandas as pd

def find_managers(employee: pd.DataFrame) -> pd.DataFrame:
    
    five = employee.groupby('managerId', as_index=False).size()
    five = five[five['size']>=5]

    result = employee[employee['id'].isin(five['managerId'])][['name']]

    return result