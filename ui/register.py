# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui\register.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt, QSize,QMetaObject, QCoreApplication
from PyQt5.QtWidgets import QSizePolicy, QWidget, QLabel, \
        QSpacerItem, QComboBox, QPushButton, QLineEdit, QGridLayout,QSizePolicy

class Ui_DockWidget(object):
    def setupUi(self, DockWidget):
        if not DockWidget.objectName():
            DockWidget.setObjectName(u"DockWidget")
        DockWidget.resize(600, 400)
        sizePolicy = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(DockWidget.sizePolicy().hasHeightForWidth())
        DockWidget.setSizePolicy(sizePolicy)
        DockWidget.setFocusPolicy(Qt.NoFocus)
        DockWidget.setContextMenuPolicy(Qt.NoContextMenu)
        DockWidget.setAcceptDrops(False)
        DockWidget.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.dockWidgetContents = QWidget()
        self.dockWidgetContents.setObjectName(u"dockWidgetContents")
        self.gridLayout = QGridLayout(self.dockWidgetContents)
        self.gridLayout.setObjectName(u"gridLayout")
        self.zhichen_input = QLineEdit(self.dockWidgetContents)
        self.zhichen_input.setObjectName(u"zhichen_input")
        self.zhichen_input.setMinimumSize(QSize(0, 30))
        font = QFont()
        font.setFamily(u"Arial")
        font.setPointSize(10)
        self.zhichen_input.setFont(font)

        self.gridLayout.addWidget(self.zhichen_input, 10, 5, 1, 1)

        self.id_label = QLabel(self.dockWidgetContents)
        self.id_label.setObjectName(u"id_label")
        self.id_label.setMinimumSize(QSize(0, 30))
        font1 = QFont()
        font1.setFamily(u"Arial")
        font1.setPointSize(10)
        font1.setKerning(True)
        self.id_label.setFont(font1)

        self.gridLayout.addWidget(self.id_label, 2, 3, 1, 1)

        self.id_input = QLineEdit(self.dockWidgetContents)
        self.id_input.setObjectName(u"id_input")
        self.id_input.setMinimumSize(QSize(0, 30))
        self.id_input.setFont(font)

        self.gridLayout.addWidget(self.id_input, 2, 4, 1, 2)

        self.pushButton = QPushButton(self.dockWidgetContents)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setEnabled(True)
        self.pushButton.setMinimumSize(QSize(0, 30))
        self.pushButton.setFont(font)

        self.gridLayout.addWidget(self.pushButton, 13, 0, 1, 6)

        self.name_input = QLineEdit(self.dockWidgetContents)
        self.name_input.setObjectName(u"name_input")
        self.name_input.setMinimumSize(QSize(0, 30))
        self.name_input.setFont(font)

        self.gridLayout.addWidget(self.name_input, 2, 1, 1, 2)

        self.verticalSpacer_4 = QSpacerItem(20, 5, QSizePolicy.Minimum, QSizePolicy.MinimumExpanding)

        self.gridLayout.addItem(self.verticalSpacer_4, 7, 1, 1, 1)

        self.title_label = QLabel(self.dockWidgetContents)
        self.title_label.setObjectName(u"title_label")
        self.title_label.setMinimumSize(QSize(0, 30))
        self.title_label.setFont(font1)

        self.gridLayout.addWidget(self.title_label, 8, 0, 1, 2)

        self.school_select = QComboBox(self.dockWidgetContents)
        self.school_select.setObjectName(u"school_select")
        self.school_select.setMinimumSize(QSize(0, 30))
        self.school_select.setFont(font)

        self.gridLayout.addWidget(self.school_select, 4, 1, 1, 2)

        self.name_label = QLabel(self.dockWidgetContents)
        self.name_label.setObjectName(u"name_label")
        self.name_label.setMinimumSize(QSize(0, 30))
        self.name_label.setFont(font1)

        self.gridLayout.addWidget(self.name_label, 2, 0, 1, 1)

        self.major_label = QLabel(self.dockWidgetContents)
        self.major_label.setObjectName(u"major_label")
        self.major_label.setMinimumSize(QSize(0, 30))
        self.major_label.setFont(font1)

        self.gridLayout.addWidget(self.major_label, 4, 3, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 5, QSizePolicy.Minimum, QSizePolicy.MinimumExpanding)

        self.gridLayout.addItem(self.verticalSpacer, 1, 1, 1, 1)

        self.title_input = QLineEdit(self.dockWidgetContents)
        self.title_input.setObjectName(u"title_input")
        self.title_input.setMinimumSize(QSize(0, 30))
        self.title_input.setFont(font)

        self.gridLayout.addWidget(self.title_input, 8, 2, 1, 4)

        self.verticalSpacer_6 = QSpacerItem(20, 5, QSizePolicy.Minimum, QSizePolicy.MinimumExpanding)

        self.gridLayout.addItem(self.verticalSpacer_6, 11, 0, 1, 1)

        self.academy_label = QLabel(self.dockWidgetContents)
        self.academy_label.setObjectName(u"academy_label")
        self.academy_label.setMinimumSize(QSize(0, 30))
        self.academy_label.setFont(font1)

        self.gridLayout.addWidget(self.academy_label, 4, 0, 1, 1)

        self.teacher_input = QLineEdit(self.dockWidgetContents)
        self.teacher_input.setObjectName(u"teacher_input")
        self.teacher_input.setMinimumSize(QSize(0, 30))
        self.teacher_input.setFont(font)

        self.gridLayout.addWidget(self.teacher_input, 10, 2, 1, 1)

        self.title_1 = QLabel(self.dockWidgetContents)
        self.title_1.setObjectName(u"title_1")
        font2 = QFont()
        font2.setFamily(u"Arial")
        font2.setPointSize(14)
        font2.setBold(False)
        font2.setWeight(50)
        font2.setKerning(True)
        self.title_1.setFont(font2)
        self.title_1.setMouseTracking(True)
        self.title_1.setTextFormat(Qt.AutoText)
        self.title_1.setAlignment(Qt.AlignCenter)
        self.title_1.setWordWrap(False)

        self.gridLayout.addWidget(self.title_1, 0, 0, 1, 6)

        self.grade_input = QLineEdit(self.dockWidgetContents)
        self.grade_input.setObjectName(u"grade_input")
        self.grade_input.setMinimumSize(QSize(0, 30))
        self.grade_input.setFont(font)

        self.gridLayout.addWidget(self.grade_input, 6, 1, 1, 2)

        self.banji_input = QLineEdit(self.dockWidgetContents)
        self.banji_input.setObjectName(u"banji_input")
        self.banji_input.setMinimumSize(QSize(0, 30))
        self.banji_input.setFont(font)
        self.banji_input.setFrame(True)
        self.banji_input.setDragEnabled(False)
        self.banji_input.setReadOnly(False)

        self.gridLayout.addWidget(self.banji_input, 6, 4, 1, 2)

        self.verticalSpacer_2 = QSpacerItem(20, 5, QSizePolicy.Minimum, QSizePolicy.MinimumExpanding)

        self.gridLayout.addItem(self.verticalSpacer_2, 3, 1, 1, 1)

        self.banji_label = QLabel(self.dockWidgetContents)
        self.banji_label.setObjectName(u"banji_label")
        self.banji_label.setMinimumSize(QSize(0, 30))
        self.banji_label.setFont(font1)

        self.gridLayout.addWidget(self.banji_label, 6, 3, 1, 1)

        self.grade_label = QLabel(self.dockWidgetContents)
        self.grade_label.setObjectName(u"grade_label")
        self.grade_label.setMinimumSize(QSize(0, 30))
        self.grade_label.setFont(font1)

        self.gridLayout.addWidget(self.grade_label, 6, 0, 1, 1)

        self.major_select = QComboBox(self.dockWidgetContents)
        self.major_select.setObjectName(u"major_select")
        self.major_select.setMinimumSize(QSize(0, 30))
        self.major_select.setFont(font)

        self.gridLayout.addWidget(self.major_select, 4, 4, 1, 2)

        self.zhichen_label = QLabel(self.dockWidgetContents)
        self.zhichen_label.setObjectName(u"zhichen_label")
        self.zhichen_label.setMinimumSize(QSize(0, 30))
        self.zhichen_label.setFont(font1)

        self.gridLayout.addWidget(self.zhichen_label, 10, 3, 1, 2)

        self.verticalSpacer_5 = QSpacerItem(20, 5, QSizePolicy.Minimum, QSizePolicy.MinimumExpanding)

        self.gridLayout.addItem(self.verticalSpacer_5, 9, 0, 1, 1)

        self.teacher_label = QLabel(self.dockWidgetContents)
        self.teacher_label.setObjectName(u"teacher_label")
        self.teacher_label.setMinimumSize(QSize(0, 30))
        self.teacher_label.setFont(font1)

        self.gridLayout.addWidget(self.teacher_label, 10, 0, 1, 2)

        self.verticalSpacer_3 = QSpacerItem(20, 5, QSizePolicy.Minimum, QSizePolicy.MinimumExpanding)

        self.gridLayout.addItem(self.verticalSpacer_3, 5, 1, 1, 1)

        self.warning = QLabel(self.dockWidgetContents)
        self.warning.setObjectName(u"warning")
        self.warning.setEnabled(True)
        self.warning.setStyleSheet(u"color:red")
        self.warning.setScaledContents(False)
        self.warning.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.warning, 12, 0, 1, 6)

        DockWidget.setWidget(self.dockWidgetContents)
