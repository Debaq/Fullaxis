# pylint: disable=E0611
import pyqtgraph as pg
from lib.CustomWidgets import PupilWidget
from lib.Ui_constructors import set_button_icon
from lib.video.config_video import ConfigVideoWindow
from PySide6.QtCore import QEvent, Signal
from PySide6.QtWidgets import QWidget, QLabel, QApplication
from PySide6.QtCore import Qt, QEvent
from UI.Ui_vng_ui import Ui_video
from lib.video.FullScreenVideo import VideoPopup
from lib.Qtcronometer import Cronometro
from lib.video.ListCameras import CameraId




class WidgetVNG(QWidget, Ui_video):
    """
    Custom widget for Video Nystagmography (VNG) visualization and interaction.
    
    Attributes:
        config_open (Signal): Signal emitted when the video configuration is opened.
    """
    sig_config_open = Signal(bool)
    sig_camera_id = Signal(int)
    def __init__(self):
        """
        Initialize the WidgetVNG instance and set up the UI.
        """
        super().__init__()
        self.setupUi(self)
        self.init_ui()
        self.installEventFilters(self)
        self.fullscreen_window_open = False
        self.fullscreen_window = VideoPopup()
        
        self.cronometro = Cronometro()
        self.cronometro.tiempo_actualizado.connect(self.on_tiempo_actualizado)
        self.video_frame.setFocus()
        self.current_cam = None
        self.cb_hardware.currentIndexChanged.connect(self.change_cam)
        self.hardware_fill()


    def installEventFilters(self, parent):
        for child in parent.children():
            child.installEventFilter(self)
            self.installEventFilters(child)  # Recursividad para todos los hijos

    def eventFilter(self, obj, event):
        # Filtra el evento para detectar doble clics del mouse
        if event.type() == QEvent.MouseButtonDblClick and isinstance(obj, QLabel):
            # Imprime el objectName del QLabel al que se le hizo doble clic
            if not self.fullscreen_window_open:  # Verificar si ya hay una ventana emergente abierta
                self.open_fullscreen_window()
        return super().eventFilter(obj, event)
    
    def open_fullscreen_window(self):
        
        self.fullscreen_window_open = True  # Marcamos que la ventana emergente está abierta
        #self.fullscreen_window.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        screens = QApplication.screens()
        current_screen = QApplication.screenAt(self.geometry().center())

        for screen in screens:
            if screen != current_screen:
                # Si encontramos una pantalla que no es la pantalla actual, movemos la ventana emergente a esa pantalla
                screen_geometry = screen.geometry()
                self.fullscreen_window.move(screen_geometry.x(), screen_geometry.y())
                break

        self.fullscreen_window.closed.connect(self.reset_fullscreen_window_open)  # Conectar una función para resetear la variable cuando la ventana se destruye
        self.fullscreen_window.showFullScreen()

    def reset_fullscreen_window_open(self):
        # Función para resetear la variable fullscreen_window_open cuando la ventana emergente se destruye
        self.fullscreen_window_open = False
        
    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Space:
            if self.cronometro.is_paused:
                self.cronometro.start()
            else:
                self.cronometro.pause()
        elif event.key() == Qt.Key_Escape:
            self.cronometro.reset()
                
    def on_tiempo_actualizado(self, tiempo, show_dot, state):
        dot = ' .' if show_dot else ' '
        self.time_text = f"{state} : {tiempo} s{dot}"
        print(self.time_text)

    def init_ui(self):
        """
        Set up the initial user interface elements for the widget.
        """
        self.video_frame = PupilWidget()
        self.verticalLayout_2.addWidget(self.video_frame)
        graph = self.graph_cond("vng")
        self.horizontalLayout_3.addWidget(graph)
        set_button_icon(self.btn_configvideo, 'ph.gear', tool_tip="Configuración")

        self.btn_configvideo.clicked.connect(self.open_config_video)


    def open_config_video(self):
        """
        Emit a signal indicating that the video configuration should be opened.
        """
        self.sig_config_open.emit(True)

    def update(self, image):
        """
        Update the displayed image in the widget.
        
        Args:
            image: The image to be displayed.
        """
        self.video_frame.update_image(image)
        
        if self.fullscreen_window_open:
            self.fullscreen_window.update_video(image)
        

    def graph_cond(self, name:str) -> pg.PlotWidget:
        """
        Create and configure a PlotWidget for graph visualization.
        
        Args:
            name (str): Name of the graph.
            
        Returns:
            pg.PlotWidget: Configured plot widget.
        """
        plot_widget = pg.PlotWidget(name=name)
        plot_widget.setBackground('w')
        plot_widget.setYRange(-30, 30)
        plot_widget.setXRange(0,120)
        plot_widget.showGrid(x=True, y=True)
        #pw.setFixedSize(400,400)
        #pw.setAspectLocked(lock=True, ratio=1)
        plot_widget.setLabel('left', "", units='degrees')
        plot_widget.setLabel('bottom', 'Time', units='seconds')
        plot_widget.setLimits(xMin=-45, xMax=45, yMin=-45, yMax=45)
        return plot_widget
    
    def hardware_fill(self):
        cameras = CameraId()
        for i in cameras.get_cameras_list():
            if i[0] != 'None':
                self.cb_hardware.addItem(i[0])

    def change_cam(self):
        self.sig_camera_id.emit(self.cb_hardware.currentIndex())