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
from os import path
from os import remove
from lib import basic_functions as basic
from lib.helpers import updateUI


## ==> SE ACTUALIZAN UI Y RC SI SE ENCUENTRA EN MODO DESARROLLO

try:
    parameter = sys.argv[1]
    MODE_DEVELOPMENT = True
    print("MODE_DEVELOPMENT = ",MODE_DEVELOPMENT)


except:
    MODE_DEVELOPMENT = False


if MODE_DEVELOPMENT:
    from lib.helpers import updateUI
    if parameter == '--update-all':
        updateUI.updateUI(0)
    elif parameter == '--update-uic':
        updateUI.updateUI(1)
    elif parameter == '--update-rc':
        updateUI.updateUI(2)
    else:
        print("""
        Error : Opción desconocida.
        
        Use:   python Fullaxis.py
               python Fullaxis.py <opción>
        
        Opciones:
        --update-all   :   actualiza los archivos .ui y .rc
        --update-uic   :   actualiza los archivos .ui en devolpment/Form
        --update-rc    :   actualiza los archivos .rc en devolpment/resource
        """)
            
        sys.exit()
else:
    pass


import lib.PATH_NAME as PATH

## ==> LIBRERIAS PYQT
from PyQt5 import QtCore
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QWidget, QDialog, QLabel, QPushButton, QMenu
from PyQt5.QtWidgets import QApplication

## ==> FUNCIONES
from lib.ui_functions import UIFunctions

## ==> LIBRERIAS DEL GUI
from lib.uiForm.main_ui import Ui_FullAxis
from lib.uiForm.home_ui import Ui_HomeWidget
from lib.uiForm.login_ui import Ui_login


## ==> ESTILOS
from lib.styles.widgets import Styles as WStyles
from lib.styles.Frames import Styles as FStyles

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
        self.UI_HomePage = Ui_HomeWidget()
        self.UI_HomePage.setupUi(self)
        
class WidgetLoginPage(QDialog):
    def __init__(self, *args, **kwargs):
        super(WidgetLoginPage, self).__init__(*args, **kwargs)
        self.UI_LoginPage = Ui_login()
        self.UI_LoginPage.setupUi(self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.setStyleSheet(FStyles.Modal_login)
        self.UI_LoginPage.back_frame.setStyleSheet(FStyles.back_layout)
        self.UI_LoginPage.center_login.setStyleSheet(FStyles.Modal_login)
    
    def closeEvent(self, event):
        if os.path.isfile(PATH.LOGINLOCK):
            datos = UIFunctions.loginLockRead()
            window.verifyLogin(datos['name'])



class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_FullAxis()
        self.ui.setupUi(self)
        self.btn_basic()
        self.home_page = WidgetHomePage()
        self.homePage()
        self.verifyLogin(None)
        self.styleMethod()
        self.show()        
            
    
    def styleMethod(self):
        self.ui.Frame_info.setStyleSheet(FStyles.Frame_info)
        self.ui.Frame_center.setStyleSheet(FStyles.Frame_center)

    
    def btn_basic(self):
        self.ui.btn_login.clicked.connect(self.btnloginMethod)
    
    def verifyLogin(self, Name):
        if path.exists(PATH.LOGINLOCK):
            UIFunctions.resetLayout(self, self.ui.Login_Layout)
            user = QMenu()
            user.addAction("Salir", self.logout)
            btn_logout= UIFunctions.ButtonText(self, Name)
            btn_logout.setMenu(user)
            self.ui.Login_Layout.addWidget(btn_logout)
        else:
            UIFunctions.resetLayout(self, self.ui.Login_Layout)
            user = QMenu()
            user.addAction("Cuentas Online", self.btnloginMethod)
            btn_logout= UIFunctions.ButtonText(self, "Ingresar")
            btn_logout.setMenu(user)
            self.ui.Login_Layout.addWidget(btn_logout)

    def logout(self):
        UIFunctions.logout(self)
        UIFunctions.resetLayout(self, self.ui.Login_Layout)
        self.verifyLogin(None)
            
    def btnloginMethod(self):
        self.login = WidgetLoginPage(self)
        self.login.move(0,0)
        self.login.UI_LoginPage.btn_cancel.clicked.connect(self.login.close)
        self.login.UI_LoginPage.btn_requestlogin.setDefault(True)
        Name = self.login.UI_LoginPage.input_user
        Passw = self.login.UI_LoginPage.input_pass
        self.login.UI_LoginPage.btn_requestlogin.clicked.connect(lambda: self.loginMethod(Name.text(), Passw.text()))
        self.login.show()
       
        

    def homePage(self):
        self.ui.Center_Layout.addWidget(self.home_page)

            
            
    def loginMethod(self, Name, Passw):            
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
                pased=(1,1,1) 
            
        if pased == (1,1,1):
            app_key_id = self.data_conection[0]
            app_key = self.data_conection[1]
            bucket_name = self.data_conection[2]
            try:
                self.conection_b2 = API_conector.b2_conect(app_key_id, app_key, bucket_name)
                UIFunctions.resetLayout(self,self.ui.Center_Layout)
                UIFunctions.loginLockNew(self, Name, Passw)
                self.login.close()
                
            except:
                UIFunctions.Error(self, 'E:063')

    def closeEvent(self, event):
        if os.path.isfile(PATH.LOGINLOCK):
            UIFunctions.logout(self)
        

#################################################################
#                      SE INICIA EL PROGRAMA                     #
#################################################################
if __name__ == "__main__":
    sttg_workspace = basic.read_setting('workspace.json')
    path_workspace = sttg_workspace['Path']
    bol_oline = sttg_workspace['workspace_online']
 
    app = QApplication(sys.argv)
    window = MainWindow()
#    WidgetLoginPage()

    sys.exit(app.exec_()) 
