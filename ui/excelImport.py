import sys
sys.path.append('..')
sys.path.append('.')
import pandas as pd
from ui.excel_ui import Ui_ExcelReader
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox, QTableWidgetItem
from PyQt5.QtCore import pyqtSignal      

class excel_ui(QMainWindow):
    import_confirmed = pyqtSignal()
    def __init__(self):
        super(excel_ui, self).__init__()
        self.ui = Ui_ExcelReader()
        self.ui.setupUi(self)
        self.file_path = ""  # To store the file path
        self.df = pd.DataFrame()  # To store the Excel data
        self.ui.browse_btn.clicked.connect(self.browse_file)
        self.ui.read_btn.clicked.connect(self.read_excel)
        self.ui.clr_btn.clicked.connect(self.clear_table)
        self.ui.confirm_btn.clicked.connect(self.write_excel)

    def browse_file(self):
        """
        Open a file dialog to browse Excel files.
        """
        file_name, _ = QFileDialog.getOpenFileName(self, "Open Excel File", "", "Excel Files (*.xlsx)")
        if file_name:
            self.file_path = file_name
            self.ui.file_path_line_edit.setText(self.file_path)
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
            self.ui.table_widget.setRowCount(self.df.shape[0])
            self.ui.table_widget.setColumnCount(self.df.shape[1])
            self.ui.table_widget.setHorizontalHeaderLabels(self.df.columns)
            for i in range(self.df.shape[0]):
                for j in range(self.df.shape[1]):
                    self.ui.table_widget.setItem(i, j, QTableWidgetItem(str(self.df.iloc[i, j])))
            self.ui.table_widget.horizontalHeader().setVisible(True)
            self.ui.table_widget.verticalHeader().setVisible(True)
            self.ui.table_widget.setShowGrid(True)

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
        try:
            self.ui.table_widget.clear()
        except:
            QMessageBox.critical(self, "Error", "Please select an Excel file to read.")
            return
        self.ui.table_widget.setShowGrid(False)
        self.file_path = ""
        self.ui.file_path_line_edit.clear()
        self.ui.table_widget.horizontalHeader().setVisible(False)
        self.ui.table_widget.verticalHeader().setVisible(False)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = excel_ui()
    window.show()
    sys.exit(app.exec_())

