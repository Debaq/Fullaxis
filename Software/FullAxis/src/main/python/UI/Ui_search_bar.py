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
        search_bar.resize(672, 300)
        self.horizontalLayout_3 = QHBoxLayout(search_bar)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(6, 0, 0, 0)
        self.verticalFrame = QFrame(search_bar)
        self.verticalFrame.setObjectName(u"verticalFrame")
        self.verticalFrame.setMinimumSize(QSize(250, 0))
        self.verticalFrame.setMaximumSize(QSize(250, 16777215))
        self.verticalLayout = QVBoxLayout(self.verticalFrame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(1, -1, -1, -1)
        self.label = QLabel(self.verticalFrame)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)


        self.horizontalLayout_3.addWidget(self.verticalFrame)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.lineEdit = QLineEdit(search_bar)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setStyleSheet(u"")

        self.verticalLayout_2.addWidget(self.lineEdit)


        self.horizontalLayout_3.addLayout(self.verticalLayout_2)

        self.horizontalFrame_2 = QFrame(search_bar)
        self.horizontalFrame_2.setObjectName(u"horizontalFrame_2")
        self.horizontalFrame_2.setMinimumSize(QSize(100, 0))
        self.horizontalFrame_2.setMaximumSize(QSize(100, 16777215))
        self.verticalLayout_4 = QVBoxLayout(self.horizontalFrame_2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.pushButton = QPushButton(self.horizontalFrame_2)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout_4.addWidget(self.pushButton)


        self.horizontalLayout_3.addWidget(self.horizontalFrame_2)


        self.retranslateUi(search_bar)

        QMetaObject.connectSlotsByName(search_bar)
    # setupUi

    def retranslateUi(self, search_bar):
        search_bar.setWindowTitle(QCoreApplication.translate("search_bar", u"Form", None))
        self.label.setText(QCoreApplication.translate("search_bar", u"FullAxis", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("search_bar", u"Buscar usuario", None))
        self.pushButton.setText(QCoreApplication.translate("search_bar", u"Configuraci\u00f3n", None))
    # retranslateUi

