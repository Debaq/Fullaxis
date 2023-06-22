import cv2
from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtCore import Qt, QThread, Signal
from PySide6.QtGui import QImage, QPixmap
from PySide6.QtWidgets import QLabel

class VideoThread(QThread):
    change_pixmap_signal = Signal(QImage)

    def run(self):
        cap = cv2.VideoCapture(0)  # Captura de video desde la cámara por defecto (0)
        cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'))
        width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
        height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)        
        cap.get(cv2.CAP_PROP_FPS)
        fps = cap.set(cv2.CAP_PROP_FPS, 210)
        print(f'Ancho del marco: {width}, Altura del marco: {height}, FPS: {fps}')

        while True:
            ret, frame = cap.read()

            if ret:
                rgb_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                h, w, ch = rgb_image.shape
                bytes_per_line = ch * w
                convert_to_Qt_format = QImage(rgb_image.data, w, h, bytes_per_line, QImage.Format_RGB888)
                p = convert_to_Qt_format.scaled(640, 480, Qt.KeepAspectRatio)
                self.change_pixmap_signal.emit(p)

class CustomLabel(QLabel):
    def __init__(self):
        super().__init__()
        self.start_video()

    def start_video(self):
        self.thread = VideoThread()
        self.thread.change_pixmap_signal.connect(self.update_image)
        self.thread.start()

    @QtCore.Slot(QImage)
    def update_image(self, image):
        self.setPixmap(QPixmap.fromImage(image))

    def mouseDoubleClickEvent(self, event):
        print(self.windowState())
        if self.windowState() & Qt.WindowFullScreen:
            self.setWindowState(Qt.WindowNoState)
        else:
            self.setWindowState(Qt.WindowFullScreen)

class CustomWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('OpenCV Video Feed in PySide6')
        self.setGeometry(100, 100, 700, 500)
        self.setWindowState(Qt.WindowFullScreen)

        self.label = CustomLabel()
        layout = QtWidgets.QVBoxLayout(self)
        layout.addWidget(self.label)

        self.show()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = CustomWidget()
    sys.exit(app.exec())
