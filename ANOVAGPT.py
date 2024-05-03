import pandas as pd
from scipy.stats import f_oneway

# Read the CSV file containing the final data
df = pd.read_csv('data2.csv')

# Group data by 'Day' and extract values for each variable for each day
grouped_data = {
    'Temperature': [group['Temperature'].values for _, group in df.groupby('Day')],
    'Humidity': [group['Humidity'].values for _, group in df.groupby('Day')],
    'Gas Level': [group['Gas Level'].values for _, group in df.groupby('Day')]
}

# Perform ANOVA test for each variable
for variable, data in grouped_data.items():
    f_statistic, p_value = f_oneway(*data)
    print(f"ANOVA Test Results for {variable}:")
    print("F-Statistic:", f_statistic)
    print("P-Value:", p_value)
    print()
