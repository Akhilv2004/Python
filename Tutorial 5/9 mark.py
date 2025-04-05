import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = {
    'rollno': [1, 2, 3, 4, 5],
    'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'place': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix'],
    'mark': [85, 90, 88, 92, 80]
}

df = pd.DataFrame(data)
df.to_csv('stud.csv', index=False)

df = pd.read_csv('stud.csv')
print(df)

df.set_index('rollno', inplace=True)
print(df[['name', 'mark']])

df_sorted_by_name = df[['rollno', 'name', 'mark']].sort_values('name')
print(df_sorted_by_name)

df_sorted_by_mark = df[['rollno', 'name', 'mark']].sort_values('mark', ascending=False)
print(df_sorted_by_mark)

average_mark = df['mark'].mean()
median_mark = df['mark'].median()
mode_mark = df['mark'].mode()[0]
print("Average Mark:", average_mark)
print("Median Mark:", median_mark)
print("Mode Mark:", mode_mark)

min_mark = df['mark'].min()
max_mark = df['mark'].max()
print("Minimum Mark:", min_mark)
print("Maximum Mark:", max_mark)

variance_mark = df['mark'].var()
std_deviation_mark = df['mark'].std()
print("Variance of Marks:", variance_mark)
print("Standard Deviation of Marks:", std_deviation_mark)

df.drop('place', axis=1, inplace=True)
print(df)

df['mark'].hist()
plt.title('Histogram of Marks')
plt.xlabel('Marks')
plt.ylabel('Frequency')
plt.show()
