
__VERSION__ = '1.0.0'
import sys
import time

from base import context
from lib.graph.sot_graph import WidgetSOT
from lib.graph.tug_graph import WidgetTUG
from lib.graph.video_graph import WidgetVNG
from lib.profile_data import ProfileData
from lib.Ui_constructors import (UiFormBasic, UiNewProfile, UiSearchBar,
                                 UiWinPrincipal)
from lib.ui_helper import Helpers, istest
from PySide6.QtCore import QPoint, Qt
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import (QFrame, QHBoxLayout, QMainWindow, QMessageBox,
                               QPushButton, QSplashScreen, QTabBar)
from UI.main2 import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        #insertar aca una función que revise la resolución de la pantalla y si esta es menor a 720p no se abre la aplicación
        self.resize(1280,720)
        self.window_buttons()
        self.wd_principal = UiWinPrincipal()
        data_list_user = self.wd_principal.get_list()
        self.wd_newprofile = UiNewProfile()
        self.wd_bar_search = UiSearchBar(data_list_user)
        self.wd_bar_search.data_signal.connect(self.wd_principal.search_in_list)
        self.create_central_layers()
        self._populate_layer_principal()
        self.wd_principal.signal_profile.connect(self.handler_edit_profile)
        self.wd_principal.signal_test_new.connect(self.new_test)
        self.btn_configure()
        self.profile_data = ProfileData()
        self.tabWidget.tabCloseRequested.connect(self._is_saved_tab)
        self.tabWidget.currentChanged.connect(self._emit_change_current_tab)
        self.states_tabs=[]
        self.tab_widgets_list = []
        self.prev_tab = 0
        self.icons_test = {"TUG":QPixmap(context.get_resource("icons/png/icon_tug.png")),
                           "SOT":QPixmap(context.get_resource("icons/png/icon_sot.png")),
                           "VNG":QPixmap(context.get_resource("icons/png/icon_vng.png"))}
        
    def _is_saved_tab(self, idx_tab):
        #aca hay que agregar una función que rebise si tiene algun dato la pestaña de otra forma no es necesario guardar
        idx_tab = idx_tab - 1
        tab_data = (self.states_tabs[idx_tab])
        if tab_data["data"] and tab_data["save"] == False:
            self._save_message_box(idx_tab)
        else:
            self._closetab(idx_tab)

    def _save_message_box(self, idx_tab):
        msgBox = QMessageBox()
        msgBox.setText("El documento ha sido modificado.")
        msgBox.setInformativeText("Desea guardar?")
        msgBox.setStandardButtons(QMessageBox.Save | QMessageBox.Discard | QMessageBox.Cancel)
        btn_save = msgBox.button(QMessageBox.Save)
        btn_save.setText("Guardar")
        btn_discard = msgBox.button(QMessageBox.Discard)
        btn_discard.setText("Descartar")
        btn_cancel = msgBox.button(QMessageBox.Cancel)
        btn_cancel.setText("Cancelar")
        msgBox.setDefaultButton(QMessageBox.Save)
        ret = msgBox.exec()
        if ret == QMessageBox.Save:
            self._save_data_tab(idx_tab, True)
        elif ret == QMessageBox.Discard:
            self._closetab(idx_tab)
                    
    def _closetab(self, idx_tab, save=False):
        test = self.tabWidget.tabText(idx_tab+1)
        
        if istest(test, "VNG"):
            self.tab_widgets_list[idx_tab][1].action_end(save=save, name=test)
            
            
        self.tabWidget.removeTab(idx_tab+1)
        self.states_tabs.pop(idx_tab)
        self.tab_widgets_list.pop(idx_tab)
        for idx in range(len(self.tab_widgets_list)):
            self.tab_widgets_list[idx][0].set_number(idx)
            
    def _save_data_tab(self, idx_tab, close = False):
        self.states_tabs[idx_tab]["save"] = True
        if close:
            self._closetab(idx_tab, True)
        
    # action #1
    def mousePressEvent(self, event):
        self.oldPosition = event.globalPosition().toPoint()

	# action #2
    def mouseMoveEvent(self, event):
        delta = QPoint(event.globalPosition().toPoint() - self.oldPosition)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPosition = event.globalPosition().toPoint()
        
    def window_buttons(self):
        self.btn_min = QPushButton("_")
        self.btn_max = QPushButton("□")        
        self.btn_exit = QPushButton("X")
        self.btn_exit.setObjectName(u"btn_exit")
        self.btn_max.setObjectName(u"btn_max")
        self.btn_min.setObjectName(u"btn_min")
        self.btn_exit.setFlat(True)
        self.btn_max.setFlat(True)
        self.btn_min.setFlat(True)
        frame = QFrame()
        frame.setStyleSheet("""
            QPushButton{
                padding:5 5px;
                color:rgb(209,210,214);
                }
            QPushButton#btn_min, QPushButton#btn_max{background-color:rgba(81,83,95,0);}
            QPushButton#btn_min:hover, QPushButton#btn_max:hover{background-color:rgb(81,83,95)}
            QPushButton#btn_exit{background-color: rgba(73, 102,153,0);}
            QPushButton#btn_exit:hover{background-color: rgb(240, 96,77);}
            QPushButton:pressed{
	            background-color: rgb(232,232,232); 
	            color:rgb(95,145,230)
            }
                            """)
        layer = QHBoxLayout(frame)
        layer.setContentsMargins(0,0,0,0)
        layer.addWidget(self.btn_min)
        layer.addWidget(self.btn_max)
        layer.addWidget(self.btn_exit)
        self.tabWidget.setCornerWidget(frame)
        
    def create_central_layers(self):
        frame_menu = QFrame()
        frame_central =QFrame()
        self.main_layout.addWidget(frame_menu)
        self.main_layout.addWidget(frame_central)
        self.layout_menu = QHBoxLayout(frame_menu)
        self.layout_menu.setContentsMargins(0,0,0,0)
        self.layout_central = QHBoxLayout(frame_central)
        self.layout_central.setContentsMargins(0,0,0,0)
        self._populate_layer_principal()
        
    def _populate_layer_principal(self):
        self._clear_layer_principal()
        self.layout_menu.addWidget(self.wd_bar_search)
        self.layout_central.addWidget(self.wd_principal)

    #def _populate_layer_test(self):
    #    self.layout_menu.addWidget(self.wd_toolbar)
    
    def _clear_layer_principal(self):
        self._clear_central()
        Helpers.reset_layout(self, self.layout_menu)
        
    def _clear_central(self):
        Helpers.reset_layout(self, self.layout_central)

    def btn_configure(self):
        self.btn_exit.clicked.connect(self.close)
        self.btn_max.clicked.connect(self._toggle_maxmin)
        self.btn_min.clicked.connect(self.showMinimized)
        self.wd_principal.btn_new_user.clicked.connect(self.win_profile_data)
        
    def create_new_tab(self, profile, icon):
        # Obtiene los datos del perfil del usuario a partir de un número de perfil.
        name_user = self.profile_data.get_profile_by_number(profile[0])
        # Formatea el nombre del usuario.
        name_user = f"{name_user['first_name']} {name_user['last_name']}"
        # Obtiene el nombre de la prueba y lo convierte a mayúsculas.
        test_name = profile[1].upper()
        # Crea un nuevo marco y widget para la prueba.
        frame, widget_test = self.tab_basic(test_name)
        # Crea el nombre de la pestaña.
        name_tab = f"{test_name} - {name_user}"
        # Añade el widget de prueba al layout del marco.
        frame.horizontalLayout_2.addWidget(widget_test)
        # Añade una nueva pestaña al QTabWidget con el marco, el icono y el nombre de la pestaña.
        self.tabWidget.addTab(frame, icon, name_tab)
        # Obtiene el número de pestañas en el QTabWidget.
        count= self.tabWidget.count()     
        # Establece la pestaña actual en el QTabWidget a la última pestaña añadida.
        self.tabWidget.setCurrentIndex(count-1)
        # Habilita el cierre de pestañas en el QTabWidget.
        self.tabWidget.setTabsClosable(True)
        # Deshabilita el botón de cierre en la primera pestaña.
        self.tabWidget.tabBar().setTabButton(0, QTabBar.RightSide,None)
        # Obtiene el índice de la pestaña actual.
        tab_n = self.tabWidget.currentIndex()
        # Crea una lista con los datos del perfil y el índice de la pestaña.
        data =[profile, tab_n]
        # Llama a la función _create_state_tab con los datos de la pestaña.
        self._create_state_tab(data)
    
    def _create_state_tab(self, data):
        n_tab = data[1]-1
        self.tab_widgets_list[n_tab][0].set_number(n_tab)
        self.tab_widgets_list[n_tab][0].set_profile(data[0][0])
        data_dict = {"profile":data[0][0], "test":data[0][1], "save":False, "data":[2]}
        self.states_tabs.append(data_dict)
        
    def data_memory(self, n_profile, test):
        return {"profile":n_profile, "test": test, "data":list, "state": "unsave"}
        
    def tab_basic(self, name_test):
        new_tab_test = UiFormBasic(name_test)
        new_tab_test.state.connect(self.actions_tab)
        if name_test=="TUG":
            widget = WidgetTUG()
        elif name_test == "SOT":
            widget = WidgetSOT() 
        elif name_test == "VNG":
            widget = WidgetVNG()
        set_widget = [new_tab_test, widget]
        self.tab_widgets_list.append(set_widget)
        return self.tab_widgets_list[-1][0],self.tab_widgets_list[-1][1]
        
    def actions_tab(self, signal):
        if signal[0] == 'new':
            test = signal[3].lower()
            self.new_test([signal[4], test])
        if signal[0] == 'save':
            self._save_data_tab(signal[2])

    def win_profile_data(self):
        self._clear_central()
        self.layout_central.addWidget(self.wd_newprofile)
        self.wd_newprofile.exit_.connect(self.return_principal)

    def return_principal (self, event):
        if event:
            self._clear_central()
            self.layout_central.addWidget(self.wd_principal)
            self.wd_principal.list_user.clear()
            self.wd_principal.populate_list_profile()
            self.wd_principal.inf_profile_complete(self.current_profile)#aca hay un problema desconocido dice que no existe current_profile
    
    def _emit_change_current_tab(self, idx_tab):
        new_tab_name = self.tabWidget.tabText(idx_tab)
        prev_tab_name = self.tabWidget.tabText(self.prev_tab)
        print(idx_tab)
        
        if istest(prev_tab_name, "VNG"):
            self.tab_widgets_list[self.prev_tab-1][1].stop_video()
        
        if istest(new_tab_name, "VNG"):
            self.tab_widgets_list[idx_tab-1][1].start_video()
           
        
        self.prev_tab = idx_tab
        
        
    def handler_edit_profile(self, profile):
        self.current_profile = profile
        self.win_profile_data()
        self.wd_newprofile.load_profile(profile)
    
    def new_test(self, data):
        icon = self.icons_test[data[1].upper()]
        self.create_new_tab(data, icon=icon)
  
    def _toggle_maxmin(self):
        if self.isMaximized():
            self.showNormal()
            self.resize(1200,650)
            self.btn_max.setText("□")
        else:
            self.btn_max.setText("▫")
            self.showMaximized()

if __name__ == '__main__':
    def progress():
        for _ in range(5):
            time.sleep(0.1)
    pixmap = QPixmap(context.get_resource("img/splash.png"))
    splash = QSplashScreen(pixmap)
    #splash.showMessage("Hola", Qt.AlignHCenter | Qt.AlignBottom, Qt.white)
    splash.show()
    #progress()
    window = MainWindow()
    window.show()
    splash.finish(window)
    exit_code = context.app.exec()
    sys.exit(exit_code)
