import json
import csv
import re

# Function to convert JSON file to CSV
def json_to_csv(json_file, csv_file):
    # Open the JSON file
    with open(json_file, 'r', encoding='utf-8') as f:
        # Read all lines (each line is a JSON object)
        json_lines = f.readlines()

    # List to store all rows (each row is a dictionary)
    rows = []

    count = 1
    # Loop through each JSON line
    for line in json_lines:
        print(count)
        count+=1
        data = json.loads(line)
        rows.append(data)

    # Get all column names (keys from all dictionaries)
    all_columns = set()
    for row in rows:
        all_columns.update(row.keys())

    # Sort the columns to keep a consistent order
    all_columns = sorted(list(all_columns))

    # Open CSV file for writing
    with open(csv_file, 'w', encoding='utf-8', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=all_columns)
        
        # Write the header (column names)
        writer.writeheader()

        # Write each row, filling missing values with empty strings
        for row in rows:
            # Create a row with blank values for missing columns
            row_data = {col: row.get(col, '') for col in all_columns}
            writer.writerow(row_data)

# Example usage
json_file = 'data/fixed_steam_games_3.json'  # Replace with your actual JSON file path
csv_file = 'data/output.csv'  # Output CSV file

json_to_csv(json_file, csv_file)

print(f"Conversion complete! CSV saved to {csv_file}")



