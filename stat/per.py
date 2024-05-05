import pandas as pd

# Load data from CSV files
inside_data = pd.read_csv("inside.csv")
outside_data = pd.read_csv("outside.csv")

# Calculate mean weights
inside_mean = inside_data['Weight'].mean()
outside_mean = outside_data['Weight'].mean()

# Calculate percentage increase
percentage_increase = ((inside_mean - outside_mean) / outside_mean) * 100

print("Percentage increase in growth inside compared to outside: {:.2f}%".format(percentage_increase))
