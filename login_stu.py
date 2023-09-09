##!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author : Tang Shimeng

import os
import sys
import urllib.request, urllib.error, http.cookiejar  # 制定URL，获取网页数据
import json
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEngineProfile
from PyQt5 import QtNetwork, QtGui
from PyQt5.QtCore import QUrl, Qt, pyqtSignal
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtWidgets import QWidget, QTabWidget, QApplication, QButtonGroup, QLineEdit, QPushButton, QCheckBox, \
    QVBoxLayout, QMessageBox
from PyQt5 import QtCore

import tools.db_operate
import urllib.parse as parse


icon_path = os.getcwd() + '/static/'


class MyStyle():
    @staticmethod
    def getIconButtonStyle():
        return '''
        QPushButton{
            background-color:rgba(0,0,0,0);
            border-radius:3px;
            border:none;
        }
        QPushButton:hover{
            background-color:rgb(230,230,230);
        }
        QPushButton:pressed{
            background-color:rgb(210,210,210);
        }
        '''

    @staticmethod
    def getButtonStyle2():
        return '''
        QPushButton{
            border-radius:3px;
            background-color:rgb(236,245,255);
            font-family:"SimSun";
            font-size:18px;

        }
        QPushButton:hover{
            background-color:rgb(64,158,255);
            color:white;
        }
        QPushButton:pressed{
            background-color:rgb(58,142,230);
        }
        '''

    @staticmethod
    def getInputStyle():
        return '''
        QLineEdit{
            border-radius:3px;
            border-style:solid;
            border-width:1px;
            font-size: 16px;
            padding-right:40px;
            font-family:"Microsoft YaHei";
            border-color:rgb(200,200,200);
            background-color:white;
        }
        QLineEdit:hover{
            border-color:rgb(150,150,150);
        }

        QLineEdit:focus{
            border-color:rgb(102,177,255);
        }
        '''

    @staticmethod
    def getQTabWidgetStyle():
        return '''
        QTabWidget{
            background-color:rgb(240,240,240);
        }

        QTabBar::tab {
            background-color:rgb(236,245,255);
            height:30px;
            padding-left:10px;
            padding-right:10px;
            margin-top:0px;
            min-width:150px;
            max-width:150px;
         }
        QTabBar::tab:hover{
            color:rgb(64,158,255);
        }

        QTabBar::tab:selected{
            color:white;
            background:rgb(64,158,255);
        }
        QTabBar::close-button{
            image: url(static/close.png);
            background-color:rgba(0,0,0,0);
        }
        QTabBar::close-button:hover {
            image: url(static/close2.png);
        }
        '''

    @staticmethod
    def getQwidgetStyle2():
        return '''
        QWidget{
            background-color:rgb(250,250,250);
            border:none;
        }
        '''

    @staticmethod
    def getCheckBoxStyle():
        return '''
        QCheckBox{
            color:rgb(150,150,150);
            Background-color:rgba(0,0,0,0);
        }
        QCheckBox:hover{
            Color:rgb(149,216,255);
        }
        QCheckBox:checked{
            color:rgb(64,158,255);
        }

        '''


class MyWebView(QWebEngineView):


    def __init__(self, my, *args):
        print("初始化 webview")
        super(MyWebView, self).__init__(*args)
        print("set my")
        self.my = my
        print('这里',QWebEngineProfile.defaultProfile())
        QWebEngineProfile.defaultProfile().cookieStore().cookieAdded.connect(self.onCookieAdd)
        self.cookies = {}  # 存放cookie字典
        self.total_cookie_dic = {}
        flags = self.windowFlags()
        # self.view = None

    def createWindow(self, QWebEnginePage_WebWindowType):
        return self.my.create_view()

    def onCookieAdd(self, cookie):  # 处理cookie添加的事件
        name = cookie.name().data().decode('utf-8')  # 先获取cookie的名字，再把编码处理一下
        value = cookie.value().data().decode('utf-8')  # 先获取cookie值，再把编码处理一下
        self.cookies[name] = value  # 将cookie保存到字典里

    # 获取cookie
    def get_cookie(self):
        cookie_str = ''
        # for key, value in self.cookies.items():  # 遍历字典
        #     if key == 'THEME' or key == '_WEU' or key == 'EMAP_LANG' or key == 'MOD_AUTH_CAS' or key == 'JSESSIONID':
        #         item={key:value}
        #         self.total_cookie_dic.update(item)
        #           # 将键值对拿出来拼接一下
        #         print('字典',self.total_cookie_dic)
        #
        #     for key, value in self.total_cookie_dic.items():
        #         cookie_str += (key + '=' + value + ';')
        for key, value in self.cookies.items():  # 遍历字典
            cookie_str += (key + '=' + value + ';')
        return cookie_str  # 返回拼接好的字符串


