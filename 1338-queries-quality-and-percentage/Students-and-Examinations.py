import pandas as pd

def students_and_examinations(students: pd.DataFrame, subjects: pd.DataFrame, examinations: pd.DataFrame) -> pd.DataFrame:
    
    students=students.merge(subjects, how='cross')
    grouped_exams = examinations.groupby(by=['student_id','subject_name'], as_index=False).size()

    result = students.merge(grouped_exams,how='left', on=['student_id','subject_name']).fillna({'size':0}).rename(columns={'size':'attended_exams'}).sort_values(by=['student_id','subject_name'])

    return result