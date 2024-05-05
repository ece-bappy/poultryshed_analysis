import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

# Load the CSV files
inside_data = pd.read_csv("inside.csv")
outside_data = pd.read_csv("outside.csv")

# Calculate descriptive statistics
inside_stats = inside_data.describe()
outside_stats = outside_data.describe()

# Perform t-test
t_stat, p_value = stats.ttest_ind(inside_data['Weight'], outside_data['Weight'])

# Plot histograms
plt.figure(figsize=(10, 6))
sns.histplot(inside_data['Weight'], color='blue', kde=True, label='Inside')
sns.histplot(outside_data['Weight'], color='red', kde=True, label='Outside')
plt.xlabel('Weight')
plt.ylabel('Frequency')
plt.title('Distribution of Chicken Weights')
plt.legend()
plt.savefig('histogram.png')
plt.close()

# Plot boxplots
plt.figure(figsize=(10, 6))
sns.boxplot(data=[inside_data['Weight'], outside_data['Weight']])
plt.xlabel('Location')
plt.ylabel('Weight')
plt.title('Boxplot of Chicken Weights')
plt.xticks([0, 1], ['Inside', 'Outside'])
plt.savefig('boxplot.png')
plt.close()


# Print descriptive statistics
print("Inside Statistics:")
print(inside_stats)
print("\nOutside Statistics:")
print(outside_stats)

# Print t-test results
print("\nT-test results:")
print(f"T-statistic: {t_stat}")
print(f"P-value: {p_value}")

# Save descriptive statistics to CSV
inside_stats.to_csv('inside_stats.csv')
outside_stats.to_csv('outside_stats.csv')
