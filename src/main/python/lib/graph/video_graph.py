from PySide6.QtWidgets import QWidget
from PySide6.QtCore import Signal
from lib.CustomWidgets import PupilWidget
from UI.vng_ui_ui import Ui_video
from lib.video.config_video import ConfigVideoWindow
import pyqtgraph as pg
import numpy as np
from lib.Ui_constructors import set_button_icon


class WidgetVNG(QWidget, Ui_video):
    config_open = Signal(bool)

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.delta_r = None
        self.delta_l = None
        self.data_hor = []
        self.data_ver = []
        self.x = []
        self.initUI()
        
    def initUI(self):
        self.label = PupilWidget()
        self.verticalLayout_2.addWidget(self.label)
        self.graph = self.graph_cond("vng")
        self.horizontalLayout_3.addWidget(self.graph)
        set_button_icon(self.pushButton_configvideo, 'ph.gear', tool_tip="Configuración")

        self.pushButton_configvideo.clicked.connect(self.open_config_video)
        self.record_state = False
        self.btn_start.clicked.connect(self.record)
        self.graph.plot(self.data_hor, pen=pg.mkPen(color='y', width=2), name='x')
        self.graph.plot(self.data_ver, pen=pg.mkPen(color='g', width=2), name='y')

        
    
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
        pw.disableAutoRange(axis='x')
        #pw.setLimits(xMin=0, xMax=45, yMin=-45, yMax=45)
        return pw
    

    def record(self):
        self.record_state = not self.record_state
        if self.record_state == True:
            self.btn_start.setText("Detener")
        else:
            self.btn_start.setText("Grabar")



    def update_graph(self, coords):
        # Solo actualizar si el estado de grabación está activo
        if self.record_state:
            # Asegúrate de que ambos deltas se calculen en la misma iteración
            if coords['r'] and coords ['l']:
                if self.delta_r is None and coords['r'] or self.delta_l is None and coords['l']:
                    if coords['r']:
                        self.delta_r = coords['r'][0]  # Establece delta para el ojo derecho
                    if coords['l']:
                        self.delta_l = coords['l'][0]  # Establece delta para el ojo izquierdo

            # Si ambos deltas están establecidos, procesar las coordenadas

            if coords['r'] or coords ['l']:
                if self.delta_r is not None and self.delta_l is not None:
                    # Seleccionar el ojo para usar
                    eye_used = 'r' if coords['r'] else 'l'
                    if eye_used == 'r':
                        delta = self.delta_r
                    else:
                        delta = self.delta_l

                    # Convertir a int32 antes de realizar la resta para evitar el desbordamiento de entero
                    value_x = int(coords[eye_used][0]) - int(delta)
                    value_y = coords[eye_used][1]
                    # Añadir el punto a la lista si hay un cambio en x o y
                    #if self.data_hor and (abs(value_x - self.data_hor[-1]) > 1 or abs(value_y - self.data_ver[-1]) > 1):
                    self.data_hor.append(value_x)
                    self.data_ver.append(value_y)
                    self.x.append(self.x[-1] + 1 if self.x else 0)

                    # Graficar los datos relativos
                    self.graficar()
    
    def graficar(self):
        for item in self.graph.listDataItems():
            if item.name() == 'x':
                item.setData(x=self.x, y=self.data_hor)
            if item.name() == 'y':
                item.setData(x=self.x, y=self.data_ver)

        self.graph.autoRange()



        # Graficar los datos
        #self.graph.setData(self.x, self.data) 
            
