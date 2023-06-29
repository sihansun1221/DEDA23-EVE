import pandas as pd
import numpy as np
import statsmodels.api as sm

# Read the CPI data from the file
cpi_data = pd.read_csv('filtered_data_cpi.csv', delimiter=';')

# Calculate the rate of inflation (Πₜ)
cpi_data['rate_of_inflation'] = cpi_data['price_change'].pct_change()

# Read the money supply data from the file
money_supply_data = pd.read_csv('filtered_data_ms.csv', delimiter=';')

# Calculate the rate of growth of the money supply (Mₜ)
money_supply_data['rate_of_growth'] = money_supply_data['MoneySupply'].pct_change()

# Combine the CPI and money supply data based on the date
combined_data = pd.merge(cpi_data, money_supply_data, on='Date')

# Calculate the differences and squared differences
combined_data['D_rate_of_inflation'] = combined_data['rate_of_inflation'].diff()
combined_data['D2_rate_of_inflation'] = combined_data['D_rate_of_inflation'].diff()
combined_data['DMoneySupply'] = combined_data['MoneySupply'].diff()
combined_data['D2MoneySupply'] = combined_data['DMoneySupply'].diff()
combined_data['MoneySupply_minus_inflation'] = combined_data['MoneySupply'] - combined_data['rate_of_inflation']
combined_data['D_money_supply_minus_inflation'] = combined_data['MoneySupply_minus_inflation'].diff()

# Select the relevant columns for autocorrelation analysis
autocorr_data = combined_data[['rate_of_inflation', 'D_rate_of_inflation', 'D2_rate_of_inflation',
                               'MoneySupply', 'DMoneySupply', 'D2MoneySupply',
                               'MoneySupply_minus_inflation', 'D_money_supply_minus_inflation']]

# Calculate the autocorrelation for each variable and time lag
autocorrelation_table = pd.DataFrame()
lags = 12

for column in autocorr_data:
    autocorrs = [autocorr_data[column].autocorr(lag=lag) for lag in range(1, lags + 1)]
    autocorrelation_table[column] = autocorrs

# Add time lags to the table
autocorrelation_table.insert(0, 'Time Lag', range(1, lags + 1))

# Save the autocorrelation table as a CSV file
autocorrelation_table.to_csv('autocorrelation_table.csv', index=False)
