import pandas as pd

# Read the CSV file
input_file = "12decNight.csv"
df = pd.read_csv(input_file, header=None)

# Add timestamps
minutes_interval = 1  # Change this to the desired interval
timestamps = pd.date_range(start="00:00", periods=len(df), freq=f"{minutes_interval}T")
timestamps = timestamps.strftime("%H:%M")

df.insert(0, "Timestamp", timestamps)

# Save the updated data to a new CSV file
output_file = "12dec.csv"
df.to_csv(output_file, header=False, index=False)

print(f"Timestamps added and saved to {output_file}")
