from PySide6.QtWidgets import QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox

class NameDialog(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Introduce el nombre')
        self.setGeometry(100, 100, 300, 200)

        self.layout = QVBoxLayout(self)

        self.label = QLabel('Nombre:', self)
        self.line_edit = QLineEdit(self)
        self.accept_button = QPushButton('Aceptar', self)
        self.cancel_button = QPushButton('Cancelar', self)

        self.layout.addWidget(self.label)
        self.layout.addWidget(self.line_edit)
        self.layout.addWidget(self.accept_button)
        self.layout.addWidget(self.cancel_button)

        self.accept_button.clicked.connect(self.accept)
        self.cancel_button.clicked.connect(self.reject)

    def accept(self):
        super().accept()
        
    def get_name(self):
        return self.line_edit.text()
    
class ErrorMessageBox(QMessageBox):
    def __init__(self):
        super().__init__()

        self.setIcon(QMessageBox.Warning)
        self.setText("Error")
        self.setInformativeText("No se puede modificar.")
        self.setStandardButtons(QMessageBox.Ok)