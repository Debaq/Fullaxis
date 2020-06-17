#################################################################
#                                                               #
#                  NOMBRE PROYECTO : FULLAXIS                   #
#                       VER. 20.6 - GUI                         #
#               CREADOR : NICOLÁS QUEZADA QUEZADA               #
#                                                               #
#################################################################

## ==> LIBRERIAS BÁSICAS
import sys
import platform
import os

## ==> LIBRERIAS PYSIDE2
from PySide2 import QtCore, QtGui, QtWidgets, QtUiTools
from PySide2.QtWidgets import QApplication
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *

## ==> LIBRERIAS PROPIAS
# BACKEND
from lib import ui_functions

# FRONTEND
from lib.uiForm.ui_main import Ui_FullAxis

## ==> LIBRERIAS PLUGINS
# AUN NO HAY NADA, TAREA : BUSCAR LA FORMA DE QUE SE CARGEN

#################################################################
#                      CLASE PRINCIPAL                          #
#################################################################

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_FullAxis()
        self.ui.setupUi(self)
        self.show()
        
    def btn_basic(self):
        
        






#################################################################
#                      SE INICA EL PROGRAMA                     #
#################################################################
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_()) 