import contextlib

import qtawesome as qta
from PySide6.QtCore import QDate, Qt, Signal
from PySide6.QtGui import QIcon, QPixmap
from PySide6.QtWidgets import QMenu, QPushButton, QTreeWidgetItem, QWidget
from UI.Ui_form_basic import Ui_from_basic
from UI.Ui_new_profile import Ui_new_profile
from UI.Ui_search_bar import Ui_search_bar
from UI.Ui_tool_bar import Ui_tool_bar
from UI.Ui_windows_principal import Ui_win_principal

from lib.helpers.calculate import cal_age
from lib.profile_data import ListProfiles, ProfileData
from lib.autocomplete_list import AutoCompleteEdit

from base import context


def set_button_icon(button:QPushButton, 
                    icon:str,
                    color:str='#595959',
                    size:int=20,
                    tool_tip:str=None) -> QPushButton:
    
    if tool_tip is not None:
        button.setToolTip(tool_tip)
    icon = qta.icon(icon, color=color, color_active='#5d91f6')
    button.setStyleSheet(f"icon-size : {size}px;")
    button.setIcon(icon)
    button.setText('')
    return button


class UiToolBar(QWidget, Ui_tool_bar):
    state = Signal(list)
    def __init__(self, data,parent=None):
        super(UiToolBar, self).__init__(parent)
        self.data = data
        self.setupUi(self)
        self._btn_configure()
        self.start_test_state = False
        self.connect_9axis = False
        self._init_9axis_data()
        
    def _btn_configure(self):
        set_button_icon(self.btn_start, 'ph.play', size=30, tool_tip="Iniciar prueba")
        set_button_icon(self.btn_save, 'ph.floppy-disk', size=30, tool_tip="Guardar")
        set_button_icon(self.btn_config, 'ph.gear', size=30, tool_tip="Configurar")
        set_button_icon(self.btn_connect, 'ph.wifi-x', size=30, tool_tip="Conectar")
        set_button_icon(self.btn_battery, 'ph.battery-warning', size=20)
        set_button_icon(self.btn_new, 'ph.file-plus', size=30, tool_tip="nueva prueba")
        self.btn_start.clicked.connect(self.start_test)
        self.btn_save.clicked.connect(self.save)
        self._menu_new_test()
    
    def _menu_new_test(self):
        m_new_test = QMenu()
        m_new_test.addAction("TUG", lambda: self._new_test("TUG"))
        m_new_test.addAction("SOT", lambda: self._new_test("SOT"))
        m_new_test.addAction("VNG", lambda: self._new_test("VNG"))
        self.btn_new.setMenu(m_new_test)
        self.btn_new.menu()
    
    def _new_test(self, label):
        self.state.emit(["new", self.data, self.n_tab, label, self.profile])
    
    def _init_9axis_data(self):
        self.lbl_roll.setText("--")
        self.lbl_pitch.setText("--")
        self.lbl_yaw.setText("--")
        self.lbl_batt.setText("--")
        
    def set_number_tab(self, number):
        self.n_tab = number
        
    def get_number_tab(self):
        return self.n_tab
    
    def set_profile(self, profile):
        self.profile = profile
        
    def save(self):
        self.state.emit(["save", self.data, self.n_tab])
    
    def start_test(self):
        if self.start_test_state == False:
            signal = ["start", self.data, self.n_tab]
            self._start_pause('ph.stop', "Pausar prueba", True, signal)
        else:
            signal = ["stop", self.data, self.n_tab]
            self._start_pause('ph.play', "Iniciar prueba", False, signal)

    def _start_pause(self, icon:str, tool_tip:str, state:bool, signal:list)->None:
        set_button_icon(self.btn_start, icon, size=30, tool_tip=tool_tip)
        self.start_test_state = state
        self.state.emit(signal)
            
        

class UiFormBasic(QWidget, Ui_from_basic):
    state = Signal(list)
    def __init__(self, data,parent=None) -> None:
        super(UiFormBasic, self).__init__(parent)
        self.setupUi(self)
        self.control = UiToolBar(data)
        self.verticalLayout.addWidget(self.control)
        self.control.state.connect(self.emit_signal)
    
    def emit_signal(self, signal):
        self.state.emit(signal)
        
    def set_number(self, number):
        self.control.set_number_tab(number)
    
    def get_number(self)->int:
        return self.control.get_number_tab()
    
    def set_profile(self, profile):
        self.control.set_profile(profile)
        

