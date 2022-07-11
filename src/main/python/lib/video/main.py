from fbs_runtime.application_context.PySide6 import ApplicationContext
from PySide6 import QtGui
from PySide6.QtWidgets import QWidget, QApplication, QLabel, QVBoxLayout, QPushButton, QHBoxLayout
from PySide6.QtGui import QPixmap
import sys
import cv2
from PySide6.QtCore import Signal, Slot, Qt, QThread
import numpy as np
import pyqtgraph as pg
from proccess_vng import VideoThread as Video

class VideoThread(QThread):
    change_pixmap_signal = Signal(tuple)

    def __init__(self):
        super().__init__()
        self._run_flag = True
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




class App(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("VNG-Demo")
        self.display_width = 800
        self.display_height = 480
        # create the label that holds the image
        self.image_label = QLabel(self)
        self.image_label.resize(self.display_width, self.display_height)
        # create a text label
        self.textLabel = QLabel('VNG')

        # create a vertical box layout and add the two labels
        vbox = QVBoxLayout()
        vbox.addWidget(self.image_label)
        vbox.addWidget(self.textLabel)
        btn_hbox = QHBoxLayout()
        self.btn_calibrate = QPushButton('Calibrate')
        self.btn_calibrate.setEnabled(False)
        self.btn_start = QPushButton('Start')
        self.btn_start.setEnabled(False)
        self.btn_stop = QPushButton('Stop')
        self.btn_stop.setEnabled(False)
        self.calibrate_time = 100
        self.promX = []
        self.promY = []
        self.btn_calibrate.clicked.connect(self.calibrate)
        self.btn_start.clicked.connect(self.run)
        self.btn_stop.clicked.connect(self.stop)
        self.calibrate_data = (0,0)
        self.calibrate_run = False
        btn_hbox.addWidget(self.btn_calibrate)
        self.isImage = False
        self._run_flag = False
        btn_hbox.addWidget(self.btn_start)
        btn_hbox.addWidget(self.btn_stop)
        vbox.addLayout(btn_hbox)
        self.pw = pg.PlotWidget(name='horizontal')  ## giving the plots names allows us to link their axes together
        self.pw1 = pg.PlotWidget(name='vertical')  ## giving the plots names allows us to link their axes together

        vbox.addWidget(self.pw)  
        vbox.addWidget(self.pw1)

        self.p1 = self.pw.plot()
        self.p1.setPen((200,200,100))
        self.p2 = self.pw1.plot()
        self.p2.setPen((200,200,100))
        self.mx = [0]
        self.my= [0]
        self.t = [0]
        # set the vbox layout as the widgets layout
        self.setLayout(vbox)
        self.pw.setXRange(0, 100)
        self.pw1.setXRange(0, 100)

        # create the video capture thread
        self.thread = VideoThread()
        # connect its signal to the update_image slot
        self.thread.change_pixmap_signal.connect(self.update_image)
        # start the thread
        self.thread.start()

    def calibrate(self):
        if self.isImage:
            self.calibrate_run = True


    def closeEvent(self, event):
        self.thread.stop()
        event.accept()

    def run(self):
        self._action_start_stop(True, False)
    
    def stop(self):
        self._action_start_stop(False, True)

    def _action_start_stop(self, arg0, arg1):
        self._run_flag = arg0
        self.btn_start.setEnabled(arg1)
        self.btn_stop.setEnabled(arg0)


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
        convert_to_Qt_format = QtGui.QImage(rgb_image.data, w, h, bytes_per_line, QtGui.QImage.Format_RGB888)
        p = convert_to_Qt_format.scaled(self.display_width, self.display_height, Qt.KeepAspectRatio)
        return QPixmap.fromImage(p)

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
    
if __name__=="__main__":
    app = QApplication(sys.argv)
    a = App()
    a.show()
    sys.exit(app.exec())
"""
if __name__ == '__main__':
    appctxt = ApplicationContext()       # 1. Instantiate ApplicationContext
    window = QMainWindow()
    window.resize(250, 150)
    window.show()
    exit_code = appctxt.app.exec()      # 2. Invoke appctxt.app.exec()
    sys.exit(exit_code)
"""