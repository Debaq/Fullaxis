# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main2.ui'
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
from PySide6.QtWidgets import (QApplication, QMainWindow, QSizePolicy, QTabWidget,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet(u"background-color: rgb(61, 64, 77)\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"QTabWidget::tab-bar {\n"
"    left: 5px; /* move to the right by 5px */\n"
"}\n"
"QTabBar::tab {\n"
"		padding:5 5px;\n"
"		background-color: rgb(84, 89,105); \n"
"		color:rgb(209,210,214);\n"
"		border-left:2 solid rgb(61, 64, 77);\n"
"		border-top-right-radius:5px;\n"
"		border-top-left-radius:5px;\n"
"}\n"
"QTabBar::tab:first {\n"
"	background-color: rgb(73, 102,153); \n"
"\n"
"}\n"
"QTabBar::tab:selected{\n"
"	background-color: rgb(245, 245,245); \n"
"	color:rgb(95,145,230)\n"
"}\n"
"QTabBar::tab:first:selected{\n"
"	background-color: rgb(245, 245,245); \n"
"	color:rgb(95,145,230)\n"
"}\n"
"QTabBar::tab:hover{background: rgb(107,114,132);}\n"
"\n"
"/*background-color: rgb(245,245,245); */\n"
"")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(3)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(3, 8, 3, 3)
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setDocumentMode(True)
        self.tabWidget.setTabsClosable(False)
        self.main_tab = QWidget()
        self.main_tab.setObjectName(u"main_tab")
        self.main_layout = QVBoxLayout(self.main_tab)
        self.main_layout.setSpacing(0)
        self.main_layout.setObjectName(u"main_layout")
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.tabWidget.addTab(self.main_tab, "")

        self.verticalLayout.addWidget(self.tabWidget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.main_tab), QCoreApplication.translate("MainWindow", u"FullAxis", None))
    # retranslateUi

