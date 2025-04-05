import pandas as pd

df = pd.read_csv('student.csv')

average_cgpa = df['CGPA'].mean()
print(average_cgpa)

high_cgpa_students = df[df['CGPA'] > 9]
print(high_cgpa_students)

cse_students_high_cgpa = df[(df['Branch'] == 'CSE') & (df['CGPA'] > 9)]
print(cse_students_high_cgpa)

max_cgpa_student = df.loc[df['CGPA'].idxmax()]
print(max_cgpa_student)

average_cgpa_by_branch = df.groupby('Branch')['CGPA'].mean()
print(average_cgpa_by_branch)
