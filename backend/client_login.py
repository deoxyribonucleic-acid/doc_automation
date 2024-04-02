import tornado.ioloop
import tornado.web
from tornado.ioloop import IOLoop
import MySQLdb
import hashlib
import toml
toml_file_path = "backend\config.toml"
data = toml.load(toml_file_path)

def _getConn():
    return MySQLdb.connect(host=data['owner']['host'],user=data['owner']['user'],passwd=data['owner']['passwd'],db=data['owner']['db'],port=data['owner']['port'])

def verify_password(password, hashed_password, salt):
    """验证密码是否正确"""
    # 将输入的密码和盐值合并
    password_with_salt = password + salt

    # 使用相同的哈希算法计算哈希值
    hashed_input_password = hashlib.sha256(password_with_salt.encode()).hexdigest()

    # 比较计算出的哈希值与存储的哈希值是否一致
    return hashed_input_password == hashed_password

class LoginHandler(tornado.web.RequestHandler):
    def initialize(self,conn):
        self.conn = conn

    def post(self, *args, **kwargs):
        #获取请求参数
        pwd = self.get_argument('password')
        uname = self.get_argument('account')
        cursor = self.conn.cursor()
        #使用参数化查询以避免SQL注入攻击
        cursor.execute('SELECT t_pwd, t_salt FROM t_teacher WHERE t_id=%s', (uname,))
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
                self.write({"status": "success", "received": s_name[0], "account_type":"student"})
            else:
                self.write({"status": "error", "message": "Wrong password"})
        elif teacher_info:
            t_hashed_password = teacher_info[0]
            t_salt = teacher_info[1]
            if verify_password(pwd, t_hashed_password, t_salt) == 1:
                cursor.execute('select t_name from t_teacher where t_id=%s', (uname,))
                t_name = cursor.fetchone()
                print(t_name[0],'老师，欢迎！')
                self.write({"status": "success", "received": t_name[0],"account_type":"teacher"})
            else:
                self.write({"status": "error", "message": "Wrong password"})
        else:
            self.write({"status": "error", "message": "No user found"})


#创建应用
app = tornado.web.Application([
    (r'/login/',LoginHandler,{'conn':_getConn()})
])
        
#绑定地址和端口号
app.listen(8888)

#启动服务器不断监听端口是否有请求
tornado.ioloop.IOLoop.current().start()#instance()也可以
