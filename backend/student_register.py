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
    (r'/student_register/',RegisterHandler,{'conn':_getConn()})
],
static_path=os.path.join(os.path.dirname(__file__), "static")
)

#绑定地址和端口号
app.listen(8000)

#启动服务器不断监听端口是否有请求
IOLoop.current().start()