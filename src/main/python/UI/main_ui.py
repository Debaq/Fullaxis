# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
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
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 492)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background-color: rgb(61, 64, 77)\n"
"")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(2, 0, 2, 2)
        self.frame_win_bar = QFrame(self.centralwidget)
        self.frame_win_bar.setObjectName(u"frame_win_bar")
        self.frame_win_bar.setMinimumSize(QSize(0, 40))
        self.frame_win_bar.setMaximumSize(QSize(16777215, 40))
        self.frame_win_bar.setStyleSheet(u"QFrame{background-color: rgb(61, 64, 77)}\n"
"\n"
"QPushButton{\n"
"	padding-top: 5px;\n"
"	background-color: rgb(84, 89,105); \n"
"	color:rgb(209,210,214);\n"
"	border:none; \n"
"	border-top-right-radius:5px;\n"
"	border-top-left-radius:5px;\n"
"}\n"
"QPushButton#btn_menu{\n"
"	background-color: rgb(73, 102,153); \n"
"}\n"
"\n"
"QPushButton#btn_min, QPushButton#btn_max{\n"
"	background-color:rgba(81,83,95,0);\n"
"	padding-top: 0px;\n"
"	border:none;\n"
"	border-top-right-radius:0px;\n"
"	border-top-left-radius:0px;\n"
"}\n"
"QPushButton#btn_min:hover, QPushButton#btn_max:hover{background-color:rgb(81,83,95)}\n"
"\n"
"QPushButton#btn_exit{\n"
"	padding-top: 0px;\n"
"	border:none;\n"
"	border-top-right-radius:0px;\n"
"	border-top-left-radius:0px;\n"
"	background-color: rgba(73, 102,153,0);\n"
"}\n"
"QPushButton#btn_exit:hover{background-color: rgb(240, 96,77);}\n"
"QPushButton#btn_new{background-color: rgba(73, 102,153,0);}\n"
"QPushButton:pressed{\n"
"	background-color: rgb(232,232,232); \n"
"	color:rgb(95,145"
                        ",230)\n"
"}\n"
"QPushButton#btn_menu:checked{\n"
"	background-color: rgb(245, 245,245); \n"
"	color:rgb(95,145,230)\n"
"}\n"
"\n"
"QTabBar{\n"
"    border-top: 30px solid #3d404d;\n"
"    background-color: rgb(245,245,245);\n"
"    qproperty-drawBase:0;\n"
"    }\n"
"\n"
"QTabBar::tab {\n"
"    border: 1px solid #3d404d;\n"
"    background: rgb(84,89,105);\n"
"	color:rgb(209,210,214);\n"
"    border-top-left-radius: 5px;\n"
"    border-top-right-radius: 5px;\n"
"    border-bottom : none;\n"
"    padding-left: 5px;\n"
"    padding-right: 5px;\n"
"}\n"
"QTabBar::tab:tear {\n"
"        border-bottom : none;\n"
"        padding: 7 20px;\n"
"}\n"
"QTabBar::tab:selected:active {\n"
"    background: rgb(232,232,232);\n"
"    color:rgb(95,145,230)\n"
"}\n"
"QTabBar::tab:hover{background: rgb(107,114,132);}\n"
"QTabBar::close-button:hover {background: rgb(107,114,132);}")
        self.horizontalLayout = QHBoxLayout(self.frame_win_bar)
        self.horizontalLayout.setSpacing(2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(2, 5, 0, 0)
        self.layotu_btn_tabs = QHBoxLayout()
        self.layotu_btn_tabs.setObjectName(u"layotu_btn_tabs")
        self.layotu_btn_tabs.setContentsMargins(0, -1, -1, -1)
        self.btn_menu = QPushButton(self.frame_win_bar)
        self.btn_menu.setObjectName(u"btn_menu")
        self.btn_menu.setEnabled(False)
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
        self.btn_min.setMinimumSize(QSize(30, 40))
        font = QFont()
        font.setFamilies([u"Noto Rashi Hebrew Thin"])
        font.setPointSize(16)
        self.btn_min.setFont(font)

        self.horizontalLayout.addWidget(self.btn_min)

        self.btn_max = QPushButton(self.frame_win_bar)
        self.btn_max.setObjectName(u"btn_max")
        self.btn_max.setMinimumSize(QSize(30, 40))
        self.btn_max.setMaximumSize(QSize(20, 40))
        font1 = QFont()
        font1.setFamilies([u"Noto Rashi Hebrew Thin"])
        font1.setPointSize(16)
        font1.setBold(False)
        self.btn_max.setFont(font1)
        self.btn_max.setLayoutDirection(Qt.LeftToRight)
        self.btn_max.setFlat(True)

        self.horizontalLayout.addWidget(self.btn_max)

        self.btn_exit = QPushButton(self.frame_win_bar)
        self.btn_exit.setObjectName(u"btn_exit")
        self.btn_exit.setMinimumSize(QSize(30, 40))
        self.btn_exit.setMaximumSize(QSize(20, 40))
        self.btn_exit.setFont(font)
        self.btn_exit.setFlat(True)

        self.horizontalLayout.addWidget(self.btn_exit)


        self.verticalLayout.addWidget(self.frame_win_bar)

        self.frame_menu = QFrame(self.centralwidget)
        self.frame_menu.setObjectName(u"frame_menu")
        self.frame_menu.setMinimumSize(QSize(0, 58))
        self.frame_menu.setMaximumSize(QSize(16777215, 58))
        self.frame_menu.setStyleSheet(u"background-color: rgb(245,245,245); \n"
"")
        self.layout_menu = QHBoxLayout(self.frame_menu)
        self.layout_menu.setSpacing(0)
        self.layout_menu.setObjectName(u"layout_menu")
        self.layout_menu.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout.addWidget(self.frame_menu)

        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background-color: rgb(245,245,245); \n"
"")
        self.layout_central = QHBoxLayout(self.frame)
        self.layout_central.setSpacing(0)
        self.layout_central.setObjectName(u"layout_central")
        self.layout_central.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btn_menu.setText(QCoreApplication.translate("MainWindow", u" FullAxis ", None))
        self.btn_new.setText(QCoreApplication.translate("MainWindow", u" + Nueva Prueba ", None))
        self.btn_min.setText(QCoreApplication.translate("MainWindow", u"\u2014", None))
        self.btn_max.setText(QCoreApplication.translate("MainWindow", u"\u25a1", None))
        self.btn_exit.setText(QCoreApplication.translate("MainWindow", u"X", None))
    # retranslateUi

