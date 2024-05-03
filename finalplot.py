import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file
df = pd.read_csv('data2.csv')

# Convert 'Date' column to datetime format
df['Date'] = pd.to_datetime(df['Date'])

# Group by 'Day'
grouped = df.groupby('Day')

# Create a single figure
plt.figure(figsize=(10, 6))

# Plot each group
for day, group in grouped:
    plt.plot(group['Time'], group['Temperature'], label=f'Day {day} - Temperature')
  # plt.plot(group['Time'], group['Humidity'], label=f'Day {day} - Humidity')
  # plt.plot(group['Time'], group['Gas Level'], label=f'Day {day} - Gas Level')

plt.title('Temperature, Humidity, and Gas Level vs. Time')
plt.xlabel('Time')
plt.ylabel('Value')
plt.legend()
plt.grid(True)
plt.xticks(range(0, 24))
plt.tight_layout()
plt.show()
