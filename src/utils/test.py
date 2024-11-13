#==================================================
# Imports
#==================================================
import re
from tqdm import tqdm
from pathlib import Path

# Specify input and output file paths
input_file = 'data/test.json'       # Replace with the actual file path if different
output_file = 'data/test_1.json'

total = int(100000)
# Function to clean each line
def clean_json_line(line):
    # Remove 'u' if it prepends a key or value
    line = re.sub(r"u'([a-zA-Z0-9_]+)':", r'"\1":', line)
    line = re.sub(r": u'([^']+)'", r": '\1'", line)

    line = re.sub(r"\\'", "'", line) # Remove \ if it prepends a '

    line = re.sub(r'(?<=")([^"]*?)\\n([^"]*?)(?=")', lambda m: m.group(0).replace('\\n', ''), line) # Remove \n from text

    # # Handle already double-quoted values like u"1990's" to remove the 'u' without adding extra quotes
    line = re.sub(r'u"([^"]+)"', r'"\1"', line)                    # Values in double quotes with u

    # # # Replace boolean values True -> "True" and False -> "False"
    line = re.sub(r"(?<=: )True\b", '"True"', line)
    line = re.sub(r"(?<=: )False\b", '"False"', line)

    # # # Clean elements in arrays by removing 'u' and replacing single quotes with double quotes directly
    line = re.sub(
        r"\[([^\]]+)\]", 
        lambda m: '[' + ', '.join('"' + elem.strip(" 'u") + '"' for elem in m.group(1).split(", ")) + ']', 
        line
    )

    # print(repr(line))

    line = re.sub(r'("text": ")(.*?")(?=,)', lambda m:  "\"text\": " + "\'" + m.group(2) + "\'", line) # If ", convert to '

    return line

# Process each line of the file
with open(input_file, 'r', encoding='utf-8') as infile, open(output_file, 'w', encoding='utf-8') as outfile:
    print("Step 1...")
    for line in tqdm(infile, total=total):
        cleaned_line = clean_json_line(line)
        if not cleaned_line:
            continue
        outfile.write(cleaned_line)

#===========================================================

input_file = 'data/test_1.json'
output_file = 'data/test_2.json'

# Function to fix quotes and decode escape sequences
def fix_quotes_and_remove_trademark(line):
    # Remove unwanted \xae escape sequences (and others if needed)
    try:
        line = bytes(line, 'utf-8').decode('unicode_escape')
    except:
        return None # bad encoding
    # Remove the actual trademark symbol or any unwanted characters
    line = line.replace('™', '')  # Remove the ™ symbol if needed
    # Use a regular expression to fix double double-quotes around values
    line = re.sub(r'""([^"]+)""', r'"\1"', line)
    return line

if not Path(output_file).exists():
    # Open the input file and read line by line
    with open(input_file, 'r') as infile:
        lines = infile.readlines()
    
    fixed_lines = []

    # Apply the fix to each line and store the results
    print("Step 2...")
    for line in tqdm(lines, total=total):
        new_line = fix_quotes_and_remove_trademark(line)
        if not new_line:
            continue
        fixed_lines.append(new_line)

    # Write the fixed lines to the output file
    with open(output_file, 'w') as outfile:
        outfile.writelines(fixed_lines)

#===========================================================

input_file =  'data/test_2.json'
output_file = 'data/test_3.json'

# Function to process string values
def process_value(value):
    if isinstance(value, str):  # If value is a string
        # Remove all occurrences of '"' and surround with "
        value = '"' + value.replace('"', '') + '"'
    return value

# Function to process a list (array) of values
def process_array(array):
    return [process_value(item) if isinstance(item, str) else item for item in array]

# Function to process each line in the file
def process_file(input_filename, output_filename):
    with open(input_filename, 'r') as infile, open(output_filename, 'w') as outfile:
        print("Step 3...")
        for line in tqdm(infile, total=total):
            line = line.strip()

            # Ignore empty lines
            if not line:
                continue

            # Handle JSON-like structure manually (without json library)
            if line.startswith("{") and line.endswith("}"):


                # line = re.sub(r"\"(.*?)\"(?=:|,|})", lambda m: m.group(0).replace(',', ''), line) # Remove , found in strings - allow all ' occurences until you find a ',                
                # line = re.sub(r"'(.*?)'(?=:|,|})", lambda m: m.group(0).replace(',', ''), line)

                # re.sub(r'"text": \'(.*?)\', "early_access"', lambda m: print(m.group(1)), line)

                # re.sub(r'"text": \'(.*?)(?=\', )\'', lambda m: print(m), line) # Fix text attribute

                # If we already have ", revert back to '
                # line = re.sub(r'("text": ")(.*?)(?=",)', r'\1\'\2\'', line)

                # print(line)

                line = re.sub(r'"text": \'(.*?)(?=\', )\'', lambda m: "\"text\": \'" + m.group(1).replace(',', '').replace('\t', '').replace('\r', '') + "\'", line) # Fix text attribute

                line = line[1:-1]  # Remove the surrounding braces
                line = re.sub(r'\\', r'\\\\', line)

                # Process each key-value pair
                pairs = line.split(",")  # Split by commas to get key-value pairs
                processed_pairs = []
                for pair in pairs:
                    pair = pair.strip()  # Clean up extra whitespace
                    
                    # Skip empty strings or malformed pairs
                    if ':'in pair:
                        key, value = pair.split(":", 1)  # Split each pair by the first colon
                        key = key.strip()  # Remove leading/trailing whitespace
                        value = value.strip()  # Remove leading/trailing whitespace

                        # Process values inside arrays
                        if value.startswith("[") and value.endswith("]"):  # It's an array
                            value = value[1:-1]  # Remove the surrounding brackets
                            array_items = value.split(",")  # Split array items by commas
                            value = "[" + ", ".join(process_array(array_items)) + "]"
                        # Process string values
                        elif value.startswith('\'') and value.endswith('\''):  # It's a string
                            value = process_value(value[1:-1])  # Remove the surrounding quotes and process
                        # elif value.startswith('\'') and not value.endswith('\"') and not value.endswith('\''):
                        #     print(value)
                        #     value = process_value(value[1:-1]) 
                        

                        processed_pairs.append(f'{key}: {value}')
                    else:
                        processed_pairs.append(pair)

                # Join the processed pairs back into a single string and add the surrounding braces
                processed_line = "{" + ", ".join(processed_pairs) + "}"
                outfile.write(processed_line + '\n')

# Example usage
process_file(input_file, output_file)