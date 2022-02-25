# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'menu_lateral.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QSizePolicy, QVBoxLayout,
    QWidget)
from resource import resource_rc

class Ui_Lateral_menu(object):
    def setupUi(self, Lateral_menu):
        if not Lateral_menu.objectName():
            Lateral_menu.setObjectName(u"Lateral_menu")
        Lateral_menu.resize(50, 564)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Lateral_menu.sizePolicy().hasHeightForWidth())
        Lateral_menu.setSizePolicy(sizePolicy)
        Lateral_menu.setMinimumSize(QSize(50, 0))
        Lateral_menu.setMaximumSize(QSize(50, 16777215))
        self.verticalLayout_2 = QVBoxLayout(Lateral_menu)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.back_frame = QFrame(Lateral_menu)
        self.back_frame.setObjectName(u"back_frame")
        self.back_frame.setStyleSheet(u"")
        self.layerBack_frame = QVBoxLayout(self.back_frame)
        self.layerBack_frame.setSpacing(0)
        self.layerBack_frame.setObjectName(u"layerBack_frame")
        self.layerBack_frame.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_2.addWidget(self.back_frame)


        self.retranslateUi(Lateral_menu)

        QMetaObject.connectSlotsByName(Lateral_menu)
    # setupUi

    def retranslateUi(self, Lateral_menu):
        Lateral_menu.setWindowTitle(QCoreApplication.translate("Lateral_menu", u"Form", None))
    # retranslateUi

