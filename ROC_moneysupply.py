import pandas as pd

data = pd.read_csv('money_supply_onlytotal2.csv', delimiter=';')
data['Date'] = pd.to_datetime(data['Date'])
data.set_index('Date', inplace=True)

monthly_data = data.resample('M').last()
rate_of_change = monthly_data.pct_change()

rate_of_change_vector = rate_of_change['MoneySupply'].dropna().tolist()
rate_of_change_str = ', '.join(map(str, rate_of_change_vector))
print(rate_of_change_str)
