from tornado.web import RequestHandler
from tornado.web import Application
from tornado.ioloop import IOLoop
from tornado.web import RedirectHandler
from tornado.web import StaticFileHandler
import os

class IndexHandler(RequestHandler):
    def get(self, *args, **kwargs):
        self.render('loadStatic.html')

app = Application([
    (r'/index',IndexHandler),
    (r'/static/(.*)',StaticFileHandler,{'path':os.path.join(os.getcwd(),'static')})
],template_path=os.path.join(os.getcwd(),'templates'),xsrf_cookies=True)

if __name__ == '__main__':
    app.listen(8000)
    IOLoop.current().start()