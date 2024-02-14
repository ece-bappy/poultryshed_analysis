import pandas as pd

# Read CSV file into a pandas DataFrame
df = pd.read_csv("final_data.csv")

# Convert 'Time' column to datetime format
df["Time"] = pd.to_datetime(df["Time"], format="%H:%M")

# Group by day and hour and calculate hourly averages
hourly_averages = (
    df.groupby(["Day", df["Time"].dt.hour])
    .agg({"Temperature": "mean", "Humidity": "mean", "Gas Level": "mean"})
    .reset_index()
)

# Save the hourly averages to a new CSV file
hourly_averages.to_csv("hourly_averages.csv", index=False)
