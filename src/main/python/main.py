
"""
Module for managing the main window of the application.
Version: 1.0.0
"""

__VERSION__ = '1.0.0'
import sys

from dataclasses import dataclass

from base import context
from lib.graph.sot_graph import WidgetSOT
from lib.graph.tug_graph import WidgetTUG
from lib.graph.video_graph import WidgetVNG
from lib.Ui_constructors import UiWinPrincipal
from lib.ui_helper import Helpers, TabsHelper
from lib.video.opencamera_test import VideoThread
from lib.window_helpers import check_screen_resolution

# pylint: disable=E0611
from PySide6.QtCore import Qt, QTimer, Slot
from PySide6.QtGui import QImage, QPixmap
from PySide6.QtWidgets import (QApplication, QMainWindow, QSplashScreen, QWidget)
# pylint: enable=E0611

from UI.Ui_Main import Ui_MainWindow


@dataclass
class VideoData:
    """
    Represents the data associated with a video.

    Attributes:
        enabled (bool): Indicates if the video is enabled or not. Default is False.
        thread (any): Holds the thread associated with the video. Default is None.
        image (QImage): Represents the image data from the video. Default is an empty QImage.
    """
    enabled: bool = False
    thread: any = None
    image: any = QImage

@dataclass
class SerialData:
    """
    Represents the data associated with a serial connection.

    Attributes:
        enabled (bool): Indicates if the serial connection is enabled or not. Default is False.
    """
    enabled: bool = False

@dataclass
class Test:
    """
    Represents a test with its associated data.

    Attributes:
        widget (QWidget): The widget associated with the test. Default is None.
        type (str): The type of the test. Default is None.
        save (bool): Indicates if the test data should be saved or not. Default is False.
        profile (str): The profile associated with the test. Default is None.
        data (dict): A dictionary holding the data of the test. Default is None.
        enabled (bool): Indicates if the test is enabled or not. Default is True.
    """
    widget: QWidget = None
    type: str = None
    save : bool = False
    profile: str = None
    data: dict = None
    enabled: bool = True

