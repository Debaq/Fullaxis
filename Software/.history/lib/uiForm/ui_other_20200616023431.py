# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'homeHgcZXQ.ui'
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

class Ui_HomeWidget(object):
    def setupUi(self, HomeWidget):
        if not HomeWidget.objectName():
            HomeWidget.setObjectName(u"HomeWidget")
        HomeWidget.resize(890, 570)
        self.layoutHomeWidget = QVBoxLayout(HomeWidget)
        self.layoutHomeWidget.setSpacing(0)
        self.layoutHomeWidget.setObjectName(u"layoutHomeWidget")
        self.layoutHomeWidget.setContentsMargins(0, 0, 0, 0)
        self.HW_Header = QFrame(HomeWidget)
        self.HW_Header.setObjectName(u"HW_Header")
        self.HW_Header.setMaximumSize(QSize(16777215, 100))
        self.horizontalLayout_2 = QHBoxLayout(self.HW_Header)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.HW_HeaderLeft = QFrame(self.HW_Header)
        self.HW_HeaderLeft.setObjectName(u"HW_HeaderLeft")
        self.HW_HeaderLeft.setStyleSheet(u"background-color: rgb(237, 0, 0);")
        self.layoutHW_HeaderLeft = QHBoxLayout(self.HW_HeaderLeft)
        self.layoutHW_HeaderLeft.setSpacing(0)
        self.layoutHW_HeaderLeft.setObjectName(u"layoutHW_HeaderLeft")
        self.layoutHW_HeaderLeft.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_2.addWidget(self.HW_HeaderLeft)

        self.HW_HeaderRigth = QFrame(self.HW_Header)
        self.HW_HeaderRigth.setObjectName(u"HW_HeaderRigth")
        self.HW_HeaderRigth.setStyleSheet(u"background-color: rgb(0, 233, 79);")
        self.layoutHW_HeaderRigth = QHBoxLayout(self.HW_HeaderRigth)
        self.layoutHW_HeaderRigth.setSpacing(0)
        self.layoutHW_HeaderRigth.setObjectName(u"layoutHW_HeaderRigth")
        self.layoutHW_HeaderRigth.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_2.addWidget(self.HW_HeaderRigth)


        self.layoutHomeWidget.addWidget(self.HW_Header)

        self.HW_Body = QFrame(HomeWidget)
        self.HW_Body.setObjectName(u"HW_Body")
        self.horizontalLayout = QHBoxLayout(self.HW_Body)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.HW_BodyLeft = QFrame(self.HW_Body)
        self.HW_BodyLeft.setObjectName(u"HW_BodyLeft")
        self.HW_BodyLeft.setStyleSheet(u"background-color: rgb(92, 00, 00);")
        self.layoutHW_BodyLeft = QVBoxLayout(self.HW_BodyLeft)
        self.layoutHW_BodyLeft.setSpacing(0)
        self.layoutHW_BodyLeft.setObjectName(u"layoutHW_BodyLeft")
        self.layoutHW_BodyLeft.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout.addWidget(self.HW_BodyLeft)

        self.HW_BodyRigth = QFrame(self.HW_Body)
        self.HW_BodyRigth.setObjectName(u"HW_BodyRigth")
        self.HW_BodyRigth.setStyleSheet(u"background-color: rgb(00, 00, 110);")
        self.layoutHW_BodyRigth = QVBoxLayout(self.HW_BodyRigth)
        self.layoutHW_BodyRigth.setSpacing(0)
        self.layoutHW_BodyRigth.setObjectName(u"layoutHW_BodyRigth")
        self.layoutHW_BodyRigth.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout.addWidget(self.HW_BodyRigth)


        self.layoutHomeWidget.addWidget(self.HW_Body)


        self.retranslateUi(HomeWidget)

        QMetaObject.connectSlotsByName(HomeWidget)
    # setupUi

    def retranslateUi(self, HomeWidget):
        HomeWidget.setWindowTitle(QCoreApplication.translate("HomeWidget", u"Form", None))
    # retranslateUi

