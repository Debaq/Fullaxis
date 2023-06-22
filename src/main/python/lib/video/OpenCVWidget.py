import time
import pyqtgraph as pg
from PySide6.QtCore import QTimer
from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QDoubleSpinBox, QHBoxLayout
from PySide6.QtGui import QPixmap
from lib.video.OpenCVProcessingThread import OpenCVProcessingThread

class OpenCVWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.init_ui()

        self._thread = OpenCVProcessingThread()
        self._thread.processed_image.connect(self.update_image)
        self._thread.start()

        # Inicializar el temporizador para actualizar el gráfico
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_graph)
        self.timer.start(100)  # Actualizar cada 100 ms

        # Listas para almacenar los datos del gráfico
        self.time_data = []
        self.movements_data = []



    def init_ui(self):
        self._layout = QVBoxLayout(self)

        self._image_label = QLabel(self)
        self._layout.addWidget(self._image_label)

        self._controls_layout = QHBoxLayout()

      
        self._contrast_spinbox_od = QDoubleSpinBox(self)
        self._contrast_spinbox_od.setObjectName("OD")
        self._contrast_spinbox_od.setRange(0.1, 10.0)
        self._contrast_spinbox_od.setSingleStep(0.1)
        self._contrast_spinbox_od.setValue(1.0)
        self._contrast_spinbox_od.valueChanged.connect(self.on_contrast_changed)
        self._controls_layout.addWidget(self._contrast_spinbox_od)
        self._controls_layout.addWidget(QLabel("C-OD"))

        self._contrast_spinbox_oi = QDoubleSpinBox(self)
        self._contrast_spinbox_oi.setObjectName("OI")
        self._contrast_spinbox_oi.setRange(0.1, 10.0)
        self._contrast_spinbox_oi.setSingleStep(0.1)
        self._contrast_spinbox_oi.setValue(1.0)
        self._contrast_spinbox_oi.valueChanged.connect(self.on_contrast_changed)
        self._controls_layout.addWidget(self._contrast_spinbox_oi)
        self._controls_layout.addWidget(QLabel("C-OI"))
        
        


        self._layout.addLayout(self._controls_layout)
        
        # Agregar el gráfico de pyqtgraph
        self.graph = pg.PlotWidget()
        self.graph.setTitle("Movimientos en función del tiempo")
        self.graph.setLabel("left", "Movimientos")
        self.graph.setLabel("bottom", "Tiempo", "s")
        self.curve = self.graph.plot(pen="y")
        self._layout.addWidget(self.graph)

        #self._layout.addWidget(self.graph)

    def update_image(self, qt_image):
        pixmap = QPixmap.fromImage(qt_image)
        self._image_label.setPixmap(pixmap)

    # Función para actualizar el gráfico
    def update_graph(self):
        # Obtener datos de tiempo y movimientos desde el hilo (aquí necesitas implementar el mecanismo para obtener estos datos)
        current_time = time.time()
        current_movements = self._thread.get_movements()

        # Agregar datos a las listas
        self.time_data.append(current_time)
        self.movements_data.append(current_movements)

        # Actualizar la curva del gráfico
        #self.curve.setData(self.time_data, self.movements_data)

       
    def on_threshold_changed(self, state):
        self._thread.set_threshold(state)
        
    def on_contrast_changed(self, value):
        wid = self.sender()
        #print(wid.objectName())
        self._thread.set_contrast(value, wid.objectName())
        

    def stop_thread(self):
        self._thread.stop()
        self._thread.wait()
        self._thread.quit()