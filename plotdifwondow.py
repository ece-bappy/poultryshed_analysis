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

# Plotting for Temperature
fig_temp, ax_temp = plt.subplots(figsize=(10, 6))

for day, day_df in grouped_df.groupby("Day"):
    color = day_colors[day]
    ax_temp.plot(
        day_df["Time"], day_df["Temperature"], label=f"Day {int(day)}", color=color
    )

ax_temp.set_xlabel("Hour of the Day")
ax_temp.set_ylabel("Temperature")
ax_temp.set_title("Hourly Average Temperature")
ax_temp.legend()
ax_temp.grid(True)
plt.xticks(range(24))
plt.tight_layout()

# Plotting for Humidity
fig_humidity, ax_humidity = plt.subplots(figsize=(10, 6))

for day, day_df in grouped_df.groupby("Day"):
    color = day_colors[day]
    ax_humidity.plot(
        day_df["Time"], day_df["Humidity"], label=f"Day {int(day)}", color=color
    )

ax_humidity.set_xlabel("Hour of the Day")
ax_humidity.set_ylabel("Humidity")
ax_humidity.set_title("Hourly Average Humidity")
ax_humidity.legend()
ax_humidity.grid(True)
plt.xticks(range(24))
plt.tight_layout()

# Plotting for Gas Level
fig_gas, ax_gas = plt.subplots(figsize=(10, 6))

for day, day_df in grouped_df.groupby("Day"):
    color = day_colors[day]
    ax_gas.plot(
        day_df["Time"], day_df["Gas Level"], label=f"Day {int(day)}", color=color
    )

ax_gas.set_xlabel("Hour of the Day")
ax_gas.set_ylabel("Gas Level")
ax_gas.set_title("Hourly Average Gas Level")
ax_gas.legend()
ax_gas.grid(True)
plt.xticks(range(24))
plt.tight_layout()

# Show the plots
plt.show()
