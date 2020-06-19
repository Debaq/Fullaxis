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

## ==> FUNCIONES
from lib.ui_functions import *
from lib import basic_functions as basic

## ==> LIBRERIAS DEL GUI
from lib.uiForm import *

## ==> ESTILOS

from lib.styles.widgets import Styles as WStyles

## ==> APIS
from lib import API_conector


## ==> LIBRERIAS PLUGINS
# AUN NO HAY NADA, TAREA : BUSCAR LA FORMA DE QUE SE CARGEN

#################################################################
#                      CLASE PRINCIPAL                          #
#################################################################




class WidgetHomePage(QWidget):
    def __init__(self, *args, **kwargs):
        QWidget.__init__(self, *args, **kwargs)
        self.UI_HomePage = ui_home.Ui_HomeWidget()
        self.UI_HomePage.setupUi(self)
        
class WidgetLoginPage(QWidget):
    def __init__(self, *args, **kwargs):
        QWidget.__init__(self, *args, **kwargs)
        self.UI_LoginPage = ui_login.Ui_login()
        self.UI_LoginPage.setupUi(self)



class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = ui_main.Ui_FullAxis()
        self.ui.setupUi(self)
        self.btn_basic()
        self.home_page = WidgetHomePage()
        self.homePage()
        self.btnLoginMetod()
        self.show()        
        
    def btn_basic(self):
        self.ui.btn_ContractExplorer.clicked.connect(lambda: UIFunctions.toggleFrameOption_L5(self,20, True))
        self.ui.btn_MenuHome.clicked.connect(self.homePage)
        

        #self.ui.btn_MenuUser.clicked.connect(self.Open_user)
        self.ui.btn_MenuInfo.clicked.connect(lambda: UIFunctions.toggleFrameOption_L5(self,20, True))
        self.ui.btn_MenuPlugins.clicked.connect(lambda: UIFunctions.toggleFrameOption_L5(self,20, True))
        self.ui.btn_MenuSetting.clicked.connect(lambda: UIFunctions.toggleFrameOption_L5(self,20, True))


    def btnLoginMetod(self):
        self.btnLogin = QPushButton()
        self.btnLogin.setObjectName("btn_login")
        self.btnLogin.setText("Ingresar")
        self.btnLogin.setStyleSheet(WStyles.style_bt_text)
        self.btnLogin.clicked.connect(self.loginPage)
        self.home_page.UI_HomePage.layoutFrame_login.addWidget(self.btnLogin)
        
    def loginPage(self):
        UIFunctions.resetLayout(self,self.ui.layoutFrameCenter_L5)
        self.login_page = WidgetLoginPage()
        self.ui.layoutFrameCenter_L5.addWidget(self.login_page)
        self.login_page.UI_LoginPage.btn_requestlogin.clicked.connect(self.loginMethod)


    def homePage(self):
        UIFunctions.resetLayout(self,self.ui.layoutFrameCenter_L5)
        self.ui.layoutFrameCenter_L5.addWidget(self.home_page)
        width = self.ui.FrameOption_L5.width()
        if width == 200:
            UIFunctions.toggleFrameOption_L5(self,20, True)
    
        
            
    def loginMethod(self):            
        Name =self.login_page.UI_LoginPage.input_user.text()
        Passw = self.login_page.UI_LoginPage.input_pass.text()
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
                UIFunctions.Error(self,'CLEAR')
                UIFunctions.labelUserName(self, Name)
                pased=(1,1,1) 
            
        if pased == (1,1,1):
            app_key_id = self.data_conection[0]
            app_key = self.data_conection[1]
            bucket_name = self.data_conection[2]
            try:
                self.conection_b2 = API_conector.b2_conect(app_key_id, app_key, bucket_name)
                UIFunctions.resetLayout(self,self.ui.layoutFrameCenter_L5)
                UIFunctions.resetLayout(self,self.home_page.UI_HomePage.layoutFrame_login)

                self.ui.layoutFrameCenter_L5.addWidget(self.home_page)
                temp_log = open("temp/login.lock","w+")
                temp_log.close()
                
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
    WidgetLoginPage()

    sys.exit(app.exec_()) 
