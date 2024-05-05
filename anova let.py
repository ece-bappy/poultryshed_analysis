import pandas as pd
from scipy.stats import f_oneway

# Read data from data2.csv and data3.csv
data2 = pd.read_csv('data2.csv')
data3 = pd.read_csv('data3.csv')

# Combine the data
data2['Environment'] = 'Controlled'
data3['Environment'] = 'Traditional'
combined_data = pd.concat([data2, data3])

# Convert 'Time' column to string
combined_data['Time'] = combined_data['Time'].astype(str)

# Perform ANOVA analysis for each variable (Temperature, Humidity, Gas Level)
variables = ['Temperature', 'Humidity', 'Gas Level']
for variable in variables:
    # Group by hour for each day
    groups = []
    for day in combined_data['Day'].unique():
        groups.append(combined_data.loc[combined_data['Day'] == day, variable])

    # Perform ANOVA
    f_statistic, p_value = f_oneway(*groups)
    
    # Print ANOVA results
    print(f'ANOVA Test Results for {variable}:')
    print(f'F-Statistic: {f_statistic}')
    print(f'P-Value: {p_value}')
    print()
