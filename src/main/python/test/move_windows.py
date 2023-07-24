import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QFrame, QVBoxLayout, QWidget
from PySide6.QtCore import Qt, QTimer

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
                self.was_maximized = False
            else:
              
                self.window().move(self.window().pos() + event.position().toPoint() - self.mouse_press_position)

    def mouseReleaseEvent(self, event):
        # Si el botón izquierdo del ratón se suelta, borra la posición guardada del ratón
        if event.button() == Qt.LeftButton:
            self.mouse_press_position = None

    def mouseDoubleClickEvent(self, event):
        # Si se hace doble clic en el widget, maximiza o restaura la ventana principal
        if event.button() == Qt.LeftButton:
            if self.window().isMaximized():
                self.window().showNormal()
            else:
                self.window().showMaximized()

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Crea tres QFrames con diferentes colores de fondo
        self.red_frame = DraggableWidget()
        self.red_frame.setStyleSheet("background-color: red")
        self.blue_frame = QFrame()
        self.blue_frame.setStyleSheet("background-color: blue")
        self.green_frame = QFrame()
        self.green_frame.setStyleSheet("background-color: green")

        # Crea un QWidget para ser el widget central de la ventana
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Crea un QVBoxLayout y añade los QFrames a él
        layout = QVBoxLayout()
        layout.addWidget(self.red_frame)
        layout.addWidget(self.blue_frame)
        layout.addWidget(self.green_frame)
        central_widget.setLayout(layout)

app = QApplication(sys.argv)

window = MainWindow()
window.show()

sys.exit(app.exec())
