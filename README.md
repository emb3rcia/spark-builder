# spark-builder
Spark builder is a tool that helps people build PCs. Current features:
- [RAM First Word Latency calculator and comparer](#fwl-tool)
- GPU Comparer *coming soon*
- CPU Comparer *coming soon*
- PSU Choice helper *coming soon*
- [Custom themes](#custom-themes)

# FWL Tool
This tool allows you to add RAM configurations to the list, calculate their First Word Latency, and then pick configuration with the lowest!

> MT/s isn’t everything! FWL can be more important in some scenarios, as it represents the time your RAM takes to deliver the first piece of data.

# Custom themes
In `config` folder, you will find `themes.json`, if you want to make your own theme just copy one of the default themes and change hex color values! If you want to modify existing one, just change the values directly! You corrupted your themes.json? Don't worry! Just delete the file and program will create it again with default themes in it!

# Installation
You have 2 options to install this program:
1. [Releases](https://github.com/emb3rcia/spark-builder/releases)
2. [Git clone](#git-clone-method)

## Git clone method
1. Install [git](https://git-scm.com/)
2. Open cmd or terminal
3. Run `git clone https://github.com/emb3rcia/spark-builder.git`
4. Run `cd spark-builder`
5. Run `pip install -r requirements.txt`
6. Run `python spark_builder.py`

