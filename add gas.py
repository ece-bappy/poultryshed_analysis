import pandas as pd
import random

# Read the CSV file
df = pd.read_csv('sorted_file.csv')

# Generate random values between 10 and 26 to replace existing values
random_values = [random.uniform(10, 26) for _ in range(len(df))]

# Replace existing values in the "Gas Level" column with random values
df['Gas Level'] = random_values

# Save the modified DataFrame to a new CSV file
df.to_csv('randomized_gas_levels.csv', index=False)

print("Existing values in 'Gas Level' column replaced with random values. New CSV file saved as 'randomized_gas_levels.csv'")
