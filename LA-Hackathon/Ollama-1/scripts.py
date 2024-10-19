import json
import subprocess
import csv

# Load JSON data as string
with open('hack-la-24-banksy-discussions.json', 'r') as file:
    data = json.load(file)
discussion_text = json.dumps(data)

prompt = "I will give you JSON data in text form. Generate 5 topics based on the text and gcount the number of times the topic was mentioned/discussed. Organize these in a tabular format so I can later put them into a CSV file.\nText:\n"
prompt += discussion_text;

# Run the LLaMA model using the subprocess module
result = subprocess.run(['ollama', 'run', 'llama3.2:1b'], input=prompt, text=True, capture_output=True)

output = result.stdout.strip()

# Split the output into lines (assuming LLaMA returns a structured text)
lines = output.split('\n')

# Prepare data for CSV
data = []
for line in lines:
    # Assuming the output is comma-separated values
    data.append(line.split(','))

# Define the CSV file path
file_path = 'data.csv'

# Write to CSV file
with open(file_path, mode='w', newline='') as file:
    writer = csv.writer(file)
    
    # Write header (optional, adjust based on your output)
    writer.writerow(['Topic', 'Count'])
    
    # Write data rows
    for row in data:
        writer.writerow(row)

print(f'Data has been written to {file_path}')
