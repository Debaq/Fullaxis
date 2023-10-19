from PySide6 import QtWidgets, QtCore, QtGui
from PySide6.QtCore import Slot,Qt
from PySide6.QtCore import QMetaObject
from Qtcronometer import Cronometro

import cv2
import sys
from threading import Thread
import queue
import numpy as np

class FullscreenWindow(QtWidgets.QWidget):
    closed = QtCore.Signal()
    def __init__(self, frame):
        super().__init__()
        self.label = QtWidgets.QLabel(self)
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.label)
        self.setLayout(layout)
        
        self.image_queue = queue.Queue()
        self.image_queue.put(frame)
        
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.show_frame)
        self.timer.start(30)
    
    def show_frame(self):
        if not self.image_queue.empty():
            frame = self.image_queue.get()
            height, width, _ = frame.shape
            bytes_per_line = 3 * width
            q_img = QtGui.QImage(frame.data, width, height, bytes_per_line, QtGui.QImage.Format_RGB888)
            pixmap = QtGui.QPixmap.fromImage(q_img)

            screen_geometry = QtWidgets.QApplication.screenAt(self.geometry().center()).geometry()
            self.label.resize(screen_geometry.width(), screen_geometry.height())  # Cambiar el tamaño del label al tamaño de la pantalla

            self.label.setPixmap(pixmap.scaled(self.label.width(), self.label.height(), QtCore.Qt.IgnoreAspectRatio))

    @Slot(object)
    def upgrade_frame(self, img):
        self.image_queue.put(img)
        QMetaObject.invokeMethod(self, "show_frame", Qt.QueuedConnection)

    def mouseDoubleClickEvent(self, event):
        self.close()  # Cerramos la ventana al hacer doble clic en ella
        
    def closeEvent(self, event):
        self.closed.emit()
        super().closeEvent(event)



class WebcamWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.cap = cv2.VideoCapture(0)
        self.is_fullscreen = False
        self.fullscreen_window_open = False  # Variable de control para la ventana emergente

        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.update_frame)
        self.timer.start(30)

        self.label = QtWidgets.QLabel(self)
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.label)
        self.setLayout(layout)

        self.label.mouseDoubleClickEvent = self.mouseDoubleClickEvent
        
        self.time_text= ""
        self.cronometro = Cronometro()
        self.cronometro.tiempo_actualizado.connect(self.on_tiempo_actualizado)

        
    def update_frame(self):
        _, frame = self.cap.read()
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        cv2.putText(frame, self.time_text, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

        self.current_frame = frame
        if self.fullscreen_window_open:
            self.fullscreen_window.upgrade_frame(self.current_frame)
        self.show_frame()

    def keyPressEvent(self, event):
            if event.key() == QtCore.Qt.Key_Space:
                if self.cronometro.is_paused:
                    self.cronometro.start()
                else:
                    self.cronometro.pause()
            elif event.key() == QtCore.Qt.Key_Escape:
                self.cronometro.reset()


    def on_tiempo_actualizado(self, tiempo, show_dot, state):
        dot = ' .' if show_dot else ' '
        self.time_text = f"{state} : {tiempo} s{dot}"

    def show_frame(self):
        height, width, channel = self.current_frame.shape
        bytes_per_line = 3 * width
        q_img = QtGui.QImage(self.current_frame.data, width, height, bytes_per_line, QtGui.QImage.Format_RGB888)
        self.label.setPixmap(QtGui.QPixmap.fromImage(q_img))

   
    def mouseDoubleClickEvent(self, event):
        if not self.fullscreen_window_open:  # Verificar si ya hay una ventana emergente abierta
            self.open_fullscreen_window()
            
    def open_fullscreen_window(self):
        self.fullscreen_window_open = True  # Marcamos que la ventana emergente está abierta
        self.fullscreen_window = FullscreenWindow(self.current_frame)
        self.fullscreen_window.setWindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)

        screens = QtWidgets.QApplication.screens()
        current_screen = QtWidgets.QApplication.screenAt(self.geometry().center())

        for screen in screens:
            if screen != current_screen:
                # Si encontramos una pantalla que no es la pantalla actual, movemos la ventana emergente a esa pantalla
                screen_geometry = screen.geometry()
                self.fullscreen_window.move(screen_geometry.x(), screen_geometry.y())
                break

        self.fullscreen_window.closed.connect(self.reset_fullscreen_window_open)  # Conectar una función para resetear la variable cuando la ventana se destruye
        self.fullscreen_window.showFullScreen()

    def reset_fullscreen_window_open(self):
        # Función para resetear la variable fullscreen_window_open cuando la ventana emergente se destruye
        self.fullscreen_window_open = False

    def closeEvent(self, event):
        if self.fullscreen_window_open:  # Si la ventana emergente está abierta
            self.fullscreen_window.close()  # La cerramos

        event.accept()  # Aceptamos el evento de cierre


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    mainWin = WebcamWidget()
    mainWin.show()
    sys.exit(app.exec_())
