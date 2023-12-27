import tornado.ioloop
import tornado.web

class IndexHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.render('templates/login.html')

class LoginHandler(tornado.web.RequestHandler):
    def post(self, *args, **kwargs):
        #获取请求参数
        pwd = self.get_argument('pwd')
        uname = self.get_argument('uname')

        #判断是否登录成功
        if uname == 'zhangsan' and pwd == '123':
            self.write(u'登录成功')
        else:
            self.write(u'登录失败')


#创建应用
app = tornado.web.Application([
    (r'/',IndexHandler),
    (r'/login/',LoginHandler)
])
        
#绑定地址和端口号
app.listen(8000)

#启动服务器不断监听端口是否有请求
tornado.ioloop.IOLoop.current().start()#instance()也可以
