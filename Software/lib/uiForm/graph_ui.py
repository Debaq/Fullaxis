# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'development/Form/graph.ui'
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
        self.openFrame = QtWidgets.QFrame(widget)
        self.openFrame.setMaximumSize(QtCore.QSize(16777215, 30))
        self.openFrame.setObjectName("openFrame")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.openFrame)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(4)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.btn_open = QtWidgets.QPushButton(self.openFrame)
        self.btn_open.setMinimumSize(QtCore.QSize(84, 0))
        self.btn_open.setMaximumSize(QtCore.QSize(84, 16777215))
        self.btn_open.setStyleSheet("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons_white/icons/png/16x16/cil-folder-open.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_open.setIcon(icon)
        self.btn_open.setObjectName("btn_open")
        self.horizontalLayout_3.addWidget(self.btn_open)
        self.label_File = QtWidgets.QLabel(self.openFrame)
        self.label_File.setStyleSheet("")
        self.label_File.setText("")
        self.label_File.setObjectName("label_File")
        self.horizontalLayout_3.addWidget(self.label_File)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.verticalLayout.addWidget(self.openFrame)
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
        self.btn_savearea = QtWidgets.QPushButton(self.horizontalFrame)
        self.btn_savearea.setEnabled(False)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons_white/icons/png/16x16/cil-save.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.btn_savearea.setIcon(icon2)
        self.btn_savearea.setCheckable(False)
        self.btn_savearea.setObjectName("btn_savearea")
        self.horizontalLayout_13.addWidget(self.btn_savearea)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem1)
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
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_8 = QtWidgets.QLabel(self.frameinfo_1)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_10.addWidget(self.label_8)
        self.label_7 = QtWidgets.QLabel(self.frameinfo_1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(6)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_10.addWidget(self.label_7)
        self.lbl_minRoll = QtWidgets.QLabel(self.frameinfo_1)
        font = QtGui.QFont()
        font.setPointSize(6)
        self.lbl_minRoll.setFont(font)
        self.lbl_minRoll.setObjectName("lbl_minRoll")
        self.horizontalLayout_10.addWidget(self.lbl_minRoll)
        self.label_9 = QtWidgets.QLabel(self.frameinfo_1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(6)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_10.addWidget(self.label_9)
        self.lbl_maxRoll = QtWidgets.QLabel(self.frameinfo_1)
        font = QtGui.QFont()
        font.setPointSize(6)
        self.lbl_maxRoll.setFont(font)
        self.lbl_maxRoll.setObjectName("lbl_maxRoll")
        self.horizontalLayout_10.addWidget(self.lbl_maxRoll)
        self.label_11 = QtWidgets.QLabel(self.frameinfo_1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(6)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_10.addWidget(self.label_11)
        self.layoutInfo_1.addLayout(self.horizontalLayout_10)
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
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.label_10 = QtWidgets.QLabel(self.frameinfo_2)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_11.addWidget(self.label_10)
        self.label_14 = QtWidgets.QLabel(self.frameinfo_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_14.sizePolicy().hasHeightForWidth())
        self.label_14.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(6)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.horizontalLayout_11.addWidget(self.label_14)
        self.lbl_minPitch = QtWidgets.QLabel(self.frameinfo_2)
        font = QtGui.QFont()
        font.setPointSize(6)
        self.lbl_minPitch.setFont(font)
        self.lbl_minPitch.setObjectName("lbl_minPitch")
        self.horizontalLayout_11.addWidget(self.lbl_minPitch)
        self.label_15 = QtWidgets.QLabel(self.frameinfo_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_15.sizePolicy().hasHeightForWidth())
        self.label_15.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(6)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.horizontalLayout_11.addWidget(self.label_15)
        self.lbl_maxPitch = QtWidgets.QLabel(self.frameinfo_2)
        font = QtGui.QFont()
        font.setPointSize(6)
        self.lbl_maxPitch.setFont(font)
        self.lbl_maxPitch.setObjectName("lbl_maxPitch")
        self.horizontalLayout_11.addWidget(self.lbl_maxPitch)
        self.label_12 = QtWidgets.QLabel(self.frameinfo_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(6)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_11.addWidget(self.label_12)
        self.layoutInfo_2.addLayout(self.horizontalLayout_11)
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
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.label_13 = QtWidgets.QLabel(self.frameinfo_3)
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_12.addWidget(self.label_13)
        self.label_19 = QtWidgets.QLabel(self.frameinfo_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_19.sizePolicy().hasHeightForWidth())
        self.label_19.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(6)
        self.label_19.setFont(font)
        self.label_19.setObjectName("label_19")
        self.horizontalLayout_12.addWidget(self.label_19)
        self.lbl_minYaw = QtWidgets.QLabel(self.frameinfo_3)
        font = QtGui.QFont()
        font.setPointSize(6)
        self.lbl_minYaw.setFont(font)
        self.lbl_minYaw.setObjectName("lbl_minYaw")
        self.horizontalLayout_12.addWidget(self.lbl_minYaw)
        self.label_18 = QtWidgets.QLabel(self.frameinfo_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_18.sizePolicy().hasHeightForWidth())
        self.label_18.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(6)
        self.label_18.setFont(font)
        self.label_18.setObjectName("label_18")
        self.horizontalLayout_12.addWidget(self.label_18)
        self.lbl_maxYaw = QtWidgets.QLabel(self.frameinfo_3)
        font = QtGui.QFont()
        font.setPointSize(6)
        self.lbl_maxYaw.setFont(font)
        self.lbl_maxYaw.setObjectName("lbl_maxYaw")
        self.horizontalLayout_12.addWidget(self.lbl_maxYaw)
        self.label_17 = QtWidgets.QLabel(self.frameinfo_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_17.sizePolicy().hasHeightForWidth())
        self.label_17.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(6)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.horizontalLayout_12.addWidget(self.label_17)
        self.layoutInfo_3.addLayout(self.horizontalLayout_12)
        self.frame_3.addWidget(self.frameinfo_3)
        self.verticalLayout.addLayout(self.frame_3)
        self.copyFrame = QtWidgets.QFrame(widget)
        self.copyFrame.setMaximumSize(QtCore.QSize(16777215, 200))
        font = QtGui.QFont()
        font.setPointSize(6)
        self.copyFrame.setFont(font)
        self.copyFrame.setObjectName("copyFrame")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.copyFrame)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.verticalFrame = QtWidgets.QFrame(self.copyFrame)
        self.verticalFrame.setObjectName("verticalFrame")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalFrame)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(1)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.btn_insert = QtWidgets.QPushButton(self.verticalFrame)
        self.btn_insert.setMinimumSize(QtCore.QSize(100, 0))
        self.btn_insert.setMaximumSize(QtCore.QSize(100, 16777215))
        self.btn_insert.setStyleSheet("")
        self.btn_insert.setObjectName("btn_insert")
        self.verticalLayout_3.addWidget(self.btn_insert)
        self.btn_copyThis = QtWidgets.QPushButton(self.verticalFrame)
        self.btn_copyThis.setMaximumSize(QtCore.QSize(100, 16777215))
        self.btn_copyThis.setStyleSheet("")
        self.btn_copyThis.setObjectName("btn_copyThis")
        self.verticalLayout_3.addWidget(self.btn_copyThis)
        self.btn_copyAll = QtWidgets.QPushButton(self.verticalFrame)
        self.btn_copyAll.setMaximumSize(QtCore.QSize(100, 16777215))
        self.btn_copyAll.setStyleSheet("")
        self.btn_copyAll.setObjectName("btn_copyAll")
        self.verticalLayout_3.addWidget(self.btn_copyAll)
        self.btn_ods = QtWidgets.QPushButton(self.verticalFrame)
        self.btn_ods.setObjectName("btn_ods")
        self.verticalLayout_3.addWidget(self.btn_ods)
        self.btn_clear = QtWidgets.QPushButton(self.verticalFrame)
        self.btn_clear.setMaximumSize(QtCore.QSize(100, 16777215))
        self.btn_clear.setStyleSheet("")
        self.btn_clear.setObjectName("btn_clear")
        self.verticalLayout_3.addWidget(self.btn_clear)
        self.horizontalLayout_6.addWidget(self.verticalFrame)
        self.verticalFrame_2 = QtWidgets.QFrame(self.copyFrame)
        self.verticalFrame_2.setObjectName("verticalFrame_2")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.verticalFrame_2)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.tableWidget = QtWidgets.QTableWidget(self.verticalFrame_2)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.tableWidget.setFont(font)
        self.tableWidget.setAlternatingRowColors(False)
        self.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(15)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(12, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(13, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(14, item)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(100)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(20)
        self.tableWidget.verticalHeader().setDefaultSectionSize(12)
        self.tableWidget.verticalHeader().setMinimumSectionSize(10)
        self.tableWidget.verticalHeader().setSortIndicatorShown(False)
        self.tableWidget.verticalHeader().setStretchLastSection(False)
        self.verticalLayout_5.addWidget(self.tableWidget)
        self.horizontalLayout_6.addWidget(self.verticalFrame_2)
        self.verticalLayout.addWidget(self.copyFrame)
        self.horizontalLayout_4.addLayout(self.verticalLayout)

        self.retranslateUi(widget)
        QtCore.QMetaObject.connectSlotsByName(widget)

    def retranslateUi(self, widget):
        _translate = QtCore.QCoreApplication.translate
        widget.setWindowTitle(_translate("widget", "Form"))
        self.btn_open.setText(_translate("widget", "Abrir"))
        self.label_16.setText(_translate("widget", "Herramientas"))
        self.btn_range.setText(_translate("widget", "Región |-|"))
        self.btn_amp.setText(_translate("widget", "Amplitud —"))
        self.btn_pos.setText(_translate("widget", "Tiempo |"))
        self.btn_savearea.setText(_translate("widget", "Guardar área"))
        self.label_22.setText(_translate("widget", "Roll (Lateral)"))
        self.amp_g1.setText(_translate("widget", "Amplitud (°):"))
        self.label_3.setText(_translate("widget", "— : "))
        self.ampPoint_1.setText(_translate("widget", "--"))
        self.label_4.setText(_translate("widget", "|-| : "))
        self.ampRange_1.setText(_translate("widget", "--"))
        self.tiempo_1.setText(_translate("widget", "Tiempo (s):"))
        self.lbl_tiempo_1.setText(_translate("widget", "--"))
        self.label_8.setText(_translate("widget", "|-| : "))
        self.label_7.setText(_translate("widget", "("))
        self.lbl_minRoll.setText(_translate("widget", "-"))
        self.label_9.setText(_translate("widget", ","))
        self.lbl_maxRoll.setText(_translate("widget", "-"))
        self.label_11.setText(_translate("widget", ")"))
        self.label_21.setText(_translate("widget", "Pitch (Antero-Posterior)"))
        self.amp_g2.setText(_translate("widget", "Amplitud (°):"))
        self.label.setText(_translate("widget", "— : "))
        self.ampPoint_2.setText(_translate("widget", "--"))
        self.label_2.setText(_translate("widget", "|-| : "))
        self.ampRange_2.setText(_translate("widget", "--"))
        self.tiempo_2.setText(_translate("widget", "Tiempo (s):"))
        self.lbl_tiempo_2.setText(_translate("widget", "--"))
        self.label_10.setText(_translate("widget", "|-| : "))
        self.label_14.setText(_translate("widget", "("))
        self.lbl_minPitch.setText(_translate("widget", "-"))
        self.label_15.setText(_translate("widget", ","))
        self.lbl_maxPitch.setText(_translate("widget", "-"))
        self.label_12.setText(_translate("widget", ")"))
        self.label_20.setText(_translate("widget", "Yaw (Giro)"))
        self.amp_g3.setText(_translate("widget", "Amplitud (°):"))
        self.label_5.setText(_translate("widget", "— : "))
        self.ampPoint_3.setText(_translate("widget", "--"))
        self.label_6.setText(_translate("widget", "|-| : "))
        self.ampRange_3.setText(_translate("widget", "--"))
        self.tiempo_3.setText(_translate("widget", "Tiempo (s):"))
        self.lbl_tiempo_3.setText(_translate("widget", "--"))
        self.label_13.setText(_translate("widget", "|-| : "))
        self.label_19.setText(_translate("widget", "("))
        self.lbl_minYaw.setText(_translate("widget", "-"))
        self.label_18.setText(_translate("widget", ","))
        self.lbl_maxYaw.setText(_translate("widget", "-"))
        self.label_17.setText(_translate("widget", ")"))
        self.btn_insert.setText(_translate("widget", "Agregar"))
        self.btn_copyThis.setText(_translate("widget", "Copiar Actual"))
        self.btn_copyAll.setText(_translate("widget", "Copiar todo"))
        self.btn_ods.setText(_translate("widget", "Guardar *.ods"))
        self.btn_clear.setText(_translate("widget", "Limpiar"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("widget", "aRoll (punto)"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("widget", "aRoll (segm)"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("widget", "tRoll-delta (segm)"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("widget", "tRoll (segm A)"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("widget", "tRoll (segm B)"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("widget", "aPitch (punto)"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("widget", "aPitchl (segm)"))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("widget", "tPitch-delta (segm)"))
        item = self.tableWidget.horizontalHeaderItem(8)
        item.setText(_translate("widget", "tPitch (segm A)"))
        item = self.tableWidget.horizontalHeaderItem(9)
        item.setText(_translate("widget", "tPitch (segm B)"))
        item = self.tableWidget.horizontalHeaderItem(10)
        item.setText(_translate("widget", "aYaw (punto)"))
        item = self.tableWidget.horizontalHeaderItem(11)
        item.setText(_translate("widget", "aYaw (segm)"))
        item = self.tableWidget.horizontalHeaderItem(12)
        item.setText(_translate("widget", "tYaw-delta (segm)"))
        item = self.tableWidget.horizontalHeaderItem(13)
        item.setText(_translate("widget", "tYaw (segm A)"))
        item = self.tableWidget.horizontalHeaderItem(14)
        item.setText(_translate("widget", "tYaw (segm B)"))
from resource import resource_rc