class UiNewProfile(QWidget, Ui_new_profile):
    exit_= Signal(bool)
    def __init__(self, parent=None):
        super(UiNewProfile, self).__init__(parent)
        self.setupUi(self)
        self.change_connect_save()
        self.profile_data = ProfileData()

        self.btn_cancel_new_profile.clicked.connect(lambda: self.exit_.emit(True))
    
    def change_connect_save(self, save=True):
        if save:
            with contextlib.suppress(RuntimeError):
                self.btn_save_new_profile.clicked.disconnect()
            self.btn_save_new_profile.setText("Crear")
            self.btn_save_new_profile.clicked.connect(self.new_profile)
        else:
            self.btn_save_new_profile.clicked.disconnect()
            self.btn_save_new_profile.setText("Guardar")
            self.btn_save_new_profile.clicked.connect(self.modify_profile)
            
    def new_profile(self):
        first_name = self.line_name.text(), 
        last_name  = self.line_lastname.text(),
        data_birth= self.input_date_birth.date().toString("dd.MM.yyyy"),
        _id = self.line_id.text()
            
        if first_name and last_name and data_birth and _id:
            number_unique = self.input_number.text()
            number_unique = self.profile_data.set_data(
                first_name = first_name[0], 
                last_name  = last_name[0],
                data_birth= data_birth[0],
                id = _id,
                anamnesis = self.text_history.toPlainText(),
                sex = self.line_sex.text(),
                exam = self.text_othe_exam.document().toPlainText(),
                result = self.text_result.document().toPlainText(),
                number_unique = number_unique
                )
            self.exit_.emit(True)

            if number_unique != None:
                self.input_number.setText(str(number_unique))
                return "profile_{:05d}".format(number_unique)
                
        else:
            print("no data")
        
    def load_profile(self, _id):
        data= self.profile_data.get_profile_by_number(_id)
        self.line_name.setText(data['first_name'])
        self.line_lastname.setText(data['last_name'])
        day, month, year = data['data_birth'].split(".")
        date = QDate(int(year),int(month),int(day))
        self.input_date_birth.setDate(date)
        self.line_sex.setText(data['sex'])
        self.line_id.setText(data['id'])
        self.input_number.setText(str(data['number_unique']))
        self.text_history.setPlainText(data['anamnesis'])
        self.text_othe_exam.setPlainText(data['exam'])
        self.text_result.setPlainText(data['result'])
        self.change_connect_save(False)

    def clear_data(self):
        self.change_connect_save()
        date = QDate(2000,1,1)
        self.input_date_birth.setDate(date)
        self.line_sex.clear()
        self.line_name.clear()
        self.line_lastname.clear()
        self.line_id.clear()
        self.input_number.clear()
        self.text_history.clear()
        self.text_result.clear()
        self.text_othe_exam.clear()

    def modify_profile(self):
        first_name = self.line_name.text(), 
        last_name  = self.line_lastname.text(),
        data_birth= self.input_date_birth.date().toString("dd.MM.yyyy"),
        _id = self.line_id.text()
            
        if first_name and last_name and data_birth and _id:
            number_unique = self.input_number.text()
            self.profile_data.update_profile(
                first_name = first_name[0], 
                last_name  = last_name[0],
                data_birth= data_birth[0],
                id = _id,
                anamnesis = self.text_history.toPlainText(),
                sex = self.line_sex.text(),
                exam = self.text_othe_exam.document().toPlainText(),
                result = self.text_result.document().toPlainText(),
                number_unique = number_unique
                )
            self.exit_.emit(True)


