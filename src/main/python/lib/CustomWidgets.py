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
    """Definición de señales para emitir eventos de clic en la pestaña y cerrar la pestaña.
    se utilizo un qframe como si se tratara de un tab button"""
    click_close = Signal(str)
    click_tab = Signal(str)

    def __init__(self, test, text=None):
        """Asigna un texto predeterminado si no se proporciona uno."""
        super().__init__()
        if text is None:
            text = ''
        self.test = test
        self._active = False  # Estado de activación de la pestaña.
        self.layout = QHBoxLayout(self)  # Configura el diseño horizontal para los elementos de la pestaña.
        self.label = QLabel(text, self)  # Etiqueta para mostrar el texto de la pestaña.

        # Botón para cerrar la pestaña.
        self.btn_close = QPushButton('x', self)
        self.btn_close.setFlat(True) # Hace que el botón sea plano, sin bordes ni fondo.

        self.name = ""  # Nombre identificador de la pestaña.

        self._icon()  # Configura el icono de la pestaña basado en el test.
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.btn_close)
        self.layout.setContentsMargins(10, 0, 2, 0)  # Ajusta los márgenes del layout.
        self.setFrameShape(QFrame.NoFrame)  # Configura la forma del marco de la pestaña.

        self.btn_close.clicked.connect(self.close_tab)  # Conecta el botón de cerrar con su slot.

        self.updateStyleSheet()  # Actualiza la hoja de estilos según el estado de activación.
        self.set_buttons()  # Configura los iconos de los botones.
        self._size()  # Ajusta el tamaño de la pestaña.

    def set_name(self, name: str):
        """Asigna un nombre identificador a la pestaña."""
        self.name = name  

    def _icon(self):
        # Configura el icono de la pestaña basado en el valor de `test`.
        # esto quizas deba tomarlo desde un kson o un archivo externo para aumentar las posibilidades en un futuro
        if self.test == "TUG":
            icon = 'mdi.walk'
        elif self.test == "VNG":
            icon = 'mdi.eye-outline'
        elif self.test == "SOT":
            icon = 'mdi.foot-print'

        self.simple_widget = qta.IconWidget(icon, color='white', size=QSize(16, 16))
        self.layout.addWidget(self.simple_widget)

    def get_test(self):
        """Devuelve el tipo de test y el nombre de la pestaña."""
        return (self.test, self.name)

    def set_buttons(self):
        """Configura el icono del botón de cerrar."""
        set_button_icon(self.btn_close, "ph.x", color='white', size=15)

    def _size(self):
        #Ajusta el tamaño de la pestaña y sus componentes.
        size_btn_close = 20
        size_margins = 10 + 2
        self.btn_close.setMaximumWidth(size_btn_close)
        self.btn_close.setMaximumHeight(size_btn_close)

        self.label.adjustSize()
        width = self.label.width() + size_btn_close + size_margins
        self.setMinimumWidth(width)
        self.setMaximumHeight(43)
        self.setMinimumHeight(43)

    def set_text(self, text: str):
        """Establece el texto de la etiqueta de la pestaña."""
        self.label.setText(text)

    def close_tab(self):
        """Emite la señal `click_close` con el nombre de la pestaña al cerrarla."""
        self.click_close.emit(self.name)

    def mousePressEvent(self, event):
        """Emite la señal `click_tab` con el nombre de la pestaña al hacer clic en ella."""
        if event.button() == Qt.LeftButton:
            self.click_tab.emit(self.name)

    def getActive(self):
        """Devuelve el estado de activación de la pestaña."""
        return self._active

    def setActive(self, value):
        """Establece el estado de activación de la pestaña y actualiza la hoja de estilos."""
        if self._active != value:
            self._active = value
            self.updateStyleSheet()

    def updateStyleSheet(self):
        """Actualiza la hoja de estilos de la pestaña según su estado de activación."""
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