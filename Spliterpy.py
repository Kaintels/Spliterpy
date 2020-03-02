import pandas as pd
import os
import traceback
import math
from tqdm import tqdm
import sys, Ui

import PyQt5

from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

class MainDialog(QDialog, Ui.Ui_Form):
    def __init__(self):
        QDialog.__init__(self, None)
        self.setupUi(self)
        self.open_csv_button.clicked.connect(self.open_path)
        self.split_button.clicked.connect(self.split)
        self.information_button.clicked.connect(self.infomation)

    def open_path(self):
        file_name = QFileDialog.getOpenFileName(self, 'Open file', '.csv', "csv files (*.csv)")
        self.pathBrowser.setText(str(file_name[0]))
        data = file_name[0]

    def split(self):
        try:
            data_load = self.pathBrowser.toPlainText()
            data = pd.read_csv(data_load)
            numdata = list(data['Data'].values)
            sublist = []
            slice_data = []
            for i in range(len(numdata)):
                if numdata[i] == '-':
                    slice_data.append(sublist)
                    sublist = []
                else:
                    sublist.append(numdata[i])
            slice_data = [x for x in slice_data if x]
            slice_data.append(sublist)
            for i in range(len(slice_data)):
                Total = pd.DataFrame(slice_data[i])
                Total.to_csv("datasplit" + str(i+1) + ".csv", header=False, index=False)
            msg = QMessageBox(self)
            msg.information(self, "Information", 'CSV file splited successfully.')
            msg.setText("Done")
            self.pathBrowser.clear()
        except:
            msg = QMessageBox(self)
            msg.warning(self, "Warning", 'Please open file first.')

    def infomation(self):
        msg = QMessageBox(self)
        msg.information(self, "Information", 'Spliterpy - csv data spliter based on python \n\nVersion :  0.2.0 \n\nAuthor : Kaintels (https://github.com/Kaintels)')
        msg.setText("Done")

    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Message', "Are you sure to quit?", QMessageBox.Yes, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainDialog()
    window.setWindowTitle("Spliterpy")
    window.show()
    sys.exit(app.exec_())