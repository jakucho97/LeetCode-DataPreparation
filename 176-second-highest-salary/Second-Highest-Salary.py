import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    
    employee=employee.drop_duplicates(subset=['salary'])
    employee['rank'] = employee['salary'].rank(method='dense', ascending=False)
    

    if len(employee) < 2:
        return pd.DataFrame({'SecondHighestSalary': [None]})
    
    
    result = pd.DataFrame()
    result['SecondHighestSalary'] = employee['salary'][employee['rank']==2]
    return result