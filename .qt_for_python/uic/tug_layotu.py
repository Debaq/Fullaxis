# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tug_layotu.ui'
##
## Created by: Qt User Interface Compiler version 6.2.3
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
from PySide6.QtWidgets import (QApplication, QFormLayout, QFrame, QHBoxLayout,
    QLabel, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(868, 565)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalFrame = QFrame(Form)
        self.horizontalFrame.setObjectName(u"horizontalFrame")
        self.horizontalFrame.setMaximumSize(QSize(16777215, 150))
        self.horizontalLayout = QHBoxLayout(self.horizontalFrame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalFrame = QFrame(self.horizontalFrame)
        self.verticalFrame.setObjectName(u"verticalFrame")
        self.verticalFrame.setMaximumSize(QSize(150, 16777215))
        self.verticalLayout_2 = QVBoxLayout(self.verticalFrame)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.lbl_image = QLabel(self.verticalFrame)
        self.lbl_image.setObjectName(u"lbl_image")
        self.lbl_image.setMinimumSize(QSize(0, 115))
        self.lbl_image.setMaximumSize(QSize(16777215, 115))

        self.verticalLayout_2.addWidget(self.lbl_image)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.pushButton_2 = QPushButton(self.verticalFrame)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(20, 0))
        self.pushButton_2.setMaximumSize(QSize(20, 16777215))

        self.horizontalLayout_3.addWidget(self.pushButton_2)

        self.label = QLabel(self.verticalFrame)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label)

        self.pushButton = QPushButton(self.verticalFrame)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(20, 0))
        self.pushButton.setMaximumSize(QSize(20, 16777215))

        self.horizontalLayout_3.addWidget(self.pushButton)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)


        self.horizontalLayout.addWidget(self.verticalFrame)

        self.layout_graph = QVBoxLayout()
        self.layout_graph.setObjectName(u"layout_graph")

        self.horizontalLayout.addLayout(self.layout_graph)


        self.verticalLayout.addWidget(self.horizontalFrame)

        self.layout_result = QHBoxLayout()
        self.layout_result.setObjectName(u"layout_result")
        self.layout_result.setContentsMargins(-1, -1, 0, -1)
        self.verticalFrame_3 = QFrame(Form)
        self.verticalFrame_3.setObjectName(u"verticalFrame_3")
        self.verticalFrame_3.setMinimumSize(QSize(100, 0))
        self.verticalFrame_3.setMaximumSize(QSize(100, 16777215))
        self.verticalFrame_3.setLineWidth(0)
        self.verticalLayout_4 = QVBoxLayout(self.verticalFrame_3)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.lbl_image_pos = QLabel(self.verticalFrame_3)
        self.lbl_image_pos.setObjectName(u"lbl_image_pos")
        self.lbl_image_pos.setMaximumSize(QSize(100, 16777215))

        self.verticalLayout_4.addWidget(self.lbl_image_pos)

        self.lbl_config = QLabel(self.verticalFrame_3)
        self.lbl_config.setObjectName(u"lbl_config")
        self.lbl_config.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.verticalLayout_4.addWidget(self.lbl_config)


        self.layout_result.addWidget(self.verticalFrame_3)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")

        self.layout_result.addLayout(self.formLayout)

        self.verticalFrame1 = QFrame(Form)
        self.verticalFrame1.setObjectName(u"verticalFrame1")
        self.verticalFrame1.setMaximumSize(QSize(200, 16777215))
        self.verticalLayout_3 = QVBoxLayout(self.verticalFrame1)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")

        self.layout_result.addWidget(self.verticalFrame1)


        self.verticalLayout.addLayout(self.layout_result)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.lbl_image.setText(QCoreApplication.translate("Form", u"image", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"<", None))
        self.label.setText(QCoreApplication.translate("Form", u"Roll", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u">", None))
        self.lbl_image_pos.setText(QCoreApplication.translate("Form", u"image", None))
        self.lbl_config.setText(QCoreApplication.translate("Form", u"info", None))
    # retranslateUi

