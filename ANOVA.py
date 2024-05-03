import csv
import scipy.stats as stats
import numpy as np

# Open the CSV file
with open('data2.csv', 'r') as file:
    reader = csv.DictReader(file)
    data = list(reader)

# Create dictionaries to store the data for each hour
hourly_data = {hour: {'Temperature': [], 'Humidity': [], 'Gas Level': []} for hour in range(24)}

# Populate the hourly data dictionary
for row in data:
    hour = int(row['Time'].split(':')[0])
    hourly_data[hour]['Temperature'].append(float(row['Temperature']))
    hourly_data[hour]['Humidity'].append(float(row['Humidity']))
    hourly_data[hour]['Gas Level'].append(float(row['Gas Level']))

# Perform ANOVA for each parameter
for parameter in ['Temperature', 'Humidity', 'Gas Level']:
    data_by_hour = [hourly_data[hour][parameter] for hour in range(24)]
    f_value, p_value = stats.f_oneway(*data_by_hour)
    print(f"{parameter} ANOVA Results:")
    print(f"F-value: {f_value:.2f}")
    print(f"P-value: {p_value:.4f}")
    if p_value < 0.05:
        print("There is a significant difference between the means of the groups.")
    else:
        print("There is no significant difference between the means of the groups.")
    print()