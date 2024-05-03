import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Read CSV file into a pandas DataFrame
df = pd.read_csv("data2.csv")

# Create a box plot for Humidity without outliers
plt.figure(figsize=(8, 6))
sns.boxplot(x="Day", y="Humidity", data=df, showfliers=False, palette="Set1")
plt.title("Box Plot for Humidity Between Days (Without Outliers)")
plt.xlabel("Day")
plt.ylabel("Humidity")
plt.show()
