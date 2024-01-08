import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Read CSV file into a pandas DataFrame
df = pd.read_csv("final_data.csv")

# Convert 'Time' column to datetime format
df["Time"] = pd.to_datetime(df["Time"], format="%H:%M")

# Group by day and extract data for box plots
grouped_df = (
    df.groupby("Day")
    .agg({"Temperature": "mean", "Humidity": "mean", "Gas Level": "mean"})
    .reset_index()
)

# Create individual box plots for each variable
for variable in ["Temperature"]:
    plt.figure(figsize=(8, 6))
    sns.boxplot(x="Day", y=variable, data=df)
    plt.title(f"Box Plot for {variable} Between Days")
    plt.xlabel("Day")
    plt.ylabel(variable)

# Show all plots at once
plt.show()
