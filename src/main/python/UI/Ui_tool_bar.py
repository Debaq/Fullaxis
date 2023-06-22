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
from PySide6.QtWidgets import (QApplication, QFormLayout, QHBoxLayout, QLabel,
    QPushButton, QSizePolicy, QSpacerItem, QWidget)

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
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, -1, -1, -1)
        self.btn_start = QPushButton(tool_bar)
        self.btn_start.setObjectName(u"btn_start")
        self.btn_start.setEnabled(False)
        self.btn_start.setMinimumSize(QSize(0, 45))
        self.btn_start.setCheckable(False)
        self.btn_start.setFlat(True)

        self.horizontalLayout_3.addWidget(self.btn_start)


        self.horizontalLayout.addLayout(self.horizontalLayout_3)

        self.btn_new = QPushButton(tool_bar)
        self.btn_new.setObjectName(u"btn_new")
        self.btn_new.setMinimumSize(QSize(0, 45))
        self.btn_new.setFlat(True)

        self.horizontalLayout.addWidget(self.btn_new)

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


        self.horizontalLayout_2.addLayout(self.horizontalLayout)

        self.horizontalSpacer = QSpacerItem(174, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, -1, -1, -1)
        self.btn_connect = QPushButton(tool_bar)
        self.btn_connect.setObjectName(u"btn_connect")
        self.btn_connect.setMinimumSize(QSize(0, 45))
        self.btn_connect.setFlat(True)

        self.horizontalLayout_4.addWidget(self.btn_connect)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setHorizontalSpacing(1)
        self.formLayout.setVerticalSpacing(1)
        self.formLayout.setContentsMargins(0, -1, -1, -1)
        self.label = QLabel(tool_bar)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(8)
        self.label.setFont(font)

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label)

        self.label_2 = QLabel(tool_bar)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_2)

        self.label_3 = QLabel(tool_bar)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_3)

        self.lbl_roll = QLabel(tool_bar)
        self.lbl_roll.setObjectName(u"lbl_roll")
        self.lbl_roll.setFont(font)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.lbl_roll)

        self.lbl_pitch = QLabel(tool_bar)
        self.lbl_pitch.setObjectName(u"lbl_pitch")
        self.lbl_pitch.setFont(font)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.lbl_pitch)

        self.lbl_yaw = QLabel(tool_bar)
        self.lbl_yaw.setObjectName(u"lbl_yaw")
        self.lbl_yaw.setFont(font)

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.lbl_yaw)

        self.btn_battery = QPushButton(tool_bar)
        self.btn_battery.setObjectName(u"btn_battery")
        self.btn_battery.setMaximumSize(QSize(20, 16777215))
        self.btn_battery.setFlat(True)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.btn_battery)

        self.lbl_batt = QLabel(tool_bar)
        self.lbl_batt.setObjectName(u"lbl_batt")
        self.lbl_batt.setFont(font)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.lbl_batt)


        self.horizontalLayout_4.addLayout(self.formLayout)


        self.horizontalLayout_2.addLayout(self.horizontalLayout_4)


        self.retranslateUi(tool_bar)

        QMetaObject.connectSlotsByName(tool_bar)
    # setupUi

    def retranslateUi(self, tool_bar):
        tool_bar.setWindowTitle(QCoreApplication.translate("tool_bar", u"Form", None))
#if QT_CONFIG(tooltip)
        self.btn_start.setToolTip(QCoreApplication.translate("tool_bar", u"Iniciar", None))
#endif // QT_CONFIG(tooltip)
        self.btn_start.setText(QCoreApplication.translate("tool_bar", u"Iniciar", None))
        self.btn_new.setText(QCoreApplication.translate("tool_bar", u"Nueva", None))
#if QT_CONFIG(tooltip)
        self.btn_save.setToolTip(QCoreApplication.translate("tool_bar", u"Guardar", None))
#endif // QT_CONFIG(tooltip)
        self.btn_save.setText(QCoreApplication.translate("tool_bar", u"Guardar", None))
#if QT_CONFIG(tooltip)
        self.btn_config.setToolTip(QCoreApplication.translate("tool_bar", u"configurar", None))
#endif // QT_CONFIG(tooltip)
        self.btn_config.setText(QCoreApplication.translate("tool_bar", u"Conf", None))
        self.btn_connect.setText(QCoreApplication.translate("tool_bar", u"conectar", None))
        self.label.setText(QCoreApplication.translate("tool_bar", u"Roll", None))
        self.label_2.setText(QCoreApplication.translate("tool_bar", u"Pitch", None))
        self.label_3.setText(QCoreApplication.translate("tool_bar", u"Yaw", None))
        self.lbl_roll.setText(QCoreApplication.translate("tool_bar", u"00.00", None))
        self.lbl_pitch.setText(QCoreApplication.translate("tool_bar", u"00.00", None))
        self.lbl_yaw.setText(QCoreApplication.translate("tool_bar", u"00.00", None))
        self.btn_battery.setText(QCoreApplication.translate("tool_bar", u"b", None))
        self.lbl_batt.setText(QCoreApplication.translate("tool_bar", u"50%", None))
    # retranslateUi

