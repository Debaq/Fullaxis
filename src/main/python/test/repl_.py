import sys
from PySide6.QtWidgets import QApplication, QTextEdit, QVBoxLayout, QLineEdit, QWidget
from PySide6.QtCore import Qt

class ConsoleWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.text_edit = QTextEdit()
        self.line_edit = QLineEdit()

        layout = QVBoxLayout()
        layout.addWidget(self.text_edit)
        layout.addWidget(self.line_edit)

        self.setLayout(layout)

        self.line_edit.returnPressed.connect(self.on_return_pressed)

        self.locals = {}

    def on_return_pressed(self):
        text = self.line_edit.text()
        self.line_edit.clear()

        # Aquí es donde evaluarías el texto y producirías una salida.
        # Por simplicidad, este ejemplo simplemente imprime el texto en la consola.
        self.text_edit.append('>>> ' + text)

        # Aquí es donde evaluarías el texto y producirías una salida.
        try:
            # Primero intentamos evaluar la expresión
            output = str(eval(text, None, self.locals))
        except SyntaxError:
            # Si eval() lanza un SyntaxError, significa que el texto es una declaración, no una expresión.
            # En ese caso, usamos exec().
            try:
                exec(text, None, self.locals)
            except Exception as e:
                output = str(e)
            else:
                output = ''
        except Exception as e:
            output = str(e)

        if output:
            self.text_edit.append(output)

app = QApplication(sys.argv)

console = ConsoleWidget()
console.show()

sys.exit(app.exec())
