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

Default themes:

`dark`

<img width="577" height="238" alt="Screenshot_20260206_205428" src="https://github.com/user-attachments/assets/fa3b1e99-32a8-40a8-ae36-520f3b6c8e23" />

<img width="577" height="238" alt="Screenshot_20260206_205415" src="https://github.com/user-attachments/assets/b82b552f-23e8-4229-8759-e1f8d85ed0e3" />


`light`

<img width="577" height="238" alt="Screenshot_20260206_205454" src="https://github.com/user-attachments/assets/09dad605-dc1e-4416-94db-32c1d50e0c0e" />

<img width="577" height="238" alt="Screenshot_20260206_205501" src="https://github.com/user-attachments/assets/ee20e4b5-26b7-4c83-8de6-e56e9ab5e868" />


`amoled`

<img width="577" height="238" alt="Screenshot_20260206_205434" src="https://github.com/user-attachments/assets/0c97e515-dec6-4bf5-9c6e-d05bf25a0298" />

<img width="577" height="238" alt="Screenshot_20260206_205444" src="https://github.com/user-attachments/assets/635f7561-3490-41cd-b1de-8d9cc43effa7" />

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
