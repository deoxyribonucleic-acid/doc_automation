import sys
import pandas as pd
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox, QTableWidgetItem
from PyQt5.uic import loadUi
from PyQt5.QtCore import pyqtSignal      
sys.path.append('..')
sys.path.append('.')
class ExcelReader(QMainWindow):
    import_confirmed = pyqtSignal()
    def __init__(self):
        super(ExcelReader, self).__init__()
        print('start init')
        loadUi("./ui/ReadExcel.ui", self)  # Load the UI file
        print('ui_loaded')
        self.file_path = ""  # To store the file path
        self.df = pd.DataFrame()  # To store the Excel data
        self.browse_btn.clicked.connect(self.browse_file)
        self.read_btn.clicked.connect(self.read_excel)
        self.clr_btn.clicked.connect(self.clear_table)
        self.confirm_btn.clicked.connect(self.write_excel)

    def browse_file(self):
        """
        Open a file dialog to browse Excel files.
        """
        file_name, _ = QFileDialog.getOpenFileName(self, "Open Excel File", "", "Excel Files (*.xlsx)")
        if file_name:
            self.file_path = file_name
            self.file_path_line_edit.setText(self.file_path)
            self.read_excel()

    def read_excel(self):
        """
        Read the Excel file using Pandas and display the data in the table widget.
        """
        if not self.file_path:
            QMessageBox.critical(self, "Error", "Please select an Excel file to read.")
            return
        try:
            self.df = pd.read_excel(self.file_path)
            self.table_widget.setRowCount(self.df.shape[0])
            self.table_widget.setColumnCount(self.df.shape[1])
            self.table_widget.setHorizontalHeaderLabels(self.df.columns)
            for i in range(self.df.shape[0]):
                for j in range(self.df.shape[1]):
                    self.table_widget.setItem(i, j, QTableWidgetItem(str(self.df.iloc[i, j])))
            self.table_widget.horizontalHeader().setVisible(True)
            self.table_widget.verticalHeader().setVisible(True)
            self.table_widget.setShowGrid(True)

        except Exception as e:
            QMessageBox.critical(self, "Error", f"An error occurred while reading the Excel file.\n\n{e}")
    
    def write_excel(self):
        if self.df.empty:
            QMessageBox.critical(self, "Error", "Please select an Excel file to read.")
            return
        self.import_confirmed.emit()
        self.hide()
        return 

    def clear_table(self):
        self.table_widget.clear()
        self.table_widget.setShowGrid(False)
        self.file_path = ""
        self.file_path_line_edit.clear()
        self.table_widget.horizontalHeader().setVisible(False)
        self.table_widget.verticalHeader().setVisible(False)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ExcelReader()
    window.show()
    sys.exit(app.exec_())

