
from math import nan
import os

import pandas as pd
from PyQt5.QtCore import pyqtSignal,QObject
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox, QTableWidgetItem

import re

class student(QObject):
    import_complete = pyqtSignal()
    def __init__(self):
        super(student, self).__init__()
        db_path = os.path.join(os.getcwd(),'database')
        self.table_path = os.path.join(db_path,'student.csv')
        if not os.path.exists(self.table_path):
            table=pd.DataFrame(columns=['ID','stu_name','academy','major','grade','banji','title','teacher','zhichen','zdls','xzzz','xzcy'])
            table.to_csv(self.table_path,encoding='utf-8',index=False)
        self.table=pd.read_csv(self.table_path,index_col='ID')


    def add_item(self,item):
        self.table = pd.read_csv(self.table_path, index_col='ID',encoding='utf-8')
        key=int(item['ID'])
        data=[
        item['stu_name'],
        item['academy'],
        item['major'],
        item['grade'],
        item['banji'],
        item['title'],
        item['teacher'],
        item['zhichen'],
        '',
        '',
        ''
        ]
        #print('key',key)
        #print('data',data)
        self.table.loc[key]=data
        print(self.table)
        self.table.to_csv(self.table_path,index=True,index_label="ID",encoding='utf-8')
        self.table = pd.read_csv(self.table_path, index_col='ID',encoding='utf-8')

    def add_sig_infrom(self,ID,case,path):
        ID=int(ID)
        self.table = pd.read_csv(self.table_path, index_col='ID',encoding='utf-8')
        if case == 'zdls':
            self.table.loc[ID,'zdls']=path
            print('path',self.table.loc[ID,'zdls'])
            self.table.to_csv(self.table_path, index=True, index_label="ID",encoding='utf-8')

        if case == 'xzzz':
            self.table.loc[ID,'xzzz']=path
            print('path',self.table.loc[ID,'xzzz'])
            self.table.to_csv(self.table_path, index=True, index_label="ID",encoding='utf-8')

        if case == 'xzcy':
            self.table.loc[ID,'xzcy']=path
            print('path',self.table.loc[ID,'xzcy'])
            self.table.to_csv(self.table_path, index=True, index_label="ID",encoding='utf-8')

    def read_all_items(self):
        self.table = pd.read_csv(self.table_path, index_col='ID',encoding='utf-8')
        print(self.table)
        return self.table

    def find_item(self,ID):
        ID=int(ID)
        self.table = pd.read_csv(self.table_path, index_col='ID',encoding='utf-8')
        try:
            print('学生',self.table.loc[ID])
            return self.table.loc[ID]
        except:
            print('没找到')
            return -1

    def updata_item(self,ID,attribute,data):
        result,msg = self.verify_item(attribute,data)
        if not result:
            QMessageBox.warning(QApplication.activeWindow(), "提示", msg)
            return False
        ID=int(ID)
        self.table = pd.read_csv(self.table_path, index_col='ID',encoding='utf-8')
        self.table.loc[ID, attribute] = data
        self.table.to_csv(self.table_path,index=True,index_label="ID",encoding='utf-8')
        return True

    def verify_item(self,attribute,data):
        re_list={
            'ID':r'^\d{13}$',
            'stu_name':r'^[\u4e00-\u9fa5_a-zA-Z•]+$',
            'academy':r'^[\s\S]*$',
            'major':r'^[\s\S]*$',
            'grade':r'^[\u4e00-\u9fa5_a-zA-Z0-9（）()]+$',
            'banji':r'^[\u4e00-\u9fa5_a-zA-Z0-9（）()]+$',
            'title':r'^[\u4e00-\u9fa5_a-zA-Z0-9，。、？！：；“”（）《》【】(),.?!]+$',
            'teacher':r'^[\u4e00-\u9fa5_a-zA-Z•]+$',
            'zhichen':r'^[\u4e00-\u9fa5_a-zA-Z•]+$',
            #zdls xzzz xzcy may contain every kind of character
            'zdls':r'^[\s\S]*$',
            'xzzz':r'^[\s\S]*$',
            'xzcy':r'^[\s\S]*$'
        }
        key_chinese = {
            'ID':'学号',
            'stu_name':'学生姓名',
            'academy':'学院',
            'major':'专业',
            'grade':'年级',
            'banji':'班级',
            'title':'毕设标题',
            'teacher':'指导教师',
            'zhichen':'指导教师职称'
        }
        if not re.match(re_list[attribute],data):
            status = False
            msg = "{}格式错误:{}".format(key_chinese[attribute],data)
            return status,msg
        else:
            status = True
            msg = ''
            return status,msg


