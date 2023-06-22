# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'basic_test.ui'
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
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QCheckBox, QComboBox,
    QFrame, QHBoxLayout, QLabel, QPushButton,
    QSizePolicy, QSpacerItem, QSpinBox, QTextEdit,
    QVBoxLayout, QWidget)

class Ui_Test_basic(object):
    def setupUi(self, Test_basic):
        if not Test_basic.objectName():
            Test_basic.setObjectName(u"Test_basic")
        Test_basic.resize(798, 695)
        self.verticalLayout = QVBoxLayout(Test_basic)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalFrame = QFrame(Test_basic)
        self.horizontalFrame.setObjectName(u"horizontalFrame")
        self.horizontalFrame.setMaximumSize(QSize(16777215, 90))
        self.verticalLayout_2 = QVBoxLayout(self.horizontalFrame)
        self.verticalLayout_2.setSpacing(3)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(-1, -1, -1, 0)
        self.lbl_test_comments = QLabel(self.horizontalFrame)
        self.lbl_test_comments.setObjectName(u"lbl_test_comments")

        self.horizontalLayout_3.addWidget(self.lbl_test_comments)

        self.txt_edit_test = QTextEdit(self.horizontalFrame)
        self.txt_edit_test.setObjectName(u"txt_edit_test")
        self.txt_edit_test.setMinimumSize(QSize(0, 80))
        self.txt_edit_test.setReadOnly(False)

        self.horizontalLayout_3.addWidget(self.txt_edit_test)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)


        self.verticalLayout.addWidget(self.horizontalFrame)

        self.widget_test = QWidget(Test_basic)
        self.widget_test.setObjectName(u"widget_test")
        self.layout_test = QHBoxLayout(self.widget_test)
        self.layout_test.setObjectName(u"layout_test")
        self.layout_test.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout.addWidget(self.widget_test)

        self.frame = QFrame(Test_basic)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(0, 34))
        self.frame.setMaximumSize(QSize(16777215, 34))
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalFrame_1 = QFrame(self.frame)
        self.horizontalFrame_1.setObjectName(u"horizontalFrame_1")
        self.horizontalFrame_1.setMinimumSize(QSize(50, 0))
        self.horizontalLayout_5 = QHBoxLayout(self.horizontalFrame_1)
        self.horizontalLayout_5.setSpacing(2)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.btn_connect = QPushButton(self.horizontalFrame_1)
        self.btn_connect.setObjectName(u"btn_connect")

        self.horizontalLayout_5.addWidget(self.btn_connect)

        self.combo_serial = QComboBox(self.horizontalFrame_1)
        self.combo_serial.setObjectName(u"combo_serial")
        self.combo_serial.setInsertPolicy(QComboBox.InsertAtTop)

        self.horizontalLayout_5.addWidget(self.combo_serial)

        self.btn_view_raw = QPushButton(self.horizontalFrame_1)
        self.btn_view_raw.setObjectName(u"btn_view_raw")
        self.btn_view_raw.setEnabled(False)
        self.btn_view_raw.setFlat(False)

        self.horizontalLayout_5.addWidget(self.btn_view_raw)


        self.horizontalLayout_2.addWidget(self.horizontalFrame_1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.move_cond = QHBoxLayout()
        self.move_cond.setObjectName(u"move_cond")

        self.horizontalLayout_2.addLayout(self.move_cond)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        font = QFont()
        font.setPointSize(8)
        self.label_2.setFont(font)

        self.horizontalLayout_2.addWidget(self.label_2)

        self.time_max = QSpinBox(self.frame)
        self.time_max.setObjectName(u"time_max")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.time_max.sizePolicy().hasHeightForWidth())
        self.time_max.setSizePolicy(sizePolicy)
        self.time_max.setMaximumSize(QSize(30, 16777215))
        self.time_max.setFont(font)
        self.time_max.setLayoutDirection(Qt.RightToLeft)
        self.time_max.setAutoFillBackground(False)
        self.time_max.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.time_max.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.time_max.setMinimum(1)
        self.time_max.setMaximum(3600)
        self.time_max.setValue(15)

        self.horizontalLayout_2.addWidget(self.time_max)

        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)

        self.horizontalLayout_2.addWidget(self.label_3)

        self.btn_capture = QPushButton(self.frame)
        self.btn_capture.setObjectName(u"btn_capture")
        self.btn_capture.setEnabled(False)

        self.horizontalLayout_2.addWidget(self.btn_capture)

        self.check_delay = QCheckBox(self.frame)
        self.check_delay.setObjectName(u"check_delay")
        self.check_delay.setChecked(True)

        self.horizontalLayout_2.addWidget(self.check_delay)

        self.btn_reset = QPushButton(self.frame)
        self.btn_reset.setObjectName(u"btn_reset")
        self.btn_reset.setEnabled(False)

        self.horizontalLayout_2.addWidget(self.btn_reset)

        self.btn_save = QPushButton(self.frame)
        self.btn_save.setObjectName(u"btn_save")
        self.btn_save.setEnabled(False)

        self.horizontalLayout_2.addWidget(self.btn_save)

        self.btn_report = QPushButton(self.frame)
        self.btn_report.setObjectName(u"btn_report")
        self.btn_report.setEnabled(False)

        self.horizontalLayout_2.addWidget(self.btn_report)


        self.verticalLayout.addWidget(self.frame)


        self.retranslateUi(Test_basic)

        QMetaObject.connectSlotsByName(Test_basic)
    # setupUi

    def retranslateUi(self, Test_basic):
        Test_basic.setWindowTitle(QCoreApplication.translate("Test_basic", u"Form", None))
        self.lbl_test_comments.setText(QCoreApplication.translate("Test_basic", u"comments:", None))
        self.txt_edit_test.setDocumentTitle("")
        self.btn_connect.setText(QCoreApplication.translate("Test_basic", u"Connect ...", None))
        self.btn_view_raw.setText(QCoreApplication.translate("Test_basic", u"View Raw", None))
        self.label_2.setText(QCoreApplication.translate("Test_basic", u"max time:", None))
        self.label_3.setText(QCoreApplication.translate("Test_basic", u"s.", None))
        self.btn_capture.setText(QCoreApplication.translate("Test_basic", u"Capture", None))
        self.check_delay.setText(QCoreApplication.translate("Test_basic", u"w/delay", None))
        self.btn_reset.setText(QCoreApplication.translate("Test_basic", u"Reset", None))
        self.btn_save.setText(QCoreApplication.translate("Test_basic", u"Save", None))
        self.btn_report.setText(QCoreApplication.translate("Test_basic", u"Report", None))
    # retranslateUi

