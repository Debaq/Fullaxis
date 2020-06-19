# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'home2WiVKQV.ui'
##
## Created by: Qt User Interface Compiler version 5.15.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *

from resource import resource_rc

class Ui_HomeWidget(object):
    def setupUi(self, HomeWidget):
        if not HomeWidget.objectName():
            HomeWidget.setObjectName(u"HomeWidget")
        HomeWidget.resize(920, 612)
        self.horizontalLayout = QHBoxLayout(HomeWidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 50, 0, 0)
        self.horizontalFrame = QFrame(HomeWidget)
        self.horizontalFrame.setObjectName(u"horizontalFrame")
        self.horizontalFrame.setMinimumSize(QSize(50, 0))
        self.horizontalLayout_2 = QHBoxLayout(self.horizontalFrame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")

        self.horizontalLayout.addWidget(self.horizontalFrame)

        self.verticalFrame = QFrame(HomeWidget)
        self.verticalFrame.setObjectName(u"verticalFrame")
        self.verticalFrame.setMinimumSize(QSize(720, 0))
        self.verticalFrame.setMaximumSize(QSize(720, 16777215))
        self.verticalLayout_3 = QVBoxLayout(self.verticalFrame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(-1, 1, -1, -1)
        self.horizontalFrame1 = QFrame(self.verticalFrame)
        self.horizontalFrame1.setObjectName(u"horizontalFrame1")
        self.horizontalFrame1.setMaximumSize(QSize(16777215, 100))
        self.horizontalFrame1.setFrameShape(QFrame.NoFrame)
        self.horizontalFrame1.setLineWidth(2)
        self.horizontalLayout_11 = QHBoxLayout(self.horizontalFrame1)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.horizontalFrame_2 = QFrame(self.horizontalFrame1)
        self.horizontalFrame_2.setObjectName(u"horizontalFrame_2")
        self.horizontalFrame_2.setStyleSheet(u"background: transparent;")
        self.horizontalLayout_12 = QHBoxLayout(self.horizontalFrame_2)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.horizontalFrame_2)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(60, 60))
        self.label.setMaximumSize(QSize(60, 60))
        self.label.setStyleSheet(u"background: transparent;\n"
"background-position: center;\n"
"background-repeat: no-repeat;\n"
"image: url(:/icons svg/icons/png/logo.png);")
        self.label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_12.addWidget(self.label)

        self.verticalFrame1 = QFrame(self.horizontalFrame_2)
        self.verticalFrame1.setObjectName(u"verticalFrame1")
        self.verticalLayout_4 = QVBoxLayout(self.verticalFrame1)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(10, 0, 0, 0)
        self.label_2 = QLabel(self.verticalFrame1)
        self.label_2.setObjectName(u"label_2")
        font = QFont()
        font.setPointSize(20)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"background: transparent;\n"
