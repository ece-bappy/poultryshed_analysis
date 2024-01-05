import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Read CSV file into a pandas DataFrame
df = pd.read_csv("output_file.csv")

# Convert 'Time' column to datetime format
df["Time"] = pd.to_datetime(df["Time"], format="%H:%M")

# Group by day and calculate hourly averages
grouped_df = (
    df.groupby(["Day", df["Time"].dt.hour])
    .agg({"Temperature": "mean", "Humidity": "mean", "Gas Level": "mean"})
    .reset_index()
)

# Plotting
fig, ax = plt.subplots(figsize=(10, 6))

# Get unique days
unique_days = grouped_df["Day"].unique()

# Assign random colors for each day
day_colors = {
    day: np.random.rand(
        3,
    )
    for day in unique_days
}

for day, day_df in grouped_df.groupby("Day"):
    color = day_colors[day]

    ax.plot(
        day_df["Time"],
        day_df["Temperature"],
        label=f"Temperature - Day {int(day)}",
        color=color,
    )
    ax.plot(
        day_df["Time"],
        day_df["Humidity"],
        label=f"Humidity - Day {int(day)}",
        linestyle="dashed",
        color=color,
    )
    ax.plot(
        day_df["Time"],
        day_df["Gas Level"],
        label=f"Gas Level - Day {int(day)}",
        linestyle="dotted",
        color=color,
    )

# Customize the plot
ax.set_xlabel("Hour of the Day")
ax.set_ylabel("Average Values")
ax.set_title("Hourly Averages of Temperature, Humidity, and Gas Level")
ax.legend()
plt.xticks(range(24))  # X-axis from 0 to 23 hours
plt.grid(True)
plt.tight_layout()

# Show the plot
plt.show()
