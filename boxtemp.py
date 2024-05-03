import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Read CSV file into a pandas DataFrame
df = pd.read_csv("data2.csv")

# Create a box plot for Temperature without outliers
plt.figure(figsize=(8, 6))
sns.boxplot(x="Day", y="Temperature", data=df, showfliers=False, palette="Set2")
plt.title("Box Plot for Temperature Between Days (Without Outliers)")
plt.xlabel("Day")
plt.ylabel("Temperature")
plt.show()
