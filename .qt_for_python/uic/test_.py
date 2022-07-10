# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'test_.ui'
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

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(400, 300)
        Form.setStyleSheet(u"background-color: rgb(245, 245, 245);\n"
"")
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_gradient_0 = QFrame(Form)
        self.frame_gradient_0.setObjectName(u"frame_gradient_0")
        self.frame_gradient_0.setMinimumSize(QSize(0, 30))
        self.frame_gradient_0.setMaximumSize(QSize(16777215, 30))
        self.frame_gradient_0.setStyleSheet(u"background-color: qlineargradient(spread:reflect, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 rgba(229, 232, 236, 255), stop:1 rgba(245, 245, 245, 255));\n"
"\n"
"")
        self.frame_gradient_0.setFrameShape(QFrame.NoFrame)
        self.frame_gradient_0.setFrameShadow(QFrame.Plain)
        self.frame_gradient_0.setLineWidth(0)

        self.verticalLayout.addWidget(self.frame_gradient_0)

        self.frame_central = QFrame(Form)
        self.frame_central.setObjectName(u"frame_central")
        self.horizontalLayout = QHBoxLayout(self.frame_central)
        self.horizontalLayout.setObjectName(u"horizontalLayout")

        self.verticalLayout.addWidget(self.frame_central)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
    # retranslateUi

