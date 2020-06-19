# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_backyNHgFv.ui'
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

class Ui_FullAxis(object):
    def setupUi(self, FullAxis):
        if not FullAxis.objectName():
            FullAxis.setObjectName(u"FullAxis")
        FullAxis.resize(1000, 700)
        FullAxis.setMinimumSize(QSize(1000, 700))
        self.FrameMain_L0 = QWidget(FullAxis)
        self.FrameMain_L0.setObjectName(u"FrameMain_L0")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.FrameMain_L0.sizePolicy().hasHeightForWidth())
        self.FrameMain_L0.setSizePolicy(sizePolicy)
        self.layoutFrameMain_L0 = QVBoxLayout(self.FrameMain_L0)
        self.layoutFrameMain_L0.setSpacing(0)
        self.layoutFrameMain_L0.setObjectName(u"layoutFrameMain_L0")
        self.layoutFrameMain_L0.setContentsMargins(0, 0, 0, 0)
        self.FrameTop_L1 = QFrame(self.FrameMain_L0)
        self.FrameTop_L1.setObjectName(u"FrameTop_L1")
        self.FrameTop_L1.setMinimumSize(QSize(0, 65))
        self.FrameTop_L1.setMaximumSize(QSize(16777215, 65))
        self.horizontalLayout = QHBoxLayout(self.FrameTop_L1)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.ConerLeftUp = QFrame(self.FrameTop_L1)
        self.ConerLeftUp.setObjectName(u"ConerLeftUp")
        self.ConerLeftUp.setMaximumSize(QSize(60, 16777215))
        self.ConerLeftUp.setStyleSheet(u"background:rgb(120,0,46)")
        self.layoutConerLeftUp = QVBoxLayout(self.ConerLeftUp)
        self.layoutConerLeftUp.setSpacing(0)
        self.layoutConerLeftUp.setObjectName(u"layoutConerLeftUp")
        self.layoutConerLeftUp.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout.addWidget(self.ConerLeftUp)

        self.verticalFrame = QFrame(self.FrameTop_L1)
        self.verticalFrame.setObjectName(u"verticalFrame")
        self.verticalLayout = QVBoxLayout(self.verticalFrame)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.Frame_toolbar_L2 = QFrame(self.verticalFrame)
        self.Frame_toolbar_L2.setObjectName(u"Frame_toolbar_L2")
        self.Frame_toolbar_L2.setMaximumSize(QSize(16777215, 20))
        self.Frame_toolbar_L2.setStyleSheet(u"background:rgb(120,0,46)")
        self.horizontalLayout_2 = QHBoxLayout(self.Frame_toolbar_L2)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.FrameMenu_L3 = QFrame(self.Frame_toolbar_L2)
        self.FrameMenu_L3.setObjectName(u"FrameMenu_L3")
        self.FrameMenu_L3.setStyleSheet(u"")
        self.layoutFrameMenu_L3 = QHBoxLayout(self.FrameMenu_L3)
        self.layoutFrameMenu_L3.setSpacing(0)
        self.layoutFrameMenu_L3.setObjectName(u"layoutFrameMenu_L3")
        self.layoutFrameMenu_L3.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_2.addWidget(self.FrameMenu_L3)

        self.FrameButtonWindow_L3 = QFrame(self.Frame_toolbar_L2)
        self.FrameButtonWindow_L3.setObjectName(u"FrameButtonWindow_L3")
        self.FrameButtonWindow_L3.setMaximumSize(QSize(100, 16777215))
        self.layoutFrameButtonWindow_L3 = QHBoxLayout(self.FrameButtonWindow_L3)
        self.layoutFrameButtonWindow_L3.setSpacing(0)
        self.layoutFrameButtonWindow_L3.setObjectName(u"layoutFrameButtonWindow_L3")
        self.layoutFrameButtonWindow_L3.setContentsMargins(0, 0, 0, 0)
        self.lbl_user_title = QLabel(self.FrameButtonWindow_L3)
        self.lbl_user_title.setObjectName(u"lbl_user_title")
        self.lbl_user_title.setStyleSheet(u"color:white")

        self.layoutFrameButtonWindow_L3.addWidget(self.lbl_user_title)


        self.horizontalLayout_2.addWidget(self.FrameButtonWindow_L3)


        self.verticalLayout.addWidget(self.Frame_toolbar_L2)

        self.Frame_menubar_L2 = QFrame(self.verticalFrame)
        self.Frame_menubar_L2.setObjectName(u"Frame_menubar_L2")
        self.Frame_menubar_L2.setStyleSheet(u"background:rgb(173,19,87)")
        self.layoutFrame_menubar_L2 = QHBoxLayout(self.Frame_menubar_L2)
        self.layoutFrame_menubar_L2.setSpacing(0)
        self.layoutFrame_menubar_L2.setObjectName(u"layoutFrame_menubar_L2")
        self.layoutFrame_menubar_L2.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout.addWidget(self.Frame_menubar_L2)


        self.horizontalLayout.addWidget(self.verticalFrame)


        self.layoutFrameMain_L0.addWidget(self.FrameTop_L1)

        self.FrameCenter_L1 = QFrame(self.FrameMain_L0)
        self.FrameCenter_L1.setObjectName(u"FrameCenter_L1")
        self.layoutFrameCenter_L1 = QHBoxLayout(self.FrameCenter_L1)
        self.layoutFrameCenter_L1.setSpacing(0)
        self.layoutFrameCenter_L1.setObjectName(u"layoutFrameCenter_L1")
        self.layoutFrameCenter_L1.setContentsMargins(0, 0, 0, 0)
        self.FrameMenuLeft_L2 = QFrame(self.FrameCenter_L1)
        self.FrameMenuLeft_L2.setObjectName(u"FrameMenuLeft_L2")
        self.FrameMenuLeft_L2.setMinimumSize(QSize(60, 0))
        self.FrameMenuLeft_L2.setMaximumSize(QSize(60, 16777215))
        self.FrameMenuLeft_L2.setStyleSheet(u"background:rgb(120,0,46)")
        self.LayoutFrameMenuLeft_L2 = QVBoxLayout(self.FrameMenuLeft_L2)
        self.LayoutFrameMenuLeft_L2.setSpacing(0)
        self.LayoutFrameMenuLeft_L2.setObjectName(u"LayoutFrameMenuLeft_L2")
        self.LayoutFrameMenuLeft_L2.setContentsMargins(0, 0, 0, 0)
        self.FrameMenuLeftDown_L3 = QFrame(self.FrameMenuLeft_L2)
        self.FrameMenuLeftDown_L3.setObjectName(u"FrameMenuLeftDown_L3")
        self.layoutFrameMenuLeftDown_L2_2 = QVBoxLayout(self.FrameMenuLeftDown_L3)
        self.layoutFrameMenuLeftDown_L2_2.setSpacing(10)
        self.layoutFrameMenuLeftDown_L2_2.setObjectName(u"layoutFrameMenuLeftDown_L2_2")
        self.layoutFrameMenuLeftDown_L2_2.setContentsMargins(0, 5, 0, 0)
        self.btn_MenuHome = QPushButton(self.FrameMenuLeftDown_L3)
        self.btn_MenuHome.setObjectName(u"btn_MenuHome")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.btn_MenuHome.sizePolicy().hasHeightForWidth())
        self.btn_MenuHome.setSizePolicy(sizePolicy1)
        self.btn_MenuHome.setMinimumSize(QSize(40, 40))
        self.btn_MenuHome.setStyleSheet(u"QPushButton {\n"
"	image: url(:/icons svg/icons/svg/fullaxis.svg);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"	border: none;\n"
"}QPushButton:hover {\n"
"	border-left: 5px solid  rgb(227,80,131);\n"
"	background-position: center ;\n"
"\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: rgb(173,19,87);\n"
"	\n"
"}")
        self.btn_MenuHome.setIconSize(QSize(30, 30))

        self.layoutFrameMenuLeftDown_L2_2.addWidget(self.btn_MenuHome)

        self.btn_MenuUser = QPushButton(self.FrameMenuLeftDown_L3)
        self.btn_MenuUser.setObjectName(u"btn_MenuUser")
        sizePolicy1.setHeightForWidth(self.btn_MenuUser.sizePolicy().hasHeightForWidth())
        self.btn_MenuUser.setSizePolicy(sizePolicy1)
        self.btn_MenuUser.setMinimumSize(QSize(40, 40))
        self.btn_MenuUser.setStyleSheet(u"QPushButton {\n"
"	background-image: url(:/icons svg/icons/svg/folder.svg);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"	border: none;\n"
"}\n"
"QPushButton:hover {\n"
"	border-left: 5px solid  rgb(227,80,131);\n"
"	background-position: center ;\n"
"\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: rgb(173,19,87);\n"
"	\n"
"}")
        self.btn_MenuUser.setIconSize(QSize(40, 40))

        self.layoutFrameMenuLeftDown_L2_2.addWidget(self.btn_MenuUser)


        self.LayoutFrameMenuLeft_L2.addWidget(self.FrameMenuLeftDown_L3, 0, Qt.AlignTop)

        self.FrameMenuLeftTop_L3 = QFrame(self.FrameMenuLeft_L2)
        self.FrameMenuLeftTop_L3.setObjectName(u"FrameMenuLeftTop_L3")
        self.FrameMenuLeftTop_L3.setMaximumSize(QSize(16777215, 100))
        self.layoutFrameMenuLeftTop_L2 = QVBoxLayout(self.FrameMenuLeftTop_L3)
        self.layoutFrameMenuLeftTop_L2.setSpacing(0)
        self.layoutFrameMenuLeftTop_L2.setObjectName(u"layoutFrameMenuLeftTop_L2")
        self.layoutFrameMenuLeftTop_L2.setContentsMargins(0, 0, 0, 0)
        self.btn_MenuInfo = QPushButton(self.FrameMenuLeftTop_L3)
        self.btn_MenuInfo.setObjectName(u"btn_MenuInfo")
        self.btn_MenuInfo.setMinimumSize(QSize(24, 24))
        self.btn_MenuInfo.setStyleSheet(u"QPushButton {\n"
"	image: url(:/icons svg/icons/svg/help-about.svg);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"	border: none;\n"
"}\n"
"QPushButton:hover {\n"
"	image: url(:/icons svg/icons/svg/help-aboutrgb.svg);\n"
"}\n"
"QPushButton:pressed {	\n"
"	image: url(:/icons svg/icons/svg/help-aboutrgb.svg);\n"
"}")
        self.btn_MenuInfo.setFlat(True)

        self.layoutFrameMenuLeftTop_L2.addWidget(self.btn_MenuInfo)

        self.btn_MenuPlugins = QPushButton(self.FrameMenuLeftTop_L3)
        self.btn_MenuPlugins.setObjectName(u"btn_MenuPlugins")
        self.btn_MenuPlugins.setMinimumSize(QSize(24, 24))
        self.btn_MenuPlugins.setStyleSheet(u"QPushButton {\n"
"	image: url(:/icons svg/icons/svg/plugins.svg);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"	border: none;\n"
"}\n"
"QPushButton:hover {\n"
"	image: url(:/icons svg/icons/svg/pluginsrgb.svg);\n"
"}\n"
"QPushButton:pressed {	\n"
"	image: url(:/icons svg/icons/svg/pluginsrgb.svg);\n"
"}")
        self.btn_MenuPlugins.setFlat(True)

        self.layoutFrameMenuLeftTop_L2.addWidget(self.btn_MenuPlugins)

        self.btn_MenuSetting = QPushButton(self.FrameMenuLeftTop_L3)
        self.btn_MenuSetting.setObjectName(u"btn_MenuSetting")
        self.btn_MenuSetting.setMinimumSize(QSize(24, 24))
        self.btn_MenuSetting.setStyleSheet(u"QPushButton {\n"
"	image: url(:/icons svg/icons/svg/adjustlevels.svg);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"	border: none;\n"
"}\n"
"QPushButton:hover {\n"
"	image: url(:/icons svg/icons/svg/adjustrgb.svg);\n"
"}\n"
"QPushButton:pressed {	\n"
"	image: url(:/icons svg/icons/svg/adjustrgb.svg);\n"
"}")
        self.btn_MenuSetting.setCheckable(False)
        self.btn_MenuSetting.setAutoDefault(False)
        self.btn_MenuSetting.setFlat(True)

        self.layoutFrameMenuLeftTop_L2.addWidget(self.btn_MenuSetting)


        self.LayoutFrameMenuLeft_L2.addWidget(self.FrameMenuLeftTop_L3)

        self.FrameMenuLeftinfo_L3 = QWidget(self.FrameMenuLeft_L2)
        self.FrameMenuLeftinfo_L3.setObjectName(u"FrameMenuLeftinfo_L3")
        self.FrameMenuLeftinfo_L3.setMinimumSize(QSize(0, 23))
        self.FrameMenuLeftinfo_L3.setMaximumSize(QSize(16777215, 23))
        self.FrameMenuLeftinfo_L3.setStyleSheet(u"background:rgb(0,122,204)")
        self.layoutFrameMenuLeftinfo_L3 = QHBoxLayout(self.FrameMenuLeftinfo_L3)
        self.layoutFrameMenuLeftinfo_L3.setSpacing(0)
        self.layoutFrameMenuLeftinfo_L3.setObjectName(u"layoutFrameMenuLeftinfo_L3")
        self.layoutFrameMenuLeftinfo_L3.setContentsMargins(0, 0, 0, 0)
        self.labelMenuLeftInfo = QLabel(self.FrameMenuLeftinfo_L3)
        self.labelMenuLeftInfo.setObjectName(u"labelMenuLeftInfo")
        font = QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QFont.PreferAntialias)
        self.labelMenuLeftInfo.setFont(font)
        self.labelMenuLeftInfo.setStyleSheet(u"color:white")
        self.labelMenuLeftInfo.setTextFormat(Qt.RichText)
        self.labelMenuLeftInfo.setScaledContents(False)
        self.labelMenuLeftInfo.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.labelMenuLeftInfo.setMargin(-6)
        self.labelMenuLeftInfo.setIndent(0)

        self.layoutFrameMenuLeftinfo_L3.addWidget(self.labelMenuLeftInfo)


        self.LayoutFrameMenuLeft_L2.addWidget(self.FrameMenuLeftinfo_L3)


        self.layoutFrameCenter_L1.addWidget(self.FrameMenuLeft_L2)

        self.FrameCenter_L2 = QFrame(self.FrameCenter_L1)
        self.FrameCenter_L2.setObjectName(u"FrameCenter_L2")
        self.layoutFrameCenter_L2 = QVBoxLayout(self.FrameCenter_L2)
        self.layoutFrameCenter_L2.setSpacing(0)
        self.layoutFrameCenter_L2.setObjectName(u"layoutFrameCenter_L2")
        self.layoutFrameCenter_L2.setContentsMargins(0, 0, 0, 0)
        self.FrameCenter_L4 = QFrame(self.FrameCenter_L2)
        self.FrameCenter_L4.setObjectName(u"FrameCenter_L4")
        self.layoutFrameCenter_L4 = QHBoxLayout(self.FrameCenter_L4)
        self.layoutFrameCenter_L4.setSpacing(0)
        self.layoutFrameCenter_L4.setObjectName(u"layoutFrameCenter_L4")
        self.layoutFrameCenter_L4.setContentsMargins(0, 0, 0, 0)
        self.FrameOption_L5 = QFrame(self.FrameCenter_L4)
        self.FrameOption_L5.setObjectName(u"FrameOption_L5")
        self.FrameOption_L5.setMinimumSize(QSize(0, 0))
        self.FrameOption_L5.setMaximumSize(QSize(200, 16777215))
        self.FrameOption_L5.setStyleSheet(u"background-color: rgb(225, 226, 225);\n"
"border-right	: 1px solid gray;")
        self.FrameOption_L5.setFrameShape(QFrame.NoFrame)
        self.layaoutFrameOption_L5 = QVBoxLayout(self.FrameOption_L5)
        self.layaoutFrameOption_L5.setSpacing(0)
        self.layaoutFrameOption_L5.setObjectName(u"layaoutFrameOption_L5")
        self.layaoutFrameOption_L5.setContentsMargins(0, 0, 0, 0)
        self.TitleExplorer_L6 = QFrame(self.FrameOption_L5)
        self.TitleExplorer_L6.setObjectName(u"TitleExplorer_L6")
        self.TitleExplorer_L6.setEnabled(True)
        self.TitleExplorer_L6.setMinimumSize(QSize(0, 10))
        self.TitleExplorer_L6.setMaximumSize(QSize(16777215, 15))
        self.TitleExplorer_L6.setStyleSheet(u"border-bottom : 1px solid gray;")
        self.layoutTitleExplorer_L6 = QHBoxLayout(self.TitleExplorer_L6)
        self.layoutTitleExplorer_L6.setSpacing(0)
        self.layoutTitleExplorer_L6.setObjectName(u"layoutTitleExplorer_L6")
        self.layoutTitleExplorer_L6.setContentsMargins(5, 0, 0, 0)
        self.lbl_Explorer = QLabel(self.TitleExplorer_L6)
        self.lbl_Explorer.setObjectName(u"lbl_Explorer")
        self.lbl_Explorer.setEnabled(True)
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.lbl_Explorer.sizePolicy().hasHeightForWidth())
        self.lbl_Explorer.setSizePolicy(sizePolicy2)
        font1 = QFont()
        font1.setPointSize(9)
        font1.setBold(True)
        font1.setWeight(75)
        self.lbl_Explorer.setFont(font1)
        self.lbl_Explorer.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.layoutTitleExplorer_L6.addWidget(self.lbl_Explorer)

        self.btn_ContractExplorer = QPushButton(self.TitleExplorer_L6)
        self.btn_ContractExplorer.setObjectName(u"btn_ContractExplorer")
        self.btn_ContractExplorer.setMinimumSize(QSize(20, 0))
        self.btn_ContractExplorer.setMaximumSize(QSize(20, 16777215))
        font2 = QFont()
        font2.setPointSize(6)
        font2.setBold(False)
        font2.setWeight(50)
        font2.setKerning(False)
        self.btn_ContractExplorer.setFont(font2)
        self.btn_ContractExplorer.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);\n"
