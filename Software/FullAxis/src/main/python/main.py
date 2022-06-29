
__VERSION__ = '1.0.0'
from fileinput import close
import sys

from PySide6.QtWidgets import QMainWindow, QWidget, QPushButton, QTabBar, QPushButton
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt, QSize
from base import context
from UI.Ui_main import Ui_MainWindow
from UI.Ui_search_bar import Ui_search_bar
from UI.Ui_windows_principal import Ui_win_principal


class UiWinPrincipal(QWidget, Ui_win_principal):
    def __init__(self, parent=None):
        super(UiWinPrincipal, self).__init__(parent)
        self.setupUi(self)

        


class UiSearchBar(QWidget, Ui_search_bar):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        logo = QPixmap(context.get_resource("img/logo_w_name.png"))
        #logo = logo.scaledToHeight(50, Qt.SmoothTransformation)
        self.label.setText("")
        self.label.setPixmap(logo)

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        self.bar_search = UiSearchBar()
        self.win_principal = UiWinPrincipal()
        self.layout_menu.addWidget(self.bar_search)
        self.layout_central.addWidget(self.win_principal)
        self.btn_exit.clicked.connect(self.close)
        self.btn_min.clicked.connect(self._toggle_maxmin)
        self.btn_new.clicked.connect(self._move_new_tab)
        
    def _move_new_tab(self):
        self.sender().deleteLater()
        self.create_new_tab()
        btn = QPushButton("+")
        btn.clicked.connect(self._move_new_tab)
        self.layotu_btn_tabs.addWidget(btn)
        
    def create_new_tab(self):
        if "tb" not in dir(self):
            self.tb = QTabBar(self)
        self.tb.addTab("nueva prueba")
        self.tb.currentChanged.connect(self.tab_changed)
        self.tb.tabCloseRequested.connect(self.tab_close)
        self.tb.setTabsClosable(True)
        self.tb.setDocumentMode(True)
        self.layotu_btn_tabs.addWidget(self.tb)

    def tab_changed(self, index):
        print(index)

    def tab_close(self, index):
        print(index)
        
    def _toggle_maxmin(self):
        if self.isMaximized():
            self.showNormal()
            self.resize(800,600)
        else:
            self.showMaximized()

    def new_tab(self):
        btn = QPushButton


if __name__ == '__main__':
    #app = QApplication([])
    window = MainWindow()
    window.show()
    exit_code = context.app.exec()
    sys.exit(exit_code)
