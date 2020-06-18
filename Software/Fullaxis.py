# -*- coding: utf-8 -*-
#################################################################
#                                                               #
#                  NOMBRE PROYECTO : FULLAXIS                   #
#                       VER. 20.6 - GUI                         #
#               CREADOR : NICOLÁS QUEZADA QUEZADA               #
#                                                               #
#################################################################

## ==> LIBRERIAS BÁSICAS
import os
import platform
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
from lib import basic_functions as basic
from lib.uiForm.ui_login import Ui_login

from lib import API_conector


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
        self.ui.btn_MenuHome.clicked.connect(self.Open_user)
        self.ui.btn_MenuUser.clicked.connect(self.Open_user)
        self.ui.btn_MenuInfo.clicked.connect(lambda: UIFunctions.toggleFrameOption_L5(self,20, True))
        self.ui.btn_MenuPlugins.clicked.connect(lambda: UIFunctions.toggleFrameOption_L5(self,20, True))
        self.ui.btn_MenuSetting.clicked.connect(lambda: UIFunctions.toggleFrameOption_L5(self,20, True))




    def Open_user(self):
        width = self.ui.FrameOption_L5.width()
        if width == 200:
            UIFunctions.toggleFrameOption_L5(self,20, True)
       
        if self.ui.page_home.layout() == None:
            self.widgetlogin = Ui_login()
            self.widgetlogin.setupUi(self.ui.page_home)
            self.widgetlogin.btn_login.clicked.connect(self.loginMethod)
        else:
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_home)
        
    
    
    def loginMethod(self):
            
        Name =self.widgetlogin.input_user.text()
        Passw = self.widgetlogin.input_pass.text()
        if Name !='' and Passw != '':
            pased = (1,1,0)
        else:
            pased = (0,0,0)
            UIFunctions.Error(self, 'E:061')

        if pased == (1,1,0):
            from lib import API_conector as API
            self.data_conection = API_conector.request_key(Name, Passw)
            if self.data_conection[0] == 'E:062':
                UIFunctions.Error(self,'E:062')
                
            else:
                UIFunctions.Error(self,'')
                UIFunctions.labelUserName(self, Name)
                pased=(1,1,1) 
               
        if pased == (1,1,1):
            app_key_id = self.data_conection[0]
            app_key = self.data_conection[1]
            bucket_name = self.data_conection[2]
            try:
                self.conection_b2 = API_conector.b2_conect(app_key_id, app_key, bucket_name)
            except:
                UIFunctions.Error(self, 'E:063')
        






#################################################################
#                      SE INICIA EL PROGRAMA                     #
#################################################################
if __name__ == "__main__":
    sttg_workspace = basic.read_setting('workspace.json')
    path_workspace = sttg_workspace['Path']
    bol_oline = sttg_workspace['workspace_online']
 
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_()) 
