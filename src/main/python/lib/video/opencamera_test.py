import cv2
from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtCore import Qt, QThread, Signal
from PySide6.QtGui import QImage, QPixmap
from PySide6.QtWidgets import QLabel, QPushButton, QVBoxLayout

class VideoThread(QThread):
    change_pixmap_signal = Signal(QImage)

    def __init__(self):
        super().__init__()
        self._run_flag = True

    def run(self):
        self.cap = cv2.VideoCapture(0)  # Captura de video desde la cámara por defecto (0)
        self.out = cv2.VideoWriter('output.avi', cv2.VideoWriter_fourcc(*'XVID'), 20.0, (640, 480))

        while self._run_flag:
            ret, frame = self.cap.read()
            if ret:
                self.out.write(frame)
                rgb_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                h, w, ch = rgb_image.shape
                bytes_per_line = ch * w
                convert_to_Qt_format = QImage(rgb_image.data, w, h, bytes_per_line, QImage.Format_RGB888)
                p = convert_to_Qt_format.scaled(640, 480, Qt.KeepAspectRatio)
                self.change_pixmap_signal.emit(p)

    def stop(self):
        self._run_flag = False
        self.cap.release()
        self.out.release()

class CustomLabel(QLabel):
    def __init__(self):
        super().__init__()

    def start_video(self):
        self.thread = VideoThread()
        self.thread.change_pixmap_signal.connect(self.update_image)
        self.thread.start()

    def stop_video(self):
        self.thread.stop()

    @QtCore.Slot(QImage)
    def update_image(self, image):
        self.setPixmap(QPixmap.fromImage(image))

    def mouseDoubleClickEvent(self, event):
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

        self.label = CustomLabel()

        self.start_button = QPushButton('Start Video', self)
        self.start_button.clicked.connect(self.label.start_video)

        self.stop_button = QPushButton('Stop Video', self)
        self.stop_button.clicked.connect(self.label.stop_video)

        layout = QVBoxLayout(self)
        layout.addWidget(self.label)
        layout.addWidget(self.start_button)
        layout.addWidget(self.stop_button)

        self.show()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = CustomWidget()
    sys.exit(app.exec())
