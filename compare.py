import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV files for controlled and traditional environments
df_controlled = pd.read_csv('data2.csv')
df_traditional = pd.read_csv('data4.csv')

# Convert 'Date' column to datetime format
df_controlled['Date'] = pd.to_datetime(df_controlled['Date'])
df_traditional['Date'] = pd.to_datetime(df_traditional['Date'])

# Create a figure with subplots
fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(14, 6))

# Plot temperature for controlled environment
axes[0].plot(df_controlled['Date'], df_controlled['Temperature'], label='Controlled Environment', color='blue')
axes[0].set_title('Temperature - Controlled Environment')
axes[0].set_xlabel('Date')
axes[0].set_ylabel('Temperature (°C)')
axes[0].legend()
axes[0].grid(True)

# Plot temperature for traditional environment
axes[1].plot(df_traditional['Date'], df_traditional['Temperature'], label='Traditional Environment', color='red')
axes[1].set_title('Temperature - Traditional Environment')
axes[1].set_xlabel('Date')
axes[1].set_ylabel('Temperature (°C)')
axes[1].legend()
axes[1].grid(True)

# Adjust layout and display the plot
plt.tight_layout()
plt.show()
