# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'development/Form/compare.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_widget(object):
    def setupUi(self, widget):
        widget.setObjectName("widget")
        widget.resize(779, 806)
        widget.setStyleSheet("                QPushButton {\n"
"                    Text-align:center;\n"
"\n"
"                    color:rgb(238, 238, 236);\n"
"                    background-color: rgb(55, 144, 152);\n"
"                }\n"
"                QPushButton:hover {\n"
"                    background-color: rgb(0, 98, 106);\n"
"                }\n"
"                QPushButton:pressed {\n"
"                    text-decoration: underline;\n"
"                }\n"
"QPushButton:checked{\n"
"background-color: rgb(80, 80, 80);\n"
"}\n"
"\n"
"QLabel{\n"
"color: rgb(238, 238, 236);\n"
"}\n"
"QFrame{\n"
"color: rgb(238, 238, 236);\n"
"}")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(widget)
        self.horizontalLayout_4.setContentsMargins(4, 4, 4, 4)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(-1, 0, -1, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.openFrame1 = QtWidgets.QFrame(widget)
        self.openFrame1.setMaximumSize(QtCore.QSize(16777215, 30))
        self.openFrame1.setObjectName("openFrame1")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.openFrame1)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(4)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.btn_open1 = QtWidgets.QPushButton(self.openFrame1)
        self.btn_open1.setMinimumSize(QtCore.QSize(84, 0))
        self.btn_open1.setMaximumSize(QtCore.QSize(84, 16777215))
        self.btn_open1.setStyleSheet("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons_white/icons/png/16x16/cil-folder-open.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_open1.setIcon(icon)
        self.btn_open1.setObjectName("btn_open1")
        self.horizontalLayout_3.addWidget(self.btn_open1)
        self.label_File1 = QtWidgets.QLabel(self.openFrame1)
        self.label_File1.setStyleSheet("")
        self.label_File1.setText("")
        self.label_File1.setObjectName("label_File1")
        self.horizontalLayout_3.addWidget(self.label_File1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.verticalLayout_2.addWidget(self.openFrame1)
        self.openFrame2 = QtWidgets.QHBoxLayout()
        self.openFrame2.setSpacing(4)
        self.openFrame2.setObjectName("openFrame2")
        self.btn_open2 = QtWidgets.QPushButton(widget)
        self.btn_open2.setMinimumSize(QtCore.QSize(84, 0))
        self.btn_open2.setMaximumSize(QtCore.QSize(84, 16777215))
        self.btn_open2.setIcon(icon)
        self.btn_open2.setObjectName("btn_open2")
        self.openFrame2.addWidget(self.btn_open2)
        self.label_File2 = QtWidgets.QLabel(widget)
        self.label_File2.setText("")
        self.label_File2.setObjectName("label_File2")
        self.openFrame2.addWidget(self.label_File2)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.openFrame2.addItem(spacerItem1)
        self.verticalLayout_2.addLayout(self.openFrame2)
        self.verticalLayout.addLayout(self.verticalLayout_2)
        self.horizontalFrame = QtWidgets.QFrame(widget)
        self.horizontalFrame.setMinimumSize(QtCore.QSize(0, 0))
        self.horizontalFrame.setObjectName("horizontalFrame")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout(self.horizontalFrame)
        self.horizontalLayout_13.setContentsMargins(-1, -1, 0, -1)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.label_16 = QtWidgets.QLabel(self.horizontalFrame)
        self.label_16.setObjectName("label_16")
        self.horizontalLayout_13.addWidget(self.label_16)
        self.btn_range = QtWidgets.QPushButton(self.horizontalFrame)
        self.btn_range.setMinimumSize(QtCore.QSize(30, 0))
        self.btn_range.setStyleSheet("\n"
"QPushButton:checked{\n"
"                    background-color: rgb(80, 80, 80);\n"
"}\n"
"")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons_white/icons/png/16x16/cil-lock-unlocked.png"), QtGui.QIcon.Selected, QtGui.QIcon.Off)
        icon1.addPixmap(QtGui.QPixmap(":/icons_white/icons/png/16x16/cil-lock-locked.png"), QtGui.QIcon.Selected, QtGui.QIcon.On)
        self.btn_range.setIcon(icon1)
        self.btn_range.setCheckable(True)
        self.btn_range.setObjectName("btn_range")
        self.horizontalLayout_13.addWidget(self.btn_range)
        self.btn_amp = QtWidgets.QPushButton(self.horizontalFrame)
        self.btn_amp.setMinimumSize(QtCore.QSize(30, 0))
        self.btn_amp.setStyleSheet("QPushButton:checked{\n"
"                    background-color: rgb(80, 80, 80);\n"
"}\n"
"")
        self.btn_amp.setIcon(icon1)
        self.btn_amp.setCheckable(True)
        self.btn_amp.setObjectName("btn_amp")
        self.horizontalLayout_13.addWidget(self.btn_amp)
        self.btn_pos = QtWidgets.QPushButton(self.horizontalFrame)
        self.btn_pos.setMinimumSize(QtCore.QSize(30, 0))
        self.btn_pos.setStyleSheet("")
        self.btn_pos.setIcon(icon1)
        self.btn_pos.setCheckable(True)
        self.btn_pos.setChecked(True)
        self.btn_pos.setObjectName("btn_pos")
        self.horizontalLayout_13.addWidget(self.btn_pos)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem2)
        self.verticalLayout.addWidget(self.horizontalFrame)
        self.label_22 = QtWidgets.QLabel(widget)
        self.label_22.setObjectName("label_22")
        self.verticalLayout.addWidget(self.label_22)
        self.frame_1 = QtWidgets.QHBoxLayout()
        self.frame_1.setSpacing(6)
        self.frame_1.setObjectName("frame_1")
        self.frame_graph_1 = QtWidgets.QFrame(widget)
        self.frame_graph_1.setMinimumSize(QtCore.QSize(0, 150))
        self.frame_graph_1.setObjectName("frame_graph_1")
        self.layout_graph_1 = QtWidgets.QVBoxLayout(self.frame_graph_1)
        self.layout_graph_1.setContentsMargins(0, 0, 0, 0)
        self.layout_graph_1.setObjectName("layout_graph_1")
        self.frame_1.addWidget(self.frame_graph_1)
        self.frameinfo_1 = QtWidgets.QFrame(widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frameinfo_1.sizePolicy().hasHeightForWidth())
        self.frameinfo_1.setSizePolicy(sizePolicy)
        self.frameinfo_1.setMinimumSize(QtCore.QSize(100, 100))
        self.frameinfo_1.setMaximumSize(QtCore.QSize(100, 16777215))
        self.frameinfo_1.setObjectName("frameinfo_1")
        self.layoutInfo_1 = QtWidgets.QVBoxLayout(self.frameinfo_1)
        self.layoutInfo_1.setContentsMargins(0, 0, 4, 0)
        self.layoutInfo_1.setSpacing(4)
        self.layoutInfo_1.setObjectName("layoutInfo_1")
        self.amp_g1 = QtWidgets.QLabel(self.frameinfo_1)
        self.amp_g1.setStyleSheet("")
        self.amp_g1.setObjectName("amp_g1")
        self.layoutInfo_1.addWidget(self.amp_g1)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_3 = QtWidgets.QLabel(self.frameinfo_1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_5.addWidget(self.label_3)
        self.ampPoint_1 = QtWidgets.QLabel(self.frameinfo_1)
        self.ampPoint_1.setStyleSheet("")
        self.ampPoint_1.setObjectName("ampPoint_1")
        self.horizontalLayout_5.addWidget(self.ampPoint_1)
        self.layoutInfo_1.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_4 = QtWidgets.QLabel(self.frameinfo_1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_7.addWidget(self.label_4)
        self.ampRange_1 = QtWidgets.QLabel(self.frameinfo_1)
        self.ampRange_1.setStyleSheet("")
        self.ampRange_1.setObjectName("ampRange_1")
        self.horizontalLayout_7.addWidget(self.ampRange_1)
        self.layoutInfo_1.addLayout(self.horizontalLayout_7)
        self.tiempo_1 = QtWidgets.QLabel(self.frameinfo_1)
        self.tiempo_1.setStyleSheet("")
        self.tiempo_1.setObjectName("tiempo_1")
        self.layoutInfo_1.addWidget(self.tiempo_1)
        self.lbl_tiempo_1 = QtWidgets.QLabel(self.frameinfo_1)
        self.lbl_tiempo_1.setAutoFillBackground(False)
        self.lbl_tiempo_1.setStyleSheet("")
        self.lbl_tiempo_1.setObjectName("lbl_tiempo_1")
        self.layoutInfo_1.addWidget(self.lbl_tiempo_1)
        self.frame_1.addWidget(self.frameinfo_1)
        self.verticalLayout.addLayout(self.frame_1)
        self.label_21 = QtWidgets.QLabel(widget)
        self.label_21.setObjectName("label_21")
        self.verticalLayout.addWidget(self.label_21)
        self.frame_2 = QtWidgets.QHBoxLayout()
        self.frame_2.setSpacing(6)
        self.frame_2.setObjectName("frame_2")
        self.frame_graph_2 = QtWidgets.QFrame(widget)
        self.frame_graph_2.setMinimumSize(QtCore.QSize(0, 150))
        self.frame_graph_2.setObjectName("frame_graph_2")
        self.layout_graph_2 = QtWidgets.QVBoxLayout(self.frame_graph_2)
        self.layout_graph_2.setContentsMargins(0, 0, 0, 0)
        self.layout_graph_2.setObjectName("layout_graph_2")
        self.frame_2.addWidget(self.frame_graph_2)
        self.frameinfo_2 = QtWidgets.QFrame(widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frameinfo_2.sizePolicy().hasHeightForWidth())
        self.frameinfo_2.setSizePolicy(sizePolicy)
        self.frameinfo_2.setMinimumSize(QtCore.QSize(100, 100))
        self.frameinfo_2.setMaximumSize(QtCore.QSize(100, 16777215))
        self.frameinfo_2.setObjectName("frameinfo_2")
        self.layoutInfo_2 = QtWidgets.QVBoxLayout(self.frameinfo_2)
        self.layoutInfo_2.setContentsMargins(0, 0, 4, 0)
        self.layoutInfo_2.setSpacing(4)
        self.layoutInfo_2.setObjectName("layoutInfo_2")
        self.amp_g2 = QtWidgets.QLabel(self.frameinfo_2)
        self.amp_g2.setStyleSheet("")
        self.amp_g2.setObjectName("amp_g2")
        self.layoutInfo_2.addWidget(self.amp_g2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(0, -1, -1, -1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.frameinfo_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.ampPoint_2 = QtWidgets.QLabel(self.frameinfo_2)
        self.ampPoint_2.setStyleSheet("")
        self.ampPoint_2.setObjectName("ampPoint_2")
        self.horizontalLayout.addWidget(self.ampPoint_2)
        self.layoutInfo_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(0, -1, -1, -1)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.frameinfo_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.ampRange_2 = QtWidgets.QLabel(self.frameinfo_2)
        self.ampRange_2.setStyleSheet("")
        self.ampRange_2.setObjectName("ampRange_2")
        self.horizontalLayout_2.addWidget(self.ampRange_2)
        self.layoutInfo_2.addLayout(self.horizontalLayout_2)
        self.tiempo_2 = QtWidgets.QLabel(self.frameinfo_2)
        self.tiempo_2.setStyleSheet("")
        self.tiempo_2.setObjectName("tiempo_2")
        self.layoutInfo_2.addWidget(self.tiempo_2)
        self.lbl_tiempo_2 = QtWidgets.QLabel(self.frameinfo_2)
        self.lbl_tiempo_2.setStyleSheet("")
        self.lbl_tiempo_2.setObjectName("lbl_tiempo_2")
        self.layoutInfo_2.addWidget(self.lbl_tiempo_2)
        self.frame_2.addWidget(self.frameinfo_2)
        self.verticalLayout.addLayout(self.frame_2)
        self.label_20 = QtWidgets.QLabel(widget)
        self.label_20.setObjectName("label_20")
        self.verticalLayout.addWidget(self.label_20)
        self.frame_3 = QtWidgets.QHBoxLayout()
        self.frame_3.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.frame_3.setSpacing(6)
        self.frame_3.setObjectName("frame_3")
        self.frame_graph_3 = QtWidgets.QFrame(widget)
        self.frame_graph_3.setMinimumSize(QtCore.QSize(0, 150))
        self.frame_graph_3.setObjectName("frame_graph_3")
        self.layout_graph_3 = QtWidgets.QVBoxLayout(self.frame_graph_3)
        self.layout_graph_3.setContentsMargins(0, 0, 0, 0)
        self.layout_graph_3.setObjectName("layout_graph_3")
        self.frame_3.addWidget(self.frame_graph_3)
        self.frameinfo_3 = QtWidgets.QFrame(widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frameinfo_3.sizePolicy().hasHeightForWidth())
        self.frameinfo_3.setSizePolicy(sizePolicy)
        self.frameinfo_3.setMinimumSize(QtCore.QSize(100, 100))
        self.frameinfo_3.setMaximumSize(QtCore.QSize(100, 16777215))
        self.frameinfo_3.setObjectName("frameinfo_3")
        self.layoutInfo_3 = QtWidgets.QVBoxLayout(self.frameinfo_3)
        self.layoutInfo_3.setContentsMargins(0, 0, 4, 0)
        self.layoutInfo_3.setSpacing(4)
        self.layoutInfo_3.setObjectName("layoutInfo_3")
        self.amp_g3 = QtWidgets.QLabel(self.frameinfo_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.amp_g3.sizePolicy().hasHeightForWidth())
        self.amp_g3.setSizePolicy(sizePolicy)
        self.amp_g3.setMinimumSize(QtCore.QSize(0, 25))
        self.amp_g3.setStyleSheet("")
        self.amp_g3.setObjectName("amp_g3")
        self.layoutInfo_3.addWidget(self.amp_g3)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_5 = QtWidgets.QLabel(self.frameinfo_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_8.addWidget(self.label_5)
        self.ampPoint_3 = QtWidgets.QLabel(self.frameinfo_3)
        self.ampPoint_3.setStyleSheet("")
        self.ampPoint_3.setObjectName("ampPoint_3")
        self.horizontalLayout_8.addWidget(self.ampPoint_3)
        self.layoutInfo_3.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_6 = QtWidgets.QLabel(self.frameinfo_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_9.addWidget(self.label_6)
        self.ampRange_3 = QtWidgets.QLabel(self.frameinfo_3)
        self.ampRange_3.setStyleSheet("")
        self.ampRange_3.setObjectName("ampRange_3")
        self.horizontalLayout_9.addWidget(self.ampRange_3)
        self.layoutInfo_3.addLayout(self.horizontalLayout_9)
        self.tiempo_3 = QtWidgets.QLabel(self.frameinfo_3)
        self.tiempo_3.setMinimumSize(QtCore.QSize(0, 18))
        self.tiempo_3.setStyleSheet("")
        self.tiempo_3.setObjectName("tiempo_3")
        self.layoutInfo_3.addWidget(self.tiempo_3)
        self.lbl_tiempo_3 = QtWidgets.QLabel(self.frameinfo_3)
        self.lbl_tiempo_3.setStyleSheet("")
        self.lbl_tiempo_3.setObjectName("lbl_tiempo_3")
        self.layoutInfo_3.addWidget(self.lbl_tiempo_3)
        self.frame_3.addWidget(self.frameinfo_3)
        self.verticalLayout.addLayout(self.frame_3)
        self.horizontalLayout_4.addLayout(self.verticalLayout)

        self.retranslateUi(widget)
        QtCore.QMetaObject.connectSlotsByName(widget)

    def retranslateUi(self, widget):
        _translate = QtCore.QCoreApplication.translate
        widget.setWindowTitle(_translate("widget", "Form"))
        self.btn_open1.setText(_translate("widget", "Abrir 1"))
        self.btn_open2.setText(_translate("widget", "Abrir 2"))
        self.label_16.setText(_translate("widget", "Herramientas"))
        self.btn_range.setText(_translate("widget", "Región |-|"))
        self.btn_amp.setText(_translate("widget", "Amplitud —"))
        self.btn_pos.setText(_translate("widget", "Tiempo |"))
        self.label_22.setText(_translate("widget", "Roll (Lateral)"))
        self.amp_g1.setText(_translate("widget", "Amplitud (°):"))
        self.label_3.setText(_translate("widget", "— : "))
        self.ampPoint_1.setText(_translate("widget", "--"))
        self.label_4.setText(_translate("widget", "|-| : "))
        self.ampRange_1.setText(_translate("widget", "--"))
        self.tiempo_1.setText(_translate("widget", "Tiempo (s):"))
        self.lbl_tiempo_1.setText(_translate("widget", "--"))
        self.label_21.setText(_translate("widget", "Pitch (Antero-Posterior)"))
        self.amp_g2.setText(_translate("widget", "Amplitud (°):"))
        self.label.setText(_translate("widget", "— : "))
        self.ampPoint_2.setText(_translate("widget", "--"))
        self.label_2.setText(_translate("widget", "|-| : "))
        self.ampRange_2.setText(_translate("widget", "--"))
        self.tiempo_2.setText(_translate("widget", "Tiempo (s):"))
        self.lbl_tiempo_2.setText(_translate("widget", "--"))
        self.label_20.setText(_translate("widget", "Yaw (Giro)"))
        self.amp_g3.setText(_translate("widget", "Amplitud (°):"))
        self.label_5.setText(_translate("widget", "— : "))
        self.ampPoint_3.setText(_translate("widget", "--"))
        self.label_6.setText(_translate("widget", "|-| : "))
        self.ampRange_3.setText(_translate("widget", "--"))
        self.tiempo_3.setText(_translate("widget", "Tiempo (s):"))
        self.lbl_tiempo_3.setText(_translate("widget", "--"))
from resource import resource_rc
