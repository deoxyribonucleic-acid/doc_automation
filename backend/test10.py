from tornado.web import Application
from tornado.ioloop import IOLoop
from tornado.template import Template
from tornado.web import RequestHandler
import os
class Person(object):
    def __init__(self,pname):
        self.pname = pname

def reverse(obj):
    if isinstance(obj,list):
        obj.reverse()
    return obj

class IndexHandler(RequestHandler):
    def get(self, *args, **kwargs):
        # 方法一：
        # with open(os.path.join(os.getcwd(),'templates','temp.html'),'rb') as fr:
        #     content = fr.read()
        
        # t = Template(content)
        # c = t.generate(uname='zhangsan')
        # self.write(c)
        l = ['a1','a2','a3']

        d = {'k1':'v1','k2':'v2'}

        p = Person('xiaoming')

        s = '<h1>fuckoff</h1>'
        self.render('temp.html',uname='wangwu',l=l,d=d,p=p,rev=reverse,s=s)

app = Application([
    (r'/index',IndexHandler)
],template_path=os.path.join(os.getcwd(),'templates'))

if __name__ == '__main__':
    app.listen(8000)
    IOLoop.current().start()