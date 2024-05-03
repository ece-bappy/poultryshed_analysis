import pandas as pd

# Read the CSV file
df = pd.read_csv('hourly_averages_with_date.csv')

# Define a dictionary to map old values to new values
time_mapping = {0: 16, 1: 17, 2: 18, 3: 19, 4: 20, 5: 21, 6: 22, 7: 23,
                8: 0, 9: 1, 10: 2, 11: 3, 12: 4, 13: 5, 14: 6, 15: 7,
                16: 8, 17: 9, 18: 10, 19: 11, 20: 12, 21: 13, 22: 14, 23: 15}

# Replace values in the 'Time' column using the mapping
df['Time'] = df['Time'].map(time_mapping)

# Save the modified DataFrame to a new CSV file
df.to_csv('modified_file.csv', index=False)

print("Modification complete. New CSV file saved as 'modified_file.csv'")
