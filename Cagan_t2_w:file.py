import matplotlib.pyplot as plt
import pandas as pd

plt.rcParams["figure.figsize"] = (11, 5)  # set default figure size

# Load data from CSV file
data = pd.read_csv('/Users/admin/Documents/GitHub/DEDA23-EVE/money_supply_onlytotal2.csv', sep=';')

# Extract relevant columns from the data
date = pd.to_datetime(data['Date'])
money_supply = data['MoneySupply']

# Plotting the data
plt.plot(date, money_supply, label='Money Supply')
plt.xlabel('Date')
plt.ylabel('Money Supply')
plt.title('Money Supply over Time')
plt.legend()
plt.show()
