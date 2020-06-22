import sys
import os
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QFileDialog
import testcsv


class Sheet(QMainWindow):
    def __init__(self):
        super().__init__()
        path = QFileDialog.getOpenFileName(self, 'Open CSV',  'CSV(*.csv)')
        a = testcsv.dataFrame()
        a.r_csv(path[0])
        print(a.header())

        self.show()

app = QApplication(sys.argv)
sheet = Sheet()
sys.exit(app.exec_())
