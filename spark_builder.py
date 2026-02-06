#required imports
import sys
from PyQt6.QtWidgets import QApplication, QLabel, QPushButton, QTableWidget, QTableWidgetItem, QVBoxLayout, QHBoxLayout, QMainWindow, QWidget, QStackedWidget
from widgets.RAM_widget import RAM_widget
from widgets.settings_widget import settings_widget
from helpers.theme_helper import initializeThemes
from helpers.settings_helper import initializeSettings
from styled_functions.styled_functions import Button, Label, LineEdit, MainWindow, TableWidget, Widget, StackedWidget, ComboBox

#initialize themes
theme_data = initializeThemes()

#initialize settings
settings_data = initializeSettings()

current_theme_name = settings_data['theme']
theme = theme_data[current_theme_name]

#define app
app = QApplication(sys.argv)

#apply tooltip theme globally function
def setTooltipStyle():
    app.instance().setStyleSheet(f"""
        QToolTip {{
            background-color: {theme['main_backgrounds']['tooltip_background']};
            color: {theme['text']['text_tooltip']};
            border: 1px solid {theme['accent']['accent_primary']};
        }}
    """)

setTooltipStyle()


#define main window
window = MainWindow(theme['main_backgrounds'])
central = Widget(theme['main_backgrounds'])
window.setCentralWidget(central)

#refresh theme function / made in help with chat gpt but not by him
def refresh_theme(theme_name):
    theme = theme_data[theme_name]

    setTooltipStyle()

    window.update_theme(theme['main_backgrounds'])

    for widget in window.findChildren(QWidget):
        if hasattr(widget, "update_theme"):
            if isinstance(widget, Button):
                widget.update_theme(theme['button'], theme['text']['text_disabled'])
            elif isinstance(widget, Label):
                widget.update_theme(theme['text'])
            elif isinstance(widget, LineEdit):
                widget.update_theme(theme['input'], theme['highlight'], theme['text']['text_disabled'])
            elif isinstance(widget, MainWindow):
                widget.update_theme(theme['main_backgrounds'])
            elif isinstance(widget, TableWidget):
                widget.update_theme(theme['table'], theme['extra'], theme['text']['text_disabled'])
            elif isinstance(widget, Widget):
                widget.update_theme(theme['main_backgrounds'])
            elif isinstance(widget, StackedWidget):
                widget.update_theme(theme['main_backgrounds'])
            elif isinstance(widget, ComboBox):
                widget.update_theme(theme['combo-box'], theme['text']['text_disabled'])

#define main layout and set in as layout for main window
main_layout = QHBoxLayout()
central.setLayout(main_layout)

#tool selector section
tool_selector = Widget(theme['main_backgrounds'])
tool_selector_layout = QVBoxLayout()
tool_selector.setLayout(tool_selector_layout)

#current tool section
current_tool = StackedWidget(theme['main_backgrounds'])
current_tool.addWidget(RAM_widget(theme))

#setting current tool to ram function
def setToolToRAM():
    current_tool.setCurrentIndex(0)

RAM_tool = Button("RAM tool", theme['button'], theme['text']['text_disabled'])
RAM_tool.clicked.connect(setToolToRAM)
tool_selector_layout.addWidget(RAM_tool)

current_tool.addWidget(settings_widget(theme, settings_data, refresh_theme))

#setting current tool to settings function
def setToolToSettings():
    current_tool.setCurrentIndex(1)

Settings = Button("Settings", theme['button'], theme['text']['text_disabled'])
Settings.clicked.connect(setToolToSettings)
tool_selector_layout.addWidget(Settings)

#add tool selector and current tool view to main window
main_layout.addWidget(tool_selector)
main_layout.addWidget(current_tool)

#show window
window.show()

#exit app
app.exec()