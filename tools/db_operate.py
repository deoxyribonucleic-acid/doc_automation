import os

import pandas as pd
from numpy import nan
from PyQt5.QtCore import pyqtSignal,QObject
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox, QTableWidgetItem
from tools.FileManager import getPath

import re

class student(QObject):
    import_complete = pyqtSignal()
    def __init__(self):
        super(student, self).__init__()
        
        self.table_path = getPath('database/student.csv')
        if not os.path.exists(getPath('database')):
            os.mkdir(getPath('database'))
        if not os.path.exists(self.table_path):
            table=pd.DataFrame(columns=['ID','stu_name','academy','major','grade','banji','title','teacher','zhichen','zdls','xzzz','xzcy',
            'com_1_1','com_1_2','com_1_3','com_1_4','com_1_5','com_1_6','com_1_7','com_1_8','com_1_9',
            'com_2_1','com_2_2','com_2_3','com_2_4','com_2_5','com_2_6','com_2_7','com_2_8',
            'com_3_1','com_3_2','com_3_3','com_3_4','com_3_5','com_3_6','com_3_7','com_3_8','com_3_9','com_3_10'
                                        ])
            table.to_csv(self.table_path,encoding='utf-8',index=False)
        self.table=pd.read_csv(self.table_path,index_col='ID',dtype=str)
        self.table.replace(nan, '')


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
        '',
        
        '0',
        '0',
        '0',
        '0',
        '0',
        '0',
        '0',
        '0',
        '0',

        '0',
        '0',
        '0',
        '0',
        '0',
        '0',
        '0',
        '0',
        '0',

        '0',
        '0',
        '0',
        '0',
        '0',
        '0',
        '0',
        '0',
        '0',
        ]
        # print('key',key)
        # print('data',data)
        self.table.loc[key]=data
        # print(self.table)
        self.table.to_csv(self.table_path,index=True,index_label="ID",encoding='utf-8')
        self.table = pd.read_csv(self.table_path, index_col='ID',encoding='utf-8')

    def add_sig_infrom(self,ID,case,path):
        ID=int(ID)
        self.table = pd.read_csv(self.table_path, index_col='ID',encoding='utf-8')
        if case == 'zdls':
            self.table.loc[ID,'zdls']=path
            # print('path',self.table.loc[ID,'zdls'])
            self.table.to_csv(self.table_path, index=True, index_label="ID",encoding='utf-8')

        if case == 'xzzz':
            self.table.loc[ID,'xzzz']=path
            # print('path',self.table.loc[ID,'xzzz'])
            self.table.to_csv(self.table_path, index=True, index_label="ID",encoding='utf-8')

        if case == 'xzcy':
            self.table.loc[ID,'xzcy']=path
            # print('path',self.table.loc[ID,'xzcy'])
            self.table.to_csv(self.table_path, index=True, index_label="ID",encoding='utf-8')

    def read_all_items(self):
        self.table = pd.read_csv(self.table_path, index_col='ID',encoding='utf-8`',dtype=str)
        # print(self.table)
        return self.table

    def find_item(self,ID):
        ID=int(ID)
        self.table = pd.read_csv(self.table_path, index_col='ID',encoding='utf-8')
        try:
            # print('学生',self.table.loc[ID])
            return self.table.loc[ID]
        except:
            # print('没找到')
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
        return result
    
    def update_score(self,ID,attribute,score):
        result,msg = self.verify_score(attribute,score)
        if not result:
            QMessageBox.warning(QApplication.activeWindow(), "提示", msg)
            return False
        # scores currently not in database
        # TODO: add score to database
        return result

    @staticmethod
    def verify_item(attribute,data):
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
            'xzcy':r'^[\s\S]*$',
            #sect 1 contains 9 parts part3&4 range from 0-15, part1&2&5-9 range from 0-10
            'com_1_1':r'^(10|[0-9])$',
            'com_1_2':r'^(10|[0-9])$',
            'com_1_3':r'^(1[0-5]|[0-9])$',
            'com_1_4':r'^(1[0-5]|[0-9])$',
            'com_1_5':r'^(10|[0-9])$',
            'com_1_6':r'^(10|[0-9])$',
            'com_1_7':r'^(10|[0-9])$',
            'com_1_8':r'^(10|[0-9])$',
            'com_1_9':r'^(10|[0-9])$',
            #sect 2 contains 8 parts part1&2 range from 0-20, part3-8 range from 0-10
            'com_2_1':r'^(2[0]|1[1-9]|[0-9])$',
            'com_2_2':r'^(2[0]|1[1-9]|[0-9])$',
            'com_2_3':r'^(10|[0-9])$',
            'com_2_4':r'^(10|[0-9])$',
            'com_2_5':r'^(10|[0-9])$',
            'com_2_6':r'^(10|[0-9])$',
            'com_2_7':r'^(10|[0-9])$',
            'com_2_8':r'^(10|[0-9])$',
            #sect 3 contains 10 parts, each has range of 0-10
            'com_3_1':r'^(10|[0-9])$',
            'com_3_2':r'^(10|[0-9])$',
            'com_3_3':r'^(10|[0-9])$',
            'com_3_4':r'^(10|[0-9])$',
            'com_3_5':r'^(10|[0-9])$',
            'com_3_6':r'^(10|[0-9])$',
            'com_3_7':r'^(10|[0-9])$',
            'com_3_8':r'^(10|[0-9])$',
            'com_3_9':r'^(10|[0-9])$',
            'com_3_10':r'^(10|[0-9])$',
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
            'zhichen':'指导教师职称',
            'zdls':'指导老师签名',
            'xzzz':'小组组长签名',
            'xzcy':'小组成员签名',
            #sect 1 开题报告评分
            'com_1_1':'1、选题理论和实用性',
            'com_1_2':'2、选题难度和创可行性',
            'com_1_3':'3、研究方法的合理性',
            'com_1_4':'4、开题报告的文字表达,参考文献的引用',
            'com_1_5':'5、资料准备的充分性',
            'com_1_6':'6、对课题的了解程度',
            'com_1_7':'7、基本概念清楚、明确选题的意义',
            'com_1_8':'8、论证严密、逻辑性强',
            'com_1_9':'9、回答问题条理清晰、应答切题',
            #sect 2 中期检查评分
            'com_2_1':'1、已完成的工作量符合进度要求',
            'com_2_2':'2、毕设内容符合课题要求',
            'com_2_3':'3、资料收集充分',
            'com_2_4':'4、对课题内容理解深刻,准确',
            'com_2_5':'5、能清晰把握目前设计情况,对下一步的任务有清楚的认识',
            'com_2_6':'6、学习态度端正,能够在毕设中投入较多时间和精力',
            'com_2_7':'7、课题陈述清晰,逻辑性强',
            'com_2_8':'8、思维缜密,回答问题正确',
            #sect 3 答辩评分
            'com_3_1':'1、论文结构合理,条理清晰,文笔流畅,格式规范',
            'com_3_2':'2、基本概念和基本原理清楚、正确',
            'com_3_3':'3、实验数据真实、结论正确',
            'com_3_4':'4、论文主要内容为本人独立完成',
            'com_3_5':'5、完成了规定的毕设任务',
            'com_3_6':'6、掌握了相关的理论知识和专业技能',
            'com_3_7':'7、具备一定的分析问题和解决问题的能力',
            'com_3_8':'8、学习态度好,能够在毕设中投入较多时间和精力',
            'com_3_9':'9、能够简明扼要、重点突出地阐述论文的主要内容',
            'com_3_10':'10、能够准确、流利地回答评审老师提出的问题',
        }
        if not re.match(re_list[attribute],data):
            status = False
            msg = "项目“{}”格式错误:{}".format(key_chinese[attribute],data)
            return status,msg
        else:
            status = True
            msg = ''
            return status,msg


