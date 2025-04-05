import pandas as pd

data = {'Name': ['Alice', 'Bob', 'Charlie'], 'Age': [24, 27, 22]}
df = pd.DataFrame(data)

df.to_excel('output.xlsx', index=False)
