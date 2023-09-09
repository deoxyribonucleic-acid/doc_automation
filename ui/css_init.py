class main_style():
    @staticmethod
    def getInputStyle():
        return '''
        QLineEdit{
            border-radius:3px;
            border-style:solid;
            border-width:1px;
            font-size: 16px;
            padding-right:40px;
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

    @staticmethod
    def input_box():
        return '''
                QLineEdit{
                    background: #F5F5F7;
                    border-radius: 5px;
                }
                QLineEdit:hover{
                    background: #F5F5F7;
                    border: 2px solid #80BEFC;
                    border-radius: 5px
                }

                QLineEdit:focus{
                    background: #FFFFFF;
                    border: 2px solid #80BEFC;
                    border-radius: 5px;
                }
                '''



    @staticmethod
    def header():
        return '''
                background-color: #363740;
                border-radius: 5px;

                '''

    @staticmethod
    def add_sig_btn():
        return '''
        QPushButton{
            background-color:#ffffff;
            border-radius:3px;
            border:none;
        }
        QPushButton:hover{
            background-color:#e6e6e6;
        }
        QPushButton:pressed{
            background-color:#d2d2d2;
        }
                '''

    @staticmethod
    def login_btn():
        return '''
                QPushButton{
            background: #4CA6FF;
            border-radius:3px;
            color:#ffffff;
            border:none;
        }
        QPushButton:hover{
            background: #0573E0;
            color:#ffffff;
        }
        QPushButton:pressed{
            background: #044F9A;
            color:#ffffff;

        }
        '''
    @staticmethod
    def stu_choice():
        return '''
        /* 未下拉时，QComboBox的样式 */
QComboBox {
    
    border-radius: 3px;   /* 圆角 */
    padding: 1px 18px 1px 3px;   /* 字体填衬 */
    color: #363740;
    font: normal normal 15px;
    background: #ffffff;
}

/* 下拉后，整个下拉窗体样式 */
QComboBox QAbstractItemView {
    border-radius: 3px;   /* 圆角 */
    background-color: #ffffff;   /* 整个下拉窗体的背景色 */
    selection-background-color: #363740;   /* 整个下拉窗体被选中项的背景色 */
}
        '''
    @staticmethod
    def path_select_btn():
        return '''
                 QPushButton{
            color:#80BEFC;
            background: #FFFFFF;
            border: 2px solid #80BEFC;
            border:none;
            border-radius:5px;
        }
        QPushButton:hover{
            background: #E6E6E6;
            border: 2px solid #80BEFC;
        }
        QPushButton:pressed{
            background-color:#d2d2d2;
            border: 2px solid #80BEFC;
        }
        '''

    @staticmethod
    def show_box():
        return '''
         QLineEdit{
                    background: #F5F5F7;
                    border-radius: 5px;
                }
        '''

    @staticmethod
    def show_list():
        return '''
    QListWidget
{
 background: #F5F5F7;
border-radius: 5px;
}
        '''

    @staticmethod
    def tab_view():
        return '''
    QTabWidget::pane{
	border: 2px solid #f2f2f2;
	background:#ffffff;
	border-top-color:transparent;
	border-bottom-left-radius: 5px;
	border-bottom-right-radius: 5px;
}
QTabWidget::tab-bar{
	background:rgb(0, 0, 0);
	subcontrol-position:left;
}
QTabBar::tab{
	width:100px;/*宽度根据实际需要进行调整*/
	height:25px;
	background:#ffffff;
	border: 2px solid #f2f2f2;
	border-top-left-radius: 5px;
	border-top-right-radius: 5px;
}
QTabBar::tab:selected{	
	background:#4CA6FF;
	border-bottom-color:#ffffff;
	color:#ffffff;
}
QTabBar::tab:!selected{
    background:#ffffff;
	border-bottom-color:#ffffff;}
 
        '''

    @staticmethod
    def reg_window():
        return '''
         QLineEdit{
                    background: #F5F5F7;
                    border-radius: 5px;
                }
                QLineEdit:hover{
                    background: #F5F5F7;
                    border: 2px solid #80BEFC;
                    border-radius: 5px
                }

                QLineEdit:focus{
                    background: #FFFFFF;
                    border: 2px solid #80BEFC;
                    border-radius: 5px;
                }
                
                      QPushButton{
                            background: #4CA6FF;
                            border-radius:3px;
                            color:#ffffff;
                            border:none;
                        }
                        QPushButton:hover{
                            background: #0573E0;
                            color:#ffffff;
                        }
                        QPushButton:pressed{
                            background: #044F9A;
                            color:#ffffff;
                        }
                        

        '''
    @staticmethod
    def reg_mess():
        return '''
     QMessageBox {
	  background-color: #ffffff;
    border-radius: 3px;
    width: 300px;
    height: 180px;
}

QMessageBox QLabel#qt_msgbox_label { /* textLabel */
    text-align:center;
    /*word-wrap: break-word;*/
	color: #363740;
	background-color: transparent;
}

QMessageBox QLabel#qt_msgboxex_icon_label { /* iconLabel */
	width: 40px;
	height: 40px; /* textLabel和iconLabel高度保持一致 */
}

QMessageBox QPushButton { /* QMessageBox中的QPushButton样式 */
	border: 2px solid #4CA6FF;
	border-radius: 3px;
	color: #298DFF;
	font-size: 10pt;
	min-width: 70px;
	min-height: 25px;
}

QMessageBox QPushButton:hover {
	background-color: #0573E0;
	color: #ffffff;
}

QMessageBox QPushButton:pressed {
	background-color: #044F9A;
}

QMessageBox QDialogButtonBox{ /* buttonBox */
	background-color: #515151;
	button-layout: 0; /* 设置QPushButton布局好像没啥作用 */
}
        '''
    @staticmethod
    def main_window():
        return '''
        QMainWindow{
        background-color:#ffffff;
        font:  "思源黑体 CN Normal";
        }
        QMessageBox {
	  background-color: #ffffff;
    border-radius: 3px;
    width: 300px;
    height: 180px;
}

QMessageBox QLabel#qt_msgbox_label { /* textLabel */
    text-align:center;
    /*word-wrap: break-word;*/
	color: #363740;
	background-color: transparent;
}

QMessageBox QLabel#qt_msgboxex_icon_label { /* iconLabel */
	width: 40px;
	height: 40px; /* textLabel和iconLabel高度保持一致 */
}

QMessageBox QPushButton { /* QMessageBox中的QPushButton样式 */
	border: 2px solid #4CA6FF;
	border-radius: 3px;
	color: #298DFF;
	font-size: 10pt;
	min-width: 70px;
	min-height: 25px;
}

QMessageBox QPushButton:hover {
	background-color: #0573E0;
	color: #ffffff;
}

QMessageBox QPushButton:pressed {
	background-color: #044F9A;
}

QMessageBox QDialogButtonBox{ /* buttonBox */
	background-color: #515151;
	button-layout: 0; /* 设置QPushButton布局好像没啥作用 */
}

        '''
    @staticmethod
    def input_box_s():
        return '''
                        QLineEdit{
                            background: #fee4b3;
                            border-radius: 5px;

                        }
                        QLineEdit:hover{
                            background: #F5F5F7;
                            border: 2px solid #80BEFC;
                            border-radius: 5px
                        }

                        QLineEdit:focus{
                            background: #FFFFFF;
                            border: 2px solid #80BEFC;
                            border-radius: 5px;
                        }
                        '''