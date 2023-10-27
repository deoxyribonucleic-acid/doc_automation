import glob
import os, sys
from tools import global_variable as glv
from PyQt5.Qt import QApplication, QMainWindow, QLabel
# 获取路径
def getPath(fileName):
    if sys.platform == 'darwin' and not glv.get('debug'):
        path = os.path.join(os.path.dirname(sys.argv[0].rsplit('/',2)[0]), fileName)
    else:
        path = os.path.join(os.path.dirname(sys.argv[0]), fileName)
    return path

# Debug Only
if __name__ == '__main__':
    class Main(QMainWindow):
        def __init__(self):
            super().__init__()
            self.initUI()

        def initUI(self):
            self.resize(400, 300)
            self.setWindowTitle('获取路径')
            self.show()
            self.path = getPath("test.txt")
            self.label = QLabel(self)
            self.label.setText(self.path)
            self.label.move(20, 20)
            self.label.resize(2000, 20)
            self.label.show()
    app = QApplication(sys.argv)
    main = Main()
    sys.exit(app.exec_())