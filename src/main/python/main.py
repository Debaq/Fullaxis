
__VERSION__ = '1.0.0'
import sys
import time

from PySide6.QtCore import QSize, Qt, QPoint 
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import (QFrame, QHBoxLayout, QMainWindow, QPushButton,
                               QTabBar, QSplashScreen)

from base import context
from lib.profile_data import ProfileData
from lib.Ui_constructors import (UiFormBasic, UiNewProfile, UiSearchBar,
                                 UiToolBar, UiWinPrincipal)
from lib.ui_helper import Helpers
from UI.main2 import Ui_MainWindow
from lib.graph.tug_graph import WidgetTUG, WidgetSOT, WidgetVNG


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        self.resize(1200,650)
        self.window_buttons()
        self.wd_bar_search = UiSearchBar()
        self.wd_principal = UiWinPrincipal()
        self.wd_newprofile = UiNewProfile()
        self.wd_toolbar = UiToolBar()
        self.create_central_layers()
        self._populate_layer_principal()
        self.wd_principal.signal_profile.connect(self.handler_edit_profile)
        self.wd_principal.signal_test_new.connect(self.new_test)
        self.btn_configure()
        self.profile_data = ProfileData()
        self.test_list = {"TUG":WidgetTUG(), "SOT":WidgetSOT(), "VNG":WidgetVNG()}
        self.tabWidget.tabCloseRequested.connect(self.tabWidget.removeTab)
        self.states_tabs={}
        self.icons_test = {"TUG":QPixmap(context.get_resource("icons/png/icon_tug.png")),
                           "SOT":QPixmap(context.get_resource("icons/png/icon_sot.png")),
                           "VNG":QPixmap(context.get_resource("icons/png/icon_vng.png"))}
        
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

    def _populate_layer_test(self):
        self.layout_menu.addWidget(self.wd_toolbar)
    
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
        
    def create_new_tab(self, name, icon):
        name_user = self.profile_data.get_profile_by_number(name[0])
        name_user = f"{name_user['first_name']} {name_user['last_name']}"
        test_name = name[1].upper()
        frame = self.tab_basic()
        name_tab = f"{test_name} - {name_user}"
        frame.horizontalLayout_2.addWidget(self.test_list[test_name])
        self.tabWidget.addTab(frame, icon, name_tab)
        count= self.tabWidget.count()     
        self.tabWidget.setCurrentIndex(count-1)
        self.tabWidget.setTabsClosable(True)
        self.tabWidget.tabBar().setTabButton(0, QTabBar.RightSide,None)
        
        
        print(self.tabWidget.currentIndex())
        
    def data_memory(self, n_profile, test):
        return {"profile":n_profile, "test": test, "data":list, "state": "unsave"}
        
    def tab_basic(self):
        return UiFormBasic()

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
            self.wd_principal.inf_profile_complete(self.current_profile)
    
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
    progress()
    window = MainWindow()
    window.show()
    splash.finish(window)
    exit_code = context.app.exec()
    sys.exit(exit_code)
