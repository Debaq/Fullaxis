################################################################################
##
## CREADOR: NICOLÁS QUEZADA QUEZADA
## AGRADECIMEINTOS A: WANDERSON M.PIMENTA
## NOMBRE DEL PROYECTO: FULLAXIS
## V: 1.0.0-GUI
##
################################################################################

import sys
import platform
import os


from PySide2 import QtCore, QtGui, QtWidgets, QtUiTools
from PySide2.QtWidgets import QApplication
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *

# GUI FILE
from ui_form import Ui_FullAxis
from ui_home import Ui_HomeWidget

# IMPORT FUNCTIONS
from ui_functions import * 

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_FullAxis()
        self.ui.setupUi(self)
        self.show()

    ########################################################################
        ## START - WINDOW ATTRIBUTES
    ########################################################################
    ## ==> TOGGLE EXPLORER

        self.ui.btn_ContractExplorer.clicked.connect(lambda: UIFunctions.toggleFrameOption_L5(self,20, True))
        self.widget = Ui_HomeWidget()
        self.widget.setupUi(self.ui.FrameCenter_L5)
        #self.ui.layoutFrameCenter_L5.addWidget(widget)



    ########################################################################
    ## START ==> APP EVENTS
    ########################################################################

    ## EVENT ==> MOUSE DOUBLE CLICK
    ########################################################################
    def eventFilter(self, watched, event):
        if watched == self.le and event.type() == QtCore.QEvent.MouseButtonDblClick:
            print("pos: ", event.pos())
    ## ==> END ##

    ## EVENT ==> MOUSE CLICK
    ########################################################################
    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()
        if event.buttons() == Qt.LeftButton:
            print('Mouse click: LEFT CLICK')
        if event.buttons() == Qt.RightButton:
            print('Mouse click: RIGHT CLICK')
        if event.buttons() == Qt.MidButton:
            print('Mouse click: MIDDLE BUTTON')
    ## ==> END ##

    ## EVENT ==> KEY PRESSED
    ########################################################################
    def keyPressEvent(self, event):
        print('Key: ' + str(event.key()) + ' | Text Press: ' + str(event.text()))
    ## ==> END ##

    ## EVENT ==> RESIZE EVENT
    ########################################################################
    def resizeEvent(self, event):
        self.resizeFunction()
        return super(MainWindow, self).resizeEvent(event)

    def resizeFunction(self):
        print('Height: ' + str(self.height()) + ' | Width: ' + str(self.width()))
    ## ==> END ##

    ########################################################################
    ## END ==> APP EVENTS
    ############################## ---/--/--- ##############################

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())   