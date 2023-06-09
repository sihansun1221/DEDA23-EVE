import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# INFLATION RATE CALCULATION
# Create a DataFrame from the provided data
data = {
    'history_date': [
        '2017-01-01', '2017-02-01', '2017-03-01', '2017-04-01', '2017-05-01', '2017-06-01', '2017-07-01', '2017-08-01',
        '2017-09-01', '2017-10-01', '2017-11-01', '2017-12-01', '2018-01-01', '2018-02-01', '2018-03-01', '2018-04-01',
        '2018-05-01', '2018-06-01', '2018-07-01', '2018-08-01', '2018-09-01', '2018-10-01', '2018-11-01', '2018-12-01',
        '2019-01-01', '2019-02-01', '2019-03-01', '2019-04-01', '2019-05-01', '2019-06-01', '2019-07-01', '2019-08-01',
        '2019-09-01', '2019-10-01', '2019-11-01', '2019-12-01', '2020-01-01', '2020-02-01', '2020-03-01', '2020-04-01',
        '2020-05-01', '2020-06-01', '2020-07-01', '2020-08-01', '2020-09-01', '2020-10-01', '2020-11-01', '2020-12-01',
        '2021-01-01', '2021-02-01', '2021-03-01', '2021-04-01', '2021-05-01', '2021-06-01', '2021-07-01', '2021-08-01',
        '2021-09-01', '2021-10-01', '2021-11-01', '2021-12-01', '2022-01-01', '2022-02-01', '2022-03-01', '2022-04-01',
        '2022-05-01', '2022-06-01', '2022-07-01', '2022-08-01', '2022-09-01', '2022-10-01', '2022-11-01', '2022-12-01',
        '2023-01-01', '2023-02-01', '2023-03-01', '2023-04-01'
    ],
    'Real Price Change': [
        0.0003978082270312437, 0.00042140546593938784, -0.000192557023030297, -0.00010377523884848786,
        0.00042824097078787883, 0.0008632039426060607, 0.0011748775262424092, 0.0007480379379999938,
        0.00022082990790625313, 0.0006990297174062438, -0.00012667258080645164, 0.00046950018419354835,
        0.0006549674145161226, -0.00019139051287095805, 8.445702490321935e-05, 0.0005574195048387031,
        0.00016947502513888613, 0.0005699075468888888, -0.0008322634387222167, 0.00031567094538888604,
        -0.00030084955908332776, -0.00029197754452776664, 0.00012657045750000278, 0.0006596340189444444,
        -1.4166454166694488e-06, 0.00037475577630554724, 0.0002963190056111166, 0.0009105286677222195,
        0.0004575681319166528, 0.0003853252599722139, -0.00014532610744444165, -0.0008479696124722223,
        -0.0007357844674444333, 0.00010071161047222222, 0.00015685651555555553, 0.0007290409934166528,
        0.00014927521972221388, -0.00025516406758334165, -2.8212306222222198e-05, 0.00014526232358333334,
        -0.0005514136781944417, -0.001070263366416661, 3.067153052778335e-05, -0.0006965095472499916,
        0.0005113148525555528, 0.001047463785138872, -0.0002465411578333305, -0.00010040785083333332,
        0.0003843196623611111, 0.0001425872531388861, 0.0002878988422499944, 0.0018224112747222167,
        0.0006574193894444417, -0.0004159219262222222, 9.752134119444445e-05, 0.000858724663916675,
        0.00037902069824998885, 0.00017379505066666392, -0.0001688915149166639, 6.1114581388888715e-06,
        0.00013000553222221664, -0.00035100582600000835, -0.00054626386919445, -8.274465397222501e-05,
        0.00019241326669444168, 0.000638221380277775, 0.00010895874511110835, 0.00048537870041666115,
        0.0004873515779722194, 0.0007899978405555445, 0.0006670874948333194, 0.001097677325194436,
        0.0003413531940833277, -1.3236402638883308e-05, 0.0005076391490277695, -0.0002489058273611
    ]
}

df = pd.DataFrame(data)

# Convert 'history_date' column to datetime type
df['history_date'] = pd.to_datetime(df['history_date'])

# Sort the DataFrame by 'history_date'
df = df.sort_values('history_date')

# Calculate the cumulative sum of price changes
df['Price'] = (1 + df['Real Price Change']).cumprod()

# Print the inflation rate as a vector
inflation_rate = df['Real Price Change'].values
inflation_rate_str = ', '.join([str(rate) for rate in inflation_rate])
### print("Inflation Rate:", inflation_rate_str)

# MONEY SUPPLY
data = pd.read_csv('money_supply_onlytotal2.csv', delimiter=';')
data['Date'] = pd.to_datetime(data['Date'])
data.set_index('Date', inplace=True)

monthly_data = data.resample('M').last()
rate_of_change = monthly_data.pct_change()

rate_of_change_vector = rate_of_change['MoneySupply'].dropna().tolist()

# Truncate or pad the inflation_rate array to match the length of rate_of_change_vector
inflation_rate_truncated = inflation_rate[:len(rate_of_change_vector)]

def plot_inflation_vs_money_supply(inflation_rate, money_supply):
    months = range(len(inflation_rate))

    fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True)

    ax1.set_ylabel('Inflation Rate')
    ax1.plot(months, inflation_rate, color='red')

    ax2.set_ylabel('Money Supply')
    ax2.plot(months, money_supply, color='blue')

    fig.suptitle('Inflation Rate vs Money Supply')
    plt.xlabel('Month')

    plt.show()


plot_inflation_vs_money_supply(inflation_rate_truncated, rate_of_change_vector)

# Compute the correlation coefficient
correlation = np.corrcoef(rate_of_change_vector, inflation_rate_truncated)[0, 1]
print('Correlation coefficient:', correlation)
