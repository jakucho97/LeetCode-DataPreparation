import pandas as pd

def top_three_salaries(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    
    employee = employee.rename(columns={'name':'Employee','salary':'Salary'})
    department = department.rename(columns={'id':'departmentId','name':'Department'})

    employee['rank'] = employee.groupby('departmentId')['Salary'].rank(method='dense', ascending=False)

    result = employee.merge(department, how='left',on='departmentId')
    result = result[result['rank']<=3][['Department','Employee','Salary']]

    return result