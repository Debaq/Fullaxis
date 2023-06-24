from PySide6.QtGui import QImage, QPixmap
from PySide6.QtWidgets import QLabel


class PupilWidget(QLabel):
    def __init__(self):
        super().__init__()

    def update_image(self, image):
        self.setPixmap(QPixmap.fromImage(image))
