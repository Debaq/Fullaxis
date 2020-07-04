# -*- coding: utf-8 -*-
#################################################################
#                                                               #
#                  NOMBRE PROYECTO : FULLAXIS                   #
#                   VER. 20.7.3 - GUI PYQT5                     #
#                    NOMBRE VER. : AzoGuer                      #
#               CREADOR : NICOLÁS QUEZADA QUEZADA               #
#                                                               #
#################################################################

# ==> LIBRERIAS BÁSICAS
import os
import platform
import sys
from os import path, remove


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
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import (QApplication, QDialog, QLabel, QMainWindow, QMenu,
                             QStyleFactory, QTableView, QVBoxLayout, QWidget, 
                             QVBoxLayout, QHBoxLayout)

import lib.old_exchange as old_csv
import lib.PATH_NAME as PATH
# ==> APIS
from lib import API_conector
from lib import basic_functions as basic
from lib.helpers import updateUI
from lib.styles.Frames import Styles as FStyles
from lib import old_exchange
# ==> ESTILOS
from lib.styles.widgets import Styles as WStyles
# ==> FUNCIONES
from lib.ui_functions import TableModel
from lib.ui_functions import UIFunctions as UIFunc
from lib.uiForm.home_ui import Ui_HomeWidget
from lib.uiForm.login_ui import Ui_login
# ==> LIBRERIAS DEL GUI
from lib.uiForm.main_ui import Ui_FullAxis
from lib.uiForm.menu_lateral_ui import Ui_Lateral_menu
#from lib.uiForm.transform_ui import Ui_Form
from lib.uiForm.graph_ui import Ui_widget


# ==> LIBRERIAS PLUGINS
# AUN NO HAY NADA, TAREA : BUSCAR LA FORMA DE QUE SE CARGEN


#################################################################
#                      CLASES WIDGETS                           #
#################################################################

File = None

