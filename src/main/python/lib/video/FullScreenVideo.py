import sys
from PySide6.QtCore import Qt, QEvent, QRect, Signal
from PySide6.QtGui import QPixmap, QScreen, QImage, QPainter, QColor, QFont
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLabel, QDialog

class VideoPopup(QDialog):
    closed = Signal()
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Pantalla completa")

        # Establece la ventana emergente en modo de pantalla completa
        #self.showFullScreen()

        # Creación del QLabel para el video
        self.video_label = QLabel(self)
        self.video_label.setObjectName("video")
        self.video_label.setAlignment(Qt.AlignCenter)

        # Establece un layout y añade el QLabel
        layout = QVBoxLayout(self)
        layout.addWidget(self.video_label)

    def add_text_to_image(self, image, text, position=(10, 30), font_size=20, color=QColor(255, 255, 255)):
        """
        Agrega texto a una QImage.

        :param image: La QImage original.
        :param text: El texto a agregar.
        :param position: Una tupla (x, y) que define la posición donde empezará el texto.
        :param font_size: El tamaño de la fuente del texto.
        :param color: El color del texto.
        :return: La QImage con el texto agregado.
        """
        painter = QPainter(image)
        painter.setPen(color)
        font = QFont()
        font.setPixelSize(font_size)
        painter.setFont(font)
        painter.drawText(position[0], position[1], text)
        painter.end()
        return image

    def update_video(self, image: QImage, time = "waiting <space> for initialize..."):
        scaled_image = self.add_text_to_image(image, time)
        scaled_image = image.scaled(self.video_label.width(), self.video_label.height(), Qt.KeepAspectRatio)
        self.video_label.setPixmap(QPixmap.fromImage(scaled_image))
        
        
    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            self.close()
        
    def closeEvent(self, event):
        self.closed.emit()
        super().closeEvent(event)