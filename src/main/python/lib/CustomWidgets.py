from lib.video.OpenCVProcessingThread import OpenCVProcessingThread
from PySide6 import QtCore
from PySide6.QtGui import QImage, QPixmap
from PySide6.QtWidgets import QLabel


class CustomLabel(QLabel):
    def __init__(self):
        super().__init__()
        self.start_video()

    def start_video(self):
        self.thread = OpenCVProcessingThread()
        self.thread.change_pixmap_signal.connect(self.update_image)
        self.thread.start()

    def stop_video(self, save, name):
        self.thread.stop(save, name)
        self.thread.quit()

    @QtCore.Slot(QImage)
    def update_image(self, image):
        self.setPixmap(QPixmap.fromImage(image))
