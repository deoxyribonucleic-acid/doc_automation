import torndb_for_python3 as torndb

from tornado.web import RequestHandler
from tornado.web import Application
from tornado.ioloop import IOLoop
import MySQLdb
import toml
import hashlib
import re
import pymysql
toml_file_path = "backend\config.toml"
data_toml = toml.load(toml_file_path)

def _getConn():
    return MySQLdb.connect(host=data_toml['owner']['host'],user=data_toml['owner']['user'],passwd=data_toml['owner']['passwd'],db=data_toml['owner']['db'],port=data_toml['owner']['port'],charset='utf8',autocommit = 1)

def verify_password(password, hashed_password, salt):
    """验证密码是否正确"""
    # 将输入的密码和盐值合并
    password_with_salt = password + salt

    # 使用相同的哈希算法计算哈希值
    hashed_input_password = hashlib.sha256(password_with_salt.encode()).hexdigest()

    # 比较计算出的哈希值与存储的哈希值是否一致
    return hashed_input_password == hashed_password

class LoginHandler(RequestHandler):
    def initialize(self,conn):
        self.conn = conn

    def post(self, *args, **kwargs):
        #获取请求参数
        pwd = self.get_argument('password')
        uname = self.get_argument('account')
        cursor = self.conn.cursor()
        #使用参数化查询以避免SQL注入攻击
        cursor.execute('SELECT t_pwd, t_salt, t_id FROM t_teacher WHERE t_id=%s', (uname,))
        teacher_info = cursor.fetchone()
        cursor.execute('select s_pwd, s_salt from t_student where s_id=%s', (uname,))
        student_info = cursor.fetchone()
        #判断登录者是老师还是学生
        if student_info:
            s_hashed_password = student_info[0]
            s_salt = student_info[1]
            #判断密码是否正确
            if verify_password(pwd, s_hashed_password, s_salt) == 1:
                cursor.execute('select s_name from t_student where s_id=%s', (uname,))
                s_name = cursor.fetchone()
                print(s_name[0],'同学，欢迎！')
                cursor.execute('select s_id, s_name, s_school, s_major, s_grade, s_class, s_title from t_student where s_id=%s',(uname,))
                stu_info = cursor.fetchone()
                cursor.execute('select s_instructor_id from t_student where s_id=%s',(uname,))
                s_instructor_id = cursor.fetchone()
                cursor.execute('select t_name, t_title from t_teacher where t_id=%s', (s_instructor_id,))
                t_info = cursor.fetchone()
                t_name = t_info[0]
                t_title = t_info[1]
                self.write({"status": "success", "received": s_name[0], "account_type":"student", "stu_info":stu_info,"t_name":t_name,"t_title":t_title})

            else:
                self.write({"status": "error", "message": "Wrong password"})
        elif teacher_info:
            t_hashed_password = teacher_info[0]
            t_salt = teacher_info[1]
            t_id = teacher_info[2]
            if verify_password(pwd, t_hashed_password, t_salt) == 1:
                cursor.execute('select t_name, t_title from t_teacher where t_id=%s', (uname,))
                teacher_info = cursor.fetchone()
                t_title = teacher_info[1]
                t_name = teacher_info[0]
                print(t_name,'老师，欢迎！')
                #获取登录教师名下的所有学生id
                cursor.execute('select s_id, s_name, s_school, s_major, s_grade, s_class, s_title from t_student where s_instructor_id=%s',(t_id,))
                s_id_list = cursor.fetchall()
                
                print(s_id_list)
                self.write({"status": "success", "received": t_name,
                            "account_type":"teacher","stu_list":s_id_list,"t_title":t_title})                
            else:
                self.write({"status": "error", "message": "Wrong password"})
        else:
            self.write({"status": "error", "message": "No user found"})

