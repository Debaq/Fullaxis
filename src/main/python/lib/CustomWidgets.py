from PySide6.QtGui import QImage, QPixmap
from PySide6.QtWidgets import QLabel, QHBoxLayout, QPushButton, QFrame
from PySide6.QtCore import Qt, Signal, Property, QTimer, QSize
from lib.Ui_constructors import set_button_icon
import qtawesome as qta


class PupilWidget(QLabel):
    def __init__(self):
        super().__init__()

    def update_image(self, image):
        self.setPixmap(QPixmap.fromImage(image))


class TabButton(QFrame):
    click_close = Signal(str)
    click_tab = Signal(str)

    def __init__(self, test, text=None):
        super().__init__()
        if text is None:
            text = ''
        self.test = test
        self._active = False
        self.layout = QHBoxLayout(self)
        self.label = QLabel(text, self)

   

        self.btn_close = QPushButton('x', self)
        self.btn_close.setFlat(True)

        self.name = ""

        self._icon()
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.btn_close)
        self.layout.setContentsMargins(10, 0, 2, 0)
        self.setFrameShape(QFrame.NoFrame)

        self.btn_close.clicked.connect(self.close_tab)

        self.updateStyleSheet()
        self.set_buttons()
        self._size()

    def setName(self, name: str):
        self.name = name

    def _icon(self):

        if self.test == "TUG":
            icon = 'mdi.walk'
        elif self.test == "VNG":
            icon = 'mdi.eye-outline'
        elif self.test == "SOT":
            icon = 'mdi.foot-print'
        
        self.simple_widget = qta.IconWidget(icon, color='white', 
                               size=QSize(16, 16))
        self.layout.addWidget(self.simple_widget)
        

    
    def get_test(self):
        return  (self.test, self.name)
    
    def set_buttons(self):
        set_button_icon(self.btn_close, "ph.x", color='white', size=15)


    def _size(self):
        size_btn_close = 20
        size_margins = 10 + 2
        self.btn_close.setMaximumWidth(size_btn_close)
        self.btn_close.setMaximumHeight(size_btn_close)   

        self.label.adjustSize()
        
        width = self.label.width() + size_btn_close + size_margins
        
        self.setMinimumWidth(width)
        
        self.setMaximumHeight(43)
        self.setMinimumHeight(43)

    def setText(self, text: str):
        self.label.setText(text)
    
    def close_tab(self):
        self.click_close.emit(self.name)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.click_tab.emit(self.name)

    def getActive(self):
        return self._active

    def setActive(self, value):
        if self._active != value:
            self._active = value
            self.updateStyleSheet()


    def updateStyleSheet(self):
        if self._active:
            self.setStyleSheet("""
                    TabButton{
                    background-color: rgba(37, 37, 37, 1);
                    border: 1px solid black;
                    border-radius: 3px;}
                    IconWidget{background-color: rgba(37, 37, 37, 1);}
                    QLabel{background-color: rgba(37, 37, 37, 1);}
            """)
            self.label.setStyleSheet('background-color: rgba(37, 37, 37, 1)')
            self.label.setStyleSheet('border: 0px')
        else:
            self.setStyleSheet("""
                    background-color: rgba(65, 65, 65, 1);
                    border: none;
            """)
            self.label.setStyleSheet('background-color: rgba(65, 65, 65, 1)')


class DraggableWidget(QFrame):
    def __init__(self):
        super().__init__()

        # Guarda la posición del ratón cuando se presiona el botón del ratón
        self.mouse_press_position = None
        self.was_maximized = False  # Agrega una variable para rastrear si la ventana estaba maximizada


    def mousePressEvent(self, event):
        # Si el botón izquierdo del ratón se presiona dentro del widget, guarda la posición del ratón
        if event.button() == Qt.LeftButton:
            self.mouse_press_position = event.position().toPoint()
            self.was_maximized = self.window().isMaximized()  # Guarda si la ventana estaba maximizada

    def mouseMoveEvent(self, event):
        # Si el botón izquierdo del ratón se está moviendo y se ha presionado dentro del widget,
        # mueve la ventana principal a la posición del ratón
        if event.buttons() == Qt.LeftButton and self.mouse_press_position is not None:
            if self.was_maximized:
                self.window().showNormal()
                
            else:
                
                self.window().move(self.window().pos() + event.position().toPoint() - self.mouse_press_position)

    def mouseReleaseEvent(self, event):
        # Si el botón izquierdo del ratón se suelta, borra la posición guardada del ratón
        if event.button() == Qt.LeftButton:
            self.mouse_press_position = None
            self.was_maximized = False

    def mouseDoubleClickEvent(self, event):
        # Si se hace doble clic en el widget, maximiza o restaura la ventana principal
        if event.button() == Qt.LeftButton:
            if self.window().isMaximized():
                self.window().showNormal()
            else:
                self.window().showMaximized()

class HoverButton(QPushButton):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setStyleSheet("background-color: white;")

    def enterEvent(self, event):
        self.setStyleSheet("background-color: red;")

    def leaveEvent(self, event):
        self.setStyleSheet("background-color: white;")