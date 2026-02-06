import json
import os

default_settings = {
    "theme": "dark"
}

# get the absolute path to config folder / made with help of chatgpt
config_path = os.path.join(os.path.dirname(__file__), "..", "config")
os.makedirs(config_path, exist_ok=True)  # create folder if it doesn't exist
settings_file = os.path.join(config_path, "settings.json")

#define initialize settings function
def initializeSettings():
    #try to open already created settings.json file
    try:
        with open(settings_file, "r") as f:
            settings_data = json.load(f)
            f.close()
    #if file not found, create one and write default settings to it
    except FileNotFoundError:
        with open(settings_file, "w+") as f:
            json.dump(default_settings, f, indent=4)
            f.close()
        settings_data = default_settings
        
    return settings_data