import pandas as pd

def employee_bonus(employee: pd.DataFrame, bonus: pd.DataFrame) -> pd.DataFrame:
    
    merged = employee.merge(bonus, how='left', on=['empId'])

    result = merged[(merged['bonus']<1000) | (merged['bonus'].isnull())]

    return result[['name', 'bonus']]