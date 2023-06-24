from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QDialog, QVBoxLayout, QSlider

class SecondWindow(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Segunda Ventana')
        self.setGeometry(100, 100, 300, 200)

        self.layout = QVBoxLayout(self)

        self.button1 = QPushButton('Botón 1', self)
        self.button2 = QPushButton('Botón 2', self)
        self.slider = QSlider(self)

        self.layout.addWidget(self.button1)
        self.layout.addWidget(self.button2)
        self.layout.addWidget(self.slider)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Ventana Principal')
        self.setGeometry(100, 100, 300, 200)

        self.button = QPushButton('Abrir Segunda Ventana', self)
        self.button.clicked.connect(self.open_second_window)
        self.setCentralWidget(self.button)

    def open_second_window(self):
        self.second_window = SecondWindow()
        self.second_window.exec()

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
