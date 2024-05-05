import pandas as pd
from scipy.stats import f_oneway
from statsmodels.stats.multicomp import pairwise_tukeyhsd

# Read data from data2.csv and data3.csv
data2 = pd.read_csv('data2.csv')
data3 = pd.read_csv('data3.csv')

# Combine the data
data2['Environment'] = 'Controlled'
data3['Environment'] = 'Traditional'
combined_data = pd.concat([data2, data3])

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
    
    # Perform HSD test
    tukey_results = pairwise_tukeyhsd(combined_data[variable], combined_data['Time'], alpha=0.05)
    
    # Print HSD test results
    print(f'HSD Test Results for {variable}:')
    print(tukey_results)
    print()
