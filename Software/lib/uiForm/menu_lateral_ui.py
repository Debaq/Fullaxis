# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'development/Form/menu_lateral.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Lateral_menu(object):
    def setupUi(self, Lateral_menu):
        Lateral_menu.setObjectName("Lateral_menu")
        Lateral_menu.resize(100, 525)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Lateral_menu.sizePolicy().hasHeightForWidth())
        Lateral_menu.setSizePolicy(sizePolicy)
        Lateral_menu.setMinimumSize(QtCore.QSize(100, 0))
        Lateral_menu.setMaximumSize(QtCore.QSize(100, 16777215))
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Lateral_menu)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.back_frame = QtWidgets.QFrame(Lateral_menu)
        self.back_frame.setStyleSheet("")
        self.back_frame.setObjectName("back_frame")
        self.layerBack_frame = QtWidgets.QVBoxLayout(self.back_frame)
        self.layerBack_frame.setContentsMargins(0, 0, 0, 0)
        self.layerBack_frame.setSpacing(0)
        self.layerBack_frame.setObjectName("layerBack_frame")
        self.verticalLayout_2.addWidget(self.back_frame)

        self.retranslateUi(Lateral_menu)
        QtCore.QMetaObject.connectSlotsByName(Lateral_menu)

    def retranslateUi(self, Lateral_menu):
        _translate = QtCore.QCoreApplication.translate
        Lateral_menu.setWindowTitle(_translate("Lateral_menu", "Form"))

from resource import resource_rc
