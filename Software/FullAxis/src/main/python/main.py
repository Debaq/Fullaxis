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

import datetime

import qtawesome as qta
import qtvscodestyle as qtvsc
from PySide6.QtCore import QDate, Qt, Signal
from PySide6.QtWidgets import QMainWindow, QTreeWidgetItem, QWidget, QVBoxLayout

from init import context
from lib.basic_profile_ui import Ui_Profile_user
from lib.basic_test_ui import Ui_Test_basic
from lib.list_user_ui import Ui_List_user
from lib.main_ui import Ui_MainWindow
from plug_hw import FullAxisReceptor, ReceiverData
from profile_data import ActivityData, ListProfiles, ProfileData, SessionData
from ui_helper import helpers
from Widgets_test import WidgetSOT, WidgetTUG


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
            #position = i['number_unique']
            #self.list_user.topLevelItem(position)
        self.list_user.itemDoubleClicked.connect(self.handler)

    def handler(self, item, column_no):
        number_user = "profile_{:05d}".format(int(item.text(0)))
        self.user_selected.emit(number_user)
        
class Profile(QWidget,Ui_Profile_user):
    def __init__(self, profile):
        super().__init__()
        self.setupUi(self)
        self.tabWidget.setTabEnabled(1, False)
        self.tabWidget.setTabEnabled(2, False)
        selmodel = self.list_records.selectionModel()
        selmodel.selectionChanged.connect(self.handle_selection)
        self.session = None
        self.profile = None
        self.configure_btn()
        if profile:
            self.profile = profile
            self.user_fill(profile)
        else:
            self.clean_data()
        
    def configure_btn(self):
        self.btn_save.clicked.connect(self.save_profile_data)
        self.btn_create_session.clicked.connect(self.create_new_session)
        self.btn_new_sot.clicked.connect(
            lambda : self.create_new_test(
                self.profile, 
                self.session, 
                "SOT"))
        self.btn_new_tug.clicked.connect(
            lambda : self.create_new_test(
                self.profile, 
                self.session, 
                "TUG"))
    
    def clean_data(self):
        self.input_id.setText("")
        self.input_number.setText("nn")
        self.input_first_name.setText("")
        self.input_last_name.setText("")
        self.tabWidget.setTabEnabled(1, False)
        self.tabWidget.setTabEnabled(2, False)
        self.session = None
        self.profile = None
        self.list_records.clear()
        self.input_info.setText("")
        ###esto no lo hace ni idea de porque?
        date_now = datetime.datetime.now()
        date = "{}.{}.{}".format(date_now.day, date_now.month, date_now.year)
        self.input_date_birth.setMaximumDate(QDate.fromString(date, "dd.MM.yyyy"))
        self.input_date_birth.setDate(QDate.fromString(date, "dd.MM.yyyy"))

    def user_fill(self, user):
        profile = (ListProfiles().get_profile_full(user))
        self.input_id.setText(profile['id'])
        self.input_number.setText(str(profile['number_unique']))
        self.input_first_name.setText(profile['first_name'])
        self.input_last_name.setText(profile['last_name'])
        self.input_info.setText(profile['info'])
        self.input_date_birth.setDate(QDate.fromString(profile['data_birth'], "dd.MM.yyyy"))
        self.tabWidget.setTabEnabled(1, True)
        self.load_session(user)
        self.tabWidget.setCurrentIndex(0)

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
            self.profile = "profile_{:05d}".format(number_unique)

    def load_session(self, profile):
        self.profile = profile
        self.list_records.clear()
        sessions_data=SessionData().load_sessions(profile)
        self.populate_list_records(profile, sessions_data)
        
    def populate_list_records(self, profile:str, sessions:list):
        """
        Recibe una lista de sesiones desde tinydb y la muestra en el QTreeWidget
        además busca las actividades y las carga como child dentro de las sessiones

        Args:
            profile (str): numero del perfil debe estar seteado como perfil_{:05d}
            sessions (list): lista con todas las sessiones de un perfil que sean del 
            tipo "session"
        """
        icon_folder = qta.icon('fa.folder', selected='fa.folder-open',
                        color_off='orange',
                        color_on='orange')
        icon_file = qta.icon('ri.file-chart-line', color='green')
        for s in sessions:
            session = QTreeWidgetItem(self.list_records)
            session.setIcon(0, icon_folder)
            session.setText(0, s['name'])
            session.setText(2, s['date_create'])
            activities=ActivityData().load_activities(profile, s["unique_id"])
            for a in activities:
                activity = QTreeWidgetItem()
                activity.setIcon(1, icon_file)
                activity.setText(1, a['name'])
                activity.setText(2, a['date_create'])
                session.addChild(activity)
            
    def create_new_session(self):
        data = SessionData().create_session(int(self.input_number.text()))
        self.populate_list_records(self.profile, data)
        
    def handle_selection(self, selected, deselected):
        for index in selected.indexes():
            item = self.list_records.itemFromIndex(index)
            if item.text(0):
                self.tabWidget.setTabEnabled(2, True)
                self.tabWidget.setTabText(2, item.text(0))
                self.session = item.text(0)
            if item.text(1):
                self.view_results(item.text(1),item.text(2))
            #profile = self.input_number.text()
            #self.data_export.emit([profile, item.text(0)])
            #print('SEL: row: %s, col: %s, text: %s' % (
            #    index.row(), index.column(), item.text(0)))
        for index in deselected.indexes():
            item = self.list_records.itemFromIndex(index)
            #print('DESEL: row: %s, col: %s, text: %s' % (
            #    index.row(), index.column(), item.text(0)))

    def create_new_test(self, profile:str, session, test:str):
        helpers.reset_layout(self,self.layout_session)
        widget_test = BasicTest()
        widget_test.set_data(profile, session, test)
        self.list_records.clear()
        self.load_session(profile)
        self.layout_session.addWidget(widget_test)
        
    def view_results(self,name, date):
        new_tab = QWidget()
        new_tab.setObjectName(u"view_results")
        self.layout_view_results = QVBoxLayout(new_tab)
        name = "{} {}".format(name, date)
        self.tabWidget.addTab(new_tab, name)




