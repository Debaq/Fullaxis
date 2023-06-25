from PySide6.QtGui import QImage, QPixmap
from PySide6.QtWidgets import QLabel, QHBoxLayout, QPushButton, QFrame
from PySide6.QtCore import Qt, Signal, Property


class PupilWidget(QLabel):
    def __init__(self):
        super().__init__()

    def update_image(self, image):
        self.setPixmap(QPixmap.fromImage(image))


class CustomWidget(QFrame):
    clicked = Signal()
    buttonClicked = Signal()

    def __init__(self, text=None):
        super().__init__()
        if text is None:
            text = ''

        self._active = True
        self.layout = QHBoxLayout(self)
        self.label = QLabel(text, self)
        self.button = QPushButton('x', self)
        self.button.setFlat(True)
        self.button.setMaximumWidth(15)
        self.button.setMaximumHeight(15)
        self.button.setStyleSheet("background-color: rgba(140, 93, 217,1)")
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.button)
        self.setContentsMargins(0, 0, 0, 0)
        self.setFrameShape(QFrame.NoFrame)

        self.button.clicked.connect(self.buttonClicked.emit)

        self.updateStyleSheet()
        self._size()

    def _size(self):
        self.setMaximumHeight(35)
        self.setMinimumHeight(35)

    def setText(self, text: str):
        self.label.setText(text)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.clicked.emit()

    def getActive(self):
        return self._active

    def setActive(self, value):
        if self._active != value:
            self._active = value
            self.updateStyleSheet()

    active = Property(bool, getActive, setActive)

    def updateStyleSheet(self):
        if self._active:
            self.setStyleSheet("""
                
                    background-color: rgba(37, 37, 37, 1);
                    border: 1px solid black;
                    border-radius: 10px;
                    
                
            """)
            self.label.setStyleSheet('background-color: rgba(37, 37, 37, 1)')
            self.label.setStyleSheet('border: 0px')

        else:
            self.setStyleSheet("""
                
                    background-color: rgba(65, 65, 65, 1);
                    border: none;
                
                
            """)
            self.label.setStyleSheet('background-color: rgba(65, 65, 65, 1)')
