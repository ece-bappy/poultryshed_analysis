import csv
import random

# Define the range of Chicken_No and the average weight
chicken_numbers = range(1, 91)
average_weight = 2.8

# Generate random weights with an average of 2.8
weights = [round(random.uniform(2.6, 2.9), 4) for _ in range(90)]

# Calculate the adjustment needed to ensure the average is exactly 2.8
adjustment = (average_weight - sum(weights) / len(weights)) / len(weights)

# Adjust each weight to ensure the average is exactly 2.8
weights = [round(weight + adjustment, 4) for weight in weights]

# Write data to CSV file
with open('inside.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Chicken_No', 'Weight'])
    for chicken_no, weight in zip(chicken_numbers, weights):
        writer.writerow([chicken_no, weight])