class dbutils:
    @staticmethod
    def batch_import(input_path,db_obj=student()):
        #先检测整个table，确保数据无误再输入，若有误直接弹出报错窗口
        data = pd.DataFrame(pd.read_excel(input_path))
        if sum(data.duplicated('学号',keep=False)) > 0:
             
             dst=data[data.duplicated('学号',keep=False)]
             print(dst)
             dst=dst[['学号','学生姓名']]
             print(dst)
             dst=dst.to_string()
             print(dst)
             QMessageBox.information(QApplication.activeWindow(), "错误", "数据中存在重复学号\n{}".format(dst))
        else:
            key_attributes = [
            'ID',
            'stu_name',
            'academy',
            'major',
            'grade',
            'banji',
            'title',
            'teacher',
            'zhichen'
            ]
            table = pd.read_excel(input_path)
            table1 = table.values
            table1 = table1.tolist()
            #print(table)
            final_msg=""
            final_result=True
            for idx_line,line in enumerate(table1):
                #print(line)
                
                for idx,value in enumerate(line):
                    if idx==0:
                        value=str(value)
                    result, msg=db_obj.verify_item(key_attributes[idx],value)
                    if result == False: 
                        #print("位置：{}行{}列".format(idx_line+1,idx+1),msg)
                        final_msg+="位置：{}行{}列".format(idx_line+1,idx+1)+msg+"\n"
                        final_result=False
            print(final_msg)
            if final_result == False:
                final_msg+="\n请导入格式正确的文件！"
                QMessageBox.information(QApplication.activeWindow(), "错误", final_msg)
                return 
            for i in table.index.values.tolist():
                item = table.loc[i]
                #print(item)
                db_obj.add_item(dbutils.transfer_item(item))
            db_obj.import_complete.emit()
            QMessageBox.information(QApplication.activeWindow(), "提示", "导入成功！")


    @staticmethod
    def transfer_item(item):
        t_item = {
            'ID':item['学号'],
            'stu_name':item['学生姓名'],
            'academy':item['学院'],
            'major':item['专业'],
            'grade':item['年级'],
            'banji':item['班级'],
            'title':item['毕设标题'],
            'teacher':item['指导教师'],
            'zhichen':item['指导教师职称'],
        }
        #print(t_item)
        return t_item
    
    @staticmethod
    def verify_item(db:student,item):
        result = True
        err_msg = ''
        key_chinese = {
            'ID':'学号',
            'stu_name':'学生姓名',
            'academy':'学院',
            'major':'专业',
            'grade':'年级',
            'banji':'班级',
            'title':'毕设标题',
            'teacher':'指导教师',
            'zhichen':'指导教师职称'
        }
        # detect id conflict
        print(db.table.index)
    
        if item['ID'] is not None and item['ID'] != '':
            if db.table.index.isin([int(item['ID'])]).any():
                result = False
                err_msg = '学号{}已存在'.format(item['ID'])

        for key,value in item.items():
            if not value or value == '':
                result = False
                err_msg = '{}不能为空'.format(key_chinese[key])
                break
            #id contains 13 number
            elif key == 'ID':
                if not re.match(r'^\d{13}$',value):
                    result = False
                    err_msg = '{}格式错误'.format(key_chinese[key])
                    break
            elif key == 'title':
                if not re.match(r'^[\u4e00-\u9fa5_a-zA-Z0-9，。、？！：；“”（）《》【】(),.?!]+$',value):
                    result = False
                    err_msg = '{}存在非法字符'.format(key_chinese[key])
                    break
            elif key == 'stu_name' or key == 'teacher' or key == 'zhichen':
                if not re.match(r'^[\u4e00-\u9fa5_a-zA-Z•]+$',value):
                    result = False
                    err_msg = '{}格式错误'.format(key_chinese[key])
                    break
            else:
                if not re.match(r'^[\u4e00-\u9fa5_a-zA-Z0-9（）()]+$',value):
                    result = False
                    err_msg = '{}格式错误'.format(key_chinese[key])
                    break
        return result,err_msg
    
if __name__=="__main__":
    dbutils.batch_import(os.path.join(os.getcwd(),'database','import.xlsx'))