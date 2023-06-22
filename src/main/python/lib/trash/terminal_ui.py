# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'terminal.ui'
##
## Created by: Qt User Interface Compiler version 6.2.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLineEdit,
    QPlainTextEdit, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_terminal(object):
    def setupUi(self, terminal):
        if not terminal.objectName():
            terminal.setObjectName(u"terminal")
        terminal.resize(400, 300)
        self.verticalLayout = QVBoxLayout(terminal)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lbl_com = QLabel(terminal)
        self.lbl_com.setObjectName(u"lbl_com")

        self.verticalLayout.addWidget(self.lbl_com)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.input_data = QLineEdit(terminal)
        self.input_data.setObjectName(u"input_data")

        self.horizontalLayout.addWidget(self.input_data)

        self.btn_send = QPushButton(terminal)
        self.btn_send.setObjectName(u"btn_send")

        self.horizontalLayout.addWidget(self.btn_send)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.text_serial_output = QPlainTextEdit(terminal)
        self.text_serial_output.setObjectName(u"text_serial_output")

        self.verticalLayout.addWidget(self.text_serial_output)


        self.retranslateUi(terminal)

        QMetaObject.connectSlotsByName(terminal)
    # setupUi

    def retranslateUi(self, terminal):
        terminal.setWindowTitle(QCoreApplication.translate("terminal", u"Form", None))
        self.lbl_com.setText(QCoreApplication.translate("terminal", u"nn", None))
        self.btn_send.setText(QCoreApplication.translate("terminal", u"send", None))
    # retranslateUi

