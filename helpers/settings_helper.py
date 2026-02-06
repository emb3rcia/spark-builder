import json
import os
from helpers.theme_helper import listThemes, default_themes

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
    if os.path.exists(settings_file):
        with open(settings_file, "r") as f:
            try:
                settings_data = json.load(f)
            except json.JSONDecodeError:
                settings_data = default_settings.copy()
    else:
        settings_data = default_settings.copy()

    #check if selected theme exists in themes.json
    from helpers.theme_helper import listThemes

    all_themes = listThemes()
    current_theme = settings_data.get("theme", "dark")

    if current_theme not in all_themes:
        #fallback logic
        if current_theme in default_themes:
            #append default theme to themes.json (handled by initializeThemes)
            settings_data["theme"] = current_theme
        else:
            #custom theme missing -> fallback to dark
            if "dark" in all_themes:
                settings_data["theme"] = "dark"
            else:
                #if dark itself missing, initializeThemes will recreate it
                settings_data["theme"] = "dark"

    #save updated settings safely
    tmp_file = settings_file + ".tmp"
    with open(tmp_file, "w") as f:
        json.dump(settings_data, f, indent=4)
    os.replace(tmp_file, settings_file)

    return settings_data
