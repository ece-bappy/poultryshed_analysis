import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Read CSV file into a pandas DataFrame
df = pd.read_csv("final_data.csv")

# Convert 'Time' column to datetime format
df["Time"] = pd.to_datetime(df["Time"], format="%H:%M")

# Group by day and calculate hourly averages
grouped_df = (
    df.groupby(["Day", df["Time"].dt.hour])
    .agg({"Temperature": "mean", "Humidity": "mean", "Gas Level": "mean"})
    .reset_index()
)

# Get unique days
unique_days = grouped_df["Day"].unique()

# Assign random colors for each day
day_colors = {
    day: np.random.rand(
        3,
    )
    for day in unique_days
}

# Lists to store standard deviation and mean variance values
temp_std_dev = []
temp_mean_variance = []
humidity_std_dev = []
humidity_mean_variance = []
gas_std_dev = []
gas_mean_variance = []

# Plotting for Temperature
fig_temp, ax_temp = plt.subplots(figsize=(10, 6))

for day, day_df in grouped_df.groupby("Day"):
    color = day_colors[day]
    ax_temp.plot(
        day_df["Time"], day_df["Temperature"], label=f"Day {int(day)}", color=color
    )

    # Calculate standard deviation and mean variance for temperature
    temp_std_dev.append(day_df["Temperature"].std())
    temp_mean_variance.append(day_df["Temperature"].var())

ax_temp.set_xlabel("Hour of the Day")
ax_temp.set_ylabel("Temperature")
ax_temp.set_title("Hourly Average Temperature")
ax_temp.legend()
ax_temp.grid(True)
plt.xticks(range(24))
plt.tight_layout()

# Print standard deviation and mean variance for Temperature
print(f"Temperature Std Dev: {np.mean(temp_std_dev):.2f}")
print(f"Temperature Mean Variance: {np.mean(temp_mean_variance):.2f}")
print()

# Plotting for Humidity
fig_humidity, ax_humidity = plt.subplots(figsize=(10, 6))

for day, day_df in grouped_df.groupby("Day"):
    color = day_colors[day]
    ax_humidity.plot(
        day_df["Time"], day_df["Humidity"], label=f"Day {int(day)}", color=color
    )

    # Calculate standard deviation and mean variance for humidity
    humidity_std_dev.append(day_df["Humidity"].std())
    humidity_mean_variance.append(day_df["Humidity"].var())

ax_humidity.set_xlabel("Hour of the Day")
ax_humidity.set_ylabel("Humidity")
ax_humidity.set_title("Hourly Average Humidity")
ax_humidity.legend()
ax_humidity.grid(True)
plt.xticks(range(24))
plt.tight_layout()

# Print standard deviation and mean variance for Humidity
print(f"Humidity Std Dev: {np.mean(humidity_std_dev):.2f}")
print(f"Humidity Mean Variance: {np.mean(humidity_mean_variance):.2f}")
print()

# Plotting for Gas Level
fig_gas, ax_gas = plt.subplots(figsize=(10, 6))

for day, day_df in grouped_df.groupby("Day"):
    color = day_colors[day]
    ax_gas.plot(
        day_df["Time"], day_df["Gas Level"], label=f"Day {int(day)}", color=color
    )

    # Calculate standard deviation and mean variance for gas level
    gas_std_dev.append(day_df["Gas Level"].std())
    gas_mean_variance.append(day_df["Gas Level"].var())

ax_gas.set_xlabel("Hour of the Day")
ax_gas.set_ylabel("Gas Level")
ax_gas.set_title("Hourly Average Gas Level")
ax_gas.legend()
ax_gas.grid(True)
plt.xticks(range(24))
plt.tight_layout()

# Print standard deviation and mean variance for Gas Level
print(f"Gas Level Std Dev: {np.mean(gas_std_dev):.2f}")
print(f"Gas Level Mean Variance: {np.mean(gas_mean_variance):.2f}")
print()

# Show the plots
plt.show()
