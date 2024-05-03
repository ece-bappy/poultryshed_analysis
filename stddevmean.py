import csv
import matplotlib.pyplot as plt

# Open the CSV file
with open('stddev.csv', 'r') as file:
    reader = csv.DictReader(file)
    data = list(reader)

# Create dictionaries to store the data for each parameter
std_dev_data = {'Temperature': [], 'Humidity': [], 'Gas Level': []}
variance_data = {'Temperature': [], 'Humidity': [], 'Gas Level': []}

# Populate the data dictionaries
for row in data:
    parameter = row['Parameter']
    std_dev_data[parameter].append(float(row['Standard Deviation']))
    variance_data[parameter].append(float(row['Variance']))

# Create a list of hours
hours = list(range(24))

# Plot the standard deviation graph
plt.figure(figsize=(12, 6))
plt.title('Standard Deviation')
plt.xlabel('Hour')
plt.ylabel('Standard Deviation')
for parameter, values in std_dev_data.items():
    plt.plot(hours, values, label=parameter)
plt.legend()
plt.xticks(hours)
plt.savefig('standard_deviation.png', dpi=300, bbox_inches='tight')

# Plot the variance graph
plt.figure(figsize=(12, 6))
plt.title('Variance')
plt.xlabel('Hour')
plt.ylabel('Variance')
for parameter, values in variance_data.items():
    plt.plot(hours, values, label=parameter)
plt.legend()
plt.xticks(hours)
plt.savefig('variance.png', dpi=300, bbox_inches='tight')

print("Graphs saved as 'standard_deviation.png' and 'variance.png'")