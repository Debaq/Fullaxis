from PySide6.QtWidgets import QWidget
from PySide6.QtCore import Signal
from lib.CustomWidgets import PupilWidget
from UI.Ui_vng_ui import Ui_video
from lib.video.config_video import ConfigVideoWindow
import pyqtgraph as pg
import numpy as np
from lib.Ui_constructors import set_button_icon

class WidgetVNG(QWidget, Ui_video):
    """
    Custom widget for Video Nystagmography (VNG) visualization and interaction.
    
    Attributes:
        config_open (Signal): Signal emitted when the video configuration is opened.
    """
    config_open = Signal(bool)

    def __init__(self):
        """
        Initialize the WidgetVNG instance and set up the UI.
        """
        super().__init__()
        self.setupUi(self)
        self.init_ui()

    def init_ui(self):
        """
        Set up the initial user interface elements for the widget.
        """
        self.video_frame = PupilWidget()
        self.verticalLayout_2.addWidget(self.video_frame)
        graph = self.graph_cond("vng")
        self.horizontalLayout_3.addWidget(graph)
        set_button_icon(self.pushButton_configvideo, 'ph.gear', tool_tip="Configuración")

        self.pushButton_configvideo.clicked.connect(self.open_config_video)


    def open_config_video(self):
        """
        Emit a signal indicating that the video configuration should be opened.
        """
        self.config_open.emit(True)

    def update(self, image):
        """
        Update the displayed image in the widget.
        
        Args:
            image: The image to be displayed.
        """
        self.video_frame.update_image(image)

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

