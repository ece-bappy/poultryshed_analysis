import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data from CSV files
inside_data = pd.read_csv("inside.csv")
outside_data = pd.read_csv("outside.csv")

# Statistical analysis
inside_mean = inside_data['Weight'].mean()
outside_mean = outside_data['Weight'].mean()

inside_std = inside_data['Weight'].std()
outside_std = outside_data['Weight'].std()

inside_count = inside_data['Weight'].count()
outside_count = outside_data['Weight'].count()

# Plotting
plt.figure(figsize=(10, 6))

# Histograms
plt.subplot(2, 1, 1)
sns.histplot(inside_data['Weight'], kde=True, color='blue', label='Controlled')
sns.histplot(outside_data['Weight'], kde=True, color='orange', label='Traditional')
plt.xlabel('Weight(kg)')
plt.ylabel('Frequency')
plt.title('Weight Distribution')
plt.legend()

# Boxplots
plt.subplot(2, 1, 2)
sns.boxplot(data=[inside_data['Weight'], outside_data['Weight']])
plt.xticks([0, 1], ['Traditional', 'Traditional'])
plt.ylabel('Weight (kg)')
plt.title('Weight Distribution')

# Save plots as PNG files
plt.tight_layout()
plt.savefig('weight_distribution.png')
plt.close()

# Summary statistics
summary_stats = pd.DataFrame({
    'Statistic': ['Mean', 'Standard Deviation', 'Count'],
    'Inside': [inside_mean, inside_std, inside_count],
    'Outside': [outside_mean, outside_std, outside_count]
})
summary_stats.set_index('Statistic', inplace=True)

# Save summary statistics to CSV
summary_stats.to_csv('summary_statistics.csv')

print("Summary Statistics:")
print(summary_stats)
print("Plots saved as weight_distribution.png")
