import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('weather.csv')

print(df.head(10))

max_temp = df['temperature'].max()
min_temp = df['temperature'].min()
print(max_temp, min_temp)

places_less_than_28 = df[df['temperature'] < 28]['place']
print(places_less_than_28)

cloudy_places = df[df['weather'] == 'Cloudy']['place']
print(cloudy_places)

weather_frequency = df['weather'].value_counts()
print(weather_frequency)

df.plot(x='date', y='temperature', kind='bar', figsize=(10, 6))
plt.title('Temperature of Each Day')
plt.xlabel('Date')
plt.ylabel('Temperature')
plt.show()
