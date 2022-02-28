# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'basic_TUG.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QHeaderView, QPushButton,
    QSizePolicy, QTableWidget, QTableWidgetItem, QToolButton,
    QVBoxLayout, QWidget)

class Ui_TUG(object):
    def setupUi(self, TUG):
        if not TUG.objectName():
            TUG.setObjectName(u"TUG")
        TUG.resize(636, 498)
        self.verticalLayout_2 = QVBoxLayout(TUG)
        self.verticalLayout_2.setSpacing(3)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, -1, -1, -1)
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.pushButton_2 = QPushButton(TUG)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMaximumSize(QSize(16777215, 25))

        self.horizontalLayout_2.addWidget(self.pushButton_2)

        self.pushButton_3 = QPushButton(TUG)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setMaximumSize(QSize(16777215, 25))

        self.horizontalLayout_2.addWidget(self.pushButton_3)

        self.pushButton = QPushButton(TUG)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMaximumSize(QSize(16777215, 25))

        self.horizontalLayout_2.addWidget(self.pushButton)

        self.toolButton = QToolButton(TUG)
        self.toolButton.setObjectName(u"toolButton")
        self.toolButton.setMaximumSize(QSize(16777215, 26))

        self.horizontalLayout_2.addWidget(self.toolButton)


        self.verticalLayout_4.addLayout(self.horizontalLayout_2)

        self.tableWidget = QTableWidget(TUG)
        if (self.tableWidget.columnCount() < 2):
            self.tableWidget.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        self.tableWidget.setObjectName(u"tableWidget")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        self.tableWidget.setMaximumSize(QSize(16777215, 50))

        self.verticalLayout_4.addWidget(self.tableWidget)


        self.horizontalLayout.addLayout(self.verticalLayout_4)

        self.layout_detail = QVBoxLayout()
        self.layout_detail.setObjectName(u"layout_detail")

        self.horizontalLayout.addLayout(self.layout_detail)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.verticalWidget = QWidget(TUG)
        self.verticalWidget.setObjectName(u"verticalWidget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.verticalWidget.sizePolicy().hasHeightForWidth())
        self.verticalWidget.setSizePolicy(sizePolicy1)
        self.layout_test_TUG = QVBoxLayout(self.verticalWidget)
        self.layout_test_TUG.setSpacing(0)
        self.layout_test_TUG.setObjectName(u"layout_test_TUG")

        self.verticalLayout_2.addWidget(self.verticalWidget)


        self.retranslateUi(TUG)

        QMetaObject.connectSlotsByName(TUG)
    # setupUi

    def retranslateUi(self, TUG):
        TUG.setWindowTitle(QCoreApplication.translate("TUG", u"Form", None))
        self.pushButton_2.setText(QCoreApplication.translate("TUG", u"PushButton", None))
        self.pushButton_3.setText(QCoreApplication.translate("TUG", u"PushButton", None))
        self.pushButton.setText(QCoreApplication.translate("TUG", u"PushButton", None))
        self.toolButton.setText(QCoreApplication.translate("TUG", u"...", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("TUG", u"Name Variable", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("TUG", u"Variable", None));
    # retranslateUi

