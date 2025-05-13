import pandas as pd

def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    
    merged = employee.merge(department, how='left', left_on=['departmentId'], right_on=['id'])
    merged['rank'] = merged.groupby(by=['departmentId'])['salary'].rank(method='dense', ascending=False)
    merged=merged.rename(columns={'name_x':'Employee','name_y':'Department','salary':'Salary'})

    return merged[merged['rank']==1][['Department','Employee','Salary']]