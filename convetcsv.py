import csv

# Read the input text file
with open("1415.txt", "r") as file:
    lines = file.readlines()

# Write the CSV file
with open("output.csv", "w", newline="") as csvfile:
    csv_writer = csv.writer(csvfile)

    # Write header
    csv_writer.writerow(["Time", "Temperature", "Humidity", "Gas Level"])

    # Write data
    for line in lines:
        fields = line.strip().split(",")
        csv_writer.writerow(fields)

print("CSV file has been created successfully.")
