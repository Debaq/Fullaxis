from PySide6.QtWidgets import QTreeWidget
from PySide6.QtCore import Qt

class SessionList(QTreeWidget):
    def __init__(self,  *args, **kwargs) -> None:
        super(SessionList, self).__init__( *args, **kwargs)
    
    def mousePressEvent(self, event):
        print("se presiona")
        if event.button() == Qt.LeftButton:
            self.clicked.emit(self.currentIndex())
        
    
    def mouseDoubleClickEvent(self, event):
        print("dobleclick")
        if event.button() == Qt.LeftButton:
            self.doubleClicked.emit(self.currentIndex())
    
    def mouseReleaseEvent(self, event):
        print("se suelta")
        if event.button() == Qt.LeftButton:
            self.released.emit(self.currentIndex())