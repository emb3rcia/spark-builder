from PyQt6 import QtWidgets

version = "alpha 0.1"

app = QtWidgets.QApplication()

window = QtWidgets.QMainWindow()
window.setWindowTitle("spark builder " + version)

app.exec()