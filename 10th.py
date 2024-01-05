import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file into a DataFrame
df = pd.read_csv("output.csv")

# Convert the 'Time' column to datetime format
df["Time"] = pd.to_datetime(df["Time"], format="%H:%M")

# Extract day and hour information
df["Day"] = df["Time"].dt.day
df["Hour"] = df["Time"].dt.hour

# Calculate hourly averages for each variable
hourly_avg = df.groupby(["Day", "Hour"]).mean().reset_index()

# Set the figure size
plt.figure(figsize=(15, 8))

# Plot Temperature
plt.plot(hourly_avg["Hour"], hourly_avg["Temperature"], label="Temperature", marker="o")

# Plot Humidity
plt.plot(hourly_avg["Hour"], hourly_avg["Humidity"], label="Humidity", marker="o")

# Plot Gas Level
plt.plot(hourly_avg["Hour"], hourly_avg["Gas Level"], label="Gas Level", marker="o")

# Customize the plot
plt.title("Hourly Averages: Temperature, Humidity, and Gas Level")
plt.xlabel("Hour of the Day")
plt.ylabel("Average Values")
plt.legend()
plt.grid(True)
plt.xticks(range(24))  # Assuming 24 hours in a day

# Show the plot
plt.tight_layout()
plt.show()
