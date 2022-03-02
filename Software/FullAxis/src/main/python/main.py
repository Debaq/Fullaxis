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
from lib.main_ui import Ui_MainWindow
from lib.basic_test import Ui_Test_basic
from plug_hw import ReceiverData
from save_profile import ProfileData, SessionData
from Widgets_test import WidgetTUG, WidgetSOT

class Profile(QWidget, BasicProfile):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.btn_save.clicked.connect(self.save_profile_data)
        self.tabWidget.setTabEnabled(1, False)
        self.tabWidget.setTabEnabled(2, False)
        self.btn_create_session.clicked.connect(self.create_new_session)
        selmodel = self.list_records.selectionModel()
        selmodel.selectionChanged.connect(self.handle_selection)
        self.btn_new_sot.clicked.connect(self.create_new_sot)
        self.btn_new_tug.clicked.connect(self.create_new_tug)
      
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

    def create_new_session(self):
        test = SessionData()
        name, position = test.create_session(int(self.input_number.text()))
        new_session = QTreeWidgetItem(self.list_records)
        new_session = self.list_records.topLevelItem(position)
        new_session.setText(0, name)
    
    def handle_selection(self, selected, deselected):
        for index in selected.indexes():
            item = self.list_records.itemFromIndex(index)
            self.tabWidget.setTabEnabled(2, True)
            self.tabWidget.setTabText(2, item.text(0))
            #print('SEL: row: %s, col: %s, text: %s' % (
            #    index.row(), index.column(), item.text(0)))
        for index in deselected.indexes():
            item = self.list_records.itemFromIndex(index)
            #print('DESEL: row: %s, col: %s, text: %s' % (
            #    index.row(), index.column(), item.text(0)))

    def create_new_sot(self):
        self.resetLayout(self.layout_session)
        self.layout_session.addWidget(BasicTest("SOT"))

    def create_new_tug(self):
        self.resetLayout(self.layout_session)
        self.layout_session.addWidget(BasicTest("TUG"))


    def resetLayout(self, layout):
        for i in reversed(range(layout.count())): 
            widgetToRemove = layout.itemAt(i).widget()
            # remove it from the layout list
            layout.removeWidget(widgetToRemove)
            # remove it from the gui
            widgetToRemove.setParent(None) 

class  BasicTest(QWidget, Ui_Test_basic):
    def __init__(self, model):
        super().__init__()
        self.setupUi(self)
        
        self.btn_capture.clicked.connect(self.test_variable)
        self.btn_reset.clicked.connect(self.reset_graph)
        self.buttons_disabled = True
        self.capture = False
        self.activate_serial()

        if model == "TUG":
            self.create_tug_test()
            self.check_delay.stateChanged.connect(self.with_delay)
        elif model == "SOT":
            self.create_sot_test()
    

    def create_tug_test(self):
        self.widget = WidgetTUG()
        self.resetLayout(self.layout_test)
        self.layout_test.addWidget(self.widget)

    def reset_graph(self):
        self.widget.reset_graph()

    def with_delay(self):
        #self.widget.set_with_delay(self.check_delay.isChecked())
        self.widget.with_delay = self.check_delay.isChecked()

    def activate_serial(self):
        self.receiver = ReceiverData()
        self.receiver.start()
        self.receiver.data.connect(self.receive_data_and_graph)


    def receive_data_and_graph(self, data):
        if self.buttons_disabled:
            self.buttons_disabled = False
            self.btn_capture.setEnabled(True)
            self.btn_reset.setEnabled(True)
            
        if self.capture == True:
            if not self.widget.stop:
                self.widget.update_graph_display(data)
            else:
                #self.receiver.quit()
                #self.receiver.data.disconnect(self.receive_data_and_graph)
                self.capture = False
                self.btn_capture.setText("Capture")
                self.btn_save.setEnabled(True)

    def test_variable(self):
        if self.capture == False:
            self.capture = True
            self.btn_capture.setText("Pause")
            time_max = self.time_max.value()
            self.widget.set_time_max(time_max)
        else:
            self.capture = False
            self.btn_capture.setText("Capture")
    
    def capture_data(self):
        self.activate_serial()

    def create_sot_test(self):
        widget = WidgetTUG()
        self.resetLayout(self.layout_test)
        self.layout_test.addWidget(widget)
    
    def resetLayout(self, layout):
        for i in reversed(range(layout.count())): 
            widgetToRemove = layout.itemAt(i).widget()
            # remove it from the layout list
            layout.removeWidget(widgetToRemove)
            # remove it from the gui
            widgetToRemove.setParent(None) 


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
    #port = verify_receptor_serial()
    windows = MainWindows(None)
    exit_code = context.app.exec()
    #reset_hw(port)
    sys.exit(exit_code)
