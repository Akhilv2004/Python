import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('sales.csv')

# 1) Toothpaste sales data of each month and show it using a scatter plot
plt.scatter(df['month_number'], df['toothpaste'])
plt.title('Toothpaste Sales Data')
plt.xlabel('Month Number')
plt.ylabel('Toothpaste Sales')
plt.show()

# 2) Face cream and face wash product sales data and show it using the bar chart
df[['month_number', 'facecream', 'facewash']].set_index('month_number').plot(kind='bar', figsize=(10, 6))
plt.title('Face Cream and Face Wash Sales Data')
plt.xlabel('Month Number')
plt.ylabel('Sales')
plt.show()

# 3) Calculate total sale data for last year for each product and show it using a Pie chart
total_sales = df[['facecream', 'facewash', 'toothpaste', 'bathingsoap', 'shampoo', 'moisturizer']].sum()
total_sales.plot(kind='pie', autopct='%1.1f%%', figsize=(8, 8), title='Total Sales Data for Last Year')
plt.ylabel('')
plt.show()