class ProposalHandler(RequestHandler):
    def initialize(self,conn):
        return
        
    def get(self):
        #自动提交事务
        conn = pymysql.connect(host=data_toml['owner']['host'],user=data_toml['owner']['user'],password=data_toml['owner']['passwd'],database=data_toml['owner']['db'])
        cursor = conn.cursor()
        ID = self.get_argument("ID")
        if len(ID)>0:
            cursor.execute('select * from t_proposal_review where s_id =%s',(ID,))
            proposal_list = cursor.fetchone()
            print("proposal_list:",proposal_list)
            if len(proposal_list) != 10:
                self.write({"status":"error","msg":"分数不全,请联系管理员"})
            else:
                self.write({"status":"success","received":proposal_list})
        else:
            self.write({"status": "error", "message": "No user found"})
        cursor.close()    
    def post(self):
        attribute = self.get_argument("attribute")
        data = self.get_argument("data")
        ID = self.get_argument("ID")
        print('attribute:',attribute,'data:',data,'ID:',ID)
        if len(ID)>0 and len(attribute)>0 and len(data)>0 :
            # 调用更新数据库的函数
            data_float = float(data)
            status, msg = self.verify_item(attribute,data)
            if status == True:
                sql = 'update t_proposal_review set %s="%f" where s_id="%s"'%(attribute,data_float,ID)
                print(sql)
                conn = torndb.Connection(host=data_toml['owner']['host'],user=data_toml['owner']['user'],password=data_toml['owner']['passwd'],database=data_toml['owner']['db'])
                conn.update(sql)
                conn.close()
                self.write({"status": "success", "message": "Data updated successfully"})
            else:
                self.write(msg)
        else:
            self.write({"status": "error", "message": "No data provided"})
            
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
        

class MidtermHandler(RequestHandler):
    def initialize(self,conn):
        self.conn = conn
        self.cursor = self.conn.cursor()
    def get(self):
        ID = self.get_argument("ID")
        if len(ID)>0:
            self.cursor.execute('select * from t_midterm_review where s_id =%s',(ID,))
            midterm_list = self.cursor.fetchone()
            self.conn.commit()
            if len(midterm_list) != 9:
                self.write({"status":"error","msg":"分数不全,请联系管理员"})
            else:
                self.write({"status":"success","received":midterm_list})
        else:
            self.write({"status": "error", "message": "No user found"})

    def post(self):
        attribute = self.get_argument("attribute")
        data = self.get_argument("data")
        ID = self.get_argument("ID")
        if len(ID)>0 and len(attribute)>0 and len(data)>0:
            # 调用更新数据库的函数
            data_float = float(data)
            status, msg = self.verify_item(attribute,data)
            if status == True:
                sql = 'update t_midterm_review set %s="%f" where s_id="%s"'%(attribute,data_float,ID)
                conn = torndb.Connection(host=data_toml['owner']['host'],user=data_toml['owner']['user'],password=data_toml['owner']['passwd'],database=data_toml['owner']['db'])
                conn.update(sql)
                conn.close()
                self.write({"status": "success", "message": "Data updated successfully"})
            else:
                self.write(msg)
        else:
            self.write({"status": "error", "message": "No data provided"})

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
        
class DefenseHandler(RequestHandler):
    def initialize(self,conn):
        self.conn = conn
        self.cursor = self.conn.cursor()
    def get(self):
        ID = self.get_argument("ID")
        if len(ID)>0:
            self.cursor.execute('select * from t_defense_review where s_id =%s',(ID,))
            defense_list = self.cursor.fetchone()
            self.conn.commit()
            if len(defense_list) != 11:
                self.write({"status":"error","msg":"分数不全,请联系管理员"})
            else:
                self.write({"status":"success","received":defense_list})
        else:
            self.write({"status": "error", "message": "No user found"})

    def post(self):
        attribute = self.get_argument("attribute")
        data = self.get_argument("data")
        ID = self.get_argument("ID")

        if len(ID)>0 and len(attribute)>0 and len(data)>0:
            # 调用更新数据库的函数
            data_float = float(data)
            status, msg = self.verify_item(attribute,data)
            if status == True:
                sql = 'update t_defense_review set %s="%f" where s_id="%s"'%(attribute,data_float,ID)
                conn = torndb.Connection(host=data_toml['owner']['host'],user=data_toml['owner']['user'],password=data_toml['owner']['passwd'],database=data_toml['owner']['db'])
                conn.update(sql)
                conn.close()
                self.write({"status": "success", "message": "Data updated successfully"})
            else:
                self.write(msg)
        else:
            self.write({"status": "error", "message": "No data provided"})            

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
        
if __name__=="__main__":
    app = Application([
        (r'/login/',LoginHandler,{'conn':_getConn()}),
        (r'/update_proposal/',ProposalHandler,{'conn':_getConn()}),
        (r'/update_midterm/',MidtermHandler,{'conn':_getConn()}),
        (r'/update_defense/',DefenseHandler,{'conn':_getConn()})
    ])
    #绑定地址和端口号
    app.listen(8888)
    #启动服务器不断监听端口是否有请求
    IOLoop.current().start()
