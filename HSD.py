import pandas as pd
from statsmodels.stats.multicomp import pairwise_tukeyhsd

# Read the CSV file containing the final data
df = pd.read_csv('data2.csv')

# Perform Tukey's HSD test for Temperature
tukey_temperature = pairwise_tukeyhsd(df['Temperature'], df['Day'])
print("Tukey's HSD Test Results for Temperature:")
print(tukey_temperature)

# Perform Tukey's HSD test for Humidity
tukey_humidity = pairwise_tukeyhsd(df['Humidity'], df['Day'])
print("\nTukey's HSD Test Results for Humidity:")
print(tukey_humidity)

# Perform Tukey's HSD test for Gas Level
tukey_gas_level = pairwise_tukeyhsd(df['Gas Level'], df['Day'])
print("\nTukey's HSD Test Results for Gas Level:")
print(tukey_gas_level)
