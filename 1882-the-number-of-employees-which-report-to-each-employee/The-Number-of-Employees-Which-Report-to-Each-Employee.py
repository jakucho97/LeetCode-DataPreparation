import pandas as pd

def count_employees(employees: pd.DataFrame) -> pd.DataFrame:
    employees = employees.merge(employees, left_on='employee_id', right_on='reports_to')
    employees = employees.groupby(by=['employee_id_x','name_x'], as_index=False).agg(reports_count=('employee_id_x','size'),average_age=('age_y',lambda x: int(x.mean()+0.5)))

    return employees.rename(columns={'employee_id_x':'employee_id','name_x':'name'})