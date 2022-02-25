# -*- coding: utf-8 -*-

#################################################################
#                                                               #
#                  NOMBRE PROYECTO : FULLAXIS                   #
#                   VER. 22.2.25 - GUI PySide6                     #
#                    NOMBRE VER. : AzoGuer                      #
#               CREADOR : NICOLÁS QUEZADA QUEZADA               #
#                                                               #
#################################################################

# ==> LIBRERIAS BÁSICAS
import os
import sys
from os import path
from fbs_runtime.application_context.PyQt6 import ApplicationContext


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



import numpy as np
# ==> LIBRERIAS PYQT
from PySide6 import QtCore
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import (QApplication, QDialog, QMainWindow, QMenu,
                               QWidget)

import lib.PATH_NAME as PATH
# ==> APIS
from lib import API_conector
#from lib import basic_functions as basic
#from lib.helpers import updateUI
from lib.styles.Frames import Styles as FStyles
# ==> ESTILOS
#from lib.styles.widgets import Styles as WStyles
# ==> FUNCIONES
#from lib.ui_functions import TableModel
from lib.ui_functions import UIFunctions as UIFunc
from lib.uiForm.home_ui import Ui_HomeWidget
from lib.uiForm.login_ui import Ui_login
# ==> LIBRERIAS DEL GUI
from lib.uiForm.main_ui import Ui_FullAxis
from lib.uiForm.menu_lateral_ui import Ui_Lateral_menu
#from lib.uiForm.transform_ui import Ui_Form
from plugins.faxyGraph.faxyGraph import WidgetGraph
from plugins.faxyCompare.faxyCompare import WidgetCompare



# ==> LIBRERIAS PLUGINS
# AUN NO HAY NADA, TAREA : BUSCAR LA FORMA DE QUE SE CARGEN


#################################################################
#                      CLASES WIDGETS                           #
#################################################################



class WidgetHomePage(QWidget):
    def __init__(self, *args, **kwargs):
        QWidget.__init__(self, *args, **kwargs)
        self.UI_HomePage = Ui_HomeWidget()
        self.UI_HomePage.setupUi(self)


class WidgetLateralMenu(QWidget):
    def __init__(self, *args, **kwargs):
        QWidget.__init__(self, *args, **kwargs)
        self.UI_LateralMenu = Ui_Lateral_menu()
        self.UI_LateralMenu.setupUi(self)
        self.UI_LateralMenu.back_frame.setStyleSheet(FStyles.Frame_lateral)


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
            datos = UIFunc.loginLockRead(self)
            window.verifyLogin(datos['name'])


class WidgetFourier(QWidget):
    pass
#################################################################
#                      CLASE PRINCIPAL                          #
#################################################################

