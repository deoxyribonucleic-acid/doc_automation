# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_ui_teacherOZSAVO.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


import ui.back

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(477, 500)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(450, 500))
        MainWindow.setMaximumSize(QSize(16777215, 16777215))
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"font:  \"\u601d\u6e90\u9ed1\u4f53 CN Normal\";\n"
"\n"
"")
        self.template_generation = QAction(MainWindow)
        self.template_generation.setObjectName(u"template_generation")
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(10)
        self.template_generation.setFont(font)
        self.signature_fill = QAction(MainWindow)
        self.signature_fill.setObjectName(u"signature_fill")
        self.signature_fill.setFont(font)
        self.assess = QAction(MainWindow)
        self.assess.setObjectName(u"assess")
        self.assess.setFont(font)
        self.merge = QAction(MainWindow)
        self.merge.setObjectName(u"merge")
        self.merge.setFont(font)
        self.add_stu = QAction(MainWindow)
        self.add_stu.setObjectName(u"add_stu")
        self.doc_to_docx = QAction(MainWindow)
        self.doc_to_docx.setObjectName(u"doc_to_docx")
        self.doc_to_docx.setFont(font)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(1)
        sizePolicy1.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy1)
        self.frame.setMinimumSize(QSize(1, 0))
        self.frame.setStyleSheet(u"")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Plain)
        self.frame.setLineWidth(0)
        self.gridLayout = QGridLayout(self.frame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(12, 12, 12, 12)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SetMaximumSize)
        self.current_stu_label = QLabel(self.frame)
        self.current_stu_label.setObjectName(u"current_stu_label")
        self.current_stu_label.setMinimumSize(QSize(0, 30))
        font1 = QFont()
        font1.setFamily(u"Segoe UI")
        font1.setPointSize(14)
        font1.setBold(False)
        font1.setItalic(False)
        font1.setWeight(50)
        font1.setKerning(True)
        self.current_stu_label.setFont(font1)
        self.current_stu_label.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);\n"
"color: rgb(255, 255, 255);")

        self.verticalLayout.addWidget(self.current_stu_label)

        self.verticalSpacer_3 = QSpacerItem(13, 13, QSizePolicy.Minimum, QSizePolicy.Preferred)

        self.verticalLayout.addItem(self.verticalSpacer_3)

        self.stu_info = QHBoxLayout()
        self.stu_info.setObjectName(u"stu_info")
        self.choice_stu = QComboBox(self.frame)
        self.choice_stu.setObjectName(u"choice_stu")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.choice_stu.sizePolicy().hasHeightForWidth())
        self.choice_stu.setSizePolicy(sizePolicy2)
        self.choice_stu.setMinimumSize(QSize(0, 30))
        font2 = QFont()
        font2.setFamily(u"Segoe UI")
        font2.setPointSize(10)
        font2.setBold(False)
        font2.setItalic(False)
        font2.setWeight(50)
        self.choice_stu.setFont(font2)

        self.stu_info.addWidget(self.choice_stu)

        self.horizontalSpacer = QSpacerItem(30, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.stu_info.addItem(self.horizontalSpacer)

        self.add_stu_btn = QPushButton(self.frame)
        self.add_stu_btn.setObjectName(u"add_stu_btn")
        sizePolicy3 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.add_stu_btn.sizePolicy().hasHeightForWidth())
        self.add_stu_btn.setSizePolicy(sizePolicy3)
        self.add_stu_btn.setMinimumSize(QSize(75, 30))
        self.add_stu_btn.setMaximumSize(QSize(100, 16777215))
        font3 = QFont()
        font3.setFamily(u"\u601d\u6e90\u9ed1\u4f53 CN Normal")
        font3.setPointSize(13)
        font3.setBold(False)
        font3.setItalic(False)
        font3.setWeight(50)
        self.add_stu_btn.setFont(font3)
        self.add_stu_btn.setStyleSheet(u"font: 13pt \"\u601d\u6e90\u9ed1\u4f53 CN Normal\";")

        self.stu_info.addWidget(self.add_stu_btn)

        self.horizontalSpacer_2 = QSpacerItem(30, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.stu_info.addItem(self.horizontalSpacer_2)

        self.login_btn = QPushButton(self.frame)
        self.login_btn.setObjectName(u"login_btn")
        sizePolicy3.setHeightForWidth(self.login_btn.sizePolicy().hasHeightForWidth())
        self.login_btn.setSizePolicy(sizePolicy3)
        self.login_btn.setMinimumSize(QSize(75, 30))
        self.login_btn.setMaximumSize(QSize(100, 30))
        self.login_btn.setFont(font2)

        self.stu_info.addWidget(self.login_btn)

        self.stu_info.setStretch(0, 4)
        self.stu_info.setStretch(1, 1)
        self.stu_info.setStretch(2, 4)
        self.stu_info.setStretch(3, 1)
        self.stu_info.setStretch(4, 4)

        self.verticalLayout.addLayout(self.stu_info)

        self.verticalSpacer_2 = QSpacerItem(13, 13, QSizePolicy.Minimum, QSizePolicy.Preferred)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.xzcy_sig = QLabel(self.frame)
        self.xzcy_sig.setObjectName(u"xzcy_sig")
        sizePolicy4 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.xzcy_sig.sizePolicy().hasHeightForWidth())
        self.xzcy_sig.setSizePolicy(sizePolicy4)
        self.xzcy_sig.setMinimumSize(QSize(40, 30))
        font4 = QFont()
        font4.setFamily(u"Segoe UI")
        font4.setPointSize(10)
        font4.setBold(False)
        font4.setItalic(False)
        font4.setWeight(50)
        font4.setKerning(True)
        self.xzcy_sig.setFont(font4)
        self.xzcy_sig.setLayoutDirection(Qt.RightToLeft)
        self.xzcy_sig.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);\n"
"color: rgb(255, 255, 255);")
        self.xzcy_sig.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.xzcy_sig.setWordWrap(True)

        self.horizontalLayout.addWidget(self.xzcy_sig)

        self.xzcy_add = QPushButton(self.frame)
        self.xzcy_add.setObjectName(u"xzcy_add")
        sizePolicy5 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.xzcy_add.sizePolicy().hasHeightForWidth())
        self.xzcy_add.setSizePolicy(sizePolicy5)
        self.xzcy_add.setMinimumSize(QSize(75, 30))
        self.xzcy_add.setMaximumSize(QSize(16777215, 30))
        self.xzcy_add.setFont(font2)

        self.horizontalLayout.addWidget(self.xzcy_add)


        self.horizontalLayout_4.addLayout(self.horizontalLayout)

        self.horizontalSpacer_4 = QSpacerItem(30, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_4)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.xzzz_sig = QLabel(self.frame)
        self.xzzz_sig.setObjectName(u"xzzz_sig")
        sizePolicy4.setHeightForWidth(self.xzzz_sig.sizePolicy().hasHeightForWidth())
        self.xzzz_sig.setSizePolicy(sizePolicy4)
        self.xzzz_sig.setMinimumSize(QSize(40, 30))
        self.xzzz_sig.setFont(font4)
        self.xzzz_sig.setLayoutDirection(Qt.RightToLeft)
        self.xzzz_sig.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);\n"
"color: rgb(255, 255, 255);")
        self.xzzz_sig.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.xzzz_sig.setWordWrap(True)

        self.horizontalLayout_2.addWidget(self.xzzz_sig)

        self.xzzz_add = QPushButton(self.frame)
        self.xzzz_add.setObjectName(u"xzzz_add")
        sizePolicy5.setHeightForWidth(self.xzzz_add.sizePolicy().hasHeightForWidth())
        self.xzzz_add.setSizePolicy(sizePolicy5)
        self.xzzz_add.setMinimumSize(QSize(75, 30))
        self.xzzz_add.setMaximumSize(QSize(16777215, 30))
        self.xzzz_add.setFont(font2)

        self.horizontalLayout_2.addWidget(self.xzzz_add)


        self.horizontalLayout_4.addLayout(self.horizontalLayout_2)

        self.horizontalSpacer_3 = QSpacerItem(30, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_3)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.zdls_sig = QLabel(self.frame)
        self.zdls_sig.setObjectName(u"zdls_sig")
        sizePolicy4.setHeightForWidth(self.zdls_sig.sizePolicy().hasHeightForWidth())
        self.zdls_sig.setSizePolicy(sizePolicy4)
        self.zdls_sig.setMinimumSize(QSize(40, 30))
        self.zdls_sig.setFont(font4)
        self.zdls_sig.setLayoutDirection(Qt.RightToLeft)
        self.zdls_sig.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);\n"
