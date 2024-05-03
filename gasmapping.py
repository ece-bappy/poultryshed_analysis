import pandas as pd
import random

# Read the CSV file
df = pd.read_csv('data1.csv')

# Define gas level ranges for different time intervals
ranges = {
    (0, 4): (18, 20),
    (5, 9): (20, 21),
    (10, 14): (21, 24),
    (15, 20): (20, 23),
    (21, 23): (17, 20)
}

# Generate random values within defined ranges for each hour of each day
random_values = []
for _, row in df.iterrows():
    hour_range = None
    for start, end in ranges.keys():
        if start <= row['Time'] <= end:
            hour_range = ranges[(start, end)]
            break
    random_values.append(random.uniform(hour_range[0], hour_range[1]))

# Replace existing values in the "Gas Level" column with random values
df['Gas Level'] = random_values

# Save the modified DataFrame to a new CSV file
df.to_csv('data2.csv', index=False)

print("Gas level values replaced with trend-based random values. New CSV file saved as 'trend_randomized_gas_levels.csv'")
