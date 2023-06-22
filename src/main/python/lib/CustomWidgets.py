from lib.video.OpenCVProcessingThread import OpenCVProcessingThread
from PySide6 import QtCore
from PySide6.QtGui import QImage, QPixmap
from PySide6.QtWidgets import QLabel


class PupilWidget(QLabel):
    def __init__(self):
        super().__init__()
        self.start_thread()

    def start_thread(self):
        self.thread_ = OpenCVProcessingThread()
        self.thread_.change_pixmap_signal.connect(self.update_image)
        self.thread_.signal_frame_states.connect(self.states_video)
        self.thread_.start()
        self.stop = False


        
    def stop_thread(self, save, name):
        self.thread_.stop(save, name)
        self.thread_.quit()
    
    def stop_video(self):
        self.thread_.close_cap()

    def start_video(self):
        print(self.stop)
        if self.stop:
            self.thread_.open_cap()

    @QtCore.Slot(dict)
    def states_video(self, states):
        self.stop = not states[2]

    @QtCore.Slot(QImage)
    def update_image(self, image):
        self.setPixmap(QPixmap.fromImage(image))
