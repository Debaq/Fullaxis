from PySide6.QtWidgets import QApplication, QFrame, QHBoxLayout, QLabel, QPushButton, QHBoxLayout, QWidget
from PySide6.QtCore import Signal, Property, Qt

class CustomWidget(QFrame):
    clicked = Signal()
    buttonClicked = Signal()

    def __init__(self, text = None):
        super().__init__()
        if text is  None:
            text = ''
        

        self._active = True
        self.layout = QHBoxLayout(self)
        self.label = QLabel(text, self)
        self.button = QPushButton('x',self)
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
    def setText(self, text:str):
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
            

if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)

    widget1 = CustomWidget()
    widget2 = CustomWidget()
    
    widget1.setText('pestaña 1')
    widget2.setText('pestaña 2')

    widget1.clicked.connect(lambda: (widget1.setActive(True), widget2.setActive(False)))
    widget2.clicked.connect(lambda: (widget2.setActive(True), widget1.setActive(False)))

    widget1.buttonClicked.connect(lambda: print('Botón 1 fue presionado'))
    widget2.buttonClicked.connect(lambda: print('Botón 2 fue presionado'))

    layout = QHBoxLayout()
    layout.addWidget(widget1)
    layout.addWidget(widget2)

    container = QFrame()
    container.setStyleSheet('background-color: rgba(65, 65, 65,1)')

    container.setLayout(layout)
    container.show()

    sys.exit(app.exec())
