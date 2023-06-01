import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# Load data from CSV files
money_supply_data = pd.read_csv('/Users/admin/Documents/GitHub/DEDA23-EVE/money_supply_onlytotal2.csv', delimiter=';')
cpi_data = pd.read_csv('/Users/admin/Documents/GitHub/DEDA23-EVE/extracted_data/economy_indices_details.csv')

# Extract relevant columns from the data
money_supply_dates = pd.to_datetime(money_supply_data['Date'])
money_supply = money_supply_data['MoneySupply'].values
cpi_dates = pd.to_datetime(cpi_data['history_date'])
cpi_change = cpi_data['price_change'].values

# Filter money supply data for first day of each month
money_supply_first_day = money_supply[money_supply_dates.isin(cpi_dates)]

# Define parameters to test
inflation_coefficients = [0.01, 0.02, 0.03]  # Coefficients linking money growth to inflation
expected_inflations = [0.02, 0.03, 0.04]  # Initial expected inflation rates

# Initialize variables to store best correlation and corresponding parameters
best_correlation = -1
best_inflation_coefficient = None
best_expected_inflation = None
best_inflation_rate = None
best_expected_inflation_rate = None

# Define the number of time periods based on the smaller length of cpi_change or money_supply_first_day
time_periods = min(len(cpi_change), len(money_supply_first_day))

# Set initial money supply
initial_money_supply = money_supply_first_day[0]

# Iterate through parameter combinations
for inflation_coefficient in inflation_coefficients:
    for expected_inflation in expected_inflations:
        # Initialize arrays to store results
        inflation_rate = np.zeros(time_periods)
        expected_inflation_rate = np.zeros(time_periods)
        updated_money_supply = np.zeros(time_periods+1)

        # Set initial money supply
        updated_money_supply[0] = initial_money_supply

        # Simulate the Cagan model
        for t in range(1, time_periods+1):
            # Calculate current inflation rate based on CPI change
            current_inflation = cpi_change[t-1] / 100.0

            # Update expected inflation rate based on previous period's expectation
            expected_inflation_rate[t-1] = expected_inflation

            # Calculate new expected inflation rate based on current inflation and previous expectation
            expected_inflation = expected_inflation + 0.5 * (current_inflation - expected_inflation)

            # Calculate money growth based on the Cagan model equation
            money_growth = (1 + current_inflation) / (1 + expected_inflation) - 1

            # Update money supply by applying money growth
            updated_money_supply[t] = updated_money_supply[t-1] * (1 + money_growth)

            # Calculate actual inflation rate using the Cagan model equation
            inflation_rate[t-1] = (updated_money_supply[t] / updated_money_supply[t-1]) - 1

        # Calculate correlation between actual inflation and expected inflation
        correlation = np.corrcoef(inflation_rate, expected_inflation_rate)[0, 1]

        # Check if the current correlation is better than the previous best correlation
        if correlation > best_correlation:
            best_correlation = correlation
            best_inflation_coefficient = inflation_coefficient
            best_expected_inflation = expected_inflation
            best_inflation_rate = inflation_rate
            best_expected_inflation_rate = expected_inflation_rate

# Convert time_periods to corresponding dates
start_date = pd.to_datetime(cpi_dates.iloc[0])
dates = pd.date_range(start=start_date, periods=time_periods, freq='M')

# Plot the results for the best parameter combination
fig, ax = plt.subplots()
ax.plot(dates, best_inflation_rate, label='Actual Inflation')
ax.plot(dates, best_expected_inflation_rate, label='Expected Inflation')
ax.xaxis.set_major_locator(mdates.YearLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))
plt.xlabel('Time')
plt.ylabel('Inflation Rate')
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.title(f'Best Correlation: {best_correlation:.2f} | Inflation Coefficient: {best_inflation_coefficient} | Expected Inflation: {best_expected_inflation}')
plt.show()