class  BasicTest(QWidget, Ui_Test_basic):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.buttons_disabled = True
        self.capture = False
        #self.activate_serial()
        self.combo_serial_complete()
        self.btns_icons()
        self.btns_tools_clicked()

    def set_data(self, profile:str, session, test:str) -> None:
        self.profile = profile
        self.session = session
        if test == "TUG":
            self.create_tug_test()
            self.check_delay.stateChanged.connect(self.with_delay)
        elif test == "SOT":
            self.create_sot_test()
    
    def get_unique_id(self) -> str:
        return self.activity_data['unique_id']
            
    def create_tug_test(self) -> None:
        self.widget = WidgetTUG()
        helpers.reset_layout(self, self.layout_test)
        self.layout_test.addWidget(self.widget)
        self.create_db("TUG")
    
    def create_db(self, type_test):
        db = ActivityData()
        self.activity_data = db.create_activity(self.profile, self.session, type_test)
        
    def reset_graph(self):
        self.widget.reset_graph()

    def with_delay(self):
        #self.widget.set_with_delay(self.check_delay.isChecked())
        self.widget.with_delay = self.check_delay.isChecked()

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
    
    def create_sot_test(self):
        widget = WidgetTUG()
        helpers.reset_layout(self, self.layout_test)
        self.layout_test.addWidget(widget)
        
    def connect_serial(self):
        port = self.combo_serial.currentText()
        connection = FullAxisReceptor()
        connection.activate_connection(port)
        connection.reset()
        self.receiver = ReceiverData()
        self.receiver.start()
        self.receiver.set_connection(connection)
        self.receiver.data.connect(self.receive_data_and_graph)

    def combo_serial_complete(self) -> None:
        ports = FullAxisReceptor()
        icon_signal = qta.icon('fa5s.signal',color='#c5c5c5')

        for i in ports.search_ports():
            if i[2] != 'n/a':
                self.combo_serial.addItem(icon_signal, i[0])
                self.combo_serial.setCurrentText(i[0])
            else:
                self.combo_serial.addItem(i[0])
                
    def save_data(self):
        db = ActivityData()
        unique_id = self.activity_data['unique_id']
        data = self.widget.get_data()
        db.save_data(self.profile, unique_id, data)
        self.btn_capture.setEnabled(False)
        self.btn_reset.setEnabled(False)
        
                
    def btns_icons(self) -> None:
        terminal = qta.icon('fa5s.terminal', color='#c5c5c5')
        icon_conect = qta.icon('fa5s.plug', color='#c5c5c5')
        self.btn_view_raw.setIcon(terminal)
        self.btn_connect.setIcon(icon_conect)
        
        
    def btns_tools_clicked(self) -> None:
        self.btn_connect.clicked.connect(self.connect_serial)
        self.btn_capture.clicked.connect(self.test_variable)
        self.btn_save.clicked.connect(self.save_data)
        self.btn_reset.clicked.connect(self.reset_graph)
        
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
        user_new = qta.icon('ri.user-add-line', color='#c5c5c5')
        user_list = qta.icon('ri.contacts-book-line', color='#c5c5c5')
        self.btn_new_profile.setIcon(user_new)
        self.btn_open_profile.setIcon(user_list)    
        
    def btns_tools_clicked(self) -> None:
        self.btn_new_profile.clicked.connect(lambda:self.new_profile(None))
        self.btn_open_profile.clicked.connect(self.open_profile)
    
    def new_profile(self, user) -> None:
        if not 'profile' in dir(self):
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
    theme_file = context.get_resource("OneDark-Pro-flat.json")
    stylesheet = qtvsc.load_stylesheet(theme_file)
    windows.setStyleSheet(stylesheet)
    exit_code = context.app.exec()
    sys.exit(exit_code)
