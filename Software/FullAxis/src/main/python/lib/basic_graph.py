# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'basic_graph.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGroupBox, QHBoxLayout,
    QHeaderView, QPushButton, QSizePolicy, QTableWidget,
    QTableWidgetItem, QToolButton, QVBoxLayout, QWidget)

class Ui_graph(object):
    def setupUi(self, graph):
        if not graph.objectName():
            graph.setObjectName(u"graph")
        graph.resize(865, 622)
        self.verticalLayout_4 = QVBoxLayout(graph)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalFrame_3 = QFrame(graph)
        self.horizontalFrame_3.setObjectName(u"horizontalFrame_3")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.horizontalFrame_3.sizePolicy().hasHeightForWidth())
        self.horizontalFrame_3.setSizePolicy(sizePolicy)
        self.horizontalFrame_3.setMaximumSize(QSize(16777215, 90))
        self.horizontalLayout_3 = QHBoxLayout(self.horizontalFrame_3)
        self.horizontalLayout_3.setSpacing(3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(3)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalGroupBox = QGroupBox(self.horizontalFrame_3)
        self.horizontalGroupBox.setObjectName(u"horizontalGroupBox")
        self.horizontalGroupBox.setMaximumSize(QSize(300, 25))
        self.horizontalLayout = QHBoxLayout(self.horizontalGroupBox)
        self.horizontalLayout.setSpacing(3)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.pushButton_2 = QPushButton(self.horizontalGroupBox)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.horizontalLayout.addWidget(self.pushButton_2)

        self.pushButton_3 = QPushButton(self.horizontalGroupBox)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.horizontalLayout.addWidget(self.pushButton_3)

        self.pushButton = QPushButton(self.horizontalGroupBox)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout.addWidget(self.pushButton)

        self.toolButton = QToolButton(self.horizontalGroupBox)
        self.toolButton.setObjectName(u"toolButton")

        self.horizontalLayout.addWidget(self.toolButton)


        self.verticalLayout.addWidget(self.horizontalGroupBox)

        self.tableWidget = QTableWidget(self.horizontalFrame_3)
        self.tableWidget.setObjectName(u"tableWidget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy1)
        self.tableWidget.setMaximumSize(QSize(300, 16777215))

        self.verticalLayout.addWidget(self.tableWidget)


        self.horizontalLayout_3.addLayout(self.verticalLayout)

        self.widget_graph_detail = QFrame(self.horizontalFrame_3)
        self.widget_graph_detail.setObjectName(u"widget_graph_detail")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.widget_graph_detail.sizePolicy().hasHeightForWidth())
        self.widget_graph_detail.setSizePolicy(sizePolicy2)
        self.widget_graph_detail.setMinimumSize(QSize(300, 0))
        self.verticalLayout_2 = QVBoxLayout(self.widget_graph_detail)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_3.addWidget(self.widget_graph_detail)


        self.verticalLayout_4.addWidget(self.horizontalFrame_3)

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
        self.pushButton_2.setText(QCoreApplication.translate("graph", u"PushButton", None))
        self.pushButton_3.setText(QCoreApplication.translate("graph", u"PushButton", None))
        self.pushButton.setText(QCoreApplication.translate("graph", u"PushButton", None))
        self.toolButton.setText(QCoreApplication.translate("graph", u"...", None))
    # retranslateUi

