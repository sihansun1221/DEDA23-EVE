import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

plt.rcParams["figure.figsize"] = (11, 5)  # set default figure size

# Load data from CSV file
data = pd.read_csv('/Users/admin/Documents/GitHub/DEDA23-EVE/money_supply_onlytotal2.csv', sep=';')

# Extract relevant column from the data
money_supply = data['MoneySupply']

# Define the parameters
p_1 = 0.5
p_2 = 0.3
a = 0.1

# Initialize the arrays for storing the simulated values
T = len(money_supply)
m_t = np.zeros(T)
p_t = np.zeros(T)

# Set the initial values
m_t[0] = money_supply[0]
p_t[0] = np.log(m_t[0])

# Simulate the paths
for t in range(1, T):
    m_t[t] = a + p_1 * m_t[t-1] + p_2 * m_t[t-2]
    p_t[t] = np.log(m_t[t])

# Plotting the simulated paths
plt.plot(range(T), m_t, label='$m_t$')
plt.plot(range(T), p_t, label='$p_t$')
plt.xlabel('t')
plt.ylabel('Value')
plt.title('Simulated Paths of $m_t$ and $p_t$')
plt.legend()
plt.show()

print()