class WidgetGraph(QWidget):
    def __init__(self, *args, **kwargs):
        QWidget.__init__(self, *args, **kwargs)
        self.UI_vertical = Ui_widget()
        self.UI_vertical.setupUi(self)
        data_raw = old_exchange.dataFrame() 
        if File[1] == "JSON(*.json)":
            data_raw.read(File[0], "json")
            self.data1 = data_raw.onlyColumn("roll")
            self.data2 = data_raw.onlyColumn("pitch")
            self.data3 = data_raw.onlyColumn("yaw")
            self.timeMilli = data_raw.onlyColumn("time")
            self.time()
            self.graph()

        if File[1] == "CSV(*.csv)":
            data_raw.read(File[0], "csv")
            self.data1 = data_raw.onlyColumn("A")
            self.data1=self.normalize(self.data1)
            self.data2 = data_raw.onlyColumn("B")
            self.data2=self.normalize(self.data2)
            self.data3 = data_raw.onlyColumn("C")
            self.data3=self.normalize(self.data3)
            
            self.timeMilli = data_raw.onlyColumn("D")
            self.time()
            self.graph()

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

    def time(self):
        self.time = []
        calibrateTime = self.timeMilli[0]
        for x in self.timeMilli:
            self.time.append((x-calibrateTime)/1000)
    
    def verticalPos(self, data, div):
        sec = min(data)/div
        posVertical = sec*(div-1)
        return posVertical





    def graph(self):
        self.region1 = pg.LinearRegionItem()
        self.region2 = pg.LinearRegionItem()
        self.region3 = pg.LinearRegionItem()
        self.region1.setZValue(9)
        self.region2.setZValue(9)
        self.region3.setZValue(9)            
        self. region1.setRegion([(max(self.time)-1),max(self.time)])
        self. region2.setRegion([(max(self.time)-1),max(self.time)])
        self. region3.setRegion([(max(self.time)-1),max(self.time)])
                    
        pw1 = pg.PlotWidget(name='Plot1') 
        pw2 = pg.PlotWidget(name='Plot2')
        pw3 = pg.PlotWidget(name='Plot3')  

        pw1.addItem(self.region1, ignoreBounds=False)
        pw2.addItem(self.region2, ignoreBounds=False)
        pw3.addItem(self.region3, ignoreBounds=False)

        self.UI_vertical.layout_graph_1.addWidget(pw1)
        self.UI_vertical.layout_graph_2.addWidget(pw2)
        self.UI_vertical.layout_graph_3.addWidget(pw3)

        p1 = pw1.plot(self.time, self.data1, pen="c")
        p2 = pw2.plot(self.time, self.data2, pen="g")
        p3 = pw3.plot(self.time, self.data3, pen="r")


        div = 4
        posh1Line = self.verticalPos(self.data1, div)
        posh2Line = self.verticalPos(self.data2, div)
        posh3Line = self.verticalPos(self.data3, div)
        self.v1Line = pg.InfiniteLine(angle=90, movable=True)
        self.h1Line = pg.InfiniteLine(pos=posh1Line, angle=0, movable=True)
        self.v2Line = pg.InfiniteLine(angle=90, movable=True)
        self.h2Line = pg.InfiniteLine(pos=posh2Line,angle=0, movable=True)
        self.v3Line = pg.InfiniteLine(angle=90, movable=True)
        self.h3Line = pg.InfiniteLine(pos=posh3Line, angle=0, movable=True)

        self.v1Line.setZValue(10)
        self.v2Line.setZValue(10)
        self.v3Line.setZValue(10)
        self.h1Line.setZValue(10)
        self.h2Line.setZValue(10)
        self.h3Line.setZValue(10)

        pw1.addItem(self.v1Line, ignoreBounds=True)
        pw1.addItem(self.h1Line, ignoreBounds=True)
        pw2.addItem(self.v2Line, ignoreBounds=True)
        pw2.addItem(self.h2Line, ignoreBounds=True)
        pw3.addItem(self.v3Line, ignoreBounds=True)
        pw3.addItem(self.h3Line, ignoreBounds=True)

        self.region1.sigRegionChanged.connect(self.update)
        self.region2.sigRegionChanged.connect(self.update)
        self.region3.sigRegionChanged.connect(self.update)

        self.v1Line.sigDragged.connect(lambda:self.move_drag(1))
        self.v2Line.sigDragged.connect(lambda:self.move_drag(2))
        self.v3Line.sigDragged.connect(lambda:self.move_drag(3))
        self.h1Line.sigDragged.connect(lambda:self.move_drag(4))
        self.h2Line.sigDragged.connect(lambda:self.move_drag(5))
        self.h3Line.sigDragged.connect(lambda:self.move_drag(6))


    def move_drag(self, Q):
        self.v1Line.setZValue(10)
        self.v2Line.setZValue(10)
        self.v3Line.setZValue(10)
        self.h1Line.setZValue(10)
        self.h2Line.setZValue(10)
        self.h3Line.setZValue(10)

        if Q == 1:
            pos = self.v1Line.value()
            self.v2Line.setPos(pos)
            self.v3Line.setPos(pos)
        if Q == 2:
            pos = self.v2Line.value()
            self.v1Line.setPos(pos)
            self.v3Line.setPos(pos)
        if Q == 3:
            pos = self.v3Line.value()
            self.v1Line.setPos(pos)
            self.v2Line.setPos(pos)
        if Q == 4:
            pos = self.h1Line.value()
            #self.h2Line.setPos(pos)
            #self.h3Line.setPos(pos)
            self.UI_vertical.ampPoint_1.setText("""
            <span style='font-size: 10pt'>— :%0.2f°</span>"""
            % (pos))
        if Q == 5:
            pos = self.h2Line.value()
            #self.h1Line.setPos(pos)
            #self.h3Line.setPos(pos)
            self.UI_vertical.ampPoint_2.setText("""
            <span style='font-size: 10pt'>— :%0.2f°</span>"""
            % (pos))
        if Q == 6:
            pos = self.h3Line.value()
            #self.h1Line.setPos(pos)
            #self.h2Line.setPos(pos)
            self.UI_vertical.ampPoint_3.setText("""
            <span style='font-size: 10pt'>— :%0.2f°</span>"""
            % (pos))



    def update(self):

        self.region1.setZValue(9)
        self.region2.setZValue(9)
        self.region3.setZValue(9)
        minX_reg1, maxX_reg1 = self.region1.getRegion()
        minX_reg2, maxX_reg2 = self.region2.getRegion()
        minX_reg3, maxX_reg3 = self.region3.getRegion()

        ampRange_1 = self.closest(self.time, self.data1, maxX_reg1, minX_reg1)
        ampRange_2 = self.closest(self.time, self.data2, maxX_reg2, minX_reg2)
        ampRange_3 = self.closest(self.time, self.data3, maxX_reg3, minX_reg3)
                
        tdelta_reg1 = maxX_reg1-minX_reg1
        tdelta_reg2 = maxX_reg2-minX_reg2
        tdelta_reg3 = maxX_reg3-minX_reg3

        if minX_reg1 > 0 and maxX_reg1 < self.time[-1]:
            self.UI_vertical.lbl_tiempo_1.setText("""
            <span style='font-size: 10pt'>%0.2f,
            <span style='font-size:7pt'>(%0.1f,%0.1f)</span>"""
            % (tdelta_reg1, minX_reg1,maxX_reg1))
            self.UI_vertical.ampRange_1.setText("""
            <span style='font-size: 10pt'>|-| :  %0.2f°</span>"""
            % (ampRange_1))

        if minX_reg2 > 0 and maxX_reg2 < self.time[-1]:
            self.UI_vertical.lbl_tiempo_2.setText("""
            <span style='font-size: 10pt'>%0.2f,
            <span style='font-size:7pt'>(%0.1f,%0.1f)</span>"""
            % (tdelta_reg2, minX_reg2,maxX_reg2))
            self.UI_vertical.ampRange_2.setText("""
            <span style='font-size: 10pt'>|-| :%0.2f°</span>"""
            % (ampRange_2))



        if minX_reg3 > 0 and maxX_reg3 < self.time[-1]:
            self.UI_vertical.lbl_tiempo_3.setText("""
            <span style='font-size: 10pt'>%0.2f,
            <span style='font-size:7pt'>(%0.1f,%0.1f)</span>"""
            % (tdelta_reg3, minX_reg3,maxX_reg3))
            self.UI_vertical.ampRange_3.setText("""
            <span style='font-size: 10pt'>|-| :%0.2f°</span>"""
            % (ampRange_3))



    def closest(self, lstin, lstout, maxX, minX): 

        array = np.asarray(lstin)
        index_0 = (np.abs(array - minX)).argmin()
        index_1 = (np.abs(array - maxX)).argmin()

        #closed_0 = lstin[minX(range(len(lstin)), key = lambda i: abs(lstin[i]-minX))]
        #closed_1 = lstin[maxX(range(len(lstin)), key = lambda i: abs(lstin[i]-maxX))]
        #index_0 = self.time.index(closed_0)
        #index_1 = self.time.index(closed_1)
        data_0 = lstout[index_0]
        data_1 = lstout[index_1]
        Amp = abs(data_1-data_0)
        return Amp

 
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

