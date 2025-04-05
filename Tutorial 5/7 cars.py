import pandas as pd

df = pd.read_csv("auto.csv")
df.dropna(inplace=True)
df['engine-type'] = df['engine-type'].replace('unknown', 'Other')
df.to_csv("cleaned_auto.csv", index=False)

most_expensive_car = df.loc[df['price'].idxmax()]
print(most_expensive_car['company'])

toyota_cars = df[df['company'] == 'Toyota']
print(toyota_cars)

total_cars = df['company'].value_counts()
print(total_cars)

highest_priced_car = df.loc[df['price'].idxmax()]
print(highest_priced_car)

average_mileage = df.groupby('company')['average-mileage'].mean()
print(average_mileage)

sorted_cars = df.sort_values('price', ascending=False)
print(sorted_cars)
