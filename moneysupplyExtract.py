import pandas as pd

# Read the CSV file into a DataFrame
df = pd.read_csv('/Users/admin/Documents/GitHub/DEDA23-EVE/money_supply_onlytotal2.csv', sep=';')

# Convert the 'Date' column to datetime type
df['Date'] = pd.to_datetime(df['Date'])

# Extract the year and month from the 'Date' column
df['Year'] = df['Date'].dt.year
df['Month'] = df['Date'].dt.month

# Filter the DataFrame to keep only the rows with the first day of each month
df_filtered = df[df['Date'].dt.is_month_start]

# Extract the money supply values for the first day of each month
money_supply_vector = df_filtered['MoneySupply'].values

# Convert the money supply values to strings and join them with commas
money_supply_str = ', '.join([str(money) for money in money_supply_vector])

# Print the money supply vector with commas
print("Money Supply Vector:", money_supply_str)
