from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QSplashScreen
from PySide6.QtGui import QPixmap
from PySide6.QtCore import QTimer
import sys
from base import context

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Ventana Principal')
        self.setGeometry(100, 100, 300, 200)

def check_screen_resolution(app):
    screen_resolution = app.primaryScreen().size()
    if screen_resolution.width() < 1280 or screen_resolution.height() < 720:
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Critical)
        msgBox.setText("Resolución de pantalla insuficiente")
        msgBox.setInformativeText("Se necesita una resolución mínima de 720p para ejecutar este programa.")
        msgBox.exec()
        return False
    else:
        return True

if __name__ == "__main__":
    app = QApplication([])

    if not check_screen_resolution(app):
        sys.exit()

    splash = QSplashScreen(QPixmap(context.get_resource("img/splash.png")))  # Reemplaza 'ruta/a/tu/imagen.png' con la ruta a tu imagen de splash screen
    splash.show()

    QTimer.singleShot(2000, splash.close)  # Muestra el splash screen durante 2 segundos

    window = MainWindow()
    window.show()

    sys.exit(app.exec())