#################################################################
#                      CLASE PRINCIPAL                          #
#################################################################


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
            self.ui.Login_Layout.addWidget(btn_logout)
            self.lateralMenu()
            self.homePage()

        else:
            UIFunc.resetLayout(self, self.ui.Login_Layout)
            user = QMenu()
            user.addAction("Cuenta Online", self.btnloginMethod)
            btn_logout = UIFunc.ButtonFlat(self, "Ingresar a la cuenta")
            btn_logout.setMenu(user)
            self.ui.Login_Layout.addWidget(btn_logout)
            self.lateralMenu()


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
        self.ui.Center_layout.addWidget(WidgetGraph())


    # def transformPage(self):
    #   transformPage = Widgettransform()
      #  self.ui.Center_layout.addWidget(transformPage)

    def lateralMenu(self):
        # => CARGA WIDGET
        self.LateralMenu = WidgetLateralMenu()
        # =>SE CREAN LOS BOTONES
        btn_home = UIFunc.createBtnMenuLat(
            self, "btn_home", "", "home", "Inicio")
        btn_open = UIFunc.createBtnMenuLat(
            self, "btn_open", "", "folder", "Abrir")
        btn_graph = UIFunc.createBtnMenuLat(
            self, "btn_graph", "", "chart-line", "Medir")
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
        global File

        btnWidget = self.sender()

        if btnWidget.objectName() == "btn_home":
            UIFunc.resetLayout(self, self.ui.Center_layout)
            self.homePage()
            UIFunc.resetStyle(self, "btn_home")
            btnWidget.setStyleSheet(UIFunc.selectMenu(btnWidget.styleSheet()))

        if btnWidget.objectName() == "btn_open":
            UIFunc.resetLayout(self, self.ui.Center_layout)
            UIFunc.resetStyle(self, "btn_graph")
            path = UIFunc.openFile(self)
            File = path
            self.graphPage()
            btnWidget.setStyleSheet(UIFunc.selectMenu(btnWidget.styleSheet()))


        if btnWidget.objectName() == "btn_graph":
            if File:
                UIFunc.resetLayout(self, self.ui.Center_layout)
                self.ui.Center_layout.addWidget(WidgetGraph())
                UIFunc.resetStyle(self, "btn_graph")
                btnWidget.setStyleSheet(UIFunc.selectMenu(btnWidget.styleSheet()))

    def closeEvent(self, event):
        if os.path.isfile(PATH.LOGINLOCK):
            UIFunc.logout(self)


#################################################################
#                      SE INICIA EL PROGRAMA                     #
#################################################################
if __name__ == "__main__":
    sttg_workspace = basic.read_setting('workspace.json')
    path_workspace = sttg_workspace['Path']
    bol_oline = sttg_workspace['workspace_online']

#    app = QApplication(sys.argv)
    app = QApplication([])
    app.setStyle('Windows')
    # print(QStyleFactory.keys())
    window = MainWindow()
    sys.exit(app.exec_())
