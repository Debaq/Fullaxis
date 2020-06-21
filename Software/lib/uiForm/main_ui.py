# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'development/Form/main.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_FullAxis(object):
    def setupUi(self, FullAxis):
        FullAxis.setObjectName("FullAxis")
        FullAxis.resize(1000, 700)
        FullAxis.setMinimumSize(QtCore.QSize(1000, 700))
        self.centralwidget = QtWidgets.QWidget(FullAxis)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalFrame = QtWidgets.QFrame(self.centralwidget)
        self.horizontalFrame.setMinimumSize(QtCore.QSize(0, 50))
        self.horizontalFrame.setMaximumSize(QtCore.QSize(16777215, 50))
        self.horizontalFrame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.horizontalFrame.setObjectName("horizontalFrame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalFrame)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(100)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setContentsMargins(20, -1, -1, -1)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label = QtWidgets.QLabel(self.horizontalFrame)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/icons svg/icons/png/logo_wName.png"))
        self.label.setObjectName("label")
        self.horizontalLayout_4.addWidget(self.label)
        self.horizontalLayout.addLayout(self.horizontalLayout_4)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.Login_Layout = QtWidgets.QHBoxLayout()
        self.Login_Layout.setContentsMargins(20, -1, 20, -1)
        self.Login_Layout.setObjectName("Login_Layout")
        self.btn_login = QtWidgets.QPushButton(self.horizontalFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_login.sizePolicy().hasHeightForWidth())
        self.btn_login.setSizePolicy(sizePolicy)
        self.btn_login.setMinimumSize(QtCore.QSize(0, 30))
        self.btn_login.setMaximumSize(QtCore.QSize(200, 16777215))
        self.btn_login.setStyleSheet("    QPushButton {\n"
"       Text-align:center;\n"
"       border: none;\n"
"       color:rgb(238, 238, 236);\n"
"       background-color: rgb(55, 144, 152);\n"
"\n"
"    }\n"
"    QPushButton:hover {\n"
"    background-color: rgb(0, 98, 106);\n"
"    }\n"
"    QPushButton:pressed {\n"
"  text-decoration: underline;\n"
"\n"
"    }\n"
"")
        self.btn_login.setObjectName("btn_login")
        self.Login_Layout.addWidget(self.btn_login)
        self.horizontalLayout.addLayout(self.Login_Layout)
        self.verticalLayout.addWidget(self.horizontalFrame)
        self.Frame_center = QtWidgets.QFrame(self.centralwidget)
        self.Frame_center.setObjectName("Frame_center")
        self.Center_Layout = QtWidgets.QHBoxLayout(self.Frame_center)
        self.Center_Layout.setSpacing(0)
        self.Center_Layout.setObjectName("Center_Layout")
        self.verticalLayout.addWidget(self.Frame_center)
        self.Frame_info = QtWidgets.QFrame(self.centralwidget)
        self.Frame_info.setMaximumSize(QtCore.QSize(16777215, 30))
        self.Frame_info.setObjectName("Frame_info")
        self.layout_info = QtWidgets.QHBoxLayout(self.Frame_info)
        self.layout_info.setObjectName("layout_info")
        self.verticalLayout.addWidget(self.Frame_info)
        FullAxis.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(FullAxis)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1000, 27))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.menubar.setFont(font)
        self.menubar.setStyleSheet("background-color: rgb(238, 238, 236);")
        self.menubar.setObjectName("menubar")
        self.menufile = QtWidgets.QMenu(self.menubar)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.menufile.setFont(font)
        self.menufile.setObjectName("menufile")
        self.menuhelp = QtWidgets.QMenu(self.menubar)
        self.menuhelp.setStyleSheet("background-color: rgb(238, 238, 236);")
        self.menuhelp.setObjectName("menuhelp")
        FullAxis.setMenuBar(self.menubar)
        self.actionPreferences = QtWidgets.QAction(FullAxis)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.actionPreferences.setFont(font)
        self.actionPreferences.setObjectName("actionPreferences")
        self.actionQuit = QtWidgets.QAction(FullAxis)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.actionQuit.setFont(font)
        self.actionQuit.setObjectName("actionQuit")
        self.actionOnline_Documentation = QtWidgets.QAction(FullAxis)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.actionOnline_Documentation.setFont(font)
        self.actionOnline_Documentation.setObjectName("actionOnline_Documentation")
        self.actionlog_view = QtWidgets.QAction(FullAxis)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.actionlog_view.setFont(font)
        self.actionlog_view.setObjectName("actionlog_view")
        self.actionAbout = QtWidgets.QAction(FullAxis)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.actionAbout.setFont(font)
        self.actionAbout.setObjectName("actionAbout")
        self.menufile.addAction(self.actionPreferences)
        self.menufile.addAction(self.actionQuit)
        self.menuhelp.addAction(self.actionOnline_Documentation)
        self.menuhelp.addAction(self.actionlog_view)
        self.menuhelp.addSeparator()
        self.menuhelp.addAction(self.actionAbout)
        self.menubar.addAction(self.menufile.menuAction())
        self.menubar.addAction(self.menuhelp.menuAction())

        self.retranslateUi(FullAxis)
        QtCore.QMetaObject.connectSlotsByName(FullAxis)

    def retranslateUi(self, FullAxis):
        _translate = QtCore.QCoreApplication.translate
        FullAxis.setWindowTitle(_translate("FullAxis", "FullAxis"))
        self.btn_login.setText(_translate("FullAxis", "Ingresar a la cuenta"))
        self.menufile.setTitle(_translate("FullAxis", "Archivo"))
        self.menuhelp.setTitle(_translate("FullAxis", "Ayuda"))
        self.actionPreferences.setText(_translate("FullAxis", "Preferencias"))
        self.actionQuit.setText(_translate("FullAxis", "Salir"))
        self.actionOnline_Documentation.setText(_translate("FullAxis", "Online Documentation"))
        self.actionlog_view.setText(_translate("FullAxis", "Logview"))
        self.actionAbout.setText(_translate("FullAxis", "Sobre nosotros"))

from resource import resource_rc
