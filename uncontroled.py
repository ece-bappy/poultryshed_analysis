import csv
import random

# Open the CSV file for reading
with open('data3.csv', 'r') as file:
    # Create a CSV reader object
    reader = csv.DictReader(file)
    
    # Create a list to hold modified data
    modified_data = []
    
    # Iterate over each row in the CSV file
    for row in reader:
        # Generate a random value between 5 and 15 for Humidity
        humidity_subtract = random.randint(5, 20)
        
        # Subtract random value from Humidity column
        row['Humidity'] = str(float(row['Humidity']) - humidity_subtract)
        
        # Generate a random value between 5 and 10 for Gas Level
        gas_add = random.randint(7, 15)
        
        # Add random value to Gas Level column
        row['Gas Level'] = str(float(row['Gas Level']) + gas_add)
        
        # Append modified row to the list
        modified_data.append(row)

# Write modified data back to a new CSV file
with open('data4.csv', 'w', newline='') as file:
    # Define the fieldnames based on the original CSV file
    fieldnames = ['Day', 'Date', 'Time', 'Temperature', 'Humidity', 'Gas Level']
    
    # Create a CSV writer object
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    
    # Write the header
    writer.writeheader()
    
    # Write modified data to the file
    writer.writerows(modified_data)

print("Data has been modified and saved to 'modified_data.csv'")
