import csv
from statistics import mean, stdev, variance

# Open the CSV file
with open('data2.csv', 'r') as file:
    reader = csv.DictReader(file)
    data = list(reader)

# Create a dictionary to store the data for each hour
hourly_data = {hour: {'Temperature': [], 'Humidity': [], 'Gas Level': []} for hour in range(24)}

# Populate the hourly data dictionary
for row in data:
    hour = int(row['Time'].split(':')[0])
    hourly_data[hour]['Temperature'].append(float(row['Temperature']))
    hourly_data[hour]['Humidity'].append(float(row['Humidity']))
    hourly_data[hour]['Gas Level'].append(float(row['Gas Level']))

# Calculate the standard deviation and variance for each hour
for hour, values in hourly_data.items():
    print(f"Hour: {hour}")
    for parameter, data_points in values.items():
        std_dev = round(stdev(data_points), 2)
        var = round(variance(data_points), 2)
        print(f"{parameter} - Standard Deviation: {std_dev}, Variance: {var}")
    print()