class Webbox(QWidget):
    def __init__(self, my, *args):
        super(Webbox, self).__init__(*args)
        self.my = my
        self.setGUI()

    def setGUI(self):
        print('set up webbox')
        self.webview = MyWebView(self.my, self)
        print('webview',self.webview)
        self.buttons = []
        self.url_input = QLineEdit(self)
        self.function_group = QButtonGroup(self)
        self.function_group.setExclusive(True)
        self.url_input.setStyleSheet(MyStyle.getInputStyle())
        self.homepage()
        self.webview.loadFinished.connect(self.update_view)
        icon = ['back.png', 'forward.png', 'reload.png', 'home.png']
        for i in icon:
            button = QPushButton(self)
            button.setIcon(QIcon(QPixmap(self.get_resource_path(icon_path + i))))
            button.setStyleSheet(MyStyle.getIconButtonStyle())
            self.buttons.append(button)
        self.buttons[1].clicked.connect(lambda: self.webview.forward())
        self.buttons[0].clicked.connect(lambda: self.webview.back())
        self.buttons[2].clicked.connect(lambda: self.webview.reload())
        self.buttons[3].clicked.connect(self.homepage)
        self.url_input.returnPressed.connect(self.init)

    def homepage(self):
        self.webview.load(QUrl('https://e.cuc.edu.cn/new/index.html'))
        self.url_input.setText('https://e.cuc.edu.cn/new/index.html')

    def resizeEvent(self, a0: QtGui.QResizeEvent) -> None:
        self.buttons[0].setGeometry(5, 5, 45, 30)
        self.buttons[1].setGeometry(50 * 1 + 5, 5, 45, 30)
        self.buttons[2].setGeometry(50 * 2 + 5, 5, 45, 30)
        self.buttons[3].setGeometry(50 * 3 + 5, 5, 45, 30)
        self.url_input.setGeometry(50 * 4 + 5, 5, self.width() - 4 * 50 + 10 - 3 * 35 - 80, 30)
        self.webview.setGeometry(0, 50, self.width(), self.height() - 35)

    def init(self):
        if 'http' in self.url_input.text():
            self.webview.load(QUrl(self.url_input.text()))
        elif self.url_input.text() == '':
            self.zhuye()
        else:
            self.webview.load(QUrl(r'http://' + self.url_input.text()))
        self.url_input.setText(self.webview.url().toString())

    def update_view(self):
        self.url_input.setText(self.webview.url().toString())
        self.url_input.setCursorPosition(0)
        self.my.update_title(self)


    def get_resource_path(self, relative_path):
        if hasattr(sys, '_MEIPASS'):
            return os.path.join(sys._MEIPASS, relative_path)
        return os.path.join(os.path.abspath(""), relative_path)


