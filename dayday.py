# this code adds day no in the main CSV as day wasn't taken as input while logging.
import csv


# Function to calculate day based on conditions
def calculate_day(prev_hour, current_hour, prev_day):
    if prev_hour - current_hour == 23:
        return prev_day + 1
    else:
        return prev_day


# Input and output file paths
input_file_path = "final.csv"
output_file_path = "final_data.csv"

# Read CSV file and update day column
with open(input_file_path, "r") as infile, open(
    output_file_path, "w", newline=""
) as outfile:
    reader = csv.reader(infile)
    header = next(reader)
    header.append("Day")  # Add 'Day' column to header

    writer = csv.writer(outfile)
    writer.writerow(header)

    prev_hour = None
    prev_day = 0

    for row in reader:
        time = row[0].split(":")
        current_hour = int(time[0])

        if prev_hour is not None:
            row.append(str(calculate_day(prev_hour, current_hour, prev_day)))
        else:
            row.append("1")  # Set day=1 for the first record

        writer.writerow(row)
        prev_hour = current_hour
        prev_day = int(row[-1])  # Update prev_day for the next iteration

print(f"Days inserted and output saved to {output_file_path}")
