import pandas as pd

# Read CSV file into a pandas DataFrame
df = pd.read_csv("final_data.csv")

# Convert 'Time' column to datetime format
df["Time"] = pd.to_datetime(df["Time"], format="%H:%M")

# Define the starting date
start_date = pd.to_datetime("2023-12-12")

# Add 'Date' column with automatically incremented dates
df["Date"] = start_date + pd.to_timedelta(df["Day"] - 1, unit="D")

# Group by day and hour and calculate hourly averages, rounding to 2 decimal places
hourly_averages = (
    df.groupby(["Day", "Date", df["Time"].dt.hour])
    .agg(
        {
            "Temperature": lambda x: round(x.mean(), 2),
            "Humidity": lambda x: round(x.mean(), 2),
            "Gas Level": lambda x: round(x.mean(), 2),
        }
    )
    .reset_index()
)

# Format the 'Date' column to remove the time part
hourly_averages["Date"] = hourly_averages["Date"].dt.strftime("%m/%d/%Y")

# Save the hourly averages to a new Excel file
hourly_averages.to_excel("hourly_averages_with_date.xlsx", index=False)
