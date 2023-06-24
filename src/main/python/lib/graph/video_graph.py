from PySide6.QtWidgets import QWidget
from PySide6.QtCore import Signal
from lib.CustomWidgets import PupilWidget
from UI.Ui_vng_ui import Ui_video
from lib.video.config_video import ConfigVideoWindow
import pyqtgraph as pg
import numpy as np

class WidgetVNG(QWidget, Ui_video):
    config_open = Signal(bool)

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUI()
        
    def initUI(self):
        self.label = PupilWidget()
        self.verticalLayout_2.addWidget(self.label)
        graph = self.graph_cond("vng")
        self.horizontalLayout_3.addWidget(graph)
        self.pushButton_configvideo.clicked.connect(self.open_config_video)
    
    def open_config_video(self):
        self.config_open.emit(True)
        
    def update(self, image):
        self.label.update_image(image)
        
    def graph_cond(self, name:str) -> pg.PlotWidget:
        pw = pg.PlotWidget(name=name)
        pw.setBackground('w')
        pw.setYRange(-30, 30)
        pw.setXRange(0,120)
        pw.showGrid(x=True, y=True)
        #pw.setFixedSize(400,400)
        #pw.setAspectLocked(lock=True, ratio=1)
        pw.setLabel('left', "", units='degrees')
        pw.setLabel('bottom', 'Time', units='seconds')
        pw.setLimits(xMin=-45, xMax=45, yMin=-45, yMax=45)
        return pw
