import os

# Read the requirements.txt file
with open('D://prompt-engineering-for-generative-ai-examples//requirements.txt', 'r') as req_file:
    requirements = req_file.readlines()

# Filter out comments and blank lines
packages = [line.strip() for line in requirements if line.strip() and not line.startswith("#")]

# Prepare the .yml content
yml_content = """name: promptenv
channels:
  - defaults
  - conda-forge
dependencies:
  - python=3.9
  - pip
  - pip:\n"""

for pkg in packages:
    yml_content += f"      - {pkg}\n"

# Write the .yml file
with open('D://prompt-engineering-for-generative-ai-examples//environment.yml', 'w') as yml_file:
    yml_file.write(yml_content)

print("environment.yml created successfully.")
