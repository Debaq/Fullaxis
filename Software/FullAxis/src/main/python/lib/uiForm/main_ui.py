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
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QMainWindow, QMenu, QMenuBar, QPushButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)
from resource import resource_rc

class Ui_FullAxis(object):
    def setupUi(self, FullAxis):
        if not FullAxis.objectName():
            FullAxis.setObjectName(u"FullAxis")
        FullAxis.resize(1000, 700)
        FullAxis.setMinimumSize(QSize(1000, 700))
        self.actionPreferences = QAction(FullAxis)
        self.actionPreferences.setObjectName(u"actionPreferences")
        font = QFont()
        font.setPointSize(9)
        self.actionPreferences.setFont(font)
        self.actionQuit = QAction(FullAxis)
        self.actionQuit.setObjectName(u"actionQuit")
        self.actionQuit.setFont(font)
        self.actionOnline_Documentation = QAction(FullAxis)
        self.actionOnline_Documentation.setObjectName(u"actionOnline_Documentation")
        self.actionOnline_Documentation.setFont(font)
        self.actionlog_view = QAction(FullAxis)
        self.actionlog_view.setObjectName(u"actionlog_view")
        self.actionlog_view.setFont(font)
        self.actionAbout = QAction(FullAxis)
        self.actionAbout.setObjectName(u"actionAbout")
        self.actionAbout.setFont(font)
        self.centralwidget = QWidget(FullAxis)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalFrame = QFrame(self.centralwidget)
        self.horizontalFrame.setObjectName(u"horizontalFrame")
        self.horizontalFrame.setMinimumSize(QSize(0, 50))
        self.horizontalFrame.setMaximumSize(QSize(16777215, 50))
        self.horizontalFrame.setStyleSheet(u"border-bottom: 3px rgb(136, 138, 133); \n"
"")
        self.horizontalFrame.setFrameShape(QFrame.NoFrame)
        self.horizontalLayout = QHBoxLayout(self.horizontalFrame)
        self.horizontalLayout.setSpacing(100)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(20, -1, -1, -1)
        self.label = QLabel(self.horizontalFrame)
        self.label.setObjectName(u"label")
        self.label.setPixmap(QPixmap(u":/icons svg/icons/png/logo_wName.png"))

        self.horizontalLayout_4.addWidget(self.label)


        self.horizontalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.Login_Layout = QHBoxLayout()
        self.Login_Layout.setObjectName(u"Login_Layout")
        self.Login_Layout.setContentsMargins(20, -1, 20, -1)
        self.btn_login = QPushButton(self.horizontalFrame)
        self.btn_login.setObjectName(u"btn_login")
        sizePolicy = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_login.sizePolicy().hasHeightForWidth())
        self.btn_login.setSizePolicy(sizePolicy)
        self.btn_login.setMinimumSize(QSize(0, 30))
        self.btn_login.setMaximumSize(QSize(200, 16777215))
        self.btn_login.setStyleSheet(u"    QPushButton {\n"
"       Text-align:center;\n"
"       border: none;\n"
"       color:rgb(238, 238, 236);\n"
"	   background-color: rgb(55, 144, 152);\n"
"\n"
"    }\n"
"    QPushButton:hover {\n"
"	background-color: rgb(0, 98, 106);\n"
"    }\n"
"    QPushButton:pressed {\n"
"  text-decoration: underline;\n"
"\n"
"    }\n"
"")

        self.Login_Layout.addWidget(self.btn_login)


        self.horizontalLayout.addLayout(self.Login_Layout)


        self.verticalLayout.addWidget(self.horizontalFrame)

        self.Frame_center_root = QFrame(self.centralwidget)
        self.Frame_center_root.setObjectName(u"Frame_center_root")
        self.Center_Layout_root = QHBoxLayout(self.Frame_center_root)
        self.Center_Layout_root.setSpacing(0)
        self.Center_Layout_root.setObjectName(u"Center_Layout_root")
        self.Center_Layout_root.setContentsMargins(0, 0, 0, 0)
        self.Fame_lateral = QFrame(self.Frame_center_root)
        self.Fame_lateral.setObjectName(u"Fame_lateral")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.Fame_lateral.sizePolicy().hasHeightForWidth())
        self.Fame_lateral.setSizePolicy(sizePolicy1)
        self.Lateral_layout = QVBoxLayout(self.Fame_lateral)
        self.Lateral_layout.setSpacing(0)
        self.Lateral_layout.setObjectName(u"Lateral_layout")
        self.Lateral_layout.setContentsMargins(0, 0, 0, 0)

        self.Center_Layout_root.addWidget(self.Fame_lateral)

        self.Frame_center = QFrame(self.Frame_center_root)
        self.Frame_center.setObjectName(u"Frame_center")
        self.Center_layout = QHBoxLayout(self.Frame_center)
        self.Center_layout.setSpacing(0)
        self.Center_layout.setObjectName(u"Center_layout")
        self.Center_layout.setContentsMargins(0, 0, 0, 0)

        self.Center_Layout_root.addWidget(self.Frame_center)


        self.verticalLayout.addWidget(self.Frame_center_root)

        self.Frame_info = QFrame(self.centralwidget)
        self.Frame_info.setObjectName(u"Frame_info")
        self.Frame_info.setMaximumSize(QSize(16777215, 30))
        self.layout_info = QHBoxLayout(self.Frame_info)
        self.layout_info.setObjectName(u"layout_info")

        self.verticalLayout.addWidget(self.Frame_info)

        FullAxis.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(FullAxis)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1000, 32))
        self.menubar.setFont(font)
        self.menubar.setStyleSheet(u"background-color: rgb(238, 238, 236);")
        self.menufile = QMenu(self.menubar)
        self.menufile.setObjectName(u"menufile")
        self.menufile.setFont(font)
        self.menuhelp = QMenu(self.menubar)
        self.menuhelp.setObjectName(u"menuhelp")
        self.menuhelp.setStyleSheet(u"background-color: rgb(238, 238, 236);")
        FullAxis.setMenuBar(self.menubar)

        self.menubar.addAction(self.menufile.menuAction())
        self.menubar.addAction(self.menuhelp.menuAction())
        self.menufile.addAction(self.actionPreferences)
        self.menufile.addAction(self.actionQuit)
        self.menuhelp.addAction(self.actionOnline_Documentation)
        self.menuhelp.addAction(self.actionlog_view)
        self.menuhelp.addSeparator()
        self.menuhelp.addAction(self.actionAbout)

        self.retranslateUi(FullAxis)

        QMetaObject.connectSlotsByName(FullAxis)
    # setupUi

    def retranslateUi(self, FullAxis):
        FullAxis.setWindowTitle(QCoreApplication.translate("FullAxis", u"FullAxis", None))
        self.actionPreferences.setText(QCoreApplication.translate("FullAxis", u"Preferencias", None))
        self.actionQuit.setText(QCoreApplication.translate("FullAxis", u"Salir", None))
        self.actionOnline_Documentation.setText(QCoreApplication.translate("FullAxis", u"Online Documentation", None))
        self.actionlog_view.setText(QCoreApplication.translate("FullAxis", u"Logview", None))
        self.actionAbout.setText(QCoreApplication.translate("FullAxis", u"Sobre nosotros", None))
        self.label.setText("")
        self.btn_login.setText(QCoreApplication.translate("FullAxis", u"Ingresar a la cuenta", None))
        self.menufile.setTitle(QCoreApplication.translate("FullAxis", u"Archivo", None))
        self.menuhelp.setTitle(QCoreApplication.translate("FullAxis", u"Ayuda", None))
    # retranslateUi

