import pandas as pd
import random

# Read the CSV file
df = pd.read_csv('data1.csv')

# Define humidity ranges for different time intervals
humidity_ranges = {
    (0, 4): (62, 65),
    (5, 9): (61, 64),
    (10, 14): (62, 69),
    (15, 20): (63, 70),
    (21, 23): (62, 68)
}

# Generate random humidity values within defined ranges for each hour of each day
random_humidity_values = []
for _, row in df.iterrows():
    hour_range = None
    for start, end in humidity_ranges.keys():
        if start <= row['Time'] <= end:
            hour_range = humidity_ranges[(start, end)]
            break
    random_humidity_values.append(random.uniform(hour_range[0], hour_range[1]))

# Replace existing values in the "Humidity" column with trend-based random values
df['Humidity'] = random_humidity_values

# Save the modified DataFrame to a new CSV file
df.to_csv('data2.csv', index=False)

print("Humidity values replaced with trend-based random values. New CSV file saved as 'randomized_gas_and_humidity_levels.csv'")
