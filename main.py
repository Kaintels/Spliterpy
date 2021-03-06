import pandas as pd
import Ui
from PySide2.QtGui import *
from PySide2.QtCore import *
from PySide2.QtWidgets import *

class MainDialog(QDialog, Ui.Ui_Form):
    def __init__(self):
        QDialog.__init__(self, None)
        self.setupUi(self)
        self.open_csv_button.clicked.connect(self.open_path)
        self.split_button.clicked.connect(self.split)
        self.information_button.clicked.connect(self.infomation)

    def open_path(self):
        file_name = QFileDialog.getOpenFileName(self, 'Open file', '.csv', "csv files (*.csv)")
        self.open_pathBrowser.setText(str(file_name[0]))

    def split(self):
        try:
            data_load = self.open_pathBrowser.toPlainText()
            want_data_name = self.textEdit.toPlainText()
            data = pd.read_csv(data_load, header=None, dtype='object')
            data = data.fillna("-")
            sublist = []
            slice_data = []
            for i in range(len(data.index)):
                if (data.loc[i] == '-').any():
                    slice_data.append(sublist)
                    sublist = []
                else:
                    sublist.append(data.loc[i])
            slice_data = [x for x in slice_data if x]
            slice_data.append(sublist)
            for i in range(len(slice_data)):
                total = pd.DataFrame(slice_data[i])
                total.to_csv(want_data_name+"_"+ str(i+1) + ".csv", header=False, index=False, encoding='utf-8-sig')
            msg = QMessageBox(self)
            msg.information(self, "Information", 'CSV file splited successfully.')
            self.open_pathBrowser.clear()
        except:
            msg = QMessageBox(self)
            msg.warning(self, "Warning", 'Please open file first.')

    def infomation(self):
        msg = QMessageBox(self)
        msg.information(self, "Information", 'Spliterpy - csv data spliter based on python \n\nVersion :  0.2.6 \n\nAuthor : S.Han (https://github.com/Kaintels)')
        msg.setText("Done")

    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Message', "Are you sure to quit?", QMessageBox.Yes, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

if __name__ == "__main__":
    import sys
    sys.setrecursionlimit(10000)
    app = QApplication(sys.argv)
    window = MainDialog()
    window.setWindowTitle("Spliterpy")
    window.show()
    sys.exit(app.exec_())