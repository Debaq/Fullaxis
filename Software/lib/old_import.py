import sys
import os
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QFileDialog
import old_exchange



class Sheet(QMainWindow):
    def __init__(self):
        super().__init__()
        a = old_exchange.dataFrame() 
        path = QFileDialog.getOpenFileName(None, 'Abrir Archivo de Datos', os.getenv("HOME") ,("CSV(*.csv);;JSON(*.json)"))
        print(path[0])
        if path[1] == "JSON(*.json)":
            a.read(path[0], "json")
            print(a.header())
        if path[1] == "CSV(*.csv)":
            a.read(path[0], "csv")
            print(a.header())
        
        
        
        self.show()


app = QApplication(sys.argv)
sheet = Sheet()
sys.exit(app.exec_())