"color:rgb(204,204,204);")
        self.label_2.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)

        self.verticalLayout_4.addWidget(self.label_2)

        self.label_3 = QLabel(self.verticalFrame1)
        self.label_3.setObjectName(u"label_3")
        font1 = QFont()
        font1.setPointSize(12)
        self.label_3.setFont(font1)
        self.label_3.setStyleSheet(u"background: transparent;\n"
"color:rgb(204,204,204);")
        self.label_3.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.verticalLayout_4.addWidget(self.label_3)


        self.horizontalLayout_12.addWidget(self.verticalFrame1)


        self.horizontalLayout_11.addWidget(self.horizontalFrame_2)

        self.Frame_login = QFrame(self.horizontalFrame1)
        self.Frame_login.setObjectName(u"Frame_login")
        self.Frame_login.setStyleSheet(u"background: transparent;")
        self.Frame_login.setFrameShape(QFrame.Box)
        self.layoutFrame_login = QHBoxLayout(self.Frame_login)
        self.layoutFrame_login.setObjectName(u"layoutFrame_login")
        self.layoutFrame_login.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_11.addWidget(self.Frame_login)


        self.verticalLayout_3.addWidget(self.horizontalFrame1)

        self.horizontalFrame_4 = QFrame(self.verticalFrame)
        self.horizontalFrame_4.setObjectName(u"horizontalFrame_4")
        self.horizontalFrame_4.setMinimumSize(QSize(0, 0))
        self.horizontalFrame_4.setMaximumSize(QSize(16777215, 16777215))
        self.horizontalLayout_10 = QHBoxLayout(self.horizontalFrame_4)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, -1, -1, -1)
        self.verticalFrame_2 = QFrame(self.horizontalFrame_4)
        self.verticalFrame_2.setObjectName(u"verticalFrame_2")
        self.verticalFrame_2.setMinimumSize(QSize(270, 0))
        self.verticalFrame_2.setMaximumSize(QSize(270, 16777215))
        self.verticalLayout_9 = QVBoxLayout(self.verticalFrame_2)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalFrame_3 = QFrame(self.verticalFrame_2)
        self.verticalFrame_3.setObjectName(u"verticalFrame_3")
        self.verticalFrame_3.setMinimumSize(QSize(260, 150))
        self.verticalFrame_3.setMaximumSize(QSize(16777215, 160))
        self.verticalLayout_12 = QVBoxLayout(self.verticalFrame_3)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.horizontalFrame_5 = QFrame(self.verticalFrame_3)
        self.horizontalFrame_5.setObjectName(u"horizontalFrame_5")
        self.horizontalFrame_5.setMaximumSize(QSize(16777215, 40))
        self.horizontalLayout_13 = QHBoxLayout(self.horizontalFrame_5)
        self.horizontalLayout_13.setSpacing(6)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_4 = QLabel(self.horizontalFrame_5)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(24, 24))
        self.label_4.setStyleSheet(u"background: transparent;\n"
"background-position: center;\n"
"background-image: url(:/icons_white/icons/png/16x16/cil-home.png);\n"
"background-repeat: no-repeat;")

        self.horizontalLayout_13.addWidget(self.label_4)

        self.label_5 = QLabel(self.horizontalFrame_5)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font1)
        self.label_5.setStyleSheet(u"background: transparent;\n"
"color:rgb(204,204,204);")

        self.horizontalLayout_13.addWidget(self.label_5)


        self.verticalLayout_12.addWidget(self.horizontalFrame_5)

        self.verticalFrame_7 = QFrame(self.verticalFrame_3)
        self.verticalFrame_7.setObjectName(u"verticalFrame_7")
        self.verticalLayout_16 = QVBoxLayout(self.verticalFrame_7)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(29, -1, -1, -1)
        self.btn_newregister = QPushButton(self.verticalFrame_7)
        self.btn_newregister.setObjectName(u"btn_newregister")
        self.btn_newregister.setCursor(QCursor(Qt.ArrowCursor))
        self.btn_newregister.setStyleSheet(u"QPushButton {\n"
"	Text-align:left;\n"
"	background: transparent;\n"
"	color:rgb(54,114,240);\n"
"	border: none;\n"
"}\n"
"QPushButton:hover {\n"
"	color:rgb(54,156,240);\n"
"}\n"
"QPushButton:pressed {	\n"
"	color:rgb(35,187,255);\n"
"\n"
"}")

        self.verticalLayout_16.addWidget(self.btn_newregister)

        self.btn_openReg = QPushButton(self.verticalFrame_7)
        self.btn_openReg.setObjectName(u"btn_openReg")
        self.btn_openReg.setStyleSheet(u"QPushButton {\n"
"	Text-align:left;\n"
"	background: transparent;\n"
"	color:rgb(54,114,240);\n"
"	border: none;\n"
"}\n"
"QPushButton:hover {\n"
"	color:rgb(54,156,240);\n"
"}\n"
"QPushButton:pressed {	\n"
"	color:rgb(35,187,255);\n"
"\n"
"}")

        self.verticalLayout_16.addWidget(self.btn_openReg)

        self.btn_newProt = QPushButton(self.verticalFrame_7)
        self.btn_newProt.setObjectName(u"btn_newProt")
        self.btn_newProt.setStyleSheet(u"QPushButton {\n"
"	Text-align:left;\n"
"	background: transparent;\n"
"	color:rgb(54,114,240);\n"
"	border: none;\n"
"}\n"
"QPushButton:hover {\n"
"	color:rgb(54,156,240);\n"
"}\n"
"QPushButton:pressed {	\n"
"	color:rgb(35,187,255);\n"
"\n"
"}")

        self.verticalLayout_16.addWidget(self.btn_newProt)

        self.btn_toXforfaxy = QPushButton(self.verticalFrame_7)
        self.btn_toXforfaxy.setObjectName(u"btn_toXforfaxy")
        self.btn_toXforfaxy.setStyleSheet(u"QPushButton {\n"
"	Text-align:left;\n"
"	background: transparent;\n"
"	color:rgb(54,114,240);\n"
"	border: none;\n"
"}\n"
"QPushButton:hover {\n"
"	color:rgb(54,156,240);\n"
"}\n"
"QPushButton:pressed {	\n"
"	color:rgb(35,187,255);\n"
"\n"
"}")

        self.verticalLayout_16.addWidget(self.btn_toXforfaxy)


        self.verticalLayout_12.addWidget(self.verticalFrame_7, 0, Qt.AlignTop)


        self.verticalLayout_9.addWidget(self.verticalFrame_3)

        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.horizontalFrame_6 = QFrame(self.verticalFrame_2)
        self.horizontalFrame_6.setObjectName(u"horizontalFrame_6")
        self.horizontalFrame_6.setMinimumSize(QSize(0, 40))
        self.horizontalFrame_6.setMaximumSize(QSize(16777215, 40))
        self.horizontalLayout_14 = QHBoxLayout(self.horizontalFrame_6)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.label_6 = QLabel(self.horizontalFrame_6)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMaximumSize(QSize(24, 24))
        self.label_6.setStyleSheet(u"background: transparent;\n"
"background-image:url(:/icons_white/icons/png/16x16/cil-clock.png);\n"
"background-position: center;\n"
"background-repeat: no-repeat;")

        self.horizontalLayout_14.addWidget(self.label_6)

        self.label_7 = QLabel(self.horizontalFrame_6)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font1)
        self.label_7.setStyleSheet(u"background: transparent;\n"
"color:rgb(204,204,204);")

        self.horizontalLayout_14.addWidget(self.label_7)


        self.verticalLayout_11.addWidget(self.horizontalFrame_6)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")

        self.verticalLayout_11.addLayout(self.horizontalLayout_15)


        self.verticalLayout_9.addLayout(self.verticalLayout_11)


        self.horizontalLayout_10.addWidget(self.verticalFrame_2)

        self.verticalFrame_4 = QFrame(self.horizontalFrame_4)
        self.verticalFrame_4.setObjectName(u"verticalFrame_4")
        self.verticalFrame_4.setMaximumSize(QSize(526, 16777215))
        self.verticalLayout_8 = QVBoxLayout(self.verticalFrame_4)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_15 = QVBoxLayout()
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.horizontalFrame_7 = QFrame(self.verticalFrame_4)
        self.horizontalFrame_7.setObjectName(u"horizontalFrame_7")
        self.horizontalFrame_7.setMinimumSize(QSize(0, 40))
        self.horizontalFrame_7.setMaximumSize(QSize(16777215, 40))
        self.horizontalLayout_20 = QHBoxLayout(self.horizontalFrame_7)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.label_12 = QLabel(self.horizontalFrame_7)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setMaximumSize(QSize(24, 24))
        self.label_12.setStyleSheet(u"background: transparent;\n"
"background-image:url(:/icons_white/icons/png/16x16/cil-settings.png);\n"
"background-position: center;\n"
"background-repeat: no-repeat;")

        self.horizontalLayout_20.addWidget(self.label_12)

        self.label_13 = QLabel(self.horizontalFrame_7)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setFont(font1)
        self.label_13.setStyleSheet(u"background: transparent;\n"
"color:rgb(204,204,204);")

        self.horizontalLayout_20.addWidget(self.label_13)


        self.verticalLayout_15.addWidget(self.horizontalFrame_7)

        self.frame = QFrame(self.verticalFrame_4)
        self.frame.setObjectName(u"frame")
        self.verticalLayout_19 = QVBoxLayout(self.frame)
        self.verticalLayout_19.setSpacing(0)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(39, -1, -1, -1)
        self.btn_installPlug = QPushButton(self.frame)
        self.btn_installPlug.setObjectName(u"btn_installPlug")
        self.btn_installPlug.setStyleSheet(u"QPushButton {\n"
"	Text-align:left;\n"
"	background: transparent;\n"
"	color:rgb(54,114,240);\n"
"	border: none;\n"
"}\n"
"QPushButton:hover {\n"
"	color:rgb(54,156,240);\n"
"}\n"
"QPushButton:pressed {	\n"
"	color:rgb(35,187,255);\n"
"\n"
"}")

        self.verticalLayout_19.addWidget(self.btn_installPlug)

        self.btn_Updates = QPushButton(self.frame)
        self.btn_Updates.setObjectName(u"btn_Updates")
        self.btn_Updates.setStyleSheet(u"QPushButton {\n"
"	Text-align:left;\n"
"	background: transparent;\n"
"	color:rgb(54,114,240);\n"
"	border: none;\n"
"}\n"
"QPushButton:hover {\n"
"	color:rgb(54,156,240);\n"
"}\n"
"QPushButton:pressed {	\n"
"	color:rgb(35,187,255);\n"
"\n"
"}")

        self.verticalLayout_19.addWidget(self.btn_Updates)


        self.verticalLayout_15.addWidget(self.frame, 0, Qt.AlignTop)


        self.verticalLayout_8.addLayout(self.verticalLayout_15)

        self.verticalLayout_13 = QVBoxLayout()
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.horizontalFrame_8 = QFrame(self.verticalFrame_4)
        self.horizontalFrame_8.setObjectName(u"horizontalFrame_8")
        self.horizontalFrame_8.setMinimumSize(QSize(0, 40))
        self.horizontalFrame_8.setMaximumSize(QSize(16777215, 40))
        self.horizontalLayout_16 = QHBoxLayout(self.horizontalFrame_8)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.label_8 = QLabel(self.horizontalFrame_8)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMaximumSize(QSize(24, 24))
        self.label_8.setStyleSheet(u"background: transparent;\n"
"background-image:url(:/icons_white/icons/png/16x16/cil-pin.png);\n"
"background-position: center;\n"
"background-repeat: no-repeat;")

        self.horizontalLayout_16.addWidget(self.label_8)

        self.label_9 = QLabel(self.horizontalFrame_8)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font1)
        self.label_9.setStyleSheet(u"background: transparent;\n"
"color:rgb(204,204,204);")

        self.horizontalLayout_16.addWidget(self.label_9)


        self.verticalLayout_13.addWidget(self.horizontalFrame_8)

        self.frame_2 = QFrame(self.verticalFrame_4)
        self.frame_2.setObjectName(u"frame_2")
        self.verticalLayout_21 = QVBoxLayout(self.frame_2)
        self.verticalLayout_21.setSpacing(0)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(38, -1, -1, -1)
        self.btn_helpReg = QPushButton(self.frame_2)
        self.btn_helpReg.setObjectName(u"btn_helpReg")
        self.btn_helpReg.setStyleSheet(u"QPushButton {\n"
"	Text-align:left;\n"
"	background: transparent;\n"
"	color:rgb(54,114,240);\n"
"	border: none;\n"
"}\n"
"QPushButton:hover {\n"
"	color:rgb(54,156,240);\n"
"}\n"
"QPushButton:pressed {	\n"
"	color:rgb(35,187,255);\n"
"\n"
"}")

        self.verticalLayout_21.addWidget(self.btn_helpReg)

        self.btn_helpprot = QPushButton(self.frame_2)
        self.btn_helpprot.setObjectName(u"btn_helpprot")
        self.btn_helpprot.setStyleSheet(u"QPushButton {\n"
"	Text-align:left;\n"
"	background: transparent;\n"
"	color:rgb(54,114,240);\n"
"	border: none;\n"
"}\n"
"QPushButton:hover {\n"
"	color:rgb(54,156,240);\n"
"}\n"
"QPushButton:pressed {	\n"
"	color:rgb(35,187,255);\n"
"\n"
"}")

        self.verticalLayout_21.addWidget(self.btn_helpprot)

        self.btn_helpcode = QPushButton(self.frame_2)
        self.btn_helpcode.setObjectName(u"btn_helpcode")
        self.btn_helpcode.setStyleSheet(u"QPushButton {\n"
"	Text-align:left;\n"
"	background: transparent;\n"
"	color:rgb(54,114,240);\n"
"	border: none;\n"
"}\n"
"QPushButton:hover {\n"
"	color:rgb(54,156,240);\n"
"}\n"
"QPushButton:pressed {	\n"
"	color:rgb(35,187,255);\n"
"\n"
"}")

        self.verticalLayout_21.addWidget(self.btn_helpcode)

        self.btn_helpFAXY = QPushButton(self.frame_2)
        self.btn_helpFAXY.setObjectName(u"btn_helpFAXY")
        self.btn_helpFAXY.setStyleSheet(u"QPushButton {\n"
"	Text-align:left;\n"
"	background: transparent;\n"
"	color:rgb(54,114,240);\n"
"	border: none;\n"
"}\n"
"QPushButton:hover {\n"
"	color:rgb(54,156,240);\n"
"}\n"
"QPushButton:pressed {	\n"
"	color:rgb(35,187,255);\n"
"\n"
"}")

        self.verticalLayout_21.addWidget(self.btn_helpFAXY)


        self.verticalLayout_13.addWidget(self.frame_2, 0, Qt.AlignTop)


        self.verticalLayout_8.addLayout(self.verticalLayout_13)

        self.verticalLayout_14 = QVBoxLayout()
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.horizontalFrame_9 = QFrame(self.verticalFrame_4)
        self.horizontalFrame_9.setObjectName(u"horizontalFrame_9")
        self.horizontalFrame_9.setMinimumSize(QSize(0, 40))
        self.horizontalFrame_9.setMaximumSize(QSize(16777215, 40))
        self.horizontalLayout_18 = QHBoxLayout(self.horizontalFrame_9)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.label_10 = QLabel(self.horizontalFrame_9)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMaximumSize(QSize(24, 24))
        self.label_10.setStyleSheet(u"background: transparent;\n"
"background-image:url(:/icons_white/icons/png/16x16/cil-heart.png);\n"
"background-position: center;\n"
"background-repeat: no-repeat;")

        self.horizontalLayout_18.addWidget(self.label_10)

        self.label_11 = QLabel(self.horizontalFrame_9)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font1)
        self.label_11.setStyleSheet(u"background: transparent;\n"
"color:rgb(204,204,204);")

        self.horizontalLayout_18.addWidget(self.label_11)


        self.verticalLayout_14.addWidget(self.horizontalFrame_9)

        self.frame_3 = QFrame(self.verticalFrame_4)
        self.frame_3.setObjectName(u"frame_3")
        self.verticalLayout_20 = QVBoxLayout(self.frame_3)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(40, -1, -1, -1)
        self.verticalLayout_18 = QVBoxLayout()
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.label_15 = QLabel(self.frame_3)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setMaximumSize(QSize(16777215, 10))
        font2 = QFont()
        font2.setPointSize(8)
        self.label_15.setFont(font2)
        self.label_15.setStyleSheet(u"background: transparent;\n"
"color:rgb(204,204,204);")

        self.verticalLayout_18.addWidget(self.label_15)

        self.horizontalFrame_10 = QFrame(self.frame_3)
        self.horizontalFrame_10.setObjectName(u"horizontalFrame_10")
        self.horizontalLayout_19 = QHBoxLayout(self.horizontalFrame_10)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.label_25 = QLabel(self.horizontalFrame_10)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setMinimumSize(QSize(40, 40))
        self.label_25.setMaximumSize(QSize(40, 40))
        self.label_25.setStyleSheet(u"background: transparent;\n"
"background-position: center;\n"
"background-repeat: no-repeat;\n"
"image: url(:/icons svg/icons/png/TMPM.png);")

        self.horizontalLayout_19.addWidget(self.label_25)


        self.verticalLayout_18.addWidget(self.horizontalFrame_10, 0, Qt.AlignLeft)


        self.verticalLayout_20.addLayout(self.verticalLayout_18)

        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_16 = QLabel(self.frame_3)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setMaximumSize(QSize(16777215, 10))
        self.label_16.setFont(font2)
        self.label_16.setStyleSheet(u"background: transparent;\n"
"color:rgb(204,204,204);")

        self.verticalLayout_10.addWidget(self.label_16)

        self.verticalFrame_9 = QFrame(self.frame_3)
        self.verticalFrame_9.setObjectName(u"verticalFrame_9")
        self.horizontalLayout_21 = QHBoxLayout(self.verticalFrame_9)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.label_19 = QLabel(self.verticalFrame_9)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setMinimumSize(QSize(40, 40))
        self.label_19.setMaximumSize(QSize(40, 40))
        self.label_19.setStyleSheet(u"background: transparent;\n"
"background-position: center;\n"
"background-repeat: no-repeat;\n"
"image: url(:/faces/faces/Mancilla.png);")

        self.horizontalLayout_21.addWidget(self.label_19)

        self.label_18 = QLabel(self.verticalFrame_9)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setMinimumSize(QSize(40, 40))
        self.label_18.setMaximumSize(QSize(40, 40))
        self.label_18.setStyleSheet(u"background: transparent;\n"
"background-position: center;\n"
"background-repeat: no-repeat;\n"
"image: url(:/faces/faces/Gallo.png);")

        self.horizontalLayout_21.addWidget(self.label_18)

        self.label_20 = QLabel(self.verticalFrame_9)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setMinimumSize(QSize(40, 40))
        self.label_20.setMaximumSize(QSize(40, 40))
        self.label_20.setStyleSheet(u"background: transparent;\n"
"background-position: center;\n"
"background-repeat: no-repeat;\n"
"image: url(:/faces/faces/Villarroel.png);")

        self.horizontalLayout_21.addWidget(self.label_20)

        self.label_22 = QLabel(self.verticalFrame_9)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setMinimumSize(QSize(40, 40))
        self.label_22.setMaximumSize(QSize(40, 40))
        self.label_22.setStyleSheet(u"background: transparent;\n"
"background-position: center;\n"
"background-repeat: no-repeat;\n"
"image: url(:/faces/faces/Ruchichi.png);")

        self.horizontalLayout_21.addWidget(self.label_22)

        self.label_21 = QLabel(self.verticalFrame_9)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setMinimumSize(QSize(40, 40))
        self.label_21.setMaximumSize(QSize(40, 40))
        self.label_21.setStyleSheet(u"background: transparent;\n"
"background-position: center;\n"
"background-repeat: no-repeat;\n"
"image: url(:/faces/faces/Soto.png);\n"
"toolTip{\n"
"	background-color: rgb(255, 255, 255);\n"
"}")

        self.horizontalLayout_21.addWidget(self.label_21)

        self.label_17 = QLabel(self.verticalFrame_9)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setMinimumSize(QSize(40, 40))
        self.label_17.setMaximumSize(QSize(40, 40))
        self.label_17.setStyleSheet(u"background: transparent;\n"
"background-position: center;\n"
"background-repeat: no-repeat;\n"
"image: url(:/faces/faces/Mardones.png);")

        self.horizontalLayout_21.addWidget(self.label_17)

        self.label_23 = QLabel(self.verticalFrame_9)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setMinimumSize(QSize(40, 40))
        self.label_23.setMaximumSize(QSize(40, 40))
        self.label_23.setStyleSheet(u"background: transparent;\n"
"background-position: center;\n"
"background-repeat: no-repeat;\n"
"image: url(:/faces/faces/Latorre.png);")

        self.horizontalLayout_21.addWidget(self.label_23)

        self.label_24 = QLabel(self.verticalFrame_9)
        self.label_24.setObjectName(u"label_24")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_24.sizePolicy().hasHeightForWidth())
        self.label_24.setSizePolicy(sizePolicy)
        self.label_24.setMinimumSize(QSize(40, 40))
        self.label_24.setMaximumSize(QSize(40, 40))
        self.label_24.setStyleSheet(u"background: transparent;\n"
"background-position: center;\n"
"background-repeat: no-repeat;\n"
"image: url(:/faces/faces/Inarejo.png);")

        self.horizontalLayout_21.addWidget(self.label_24)


        self.verticalLayout_10.addWidget(self.verticalFrame_9, 0, Qt.AlignLeft)


        self.verticalLayout_20.addLayout(self.verticalLayout_10)


        self.verticalLayout_14.addWidget(self.frame_3)


        self.verticalLayout_8.addLayout(self.verticalLayout_14)


        self.horizontalLayout_10.addWidget(self.verticalFrame_4)


        self.verticalLayout_3.addWidget(self.horizontalFrame_4)


        self.horizontalLayout.addWidget(self.verticalFrame)

        self.horizontalFrame_21 = QFrame(HomeWidget)
        self.horizontalFrame_21.setObjectName(u"horizontalFrame_21")
        self.horizontalFrame_21.setMinimumSize(QSize(50, 0))
        self.horizontalLayout_3 = QHBoxLayout(self.horizontalFrame_21)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")

        self.horizontalLayout.addWidget(self.horizontalFrame_21)


        self.retranslateUi(HomeWidget)

        QMetaObject.connectSlotsByName(HomeWidget)
    # setupUi

    def retranslateUi(self, HomeWidget):
        HomeWidget.setWindowTitle(QCoreApplication.translate("HomeWidget", u"Form", None))
        self.label.setText("")
        self.label_2.setText(QCoreApplication.translate("HomeWidget", u"Full Axis", None))
        self.label_3.setText(QCoreApplication.translate("HomeWidget", u"Sistema de evaluaci\u00f3n de la marcha ", None))
        self.label_4.setText("")
        self.label_5.setText(QCoreApplication.translate("HomeWidget", u"Inicio", None))
        self.btn_newregister.setText(QCoreApplication.translate("HomeWidget", u"Nuevo registro", None))
        self.btn_openReg.setText(QCoreApplication.translate("HomeWidget", u"Abrir Registro...", None))
        self.btn_newProt.setText(QCoreApplication.translate("HomeWidget", u"Nuevo Protocolo", None))
        self.btn_toXforfaxy.setText(QCoreApplication.translate("HomeWidget", u"Transformar a formato *.faxy", None))
        self.label_6.setText("")
        self.label_7.setText(QCoreApplication.translate("HomeWidget", u"Recientes", None))
        self.label_12.setText("")
        self.label_13.setText(QCoreApplication.translate("HomeWidget", u"Personalizar", None))
        self.btn_installPlug.setText(QCoreApplication.translate("HomeWidget", u"Instalar plugins...", None))
        self.btn_Updates.setText(QCoreApplication.translate("HomeWidget", u"Buscar Actualizaciones...", None))
        self.label_8.setText("")
        self.label_9.setText(QCoreApplication.translate("HomeWidget", u"Aprenda sobre...", None))
        self.btn_helpReg.setText(QCoreApplication.translate("HomeWidget", u"Registro B\u00e1sico", None))
        self.btn_helpprot.setText(QCoreApplication.translate("HomeWidget", u"Desarrollo de protocolos", None))
        self.btn_helpcode.setText(QCoreApplication.translate("HomeWidget", u"Nuestro c\u00f3digo fuente", None))
        self.btn_helpFAXY.setText(QCoreApplication.translate("HomeWidget", u"El formato *.faxy", None))
        self.label_10.setText("")
        self.label_11.setText(QCoreApplication.translate("HomeWidget", u"Con el apoyo de...", None))
        self.label_15.setText(QCoreApplication.translate("HomeWidget", u"Instituciones :", None))
