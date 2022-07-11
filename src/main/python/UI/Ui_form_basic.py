# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form_basic.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_from_basic(object):
    def setupUi(self, from_basic):
        if not from_basic.objectName():
            from_basic.setObjectName(u"from_basic")
        from_basic.resize(400, 300)
        self.verticalLayout_2 = QVBoxLayout(from_basic)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalWidget = QWidget(from_basic)
        self.verticalWidget.setObjectName(u"verticalWidget")
        self.verticalWidget.setMinimumSize(QSize(0, 58))
        self.verticalWidget.setMaximumSize(QSize(16777215, 58))
        self.verticalWidget.setStyleSheet(u"background-color: rgb(245, 245, 245);\n"
"\n"
"")
        self.verticalLayout = QVBoxLayout(self.verticalWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")

        self.verticalLayout_2.addWidget(self.verticalWidget)

        self.horizontalWidget = QWidget(from_basic)
        self.horizontalWidget.setObjectName(u"horizontalWidget")
        self.horizontalWidget.setMinimumSize(QSize(0, 30))
        self.horizontalWidget.setMaximumSize(QSize(16777215, 30))
        self.horizontalWidget.setStyleSheet(u"background-color: qlineargradient(spread:reflect, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 rgba(229, 232, 236, 255), stop:1 rgba(245, 245, 245, 255));\n"
"\n"
"")
        self.horizontalLayout = QHBoxLayout(self.horizontalWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")

        self.verticalLayout_2.addWidget(self.horizontalWidget)

        self.horizontalFrame_2 = QFrame(from_basic)
        self.horizontalFrame_2.setObjectName(u"horizontalFrame_2")
        self.horizontalFrame_2.setStyleSheet(u"background-color: rgb(245, 245, 245);\n"
"\n"
"")
        self.horizontalLayout_2 = QHBoxLayout(self.horizontalFrame_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")

        self.verticalLayout_2.addWidget(self.horizontalFrame_2)


        self.retranslateUi(from_basic)

        QMetaObject.connectSlotsByName(from_basic)
    # setupUi

    def retranslateUi(self, from_basic):
        from_basic.setWindowTitle(QCoreApplication.translate("from_basic", u"Form", None))
    # retranslateUi

