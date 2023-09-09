from PyQt5 import QtCore

from tools.db_operate import *
from PyQt5.QtWidgets import QFileDialog, QMessageBox
import sys
sys.path.append("..")
sys.path.append(".")
from tools.db_operate import dbutils as dbutils

class reg:

    def __init__(self,parent):
        self.parent=parent
        self.student_operate=student()
        self.parent.setWindowModality(QtCore.Qt.ApplicationModal)
        self.major_db=pd.read_excel('database/majors.xlsx')


    def init(self):
        stu_list=self.student_operate.read_all_items()
        self.setup_combobox()
        if stu_list.shape[0] > 0:
            stu=stu_list.iloc[0]
            #self.parent.academy_input.setText(str(stu.academy))
            #self.parent.major_input.setText(str(stu.major))
            self.parent.grade_input.setText(str(stu.grade))
            self.parent.banji_input.setText(str(stu.banji))
            self.parent.teacher_input.setText(str(stu.teacher))
            self.parent.zhichen_input.setText(str(stu.zhichen))

    def add_student(self):
        print('执行添加')
        items = {
            "ID": self.parent.id_input.text(),
            "stu_name": self.parent.name_input.text(),
            "academy": self.parent.school_select.currentText(),
            "major": self.parent.major_select.currentText(),
            "grade": self.parent.grade_input.text(),
            "banji": self.parent.banji_input.text(),
            "title": self.parent.title_input.text(),
            "teacher": self.parent.teacher_input.text(),
            "zhichen": self.parent.zhichen_input.text()
        }
        result, msg = dbutils.verify_item(self.student_operate, items)
        if not result:
            self.parent.warning.setText(msg)
            return
        self.parent.warning.setText('')
        try:
            self.student_operate.add_item(items)
            QMessageBox.about(self.parent, "sucess", "录入成功")
            self.parent.update_db.emit()
        except:
            QMessageBox.about(self.parent, "error", "录入失败")

    def setup_combobox(self):
        print(self.major_db)
        school_list=self.major_db.columns.values.tolist()
        for school in school_list:
            self.parent.school_select.addItem(school)
        self.setup_major()
        self.parent.school_select.currentIndexChanged.connect(self.setup_major)

    def setup_major(self):
        self.parent.major_select.clear()
        school=self.parent.school_select.currentText()
        major_list=self.major_db[school].dropna().values.tolist()
        for major in major_list:
            self.parent.major_select.addItem(major)

