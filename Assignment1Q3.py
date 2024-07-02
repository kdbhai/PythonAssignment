import configparser
import json
import os
from flask import Flask, jsonify

app = Flask(__name__)

def parse_config_file(config_file_path):
    try:
        config = configparser.ConfigParser()
        config.read(config_file_path)

        parsed_data = {}
        for section in config.sections():
            parsed_data[section] = dict(config[section])

        return parsed_data
    except FileNotFoundError:
        print("Error: Configuration file not found.")
        return None
    except Exception as e:
        print(f"Error: {e}")
        return None

def save_to_json(data, output_file_path):
    try:
        with open(output_file_path, 'w') as json_file:
            json.dump(data, json_file, indent=4)
        print(f"Saved data to {output_file_path}")
    except Exception as e:
        print(f"Error saving data to JSON: {e}")

@app.route('/get_config', methods=['GET'])
def get_config():
    try:
        with open('parsed_config.json', 'r') as json_file:
            data = json.load(json_file)
        return jsonify(data)
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    config_file_path = "sample_config.ini"  # Replace with your actual config file path
    output_file_path = "parsed_config.json"  # Replace with your desired output file path

    parsed_data = parse_config_file(config_file_path)
    if parsed_data:
        save_to_json(parsed_data, output_file_path)

    app.run(debug=True)
