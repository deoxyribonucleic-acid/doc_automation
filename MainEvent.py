from os import path, remove, mkdir, getcwd, rmdir, walk
import sys
from re import findall
from shutil import copyfile

from PyQt5.QtWidgets import QFileDialog, QMessageBox
import tools.db_operate
from tools.Template import Template
from tools.assess import assess
from tools.merge import merge
from tools.signature import signature_fill
from tools.doc2docx import doc_to_docx
from tools.db_operate import dbutils
from pandas import read_excel
from tools.FileManager import getPath
class Event:
    zdls=[]
    xzzz=[]
    xzcy=[]
    merge_total_path=''


    def __init__(self,parent):
        self.parent=parent
        self.student_operate=tools.db_operate.student()


#模板生成
    def read_all_student(self):
        # pr'执行查看')
        return self.student_operate.read_all_items()

    def choice_stu(self,stu_name):
        # print('选择学生',stu_name)
        find_id=findall("\d+", stu_name)[0]
        stu=self.student_operate.find_item(find_id)
        self.parent.name_input.setText(str(stu.stu_name))
        self.parent.id_input.setText(str(stu.name))
        self.parent.school_select.setCurrentText(str(stu.academy))
        self.parent.major_select.setCurrentText(str(stu.major))
        self.parent.grade_input.setText(str(stu.grade))
        self.parent.banji_input.setText(str(stu.banji))
        self.parent.title_input.setText(str(stu.title))
        self.parent.teacher_input.setText(str(stu.teacher))
        self.parent.zhichen_input.setText(str(stu.zhichen))

        self.parent.com_1_1.setText(str(stu.com_1_1))
        self.parent.com_1_2.setText(str(stu.com_1_2))
        self.parent.com_1_3.setText(str(stu.com_1_3))
        self.parent.com_1_4.setText(str(stu.com_1_4))
        self.parent.com_1_5.setText(str(stu.com_1_5))
        self.parent.com_1_6.setText(str(stu.com_1_6))
        self.parent.com_1_7.setText(str(stu.com_1_7))
        self.parent.com_1_8.setText(str(stu.com_1_8))
        self.parent.com_1_9.setText(str(stu.com_1_9))
        self.parent.com_2_1.setText(str(stu.com_2_1))
        self.parent.com_2_2.setText(str(stu.com_2_2))
        self.parent.com_2_3.setText(str(stu.com_2_3))
        self.parent.com_2_4.setText(str(stu.com_2_4))
        self.parent.com_2_5.setText(str(stu.com_2_5))
        self.parent.com_2_6.setText(str(stu.com_2_6))
        self.parent.com_2_7.setText(str(stu.com_2_7))
        self.parent.com_2_8.setText(str(stu.com_2_8))
        self.parent.com_3_1.setText(str(stu.com_3_1))
        self.parent.com_3_2.setText(str(stu.com_3_2))
        self.parent.com_3_3.setText(str(stu.com_3_3))
        self.parent.com_3_4.setText(str(stu.com_3_4))
        self.parent.com_3_5.setText(str(stu.com_3_5))
        self.parent.com_3_6.setText(str(stu.com_3_6))
        self.parent.com_3_7.setText(str(stu.com_3_7))
        self.parent.com_3_8.setText(str(stu.com_3_8))
        self.parent.com_3_9.setText(str(stu.com_3_9))
        self.parent.com_3_10.setText(str(stu.com_3_10))

        if type(stu.zdls)==str:
            self.zdls=stu.zdls.split(',')
            self.parent.zdls_sig.setText('指导老师已选择:' + str(len(self.zdls)))
        else:
            self.parent.zdls_sig.setText('指导老师电子签名')

        if type(stu.xzzz)==str:
            self.xzzz=stu.xzzz.split(',')
            self.parent.xzzz_sig.setText('小组组长已选择:' + str(len(self.xzzz)))
        else:
            self.parent.xzzz_sig.setText('小组组长电子签名')

        if type(stu.xzcy)==str:
            self.xzcy=stu.xzcy.split(',')
            self.parent.xzcy_sig.setText('小组成员已选择:' + str(len(self.xzcy)))
        else:
            self.parent.xzcy_sig.setText('小组成员电子签名')
    
    def choose_and_import(self):
        file=QFileDialog.getOpenFileName(None, '选择文件', getcwd(), 'Excel files(*.xlsx , *.xls)')
        input_path = file[0]
        dbutils.batch_import(input_path,self.student_operate)


    def choiceOut(self):
        path=QFileDialog.getExistingDirectory(self.parent,'打开',getcwd())
        if path:
            self.parent.output_input.setText(path)
            # prpath)


    def run(self):
        stu_data={
            "ID": self.parent.id_input.text(),
            "name": self.parent.name_input.text(),
            "academy": self.parent.school_select.currentText(),
            "major": self.parent.major_select.currentText(),
            "grade": self.parent.grade_input.text(),
            "banji": self.parent.banji_input.text(),
            "title": self.parent.title_input.text(),
            "teacher": self.parent.teacher_input.text(),
            "zhichen": self.parent.zhichen_input.text(),
        }
        save_path=self.parent.output_input.text()+'/'
        try:
            # print('保存路径',save_path)
            if not save_path == '/':
                Template(save_path,stu_data)
                QMessageBox.about(self.parent, "success", "生成成功!")
            else:
                QMessageBox.about(self.parent, "error", "请先选择生成目录")
        except:
            QMessageBox.about(self.parent, "error", "检测到文件{}正被占用，请结束word、wps进程后重试".format(save_path))


    # 填充签名
    def choice_zdls_file(self):
        # print('执行了选择指导老师')
        total_path = QFileDialog.getOpenFileNames(self.parent, '选择图片文件', getcwd(), '图片文件(*.jpg *png)"')[0]
        self.zdls = total_path
        sig_dir=getcwd()+'/signature/'+self.parent.name_input.text()
        if not path.exists(sig_dir):
            mkdir(sig_dir)
        sig_path=''
        index=1
        for img in self.zdls:
            save_path=sig_dir+'/'+self.parent.name_input.text()+'-指导老师'+str(index)+'.png'
            # print(save_path)
            sig_path =sig_path+','+save_path
            index=index+1
            copyfile(img,save_path)
        sig_path=sig_path[1:]
        self.student_operate.add_sig_infrom(self.parent.id_input.text(),'zdls',sig_path)


        # print(self.zdls)
        count = len(total_path)
        text = self.parent.zdls_sig.text()
        if total_path:
            new_text = '指导老师' + '已选择' + str(count)
            self.parent.zdls_sig.setText(new_text)

    def choice_xzzz_file(self):
        total_path = QFileDialog.getOpenFileNames(self.parent, '选择图片文件', getcwd(), '图片文件(*.jpg *png)"')[0]
        self.xzzz = total_path
        sig_dir = getcwd() + '/signature/' + self.parent.name_input.text()
        if not path.exists(sig_dir):
            mkdir(sig_dir)
        sig_path = ''
        index = 1
        for img in self.xzzz:
            save_path=sig_dir+'/'+self.parent.name_input.text()+'-小组组长'+str(index)+'.png'
            sig_path = sig_path + ',' + save_path
            index = index + 1
            copyfile(img,save_path)
        sig_path = sig_path[1:]
        self.student_operate.add_sig_infrom(self.parent.id_input.text(), 'xzzz', sig_path)

        # print(self.xzzz)
        count = len(total_path)
        text = self.parent.xzzz_sig.text()
        if total_path:
            new_text = '小组组长' + '已选择' + str(count)
            self.parent.xzzz_sig.setText(new_text)

    def choice_xzcy_file(self):
        total_path = QFileDialog.getOpenFileNames(self.parent, '选择图片文件', getcwd(), '图片文件(*.jpg *png)"')[0]
        self.xzcy = total_path
        sig_dir = getcwd() + '/signature/' + self.parent.name_input.text()
        if not path.exists(sig_dir):
            mkdir(sig_dir)
        sig_path = ''
        index = 1
        for img in self.xzcy:
            save_path=sig_dir+'/'+self.parent.name_input.text()+'-小组成员'+str(index)+'.png'
            sig_path = sig_path + ',' + save_path
            index = index + 1
            copyfile(img, save_path)
        sig_path = sig_path[1:]
        self.student_operate.add_sig_infrom(self.parent.id_input.text(), 'xzcy', sig_path)

        # print(self.xzcy)
        count = len(total_path)
        text = self.parent.xzcy_sig.text()
        if total_path:
            new_text = '小组成员' + '已选择' + str(count)
            self.parent.xzcy_sig.setText(new_text)

    def choice_Sig_file(self):
        total_path = QFileDialog.getOpenFileNames(self.parent, '选择word文件', getcwd(), 'Word文件(*docx *doc)"')
        self.parent.sig_file_list.clear()
        for path in total_path[0]:
            self.parent.sig_file_list.addItem(path)

    def run_sigature(self):
        list = self.parent.sig_file_list
        if not list.count()==0:
            i = 0
            try:
                while i < list.count():
                    path=list.item(i).text()
                    path=doc_to_docx(path)
                    signature_fill(path, self.zdls, self.xzzz, self.xzcy)
                    i = i + 1
                QMessageBox.about(self.parent, "success", "签名填充成功!")
            except:
                QMessageBox.about(self.parent, "error", "检测到文件正被占用，请结束word、wps进程后重试")

        else :
            QMessageBox.about(self.parent, "error", "请先选择待填充文件")

    #快速评审
    def choice_ass_out_path(self):
        path=QFileDialog.getExistingDirectory(self.parent, '打开', getcwd())
        if path:
            self.parent.ass_out_path.setText(path)

    def run_ass(self):
        index=self.parent.tabWidget.currentIndex()
        stu_data={
            "ID": self.parent.id_input.text(),
            "name": self.parent.name_input.text(),
            "academy": self.parent.school_select.currentText(),
            "major": self.parent.major_select.currentText(),
            "grade": self.parent.grade_input.text(),
            "banji": self.parent.banji_input.text(),

            "title": self.parent.title_input.text(),
            "teacher": self.parent.teacher_input.text(),
            "zhichen": self.parent.zhichen_input.text(),
        }
        ass={}
        if index == 0:
            ass = {
                "one": self.parent.com_1_1.text(),
                "two": self.parent.com_1_2.text(),
                "three": self.parent.com_1_3.text(),
                "four": self.parent.com_1_4.text(),
                "five": self.parent.com_1_5.text(),
                "six": self.parent.com_1_6.text(),
                "seven": self.parent.com_1_7.text(),
                "eight": self.parent.com_1_8.text(),
                "nine": self.parent.com_1_9.text(),
            }
        
        elif index == 1:
            ass = {
                "one": self.parent.com_2_1.text(),
                "two": self.parent.com_2_2.text(),
                "three": self.parent.com_2_3.text(),
                "four": self.parent.com_2_4.text(),
                "five": self.parent.com_2_5.text(),
                "six": self.parent.com_2_6.text(),
                "seven": self.parent.com_2_7.text(),
                "eight": self.parent.com_2_8.text(),
            }
            
        elif index == 2:
            ass = {
                "one": self.parent.com_3_1.text(),
                "two": self.parent.com_3_2.text(),
                "three": self.parent.com_3_3.text(),
                "four": self.parent.com_3_4.text(),
                "five": self.parent.com_3_5.text(),
                # "six": self.parent.com_3_6.text(),
                # "seven": self.parent.com_3_7.text(),
                # "eight": self.parent.com_3_8.text(),
                # "nine":self.parent.com_3_9.text(),
                # "ten":self.parent.com_3_10.text(),
            }

        total = 0
        try:
            for item in ass.values():
                total = int(total) + int(item)
            ass.update({'total': total})
            stu_data.update(ass)
            # print(stu_data)
            #TODO 校验一下成绩再生成
            # print('MainEvent.py 尝试导出', self.parent.ass_out_path.text())
            if not self.parent.ass_out_path.text()=='':
                try:
                    res_path = assess(index, self.parent.ass_out_path.text(), stu_data)
                    signature_fill(res_path, self.zdls, self.xzzz, self.xzcy)
                    QMessageBox.about(self.parent, "success", "生成成功!")
                except:
                    QMessageBox.about(self.parent, "error", "检测到文件正被占用，请结束word、wps进程后重试")
            else:
                QMessageBox.about(self.parent, "error", "请先选择输出目录")

        except:
            QMessageBox.about(self.parent, "error", "请先完善评分信息")

    #合并文件
    def choice_total_file(self):
        merge_total_path = QFileDialog.getOpenFileNames(self.parent, '选择word文件', getcwd(),'Word文件(*pdf *docx *doc)"')
        self.merge_total_path = merge_total_path[0]
        self.parent.merge_file_list.clear()
        for path in merge_total_path[0]:
            # prpath)
            self.parent.merge_file_list.addItem(path)

        string='选择dox/docx/pdf文件:'+'已选择'+str(len(self.merge_total_path))+'--应有'+'13'
        self.parent.output_label_4.setText(string)

    def choice_merge_res_path(self):
        res_path=QFileDialog.getExistingDirectory(self.parent, '打开', getcwd())
        if res_path:
            self.parent.output_input_4.setText(res_path)

    def run_merge(self):
        file_path=self.merge_total_path
        res_path=self.parent.output_input_4.text()
        name=self.parent.name_input.text()
        if not  res_path== '':
            if not file_path =='':
                try:
                    merge(name, file_path, res_path)
                    QMessageBox.about(self.parent, "success", "合并成功!")
                    self.parent.run_merge.setText('生成')

                except:
                    QMessageBox.about(self.parent, "error", "检测到文件正被占用，请结束word、wps进程后重试")

            else:
                QMessageBox.about(self.parent, "error", "请先选择待合并文件")

        else:
            QMessageBox.about(self.parent, "error", "请先选择生成目录")

    def del_temp(self):
        dir_path=sys.argv[0]+'/temp_pdf'
        for root, dirs, files in walk(dir_path, topdown=False):
            # print(root)  # 各级文件夹绝对路径
            # print(dirs)  # root下一级文件夹名称列表，如 ['文件夹1','文件夹2']
            # print(files)  # root下文件名列表，如 ['文件1','文件2']
            # 第一步：删除文件
            for name in files:
                remove(path.join(root, name))  # 删除文件
            # 第二步：删除空文件夹
            for name in dirs:
                rmdir(path.join(root, name))  # 删除一个空目录

    def update_db(self,id,attribute,data):
        if self.student_operate.updata_item(id,attribute,data):
            # print('{}更新{}为{}'.format(id,attribute,data))
            pass
        else:
            # print('校验不通过，更新失败')
            pass
              
    def setup_combobox(self):
        self.major_db=read_excel(getPath("database/majors.xlsx"))
        school_list=self.major_db.columns.values.tolist()
        for school in school_list:
            self.parent.school_select.addItem(school)
        self.setup_major()
        self.parent.school_select.currentIndexChanged.connect(self.setup_major)
    def setup_major(self):
        school=self.parent.school_select.currentText()
        major_list=self.major_db[school].dropna().values.tolist()
        self.parent.major_select.clear()
        for major in major_list:
            self.parent.major_select.addItem(major)
        #self.parent.major_select.currentIndexChanged.connect(self.update_school_and_major)

    def update_school_and_major(self):
        self.parent.update(self.parent.id_input.text(),'major',self.parent.major_select.currentText())
        self.parent.update(self.parent.id_input.text(),'academy',self.parent.school_select.currentText())

    def login2template(self):
        self.parent.stackedWidget.setCurrentIndex(0)
        self.parent.main_widget.setCurrentIndex(0)
        self.parent.toolBar.show()
        self.parent.doc_to_docx.setVisible(False)

    def login2signature(self):
        self.parent.stackedWidget.setCurrentIndex(0)
        self.parent.main_widget.setCurrentIndex(1)
        self.parent.toolBar.show()
        self.parent.doc_to_docx.setVisible(False)

    def login2assess(self):
        self.parent.stackedWidget.setCurrentIndex(0)
        self.parent.main_widget.setCurrentIndex(2)
        self.parent.toolBar.show()
        self.parent.doc_to_docx.setVisible(False)

    def login2merge(self):
        self.parent.stackedWidget.setCurrentIndex(0)
        self.parent.main_widget.setCurrentIndex(3)
        self.parent.toolBar.show()
        self.parent.doc_to_docx.setVisible(False)

    def student_mode(self):
        # print('学生模式')
        self.parent.pushButton_2.setEnabled(False)
        self.parent.pushButton_3.setEnabled(False)
        self.parent.signature_fill.setVisible(False)
        self.parent.assess.setVisible(False)
        self.parent.doc_to_docx.setVisible(False)

    def teacher_mode(self):
        # print('teacher')
        self.parent.pushButton_2.setEnabled(True)
        self.parent.pushButton_3.setEnabled(True)
        self.parent.signature_fill.setVisible(True)
        self.parent.assess.setVisible(True)
        self.parent.doc_to_docx.setVisible(False)