class MainWindow(QMainWindow, Ui_MainWindow):
    """
    Main window class for the application.
    Handles the creation and management of video and serial interfaces.
    """
    def __init__(self):
        """Initialize the main window with default settings."""
        super().__init__()
        self.setup_window()
        self.video = VideoData()
        self.serial = SerialData()
        self.tests_actives = {"active": None}
        self.tab_widgets_list = []
        self.main_()

    def setup_window(self):
        """setup window"""
        self.setupUi(self)
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        self.resize(1280, 720)
        self.wd_principal = UiWinPrincipal()
        self.helpers = Helpers()
        self.helpers_tab = TabsHelper(self.tabs_layout, self.tabs_widget)
        self.create_menu_new_tab()
        self.conf_buttons_main()

    def create_menu_new_tab(self) :
        """Create a new tab menu with test options."""
        test = ["TUG", "SOT", "VNG"]
        self.menu_test=self.helpers.menu(self.btn_menu, self.new_tab, test)
        self.btn_new.clicked.connect(lambda: self.menu_test.exec(
            self.btn_new.mapToGlobal(self.btn_new.rect().bottomLeft())
            ))
        
    def conf_buttons_main(self):
        """Configure main buttons for the window."""
        self.btn_menu.clicked.connect(self.main_)

    def new_tab(self):
        """Create a new tab based on the selected test."""
        name_tab = self.sender().text()
        tab = self.helpers_tab.create_tab(name_tab, self.selected_test, self.close_and_save)
        self.create_tab_test(tab)

    def create_tab_test(self, name_tab):
        """Create a specific test tab based on the given name."""
        # Mapping of tab names to their respective widgets and activation functions
        tab_mapping = {
            "TUG": (WidgetTUG, self.activate_serial),
            "SOT": (WidgetSOT, self.activate_serial),
            "VNG": (WidgetVNG, self.activate_video)
        }

        info_tab = self.helpers_tab.type_tab(name_tab)
        widget_class, activation_function = tab_mapping.get(info_tab[0], (None, None))

        if widget_class:
            test = widget_class()
            activation_function()

            # Create a dictionary entry for the tab 
            self.tests_actives[info_tab[1]] = Test(widget=test, type=info_tab[0], save=False, profile=None, data=None, enabled=True)
            self.tests_actives["active"] = info_tab[1]
            self.update_layout_central()


    def update_layout_central(self):
        """Update the central layout based on the active test."""
        active = self.tests_actives["active"]
        Helpers.reset_layout(self, self.layout_central)

        if active:
            self.layout_central.addWidget(self.tests_actives[active].widget)
        else:
            self.main_()

    def selected_test(self, name_tab_test):
        """Set the selected test as active and update the layout."""
        self.tests_actives["active"] = name_tab_test
        self.update_layout_central()

    def main_(self):
        """Reset the layout to the main window."""
        Helpers.reset_layout(self, self.layout_central)
        self.layout_central.addWidget(self.wd_principal)
        self.tests_actives["active"] = None

    def close_and_save(self, n_tab:int):
        """
        Check for unsaved content when closing a test.
        If there's unsaved content, prompt to save.

        Args:
            n_tab (int): Tab number being checked.
        """

        is_sot = self.tests_actives[n_tab].type == "SOT"
        active = self.tests_actives["active"]
        #print(f"save: {self.tests_actives[]}")

        # Si el test activo es el que se está cerrando
        if active == n_tab:
            # Crea una lista con los nombres de los tests que no están cerrados

            open_tests = [test for test, value in self.tests_actives.items() if test != "active" and value.enabled]


            # Si n_tab no está en open_tests, simplemente regresa
            if n_tab not in open_tests:
                return

            idx_d = open_tests.index(n_tab)
            # Si el test que se está cerrando no es el último de la lista,
            # el nuevo test activo será el siguiente. Si es el último,
            # el nuevo test activo será el anterior.
            new_active = open_tests[(idx_d + 1) % len(open_tests)]
            self.tests_actives["active"] = new_active
            self.update_layout_central()
            self.helpers_tab.select_tab(new_active)

        # Si el test que se está cerrando es un SOT, marca como cerrado.
        # Si no es un SOT, elimina del diccionario.
        if is_sot:
            self.tests_actives[n_tab].enabled = False
        else:
            self.tests_actives.pop(n_tab)

        # Si no hay ningún test de video activo, desactiva el video
        if not any(value[1] == 'VNG' for _, value in self.tests_actives.items()):
            self.deactivate_video()

        # Si no hay tests abiertos, vuelve a la vista principal
        if not any(value[5] for _, value in self.tests_actives.items() if _ != "active"):
            self.main_()



    def activate_serial(self):
        """Activate the serial interface."""
        if self.serial.enabled:
            print("Activating serial")
            self.serial.enabled = True

    def deactivate_serial(self):
        """Deactivate the serial interface."""
        print("Deactivating serial")
        self.serial.enabled = False

    def activate_video(self):
        """Activate the video interface."""
        if not self.video.enabled:
            try:
                self.video.thread = VideoThread()
                self.video.thread.start()
                self.video.thread.change_pixmap_signal.connect(self.update_image)
                self.video.enabled = True
            except Exception as exeption:
                print(f"Error activating video: {exeption}")

    def deactivate_video(self):
        """Deactivate the video interface."""
        print("Deactivating video")
        if self.video.enabled:
            try:
                self.video.thread.change_pixmap_signal.disconnect(self.update_image)
                self.video.thread.stop()
                self.video.enabled = False
            except Exception as exeption:
                print(f"Error deactivating video: {exeption}")


    @Slot(QImage)
    def update_image(self, image: QImage) -> None:
        """
        Update the displayed image.

        Args:
            image (QImage): The new image to display.
        """
        self.video.image = image
        for test, val in self.tests_actives.items():
            if test != "active" and val.widget.objectName() == "video":
                val.widget.update(image)


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
        """show splash"""
        splash.close()
        window.show()

    QTimer.singleShot(500, show_main_window)

    def exit_func():
        """acciones al salir"""
        print("saliendo")


    app.aboutToQuit.connect(exit_func)
    exit_code = context.app.exec()

    sys.exit(exit_code)
