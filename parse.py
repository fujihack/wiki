# Crap script to copy fuji camera data to json/md
import os
import yaml
import json
from datetime import datetime

def parse_yaml_file(file_path):
    with open(file_path, 'r') as file:
        try:
            yaml_data = yaml.safe_load(file)
            return yaml_data
        except yaml.YAMLError as exc:
            print(f"Error parsing YAML file {file_path}: {exc}")
            return None

def log_entry(file_name, wireless, announced, name):
    entry = {
        "Wireless": wireless,
        "Announced": announced,
        "Name": name
    }
    return entry

def find_and_parse_files(directory):
    log_entries = []

    if not os.path.exists(directory):
        print(f"Directory '{directory}' does not exist.")
        return

    for root, dirs, files in os.walk(directory):
        for file_name in files:
            if 'fuji' in file_name:
                file_path = os.path.join(root, file_name)
                yaml_data = parse_yaml_file(file_path)
                if yaml_data:
                    wireless = yaml_data.get('Specs', {}).get('Wireless', 'none')
                    announced = yaml_data.get('Specs', {}).get('Announced')
                    if announced:
                        announced = datetime.strptime(announced, '%b %d, %Y').strftime('%Y-%m-%d')
                    name = yaml_data.get('Name')
                    log_entries.append(log_entry(file_name, wireless, announced, name))

    # Sort log_entries by the 'Announced' date
    log_entries.sort(key=lambda x: x.get('Announced'), reverse=True)


    with open("dump.md", "w") as file:
        lastdate = 2023
        for e in log_entries:
            if e['Announced'][0:4] != lastdate:
                file.write("## " + e['Announced'][0:4] + "\n")
            file.write("- " + e['Name'] + "\n")
            lastdate = e['Announced'][0:4]
        #json.dump(log_entries, file, indent=4)

# Replace 'database' with the actual directory path
directory_path = 'database'
find_and_parse_files(directory_path)
