import torndb_for_python3
from tornado.web import RequestHandler
from tornado.web import Application
from tornado.ioloop import IOLoop
import MySQLdb

def _getConn():
    return torndb_for_python3.Connection(host='127.0.0.1',database='db01',user='root',password='1234567')

class RegisterHandler(RequestHandler):
    def initialize(self,conn):
        self.conn = conn

    def get(self, *args, **kwargs):
        self.render('templates/query.html')

    def post(self, *args, **kwargs):
        #获取请求参数
        cname = self.get_argument('cname')

        try:
            # cursor = self.conn.cursor()
            # stus = cursor.execute('select * from t_cls,t_stu where t_cls.cname="dmt3" and t_cls.cno=t_stu.cls')
            stus = self.conn.query('select cname, sname from t_cls,t_stu where t_cls.cname="dmt3" and t_cls.cno=t_stu.cls')
            # self.conn.commit()
            print(stus[0])
            # print(self.conn)
            self.write(stus[0])
            

        except Exception as e:
            # self.conn.rollback()
            self.write('查询失败')
            print('查询失败')
            print(e)

app = Application([
    (r'/query/',RegisterHandler,{'conn':_getConn()})
])

#绑定地址和端口号
app.listen(8000)

#启动服务器不断监听端口是否有请求
IOLoop.current().start()
#多表查询
# def queryAll(cname):
    # conn = torndb_for_python3.Connection(host='127.0.0.1',database='db01',user='root',password='1234567')

    # stus = conn.query('select * from t_cls,t_stu where t_cls.cname="%s" and t_cls.cno=t_stu.cls'%cname)

#     conn.close()

#     return stus

# print(queryAll('数媒技3班'))
#多表删除，外键设置级联删除
# def deleteByParams(cno):
#     conn = torndb_for_python3.Connection(host='127.0.0.1',database='db01',user='root',password='1234567')
#     conn.execute('delete from t_cls where cno="%s"'%cno)

#     conn.close()

#deleteByParams(1)