"color: rgb(255, 255, 255);")
        self.zdls_sig.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.zdls_sig.setWordWrap(True)

        self.horizontalLayout_3.addWidget(self.zdls_sig)

        self.zdls_add = QPushButton(self.frame)
        self.zdls_add.setObjectName(u"zdls_add")
        sizePolicy5.setHeightForWidth(self.zdls_add.sizePolicy().hasHeightForWidth())
        self.zdls_add.setSizePolicy(sizePolicy5)
        self.zdls_add.setMinimumSize(QSize(75, 30))
        self.zdls_add.setMaximumSize(QSize(16777215, 30))
        self.zdls_add.setFont(font2)

        self.horizontalLayout_3.addWidget(self.zdls_add)


        self.horizontalLayout_4.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4.setStretch(0, 4)
        self.horizontalLayout_4.setStretch(1, 1)
        self.horizontalLayout_4.setStretch(2, 4)
        self.horizontalLayout_4.setStretch(3, 1)
        self.horizontalLayout_4.setStretch(4, 4)

        self.verticalLayout.addLayout(self.horizontalLayout_4)


        self.horizontalLayout_5.addLayout(self.verticalLayout)


        self.gridLayout.addLayout(self.horizontalLayout_5, 0, 0, 1, 1)


        self.verticalLayout_2.addWidget(self.frame)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.main_widget = QStackedWidget(self.centralwidget)
        self.main_widget.setObjectName(u"main_widget")
        sizePolicy6 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(3)
        sizePolicy6.setHeightForWidth(self.main_widget.sizePolicy().hasHeightForWidth())
        self.main_widget.setSizePolicy(sizePolicy6)
        self.main_widget.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"")
        self.template_generation_2 = QWidget()
        self.template_generation_2.setObjectName(u"template_generation_2")
        self.gridLayout_6 = QGridLayout(self.template_generation_2)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.scrollArea_2 = QScrollArea(self.template_generation_2)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setFrameShape(QFrame.NoFrame)
        self.scrollArea_2.setFrameShadow(QFrame.Plain)
        self.scrollArea_2.setLineWidth(0)
        self.scrollArea_2.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea_2.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 284, 348))
        self.verticalLayout_6 = QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.title_1 = QLabel(self.scrollAreaWidgetContents_2)
        self.title_1.setObjectName(u"title_1")
        sizePolicy7 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.title_1.sizePolicy().hasHeightForWidth())
        self.title_1.setSizePolicy(sizePolicy7)
        self.title_1.setMinimumSize(QSize(0, 30))
        self.title_1.setFont(font1)
        self.title_1.setMouseTracking(True)
        self.title_1.setTextFormat(Qt.AutoText)
        self.title_1.setAlignment(Qt.AlignCenter)
        self.title_1.setWordWrap(False)

        self.verticalLayout_6.addWidget(self.title_1)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.name_label = QLabel(self.scrollAreaWidgetContents_2)
        self.name_label.setObjectName(u"name_label")
        sizePolicy2.setHeightForWidth(self.name_label.sizePolicy().hasHeightForWidth())
        self.name_label.setSizePolicy(sizePolicy2)
        self.name_label.setMinimumSize(QSize(0, 30))
        self.name_label.setFont(font4)

        self.horizontalLayout_11.addWidget(self.name_label)

        self.name_input = QLineEdit(self.scrollAreaWidgetContents_2)
        self.name_input.setObjectName(u"name_input")
        sizePolicy7.setHeightForWidth(self.name_input.sizePolicy().hasHeightForWidth())
        self.name_input.setSizePolicy(sizePolicy7)
        self.name_input.setMinimumSize(QSize(0, 30))
        self.name_input.setFont(font2)

        self.horizontalLayout_11.addWidget(self.name_input)

        self.id_label = QLabel(self.scrollAreaWidgetContents_2)
        self.id_label.setObjectName(u"id_label")
        sizePolicy2.setHeightForWidth(self.id_label.sizePolicy().hasHeightForWidth())
        self.id_label.setSizePolicy(sizePolicy2)
        self.id_label.setMinimumSize(QSize(0, 30))
        self.id_label.setFont(font4)

        self.horizontalLayout_11.addWidget(self.id_label)

        self.id_input = QLineEdit(self.scrollAreaWidgetContents_2)
        self.id_input.setObjectName(u"id_input")
        sizePolicy7.setHeightForWidth(self.id_input.sizePolicy().hasHeightForWidth())
        self.id_input.setSizePolicy(sizePolicy7)
        self.id_input.setMinimumSize(QSize(0, 30))
        self.id_input.setFont(font2)

        self.horizontalLayout_11.addWidget(self.id_input)

        self.horizontalLayout_11.setStretch(0, 1)
        self.horizontalLayout_11.setStretch(1, 4)
        self.horizontalLayout_11.setStretch(2, 1)
        self.horizontalLayout_11.setStretch(3, 4)

        self.verticalLayout_6.addLayout(self.horizontalLayout_11)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.academy_label = QLabel(self.scrollAreaWidgetContents_2)
        self.academy_label.setObjectName(u"academy_label")
        sizePolicy2.setHeightForWidth(self.academy_label.sizePolicy().hasHeightForWidth())
        self.academy_label.setSizePolicy(sizePolicy2)
        self.academy_label.setMinimumSize(QSize(0, 30))
        self.academy_label.setFont(font4)

        self.horizontalLayout_12.addWidget(self.academy_label)

        self.school_select = QComboBox(self.scrollAreaWidgetContents_2)
        self.school_select.setObjectName(u"school_select")
        sizePolicy2.setHeightForWidth(self.school_select.sizePolicy().hasHeightForWidth())
        self.school_select.setSizePolicy(sizePolicy2)
        self.school_select.setMinimumSize(QSize(0, 30))
        self.school_select.setFont(font2)

        self.horizontalLayout_12.addWidget(self.school_select)

        self.major_label = QLabel(self.scrollAreaWidgetContents_2)
        self.major_label.setObjectName(u"major_label")
        sizePolicy2.setHeightForWidth(self.major_label.sizePolicy().hasHeightForWidth())
        self.major_label.setSizePolicy(sizePolicy2)
        self.major_label.setMinimumSize(QSize(0, 30))
        self.major_label.setFont(font4)

        self.horizontalLayout_12.addWidget(self.major_label)

        self.major_select = QComboBox(self.scrollAreaWidgetContents_2)
        self.major_select.setObjectName(u"major_select")
        sizePolicy2.setHeightForWidth(self.major_select.sizePolicy().hasHeightForWidth())
        self.major_select.setSizePolicy(sizePolicy2)
        self.major_select.setMinimumSize(QSize(0, 30))
        self.major_select.setFont(font2)

        self.horizontalLayout_12.addWidget(self.major_select)

        self.horizontalLayout_12.setStretch(0, 1)
        self.horizontalLayout_12.setStretch(1, 4)
        self.horizontalLayout_12.setStretch(2, 1)
        self.horizontalLayout_12.setStretch(3, 4)

        self.verticalLayout_6.addLayout(self.horizontalLayout_12)

        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.grade_label = QLabel(self.scrollAreaWidgetContents_2)
        self.grade_label.setObjectName(u"grade_label")
        sizePolicy2.setHeightForWidth(self.grade_label.sizePolicy().hasHeightForWidth())
        self.grade_label.setSizePolicy(sizePolicy2)
        self.grade_label.setMinimumSize(QSize(0, 30))
        self.grade_label.setFont(font4)

        self.horizontalLayout_19.addWidget(self.grade_label)

        self.grade_input = QLineEdit(self.scrollAreaWidgetContents_2)
        self.grade_input.setObjectName(u"grade_input")
        sizePolicy7.setHeightForWidth(self.grade_input.sizePolicy().hasHeightForWidth())
        self.grade_input.setSizePolicy(sizePolicy7)
        self.grade_input.setMinimumSize(QSize(0, 30))
        self.grade_input.setFont(font2)

        self.horizontalLayout_19.addWidget(self.grade_input)

        self.banji_label = QLabel(self.scrollAreaWidgetContents_2)
        self.banji_label.setObjectName(u"banji_label")
        sizePolicy2.setHeightForWidth(self.banji_label.sizePolicy().hasHeightForWidth())
        self.banji_label.setSizePolicy(sizePolicy2)
        self.banji_label.setMinimumSize(QSize(0, 30))
        self.banji_label.setFont(font4)
        self.banji_label.setStyleSheet(u"")

        self.horizontalLayout_19.addWidget(self.banji_label)

        self.banji_input = QLineEdit(self.scrollAreaWidgetContents_2)
        self.banji_input.setObjectName(u"banji_input")
        sizePolicy7.setHeightForWidth(self.banji_input.sizePolicy().hasHeightForWidth())
        self.banji_input.setSizePolicy(sizePolicy7)
        self.banji_input.setMinimumSize(QSize(0, 30))
        self.banji_input.setFont(font2)
        self.banji_input.setStyleSheet(u"")
        self.banji_input.setFrame(True)
        self.banji_input.setDragEnabled(False)
        self.banji_input.setReadOnly(False)

        self.horizontalLayout_19.addWidget(self.banji_input)

        self.horizontalLayout_19.setStretch(0, 1)
        self.horizontalLayout_19.setStretch(1, 4)
        self.horizontalLayout_19.setStretch(2, 1)
        self.horizontalLayout_19.setStretch(3, 4)

        self.verticalLayout_6.addLayout(self.horizontalLayout_19)

        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.title_label = QLabel(self.scrollAreaWidgetContents_2)
        self.title_label.setObjectName(u"title_label")
        sizePolicy2.setHeightForWidth(self.title_label.sizePolicy().hasHeightForWidth())
        self.title_label.setSizePolicy(sizePolicy2)
        self.title_label.setMinimumSize(QSize(0, 30))
        self.title_label.setFont(font4)

        self.horizontalLayout_20.addWidget(self.title_label)

        self.title_input = QLineEdit(self.scrollAreaWidgetContents_2)
        self.title_input.setObjectName(u"title_input")
        sizePolicy7.setHeightForWidth(self.title_input.sizePolicy().hasHeightForWidth())
        self.title_input.setSizePolicy(sizePolicy7)
        self.title_input.setMinimumSize(QSize(0, 30))
        self.title_input.setFont(font2)

        self.horizontalLayout_20.addWidget(self.title_input)

        self.horizontalLayout_20.setStretch(0, 1)
        self.horizontalLayout_20.setStretch(1, 4)

        self.verticalLayout_6.addLayout(self.horizontalLayout_20)

        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.teacher_label = QLabel(self.scrollAreaWidgetContents_2)
        self.teacher_label.setObjectName(u"teacher_label")
        sizePolicy2.setHeightForWidth(self.teacher_label.sizePolicy().hasHeightForWidth())
        self.teacher_label.setSizePolicy(sizePolicy2)
        self.teacher_label.setMinimumSize(QSize(0, 30))
        self.teacher_label.setFont(font4)

        self.horizontalLayout_21.addWidget(self.teacher_label)

        self.teacher_input = QLineEdit(self.scrollAreaWidgetContents_2)
        self.teacher_input.setObjectName(u"teacher_input")
        self.teacher_input.setEnabled(True)
        sizePolicy7.setHeightForWidth(self.teacher_input.sizePolicy().hasHeightForWidth())
        self.teacher_input.setSizePolicy(sizePolicy7)
        self.teacher_input.setMinimumSize(QSize(0, 30))
        self.teacher_input.setFont(font2)

        self.horizontalLayout_21.addWidget(self.teacher_input)

        self.zhichen_label = QLabel(self.scrollAreaWidgetContents_2)
        self.zhichen_label.setObjectName(u"zhichen_label")
        sizePolicy2.setHeightForWidth(self.zhichen_label.sizePolicy().hasHeightForWidth())
        self.zhichen_label.setSizePolicy(sizePolicy2)
        self.zhichen_label.setMinimumSize(QSize(0, 30))
        self.zhichen_label.setFont(font4)
        self.zhichen_label.setStyleSheet(u"")

        self.horizontalLayout_21.addWidget(self.zhichen_label)

        self.zhichen_input = QLineEdit(self.scrollAreaWidgetContents_2)
        self.zhichen_input.setObjectName(u"zhichen_input")
        sizePolicy7.setHeightForWidth(self.zhichen_input.sizePolicy().hasHeightForWidth())
        self.zhichen_input.setSizePolicy(sizePolicy7)
        self.zhichen_input.setMinimumSize(QSize(0, 30))
        self.zhichen_input.setFont(font2)
        self.zhichen_input.setStyleSheet(u"")

        self.horizontalLayout_21.addWidget(self.zhichen_input)

        self.horizontalLayout_21.setStretch(0, 1)
        self.horizontalLayout_21.setStretch(1, 4)
        self.horizontalLayout_21.setStretch(2, 1)
        self.horizontalLayout_21.setStretch(3, 4)

        self.verticalLayout_6.addLayout(self.horizontalLayout_21)

        self.line = QFrame(self.scrollAreaWidgetContents_2)
        self.line.setObjectName(u"line")
        sizePolicy5.setHeightForWidth(self.line.sizePolicy().hasHeightForWidth())
        self.line.setSizePolicy(sizePolicy5)
        self.line.setMinimumSize(QSize(0, 30))
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_6.addWidget(self.line)

        self.horizontalLayout_22 = QHBoxLayout()
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.output_label = QLabel(self.scrollAreaWidgetContents_2)
        self.output_label.setObjectName(u"output_label")
        sizePolicy2.setHeightForWidth(self.output_label.sizePolicy().hasHeightForWidth())
        self.output_label.setSizePolicy(sizePolicy2)
        self.output_label.setMinimumSize(QSize(0, 30))
        self.output_label.setFont(font4)

        self.horizontalLayout_22.addWidget(self.output_label)

        self.output_input = QLineEdit(self.scrollAreaWidgetContents_2)
        self.output_input.setObjectName(u"output_input")
        sizePolicy7.setHeightForWidth(self.output_input.sizePolicy().hasHeightForWidth())
        self.output_input.setSizePolicy(sizePolicy7)
        self.output_input.setMinimumSize(QSize(0, 30))
        self.output_input.setFont(font2)
        self.output_input.setReadOnly(True)

        self.horizontalLayout_22.addWidget(self.output_input)

        self.choice_tem_out_path = QPushButton(self.scrollAreaWidgetContents_2)
        self.choice_tem_out_path.setObjectName(u"choice_tem_out_path")
        sizePolicy8 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.choice_tem_out_path.sizePolicy().hasHeightForWidth())
        self.choice_tem_out_path.setSizePolicy(sizePolicy8)
        self.choice_tem_out_path.setMinimumSize(QSize(75, 30))
        self.choice_tem_out_path.setFont(font2)

        self.horizontalLayout_22.addWidget(self.choice_tem_out_path)

        self.horizontalLayout_22.setStretch(0, 1)
        self.horizontalLayout_22.setStretch(1, 4)

        self.verticalLayout_6.addLayout(self.horizontalLayout_22)

        self.run_button = QPushButton(self.scrollAreaWidgetContents_2)
        self.run_button.setObjectName(u"run_button")
        sizePolicy7.setHeightForWidth(self.run_button.sizePolicy().hasHeightForWidth())
        self.run_button.setSizePolicy(sizePolicy7)
        self.run_button.setMinimumSize(QSize(0, 30))
        self.run_button.setFont(font2)

        self.verticalLayout_6.addWidget(self.run_button)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)

        self.gridLayout_6.addWidget(self.scrollArea_2, 0, 0, 1, 1)

        self.main_widget.addWidget(self.template_generation_2)
        self.signature_fill_2 = QWidget()
        self.signature_fill_2.setObjectName(u"signature_fill_2")
        self.verticalLayout_5 = QVBoxLayout(self.signature_fill_2)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.title_2 = QLabel(self.signature_fill_2)
        self.title_2.setObjectName(u"title_2")
        self.title_2.setMinimumSize(QSize(0, 30))
        self.title_2.setFont(font1)
        self.title_2.setMouseTracking(True)
        self.title_2.setTextFormat(Qt.AutoText)
        self.title_2.setAlignment(Qt.AlignCenter)
        self.title_2.setWordWrap(False)

        self.verticalLayout_5.addWidget(self.title_2)

        self.path_label = QLabel(self.signature_fill_2)
        self.path_label.setObjectName(u"path_label")
        self.path_label.setFont(font4)

        self.verticalLayout_5.addWidget(self.path_label)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.sig_file_list = QListWidget(self.signature_fill_2)
        self.sig_file_list.setObjectName(u"sig_file_list")
        self.sig_file_list.setFont(font2)

        self.horizontalLayout_10.addWidget(self.sig_file_list)

        self.choice_sig_path = QPushButton(self.signature_fill_2)
        self.choice_sig_path.setObjectName(u"choice_sig_path")
        sizePolicy9 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy9.setHorizontalStretch(0)
        sizePolicy9.setVerticalStretch(0)
        sizePolicy9.setHeightForWidth(self.choice_sig_path.sizePolicy().hasHeightForWidth())
        self.choice_sig_path.setSizePolicy(sizePolicy9)
        self.choice_sig_path.setMinimumSize(QSize(75, 0))
        self.choice_sig_path.setFont(font2)

        self.horizontalLayout_10.addWidget(self.choice_sig_path)


        self.verticalLayout_5.addLayout(self.horizontalLayout_10)

        self.run_signature = QPushButton(self.signature_fill_2)
        self.run_signature.setObjectName(u"run_signature")
        sizePolicy7.setHeightForWidth(self.run_signature.sizePolicy().hasHeightForWidth())
        self.run_signature.setSizePolicy(sizePolicy7)
        self.run_signature.setMinimumSize(QSize(0, 30))
        self.run_signature.setFont(font2)

        self.verticalLayout_5.addWidget(self.run_signature)

        self.main_widget.addWidget(self.signature_fill_2)
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.verticalLayout_10 = QVBoxLayout(self.page)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.title_4 = QLabel(self.page)
        self.title_4.setObjectName(u"title_4")
        self.title_4.setMinimumSize(QSize(0, 30))
        self.title_4.setFont(font1)
        self.title_4.setMouseTracking(True)
        self.title_4.setTextFormat(Qt.AutoText)
        self.title_4.setAlignment(Qt.AlignCenter)
        self.title_4.setWordWrap(False)

        self.verticalLayout_10.addWidget(self.title_4)

        self.scrollArea = QScrollArea(self.page)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setFrameShape(QFrame.NoFrame)
        self.scrollArea.setFrameShadow(QFrame.Plain)
        self.scrollArea.setLineWidth(0)
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 369, 325))
        sizePolicy10 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy10.setHorizontalStretch(0)
        sizePolicy10.setVerticalStretch(0)
        sizePolicy10.setHeightForWidth(self.scrollAreaWidgetContents.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents.setSizePolicy(sizePolicy10)
        self.scrollAreaWidgetContents.setMinimumSize(QSize(0, 0))
        self.gridLayout_3 = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.tabWidget = QTabWidget(self.scrollAreaWidgetContents)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setFont(font2)
        self.tabWidget.setAutoFillBackground(False)
        self.tabWidget.setStyleSheet(u" QLineEdit{\n"
"                background: #F5F5F7;\n"
"                    border-radius: 5px;\n"
"                }\n"
"                QLineEdit:hover{\n"
"                    background: #F5F5F7;\n"
"                    border: 2px solid #80BEFC;\n"
"                    border-radius: 5px\n"
"                }\n"
"\n"
"                QLineEdit:focus{\n"
"                    background: #FFFFFF;\n"
"                    border: 2px solid #80BEFC;\n"
"                    border-radius: 5px;\n"
"                }")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.tab.setStyleSheet(u" QLineEdit{\n"
"                background: #F5F5F7;\n"
"                    border-radius: 5px;\n"
"                }\n"
"                QLineEdit:hover{\n"
"                    background: #F5F5F7;\n"
"                    border: 2px solid #80BEFC;\n"
"                    border-radius: 5px\n"
"                }\n"
"\n"
"                QLineEdit:focus{\n"
"                    background: #FFFFFF;\n"
"                    border: 2px solid #80BEFC;\n"
"                    border-radius: 5px;\n"
"                }")
        self.gridLayout_4 = QGridLayout(self.tab)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.label = QLabel(self.tab)
        self.label.setObjectName(u"label")
        self.label.setFont(font2)

        self.gridLayout_4.addWidget(self.label, 0, 0, 1, 1)

        self.com_1_1 = QLineEdit(self.tab)
        self.com_1_1.setObjectName(u"com_1_1")
        self.com_1_1.setMinimumSize(QSize(0, 30))
        self.com_1_1.setFont(font2)

        self.gridLayout_4.addWidget(self.com_1_1, 0, 1, 1, 1)

        self.label_6 = QLabel(self.tab)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font2)

        self.gridLayout_4.addWidget(self.label_6, 0, 2, 1, 1)

        self.com_1_6 = QLineEdit(self.tab)
        self.com_1_6.setObjectName(u"com_1_6")
        self.com_1_6.setMinimumSize(QSize(0, 30))
        self.com_1_6.setFont(font2)

        self.gridLayout_4.addWidget(self.com_1_6, 0, 3, 1, 1)

        self.label_2 = QLabel(self.tab)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font2)

        self.gridLayout_4.addWidget(self.label_2, 1, 0, 1, 1)

        self.com_1_2 = QLineEdit(self.tab)
        self.com_1_2.setObjectName(u"com_1_2")
        self.com_1_2.setMinimumSize(QSize(0, 30))
        self.com_1_2.setFont(font2)

        self.gridLayout_4.addWidget(self.com_1_2, 1, 1, 1, 1)

        self.label_7 = QLabel(self.tab)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font2)
        self.label_7.setWordWrap(True)

        self.gridLayout_4.addWidget(self.label_7, 1, 2, 1, 1)

        self.com_1_7 = QLineEdit(self.tab)
        self.com_1_7.setObjectName(u"com_1_7")
        self.com_1_7.setMinimumSize(QSize(0, 30))
        self.com_1_7.setFont(font2)

        self.gridLayout_4.addWidget(self.com_1_7, 1, 3, 1, 1)

        self.label_3 = QLabel(self.tab)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font2)

        self.gridLayout_4.addWidget(self.label_3, 2, 0, 1, 1)

        self.com_1_3 = QLineEdit(self.tab)
        self.com_1_3.setObjectName(u"com_1_3")
        self.com_1_3.setMinimumSize(QSize(0, 30))
        self.com_1_3.setFont(font2)

        self.gridLayout_4.addWidget(self.com_1_3, 2, 1, 1, 1)

        self.label_8 = QLabel(self.tab)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font2)

        self.gridLayout_4.addWidget(self.label_8, 2, 2, 1, 1)

        self.com_1_8 = QLineEdit(self.tab)
        self.com_1_8.setObjectName(u"com_1_8")
        self.com_1_8.setMinimumSize(QSize(0, 30))
        self.com_1_8.setFont(font2)

        self.gridLayout_4.addWidget(self.com_1_8, 2, 3, 1, 1)

        self.label_4 = QLabel(self.tab)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font2)
        self.label_4.setWordWrap(True)

        self.gridLayout_4.addWidget(self.label_4, 3, 0, 1, 1)

        self.com_1_4 = QLineEdit(self.tab)
        self.com_1_4.setObjectName(u"com_1_4")
        self.com_1_4.setMinimumSize(QSize(0, 30))
        self.com_1_4.setFont(font2)

        self.gridLayout_4.addWidget(self.com_1_4, 3, 1, 1, 1)

        self.label_9 = QLabel(self.tab)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font2)
        self.label_9.setWordWrap(True)

        self.gridLayout_4.addWidget(self.label_9, 3, 2, 1, 1)

        self.com_1_9 = QLineEdit(self.tab)
        self.com_1_9.setObjectName(u"com_1_9")
        self.com_1_9.setMinimumSize(QSize(0, 30))
        self.com_1_9.setFont(font2)

        self.gridLayout_4.addWidget(self.com_1_9, 3, 3, 1, 1)

        self.label_5 = QLabel(self.tab)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font2)
        self.label_5.setWordWrap(True)

        self.gridLayout_4.addWidget(self.label_5, 4, 0, 1, 1)

        self.com_1_5 = QLineEdit(self.tab)
        self.com_1_5.setObjectName(u"com_1_5")
        self.com_1_5.setMinimumSize(QSize(0, 30))
        self.com_1_5.setFont(font2)

        self.gridLayout_4.addWidget(self.com_1_5, 4, 1, 1, 1)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.tab_2.setStyleSheet(u" QLineEdit{\n"
"                background: #F5F5F7;\n"
"                    border-radius: 5px;\n"
"                }\n"
"                QLineEdit:hover{\n"
"                    background: #F5F5F7;\n"
"                    border: 2px solid #80BEFC;\n"
"                    border-radius: 5px\n"
"                }\n"
"\n"
"                QLineEdit:focus{\n"
"                    background: #FFFFFF;\n"
"                    border: 2px solid #80BEFC;\n"
"                    border-radius: 5px;\n"
"                }")
        self.gridLayout_5 = QGridLayout(self.tab_2)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.label_12 = QLabel(self.tab_2)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font2)
        self.label_12.setWordWrap(True)

        self.gridLayout_5.addWidget(self.label_12, 0, 0, 1, 1)

        self.com_2_1 = QLineEdit(self.tab_2)
        self.com_2_1.setObjectName(u"com_2_1")
        self.com_2_1.setMinimumSize(QSize(0, 30))
        self.com_2_1.setFont(font2)

        self.gridLayout_5.addWidget(self.com_2_1, 0, 1, 1, 1)

        self.label_15 = QLabel(self.tab_2)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setFont(font2)
        self.label_15.setWordWrap(True)

        self.gridLayout_5.addWidget(self.label_15, 0, 2, 1, 1)

        self.com_2_5 = QLineEdit(self.tab_2)
        self.com_2_5.setObjectName(u"com_2_5")
        self.com_2_5.setMinimumSize(QSize(0, 30))
        self.com_2_5.setFont(font2)

        self.gridLayout_5.addWidget(self.com_2_5, 0, 3, 1, 1)

        self.label_18 = QLabel(self.tab_2)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setFont(font2)
        self.label_18.setWordWrap(True)

        self.gridLayout_5.addWidget(self.label_18, 1, 0, 1, 1)

        self.com_2_2 = QLineEdit(self.tab_2)
        self.com_2_2.setObjectName(u"com_2_2")
        self.com_2_2.setMinimumSize(QSize(0, 30))
        self.com_2_2.setFont(font2)

        self.gridLayout_5.addWidget(self.com_2_2, 1, 1, 1, 1)

        self.label_10 = QLabel(self.tab_2)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font2)
        self.label_10.setWordWrap(True)

        self.gridLayout_5.addWidget(self.label_10, 1, 2, 1, 1)

        self.com_2_6 = QLineEdit(self.tab_2)
        self.com_2_6.setObjectName(u"com_2_6")
        self.com_2_6.setMinimumSize(QSize(0, 30))
        self.com_2_6.setFont(font2)

        self.gridLayout_5.addWidget(self.com_2_6, 1, 3, 1, 1)

        self.label_11 = QLabel(self.tab_2)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font2)

        self.gridLayout_5.addWidget(self.label_11, 2, 0, 1, 1)

        self.com_2_3 = QLineEdit(self.tab_2)
        self.com_2_3.setObjectName(u"com_2_3")
        self.com_2_3.setMinimumSize(QSize(0, 30))
        self.com_2_3.setFont(font2)

        self.gridLayout_5.addWidget(self.com_2_3, 2, 1, 1, 1)

        self.label_13 = QLabel(self.tab_2)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setFont(font2)
        self.label_13.setWordWrap(True)

        self.gridLayout_5.addWidget(self.label_13, 2, 2, 1, 1)

        self.com_2_7 = QLineEdit(self.tab_2)
        self.com_2_7.setObjectName(u"com_2_7")
        self.com_2_7.setMinimumSize(QSize(0, 30))
        self.com_2_7.setFont(font2)

        self.gridLayout_5.addWidget(self.com_2_7, 2, 3, 1, 1)

        self.label_16 = QLabel(self.tab_2)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setFont(font2)
        self.label_16.setWordWrap(True)

        self.gridLayout_5.addWidget(self.label_16, 3, 0, 1, 1)

        self.com_2_4 = QLineEdit(self.tab_2)
        self.com_2_4.setObjectName(u"com_2_4")
        self.com_2_4.setMinimumSize(QSize(0, 30))
        self.com_2_4.setFont(font2)

        self.gridLayout_5.addWidget(self.com_2_4, 3, 1, 1, 1)

        self.label_17 = QLabel(self.tab_2)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setFont(font2)
        self.label_17.setWordWrap(True)

        self.gridLayout_5.addWidget(self.label_17, 3, 2, 1, 1)

        self.com_2_8 = QLineEdit(self.tab_2)
        self.com_2_8.setObjectName(u"com_2_8")
        self.com_2_8.setMinimumSize(QSize(0, 30))
        self.com_2_8.setFont(font2)

        self.gridLayout_5.addWidget(self.com_2_8, 3, 3, 1, 1)

        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.tab_3.setStyleSheet(u" QLineEdit{\n"
"                background: #F5F5F7;\n"
"                    border-radius: 5px;\n"
"                }\n"
"                QLineEdit:hover{\n"
"                    background: #F5F5F7;\n"
"                    border: 2px solid #80BEFC;\n"
"                    border-radius: 5px\n"
"                }\n"
"\n"
"                QLineEdit:focus{\n"
"                    background: #FFFFFF;\n"
"                    border: 2px solid #80BEFC;\n"
"                    border-radius: 5px;\n"
"                }")
        self.gridLayout_7 = QGridLayout(self.tab_3)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.label_24 = QLabel(self.tab_3)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setFont(font2)
        self.label_24.setWordWrap(True)

        self.gridLayout_7.addWidget(self.label_24, 0, 0, 1, 1)

        self.com_3_1 = QLineEdit(self.tab_3)
        self.com_3_1.setObjectName(u"com_3_1")
        self.com_3_1.setMinimumSize(QSize(0, 30))
        self.com_3_1.setFont(font2)

        self.gridLayout_7.addWidget(self.com_3_1, 0, 1, 1, 1)

        self.label_22 = QLabel(self.tab_3)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setFont(font2)
        self.label_22.setWordWrap(True)

        self.gridLayout_7.addWidget(self.label_22, 0, 2, 1, 1)

        self.com_3_6 = QLineEdit(self.tab_3)
        self.com_3_6.setObjectName(u"com_3_6")
        self.com_3_6.setMinimumSize(QSize(0, 30))
        self.com_3_6.setFont(font2)

        self.gridLayout_7.addWidget(self.com_3_6, 0, 3, 1, 1)

        self.label_23 = QLabel(self.tab_3)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setFont(font2)
        self.label_23.setWordWrap(True)

        self.gridLayout_7.addWidget(self.label_23, 1, 0, 1, 1)

        self.com_3_2 = QLineEdit(self.tab_3)
        self.com_3_2.setObjectName(u"com_3_2")
        self.com_3_2.setMinimumSize(QSize(0, 30))
        self.com_3_2.setFont(font2)

        self.gridLayout_7.addWidget(self.com_3_2, 1, 1, 1, 1)

        self.label_14 = QLabel(self.tab_3)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setFont(font2)
        self.label_14.setWordWrap(True)

        self.gridLayout_7.addWidget(self.label_14, 1, 2, 1, 1)

        self.com_3_7 = QLineEdit(self.tab_3)
        self.com_3_7.setObjectName(u"com_3_7")
        self.com_3_7.setMinimumSize(QSize(0, 30))
        self.com_3_7.setFont(font2)

        self.gridLayout_7.addWidget(self.com_3_7, 1, 3, 1, 1)

        self.label_19 = QLabel(self.tab_3)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setFont(font2)
        self.label_19.setWordWrap(True)

        self.gridLayout_7.addWidget(self.label_19, 2, 0, 1, 1)

        self.com_3_3 = QLineEdit(self.tab_3)
        self.com_3_3.setObjectName(u"com_3_3")
        self.com_3_3.setMinimumSize(QSize(0, 30))
        self.com_3_3.setFont(font2)

        self.gridLayout_7.addWidget(self.com_3_3, 2, 1, 1, 1)

        self.label_21 = QLabel(self.tab_3)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setFont(font2)
        self.label_21.setWordWrap(True)

        self.gridLayout_7.addWidget(self.label_21, 2, 2, 1, 1)

        self.com_3_8 = QLineEdit(self.tab_3)
        self.com_3_8.setObjectName(u"com_3_8")
        self.com_3_8.setMinimumSize(QSize(0, 30))
        self.com_3_8.setFont(font2)

        self.gridLayout_7.addWidget(self.com_3_8, 2, 3, 1, 1)

        self.label_25 = QLabel(self.tab_3)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setFont(font2)
        self.label_25.setWordWrap(True)

        self.gridLayout_7.addWidget(self.label_25, 3, 0, 1, 1)

        self.com_3_4 = QLineEdit(self.tab_3)
        self.com_3_4.setObjectName(u"com_3_4")
        self.com_3_4.setMinimumSize(QSize(0, 30))
        self.com_3_4.setFont(font2)

        self.gridLayout_7.addWidget(self.com_3_4, 3, 1, 1, 1)

        self.label_26 = QLabel(self.tab_3)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setFont(font2)
        self.label_26.setWordWrap(True)

        self.gridLayout_7.addWidget(self.label_26, 3, 2, 1, 1)

        self.com_3_9 = QLineEdit(self.tab_3)
        self.com_3_9.setObjectName(u"com_3_9")
        self.com_3_9.setMinimumSize(QSize(0, 30))
        self.com_3_9.setFont(font2)

        self.gridLayout_7.addWidget(self.com_3_9, 3, 3, 1, 1)

        self.label_20 = QLabel(self.tab_3)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setFont(font2)
        self.label_20.setWordWrap(True)

        self.gridLayout_7.addWidget(self.label_20, 4, 0, 1, 1)

        self.com_3_5 = QLineEdit(self.tab_3)
        self.com_3_5.setObjectName(u"com_3_5")
        self.com_3_5.setMinimumSize(QSize(0, 30))
        self.com_3_5.setFont(font2)

        self.gridLayout_7.addWidget(self.com_3_5, 4, 1, 1, 1)

        self.label_27 = QLabel(self.tab_3)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setFont(font2)
        self.label_27.setWordWrap(True)

        self.gridLayout_7.addWidget(self.label_27, 4, 2, 1, 1)

        self.com_3_10 = QLineEdit(self.tab_3)
        self.com_3_10.setObjectName(u"com_3_10")
        self.com_3_10.setMinimumSize(QSize(0, 30))
        self.com_3_10.setFont(font2)

        self.gridLayout_7.addWidget(self.com_3_10, 4, 3, 1, 1)

        self.tabWidget.addTab(self.tab_3, "")

        self.gridLayout_3.addWidget(self.tabWidget, 0, 0, 1, 1)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_10.addWidget(self.scrollArea)

        self.horizontalLayout_23 = QHBoxLayout()
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.output_label_3 = QLabel(self.page)
        self.output_label_3.setObjectName(u"output_label_3")
        self.output_label_3.setMinimumSize(QSize(0, 30))
        self.output_label_3.setFont(font4)

        self.horizontalLayout_23.addWidget(self.output_label_3)

        self.ass_out_path = QLineEdit(self.page)
        self.ass_out_path.setObjectName(u"ass_out_path")
        self.ass_out_path.setMinimumSize(QSize(0, 30))
        self.ass_out_path.setMaximumSize(QSize(16777215, 30))
        self.ass_out_path.setFont(font2)
        self.ass_out_path.setReadOnly(True)

        self.horizontalLayout_23.addWidget(self.ass_out_path)

        self.choice_ass_out_path = QPushButton(self.page)
        self.choice_ass_out_path.setObjectName(u"choice_ass_out_path")
        sizePolicy8.setHeightForWidth(self.choice_ass_out_path.sizePolicy().hasHeightForWidth())
        self.choice_ass_out_path.setSizePolicy(sizePolicy8)
        self.choice_ass_out_path.setMinimumSize(QSize(75, 30))

        self.horizontalLayout_23.addWidget(self.choice_ass_out_path)

        self.horizontalLayout_23.setStretch(0, 1)
        self.horizontalLayout_23.setStretch(1, 4)

        self.verticalLayout_10.addLayout(self.horizontalLayout_23)

        self.run_ass = QPushButton(self.page)
        self.run_ass.setObjectName(u"run_ass")
        sizePolicy7.setHeightForWidth(self.run_ass.sizePolicy().hasHeightForWidth())
        self.run_ass.setSizePolicy(sizePolicy7)
        self.run_ass.setMinimumSize(QSize(0, 30))
        self.run_ass.setFont(font2)

        self.verticalLayout_10.addWidget(self.run_ass)

        self.main_widget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.verticalLayout_3 = QVBoxLayout(self.page_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.title_3 = QLabel(self.page_2)
        self.title_3.setObjectName(u"title_3")
        self.title_3.setMinimumSize(QSize(0, 30))
        self.title_3.setFont(font1)
        self.title_3.setMouseTracking(True)
        self.title_3.setTextFormat(Qt.AutoText)
        self.title_3.setAlignment(Qt.AlignCenter)
        self.title_3.setWordWrap(False)

        self.verticalLayout_3.addWidget(self.title_3)

        self.output_label_4 = QLabel(self.page_2)
        self.output_label_4.setObjectName(u"output_label_4")
        self.output_label_4.setFont(font4)

        self.verticalLayout_3.addWidget(self.output_label_4)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.merge_file_list = QListWidget(self.page_2)
        self.merge_file_list.setObjectName(u"merge_file_list")
        self.merge_file_list.setFont(font2)

        self.horizontalLayout_8.addWidget(self.merge_file_list)

        self.choice_total_file_path = QPushButton(self.page_2)
        self.choice_total_file_path.setObjectName(u"choice_total_file_path")
        sizePolicy11 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        sizePolicy11.setHorizontalStretch(0)
        sizePolicy11.setVerticalStretch(0)
        sizePolicy11.setHeightForWidth(self.choice_total_file_path.sizePolicy().hasHeightForWidth())
        self.choice_total_file_path.setSizePolicy(sizePolicy11)
        self.choice_total_file_path.setMinimumSize(QSize(75, 0))
        self.choice_total_file_path.setFont(font2)

        self.horizontalLayout_8.addWidget(self.choice_total_file_path)


        self.verticalLayout_3.addLayout(self.horizontalLayout_8)

        self.output_label_2 = QLabel(self.page_2)
        self.output_label_2.setObjectName(u"output_label_2")
        self.output_label_2.setFont(font4)
        self.output_label_2.setTextFormat(Qt.AutoText)
        self.output_label_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_3.addWidget(self.output_label_2)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.output_input_4 = QLineEdit(self.page_2)
        self.output_input_4.setObjectName(u"output_input_4")
        self.output_input_4.setMinimumSize(QSize(0, 30))
        font5 = QFont()
        font5.setFamily(u"Segoe UI")
        font5.setBold(False)
        font5.setItalic(False)
        font5.setWeight(50)
        self.output_input_4.setFont(font5)
        self.output_input_4.setReadOnly(True)

        self.horizontalLayout_7.addWidget(self.output_input_4)

        self.choice_output_4 = QPushButton(self.page_2)
        self.choice_output_4.setObjectName(u"choice_output_4")
        self.choice_output_4.setEnabled(True)
        sizePolicy8.setHeightForWidth(self.choice_output_4.sizePolicy().hasHeightForWidth())
        self.choice_output_4.setSizePolicy(sizePolicy8)
        self.choice_output_4.setMinimumSize(QSize(75, 30))
        self.choice_output_4.setMaximumSize(QSize(75, 30))
        self.choice_output_4.setFont(font5)

        self.horizontalLayout_7.addWidget(self.choice_output_4)


        self.verticalLayout_3.addLayout(self.horizontalLayout_7)

        self.run_merge = QPushButton(self.page_2)
        self.run_merge.setObjectName(u"run_merge")
        sizePolicy7.setHeightForWidth(self.run_merge.sizePolicy().hasHeightForWidth())
        self.run_merge.setSizePolicy(sizePolicy7)
        self.run_merge.setMinimumSize(QSize(0, 30))
        self.run_merge.setFont(font2)

        self.verticalLayout_3.addWidget(self.run_merge)

        self.main_widget.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.verticalLayout_4 = QVBoxLayout(self.page_3)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.title_5 = QLabel(self.page_3)
        self.title_5.setObjectName(u"title_5")
        self.title_5.setMinimumSize(QSize(0, 30))
        self.title_5.setFont(font1)
        self.title_5.setMouseTracking(True)
        self.title_5.setTextFormat(Qt.AutoText)
        self.title_5.setAlignment(Qt.AlignCenter)
        self.title_5.setWordWrap(False)

        self.verticalLayout_4.addWidget(self.title_5)

        self.path_label_2 = QLabel(self.page_3)
        self.path_label_2.setObjectName(u"path_label_2")
        self.path_label_2.setFont(font4)

        self.verticalLayout_4.addWidget(self.path_label_2)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.doc_file_list = QListWidget(self.page_3)
        self.doc_file_list.setObjectName(u"doc_file_list")

        self.horizontalLayout_9.addWidget(self.doc_file_list)

        self.choice_doc_path = QPushButton(self.page_3)
        self.choice_doc_path.setObjectName(u"choice_doc_path")
        sizePolicy11.setHeightForWidth(self.choice_doc_path.sizePolicy().hasHeightForWidth())
        self.choice_doc_path.setSizePolicy(sizePolicy11)
        self.choice_doc_path.setMinimumSize(QSize(75, 0))

        self.horizontalLayout_9.addWidget(self.choice_doc_path)


        self.verticalLayout_4.addLayout(self.horizontalLayout_9)

        self.run_signature_2 = QPushButton(self.page_3)
        self.run_signature_2.setObjectName(u"run_signature_2")
        sizePolicy7.setHeightForWidth(self.run_signature_2.sizePolicy().hasHeightForWidth())
        self.run_signature_2.setSizePolicy(sizePolicy7)
        self.run_signature_2.setFont(font2)

        self.verticalLayout_4.addWidget(self.run_signature_2)

        self.main_widget.addWidget(self.page_3)

        self.horizontalLayout_6.addWidget(self.main_widget)

        self.Image = QLabel(self.centralwidget)
        self.Image.setObjectName(u"Image")
        self.Image.setEnabled(True)
        sizePolicy12 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Maximum)
        sizePolicy12.setHorizontalStretch(0)
        sizePolicy12.setVerticalStretch(0)
        sizePolicy12.setHeightForWidth(self.Image.sizePolicy().hasHeightForWidth())
        self.Image.setSizePolicy(sizePolicy12)
        self.Image.setMinimumSize(QSize(0, 0))
        self.Image.setMaximumSize(QSize(200, 160000))
        self.Image.setStyleSheet(u"border-image: url(:/back/back_img.png);\n"
"border-radius:5px;")
        self.Image.setScaledContents(False)

        self.horizontalLayout_6.addWidget(self.Image)


        self.verticalLayout_2.addLayout(self.horizontalLayout_6)

        self.verticalLayout_2.setStretch(0, 1)
        self.verticalLayout_2.setStretch(1, 3)

        self.gridLayout_2.addLayout(self.verticalLayout_2, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QToolBar(MainWindow)
        self.toolBar.setObjectName(u"toolBar")
        font6 = QFont()
        font6.setPointSize(10)
        font6.setBold(False)
        font6.setItalic(False)
        font6.setWeight(50)
        self.toolBar.setFont(font6)
        self.toolBar.setAutoFillBackground(False)
        MainWindow.addToolBar(Qt.TopToolBarArea, self.toolBar)
#if QT_CONFIG(shortcut)
        self.current_stu_label.setBuddy(self.choice_stu)
        self.xzcy_sig.setBuddy(self.zdls_add)
        self.xzzz_sig.setBuddy(self.zdls_add)
        self.name_label.setBuddy(self.name_input)
        self.id_label.setBuddy(self.id_input)
        self.grade_label.setBuddy(self.grade_input)
        self.banji_label.setBuddy(self.banji_input)
        self.title_label.setBuddy(self.title_input)
        self.teacher_label.setBuddy(self.teacher_input)
        self.zhichen_label.setBuddy(self.zhichen_input)
        self.output_label.setBuddy(self.output_input)
        self.label.setBuddy(self.com_1_1)
        self.label_6.setBuddy(self.com_1_1)
        self.label_2.setBuddy(self.com_1_2)
        self.label_7.setBuddy(self.com_1_2)
        self.label_3.setBuddy(self.com_1_3)
        self.label_8.setBuddy(self.com_1_3)
        self.label_4.setBuddy(self.com_1_4)
        self.label_9.setBuddy(self.com_1_4)
        self.label_5.setBuddy(self.com_1_5)
        self.label_12.setBuddy(self.com_1_1)
        self.label_15.setBuddy(self.com_1_5)
        self.label_18.setBuddy(self.com_1_2)
        self.label_10.setBuddy(self.com_1_1)
        self.label_11.setBuddy(self.com_1_3)
        self.label_13.setBuddy(self.com_1_2)
        self.label_16.setBuddy(self.com_1_4)
        self.label_17.setBuddy(self.com_1_3)
        self.label_24.setBuddy(self.com_1_1)
        self.label_22.setBuddy(self.com_1_1)
        self.label_23.setBuddy(self.com_1_2)
        self.label_14.setBuddy(self.com_1_2)
        self.label_19.setBuddy(self.com_1_3)
        self.label_21.setBuddy(self.com_1_3)
        self.label_25.setBuddy(self.com_1_4)
        self.label_26.setBuddy(self.com_1_3)
        self.label_20.setBuddy(self.com_1_5)
        self.label_27.setBuddy(self.com_1_3)
        self.output_label_3.setBuddy(self.output_input)
        self.output_label_4.setBuddy(self.output_input)
        self.output_label_2.setBuddy(self.output_input)
#endif // QT_CONFIG(shortcut)
        QWidget.setTabOrder(self.choice_stu, self.name_input)
        QWidget.setTabOrder(self.name_input, self.id_input)
        QWidget.setTabOrder(self.id_input, self.grade_input)
        QWidget.setTabOrder(self.grade_input, self.banji_input)
        QWidget.setTabOrder(self.banji_input, self.title_input)
        QWidget.setTabOrder(self.title_input, self.teacher_input)
        QWidget.setTabOrder(self.teacher_input, self.zhichen_input)
        QWidget.setTabOrder(self.zhichen_input, self.output_input)
        QWidget.setTabOrder(self.output_input, self.run_button)
        QWidget.setTabOrder(self.run_button, self.sig_file_list)
        QWidget.setTabOrder(self.sig_file_list, self.run_signature)
        QWidget.setTabOrder(self.run_signature, self.com_1_1)
        QWidget.setTabOrder(self.com_1_1, self.com_1_2)
        QWidget.setTabOrder(self.com_1_2, self.com_1_3)
        QWidget.setTabOrder(self.com_1_3, self.com_1_4)
        QWidget.setTabOrder(self.com_1_4, self.com_1_5)
        QWidget.setTabOrder(self.com_1_5, self.com_1_6)
        QWidget.setTabOrder(self.com_1_6, self.com_1_7)
        QWidget.setTabOrder(self.com_1_7, self.com_1_8)
        QWidget.setTabOrder(self.com_1_8, self.com_1_9)
        QWidget.setTabOrder(self.com_1_9, self.ass_out_path)
        QWidget.setTabOrder(self.ass_out_path, self.choice_ass_out_path)
        QWidget.setTabOrder(self.choice_ass_out_path, self.run_ass)
        QWidget.setTabOrder(self.run_ass, self.com_2_1)
        QWidget.setTabOrder(self.com_2_1, self.com_2_2)
        QWidget.setTabOrder(self.com_2_2, self.com_2_3)
        QWidget.setTabOrder(self.com_2_3, self.com_2_4)
        QWidget.setTabOrder(self.com_2_4, self.com_2_5)
        QWidget.setTabOrder(self.com_2_5, self.com_2_6)
        QWidget.setTabOrder(self.com_2_6, self.com_2_7)
        QWidget.setTabOrder(self.com_2_7, self.com_2_8)
        QWidget.setTabOrder(self.com_2_8, self.com_3_1)
        QWidget.setTabOrder(self.com_3_1, self.com_3_2)
        QWidget.setTabOrder(self.com_3_2, self.com_3_3)
        QWidget.setTabOrder(self.com_3_3, self.com_3_4)
        QWidget.setTabOrder(self.com_3_4, self.com_3_5)
        QWidget.setTabOrder(self.com_3_5, self.com_3_6)
        QWidget.setTabOrder(self.com_3_6, self.com_3_7)
        QWidget.setTabOrder(self.com_3_7, self.com_3_8)
        QWidget.setTabOrder(self.com_3_8, self.com_3_9)
        QWidget.setTabOrder(self.com_3_9, self.com_3_10)
        QWidget.setTabOrder(self.com_3_10, self.merge_file_list)
        QWidget.setTabOrder(self.merge_file_list, self.choice_total_file_path)
        QWidget.setTabOrder(self.choice_total_file_path, self.output_input_4)
        QWidget.setTabOrder(self.output_input_4, self.choice_output_4)
        QWidget.setTabOrder(self.choice_output_4, self.run_merge)

        self.toolBar.addAction(self.template_generation)
        self.toolBar.addAction(self.signature_fill)
        self.toolBar.addAction(self.assess)
        self.toolBar.addAction(self.merge)
        self.toolBar.addAction(self.doc_to_docx)

        self.retranslateUi(MainWindow)

        self.main_widget.setCurrentIndex(2)
        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.template_generation.setText(QCoreApplication.translate("MainWindow", u"\u6a21\u677f\u751f\u6210", None))
        self.signature_fill.setText(QCoreApplication.translate("MainWindow", u"\u7b7e\u540d\u586b\u5145", None))
        self.assess.setText(QCoreApplication.translate("MainWindow", u"\u5feb\u901f\u8bc4\u5ba1", None))
        self.merge.setText(QCoreApplication.translate("MainWindow", u"\u4e00\u952e\u5408\u5e76", None))
        self.add_stu.setText(QCoreApplication.translate("MainWindow", u"\u4fe1\u606f\u5f55\u5165", None))
        self.doc_to_docx.setText(QCoreApplication.translate("MainWindow", u"doc\u8f6c\u6362", None))
        self.current_stu_label.setText(QCoreApplication.translate("MainWindow", u"\u5f53\u524d\u5b66\u751f:", None))
        self.add_stu_btn.setText(QCoreApplication.translate("MainWindow", u"\u624b\u52a8\u5f55\u5165", None))
        self.login_btn.setText(QCoreApplication.translate("MainWindow", u"\u6279\u91cf\u5bfc\u5165", None))
#if QT_CONFIG(accessibility)
        self.xzcy_sig.setAccessibleDescription("")
#endif // QT_CONFIG(accessibility)
        self.xzcy_sig.setText(QCoreApplication.translate("MainWindow", u"\u5c0f\u7ec4\u6210\u5458\u7535\u5b50\u7b7e\u540d:", None))
        self.xzcy_add.setText(QCoreApplication.translate("MainWindow", u"+", None))
#if QT_CONFIG(accessibility)
        self.xzzz_sig.setAccessibleDescription("")
#endif // QT_CONFIG(accessibility)
        self.xzzz_sig.setText(QCoreApplication.translate("MainWindow", u"\u5c0f\u7ec4\u7ec4\u957f\u7535\u5b50\u7b7e\u540d:", None))
        self.xzzz_add.setText(QCoreApplication.translate("MainWindow", u"+", None))
#if QT_CONFIG(accessibility)
        self.zdls_sig.setAccessibleDescription("")
#endif // QT_CONFIG(accessibility)
        self.zdls_sig.setText(QCoreApplication.translate("MainWindow", u"\u6307\u5bfc\u8001\u5e08\u7535\u5b50\u7b7e\u540d:", None))
        self.zdls_add.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.title_1.setText(QCoreApplication.translate("MainWindow", u"\u5e26\u4e2a\u4eba\u4fe1\u606f\u7684\u6a21\u677f\u6587\u4ef6\u751f\u6210", None))
        self.name_label.setText(QCoreApplication.translate("MainWindow", u"\u59d3\u540d:", None))
        self.id_label.setText(QCoreApplication.translate("MainWindow", u"\u5b66\u53f7:", None))
        self.academy_label.setText(QCoreApplication.translate("MainWindow", u"\u5b66\u9662:", None))
        self.major_label.setText(QCoreApplication.translate("MainWindow", u"\u4e13\u4e1a:", None))
        self.grade_label.setText(QCoreApplication.translate("MainWindow", u"\u5e74\u7ea7:", None))
        self.banji_label.setText(QCoreApplication.translate("MainWindow", u"\u73ed\u7ea7:", None))
        self.banji_input.setText(QCoreApplication.translate("MainWindow", u"\u5982:2019\u7ea7\u6570\u5b57\u5a92\u4f53\u6280\u672f2\u73ed", None))
        self.title_label.setText(QCoreApplication.translate("MainWindow", u"\u6bd5\u4e1a\u8bbe\u8ba1\u9898\u76ee:", None))
        self.teacher_label.setText(QCoreApplication.translate("MainWindow", u"\u6307\u5bfc\u8001\u5e08:", None))
        self.zhichen_label.setText(QCoreApplication.translate("MainWindow", u"\u6307\u5bfc\u8001\u5e08\u804c\u79f0:", None))
        self.output_label.setText(QCoreApplication.translate("MainWindow", u"\u8f93\u51fa\u76ee\u5f55", None))
        self.choice_tem_out_path.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.run_button.setText(QCoreApplication.translate("MainWindow", u"\u751f\u6210", None))
        self.title_2.setText(QCoreApplication.translate("MainWindow", u"\u586b\u5145\u7b7e\u540d", None))
        self.path_label.setText(QCoreApplication.translate("MainWindow", u"\u8bf7\u9009\u62e9\u9700\u8981\u586b\u5145\u7b7e\u540d\u7684\u6587\u4ef6:", None))
        self.choice_sig_path.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.run_signature.setText(QCoreApplication.translate("MainWindow", u"\u586b\u5145\u7b7e\u540d(\u586b\u5145\u7b7e\u540d\u540e\u8986\u76d6\u6e90\u6587\u4ef6)", None))
        self.title_4.setText(QCoreApplication.translate("MainWindow", u"\u5feb\u901f\u8bc4\u5ba1", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"1\u3001\u9009\u9898\u7406\u8bba\u548c\u5b9e\u7528\u6027:", None))
        self.com_1_1.setPlaceholderText(QCoreApplication.translate("MainWindow", u"/10", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"6\u3001\u5bf9\u8bfe\u9898\u7684\u4e86\u89e3\u7a0b\u5ea6:", None))
        self.com_1_6.setPlaceholderText(QCoreApplication.translate("MainWindow", u"/10", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"2\u3001\u9009\u9898\u96be\u5ea6\u548c\u53ef\u884c\u6027:", None))
        self.com_1_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"/10", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"7\u3001\u57fa\u672c\u6982\u5ff5\u6e05\u695a\u3001\u660e\u786e\u9009\u9898\u7684\u610f\u4e49:", None))
        self.com_1_7.setPlaceholderText(QCoreApplication.translate("MainWindow", u"/10", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"3\u3001\u7814\u7a76\u65b9\u6cd5\u7684\u5408\u7406\u6027:", None))
        self.com_1_3.setPlaceholderText(QCoreApplication.translate("MainWindow", u"/15", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"8\u3001\u8bba\u8bc1\u4e25\u5bc6\u3001\u903b\u8f91\u6027\u5f3a:", None))
        self.com_1_8.setPlaceholderText(QCoreApplication.translate("MainWindow", u"/10", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"4\u3001\u5f00\u9898\u62a5\u544a\u7684\u6587\u5b57\u8868\u8fbe,\u53c2\u8003\u6587\u732e\u7684\u5f15\u7528\uff1a", None))
        self.com_1_4.setPlaceholderText(QCoreApplication.translate("MainWindow", u"/15", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"9\u3001\u56de\u7b54\u95ee\u9898\u6761\u7406\u6e05\u6670\u3001\u5e94\u7b54\u5207\u9898:", None))
        self.com_1_9.setPlaceholderText(QCoreApplication.translate("MainWindow", u"/10", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"5\u3001\u8d44\u6599\u51c6\u5907\u7684\u5145\u5206\u6027\uff1a", None))
        self.com_1_5.setPlaceholderText(QCoreApplication.translate("MainWindow", u"/10", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"\u5f00\u9898\u8bc4\u5ba1", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"1\u3001\u5df2\u5b8c\u6210\u7684\u5de5\u4f5c\u91cf\u7b26\u5408\u8fdb\u5ea6\u8981\u6c42:", None))
        self.com_2_1.setPlaceholderText(QCoreApplication.translate("MainWindow", u"/20", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"5\u3001\u80fd\u6e05\u6670\u628a\u63e1\u76ee\u524d\u8bbe\u8ba1\u60c5\u51b5,\u5bf9\u4e0b\u4e00\u6b65\u7684\u4efb\u52a1\u6709\u6e05\u695a\u7684\u8ba4\u8bc6:", None))
        self.com_2_5.setPlaceholderText(QCoreApplication.translate("MainWindow", u"/10", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"2\u3001\u6bd5\u8bbe\u5185\u5bb9\u7b26\u5408\u8bfe\u9898\u8981\u6c42:", None))
        self.com_2_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"/20", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"6\u3001\u5b66\u4e60\u6001\u5ea6\u7aef\u6b63,\u80fd\u591f\u5728\u6bd5\u8bbe\u4e2d\u6295\u5165\u8f83\u591a\u65f6\u95f4\u548c\u7cbe\u529b:", None))
        self.com_2_6.setPlaceholderText(QCoreApplication.translate("MainWindow", u"/10", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"3\u3001\u8d44\u6599\u6536\u96c6\u5145\u5206:", None))
        self.com_2_3.setPlaceholderText(QCoreApplication.translate("MainWindow", u"/10", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"7\u3001\u8bfe\u9898\u9648\u8ff0\u6e05\u6670,\u903b\u8f91\u6027\u5f3a:", None))
        self.com_2_7.setPlaceholderText(QCoreApplication.translate("MainWindow", u"/10", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"4\u3001\u5bf9\u8bfe\u9898\u5185\u5bb9\u7406\u89e3\u6df1\u523b,\u51c6\u786e:", None))
        self.com_2_4.setPlaceholderText(QCoreApplication.translate("MainWindow", u"/10", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"8\u3001\u601d\u7ef4\u7f1c\u5bc6,\u56de\u7b54\u95ee\u9898\u6b63\u786e:", None))
        self.com_2_8.setPlaceholderText(QCoreApplication.translate("MainWindow", u"/10", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"\u4e2d\u671f\u8bc4\u5ba1", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"1\u3001\u8bba\u6587\u7ed3\u6784\u5408\u7406,\u6761\u7406\u6e05\u6670,\u6587\u7b14\u6d41\u7545,\u683c\u5f0f\u89c4\u8303:", None))
        self.com_3_1.setPlaceholderText(QCoreApplication.translate("MainWindow", u"/10", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"6\u3001\u638c\u63e1\u4e86\u76f8\u5173\u7684\u7406\u8bba\u77e5\u8bc6\u548c\u4e13\u4e1a\u6280\u80fd:", None))
        self.com_3_6.setPlaceholderText(QCoreApplication.translate("MainWindow", u"/10", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"2\u3001\u57fa\u672c\u6982\u5ff5\u548c\u57fa\u672c\u539f\u7406\u6e05\u695a\u3001\u6b63\u786e:", None))
        self.com_3_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"/10", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"7\u3001\u5177\u5907\u4e00\u5b9a\u7684\u5206\u6790\u95ee\u9898\u548c\u89e3\u51b3\u95ee\u9898\u7684\u80fd\u529b:", None))
        self.com_3_7.setPlaceholderText(QCoreApplication.translate("MainWindow", u"/10", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"3\u3001\u5b9e\u9a8c\u6570\u636e\u771f\u5b9e\u3001\u7ed3\u8bba\u6b63\u786e:", None))
        self.com_3_3.setPlaceholderText(QCoreApplication.translate("MainWindow", u"/10", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"8\u3001\u5b66\u4e60\u6001\u5ea6\u597d,\u80fd\u591f\u5728\u6bd5\u8bbe\u4e2d\u6295\u5165\u8f83\u591a\u65f6\u95f4\u548c\u7cbe\u529b:", None))
        self.com_3_8.setPlaceholderText(QCoreApplication.translate("MainWindow", u"/10", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"4\u3001\u8bba\u6587\u4e3b\u8981\u5185\u5bb9\u4e3a\u672c\u4eba\u72ec\u7acb\u5b8c\u6210:", None))
        self.com_3_4.setPlaceholderText(QCoreApplication.translate("MainWindow", u"/10", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"9\u3001\u80fd\u591f\u7b80\u660e\u627c\u8981\u3001\u91cd\u70b9\u7a81\u51fa\u5730\u9610\u8ff0\u8bba\u6587\u7684\u4e3b\u8981\u5185\u5bb9", None))
        self.com_3_9.setPlaceholderText(QCoreApplication.translate("MainWindow", u"/10", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"5\u3001\u5b8c\u6210\u4e86\u89c4\u5b9a\u7684\u6bd5\u8bbe\u4efb\u52a1:", None))
        self.com_3_5.setPlaceholderText(QCoreApplication.translate("MainWindow", u"/10", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"10\u3001\u80fd\u591f\u51c6\u786e\u3001\u6d41\u5229\u5730\u56de\u7b54\u8bc4\u5ba1\u8001\u5e08\u63d0\u51fa\u7684\u95ee\u9898:", None))
        self.com_3_10.setPlaceholderText(QCoreApplication.translate("MainWindow", u"/10", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"\u7b54\u8fa9\u8bc4\u5ba1", None))
        self.output_label_3.setText(QCoreApplication.translate("MainWindow", u"\u8f93\u51fa\u76ee\u5f55", None))
        self.choice_ass_out_path.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.run_ass.setText(QCoreApplication.translate("MainWindow", u"\u751f\u6210", None))
        self.title_3.setText(QCoreApplication.translate("MainWindow", u"\u6240\u6709\u6587\u6863\u4e00\u952e\u5408\u5e76\u4e3apdf", None))
        self.output_label_4.setText(QCoreApplication.translate("MainWindow", u"\u9009\u62e9dox/docx\u6587\u4ef6:", None))
        self.choice_total_file_path.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.output_label_2.setText(QCoreApplication.translate("MainWindow", u"\u8f93\u51fa\u76ee\u5f55:", None))
        self.choice_output_4.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.run_merge.setText(QCoreApplication.translate("MainWindow", u"\u751f\u6210", None))
        self.title_5.setText(QCoreApplication.translate("MainWindow", u"doc\u8f6c\u6362\u4e3adocx", None))
        self.path_label_2.setText(QCoreApplication.translate("MainWindow", u"\u8bf7\u9009\u62e9\u9700\u8981\u8f6c\u6362\u7684\u6587\u4ef6:", None))
        self.choice_doc_path.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.run_signature_2.setText(QCoreApplication.translate("MainWindow", u"\u8f6c\u6362\u6587\u4ef6", None))
        self.Image.setText("")
        self.toolBar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
    # retranslateUi

