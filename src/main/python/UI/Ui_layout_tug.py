# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'layout_tug.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_layout_tug(object):
    def setupUi(self, layout_tug):
        if not layout_tug.objectName():
            layout_tug.setObjectName(u"layout_tug")
        layout_tug.resize(868, 565)
        self.verticalLayout = QVBoxLayout(layout_tug)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalFrame = QFrame(layout_tug)
        self.horizontalFrame.setObjectName(u"horizontalFrame")
        self.horizontalFrame.setMaximumSize(QSize(16777215, 200))
        self.horizontalLayout = QHBoxLayout(self.horizontalFrame)
        self.horizontalLayout.setSpacing(0)
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
        self.btn_prev_state = QPushButton(self.verticalFrame)
        self.btn_prev_state.setObjectName(u"btn_prev_state")
        self.btn_prev_state.setMinimumSize(QSize(20, 0))
        self.btn_prev_state.setMaximumSize(QSize(20, 16777215))
        self.btn_prev_state.setFlat(True)

        self.horizontalLayout_3.addWidget(self.btn_prev_state)

        self.lbl_state_view = QLabel(self.verticalFrame)
        self.lbl_state_view.setObjectName(u"lbl_state_view")
        self.lbl_state_view.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.lbl_state_view)

        self.btn_next_state = QPushButton(self.verticalFrame)
        self.btn_next_state.setObjectName(u"btn_next_state")
        self.btn_next_state.setMinimumSize(QSize(20, 0))
        self.btn_next_state.setMaximumSize(QSize(20, 16777215))
        self.btn_next_state.setFlat(True)

        self.horizontalLayout_3.addWidget(self.btn_next_state)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)


        self.horizontalLayout.addWidget(self.verticalFrame)

        self.layout_graph = QVBoxLayout()
        self.layout_graph.setObjectName(u"layout_graph")

        self.horizontalLayout.addLayout(self.layout_graph)


        self.verticalLayout.addWidget(self.horizontalFrame)

        self.layout_result = QHBoxLayout()
        self.layout_result.setObjectName(u"layout_result")
        self.layout_result.setContentsMargins(-1, -1, 0, -1)
        self.verticalFrame_3 = QFrame(layout_tug)
        self.verticalFrame_3.setObjectName(u"verticalFrame_3")
        self.verticalFrame_3.setMinimumSize(QSize(200, 0))
        self.verticalFrame_3.setMaximumSize(QSize(200, 16777215))
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

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(-1, -1, 0, -1)

        self.layout_result.addLayout(self.gridLayout)

        self.verticalFrame1 = QFrame(layout_tug)
        self.verticalFrame1.setObjectName(u"verticalFrame1")
        self.verticalFrame1.setMinimumSize(QSize(200, 0))
        self.verticalFrame1.setMaximumSize(QSize(200, 16777215))
        self.verticalLayout_3 = QVBoxLayout(self.verticalFrame1)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")

        self.layout_result.addWidget(self.verticalFrame1)


        self.verticalLayout.addLayout(self.layout_result)


        self.retranslateUi(layout_tug)

        QMetaObject.connectSlotsByName(layout_tug)
    # setupUi

    def retranslateUi(self, layout_tug):
        layout_tug.setWindowTitle(QCoreApplication.translate("layout_tug", u"Form", None))
        self.lbl_image.setText(QCoreApplication.translate("layout_tug", u"image", None))
        self.btn_prev_state.setText(QCoreApplication.translate("layout_tug", u"<", None))
        self.lbl_state_view.setText("")
        self.btn_next_state.setText(QCoreApplication.translate("layout_tug", u">", None))
        self.lbl_image_pos.setText(QCoreApplication.translate("layout_tug", u"image", None))
        self.lbl_config.setText(QCoreApplication.translate("layout_tug", u"<html><head/><body><p><span style=\" font-weight:600; text-decoration: underline;\">Parametros:</span></p><p>Prueba: <span style=\" font-weight:600;\">TUG</span></p><p>Tiempo de eval.: <span style=\" font-weight:600;\">10seg</span></p><p>Posici\u00f3n: <span style=\" font-weight:600;\">Estandar</span></p><p><br/></p></body></html>", None))
    # retranslateUi