class dbutils:
    @staticmethod
    def batch_import(input_path,db_obj=student()):
        #先检测整个table，确保数据无误再输入，若有误直接弹出报错窗口
        try:
            data = pd.read_excel(input_path)
        except:
            QMessageBox.warning(QApplication.activeWindow(), "错误", "dbutils.batch_import:文件{}读取失败".format(input_path))
            return False
        if sum(data.duplicated('学号',keep=False)) > 0:
            dst=data[data.duplicated('学号',keep=False)]
            # print(dst)
            dst=dst[['学号','学生姓名']]
            # print(dst)
            dst=dst.to_string()
            # print(dst)
            QMessageBox.information(QApplication.activeWindow(), "错误", "数据中存在重复学号\n{}".format(dst))
            return False
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
            # print(table)
            final_msg=""
            final_result=True
            for idx_line,line in enumerate(table1):
                # print(line)
                
                for idx,value in enumerate(line):
                    if idx==0:
                        value=str(value)
                    result, msg=db_obj.verify_item(key_attributes[idx],value)
                    if result == False: 
                        ## print("位置：{}行{}列".format(idx_line+1,idx+1),msg)
                        final_msg+="位置：{}行{}列".format(idx_line+1,idx+1)+msg+"\n"
                        final_result=False
            # print(final_msg)
            if final_result == False:
                final_msg+="\n请导入格式正确的文件！"
                QMessageBox.information(QApplication.activeWindow(), "错误", final_msg)
                return 
            for i in table.index.values.tolist():
                item = table.loc[i]
                ## print(item)
                db_obj.add_item(dbutils.transfer_item(item))
            db_obj.import_complete.emit()
            QMessageBox.information(QApplication.activeWindow(), "提示", "导入成功！")
            return True

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
        ## print(t_item)
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
        # print(db.table.index)
    
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
    #dbutils.batch_import(os.path.join(os.getcwd(),'database','import.xlsx'))
    # print(student.verify_item('com_1_1','-100'))
    # print(student.verify_item('com_1_1','0'))
    # print(student.verify_item('com_1_1','9'))
    # print(student.verify_item('com_1_1','10'))
    # print(student.verify_item('com_1_1','11'))
    # print(student.verify_item('com_1_1','20'))
    # print(student.verify_item('com_1_1','27'))
    pass
