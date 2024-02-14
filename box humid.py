import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Read CSV file into a pandas DataFrame
df = pd.read_csv("final_data.csv")

# Convert 'Time' column to datetime format
df["Time"] = pd.to_datetime(df["Time"], format="%H:%M")

# Create a box plot for Humidity without outliers
plt.figure(figsize=(8, 6))
sns.boxplot(x="Day", y="Humidity", data=df, showfliers=False)
plt.title("Box Plot for Humidity Between Days (Without Outliers)")
plt.xlabel("Day")
plt.ylabel("Humidity")
plt.pcolor("red")
plt.show()
