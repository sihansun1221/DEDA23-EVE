import pandas as pd
import matplotlib.pyplot as plt

# Read the cleaned data into a pandas DataFrame
data = pd.read_csv('cleaned_economy_indices_details4.csv')

# Convert 'history_date' column to datetime type
data['history_date'] = pd.to_datetime(data['history_date'])

# Group the data by 'history_date' and calculate the mean of 'Real Price Change'
grouped_data = data.groupby('history_date')['Real Price Change'].mean()

# Plot the real price changes over time
plt.plot(grouped_data.index, grouped_data.values)
plt.xlabel('Date')
plt.ylabel('Price Change')
plt.title('Inflation rate')
plt.xticks(rotation=45)
plt.show()
