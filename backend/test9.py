from tornado.web import RequestHandler
from tornado.web import Application
from tornado.ioloop import IOLoop
import MySQLdb
class LoginHandler(RequestHandler):

    def _initialize(self,conn):
        self.conn = conn
    
    def prepare(self):
        if self.request.method == 'POST':
            self.uname = self.get_argument('uname')
            self.pwd = self.get_argument('pwd')

    def get(self, *args, **kwargs):
        self.render('templates/login1.html')

    def post(self, *args, **kwargs):
        #获取游标对象
        cursor = self.conn.cursor()
        #执行SQL语句
        cursor.execute('select * from t_user where uname="%s" and pwd="%s"'%(self.uname,self.pwd))
        #获取执行结果
        user = cursor.fetchone()
        #判断是否登录成功
        if user:
            self.write('登录成功！')
        else:
            self.write('登录失败！')

dbconfig=dict(host='127.0.0.1',user='root',passwd='123456',db='db01',port=3306)

app = Application([
    (r'/login',LoginHandler,{'conn':MySQLdb.connect(**dbconfig)})
])

if __name__ == '__main__':
    app.listen(8000)
    IOLoop.current().start()
