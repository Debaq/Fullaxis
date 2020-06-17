# -*- coding: utf-8 -*-
#################################################################
#                                                               #
#                  NOMBRE PROYECTO : FULLAXIS                   #
#                       VER. 20.6 - GUI                         #
#               CREADOR : NICOLÁS QUEZADA QUEZADA               #
#                                                               #
#################################################################

import os
import platform
## ==> LIBRERIAS BÁSICAS
import sys

## ==> LIBRERIAS PYSIDE2
from PySide2 import QtCore, QtGui, QtUiTools, QtWidgets
from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QEvent,
                            QMetaObject, QObject, QPoint, QPropertyAnimation,
                            QRect, QSize, Qt, QTime, QUrl)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
                           QFontDatabase, QIcon, QKeySequence, QLinearGradient,
                           QPainter, QPalette, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *
from PySide2.QtWidgets import QApplication

from lib.ui_functions import *
from lib.uiForm import *

## ==> LIBRERIAS PLUGINS
# AUN NO HAY NADA, TAREA : BUSCAR LA FORMA DE QUE SE CARGEN

#################################################################
#                      CLASE PRINCIPAL                          #
#################################################################

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = ui_main.Ui_FullAxis()
        self.ui.setupUi(self)
        self.show()
        self.btn_basic()
        
    def btn_basic(self):
        self.ui.btn_ContractExplorer.clicked.connect(lambda: UIFunctions.toggleFrameOption_L5(self,20, True))
        self.ui.btn_MenuHome.clicked.connect(UIFunctions.Open_home)
        self.ui.btn_MenuUser.clicked.connect(lambda: UIFunctions.toggleFrameOption_L5(self,20, True))
        self.ui.btn_MenuInfo.clicked.connect(lambda: UIFunctions.toggleFrameOption_L5(self,20, True))
        self.ui.btn_MenuPlugins.clicked.connect(lambda: UIFunctions.toggleFrameOption_L5(self,20, True))
        self.ui.btn_MenuSetting.clicked.connect(lambda: UIFunctions.toggleFrameOption_L5(self,20, True))



        






#################################################################
#                      SE INICA EL PROGRAMA                     #
#################################################################
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_()) 
