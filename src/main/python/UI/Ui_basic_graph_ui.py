# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'basic_graph.ui'
##
## Created by: Qt User Interface Compiler version 6.4.3
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
from PySide6.QtWidgets import (QApplication, QSizePolicy, QVBoxLayout, QWidget)

class Ui_graph(object):
    def setupUi(self, graph):
        if not graph.objectName():
            graph.setObjectName(u"graph")
        graph.resize(865, 622)
        self.verticalLayout_4 = QVBoxLayout(graph)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.widget_graph_principal = QWidget(graph)
        self.widget_graph_principal.setObjectName(u"widget_graph_principal")
        self.layout_graph_principal = QVBoxLayout(self.widget_graph_principal)
        self.layout_graph_principal.setSpacing(3)
        self.layout_graph_principal.setObjectName(u"layout_graph_principal")
        self.layout_graph_principal.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_4.addWidget(self.widget_graph_principal)


        self.retranslateUi(graph)

        QMetaObject.connectSlotsByName(graph)
    # setupUi

    def retranslateUi(self, graph):
        graph.setWindowTitle(QCoreApplication.translate("graph", u"Form", None))
    # retranslateUi

