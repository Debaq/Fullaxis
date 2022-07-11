# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tool_bar_test.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_tool_bar(object):
    def setupUi(self, tool_bar):
        if not tool_bar.objectName():
            tool_bar.setObjectName(u"tool_bar")
        tool_bar.resize(567, 81)
        tool_bar.setStyleSheet(u"QPushButton{\n"
"color: rgb(114, 126, 150);\n"
"}\n"
"QPushButton:hover{\n"
"color: rgb(114, 126, 150);\n"
"background-color: rgb(226, 229, 233);\n"
"}")
        self.horizontalLayout_2 = QHBoxLayout(tool_bar)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, -1, -1, -1)
        self.btn_start = QPushButton(tool_bar)
        self.btn_start.setObjectName(u"btn_start")
        self.btn_start.setMinimumSize(QSize(0, 45))
        self.btn_start.setCheckable(False)
        self.btn_start.setFlat(True)

        self.horizontalLayout_3.addWidget(self.btn_start)


        self.horizontalLayout.addLayout(self.horizontalLayout_3)

        self.btn_save = QPushButton(tool_bar)
        self.btn_save.setObjectName(u"btn_save")
        self.btn_save.setMinimumSize(QSize(0, 45))
        self.btn_save.setFlat(True)

        self.horizontalLayout.addWidget(self.btn_save)

        self.btn_config = QPushButton(tool_bar)
        self.btn_config.setObjectName(u"btn_config")
        self.btn_config.setMinimumSize(QSize(0, 45))
        self.btn_config.setFlat(True)

        self.horizontalLayout.addWidget(self.btn_config)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.btn_exit = QPushButton(tool_bar)
        self.btn_exit.setObjectName(u"btn_exit")
        self.btn_exit.setMinimumSize(QSize(0, 45))
        self.btn_exit.setFlat(True)

        self.horizontalLayout.addWidget(self.btn_exit)


        self.horizontalLayout_2.addLayout(self.horizontalLayout)

        self.horizontalSpacer = QSpacerItem(174, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.layout_state_hardware = QVBoxLayout()
        self.layout_state_hardware.setObjectName(u"layout_state_hardware")

        self.horizontalLayout_2.addLayout(self.layout_state_hardware)


        self.retranslateUi(tool_bar)

        QMetaObject.connectSlotsByName(tool_bar)
    # setupUi

    def retranslateUi(self, tool_bar):
        tool_bar.setWindowTitle(QCoreApplication.translate("tool_bar", u"Form", None))
        self.btn_start.setText(QCoreApplication.translate("tool_bar", u"Iniciar", None))
        self.btn_save.setText(QCoreApplication.translate("tool_bar", u"Guardar", None))
        self.btn_config.setText(QCoreApplication.translate("tool_bar", u"Conf", None))
        self.btn_exit.setText(QCoreApplication.translate("tool_bar", u"Salir", None))
    # retranslateUi

