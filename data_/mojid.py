import pandas as pd
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
import seaborn as sns

# Step 1: Read the data from the CSV file
data = pd.read_csv('data_/data.csv')

# Step 2: Calculate basic statistics
controlled_mean = data['Controlled'].mean()
traditional_mean = data['Traditional'].mean()
controlled_std = data['Controlled'].std()
traditional_std = data['Traditional'].std()

# Step 3: Perform a t-test
t_stat, p_value = stats.ttest_ind(data['Controlled'], data['Traditional'])

# Step 4: Calculate the percentage increase in weight
percentage_increase = ((controlled_mean - traditional_mean) / traditional_mean) * 100

# Step 5: Print the results
print(f"Controlled Mean: {controlled_mean}")
print(f"Traditional Mean: {traditional_mean}")
print(f"Controlled Standard Deviation: {controlled_std}")
print(f"Traditional Standard Deviation: {traditional_std}")
print(f"T-statistic: {t_stat}")
print(f"P-value: {p_value}")
print(f"Percentage Increase: {percentage_increase:.2f}%")

# Step 6: Visualize the data
# Plotting the weight comparison
plt.figure(figsize=(10, 6))
sns.boxplot(data=data, palette="Set2")
plt.title('Weight Comparison of Chickens')
plt.ylabel('Weight')
plt.xlabel('Group')
plt.show()

# Plotting the percentage increase
labels = ['Traditional', 'Controlled']
weights = [traditional_mean, controlled_mean]

plt.figure(figsize=(10, 6))
sns.barplot(x=labels, y=weights, palette="Set2")
plt.title('Average Weight of Chickens')
plt.ylabel('Weight')
plt.show()
