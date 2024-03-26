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
    return MySQLdb.connect(host=data['owner']['host'],user=data['owner']['user'],passwd=data['owner']['passwd'],db=data['owner']['db'],port=data['owner']['port'])

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
        self.render('templates/login_register_teacher.html')

    def post(self, *args, **kwargs):
        #获取请求参数
        uname = self.get_argument('newuname')
        pwd = self.get_argument('newpwd')
        t_name = self.get_argument('t_name')
        t_title = self.get_argument('t_title')
        hashed_password, salt = hash_password(pwd)
        try:
            cursor = self.conn.cursor()
            cursor.execute('insert into t_teacher values(null,"%s","%s","%s","%s","%s")'%(uname,hashed_password,t_title,t_name,salt))
            print(hashed_password)
            self.conn.commit()
            self.write('注册成功')

        except Exception as e:
            print(len(hashed_password))
            print(salt)
            self.conn.rollback()
            self.write('注册失败')
            print(e)


app = Application([
    (r'/teacher_register/',RegisterHandler,{'conn':_getConn()})
],
static_path=os.path.join(os.path.dirname(__file__), "static")
)

#绑定地址和端口号
app.listen(8000)

#启动服务器不断监听端口是否有请求
IOLoop.current().start()