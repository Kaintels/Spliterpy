# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_form.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(460, 122)
        self.open_csv_button = QtWidgets.QPushButton(Form)
        self.open_csv_button.setGeometry(QtCore.QRect(20, 60, 131, 41))
        self.open_csv_button.setObjectName("open_csv_button")
        self.split_button = QtWidgets.QPushButton(Form)
        self.split_button.setGeometry(QtCore.QRect(170, 60, 121, 41))
        self.split_button.setObjectName("split_button")
        self.path = QtWidgets.QLabel(Form)
        self.path.setGeometry(QtCore.QRect(20, 30, 56, 12))
        self.path.setObjectName("path")
        self.pathBrowser = QtWidgets.QTextBrowser(Form)
        self.pathBrowser.setGeometry(QtCore.QRect(70, 20, 381, 31))
        self.pathBrowser.setObjectName("pathBrowser")
        self.information_button = QtWidgets.QPushButton(Form)
        self.information_button.setGeometry(QtCore.QRect(360, 60, 91, 41))
        self.information_button.setObjectName("information_button")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.open_csv_button.setText(_translate("Form", "Open CSV"))
        self.split_button.setText(_translate("Form", "Split!"))
        self.path.setText(_translate("Form", "Path..."))
        self.information_button.setText(_translate("Form", "Info..."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

