import pandas as pd

# Read the CSV file
df = pd.read_csv('data2.csv')

# Calculate standard deviation and mean variance for each parameter in each hour
hourly_stats = df.groupby('Time').agg({'Temperature': ['mean', 'std', 'var'],
                                       'Humidity': ['mean', 'std', 'var'],
                                       'Gas Level': ['mean', 'std', 'var']})

# Rename the columns
hourly_stats.columns = ['Temp_Mean', 'Temp_Deviation', 'Temp_Variance',
                        'Humid_Mean', 'Humid_Deviation', 'Humid_Variance',
                        'Gas_Mean', 'Gas_Deviation', 'Gas_Variance']
hourly_stats = hourly_stats.round(2)
# Save the data to a CSV file with custom column names
hourly_stats.to_csv('hourly_statistics.csv')

print("Hourly statistics saved to 'hourly_statistics.csv'")
