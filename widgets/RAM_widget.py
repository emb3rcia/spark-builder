#imports
from PyQt6.QtWidgets import QWidget, QHBoxLayout, QTableWidget, QTableWidgetItem, QFormLayout, QLineEdit, QLabel, QPushButton, QMessageBox, QSizePolicy, QHeaderView
from PyQt6.QtGui import QIntValidator

from styled_functions.styled_functions import Button, Label, Widget, TableWidget, LineEdit

#define ram tool
class RAM_widget(QWidget):
    def __init__(self, theme_data):
        super().__init__()
        #define main layout for ram tool
        main_layout = QHBoxLayout()
        self.setLayout(main_layout)
        #define and set up table
        table = TableWidget(theme_data['table'], theme_data['text']['text_disabled'], theme_data['extra'])
        table.setColumnCount(4)
        table.setHorizontalHeaderLabels(["MT/s", "CL (ns)", "FWL (ns)", "Delete entry"])
        table.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Expanding)
        table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.ResizeToContents)
        table.setMinimumWidth(sum([table.columnWidth(i) for i in range(table.columnCount())]) + 4)
        table.horizontalHeader().setStretchLastSection(False)

        #define main widget and layout
        interact_widget = Widget(theme_data['main_backgrounds'])
        interact_layout = QFormLayout()
        #set main widget layout
        interact_widget.setLayout(interact_layout)
        #add table and main widget to main layout
        main_layout.addWidget(table)
        main_layout.addWidget(interact_widget)
        #add textboxes and validate only numbers in them
        validator = QIntValidator()
        textbox_mts = LineEdit(theme_data['input'], theme_data['highlight'], theme_data['text']['text_disabled'])
        textbox_mts.setValidator(validator)
        textbox_mts.setPlaceholderText("Enter MT/s here")
        textbox_cl = LineEdit(theme_data['input'], theme_data['highlight'], theme_data['text']['text_disabled'])
        textbox_cl.setValidator(validator)
        textbox_cl.setPlaceholderText("Enter CL here")
        #add First Word Latency label
        label_fwl = Label("0 ns", theme_data['text'], 1)
        #add textboxes and label to layout
        mts_label = Label("MT/s:", theme_data['text'], 1)
        cl_label = Label("CL:", theme_data['text'], 1)
        fwl_label = Label("FWL:", theme_data['text'], 1)
        interact_layout.addRow(mts_label, textbox_mts)
        interact_layout.addRow(cl_label, textbox_cl)
        interact_layout.addRow(fwl_label, label_fwl)
        #define function deleting entry from table
        def deleteRow(row):
            button = self.sender()
            for row in range(table.rowCount()):
                if table.cellWidget(row, 3) == button:
                    table.removeRow(row)
                    break
        #define function that calculates First Word Latency
        def calculateFWL():
            exists = False
            #calculate fwl
            cl = int(textbox_cl.text())
            mts = int(textbox_mts.text())
            fwl = ((cl*2000)/mts)
            #display calculated latency rounded to 2 decimal points
            fwl_rounded = round(fwl, 2)
            label_fwl.setText(str(fwl_rounded) + " ns")
            #only add entry to label if it doesnt exist, if it does, give error
            for row in range(table.rowCount()):
                if table.item(row, 0).text() == textbox_mts.text() and table.item(row, 1).text() == textbox_cl.text():
                    exists = True
                    QMessageBox.warning(self, "Duplicate RAM", "This RAM configuration is already in the table!")
                    break
            if not exists:
                row = table.rowCount()
                table.insertRow(row)
                table.setItem(row, 0, QTableWidgetItem(str(mts)))
                table.setItem(row, 1, QTableWidgetItem(str(cl)))
                table.setItem(row, 2, QTableWidgetItem(str(fwl_rounded)))
                delete_button = Button("Delete entry", theme_data['button'], theme_data['text']['text_disabled'])
                delete_button.clicked.connect(deleteRow)
                table.setCellWidget(row, 3, delete_button)
        #add calculate fwl button
        calculate_fwl = Button("Calculate FWL", theme_data['button'], theme_data['text']['text_disabled'])
        calculate_fwl.clicked.connect(calculateFWL)
        interact_layout.addRow(calculate_fwl)
        #define function finding ram with lowest FWL
        def findBestRam():
            best_row = None
            lowest = None
            row_count = table.rowCount()

            for row in range(row_count):
                item = table.item(row, 2)
                if item is not None:
                    try:
                        value = float(item.text())
                        if lowest is None or value < lowest:
                            lowest = value
                            best_row = row
                    except ValueError:
                        pass
            #show ram with lowest FWL
            if best_row is not None:
                mt = table.item(best_row, 0).text()
                cl = table.item(best_row, 1).text()
                fwl = table.item(best_row, 2).text()
                best_fwl.setText(f"Best ram: {mt} MT/s {cl} CL: {fwl} ns FWL")
            else:
                best_fwl.setText("No values found in table")
        #define button finding ram with lowest FWL and add it to table
        calculate_best_ram = Button("Find best ram from table", theme_data['button'], theme_data['text']['text_disabled'])
        calculate_best_ram.clicked.connect(findBestRam)
        interact_layout.addRow(calculate_best_ram)
        best_fwl = Label("", theme_data['text'], 1)
        interact_layout.addRow(best_fwl)

        