from PySide6.QtCore import Signal, Slot, Qt, QThread
from PySide6.QtWidgets import QImage, QWidget, QApplication, QLabel, QVBoxLayout, QPushButton, QHBoxLayout
from PySide6.QtGui import QPixmap
import numpy as np
import pyqtgraph as pg 
from procceess_vng import VideoThread as Video
from lib.ui_video_test import Ui_VNG_test
import cv2

class VideoThread(QThread):
    change_pixmap_signal = Signal(tuple)
    
    def __init__(self):
        super().__init__()
        self.video_thread = Video()
    
    def run(self):
        
        cap = self.video_thread.video_open()

        while self._run_flag:
            ret, cv_img, _ = self.video_thread.video_read(cap)
            if ret:
                try:
                    centroid = self.video_thread.centroid_detection(cv_img)
                    data = self.video_thread.detect_pupil(cv_img, centroid)
                    self.change_pixmap_signal.emit(data)
                except Exception:
                    data = (cv_img, None)
                    self.change_pixmap_signal.emit(data)


    def stop(self):
        """Sets run flag to False and waits for thread to finish"""
        self._run_flag = False
        self.wait()

       
class WidgetVNG(QWidget, Ui_VNG_test):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)
        
        self.load_variables()
        self.load_video()
        self.graph_init()
    
    def not_empty_data(self):
        pass
    
    def load_video(self):
        self.video_label = QLabel()
        self.video_label.resize(800,480)
        self.video_layout.addWidget(self.video_label)
        
    @Slot(tuple)
    def update_image(self, data):
        """Updates the image_label with a new opencv image"""
        cv_img = data[0]
        self.isImage = True
        self.btn_calibrate.setEnabled(True)

        qt_img = self.convert_cv_qt(cv_img)
        self.image_label.setPixmap(qt_img)
        if self.calibrate_run:
            if self.calibrate_time > 0:
                self.calibrate_time -= 1
                self.promX.append(data[1][0])
                self.promY.append(data[1][1])
            else:
                self.calibrate_data = (np.mean(self.promX), np.mean(self.promY))
                self.promX = []
                self.promY = []
                self.calibrate_time = 100
                self.btn_start.setEnabled(True)
                self.btn_calibrate.setEnabled(False)
                self.calibrate_run = False

        else:
            self.updateData(data[1])
    
    def convert_cv_qt(self, cv_img):
        """Convert from an opencv image to QPixmap"""
        rgb_image = cv2.cvtColor(cv_img, cv2.COLOR_BGR2RGB)
        h, w, ch = rgb_image.shape
        bytes_per_line = ch * w
        convert_to_Qt_format = QImage(rgb_image.data, w, h, bytes_per_line, QImage.Format_RGB888)
        p = convert_to_Qt_format.scaled(self.display_width, self.display_height, Qt.KeepAspectRatio)
        return QPixmap.fromImage(p)
    
    def graph_init(self):
        self.vertical = self.graph_axis("Vertical")
        self.horizontal = self.graph_axis("Horizontal")
        self.graph_layout.addWidget(self.vertical)
        self.graph_layout.addWidget(self.horizontal)
    
    def graph_axis(self, name):
        pw = pg.PlotWidget(name=name)
        pw.setBackground('w')
        #pw.setYRange(-90, 90)
        pw.setXRange(0, 100)
        pw.showGrid(x=True, y=True)
        pw.setMenuEnabled(False)
        pw.setLabel('left', name, units='degrees')
        pw.setLabel('bottom', 'Time', units='s')
        pw.setLimits(xMin=0)
        return pw
    
    
    def updateData(self, data):
        if self._run_flag:
            if data is not None:
                self.mx.append(data[0] - self.calibrate_data[0])
                self.my.append(data[1] - self.calibrate_data[1])
                    #self.p1.setData(self.mx, self.t)
            else:
                self.mx.append(0)
                self.my.append(0)

            t_last = self.t[-1]
            if t_last > 50:
                resto = t_last - 50
                self.pw.setXRange(0 + resto, 100 + resto)
                self.pw1.setXRange(0 + resto, 100 + resto)

            self.t.append(t_last+1)
            self.p1.setData(self.t, self.mx)
            self.p2.setData(self.t, self.my)
                #self.p1.setData(self.mx, self.t)
    
    def load_variables(self):
        self.mx = [0]
        self.my = [0]
        self.t = [0]
        self.promX = []
        self.promY = []
        self.calibrate_time = 100
        self.calibrate_data = (0, 0)
        self.calibrate_run = False
        self.isImage = False
        self._run_flag = False
                