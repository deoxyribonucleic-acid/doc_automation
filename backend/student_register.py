from tornado.web import RequestHandler
from tornado.web import Application
from tornado.ioloop import IOLoop
import MySQLdb
import hashlib
import os
import secrets
import toml

toml_file_path = "backend\config.toml"
data = toml.load(toml_file_path)

def _getConn():
    return MySQLdb.connect(host=data['owner']['host'],user=data['owner']['user'],passwd=data['owner']['passwd'],db=data['owner']['db'],port=data['owner']['port'],charset='utf8',autocommit=1)

def generate_salt(length=16):
    """生成随机盐值"""
    return secrets.token_hex(length // 2)

def hash_password(password, salt=None):
        """使用SHA-256哈希算法对密码进行加密"""
        if salt is None:
            salt = generate_salt()
        
        # 将密码和盐值合并
        password_with_salt = password + salt

        # 使用SHA-256哈希算法进行加密
        hashed_password = hashlib.sha256(password_with_salt.encode()).hexdigest()

        return hashed_password, salt

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

    def get(self, *args, **kwargs):
        self.render('templates/login_register_student.html')

    def post(self, *args, **kwargs):
        account = self.get_argument('uname')
        passwd = self.get_argument('pwd')
        cursor = self.conn.cursor()
        cursor.execute('select s_pwd, s_salt from t_student where s_id=%s', (account,))
        student_info = cursor.fetchone()
        if student_info:
            s_hashed_password = student_info[0]
            s_salt = student_info[1]
            #判断密码是否正确
            if verify_password(passwd, s_hashed_password, s_salt) == 1:
                cursor.execute('select * from t_proposal_review where s_id =%s',(account,))
                proposal_list = cursor.fetchone()
                cursor.execute('select * from t_midterm_review where s_id =%s',(account,))
                midterm_list = cursor.fetchone()
                cursor.execute('select * from t_defense_review where s_id =%s',(account,))
                defense_list = cursor.fetchone()
                self.write({"学号:":proposal_list[0],'开题评审：1、选题理论和实用性':proposal_list[1],'2、选题难度和创可行性':proposal_list[2],'3、研究方法的合理性':proposal_list[3],
                            '4、开题报告的文字表达,参考文献的引用':proposal_list[4],'5、资料准备的充分性':proposal_list[5],'6、对课题的了解程度':proposal_list[6],
                            '7、基本概念清楚、明确选题的意义':proposal_list[7],'8、论证严密、逻辑性强':proposal_list[8],'9、回答问题条理清晰、应答切题':proposal_list[9],
                            "中期评审:1、已完成的工作量符合进度要求":midterm_list[1],'2、毕设内容符合课题要求':midterm_list[2],'3、资料收集充分':midterm_list[3],'4、对课题内容理解深刻,准确':midterm_list[4],
                            '5、能清晰把握目前设计情况,对下一步的任务有清楚的认识':midterm_list[5],'6、学习态度端正,能够在毕设中投入较多时间和精力':midterm_list[6],'7、课题陈述清晰,逻辑性强':midterm_list[7],
                            '8、思维缜密,回答问题正确':midterm_list[8],
                            "答辩评审:1、论文结构合理,条理清晰,文笔流畅,格式规范":defense_list[1],'2、基本概念和基本原理清楚、正确':defense_list[2],'3、实验数据真实、结论正确':defense_list[3],'4、论文主要内容为本人独立完成':defense_list[4],
                            '5、完成了规定的毕设任务':defense_list[5],'6、掌握了相关的理论知识和专业技能':defense_list[6],'7、具备一定的分析问题和解决问题的能力':defense_list[7],'8、学习态度好,能够在毕设中投入较多时间和精力':defense_list[8],
                            '9、能够简明扼要、重点突出地阐述论文的主要内容':defense_list[9],'10、能够准确、流利地回答评审老师提出的问题':defense_list[10]})
            else:
                self.write("密码错误")

class RegisterHandler(RequestHandler):
    def initialize(self,conn):
        self.conn = conn

    def get(self, *args, **kwargs):
        self.render('templates/login_register_student.html')

    def post(self, *args, **kwargs):
        #获取请求参数
        uname = self.get_argument('newuname')
        pwd = self.get_argument('newpwd')
        tid = self.get_argument('tid')
        s_name = self.get_argument('s_name')
        s_grade = self.get_argument('s_grade')
        s_class = self.get_argument('s_class')
        s_school = self.get_argument('s_school')
        s_title = self.get_argument('s_title')
        s_major = self.get_argument('s_major')
        hashed_password, salt = hash_password(pwd)
        cursor = self.conn.cursor()
        t_rows = cursor.execute('select t_no from t_teacher where t_id="%s"'%tid)
        s_rows = cursor.execute('select s_no from t_student where s_id="%s"'%uname)
        print("t_rows=",t_rows)
        if t_rows == 0:
            self.write('导师账号不存在！')
        # 有bug需解决
        elif s_rows > 0:
            print("s_rows=",s_rows)
            self.write("该账号已存在，无法重复注册！")
        else:
            try:
                # cursor = self.conn.cursor()
                cursor.execute('insert into t_student values(null,"%s","%s","%s","%s","%s","%s","%s","%s","%s","%s")'%(uname,hashed_password,s_name,s_grade,s_class,s_school,s_major,tid,s_title,salt))
                cursor.execute('INSERT INTO t_proposal_review VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)', (uname, '0', '0', '0', '0', '0', '0', '0', '0', '0'))
                cursor.execute('INSERT INTO t_midterm_review VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)', (uname, '0', '0', '0', '0', '0', '0', '0', '0'))
                cursor.execute('INSERT INTO t_defense_review VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)', (uname, '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'))
                print(hashed_password)
                self.conn.commit()
                self.write('注册成功')

            except Exception as e:
                # print('insert into t_student values(null,"%s","%s","%s","%s","%s","%s","%s","%s","%s","%s")'%(uname,hashed_password,t_id,salt))
                self.conn.rollback()
                self.write('注册失败')
                print(e)
        return

app = Application([
    (r'/student_register/',RegisterHandler,{'conn':_getConn()}),
    (r'/student_login/',LoginHandler,{'conn':_getConn()})
],
static_path=os.path.join(os.path.dirname(__file__), "static")
)

#绑定地址和端口号
app.listen(8000)

#启动服务器不断监听端口是否有请求
IOLoop.current().start()