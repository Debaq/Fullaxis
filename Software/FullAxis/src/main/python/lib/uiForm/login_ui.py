# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_login(object):
    def setupUi(self, login):
        if not login.objectName():
            login.setObjectName(u"login")
        login.resize(1000, 700)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(login.sizePolicy().hasHeightForWidth())
        login.setSizePolicy(sizePolicy)
        login.setMinimumSize(QSize(1000, 700))
        self.back_layout = QVBoxLayout(login)
        self.back_layout.setSpacing(0)
        self.back_layout.setObjectName(u"back_layout")
        self.back_layout.setContentsMargins(0, 0, 0, 0)
        self.back_frame = QFrame(login)
        self.back_frame.setObjectName(u"back_frame")
        self.layoutback_frame = QVBoxLayout(self.back_frame)
        self.layoutback_frame.setObjectName(u"layoutback_frame")
        self.layoutback_frame.setContentsMargins(1, 1, -1, -1)
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.layoutback_frame.addItem(self.verticalSpacer)

        self.horizontalFrame = QFrame(self.back_frame)
        self.horizontalFrame.setObjectName(u"horizontalFrame")
        self.horizontalLayout_2 = QHBoxLayout(self.horizontalFrame)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(1, 1, 1, -1)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.center_login = QFrame(self.horizontalFrame)
        self.center_login.setObjectName(u"center_login")
        self.verticalLayout_2 = QVBoxLayout(self.center_login)
        self.verticalLayout_2.setSpacing(10)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(10, 10, 10, 10)
        self.verticalFrame_2 = QFrame(self.center_login)
        self.verticalFrame_2.setObjectName(u"verticalFrame_2")
        self.verticalFrame_2.setMinimumSize(QSize(0, 100))
        self.verticalLayout_3 = QVBoxLayout(self.verticalFrame_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(-1, 1, -1, -1)
        self.label = QLabel(self.verticalFrame_2)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"image: url(:/icons svg/icons/svg/fullaxis.svg);")
        self.label.setScaledContents(False)

        self.verticalLayout_3.addWidget(self.label)

        self.label_2 = QLabel(self.verticalFrame_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_2)


        self.verticalLayout_2.addWidget(self.verticalFrame_2)

        self.input_user = QLineEdit(self.center_login)
        self.input_user.setObjectName(u"input_user")

        self.verticalLayout_2.addWidget(self.input_user)

        self.input_pass = QLineEdit(self.center_login)
        self.input_pass.setObjectName(u"input_pass")
        self.input_pass.setEchoMode(QLineEdit.Password)

        self.verticalLayout_2.addWidget(self.input_pass)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btn_requestlogin = QPushButton(self.center_login)
        self.btn_requestlogin.setObjectName(u"btn_requestlogin")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.MinimumExpanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.btn_requestlogin.sizePolicy().hasHeightForWidth())
        self.btn_requestlogin.setSizePolicy(sizePolicy1)
        self.btn_requestlogin.setMinimumSize(QSize(0, 30))
        self.btn_requestlogin.setStyleSheet(u"QPushButton {\n"
" Text-align:center;\n"
" border: none;\n"
" color:rgb(238, 238, 236);\n"
"background-color: rgb(55, 144, 152);\n"
"}\n"
" QPushButton:hover {\n"
" background-color: rgb(0, 98, 106);\n"
"}\n"
"QPushButton:pressed {\n"
" text-decoration: underline;}")

        self.horizontalLayout.addWidget(self.btn_requestlogin)

        self.btn_cancel = QPushButton(self.center_login)
        self.btn_cancel.setObjectName(u"btn_cancel")
        sizePolicy1.setHeightForWidth(self.btn_cancel.sizePolicy().hasHeightForWidth())
        self.btn_cancel.setSizePolicy(sizePolicy1)
        self.btn_cancel.setMinimumSize(QSize(0, 30))
        self.btn_cancel.setStyleSheet(u"QPushButton {\n"
" Text-align:center;\n"
" border: none;\n"
" color:rgb(238, 238, 236);\n"
"background-color: rgb(204, 0, 0);\n"
"}\n"
" QPushButton:hover {\n"
" background-color: rgb(164, 0, 0);\n"
"}\n"
"QPushButton:pressed {\n"
" text-decoration: underline;}")

        self.horizontalLayout.addWidget(self.btn_cancel)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.pushButton = QPushButton(self.center_login)
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

        self.verticalLayout_2.addWidget(self.pushButton)

        self.verticalLayout_2.setStretch(0, 10)
        self.verticalLayout_2.setStretch(1, 10)
        self.verticalLayout_2.setStretch(2, 10)
        self.verticalLayout_2.setStretch(3, 10)
        self.verticalLayout_2.setStretch(4, 10)

        self.horizontalLayout_2.addWidget(self.center_login)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.layoutback_frame.addWidget(self.horizontalFrame)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.layoutback_frame.addItem(self.verticalSpacer_2)


        self.back_layout.addWidget(self.back_frame)


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
        self.btn_requestlogin.setText(QCoreApplication.translate("login", u"Ingresar", None))
        self.btn_cancel.setText(QCoreApplication.translate("login", u"Cancelar", None))
        self.pushButton.setText(QCoreApplication.translate("login", u"Cambiar configuraci\u00f3n", None))
    # retranslateUi