"	border: none;\n"
"")

        self.layoutTitleExplorer_L6.addWidget(self.btn_ContractExplorer)


        self.layaoutFrameOption_L5.addWidget(self.TitleExplorer_L6)

        self.ContentExplorer = QFrame(self.FrameOption_L5)
        self.ContentExplorer.setObjectName(u"ContentExplorer")
        self.verticalLayout_5 = QVBoxLayout(self.ContentExplorer)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)

        self.layaoutFrameOption_L5.addWidget(self.ContentExplorer)


        self.layoutFrameCenter_L4.addWidget(self.FrameOption_L5)

        self.FrameCenter_L5 = QFrame(self.FrameCenter_L4)
        self.FrameCenter_L5.setObjectName(u"FrameCenter_L5")
        self.FrameCenter_L5.setStyleSheet(u"background-color: rgb(44, 49, 60);")
        self.layoutFrameCenter_L5 = QHBoxLayout(self.FrameCenter_L5)
        self.layoutFrameCenter_L5.setSpacing(0)
        self.layoutFrameCenter_L5.setObjectName(u"layoutFrameCenter_L5")
        self.layoutFrameCenter_L5.setContentsMargins(0, 0, 0, 0)

        self.layoutFrameCenter_L4.addWidget(self.FrameCenter_L5)


        self.layoutFrameCenter_L2.addWidget(self.FrameCenter_L4)

        self.FrameInfo_L3 = QFrame(self.FrameCenter_L2)
        self.FrameInfo_L3.setObjectName(u"FrameInfo_L3")
        self.FrameInfo_L3.setMinimumSize(QSize(0, 23))
        self.FrameInfo_L3.setMaximumSize(QSize(16777215, 23))
        self.FrameInfo_L3.setStyleSheet(u"background:rgb(0,122,204)")
        self.layoutFrameInfo_L3 = QHBoxLayout(self.FrameInfo_L3)
        self.layoutFrameInfo_L3.setSpacing(0)
        self.layoutFrameInfo_L3.setObjectName(u"layoutFrameInfo_L3")
        self.layoutFrameInfo_L3.setContentsMargins(0, 0, 0, 0)

        self.layoutFrameCenter_L2.addWidget(self.FrameInfo_L3)


        self.layoutFrameCenter_L1.addWidget(self.FrameCenter_L2)


        self.layoutFrameMain_L0.addWidget(self.FrameCenter_L1)

        FullAxis.setCentralWidget(self.FrameMain_L0)

        self.retranslateUi(FullAxis)

        self.btn_MenuSetting.setDefault(False)


        QMetaObject.connectSlotsByName(FullAxis)
    # setupUi

    def retranslateUi(self, FullAxis):
        FullAxis.setWindowTitle(QCoreApplication.translate("FullAxis", u"FullAxis", None))
        self.lbl_user_title.setText("")
#if QT_CONFIG(tooltip)
        self.btn_MenuHome.setToolTip(QCoreApplication.translate("FullAxis", u"<html><head/><body><p><span style=\" font-weight:600;\">Inicio</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.btn_MenuHome.setText("")
#if QT_CONFIG(tooltip)
        self.btn_MenuUser.setToolTip(QCoreApplication.translate("FullAxis", u"<html><head/><body><p><span style=\" font-weight:600;\">\u00c1rea de Trabajo</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.btn_MenuUser.setText("")
        self.btn_MenuInfo.setText("")
        self.btn_MenuPlugins.setText("")
        self.btn_MenuSetting.setText("")
        self.labelMenuLeftInfo.setText(QCoreApplication.translate("FullAxis", u"<html><head/><body><p><br/></p></body></html>", None))
        self.lbl_Explorer.setText(QCoreApplication.translate("FullAxis", u"EXPLORADOR", None))
        self.btn_ContractExplorer.setText(QCoreApplication.translate("FullAxis", u"<", None))
    # retranslateUi

