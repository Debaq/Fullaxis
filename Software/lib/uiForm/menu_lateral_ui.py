# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'development/Form/menu_lateral.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(100, 525)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QtCore.QSize(100, 0))
        Form.setMaximumSize(QtCore.QSize(100, 16777215))
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.back_frame = QtWidgets.QFrame(Form)
        self.back_frame.setObjectName("back_frame")
        self.layerBack_frame = QtWidgets.QVBoxLayout(self.back_frame)
        self.layerBack_frame.setContentsMargins(0, 0, 0, 0)
        self.layerBack_frame.setSpacing(0)
        self.layerBack_frame.setObjectName("layerBack_frame")
        self.verticalLayout_2.addWidget(self.back_frame)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))

from resource import resource_rc
