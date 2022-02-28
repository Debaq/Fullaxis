import sys

from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLineEdit,
                               QMainWindow, QTextEdit, QVBoxLayout, QWidget)

from new_pug_hw import receiver_data


class MainWindow(QMainWindow):  
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle("Serial port display / send")
        self.message_le = QLineEdit()
        self.output_te = QTextEdit(readOnly=True)
        lay = QVBoxLayout(self)
        hlay = QHBoxLayout()
        hlay.addWidget(self.message_le)
        lay.addLayout(hlay)
        lay.addWidget(self.output_te)
        widget = QWidget()
        widget.setLayout(lay)
        self.setCentralWidget(widget)
        self.serial = receiver_data()
        self.serial.start()
        self.serial.data.connect(self.receive)
        
    def receive(self, data):
        self.output_te.append(data)

    
        
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec())