class UiWinPrincipal(QWidget, Ui_win_principal):
    signal_profile = Signal(str)
    signal_test_new = Signal(list)
    
    def __init__(self, parent=None):
        super(UiWinPrincipal, self).__init__(parent)
        self.setupUi(self)
        self._menu_order()
        self._btn_icons()
        self._btn_configure()
        self.populate_list_profile()
        self.btn_edit_profile.clicked.connect(self.emit_profile)
    
    def _btn_icons(self):
        self.icon_profile = QPixmap(context.get_resource("icons/png/icon_user.png"))
        self.icon_tug = QPixmap(context.get_resource("icons/png/icon_tug.png"))
        self.icon_sot = QPixmap(context.get_resource("icons/png/icon_sot.png"))
        self.icon_vng = QPixmap(context.get_resource("icons/png/icon_vng.png"))
        
    def _btn_configure(self):
        set_button_icon(self.btn_open_file, 'ph.folder-open', size=30, tool_tip="Abrir archivo")
        set_button_icon(self.btn_order, 'ph.list')
        set_button_icon(self.btn_new_user, 'ph.user-plus',size=30, tool_tip="Nuevo usuario")
        set_button_icon(self.btn_filter, 'ph.funnel')
        self._btn_test(self.btn_sot, self.icon_sot)
        self._btn_test(self.btn_tug, self.icon_tug)
        self._btn_test(self.btn_vng, self.icon_vng)
    
    def _btn_test(self, btn, icon):
        btn.hide()
        btn.setStyleSheet("icon-size:50px")
        btn.setIcon(QIcon(icon))
        btn.clicked.connect(self.emit_test)

    def _menu_order(self):
        m_order = QMenu()
        m_order.addAction("Ascendente", lambda: self.order())
        m_order.addAction("Descendente", lambda: self.order(False))
        self.btn_order.setMenu(m_order)
        self.btn_order.menu()
    
    def order(self, asc=True):
        if asc:
            self.list_user.sortItems(0,Qt.AscendingOrder)
        else:
            self.list_user.sortItems(0,Qt.DescendingOrder)
    
    def populate_list_profile(self):
        list_user = ListProfiles().get_list_profile_full()
        icon = QIcon(self.icon_profile)

        list_= []
        for i in list_user:
            dict_ = {"icon": icon, "name": f"{i['first_name']} {i['last_name']}", 
                     "number_unique": i['number_unique']}
            list_.append(dict_)
        self.populate_list(self.list_user, list_)
            

    def populate_list(self, wlist, list_):
        for i in list_:
            item = QTreeWidgetItem(wlist)
            item.setIcon(0, i['icon'])
            item.setText(0, i['name'])
            item.setData(0, Qt.UserRole, i['number_unique'])
        wlist.resizeColumnToContents(0)
        wlist.clicked.connect(self.handler_list)
        #wlist.itemDoubleClicked.connect(self.handler_edit_profile)
        self.data_list =[]
        for i in range(wlist.topLevelItemCount()):
            number_profile = wlist.topLevelItem(i).data(0, Qt.UserRole)
            data= ProfileData().get_profile_by_number(f"profile_{number_profile:05d}")
            self.data_list.append(data)

    def get_list(self):
        return self.data_list
    
    def search_in_list(self, data:str):
        _, number_user = data.split('#')
        number_user = f"profile_{int(number_user):05d}"
        self.inf_profile_complete(number_user)
        
    def handler_list(self, item):
        number_user = self.sender().currentItem().data(0, Qt.UserRole)
        number_user = f"profile_{number_user:05d}"
        name = item.data()
        self.inf_profile_complete(number_user)
           
    def inf_profile_complete(self, profile):
        self.current_profile = profile
        data= ProfileData().get_profile_by_number(profile)

        self.lbl_logo_selected.setPixmap(self.icon_profile)
        name = f"{data['first_name']} {data['last_name']}"
        set_button_icon(self.btn_edit_profile, 'ph.pencil',size=20, tool_tip="Editar usuario")
        self.btn_edit_profile.setEnabled(True)
        age = cal_age(data['data_birth'])
        self.lbl_name.setText(name)
        name = f"""
                <html><head/><body><p align="center">
                <span style=" font-weight:600;">
                Sexo : {data['sex']}
                </span>
                </p><p>
                <span style=" font-weight:600;">
                Edad :{age}
                </span>
                </p><p>
                <span style=" font-weight:600;">
                Fecha de Nacimiento: {data['data_birth']}
                </span>
                </p><p>
                <span style=" font-weight:600;">
                Última Atención:
                </span></p></body></html>
                """
        self.lbl_info_profile.setText(name)
        
        self.btn_sot.setVisible(True)
        self.btn_tug.setVisible(True)
        self.btn_vng.setVisible(True)
    
    def emit_profile(self):
        self.signal_profile.emit(self.current_profile)
    
    def emit_test(self):
        _, test = self.sender().objectName().split("_")
        self.signal_test_new.emit([self.current_profile,test])
    
    

class UiSearchBar(QWidget, Ui_search_bar):
    data_signal = Signal(str)
    def __init__(self, values):
        super().__init__()
        val = self.setup_list(values)
        self.setupUi(self)
        logo = QPixmap(context.get_resource("img/logo_w_name.png"))
        #logo = logo.scaledToHeight(50, Qt.SmoothTransformation)
        self.label.setText("")
        self.label.setPixmap(logo)
        self._btn_configure()
        self.line_search = AutoCompleteEdit(val, placehold = "Buscar Usuario")
        self.line_search.data_signal.connect(self.selection)
        self.verticalLayout_2.addWidget(self.line_search)

    def selection(self, data):
        self.data_signal.emit(data)

    def setup_list(self, values):
        data = []
        for i in values:
            name = f"{i['first_name']} {i['last_name']} - {i['id']} - #{i['number_unique']}"
            data.append(name)
        return data
    
    def _btn_configure(self):
        set_button_icon(self.btn_config, 'ph.gear', tool_tip="Configuración")