#if QT_CONFIG(shortcut)
        self.id_label.setBuddy(self.id_input)
        self.title_label.setBuddy(self.title_input)
        self.name_label.setBuddy(self.name_input)
        self.banji_label.setBuddy(self.banji_input)
        self.grade_label.setBuddy(self.grade_input)
        self.zhichen_label.setBuddy(self.zhichen_input)
        self.teacher_label.setBuddy(self.teacher_input)
#endif // QT_CONFIG(shortcut)
        QWidget.setTabOrder(self.name_input, self.id_input)
        QWidget.setTabOrder(self.id_input, self.grade_input)
        QWidget.setTabOrder(self.grade_input, self.banji_input)
        QWidget.setTabOrder(self.banji_input, self.title_input)
        QWidget.setTabOrder(self.title_input, self.teacher_input)
        QWidget.setTabOrder(self.teacher_input, self.zhichen_input)
        QWidget.setTabOrder(self.zhichen_input, self.pushButton)

        self.retranslateUi(DockWidget)

        QMetaObject.connectSlotsByName(DockWidget)
    # setupUi

    def retranslateUi(self, DockWidget):
        DockWidget.setWindowTitle(QCoreApplication.translate("DockWidget", u"\u4fe1\u606f\u5f55\u5165", None))
        self.id_label.setText(QCoreApplication.translate("DockWidget", u"\u5b66\u53f7:", None))
        self.pushButton.setText(QCoreApplication.translate("DockWidget", u"\u5f55\u5165", None))
        self.title_label.setText(QCoreApplication.translate("DockWidget", u"\u6bd5\u4e1a\u8bbe\u8ba1\u9898\u76ee:", None))
        self.name_label.setText(QCoreApplication.translate("DockWidget", u"\u59d3\u540d:", None))
        self.major_label.setText(QCoreApplication.translate("DockWidget", u"\u4e13\u4e1a:", None))
        self.academy_label.setText(QCoreApplication.translate("DockWidget", u"\u5b66\u9662:", None))
        self.title_1.setText(QCoreApplication.translate("DockWidget", u"\u4fe1\u606f\u5f55\u5165", None))
        self.banji_input.setText("")
        self.banji_label.setText(QCoreApplication.translate("DockWidget", u"\u73ed\u7ea7:", None))
        self.grade_label.setText(QCoreApplication.translate("DockWidget", u"\u5e74\u7ea7:", None))
        self.zhichen_label.setText(QCoreApplication.translate("DockWidget", u"\u6307\u5bfc\u8001\u5e08\u804c\u79f0:", None))
        self.teacher_label.setText(QCoreApplication.translate("DockWidget", u"\u6307\u5bfc\u8001\u5e08:", None))
#if QT_CONFIG(tooltip)
        self.warning.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.warning.setText("")
    # retranslateUi

