from tornado.web import RequestHandler
from tornado.web import Application
from tornado.ioloop import IOLoop

class GetRequestInfo(RequestHandler):
    def get(self, *args, **kwargs):
        protocal = self.request.protocol
        method = self.request.method
        uri = self.request.uri
        
        ua = self.request.headers['User-Agent']

        #设置响应信息
        self.set_status(200)
        self.set_header('Server','HelloServer')
        self.write('%s,%s,%s'%(protocal,method,uri))

app = Application([
    (r'/getReq/', GetRequestInfo)
])

app.listen(8000)
 
IOLoop.current().start()
