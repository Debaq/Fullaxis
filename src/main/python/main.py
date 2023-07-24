
__VERSION__ = '1.0.0'
import sys
import time

from base import context
from lib.graph.sot_graph import WidgetSOT
from lib.graph.tug_graph import WidgetTUG
from lib.graph.video_graph import WidgetVNG
from lib.profile_data import ProfileData
from lib.Ui_constructors import (UiFormBasic, UiNewProfile, UiSearchBar,
                                 UiWinPrincipal, set_button_icon)
from lib.ui_helper import Helpers, TabsHelper
from lib.video.OpenCVProcessingThread import OpenCVProcessingThread
from lib.window_helpers import check_screen_resolution
from PySide6.QtCore import QPoint, Qt, QTimer, Slot
from PySide6.QtGui import QImage, QPixmap,QAction
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QMainWindow,
                               QMessageBox, QPushButton, QSplashScreen,
                               QTabBar, QWidget, QMenu)
from UI.Ui_Main import Ui_MainWindow
from lib.video.config_video import ConfigVideoWindow
from lib.dialog_helpers import SaveMessageBox
from lib.video.ListCameras import CameraId
from lib.CustomWidgets import TabButton
from lib.video.opencamera_test import VideoThread


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()

        self.setupUi(self)
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        self.resize(1280, 720)
        self.helpers = Helpers()
        self.helpers_tab = TabsHelper(self.tabs_layout, self.tabs_widget)
        self.wd_principal = UiWinPrincipal()
   
        self.create_menu_new_tab()
        self.conf_buttons_main()
        self.tests_actives = {"active":None}
        self.is_video_enabled = False
        self.is_serial_enabled = False
        self.tab_widgets_list = []

        self.main_()
        
    def create_menu_new_tab(self) :
        test = ["TUG", "SOT", "VNG"]
        self.menu_test=self.helpers.menu(self.btn_menu, self.new_tab, test)        
        self.btn_new.clicked.connect(lambda: self.menu_test.exec_(
            self.btn_new.mapToGlobal(self.btn_new.rect().bottomLeft())
            ))

    def conf_buttons_main(self):
        self.btn_menu.clicked.connect(self.main_)

    def new_tab(self):
        name_tab = self.sender().text()
        tab = self.helpers_tab.create_tab(name_tab, self.selected_test, self.close_and_save)
        self.create_tab_test(tab)
    
    def create_tab_test(self, name_tab):
        info_tab = self.helpers_tab.type_tab(name_tab)
        if info_tab[0] == "TUG":
            test = WidgetTUG()
            self.activate_serial()
        elif info_tab[0] == "SOT":
            test = WidgetSOT()
            self.activate_serial()
        elif info_tab[0] == "VNG":
            test = WidgetVNG()
            self.activate_video()
            
        # TODO: se crea un diccionario que contenga {"nombretab":[widget, tipo, guardado, profile, data,enabled(bool)]}
        self.tests_actives[info_tab[1]] = [test,info_tab[0],False,None,None,True]
        self.tests_actives["active"] = info_tab[1]
        self.update_layout_central()
        
    def update_layout_central(self):
        active = self.tests_actives["active"]
        Helpers.reset_layout(self, self.layout_central)
        if active is not None:
            self.layout_central.addWidget(self.tests_actives[active][0])
        if active is None:
            self.main_()
    
    def selected_test(self, d):
        self.tests_actives["active"] = d
        self.update_layout_central()

    def main_(self):
        Helpers.reset_layout(self, self.layout_central)
        self.layout_central.addWidget(self.wd_principal)
        self.tests_actives["active"] = None
        

    def close_and_save(self, d):
        is_SOT = self.tests_actives[d][1] == "SOT"
        active = self.tests_actives["active"]

        # Si el test activo es el que se está cerrando
        if active == d:
            # Crea una lista con los nombres de los tests que no están cerrados
            open_tests = [test for test in self.tests_actives if test != "active" and self.tests_actives[test][5]]
            # Encuentra el índice del test que se está cerrando en la lista de tests abiertos
            idx_d = open_tests.index(d)

            # Si el test que se está cerrando no es el último de la lista, el nuevo test activo será el siguiente
            # Si es el último, el nuevo test activo será el anterior
            new_active = open_tests[idx_d+1] if idx_d < len(open_tests)-1 else open_tests[idx_d-1]

            # Actualiza el test activo y la interfaz de usuario
            self.tests_actives["active"] = new_active
            self.update_layout_central()
            self.helpers_tab.select_tab(new_active)

        # Si el test que se está cerrando es un SOT, marca como cerrado
        # Si no es un SOT, elimina del diccionario
        if is_SOT:
            self.tests_actives[d][5] = False
        else:
            self.tests_actives.pop(d)


        if any(self.tests_actives[test][0] == 'video' for test in self.tests_actives):
            print("existe un video")
        else:
            self.deactivate_video()
        
        # Comprueba si quedan tests abiertos
        if any(self.tests_actives[test][5] for test in self.tests_actives if test != "active"):
            return 0
        else:
            self.main_()

    def activate_serial(self):
        if self.is_serial_enabled:
            print("Activating serial")
            self.is_serial_enabled = True
            
    def deactivate_serial(self):
        print("Deactivating serial")
        self.is_serial_enabled = False
        
    def activate_video(self):
        if not self.is_video_enabled:
            try:
                self.thread.start()
            except:
                self.thread_video = VideoThread()
                self.thread_video.start()
                print("Activating video")
                self.thread_video.change_pixmap_signal.connect(self.update_image)
            
            self.is_video_enabled = True
    def deactivate_video(self):
        print("Deactivating video")
        if self.is_serial_enabled:
            try:
                self.thread_video.stop()
            except:
                self.thread_video = VideoThread()
                self.thread_video.stop()
            self.is_video_enabled = False
            

    @Slot(QImage)
    def update_image(self, image):
        self.image_video = image
        for i in self.tests_actives:
            if i != "active":
               if self.tests_actives[i][0].objectName() == "video": 
                   self.tests_actives[i][0].update(image)
            


if __name__ == '__main__':
    app = QApplication.instance()
    if app is None:
        app = QApplication(sys.argv)

    if not check_screen_resolution(app):
        sys.exyt()

    splash = QSplashScreen(QPixmap(context.get_resource("img/splash_sp.png")))
    splash.show()

    window = MainWindow()

    def show_main_window():
        splash.close()
        window.show()

    QTimer.singleShot(500, show_main_window)
    exit_code = context.app.exec()
    sys.exit(exit_code)
