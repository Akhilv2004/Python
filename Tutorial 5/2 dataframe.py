import pandas as pd

data = [['Alice', 24], ['Bob', 27], ['Charlie', 22]]
df = pd.DataFrame(data, columns=['Name', 'Age'])

df.set_index('Name', inplace=True)

print(df)
