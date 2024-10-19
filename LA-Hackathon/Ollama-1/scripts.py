import json
import subprocess

# Load JSON data as string
with open('hack-la-24-banksy-discussions.json', 'r') as file:
    data = json.load(file)
input_text = json.dumps(data)

prompt = "I am giving you a JSON file in string format containing discussion posts of a university level course about Banksy. Categorize the discussions into 5 topics and provide a count for each topic.\n"
prompt += input_text;

# Run the LLaMA model using the subprocess module
result = subprocess.run(['ollama', 'run', 'llama3.2:1b'], input=prompt, text=True, capture_output=True)

# Print the output from the model
print("STDOUT:", result.stdout)
print("STDERR:", result.stderr)