File = None

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_FullAxis()
        self.ui.setupUi(self)
        self.btn_basic()
        self.setWindowIcon(QIcon(PATH.LOGO))
        self.home_page = WidgetHomePage()
        self.homePage()
        self.verifyLogin(None)
        self.styleMethod()
        self.ui.menubar.hide()
        self.show()

    def styleMethod(self):
        self.ui.Frame_info.setStyleSheet(FStyles.Frame_info)
        self.ui.Frame_center.setStyleSheet(FStyles.Frame_center)

    def btn_basic(self):
        self.ui.btn_login.clicked.connect(self.btnloginMethod)

    def verifyLogin(self, Name):
        if path.exists(PATH.LOGINLOCK):
            UIFunc.resetLayout(self, self.ui.Login_Layout)
            user = QMenu()
            user.addAction("Salir", self.logout)
            btn_logout = UIFunc.ButtonText(self, Name)
            btn_logout.setMenu(user)
            #self.ui.Login_Layout.addWidget(btn_logout)
            self.lateralMenu()
            self.homePage()

        else:
            UIFunc.resetLayout(self, self.ui.Login_Layout)
            user = QMenu()
            user.addAction("Cuenta Online", self.btnloginMethod)
            btn_logout = UIFunc.ButtonFlat(self, "Ingresar a la cuenta")
            btn_logout.setMenu(user)
            #self.ui.Login_Layout.addWidget(btn_logout)
            self.lateralMenu()

    def openMethod(self):
        global File
        path = UIFunc.openFile(self)
        File = path[0]
        self.graphPage()
        
    def logout(self):
        UIFunc.logout(self)
        UIFunc.resetLayout(self, self.ui.Login_Layout)
        self.verifyLogin(None)

    def btnloginMethod(self):
        self.login = WidgetLoginPage(self)
        self.login.move(0, 0)
        self.login.UI_LoginPage.btn_cancel.clicked.connect(self.login.close)
        self.login.UI_LoginPage.btn_requestlogin.setDefault(True)
        Name = self.login.UI_LoginPage.input_user
        Passw = self.login.UI_LoginPage.input_pass
        self.login.UI_LoginPage.btn_requestlogin.clicked.connect(
            lambda: self.loginMethod(Name.text(), Passw.text()))
        self.login.show()

    def homePage(self):
        self.ui.Center_layout.addWidget(self.home_page)

    def graphPage(self):
        UIFunc.resetLayout(self, self.ui.Center_layout)
        self.graph_page = WidgetGraph(filedoc=File)
        self.graph_page.UI_vertical.btn_open.clicked.connect(self.openMethod)
        try:
            self.graph_page.UI_vertical.label_File.setText(File)
        except:
            self.graph_page.UI_vertical.label_File.setText("...")

        self.ui.Center_layout.addWidget(self.graph_page)


    def comparePage(self):
        UIFunc.resetLayout(self, self.ui.Center_layout)
        self.compare_page = WidgetCompare()
        self.ui.Center_layout.addWidget(self.compare_page)


    def lateralMenu(self):
        # => CARGA WIDGET
        self.LateralMenu = WidgetLateralMenu()
        # =>SE CREAN LOS BOTONES
        btn_home = UIFunc.createBtnMenuLat(
            self, "btn_home", "", "home", "Inicio")
        btn_graph = UIFunc.createBtnMenuLat(
            self, "btn_graph", "", "chart-line", "Medir")
        btn_graph = UIFunc.createBtnMenuLat(
            self, "btn_compare", "", "clone", "Comparar")
        # =>ESPACIADOR QUE MANTIENE LOS BOTONES ARRIBA
        spacer = UIFunc.spacer(self, "V")
        self.LateralMenu.UI_LateralMenu.layerBack_frame.addItem(spacer)
        # =>SE AGREGA EL MENULATERAL A LA VENTANA
        self.ui.Lateral_layout.addWidget(self.LateralMenu)

    def loginMethod(self, Name, Passw):
        if Name != '' and Passw != '':
            pased = (1, 1, 0)
        else:
            pased = (0, 0, 0)
            UIFunc.Error(self, 'E:061')

        if pased == (1, 1, 0):
            try:
                from lib import API_conector as API
                self.data_conection = API_conector.request_key(Name, Passw)
                if self.data_conection[0] == 'E:062':
                    UIFunc.Error(self, 'E:062')

                else:
                    UIFunc.Error(self, 'CLEAR')
                    pased = (1, 1, 1)
            except:
                UIFunc.Error(self, 'A:005')
        if pased == (1, 1, 1):
            app_key_id = self.data_conection[0]
            app_key = self.data_conection[1]
            bucket_name = self.data_conection[2]
            try:
                self.conection_b2 = API_conector.b2_conect(
                    app_key_id, app_key, bucket_name)
                UIFunc.resetLayout(self, self.ui.Center_layout)
                UIFunc.loginLockNew(self, Name, Passw)
                self.login.close()

            except:
                UIFunc.Error(self, 'E:063')

    def Button(self):
        btnWidget = self.sender()

        if btnWidget.objectName() == "btn_home":
            UIFunc.resetLayout(self, self.ui.Center_layout)
            self.homePage()
            UIFunc.resetStyle(self, "btn_home")
            btnWidget.setStyleSheet(UIFunc.selectMenu(btnWidget.styleSheet()))

        if btnWidget.objectName() == "btn_graph":
            self.graphPage()
            UIFunc.resetStyle(self, "btn_graph")
            btnWidget.setStyleSheet(UIFunc.selectMenu(btnWidget.styleSheet()))

        if btnWidget.objectName() == "btn_compare":
            self.comparePage()
            UIFunc.resetStyle(self, "btn_compare")
            btnWidget.setStyleSheet(UIFunc.selectMenu(btnWidget.styleSheet()))

    def closeEvent(self, event):
        if os.path.isfile(PATH.LOGINLOCK):
            UIFunc.logout(self)


#################################################################
#                      SE INICIA EL PROGRAMA                     #
#################################################################
if __name__ == "__main__":
    #sttg_workspace = basic.read_setting('workspace.json')
    #path_workspace = sttg_workspace['Path']
    #bol_oline = sttg_workspace['workspace_online']

#    app = QApplication(sys.argv)
    #app = QApplication([])
    #app.setStyle('Windows')
    # print(QStyleFactory.keys())
    context = ApplicationContext()

    window = MainWindow()
    #sys.exit(app.exec())
    exit_code = context.app.exec()
    sys.exit(exit_code)
