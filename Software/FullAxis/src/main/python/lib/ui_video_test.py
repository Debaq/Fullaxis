# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'video_testFrisdG.ui'
##
## Created by: Qt User Interface Compiler version 6.3.0
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_VNG_test(object):
    def setupUi(self, VNG_test):
        if not VNG_test.objectName():
            VNG_test.setObjectName(u"VNG_test")
        VNG_test.resize(896, 579)
        self.verticalLayout_2 = QVBoxLayout(VNG_test)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.video_layout = QHBoxLayout()
        self.video_layout.setObjectName(u"video_layout")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")

        self.video_layout.addLayout(self.verticalLayout_3)


        self.verticalLayout_2.addLayout(self.video_layout)

        self.graph_layout = QVBoxLayout()
        self.graph_layout.setObjectName(u"graph_layout")

        self.verticalLayout_2.addLayout(self.graph_layout)


        self.retranslateUi(VNG_test)

        QMetaObject.connectSlotsByName(VNG_test)
    # setupUi

    def retranslateUi(self, VNG_test):
        VNG_test.setWindowTitle(QCoreApplication.translate("VNG_test", u"Form", None))
    # retranslateUi

