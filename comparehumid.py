import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV files for controlled and traditional environments
df_controlled = pd.read_csv('data2.csv')
df_traditional = pd.read_csv('data4.csv')

# Convert 'Date' column to datetime format
df_controlled['Date'] = pd.to_datetime(df_controlled['Date'])
df_traditional['Date'] = pd.to_datetime(df_traditional['Date'])

# Group by 'Day' for both environments
grouped_controlled = df_controlled.groupby('Day')
grouped_traditional = df_traditional.groupby('Day')

# Create a single figure
plt.figure(figsize=(10, 6))

# Plot humidity for controlled environment
for day, group in grouped_controlled:
    plt.plot(group['Time'], group['Humidity'], label=f'Day {day} - Controlled Environment', color='red')

# Plot humidity for traditional environment
for day, group in grouped_traditional:
    plt.plot(group['Time'], group['Humidity'], label=f'Day {day} - Traditional Environment', color='blue')

plt.title('Humidity Comparison between Controlled(Red) and Traditional Environments(Blue)')
plt.xlabel('Time')
plt.ylabel('Humidity')
plt.grid(True)
plt.xticks(range(0, 24))
plt.tight_layout()
plt.show()
