# -*- coding: utf-8 -*-
#################################################################
#                                                               #
#                  NOMBRE PROYECTO : preview-FULLAXIS           #
#                   VER. 20.7.4 - GUI PYQT5                     #
#                    NOMBRE VER. : AzoGuer                      #
#               CREADOR : NICOLÁS QUEZADA QUEZADA               #
#                                                               #
#################################################################

# ==> LIBRERIAS BÁSICAS
import os
import sys
from os import path, remove
import platform
sistema = platform.system()
#print("Estamos en {}".format(sistema))


# ==> SE ACTUALIZAN UI Y RC SI SE ENCUENTRA EN MODO DESARROLLO

try:
    parameter = sys.argv[1]
    MODE_DEVELOPMENT = True
    print("MODE_DEVELOPMENT = ", MODE_DEVELOPMENT)


except:
    MODE_DEVELOPMENT = False


if MODE_DEVELOPMENT:
    from lib.helpers import updateUI
    if parameter == '--update-all':
        updateUI.updateUI(0)
    elif parameter == '--update-uic':
        updateUI.updateUI(1)
        sys.exit()
    elif parameter == '--update-uic-run':
        updateUI.updateUI(1)
    elif parameter == '--update-rc':
        updateUI.updateUI(2)
        sys.exit()

    else:
        print("""
        Error : Opción desconocida.
        
        Use:   python Fullaxis.py
               python Fullaxis.py <opción>
        
        Opciones:
        --update-all        :   actualiza los archivos .ui y .rc
        --update-uic        :   actualiza los archivos .ui en devolpment/Form
        --update-rc         :   actualiza los archivos .rc en devolpment/resource
        --update-uic-run    :   actualiza los archivos .ui en devolpment/Form y corre el programa
        """)

        sys.exit()
else:
    pass



import pyqtgraph as pg
import numpy as np
# ==> LIBRERIAS PYQT
from PyQt5 import QtCore
from PyQt5.QtGui import QIcon, QTableWidgetItem, QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import (QApplication, QDialog, QLabel, QMainWindow, QMenu,
                             QStyleFactory, QTableView, QVBoxLayout, QWidget, 
                             QVBoxLayout, QHBoxLayout, QFileDialog)

import lib.PATH_NAME as PATH
import lib.old_exchange as old_csv
# ==> APIS
from lib import basic_functions as basic
from lib.helpers import updateUI
from lib import old_exchange
# ==> ESTILOS
# ==> FUNCIONES
from lib.ui_functions import UIFunctions as UIFunc
# ==> LIBRERIAS DEL GUI
#from lib.uiForm.transform_ui import Ui_Form
from lib.uiForm.preview_ui import Ui_preview



#################################################################
#                      CLASE PRINCIPAL                          #
#################################################################

FOLDER = ""
FILE = []

class MainWindow(QWidget):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_preview()
        self.ui.setupUi(self)
        self.setWindowIcon(QIcon(PATH.LOGO))
        self.show()
        self.ui.pushButton.clicked.connect(self.openMethodFolder)


    def listMethod(self):
        self.model = QStandardItemModel()
        self.ui.listView.setModel(self.model)
        ls = FILE

        for i in ls:
            item = QStandardItem(i)
            self.model.appendRow(item)


    @QtCore.pyqtSlot(QtCore.QModelIndex)
    def on_listView_clicked(self, index):
        row_number = self.model.itemFromIndex(index)
        self.openMethodFile(row_number.data(QtCore.Qt.DisplayRole))


    def openMethodFolder(self):
        global FOLDER
        global FILE
        try:
            self.model.modelReset()
        except:
            pass
        FILE = []
        FOLDER = ""
        path = QFileDialog.getExistingDirectory(self, 'Select directory')
        FOLDER = path
        self.readFolder()

    def openMethodFile(self, nameFile):
        File = FOLDER+"/"+nameFile
        self.readData(File)

            
    def readFolder(self):
        global FILE
        folderOS = os.listdir(FOLDER)
        for files in folderOS:
            if os.path.isfile(os.path.join(FOLDER, files)) and files.endswith('.csv'):
                #print(files)
                FILE.append(files)
            if os.path.isfile(os.path.join(FOLDER, files)) and files.endswith('.json'):
                FILE.append(files)

        FILE = sorted(FILE)
        self.listMethod()          

    def readData(self, files):
        data_raw = old_exchange.dataFrame() 
        if files.endswith('.csv'):
            data_raw.read(files, "csv")
            self.data1 = data_raw.onlyColumn("A")
            self.data2 = data_raw.onlyColumn("B")
            self.data3 = data_raw.onlyColumn("C")
            self.timeMilli = data_raw.onlyColumn("D")

        if files.endswith('.json'):
            data_raw.read(files, "json")
            self.data1 = data_raw.onlyColumn("roll")
            self.data2 = data_raw.onlyColumn("pitch")
            self.data3 = data_raw.onlyColumn("yaw")
            self.timeMilli = data_raw.onlyColumn("time")

        self.data1=self.normalize(self.data1)
        self.data2=self.normalize(self.data2)
        self.data3=self.normalize(self.data3)
        self.timeMethod()
        self.graph()

    def timeMethod(self):
        self.time = []
        calibrateTime = self.timeMilli[0]
        for x in self.timeMilli:
            self.time.append((x-calibrateTime)/1000)

    def normalize(self, data):
        prom = np.mean([max(data),min(data)])
        out = []
        for x in data:
            inY = x
            if prom < 0:
                inY = inY+prom
            else:
                inY = inY-prom
            out.append(inY)
        return out

    def graph(self):
        UIFunc.resetLayout(self, self.ui.Layout_graph)
                  
        pw1 = pg.PlotWidget(name='Plot1') 
        pw2 = pg.PlotWidget(name='Plot2')
        pw3 = pg.PlotWidget(name='Plot3')  

        self.ui.Layout_graph.addWidget(pw1)
        self.ui.Layout_graph.addWidget(pw2)
        self.ui.Layout_graph.addWidget(pw3)

        p1 = pw1.plot(self.time, self.data1, pen="c")
        p2 = pw2.plot(self.time, self.data2, pen="g")
        p3 = pw3.plot(self.time, self.data3, pen="r")


if __name__ == "__main__":
  

    app = QApplication([])
    app.setStyle('Windows')
    window = MainWindow()
    sys.exit(app.exec_())
