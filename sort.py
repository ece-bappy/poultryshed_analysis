import pandas as pd

# Read the CSV file
df = pd.read_csv('modified_file.csv')

# Sort the DataFrame by 'Day' and 'Time' columns
df['Time'] = df['Time'].astype(int)  # Convert 'Time' column to integer for sorting
df_sorted = df.sort_values(by=['Day', 'Time'])

# Reset the 'Time' column to start from 0 and end at 23 for all days
df_sorted['Time'] = df_sorted.groupby('Day').cumcount()

# Save the modified DataFrame to a new CSV file
df_sorted.to_csv('sorted_file.csv', index=False)

print("Sorting complete. New CSV file saved as 'sorted_file.csv'")
