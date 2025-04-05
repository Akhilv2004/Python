import pandas as pd

df = pd.read_csv('employee.csv')

print(df.head(7))

print(df['name'].sort_values())

highest_salary_employee = df.loc[df['salary'].idxmax()]
print(highest_salary_employee['name'])

male_employees = df[df['gender'] == 'Male']['name']
print(male_employees)

teams = df['team'].unique()
print(teams)
