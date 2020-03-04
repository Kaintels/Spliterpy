# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_form.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *


class Ui_Form(object):
    def setupUi(self, Form):
        if Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(457, 122)
        self.open_csv_button = QPushButton(Form)
        self.open_csv_button.setObjectName(u"open_csv_button")
        self.open_csv_button.setGeometry(QRect(20, 60, 131, 41))
        self.split_button = QPushButton(Form)
        self.split_button.setObjectName(u"split_button")
        self.split_button.setGeometry(QRect(190, 60, 121, 41))
        self.openpath = QLabel(Form)
        self.openpath.setObjectName(u"openpath")
        self.openpath.setGeometry(QRect(20, 30, 56, 12))
        self.open_pathBrowser = QTextBrowser(Form)
        self.open_pathBrowser.setObjectName(u"open_pathBrowser")
        self.open_pathBrowser.setGeometry(QRect(70, 20, 191, 31))
        self.information_button = QPushButton(Form)
        self.information_button.setObjectName(u"information_button")
        self.information_button.setGeometry(QRect(340, 60, 91, 41))
        self.savename = QLabel(Form)
        self.savename.setObjectName(u"savename")
        self.savename.setGeometry(QRect(270, 30, 56, 12))
        self.textEdit = QTextEdit(Form)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(330, 20, 104, 31))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.open_csv_button.setText(QCoreApplication.translate("Form", u"Open CSV", None))
        self.split_button.setText(QCoreApplication.translate("Form", u"Split !", None))
        self.openpath.setText(QCoreApplication.translate("Form", u"Path...", None))
        self.information_button.setText(QCoreApplication.translate("Form", u"Info...", None))
        self.savename.setText(QCoreApplication.translate("Form", u"Name", None))
    # retranslateUi

