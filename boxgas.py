import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Read CSV file into a pandas DataFrame
df = pd.read_csv("data2.csv")

# Create a box plot for Gas Level without outliers
plt.figure(figsize=(8, 6))
sns.boxplot(x="Day", y="Gas Level", data=df, showfliers=False, palette="Set3")
plt.title("Box Plot for Gas Level Between Days (Without Outliers)")
plt.xlabel("Day")
plt.ylabel("Gas Level")
plt.show()
