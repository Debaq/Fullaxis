# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'search_bar.ui'
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
    QLineEdit, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_search_bar(object):
    def setupUi(self, search_bar):
        if not search_bar.objectName():
            search_bar.setObjectName(u"search_bar")
        search_bar.resize(672, 299)
        search_bar.setStyleSheet(u"QFrame{background-color: rgb(245, 245, 245);}\n"
"\n"
"                          QLineEdit {\n"
"                            border: 2px none gray;\n"
"                            border-radius: 18px;\n"
"                            padding: 10 20px;\n"
"                            background: rgb(237, 238, 240);\n"
"                            selection-background-color: darkgray;\n"
"                            }\n"
"                            QLineEdit:hover {\n"
"                                background: rgb(230, 232, 237);\n"
"                                }\n"
"                            QLineEdit:focus {\n"
"                                background: rgb(255, 255, 255);\n"
"                                \n"
"                            }\n"
"")
        self.horizontalLayout_3 = QHBoxLayout(search_bar)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalFrame = QFrame(search_bar)
        self.verticalFrame.setObjectName(u"verticalFrame")
        self.verticalFrame.setMinimumSize(QSize(250, 0))
        self.verticalFrame.setMaximumSize(QSize(250, 16777215))
        self.verticalLayout = QVBoxLayout(self.verticalFrame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(1, -1, -1, -1)
        self.label = QLabel(self.verticalFrame)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label)


        self.horizontalLayout_3.addWidget(self.verticalFrame)

        self.frame = QFrame(search_bar)
        self.frame.setObjectName(u"frame")
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.lineEdit = QLineEdit(self.frame)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setStyleSheet(u"")

        self.verticalLayout_2.addWidget(self.lineEdit)


        self.horizontalLayout_3.addWidget(self.frame)

        self.horizontalFrame_2 = QFrame(search_bar)
        self.horizontalFrame_2.setObjectName(u"horizontalFrame_2")
        self.horizontalFrame_2.setMinimumSize(QSize(100, 0))
        self.horizontalFrame_2.setMaximumSize(QSize(100, 16777215))
        self.verticalLayout_4 = QVBoxLayout(self.horizontalFrame_2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.btn_config = QPushButton(self.horizontalFrame_2)
        self.btn_config.setObjectName(u"btn_config")
        self.btn_config.setFlat(True)

        self.verticalLayout_4.addWidget(self.btn_config)


        self.horizontalLayout_3.addWidget(self.horizontalFrame_2)


        self.retranslateUi(search_bar)

        QMetaObject.connectSlotsByName(search_bar)
    # setupUi

    def retranslateUi(self, search_bar):
        search_bar.setWindowTitle(QCoreApplication.translate("search_bar", u"Form", None))
        self.label.setText(QCoreApplication.translate("search_bar", u"FullAxis", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("search_bar", u"Buscar usuario", None))
        self.btn_config.setText(QCoreApplication.translate("search_bar", u"Configuraci\u00f3n", None))
    # retranslateUi

