# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'development/Form/home.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_HomeWidget(object):
    def setupUi(self, HomeWidget):
        HomeWidget.setObjectName("HomeWidget")
        HomeWidget.resize(920, 620)
        self.horizontalLayout = QtWidgets.QHBoxLayout(HomeWidget)
        self.horizontalLayout.setContentsMargins(0, 50, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalFrame = QtWidgets.QFrame(HomeWidget)
        self.horizontalFrame.setMinimumSize(QtCore.QSize(50, 0))
        self.horizontalFrame.setObjectName("horizontalFrame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalFrame)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout.addWidget(self.horizontalFrame)
        self.verticalFrame = QtWidgets.QFrame(HomeWidget)
        self.verticalFrame.setMinimumSize(QtCore.QSize(720, 0))
        self.verticalFrame.setMaximumSize(QtCore.QSize(720, 16777215))
        self.verticalFrame.setObjectName("verticalFrame")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalFrame)
        self.verticalLayout_3.setContentsMargins(-1, 1, -1, -1)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalFrame_4 = QtWidgets.QFrame(self.verticalFrame)
        self.horizontalFrame_4.setMinimumSize(QtCore.QSize(0, 0))
        self.horizontalFrame_4.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.horizontalFrame_4.setObjectName("horizontalFrame_4")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.horizontalFrame_4)
        self.horizontalLayout_10.setContentsMargins(0, -1, -1, -1)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.verticalFrame_2 = QtWidgets.QFrame(self.horizontalFrame_4)
        self.verticalFrame_2.setMinimumSize(QtCore.QSize(270, 0))
        self.verticalFrame_2.setMaximumSize(QtCore.QSize(270, 16777215))
        self.verticalFrame_2.setObjectName("verticalFrame_2")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.verticalFrame_2)
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.verticalFrame_3 = QtWidgets.QFrame(self.verticalFrame_2)
        self.verticalFrame_3.setMinimumSize(QtCore.QSize(260, 150))
        self.verticalFrame_3.setMaximumSize(QtCore.QSize(16777215, 160))
        self.verticalFrame_3.setObjectName("verticalFrame_3")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.verticalFrame_3)
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.horizontalFrame_5 = QtWidgets.QFrame(self.verticalFrame_3)
        self.horizontalFrame_5.setMaximumSize(QtCore.QSize(16777215, 40))
        self.horizontalFrame_5.setObjectName("horizontalFrame_5")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout(self.horizontalFrame_5)
        self.horizontalLayout_13.setSpacing(6)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.label_4 = QtWidgets.QLabel(self.horizontalFrame_5)
        self.label_4.setMaximumSize(QtCore.QSize(24, 24))
        self.label_4.setStyleSheet("background: transparent;\n"
"background-position: center;\n"
"background-image: url(:/icons_white/icons/png/16x16/cil-home.png);\n"
"background-repeat: no-repeat;")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_13.addWidget(self.label_4)
        self.label_5 = QtWidgets.QLabel(self.horizontalFrame_5)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("background: transparent;\n"
"color:rgb(204,204,204);")
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_13.addWidget(self.label_5)
        self.verticalLayout_12.addWidget(self.horizontalFrame_5)
        self.verticalFrame_7 = QtWidgets.QFrame(self.verticalFrame_3)
        self.verticalFrame_7.setObjectName("verticalFrame_7")
        self.verticalLayout_16 = QtWidgets.QVBoxLayout(self.verticalFrame_7)
        self.verticalLayout_16.setContentsMargins(29, -1, -1, -1)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.btn_newregister = QtWidgets.QPushButton(self.verticalFrame_7)
        self.btn_newregister.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.btn_newregister.setStyleSheet("QPushButton {\n"
"    Text-align:left;\n"
"    background: transparent;\n"
"    color:rgb(54,114,240);\n"
"    border: none;\n"
"}\n"
"QPushButton:hover {\n"
"    color:rgb(54,156,240);\n"
"}\n"
"QPushButton:pressed {    \n"
"    color:rgb(35,187,255);\n"
"\n"
"}")
        self.btn_newregister.setObjectName("btn_newregister")
        self.verticalLayout_16.addWidget(self.btn_newregister)
        self.btn_openReg = QtWidgets.QPushButton(self.verticalFrame_7)
        self.btn_openReg.setStyleSheet("QPushButton {\n"
"    Text-align:left;\n"
"    background: transparent;\n"
"    color:rgb(54,114,240);\n"
"    border: none;\n"
"}\n"
"QPushButton:hover {\n"
"    color:rgb(54,156,240);\n"
"}\n"
"QPushButton:pressed {    \n"
"    color:rgb(35,187,255);\n"
"\n"
"}")
        self.btn_openReg.setObjectName("btn_openReg")
        self.verticalLayout_16.addWidget(self.btn_openReg)
        self.btn_newProt = QtWidgets.QPushButton(self.verticalFrame_7)
        self.btn_newProt.setStyleSheet("QPushButton {\n"
"    Text-align:left;\n"
"    background: transparent;\n"
"    color:rgb(54,114,240);\n"
"    border: none;\n"
"}\n"
"QPushButton:hover {\n"
"    color:rgb(54,156,240);\n"
"}\n"
"QPushButton:pressed {    \n"
"    color:rgb(35,187,255);\n"
"\n"
"}")
        self.btn_newProt.setObjectName("btn_newProt")
        self.verticalLayout_16.addWidget(self.btn_newProt)
        self.btn_toXforfaxy = QtWidgets.QPushButton(self.verticalFrame_7)
        self.btn_toXforfaxy.setStyleSheet("QPushButton {\n"
"    Text-align:left;\n"
"    background: transparent;\n"
"    color:rgb(54,114,240);\n"
"    border: none;\n"
"}\n"
"QPushButton:hover {\n"
"    color:rgb(54,156,240);\n"
"}\n"
"QPushButton:pressed {    \n"
"    color:rgb(35,187,255);\n"
"\n"
"}")
        self.btn_toXforfaxy.setObjectName("btn_toXforfaxy")
        self.verticalLayout_16.addWidget(self.btn_toXforfaxy)
        self.verticalLayout_12.addWidget(self.verticalFrame_7, 0, QtCore.Qt.AlignTop)
        self.verticalLayout_9.addWidget(self.verticalFrame_3)
        self.verticalLayout_11 = QtWidgets.QVBoxLayout()
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.horizontalFrame_6 = QtWidgets.QFrame(self.verticalFrame_2)
        self.horizontalFrame_6.setMinimumSize(QtCore.QSize(0, 40))
        self.horizontalFrame_6.setMaximumSize(QtCore.QSize(16777215, 40))
        self.horizontalFrame_6.setObjectName("horizontalFrame_6")
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout(self.horizontalFrame_6)
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.label_6 = QtWidgets.QLabel(self.horizontalFrame_6)
        self.label_6.setMaximumSize(QtCore.QSize(24, 24))
        self.label_6.setStyleSheet("background: transparent;\n"
"background-image:url(:/icons_white/icons/png/16x16/cil-clock.png);\n"
"background-position: center;\n"
"background-repeat: no-repeat;")
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_14.addWidget(self.label_6)
        self.label_7 = QtWidgets.QLabel(self.horizontalFrame_6)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("background: transparent;\n"
"color:rgb(204,204,204);")
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_14.addWidget(self.label_7)
        self.verticalLayout_11.addWidget(self.horizontalFrame_6)
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.verticalLayout_11.addLayout(self.horizontalLayout_15)
        self.verticalLayout_9.addLayout(self.verticalLayout_11)
        self.horizontalLayout_10.addWidget(self.verticalFrame_2)
        self.verticalFrame_4 = QtWidgets.QFrame(self.horizontalFrame_4)
        self.verticalFrame_4.setMaximumSize(QtCore.QSize(526, 16777215))
        self.verticalFrame_4.setObjectName("verticalFrame_4")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.verticalFrame_4)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.verticalLayout_15 = QtWidgets.QVBoxLayout()
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.horizontalFrame_7 = QtWidgets.QFrame(self.verticalFrame_4)
        self.horizontalFrame_7.setMinimumSize(QtCore.QSize(0, 40))
        self.horizontalFrame_7.setMaximumSize(QtCore.QSize(16777215, 40))
        self.horizontalFrame_7.setObjectName("horizontalFrame_7")
        self.horizontalLayout_20 = QtWidgets.QHBoxLayout(self.horizontalFrame_7)
        self.horizontalLayout_20.setObjectName("horizontalLayout_20")
        self.label_12 = QtWidgets.QLabel(self.horizontalFrame_7)
        self.label_12.setMaximumSize(QtCore.QSize(24, 24))
        self.label_12.setStyleSheet("background: transparent;\n"
"background-image:url(:/icons_white/icons/png/16x16/cil-settings.png);\n"
"background-position: center;\n"
"background-repeat: no-repeat;")
        self.label_12.setText("")
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_20.addWidget(self.label_12)
        self.label_13 = QtWidgets.QLabel(self.horizontalFrame_7)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_13.setFont(font)
        self.label_13.setStyleSheet("background: transparent;\n"
"color:rgb(204,204,204);")
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_20.addWidget(self.label_13)
        self.verticalLayout_15.addWidget(self.horizontalFrame_7)
        self.frame = QtWidgets.QFrame(self.verticalFrame_4)
        self.frame.setObjectName("frame")
        self.verticalLayout_19 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_19.setContentsMargins(39, -1, -1, -1)
        self.verticalLayout_19.setSpacing(0)
        self.verticalLayout_19.setObjectName("verticalLayout_19")
        self.btn_installPlug = QtWidgets.QPushButton(self.frame)
        self.btn_installPlug.setStyleSheet("QPushButton {\n"
"    Text-align:left;\n"
"    background: transparent;\n"
"    color:rgb(54,114,240);\n"
"    border: none;\n"
"}\n"
"QPushButton:hover {\n"
"    color:rgb(54,156,240);\n"
"}\n"
"QPushButton:pressed {    \n"
"    color:rgb(35,187,255);\n"
"\n"
"}")
        self.btn_installPlug.setObjectName("btn_installPlug")
        self.verticalLayout_19.addWidget(self.btn_installPlug)
        self.btn_Updates = QtWidgets.QPushButton(self.frame)
        self.btn_Updates.setStyleSheet("QPushButton {\n"
"    Text-align:left;\n"
"    background: transparent;\n"
"    color:rgb(54,114,240);\n"
"    border: none;\n"
"}\n"
"QPushButton:hover {\n"
"    color:rgb(54,156,240);\n"
"}\n"
"QPushButton:pressed {    \n"
"    color:rgb(35,187,255);\n"
"\n"
"}")
        self.btn_Updates.setObjectName("btn_Updates")
        self.verticalLayout_19.addWidget(self.btn_Updates)
        self.verticalLayout_15.addWidget(self.frame, 0, QtCore.Qt.AlignTop)
        self.verticalLayout_8.addLayout(self.verticalLayout_15)
        self.verticalLayout_13 = QtWidgets.QVBoxLayout()
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.horizontalFrame_8 = QtWidgets.QFrame(self.verticalFrame_4)
        self.horizontalFrame_8.setMinimumSize(QtCore.QSize(0, 40))
        self.horizontalFrame_8.setMaximumSize(QtCore.QSize(16777215, 40))
        self.horizontalFrame_8.setObjectName("horizontalFrame_8")
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout(self.horizontalFrame_8)
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.label_8 = QtWidgets.QLabel(self.horizontalFrame_8)
        self.label_8.setMaximumSize(QtCore.QSize(24, 24))
        self.label_8.setStyleSheet("background: transparent;\n"
"background-image:url(:/icons_white/icons/png/16x16/cil-pin.png);\n"
"background-position: center;\n"
"background-repeat: no-repeat;")
        self.label_8.setText("")
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_16.addWidget(self.label_8)
        self.label_9 = QtWidgets.QLabel(self.horizontalFrame_8)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("background: transparent;\n"
"color:rgb(204,204,204);")
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_16.addWidget(self.label_9)
        self.verticalLayout_13.addWidget(self.horizontalFrame_8)
        self.frame_2 = QtWidgets.QFrame(self.verticalFrame_4)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_21 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_21.setContentsMargins(38, -1, -1, -1)
        self.verticalLayout_21.setSpacing(0)
        self.verticalLayout_21.setObjectName("verticalLayout_21")
        self.btn_helpReg = QtWidgets.QPushButton(self.frame_2)
        self.btn_helpReg.setStyleSheet("QPushButton {\n"
"    Text-align:left;\n"
"    background: transparent;\n"
"    color:rgb(54,114,240);\n"
"    border: none;\n"
"}\n"
"QPushButton:hover {\n"
"    color:rgb(54,156,240);\n"
"}\n"
"QPushButton:pressed {    \n"
"    color:rgb(35,187,255);\n"
"\n"
"}")
        self.btn_helpReg.setObjectName("btn_helpReg")
        self.verticalLayout_21.addWidget(self.btn_helpReg)
        self.btn_helpprot = QtWidgets.QPushButton(self.frame_2)
        self.btn_helpprot.setStyleSheet("QPushButton {\n"
"    Text-align:left;\n"
"    background: transparent;\n"
"    color:rgb(54,114,240);\n"
"    border: none;\n"
"}\n"
"QPushButton:hover {\n"
"    color:rgb(54,156,240);\n"
"}\n"
"QPushButton:pressed {    \n"
"    color:rgb(35,187,255);\n"
"\n"
"}")
        self.btn_helpprot.setObjectName("btn_helpprot")
        self.verticalLayout_21.addWidget(self.btn_helpprot)
        self.btn_helpcode = QtWidgets.QPushButton(self.frame_2)
        self.btn_helpcode.setStyleSheet("QPushButton {\n"
"    Text-align:left;\n"
"    background: transparent;\n"
"    color:rgb(54,114,240);\n"
"    border: none;\n"
"}\n"
"QPushButton:hover {\n"
"    color:rgb(54,156,240);\n"
"}\n"
"QPushButton:pressed {    \n"
"    color:rgb(35,187,255);\n"
"\n"
"}")
        self.btn_helpcode.setObjectName("btn_helpcode")
        self.verticalLayout_21.addWidget(self.btn_helpcode)
        self.btn_helpFAXY = QtWidgets.QPushButton(self.frame_2)
        self.btn_helpFAXY.setStyleSheet("QPushButton {\n"
"    Text-align:left;\n"
"    background: transparent;\n"
"    color:rgb(54,114,240);\n"
"    border: none;\n"
"}\n"
"QPushButton:hover {\n"
"    color:rgb(54,156,240);\n"
"}\n"
"QPushButton:pressed {    \n"
"    color:rgb(35,187,255);\n"
"\n"
"}")
        self.btn_helpFAXY.setObjectName("btn_helpFAXY")
        self.verticalLayout_21.addWidget(self.btn_helpFAXY)
        self.verticalLayout_13.addWidget(self.frame_2, 0, QtCore.Qt.AlignTop)
        self.verticalLayout_8.addLayout(self.verticalLayout_13)
        self.verticalLayout_14 = QtWidgets.QVBoxLayout()
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.horizontalFrame_9 = QtWidgets.QFrame(self.verticalFrame_4)
        self.horizontalFrame_9.setMinimumSize(QtCore.QSize(0, 40))
        self.horizontalFrame_9.setMaximumSize(QtCore.QSize(16777215, 40))
        self.horizontalFrame_9.setObjectName("horizontalFrame_9")
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout(self.horizontalFrame_9)
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.label_10 = QtWidgets.QLabel(self.horizontalFrame_9)
        self.label_10.setMaximumSize(QtCore.QSize(24, 24))
        self.label_10.setStyleSheet("background: transparent;\n"
"background-image:url(:/icons_white/icons/png/16x16/cil-heart.png);\n"
"background-position: center;\n"
"background-repeat: no-repeat;")
        self.label_10.setText("")
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_18.addWidget(self.label_10)
        self.label_11 = QtWidgets.QLabel(self.horizontalFrame_9)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("background: transparent;\n"
"color:rgb(204,204,204);")
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_18.addWidget(self.label_11)
        self.verticalLayout_14.addWidget(self.horizontalFrame_9)
        self.frame_3 = QtWidgets.QFrame(self.verticalFrame_4)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_20 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_20.setContentsMargins(40, -1, -1, -1)
        self.verticalLayout_20.setObjectName("verticalLayout_20")
        self.verticalLayout_18 = QtWidgets.QVBoxLayout()
        self.verticalLayout_18.setObjectName("verticalLayout_18")
        self.label_15 = QtWidgets.QLabel(self.frame_3)
        self.label_15.setMaximumSize(QtCore.QSize(16777215, 10))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_15.setFont(font)
        self.label_15.setStyleSheet("background: transparent;\n"
"color:rgb(204,204,204);")
        self.label_15.setObjectName("label_15")
        self.verticalLayout_18.addWidget(self.label_15)
        self.horizontalFrame_10 = QtWidgets.QFrame(self.frame_3)
        self.horizontalFrame_10.setObjectName("horizontalFrame_10")
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout(self.horizontalFrame_10)
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.label_25 = QtWidgets.QLabel(self.horizontalFrame_10)
        self.label_25.setMinimumSize(QtCore.QSize(40, 40))
        self.label_25.setMaximumSize(QtCore.QSize(40, 40))
        self.label_25.setStyleSheet("background: transparent;\n"
"background-position: center;\n"
"background-repeat: no-repeat;\n"
"image: url(:/icons svg/icons/png/TMPM.png);")
        self.label_25.setText("")
        self.label_25.setObjectName("label_25")
        self.horizontalLayout_19.addWidget(self.label_25)
        self.verticalLayout_18.addWidget(self.horizontalFrame_10, 0, QtCore.Qt.AlignLeft)
        self.verticalLayout_20.addLayout(self.verticalLayout_18)
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.label_16 = QtWidgets.QLabel(self.frame_3)
        self.label_16.setMaximumSize(QtCore.QSize(16777215, 10))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_16.setFont(font)
        self.label_16.setStyleSheet("background: transparent;\n"
"color:rgb(204,204,204);")
        self.label_16.setObjectName("label_16")
        self.verticalLayout_10.addWidget(self.label_16)
        self.verticalFrame_9 = QtWidgets.QFrame(self.frame_3)
        self.verticalFrame_9.setObjectName("verticalFrame_9")
        self.horizontalLayout_21 = QtWidgets.QHBoxLayout(self.verticalFrame_9)
        self.horizontalLayout_21.setObjectName("horizontalLayout_21")
        self.label_19 = QtWidgets.QLabel(self.verticalFrame_9)
        self.label_19.setMinimumSize(QtCore.QSize(40, 40))
        self.label_19.setMaximumSize(QtCore.QSize(40, 40))
        self.label_19.setStyleSheet("background: transparent;\n"
"background-position: center;\n"
"background-repeat: no-repeat;\n"
"image: url(:/faces/faces/Mancilla.png);")
        self.label_19.setText("")
        self.label_19.setObjectName("label_19")
        self.horizontalLayout_21.addWidget(self.label_19)
        self.label_18 = QtWidgets.QLabel(self.verticalFrame_9)
        self.label_18.setMinimumSize(QtCore.QSize(40, 40))
        self.label_18.setMaximumSize(QtCore.QSize(40, 40))
        self.label_18.setStyleSheet("background: transparent;\n"
"background-position: center;\n"
"background-repeat: no-repeat;\n"
"image: url(:/faces/faces/Gallo.png);")
        self.label_18.setText("")
        self.label_18.setObjectName("label_18")
        self.horizontalLayout_21.addWidget(self.label_18)
        self.label_20 = QtWidgets.QLabel(self.verticalFrame_9)
        self.label_20.setMinimumSize(QtCore.QSize(40, 40))
        self.label_20.setMaximumSize(QtCore.QSize(40, 40))
        self.label_20.setStyleSheet("background: transparent;\n"
"background-position: center;\n"
"background-repeat: no-repeat;\n"
"image: url(:/faces/faces/Villarroel.png);")
        self.label_20.setText("")
        self.label_20.setObjectName("label_20")
        self.horizontalLayout_21.addWidget(self.label_20)
        self.label_22 = QtWidgets.QLabel(self.verticalFrame_9)
        self.label_22.setMinimumSize(QtCore.QSize(40, 40))
        self.label_22.setMaximumSize(QtCore.QSize(40, 40))
        self.label_22.setStyleSheet("background: transparent;\n"
"background-position: center;\n"
"background-repeat: no-repeat;\n"
"image: url(:/faces/faces/Ruchichi.png);")
        self.label_22.setText("")
        self.label_22.setObjectName("label_22")
        self.horizontalLayout_21.addWidget(self.label_22)
        self.label_21 = QtWidgets.QLabel(self.verticalFrame_9)
        self.label_21.setMinimumSize(QtCore.QSize(40, 40))
        self.label_21.setMaximumSize(QtCore.QSize(40, 40))
        self.label_21.setStyleSheet("background: transparent;\n"
"background-position: center;\n"
"background-repeat: no-repeat;\n"
"image: url(:/faces/faces/Soto.png);\n"
"toolTip{\n"
"    background-color: rgb(255, 255, 255);\n"
"}")
        self.label_21.setText("")
        self.label_21.setObjectName("label_21")
        self.horizontalLayout_21.addWidget(self.label_21)
        self.label_17 = QtWidgets.QLabel(self.verticalFrame_9)
        self.label_17.setMinimumSize(QtCore.QSize(40, 40))
        self.label_17.setMaximumSize(QtCore.QSize(40, 40))
        self.label_17.setStyleSheet("background: transparent;\n"
"background-position: center;\n"
"background-repeat: no-repeat;\n"
"image: url(:/faces/faces/Mardones.png);")
        self.label_17.setText("")
        self.label_17.setObjectName("label_17")
        self.horizontalLayout_21.addWidget(self.label_17)
        self.label_23 = QtWidgets.QLabel(self.verticalFrame_9)
        self.label_23.setMinimumSize(QtCore.QSize(40, 40))
        self.label_23.setMaximumSize(QtCore.QSize(40, 40))
        self.label_23.setStyleSheet("background: transparent;\n"
"background-position: center;\n"
"background-repeat: no-repeat;\n"
"image: url(:/faces/faces/Latorre.png);")
        self.label_23.setText("")
        self.label_23.setObjectName("label_23")
        self.horizontalLayout_21.addWidget(self.label_23)
        self.label_24 = QtWidgets.QLabel(self.verticalFrame_9)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_24.sizePolicy().hasHeightForWidth())
        self.label_24.setSizePolicy(sizePolicy)
        self.label_24.setMinimumSize(QtCore.QSize(40, 40))
        self.label_24.setMaximumSize(QtCore.QSize(40, 40))
        self.label_24.setStyleSheet("background: transparent;\n"
"background-position: center;\n"
"background-repeat: no-repeat;\n"
"image: url(:/faces/faces/Inarejo.png);")
        self.label_24.setText("")
        self.label_24.setObjectName("label_24")
        self.horizontalLayout_21.addWidget(self.label_24)
        self.verticalLayout_10.addWidget(self.verticalFrame_9, 0, QtCore.Qt.AlignLeft)
        self.verticalLayout_20.addLayout(self.verticalLayout_10)
        self.verticalLayout_14.addWidget(self.frame_3)
        self.verticalLayout_8.addLayout(self.verticalLayout_14)
        self.horizontalLayout_10.addWidget(self.verticalFrame_4)
        self.verticalLayout_3.addWidget(self.horizontalFrame_4)
        self.horizontalLayout.addWidget(self.verticalFrame)
        self.horizontalFrame_2 = QtWidgets.QFrame(HomeWidget)
        self.horizontalFrame_2.setMinimumSize(QtCore.QSize(50, 0))
        self.horizontalFrame_2.setObjectName("horizontalFrame_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalFrame_2)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.horizontalLayout.addWidget(self.horizontalFrame_2)

        self.retranslateUi(HomeWidget)
        QtCore.QMetaObject.connectSlotsByName(HomeWidget)

    def retranslateUi(self, HomeWidget):
        _translate = QtCore.QCoreApplication.translate
        HomeWidget.setWindowTitle(_translate("HomeWidget", "Form"))
        self.label_5.setText(_translate("HomeWidget", "Inicio"))
        self.btn_newregister.setText(_translate("HomeWidget", "Nuevo registro"))
        self.btn_openReg.setText(_translate("HomeWidget", "Abrir Registro..."))
        self.btn_newProt.setText(_translate("HomeWidget", "Nuevo Protocolo"))
        self.btn_toXforfaxy.setText(_translate("HomeWidget", "Transformar a formato *.faxy"))
        self.label_7.setText(_translate("HomeWidget", "Recientes"))
        self.label_13.setText(_translate("HomeWidget", "Personalizar"))
        self.btn_installPlug.setText(_translate("HomeWidget", "Instalar plugins..."))
        self.btn_Updates.setText(_translate("HomeWidget", "Buscar Actualizaciones..."))
        self.label_9.setText(_translate("HomeWidget", "Aprenda sobre..."))
        self.btn_helpReg.setText(_translate("HomeWidget", "Registro Básico"))
        self.btn_helpprot.setText(_translate("HomeWidget", "Desarrollo de protocolos"))
        self.btn_helpcode.setText(_translate("HomeWidget", "Nuestro código fuente"))
        self.btn_helpFAXY.setText(_translate("HomeWidget", "El formato *.faxy"))
        self.label_11.setText(_translate("HomeWidget", "Con el apoyo de..."))
        self.label_15.setText(_translate("HomeWidget", "Instituciones :"))
        self.label_25.setToolTip(_translate("HomeWidget", "Escuela de TM. UACH-PM"))
        self.label_16.setText(_translate("HomeWidget", "Investigadores :"))
        self.label_19.setToolTip(_translate("HomeWidget", "TM. Elvis Eduardo Mancilla Goldschmidt "))
        self.label_18.setToolTip(_translate("HomeWidget", "TM. Enrique Gallo Barraza "))
        self.label_20.setToolTip(_translate("HomeWidget", "TM. Daniela Villarroel Vera "))
        self.label_22.setToolTip(_translate("HomeWidget", "TM. Nicolás Ruchichi "))
        self.label_21.setToolTip(_translate("HomeWidget", "TM. Julio Cesar Soto González "))
        self.label_17.setToolTip(_translate("HomeWidget", "TM. Jorge Omar Mardones Meléndez "))
        self.label_23.setToolTip(_translate("HomeWidget", "TM. María Paz Latorre Gonzalez "))
        self.label_24.setToolTip(_translate("HomeWidget", "TM. Ignacia Inarejo Inarejo "))

from resource import resource_rc