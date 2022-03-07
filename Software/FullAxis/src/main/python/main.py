# -*- coding: utf-8 -*-

#################################################################
#                                                               #
#                  NAME PROJECT : FULLAXIS                      #
#                   VER. 22.2.25 - GUI PySide6                  #
#                    NAME  VER. : reboot                        #
#               CREATOR : DAVID ÁVILA QUEZADA                   #
#                          AKA: NICOLÁS QUEZADA BAIER           #
#                                                               #
#################################################################

import os
import sys


os_system = 'win' if os.name == 'nt' else 'linux'

if len(sys.argv) > 1:
    from init import ParameterInput
    parameters = ParameterInput(sys.argv[1], os_system)
    if parameters.final_state == "stop":
        sys.exit()


import qtawesome as qta
from PySide6.QtCore import Qt, Signal
from PySide6.QtWidgets import (QMainWindow,QTreeWidgetItem,QWidget)
from init import context
from lib.list_user_ui import Ui_List_user
from lib.main_ui import Ui_MainWindow
from profile_data import ListProfiles
from ui_helper import helpers
from WidgetProfile import Profile




class ListUser(QWidget, Ui_List_user):
    user_selected = Signal(str)
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)
        self.list_user.setSortingEnabled(True)
        self.list_user.sortByColumn(0, Qt.AscendingOrder)
        self.complete_list_user()

    def complete_list_user(self):
        list_user = ListProfiles().get_list_profile_full()
        icon = qta.icon('ri.user-line', selected='ri.user-received-2-line',
                        color_off='orange',
                        color_on='orange')
        for i in list_user:
            item = QTreeWidgetItem(self.list_user)
            item.setIcon(0, icon)
            item.setText(0, str(i['number_unique']))
            item.setText(1, i['id'])
            item.setText(2, i['first_name'])
            item.setText(3, i['last_name'])
        self.list_user.itemDoubleClicked.connect(self.handler)

    def handler(self, item, column_no):
        number_user = "profile_{:05d}".format(int(item.text(0)))
        self.user_selected.emit(number_user)
   
        
class MainWindows(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.configure_window()
        self.btns_tools_clicked()
        self.btns_icons()
        self.show()
       
    def configure_window(self) -> None:
        self.resize(1024,600)
        self.setWindowTitle("FullAxis")

    def open_profile(self):
        self.list_user = ListUser()
        self.list_user.user_selected.connect(self.load_profile)
        helpers.reset_layout(self, self.layout_central)
        self.layout_central.addWidget(self.list_user)        
        
    def load_profile(self, user):
        helpers.reset_layout(self, self.layout_central)
        if 'profile' in dir(self):
            self.layout_central.addWidget(self.profile)
            self.profile.user_fill(user)
        else:
            self.new_profile(user)
        
    def btns_icons(self):
        user_new = qta.icon('ri.user-add-line', color='#595959')
        user_list = qta.icon('ri.contacts-book-line', color='#595959')
        self.btn_new_profile.setIcon(user_new)
        self.btn_open_profile.setIcon(user_list)    
        
    def btns_tools_clicked(self) -> None:
        self.btn_new_profile.clicked.connect(lambda:self.new_profile(None))
        self.btn_open_profile.clicked.connect(self.open_profile)
    
    def new_profile(self, user) -> None:
        if 'profile' not in dir(self):
            self.profile = Profile(user)
        if user is None:
            self.profile.clean_data()
        helpers.reset_layout(self, self.layout_central)
        self.layout_central.addWidget(self.profile)

        
if __name__ == "__main__":
    windows = MainWindows()
    """ extra = {
    
    # Density Scale
    'density_scale': '-2',
}

     apply_stylesheet(windows, theme='dark_teal.xml', extra=extra)
     """
    #theme_file = context.get_resource("OneDark-Pro-flat.json")
    #stylesheet = qtvsc.load_stylesheet(theme_file)
    #windows.setStyleSheet(stylesheet)
    exit_code = context.app.exec()
    sys.exit(exit_code)

###error observado 
"""
guarda la prueba antes de presionar el boton de guardar (solucionado)
se pega la conexion cuando se intenta tomar mas de una prueba (solucionado)
cambiar list de datos en graph de list a numpy.array (solucionado)
no tiene sentido el flujod e los botones capture y reset
existe un delay del buffer luego de los 5 segundos (ni idea hay que probarlo)
no se pueden borrar las sesiones(incompleto) ni las pruebas (solucionado)
no puede medir en los graficos de la vista de la prueba (solucionado)
cambiar en el eje y amplitud por nombre de plano (solucionado)
poner dibujo para los ejes (solucionado)

"""
