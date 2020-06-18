# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'loginCMxjHz.ui'
##
## Created by: Qt User Interface Compiler version 5.15.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *

from resource import resource_rc

class Ui_login(object):
    def setupUi(self, login):
        if not login.objectName():
            login.setObjectName(u"login")
        login.resize(200, 250)
        login.setMinimumSize(QSize(200, 250))
        login.setMaximumSize(QSize(200, 250))
        self.verticalLayout = QVBoxLayout(login)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(login)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"image: url(:/icons svg/icons/svg/fullaxis.svg);")
        self.label.setScaledContents(False)

        self.verticalLayout.addWidget(self.label)

        self.label_2 = QLabel(login)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_2)

        self.input_user = QLineEdit(login)
        self.input_user.setObjectName(u"input_user")

        self.verticalLayout.addWidget(self.input_user)

        self.input_pass = QLineEdit(login)
        self.input_pass.setObjectName(u"input_pass")
        self.input_pass.setEchoMode(QLineEdit.Password)

        self.verticalLayout.addWidget(self.input_pass)

        self.btn_login = QPushButton(login)
        self.btn_login.setObjectName(u"btn_login")

        self.verticalLayout.addWidget(self.btn_login)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton = QPushButton(login)
        self.pushButton.setObjectName(u"pushButton")
        font = QFont()
        font.setPointSize(8)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet(u"QPushButton {\n"
"background-position: center;\n"
"border: none;\n"
"color:rgb(52, 101, 164)\n"
"}\n"
"QPushButton:hover {\n"
"color:rgb(114, 159, 207)\n"
"}\n"
"QPushButton:pressed {\n"
"}")
        self.pushButton.setFlat(True)

        self.horizontalLayout.addWidget(self.pushButton)


        self.verticalLayout.addLayout(self.horizontalLayout)

        QWidget.setTabOrder(self.input_user, self.input_pass)
        QWidget.setTabOrder(self.input_pass, self.btn_login)

        self.retranslateUi(login)

        QMetaObject.connectSlotsByName(login)
    # setupUi

    def retranslateUi(self, login):
        login.setWindowTitle(QCoreApplication.translate("login", u"Form", None))
        self.label.setText("")
        self.label_2.setText(QCoreApplication.translate("login", u"FullAxis", None))
        self.input_user.setText("")
        self.input_user.setPlaceholderText(QCoreApplication.translate("login", u"Identificaci\u00f3n", None))
        self.input_pass.setPlaceholderText(QCoreApplication.translate("login", u"Contrase\u00f1a", None))
        self.btn_login.setText(QCoreApplication.translate("login", u"Ingresar", None))
        self.pushButton.setText(QCoreApplication.translate("login", u"Cambiar configuraci\u00f3n", None))
    # retranslateUi

