import sys

from tools import global_variable as glv
glv._init()

import PyQt5.QtCore as QtCore
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QMainWindow, QDockWidget, QMessageBox, QApplication
from ui.main_ui_teacher import Ui_MainWindow 
from ui.register import Ui_DockWidget
from ui.css_init import main_style
from ui import excelImport

from MainEvent import Event
from RegEvent import reg
from tools.db_operate import dbutils

class reg_ui(QDockWidget,Ui_DockWidget):
    update_db=pyqtSignal()

    def __init__(self):
        super(reg_ui,self).__init__()
        self.controller=reg(self)
        self.activateWindow()
        self.setupUi(self)
        self.bind()
        if not self.controller.init():
            QMessageBox.warning(self.parent(),"警告","专业信息表缺失，程序即将退出")
            # Wait 2s
            QtCore.QTimer.singleShot(2000, QtCore.QCoreApplication.instance().quit)
        self.init()

    def bind(self):
        self.pushButton.clicked.connect(self.controller.add_student)

    def init(self):
        self.dockWidgetContents.setStyleSheet(main_style.reg_window())
        self.setStyleSheet(main_style.reg_mess())
# main window should edit
class main_ui(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super(main_ui,self).__init__()
        self.controller=Event(self)
        self.activateWindow()
        self.setupUi(self)
        self.bind()
        self.css_init()
        self.stackedWidget.setCurrentIndex(1)
        self.toolBar.hide()
        self.init_mode()

    def css_init(self):
        self.setStyleSheet(main_style.main_window())
        self.name_input.setStyleSheet(main_style.input_box())
        self.id_input.setStyleSheet(main_style.input_box())
        #self.major_input.setStyleSheet(main_style.input_box())
        #self.academy_input.setStyleSheet(main_style.input_box())
        self.grade_input.setStyleSheet(main_style.input_box())
        self.banji_input.setStyleSheet(main_style.input_box())
        self.title_input.setStyleSheet(main_style.input_box())
        self.teacher_input.setStyleSheet(main_style.input_box())
        self.zhichen_input.setStyleSheet(main_style.input_box())
        self.output_input.setStyleSheet(main_style.show_box())
        self.output_input_4.setStyleSheet(main_style.show_box())
        self.frame.setStyleSheet(main_style.header())
        self.zdls_add.setStyleSheet(main_style.add_sig_btn())
        self.xzzz_add.setStyleSheet(main_style.add_sig_btn())
        self.xzcy_add.setStyleSheet(main_style.add_sig_btn())
        self.choice_stu.setStyleSheet(main_style.stu_choice())
        self.add_stu_btn.setStyleSheet(main_style.add_sig_btn())
        self.login_btn.setStyleSheet(main_style.login_btn())
        self.run_button.setStyleSheet(main_style.login_btn())
        self.run_signature.setStyleSheet(main_style.login_btn())
        self.run_ass.setStyleSheet(main_style.login_btn())
        self.run_merge.setStyleSheet(main_style.login_btn())
        self.choice_tem_out_path.setStyleSheet(main_style.path_select_btn())
        self.choice_sig_path.setStyleSheet(main_style.path_select_btn())
        self.choice_ass_out_path.setStyleSheet(main_style.path_select_btn())
        self.choice_total_file_path.setStyleSheet(main_style.path_select_btn())
        self.choice_output_4.setStyleSheet(main_style.path_select_btn())
        self.ass_out_path.setStyleSheet(main_style.show_box())
        self.sig_file_list.setStyleSheet(main_style.show_list())
        self.merge_file_list.setStyleSheet(main_style.show_list())
        self.tabWidget.setStyleSheet(main_style.tab_view())



    def init(self):
        self.controller.del_temp()
        self.choice_stu.clear()
        while(True):
            stu_table=self.controller.read_all_student()
            if stu_table.shape[0]==0:
                # self.controller.choose_and_import()
                QMessageBox.warning(self,"警告","学生列表为空，请录入或导入学生信息！")
                break
            else:
                self.init_info()
                break
            
            
    def init_info(self):
        stu_table=self.controller.read_all_student()
        stu = stu_table.head(1)
        # print(stu)
        self.id_input.setText(str(stu.index.values[0]))
        self.name_input.setText(str(stu.stu_name.values[0]))
        self.controller.setup_combobox()
        #self.academy_input.setText(str(stu.academy.values[0]))
        #self.major_input.setText(str(stu.major.values[0]))
        self.grade_input.setText(str(stu.grade.values[0]))
        self.school_select.setCurrentText(str(stu.academy.values[0]))
        self.major_select.setCurrentText(str(stu.major.values[0]))
        self.banji_input.setText(str(stu.banji.values[0]))
        self.title_input.setText(str(stu.title.values[0]))
        self.teacher_input.setText(str(stu.teacher.values[0]))
        self.zhichen_input.setText(str(stu.zhichen.values[0]))

        self.com_1_1.setText(stu.com_1_1.values[0])
        self.com_1_2.setText(stu.com_1_2.values[0])
        self.com_1_3.setText(stu.com_1_3.values[0])
        self.com_1_4.setText(stu.com_1_4.values[0])
        self.com_1_5.setText(stu.com_1_5.values[0])
        self.com_1_6.setText(stu.com_1_6.values[0])
        self.com_1_7.setText(stu.com_1_7.values[0])
        self.com_1_8.setText(stu.com_1_8.values[0])
        self.com_1_9.setText(stu.com_1_9.values[0])
        self.com_2_1.setText(stu.com_2_1.values[0])
        self.com_2_2.setText(stu.com_2_2.values[0])
        self.com_2_3.setText(stu.com_2_3.values[0])
        self.com_2_4.setText(stu.com_2_4.values[0])
        self.com_2_5.setText(stu.com_2_5.values[0])
        self.com_2_6.setText(stu.com_2_6.values[0])
        self.com_2_7.setText(stu.com_2_7.values[0])
        self.com_2_8.setText(stu.com_2_8.values[0])
        self.com_3_1.setText(stu.com_3_1.values[0])
        self.com_3_2.setText(stu.com_3_2.values[0])
        self.com_3_3.setText(stu.com_3_3.values[0])
        self.com_3_4.setText(stu.com_3_4.values[0])
        self.com_3_5.setText(stu.com_3_5.values[0])
        self.com_3_6.setText(stu.com_3_6.values[0])
        self.com_3_7.setText(stu.com_3_7.values[0])
        self.com_3_8.setText(stu.com_3_8.values[0])
        self.com_3_9.setText(stu.com_3_9.values[0])
        self.com_3_10.setText(stu.com_3_10.values[0])

        # print(self.banji_input.text())
        if '?' in self.banji_input.text():
            self.banji_input.setStyleSheet(main_style.input_box_s())

        if '职称' in self.zhichen_input.text():
            self.zhichen_input.setStyleSheet(main_style.input_box_s())

        if type(stu.zdls.values[0]) == str:
            zdls = stu.zdls.values[0].split(',')
            self.zdls_sig.setText('指导老师已选择:' + str(len(zdls)))
            self.controller.zdls = zdls
            # print('contro.zdls', zdls)

        if type(stu.xzzz.values[0]) == str:
            xzzz = stu.xzzz.values[0].split(',')
            # print('xzzz',xzzz)
            self.xzzz_sig.setText('小组组长已选择:' + str(len(xzzz)))
            self.controller.xzzz = xzzz

        if type(stu.xzcy.values[0]) == str:
            xzcy = stu.xzcy.values[0].split(',')
            self.xzcy_sig.setText('小组成员已选择:' + str(len(xzcy)))
            self.controller.xzcy = xzcy

        for index, row in stu_table.iterrows():
            item = str(index) + ':' + str(row.stu_name)
            self.choice_stu.addItem(item)

    def init_mode(self):
        if glv.get('mode') == 'teacher':
            self.radioButton.setChecked(True)
            self.radioButton.setEnabled(False)
            self.radioButton_2.setChecked(False)
            self.radioButton_2.setEnabled(False)
            self.controller.teacher_mode()
        elif glv.get('mode') == 'student':
            self.radioButton.setChecked(False)
            self.radioButton_2.setChecked(True)
            self.radioButton.setEnabled(False)
            self.radioButton_2.setEnabled(False)
            self.controller.student_mode()
        else:
            self.radioButton.setChecked(True)
            self.radioButton_2.setChecked(False)


    # def show_web(self):
    #     window = login_teacher.WebView()
    #     window.resize(1440, 720)
    #     window.setMinimumWidth(800)
    #     window.setWindowTitle('登录')
    #     window.setWindowIcon(QIcon(window.get_resource_path(login_teacher.icon_path + "ico.png")))
    #     window.show()
        # window.setWindowState(Qt.WindowModal)
        # window.setWindowState(Qt.WindowMinimized)
        # window.setWindowFlags(Qt.Popup)
        #window.update_db.connect(self.update_inform)

    def import_excel(self):
        self.excel_window=excelImport.excel_ui()
        self.excel_window.show()
        self.excel_window.import_confirmed.connect(lambda:dbutils.batch_import(self.excel_window.file_path,self.controller.student_operate))
        self.controller.student_operate.import_complete.connect(self.update_inform)

    def update_inform(self):
        # print('释放信号')
        self.init()

    def resizeEvent(self, event):
        if self.width() < 600:
            pass
            #self.Image.hide()
        else:
            pass
            #self.Image.show()

    def show_reg_ui(self):
        reg = reg_ui()
        reg.show()
        reg.update_db.connect(self.init)

    def bind(self):
        self.choice_tem_out_path.clicked.connect(self.controller.choiceOut)
        self.run_button.clicked.connect(self.controller.run)
        self.choice_stu.activated.connect(
            lambda:self.controller.choice_stu(self.choice_stu.currentText())
        )
        self.choice_stu.activated.connect(
            lambda: self.update_css()
        )
        self.template_generation.triggered.connect(lambda:self.main_widget.setCurrentIndex(0))
        self.signature_fill.triggered.connect(lambda:self.main_widget.setCurrentIndex(1))
        self.assess.triggered.connect(lambda:self.main_widget.setCurrentIndex(2))
        self.merge.triggered.connect(lambda:self.main_widget.setCurrentIndex(3))
        self.doc_to_docx.triggered.connect(lambda:self.main_widget.setCurrentIndex(4))
        self.choice_sig_path.clicked.connect(self.controller.choice_Sig_file)
        self.run_signature.clicked.connect(self.controller.run_sigature)
        self.zdls_add.clicked.connect(self.controller.choice_zdls_file)
        self.xzzz_add.clicked.connect(self.controller.choice_xzzz_file)
        self.xzcy_add.clicked.connect(self.controller.choice_xzcy_file)
        self.choice_total_file_path.clicked.connect(self.controller.choice_total_file)
        self.choice_output_4.clicked.connect(self.controller.choice_merge_res_path)
        self.run_merge.clicked.connect(self.controller.run_merge)
        self.choice_ass_out_path.clicked.connect(self.controller.choice_ass_out_path)
        self.run_ass.clicked.connect(self.controller.run_ass)
        self.add_stu.triggered.connect(self.show_reg_ui)
        self.add_stu_btn.clicked.connect(self.show_reg_ui)
        #self.login_btn.clicked.connect(self.show_web)
        self.login_btn.clicked.connect(self.import_excel)

        self.pushButton.clicked.connect(self.controller.login2template)
        self.pushButton_2.clicked.connect(self.controller.login2signature)
        self.pushButton_3.clicked.connect(self.controller.login2assess)
        self.pushButton_4.clicked.connect(self.controller.login2merge)

        self.radioButton.toggled.connect(self.controller.teacher_mode)
        self.radioButton_2.toggled.connect(self.controller.student_mode)

        #修改信息
        self.banji_input.editingFinished.connect(lambda:self.update(self.id_input.text(),'banji',self.banji_input.text()))
        self.zhichen_input.editingFinished.connect(lambda:self.update(self.id_input.text(),'zhichen',self.zhichen_input.text()))
        self.name_input.editingFinished.connect(lambda:self.update(self.id_input.text(),'stu_name',self.name_input.text()))
        #self.major_input.editingFinished.connect(lambda:self.update(self.id_input.text(),'major',self.major_input.text()))
        self.teacher_input.editingFinished.connect(lambda:self.update(self.id_input.text(),'teacher',self.teacher_input.text()))
        #self.academy_input.editingFinished.connect(lambda:self.update(self.id_input.text(),'academy',self.academy_input.text()))
        self.grade_input.editingFinished.connect(lambda:self.update(self.id_input.text(),'grade',self.grade_input.text()))
        self.title_input.editingFinished.connect(lambda:self.update(self.id_input.text(),'title',self.title_input.text()))
        self.major_select.currentTextChanged.connect(self.controller.update_school_and_major)

        #update score sect1 9 parts
        self.com_1_1.editingFinished.connect(lambda:self.update_proposal(self.id_input.text(),'com_1_1',self.com_1_1.text()))
        self.com_1_2.editingFinished.connect(lambda:self.update_proposal(self.id_input.text(),'com_1_2',self.com_1_2.text()))
        self.com_1_3.editingFinished.connect(lambda:self.update_proposal(self.id_input.text(),'com_1_3',self.com_1_3.text()))
        self.com_1_4.editingFinished.connect(lambda:self.update_proposal(self.id_input.text(),'com_1_4',self.com_1_4.text()))
        self.com_1_5.editingFinished.connect(lambda:self.update_proposal(self.id_input.text(),'com_1_5',self.com_1_5.text()))
        self.com_1_6.editingFinished.connect(lambda:self.update_proposal(self.id_input.text(),'com_1_6',self.com_1_6.text()))
        self.com_1_7.editingFinished.connect(lambda:self.update_proposal(self.id_input.text(),'com_1_7',self.com_1_7.text()))
        self.com_1_8.editingFinished.connect(lambda:self.update_proposal(self.id_input.text(),'com_1_8',self.com_1_8.text()))
        self.com_1_9.editingFinished.connect(lambda:self.update_proposal(self.id_input.text(),'com_1_9',self.com_1_9.text()))
        #update score sect2 8 parts
        self.com_2_1.editingFinished.connect(lambda:self.update_midterm(self.id_input.text(),'com_2_1',self.com_2_1.text()))
        self.com_2_2.editingFinished.connect(lambda:self.update_midterm(self.id_input.text(),'com_2_2',self.com_2_2.text()))
        self.com_2_3.editingFinished.connect(lambda:self.update_midterm(self.id_input.text(),'com_2_3',self.com_2_3.text()))
        self.com_2_4.editingFinished.connect(lambda:self.update_midterm(self.id_input.text(),'com_2_4',self.com_2_4.text()))
        self.com_2_5.editingFinished.connect(lambda:self.update_midterm(self.id_input.text(),'com_2_5',self.com_2_5.text()))
        self.com_2_6.editingFinished.connect(lambda:self.update_midterm(self.id_input.text(),'com_2_6',self.com_2_6.text()))
        self.com_2_7.editingFinished.connect(lambda:self.update_midterm(self.id_input.text(),'com_2_7',self.com_2_7.text()))
        self.com_2_8.editingFinished.connect(lambda:self.update_midterm(self.id_input.text(),'com_2_8',self.com_2_8.text()))
        #update score sect3 10 parts
        self.com_3_1.editingFinished.connect(lambda:self.update_defense(self.id_input.text(),'com_3_1',self.com_3_1.text()))
        self.com_3_2.editingFinished.connect(lambda:self.update_defense(self.id_input.text(),'com_3_2',self.com_3_2.text()))
        self.com_3_3.editingFinished.connect(lambda:self.update_defense(self.id_input.text(),'com_3_3',self.com_3_3.text()))
        self.com_3_4.editingFinished.connect(lambda:self.update_defense(self.id_input.text(),'com_3_4',self.com_3_4.text()))
        self.com_3_5.editingFinished.connect(lambda:self.update_defense(self.id_input.text(),'com_3_5',self.com_3_5.text()))
        self.com_3_6.editingFinished.connect(lambda:self.update_defense(self.id_input.text(),'com_3_6',self.com_3_6.text()))
        self.com_3_7.editingFinished.connect(lambda:self.update_defense(self.id_input.text(),'com_3_7',self.com_3_7.text()))
        self.com_3_8.editingFinished.connect(lambda:self.update_defense(self.id_input.text(),'com_3_8',self.com_3_8.text()))
        self.com_3_9.editingFinished.connect(lambda:self.update_defense(self.id_input.text(),'com_3_9',self.com_3_9.text()))
        self.com_3_10.editingFinished.connect(lambda:self.update_defense(self.id_input.text(),'com_3_10',self.com_3_10.text()))

    def update(self,id,attribute,data):
        if  '?' in self.banji_input.text():
            self.banji_input.setStyleSheet(main_style.input_box_s())
        else:
            self.banji_input.setStyleSheet(main_style.input_box())

        if  '职称' in self.zhichen_input.text():
            self.zhichen_input.setStyleSheet(main_style.input_box_s())
        else:
            self.zhichen_input.setStyleSheet(main_style.input_box())

        self.controller.update_db(id, attribute, data)

    def update_proposal(self,id,attribute,data):
        self.controller.student_operate.proposal(id,attribute,data)

    def update_midterm(self,id,attribute,data):
        self.controller.student_operate.midterm(id,attribute,data)

    def update_defense(self,id,attribute,data):
        self.controller.student_operate.defense(id,attribute,data)

    def update_css(self):
        if '?' in self.banji_input.text():
            self.banji_input.setStyleSheet(main_style.input_box_s())
        else:
            self.banji_input.setStyleSheet(main_style.input_box())

        if '职称' in self.zhichen_input.text():
            self.zhichen_input.setStyleSheet(main_style.input_box_s())
        else:
            self.zhichen_input.setStyleSheet(main_style.input_box())

def main(args=None):
    glv.set('debug', False)
    glv.set('mode', 'full')
    if args is None:
        args = sys.argv[1:]
    for arg in args:
        if arg == 'debug':
            glv.set('debug', True)
        elif arg == 'student':
            glv.set('mode', 'student')
        elif arg == 'teacher':
            glv.set('mode', 'teacher')
        elif arg == 'full':
            glv.set('mode', 'full')

    v_compare = QtCore.QVersionNumber(5, 6, 0)
    v_current = QtCore.QVersionNumber.fromString(QtCore.QT_VERSION_STR)[0]
    if QtCore.QVersionNumber.compare(v_current, v_compare) >= 0:
        # 适应高DPI设备
        QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
        app = QApplication(sys.argv)
    else:
        app = QApplication(sys.argv)

    fc = main_ui()
    fc.show()
    fc.init()

    sys.exit(app.exec_())
if __name__ == '__main__':
    main()

