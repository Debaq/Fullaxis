# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'windows_principal.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QListView,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_win_principal(object):
    def setupUi(self, win_principal):
        if not win_principal.objectName():
            win_principal.setObjectName(u"win_principal")
        win_principal.resize(670, 455)
        win_principal.setStyleSheet(u"")
        self.horizontalLayout = QHBoxLayout(win_principal)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_gradient = QFrame(win_principal)
        self.frame_gradient.setObjectName(u"frame_gradient")
        self.frame_gradient.setFrameShape(QFrame.StyledPanel)
        self.frame_gradient.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_gradient)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalWidget_3 = QWidget(self.frame_gradient)
        self.verticalWidget_3.setObjectName(u"verticalWidget_3")
        self.verticalWidget_3.setMinimumSize(QSize(55, 0))
        self.verticalWidget_3.setMaximumSize(QSize(55, 16777215))
        self.verticalLayout_4 = QVBoxLayout(self.verticalWidget_3)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.frame_butons = QFrame(self.verticalWidget_3)
        self.frame_butons.setObjectName(u"frame_butons")
        self.frame_butons.setMinimumSize(QSize(50, 0))
        self.frame_butons.setMaximumSize(QSize(50, 16777215))
        self.verticalLayout_2 = QVBoxLayout(self.frame_butons)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.pushButton = QPushButton(self.frame_butons)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(50, 50))
        self.pushButton.setMaximumSize(QSize(50, 50))
        self.pushButton.setFlat(True)

        self.verticalLayout_2.addWidget(self.pushButton)

        self.pushButton_3 = QPushButton(self.frame_butons)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setMinimumSize(QSize(50, 50))
        self.pushButton_3.setMaximumSize(QSize(50, 50))
        self.pushButton_3.setFlat(True)

        self.verticalLayout_2.addWidget(self.pushButton_3)

        self.pushButton_2 = QPushButton(self.frame_butons)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(50, 50))
        self.pushButton_2.setMaximumSize(QSize(50, 50))
        self.pushButton_2.setFlat(True)

        self.verticalLayout_2.addWidget(self.pushButton_2)


        self.verticalLayout_4.addWidget(self.frame_butons)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer)


        self.horizontalLayout_3.addWidget(self.verticalWidget_3)

        self.verticalFrame = QFrame(self.frame_gradient)
        self.verticalFrame.setObjectName(u"verticalFrame")
        self.verticalFrame.setMinimumSize(QSize(195, 0))
        self.verticalFrame.setMaximumSize(QSize(195, 16777215))
        self.verticalFrame.setStyleSheet(u"border-left-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        self.verticalFrame.setFrameShape(QFrame.NoFrame)
        self.verticalFrame.setFrameShadow(QFrame.Plain)
        self.verticalLayout = QVBoxLayout(self.verticalFrame)
        self.verticalLayout.setObjectName(u"verticalLayout")

        self.horizontalLayout_3.addWidget(self.verticalFrame)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, 0, -1, -1)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.pushButton_4 = QPushButton(self.frame_gradient)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.horizontalLayout_2.addWidget(self.pushButton_4)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.listView = QListView(self.frame_gradient)
        self.listView.setObjectName(u"listView")

        self.verticalLayout_3.addWidget(self.listView)


        self.horizontalLayout_3.addLayout(self.verticalLayout_3)

        self.verticalFrame_4 = QFrame(self.frame_gradient)
        self.verticalFrame_4.setObjectName(u"verticalFrame_4")
        self.verticalFrame_4.setMinimumSize(QSize(100, 0))
        self.verticalFrame_4.setMaximumSize(QSize(100, 16777215))
        self.verticalLayout_5 = QVBoxLayout(self.verticalFrame_4)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")

        self.horizontalLayout_3.addWidget(self.verticalFrame_4)


        self.horizontalLayout.addWidget(self.frame_gradient)


        self.retranslateUi(win_principal)

        QMetaObject.connectSlotsByName(win_principal)
    # setupUi

    def retranslateUi(self, win_principal):
        win_principal.setWindowTitle(QCoreApplication.translate("win_principal", u"Form", None))
        self.pushButton.setText(QCoreApplication.translate("win_principal", u"Nuevo\n"
"Usuario", None))
        self.pushButton_3.setText(QCoreApplication.translate("win_principal", u"Nueva\n"
"Prueba", None))
        self.pushButton_2.setText(QCoreApplication.translate("win_principal", u"Abrir", None))
        self.pushButton_4.setText(QCoreApplication.translate("win_principal", u"Filtro", None))
    # retranslateUi

