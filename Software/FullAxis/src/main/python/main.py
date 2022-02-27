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

from init import context
from PySide6.QtWidgets import QMainWindow, QWidget, QTreeWidgetItem

from lib.basic_profile import Ui_Form as BasicProfile
from lib.basic_test import Ui_Form as BasicTest
from lib.main_ui import Ui_MainWindow
from plug_hw import reset_hw, verify_receptor_serial
from save_profile import ProfileData, SessionData

class Profile(QWidget, BasicProfile):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.btn_save.clicked.connect(self.save_profile_data)
        self.tabWidget.setTabEnabled(1, False)
        #self.tabWidget.setTabEnabled(2, False)
        self.btn_create_session.clicked.connect(self.create_new_session)
        


    def populate_records(self):
        list = ["una", "dos", "tres"]
        self.list_records.addItems(list)

    def create_new_session(self):
        test = SessionData()
        name, position = test.create_session(int(self.input_number.text()))
        new_session = QTreeWidgetItem(self.list_records)
        #new_session = self.list_records.topLevelItem(position)
        new_session.setText(0, name)
       


    def save_profile_data(self):
        profile_data = ProfileData()
        number_unique = self.input_number.text()
        number_unique = profile_data.set_data(
            first_name = self.input_first_name.text(), 
            last_name  = self.input_last_name.text(),
            data_birth= self.input_date_birth.date().toString("dd.MM.yyyy"),
            id = self.input_id.text(),
            info = self.input_info.toMarkdown(),
            number_unique = number_unique
            )
        if number_unique != None:
            self.input_number.setText(str(number_unique))
            self.tabWidget.setTabEnabled(1, True)


class  Test(QWidget, BasicTest):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

class MainWindows(QMainWindow, Ui_MainWindow):
    def __init__(self, port):
        super().__init__()
        self.port_receptor = port
        self.setupUi(self)
        self.configure_window()
        self.show()
        self.verify_connection()
        self.btns_tools_clicked()


    def configure_window(self) -> None:
        self.resize(800,600)
        self.setWindowTitle("FullAxis")

    def verify_connection(self) -> None:
        if self.port_receptor is None:
            self.btn_connect.setEnabled(True)
            self.btn_view_raw.setEnabled(False)
        else:
            self.btn_connect.setEnabled(False)
            self.btn_view_raw.setEnabled(True)
    
    def btns_tools_clicked(self) -> None:
        self.btn_new_profile.clicked.connect(self.new_profile)
    

    def new_profile(self) -> None:
        self.profile = Profile()
        self.resetLayout(self.layout_central)
        self.layout_central.addWidget(self.profile)



    def resetLayout(self, layout):
        for i in reversed(range(layout.count())): 
            widgetToRemove = layout.itemAt(i).widget()
            # remove it from the layout list
            layout.removeWidget(widgetToRemove)
            # remove it from the gui
            widgetToRemove.setParent(None) 

    def capture(self):
        print("capturando|")
         

if __name__ == "__main__":
    port = verify_receptor_serial()
    windows = MainWindows(port)
    exit_code = context.app.exec()
    reset_hw(port)
    sys.exit(exit_code)
