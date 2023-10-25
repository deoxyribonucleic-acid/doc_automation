# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ReadExceleFESTL.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import QRect, QMetaObject, QCoreApplication
from PyQt5.QtWidgets import QSizePolicy, QWidget, QVBoxLayout, QLabel, QHBoxLayout, \
        QSpacerItem, QPushButton, QLineEdit, QGridLayout, QSizePolicy, QMenuBar, QStatusBar, QTableWidget


class Ui_ExcelReader(object):
    def setupUi(self, ExcelReader):
        if not ExcelReader.objectName():
            ExcelReader.setObjectName(u"ExcelReader")
        ExcelReader.resize(640, 480)
        self.centralwidget = QWidget(ExcelReader)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.file_path_label = QLabel(self.centralwidget)
        self.file_path_label.setObjectName(u"file_path_label")

        self.horizontalLayout.addWidget(self.file_path_label)

        self.file_path_line_edit = QLineEdit(self.centralwidget)
        self.file_path_line_edit.setObjectName(u"file_path_line_edit")
        self.file_path_line_edit.setReadOnly(True)

        self.horizontalLayout.addWidget(self.file_path_line_edit)

        self.browse_btn = QPushButton(self.centralwidget)
        self.browse_btn.setObjectName(u"browse_btn")

        self.horizontalLayout.addWidget(self.browse_btn)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.read_btn = QPushButton(self.centralwidget)
        self.read_btn.setObjectName(u"read_btn")

        self.horizontalLayout_2.addWidget(self.read_btn)

        self.clr_btn = QPushButton(self.centralwidget)
        self.clr_btn.setObjectName(u"clr_btn")

        self.horizontalLayout_2.addWidget(self.clr_btn)

        self.confirm_btn = QPushButton(self.centralwidget)
        self.confirm_btn.setObjectName(u"confirm_btn")

        self.horizontalLayout_2.addWidget(self.confirm_btn)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.table_widget = QTableWidget(self.centralwidget)
        self.table_widget.setObjectName(u"table_widget")

        self.verticalLayout.addWidget(self.table_widget)


        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        ExcelReader.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(ExcelReader)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 640, 24))
        ExcelReader.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(ExcelReader)
        self.statusbar.setObjectName(u"statusbar")
        ExcelReader.setStatusBar(self.statusbar)

        self.retranslateUi(ExcelReader)

        QMetaObject.connectSlotsByName(ExcelReader)
    # setupUi

    def retranslateUi(self, ExcelReader):
        ExcelReader.setWindowTitle(QCoreApplication.translate("ExcelReader", u"Excel Reader", None))
        self.file_path_label.setText(QCoreApplication.translate("ExcelReader", u"Excel File Path:", None))
        self.browse_btn.setText(QCoreApplication.translate("ExcelReader", u"Browse", None))
        self.read_btn.setText(QCoreApplication.translate("ExcelReader", u"Read", None))
        self.clr_btn.setText(QCoreApplication.translate("ExcelReader", u"Clear", None))
        self.confirm_btn.setText(QCoreApplication.translate("ExcelReader", u"Confirm", None))
    # retranslateUi

