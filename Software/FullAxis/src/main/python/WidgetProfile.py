   
import datetime

import qtawesome as qta
from PySide6.QtCore import QDate, Qt
from PySide6.QtGui import QAction, QCursor
from PySide6.QtWidgets import (QMenu, QMessageBox, QTreeWidgetItem,
                               QVBoxLayout, QWidget)

from BasicTest import BasicTest
from lib.basic_profile_ui import Ui_Profile_user
from profile_data import (ActivityData, DeleteData, ListProfiles, ProfileData,
                          SessionData)
from Widgets_test import WidgetSOT, WidgetTUG
from ui_helper import helpers


class Profile(QWidget,Ui_Profile_user):
    def __init__(self, profile):
        super().__init__()
        self.setupUi(self)
        self.tabWidget.setTabEnabled(1, False)
        self.tabWidget.setTabEnabled(2, False)
        self.session = None
        self.profile = None
        self.configure_btn()
        self.menu_list_delete_action = QAction("Delete")
        self.menu_list_delete_action.triggered.connect(lambda: self.menu_list_delete_item(None))
        self.menu_list_records = QMenu()
        self.menu_list_records.addAction(self.menu_list_delete_action)
        self.list_records.setContextMenuPolicy(Qt.CustomContextMenu)
        self.list_records.customContextMenuRequested.connect(self.handle_right_click)

        if profile:
            self.profile = profile
            self.user_fill(profile)
        else:
            self.clean_data()

    def handle_right_click(self, position):
        self.menu_list_select_id_unique = None
        if item := self.list_records.currentItem():
            if item.text(0):
                self.type_current_item = "session"
            elif item.text(1) in ["SOT", "TUG"]:
                self.type_current_item = "test"
            if self.list_records.itemAt(position) :
                self.menu_list_select_id_unique = item.text(3)
                self.menu_list_records.exec_(QCursor.pos())
    
    def menu_list_delete_item(self , i):

        if i is None:
            self.create_win_delete_item()
        elif i.text() == "&Yes":
            id_unique = [
                int(i)
                for i in self.menu_list_select_id_unique.split(".")
                if i.isdigit()
            ]
            DeleteData(self.profile, id_unique)
            self.change_data_list(True)

    def create_win_delete_item(self):
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Warning)
        msgBox.setText("Do you want to delete this item?")
        msgBox.setStandardButtons(QMessageBox.Yes | QMessageBox.Cancel)
        msgBox.buttonClicked.connect(self.menu_list_delete_item)
        msgBox.exec()


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
        if self.tabWidget.isTabVisible(3):
            self.tabWidget.removeTab(3)
        self.tabWidget.setTabText(2, "Sessions")
        ###esto no lo hace ni idea de porque?
        date_now = datetime.datetime.now()
        date = f"{date_now.day}.{date_now.month}.{date_now.year}"
        self.input_date_birth.setMaximumDate(QDate.fromString(date, "dd.MM.yyyy"))
        self.input_date_birth.setDate(QDate.fromString(date, "dd.MM.yyyy"))

    def user_fill(self, user):
        if self.tabWidget.isTabVisible(3):
            self.tabWidget.removeTab(3)
        self.tabWidget.setTabText(2, "Sessions")
        self.tabWidget.setTabEnabled(2, False)
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
            self.set_item_list_record(session, 0, icon_folder, s)
            activities=ActivityData().load_activities(profile, s["unique_id"])
            for a in activities:
                activity = QTreeWidgetItem()
                self.set_item_list_record(activity, 1, icon_file, a)
                session.addChild(activity)
        self.list_records.itemDoubleClicked.connect(self.handler)
        self.list_records.itemClicked.connect(self.handler_expand)

    def set_item_list_record(self, arg0, arg1, arg2, arg3):
        arg0.setIcon(arg1, arg2)
        arg0.setText(arg1, arg3['name'])
        arg0.setText(2, arg3['date_create'])
        arg0.setText(3, arg3['unique_id'])

    def create_new_session(self):
        data = SessionData().create_session(int(self.input_number.text()))
        self.populate_list_records(self.profile, data)

    def handler(self, item, column_no):
        if item.text(0):
                self.tabWidget.setTabEnabled(2, True)
                self.tabWidget.setTabText(2, item.text(0))
                self.session = item.text(0)
        if item.text(1):
                self.view_results(item.text(1),item.text(2), item.text(3))
    
    def handler_expand(self, item, column_no):
        if item.text(0):
            if not item.isExpanded():
                    item.setExpanded(True)
            else:
                item.setExpanded(False)
                
    def create_new_test(self, profile:str, session, test:str):
        self.test_current = test
        if "widget_test" in dir(self):
            self.widget_test.new()
        else:
            helpers.reset_layout(self,self.layout_session)
            self.widget_test = BasicTest()
            self.widget_test.save_true.connect(self.change_data_list)
            self.widget_test.set_data(profile, session, self.test_current)
            self.list_records.clear()
            self.load_session(profile)
            self.layout_session.addWidget(self.widget_test)
        
    def view_results(self,name_test, date, unique_id):
        if self.tabWidget.isTabVisible(3):
            self.tabWidget.removeTab(3)
        new_tab = QWidget()
        new_tab.setObjectName(u"view_results")
        self.layout_view_results = QVBoxLayout(new_tab)
        name_tab = f"{name_test} {date}"
        self.tabWidget.insertTab(3, new_tab, name_tab)
        self.load_results(name_test, unique_id)

    def change_data_list(self, data):
        if data:
            self.list_records.clear()
            self.load_session(self.profile)

    def load_results(self, name, unique_id):
        helpers.reset_layout(self,self.layout_view_results)
        if name == "TUG":
            widget_results = WidgetTUG()
        elif name =="SOT":
            widget_results = WidgetSOT()
        self.layout_view_results.addWidget(widget_results)
        data_db = ActivityData().load_data(self.profile, unique_id)
        widget_results.draw_graph(data_db)        
