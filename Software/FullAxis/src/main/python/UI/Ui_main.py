# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QMainWindow,
    QPushButton, QSizePolicy, QSpacerItem, QStatusBar,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background-color: rgb(245, 245, 245);")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, -1)
        self.frame_win_bar = QFrame(self.centralwidget)
        self.frame_win_bar.setObjectName(u"frame_win_bar")
        self.frame_win_bar.setMinimumSize(QSize(0, 30))
        self.frame_win_bar.setMaximumSize(QSize(16777215, 30))
        self.frame_win_bar.setStyleSheet(u"QFrame{background-color: rgb(61, 64, 7)}\n"
"\n"
"QTabBar{\n"
"	padding-top: 5px;\n"
"padding-bottom: 20px;\n"
"	background-color: rgb(84, 89,105); \n"
"	color:rgb(209,210,214);\n"
"	border:none; \n"
"	border-top-right-radius:5px;\n"
"	border-top-left-radius:5px;\n"
"	qproperty-drawBase: 0;\n"
"}\n"
"QPushButton{\n"
"	padding-top: 5px;\n"
"padding-bottom: 10px;\n"
"	background-color: rgb(84, 89,105); \n"
"	color:rgb(209,210,214);\n"
"	border:none; \n"
"	border-top-right-radius:5px;\n"
"	border-top-left-radius:5px;\n"
"}\n"
"QPushButton#btn_menu{\n"
"	background-color: rgb(73, 102,153); \n"
"}\n"
"QPushButton#btn_min{background-color: rgba(73, 102,153,0);}\n"
"QPushButton#btn_exit{background-color: rgba(73, 102,153,0);}\n"
"QPushButton#btn_new{background-color: rgba(73, 102,153,0);}\n"
"\n"
"QPushButton:pressed{\n"
"	background-color: rgb(232,232,232); \n"
"	color:rgb(95,145,230)\n"
"}\n"
"QPushButton#btn_menu:checked{\n"
"	background-color: rgb(245, 245,245); \n"
"	color:rgb(95,145,230)\n"
"}")
        self.horizontalLayout = QHBoxLayout(self.frame_win_bar)
        self.horizontalLayout.setSpacing(1)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, -1, -1, 0)
        self.layotu_btn_tabs = QHBoxLayout()
        self.layotu_btn_tabs.setObjectName(u"layotu_btn_tabs")
        self.layotu_btn_tabs.setContentsMargins(5, -1, -1, -1)
        self.btn_menu = QPushButton(self.frame_win_bar)
        self.btn_menu.setObjectName(u"btn_menu")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_menu.sizePolicy().hasHeightForWidth())
        self.btn_menu.setSizePolicy(sizePolicy)
        self.btn_menu.setMinimumSize(QSize(0, 25))
        self.btn_menu.setCheckable(True)
        self.btn_menu.setChecked(True)
        self.btn_menu.setFlat(False)

        self.layotu_btn_tabs.addWidget(self.btn_menu)

        self.btn_new = QPushButton(self.frame_win_bar)
        self.btn_new.setObjectName(u"btn_new")
        self.btn_new.setMinimumSize(QSize(0, 25))
        self.btn_new.setFlat(False)

        self.layotu_btn_tabs.addWidget(self.btn_new)


        self.horizontalLayout.addLayout(self.layotu_btn_tabs)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.btn_min = QPushButton(self.frame_win_bar)
        self.btn_min.setObjectName(u"btn_min")
        self.btn_min.setMinimumSize(QSize(20, 20))
        self.btn_min.setMaximumSize(QSize(20, 20))
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.btn_min.setFont(font)
        self.btn_min.setLayoutDirection(Qt.LeftToRight)
        self.btn_min.setFlat(True)

        self.horizontalLayout.addWidget(self.btn_min)

        self.btn_exit = QPushButton(self.frame_win_bar)
        self.btn_exit.setObjectName(u"btn_exit")
        self.btn_exit.setMinimumSize(QSize(20, 20))
        self.btn_exit.setMaximumSize(QSize(20, 20))
        font1 = QFont()
        font1.setBold(True)
        self.btn_exit.setFont(font1)
        self.btn_exit.setFlat(True)

        self.horizontalLayout.addWidget(self.btn_exit)


        self.verticalLayout.addWidget(self.frame_win_bar)

        self.frame_menu = QFrame(self.centralwidget)
        self.frame_menu.setObjectName(u"frame_menu")
        self.frame_menu.setMinimumSize(QSize(0, 58))
        self.frame_menu.setMaximumSize(QSize(16777215, 58))
        self.frame_menu.setStyleSheet(u"background-color: rgb(245, 245, 245);")
        self.layout_menu = QHBoxLayout(self.frame_menu)
        self.layout_menu.setObjectName(u"layout_menu")
        self.layout_menu.setContentsMargins(0, 0, 0, -1)

        self.verticalLayout.addWidget(self.frame_menu)

        self.layout_central = QHBoxLayout()
        self.layout_central.setObjectName(u"layout_central")

        self.verticalLayout.addLayout(self.layout_central)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btn_menu.setText(QCoreApplication.translate("MainWindow", u" FullAxis ", None))
        self.btn_new.setText(QCoreApplication.translate("MainWindow", u" + Nueva Prueba ", None))
        self.btn_min.setText(QCoreApplication.translate("MainWindow", u"_", None))
        self.btn_exit.setText(QCoreApplication.translate("MainWindow", u"X", None))
    # retranslateUi