#if QT_CONFIG(tooltip)
        self.label_25.setToolTip(QCoreApplication.translate("HomeWidget", u"Escuela de TM. UACH-PM", None))
#endif // QT_CONFIG(tooltip)
        self.label_25.setText("")
        self.label_16.setText(QCoreApplication.translate("HomeWidget", u"Investigadores :", None))
#if QT_CONFIG(tooltip)
        self.label_19.setToolTip(QCoreApplication.translate("HomeWidget", u"TM. Elvis Eduardo Mancilla Goldschmidt ", None))
#endif // QT_CONFIG(tooltip)
        self.label_19.setText("")
#if QT_CONFIG(tooltip)
        self.label_18.setToolTip(QCoreApplication.translate("HomeWidget", u"TM. Enrique Gallo Barraza ", None))
#endif // QT_CONFIG(tooltip)
        self.label_18.setText("")
#if QT_CONFIG(tooltip)
        self.label_20.setToolTip(QCoreApplication.translate("HomeWidget", u"TM. Daniela Villarroel Vera ", None))
#endif // QT_CONFIG(tooltip)
        self.label_20.setText("")
#if QT_CONFIG(tooltip)
        self.label_22.setToolTip(QCoreApplication.translate("HomeWidget", u"TM. Nicol\u00e1s Ruchichi ", None))
#endif // QT_CONFIG(tooltip)
        self.label_22.setText("")
#if QT_CONFIG(tooltip)
        self.label_21.setToolTip(QCoreApplication.translate("HomeWidget", u"TM. Julio Cesar Soto Gonz\u00e1lez ", None))
#endif // QT_CONFIG(tooltip)
        self.label_21.setText("")
#if QT_CONFIG(tooltip)
        self.label_17.setToolTip(QCoreApplication.translate("HomeWidget", u"TM. Jorge Omar Mardones Mel\u00e9ndez ", None))
#endif // QT_CONFIG(tooltip)
        self.label_17.setText("")
#if QT_CONFIG(tooltip)
        self.label_23.setToolTip(QCoreApplication.translate("HomeWidget", u"TM. Mar\u00eda Paz Latorre Gonzalez ", None))
#endif // QT_CONFIG(tooltip)
        self.label_23.setText("")
#if QT_CONFIG(tooltip)
        self.label_24.setToolTip(QCoreApplication.translate("HomeWidget", u"TM. Ignacia Inarejo Inarejo ", None))
#endif // QT_CONFIG(tooltip)
        self.label_24.setText("")
    # retranslateUi