class WebView(QWidget):
    update_db=pyqtSignal()
    realcookie = ''

    def __init__(self, *args):
        super(WebView, self).__init__(*args)
        # self.setWindowModality(QtCore.Qt.WindowModal)
        self.student_operate=tools.db_operate.student()
        self.windows = []
        self.buttons = []
        self.setUI()
        # self.setWindowState(Qt.WindowActive)

        # 窗口跳到最前端
        # self.setWindowFlags(Qt.WindowStaysOnTopHint)

    def setUI(self):
        self.box = QVBoxLayout(self)
        self.tabbar = QTabWidget(self)
        self.tabbar.setTabsClosable(True)
        self.tabbar.setStyleSheet(MyStyle.getQTabWidgetStyle())
        self.tabbar.tabCloseRequested.connect(self.close_tab)
        self.setStyleSheet(MyStyle.getQwidgetStyle2())
        view = Webbox(self)
        print('view', view)
        self.windows.append(view)
        self.tabbar.addTab(view, view.webview.title())
        self.btn_get = QPushButton(self)
        self.btn_get.setText('获取信息')
        # self.btn_get.setIcon(QIcon(QPixmap(self.get_resource_path(icon_path +'shouchang1.png' ))))
        self.btn_get.setStyleSheet(MyStyle.getButtonStyle2())
        self.btn_get.clicked.connect(self.get_inform)
        self.buttonsname = ['shouchang1.png', 'shouchang2.png', 'more.png', 'add.png']
        for i in self.buttonsname:
            button = QPushButton(self)
            button.setIcon(QIcon(QPixmap(self.get_resource_path(icon_path + i))))
            button.setStyleSheet(MyStyle.getIconButtonStyle())
            self.buttons.append(button)
        self.buttons[3].setStyleSheet(MyStyle.getButtonStyle2())
        self.buttons[3].setGeometry(self.tabbar.count() * 170, 0, 30, 30)
        self.buttons[3].clicked.connect(self.create_view)
        print("setUI")

    # 创建一个新的Webobox容器来装新的页面
    def create_view(self):
        try:
            view = Webbox(self)
            self.windows.append(view)
            self.tabbar.addTab(view, view.webview.title())
            self.tabbar.setCurrentWidget(view)
            if self.tabbar.count() * 150 > self.width():
                self.buttons[3].setGeometry(self.width() - 40, 0, 30, 30)
            else:
                self.buttons[3].setGeometry(self.tabbar.count() * 170, 0, 30, 30)

            return view.webview
        except Exception as e:
            print(e)

    def close_tab(self, currentIndex):
        currentQWidget = self.tabbar.widget(currentIndex)
        currentQWidget.deleteLater()
        self.windows.remove(currentQWidget)
        self.tabbar.removeTab(currentIndex)
        if self.tabbar.count() * 150 > self.width():
            self.buttons[3].setGeometry(self.width() - 40, 0, 30, 30)
        else:
            self.buttons[3].setGeometry(self.tabbar.count() * 170, 0, 30, 30)

    def resizeEvent(self, a0: QtGui.QResizeEvent) -> None:
        # self.proxies.move(self.width() - 160, 41)
        self.btn_get.setGeometry(self.width() - 160, 5 + 30, 150, 30)
        self.buttons[0].setGeometry(self.width() - 40 * 3 - 80, 7 + 30, 0, 0)
        self.buttons[1].setGeometry(self.width() - 35 * 2, 5 + 30, 0, 0)
        self.buttons[2].setGeometry(self.width() - 40, 5 + 30, 0, 0)
        self.tabbar.setGeometry(0, 0, self.width(), self.height())

    def update_title(self, view):
        self.tabbar.setTabText(self.tabbar.indexOf(view), view.webview.title())
        #获取页面cookie
        # index = self.tabbar.currentIndex()
        # print('获取到cookie: ', self.windows[index].webview.get_cookie())
        # cookie = self.windows[index].webview.get_cookie()
        # # if key == 'THEME' or key =='_WEU' or key =='EMAP_LANG' or key =='MOD_AUTH_CAS' or key =='JSESSIONID':
        # if 'THEME' in cookie and '_WEU' in cookie and 'EMAP_LANG' in cookie and 'MOD_AUTH_CAS' in cookie and 'JSESSIONID' in cookie:
        #     self.realcookie = cookie

    def get_resource_path(self, relative_path):
        if hasattr(sys, '_MEIPASS'):
            return os.path.join(sys._MEIPASS, relative_path)
        return os.path.join(os.path.abspath(""), relative_path)

    def IsProxies(self):
        if self.proxies.isChecked():
            proxy = QtNetwork.QNetworkProxy()
            # Http访问代理
            proxy.setType = QtNetwork.QNetworkProxy.HttpProxy
            # 代理ip地址HttpProxy
            proxy.setHostName("127.0.0.1")
            # 端口号
            proxy.setPort(8888)
            proxy.setUser("4")
            proxy.setPassword("1")
            QtNetwork.QNetworkProxy.setApplicationProxy(proxy)

    def get_inform(self):
        # this_window=self.create_view()
        # this_window.load(QUrl('https://bkjw.cuc.edu.cn/jwapp/sys/xsbysj/*default/index.do'))
        # index = self.tabbar.currentIndex()
        # print('获取到cookie: ', self.windows[index].webview.get_cookie())
        # cookie = self.windows[index].webview.get_cookie()
        # # if key == 'THEME' or key =='_WEU' or key =='EMAP_LANG' or key =='MOD_AUTH_CAS' or key =='JSESSIONID':
        # if 'THEME' in cookie and '_WEU' in cookie and 'EMAP_LANG' in cookie and 'MOD_AUTH_CAS' in cookie and 'JSESSIONID' in cookie:
        #     self.realcookie = cookie

        index = self.tabbar.currentIndex()
        cookie = self.windows[index].webview.get_cookie()
        if 'THEME' in cookie and '_WEU' in cookie and 'EMAP_LANG' in cookie and 'MOD_AUTH_CAS' in cookie and 'JSESSIONID' in cookie:
            self.realcookie = cookie

        if self.realcookie  == '':
            QMessageBox.about(self, "提示", "请先进入毕业设计管理页面后点击获取")

        if  self.realcookie  != '':
            print('realcookie',self.realcookie)
            url = 'https://bkjw.cuc.edu.cn/jwapp/sys/xsbysj/modules/xsbmgl/xsckzjktbbhtdffzrwb.do'
            formdata = {

            }
            data = urllib.parse.urlencode(formdata).encode("utf-8")
            try:
                res = self.askURL(url,self.realcookie,data)['datas']['xsckzjktbbhtdffzrwb']['rows']
                WID=res[0]['WID']
                formdata={
                    'WID':WID
                }
                data = urllib.parse.urlencode(formdata).encode("utf-8")
                url ='https://bkjw.cuc.edu.cn/jwapp/sys/xsbysj/modules/gcglmodule/xsbmxxcx.do'
                inform=self.askURL(url,self.realcookie,data)['datas']['xsbmxxcx']['rows']
                print(inform)
                this_stu={
                    'ID':int(inform[0]['XH']),
                    "name": inform[0]['XM'],
                    "academy": inform[0]['YXDM_DISPLAY'],
                    "major": inform[0]['ZYDM_DISPLAY'],
                    "grade": inform[0]['NJ_DISPLAY'],
                    "banji": inform[0]['NJ_DISPLAY']+inform[0]['ZYDM_DISPLAY']+'?班',
                    "title": inform[0]['LWTM'],
                    "teacher": inform[0]['JSXM'],
                    "zhichen":'请填写职称',
                }

                self.student_operate.add_item(this_stu)
                self.update_db.emit()
                QMessageBox.about(self, "success", "个人信息已录入生成工具!")
            except:
                QMessageBox.about(self, "error", "请重新打开浏览器直接进入毕业设计页面获取")


    def askURL(self, url, cookie,data):
        print('cookie',cookie)
        headers = {
            'Cookie': cookie,
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.76'
        }
        req = urllib.request.Request(url, headers=headers ,data=data)
        html = ""
        try:
            resp = urllib.request.urlopen(req)
            html = resp.read().decode("utf-8")
            # print(html)
        except urllib.error.URLError as e:
            if hasattr(e, "code"):  # hasattr（e,"code“): 判断e这个对象里面是否包含code这个属性
                print(e.code)
            if hasattr(e, "reason"):
                print(e.reason)

        try:
            response = json.loads(html)
            return response
        except:
            print('error')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    print(app)
    window = WebView()
    print(window)
    window.resize(1440, 720)
    window.setMinimumWidth(800)
    window.setWindowTitle('登录')
    window.setWindowIcon(QIcon(window.get_resource_path(icon_path + "ico.png")))
    window.show()
    sys.exit(app.exec_())
