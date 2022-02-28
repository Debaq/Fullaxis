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
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QGroupBox,
    QHBoxLayout, QLabel, QPushButton, QSizePolicy,
    QSpacerItem, QSpinBox, QTextEdit, QVBoxLayout,
    QWidget)

class Ui_Test_basic(object):
    def setupUi(self, Test_basic):
        if not Test_basic.objectName():
            Test_basic.setObjectName(u"Test_basic")
        Test_basic.resize(684, 530)
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
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, 0, -1, -1)
        self.lbl_test_name = QLabel(self.horizontalFrame)
        self.lbl_test_name.setObjectName(u"lbl_test_name")
        sizePolicy = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_test_name.sizePolicy().hasHeightForWidth())
        self.lbl_test_name.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.lbl_test_name)

        self.label = QLabel(self.horizontalFrame)
        self.label.setObjectName(u"label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy1)

        self.horizontalLayout.addWidget(self.label)

        self.lbl_test_date = QLabel(self.horizontalFrame)
        self.lbl_test_date.setObjectName(u"lbl_test_date")

        self.horizontalLayout.addWidget(self.lbl_test_date)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(-1, -1, -1, 0)
        self.lbl_test_comments = QLabel(self.horizontalFrame)
        self.lbl_test_comments.setObjectName(u"lbl_test_comments")

        self.horizontalLayout_3.addWidget(self.lbl_test_comments)

        self.txt_edit_test = QTextEdit(self.horizontalFrame)
        self.txt_edit_test.setObjectName(u"txt_edit_test")
        self.txt_edit_test.setMaximumSize(QSize(16777215, 50))
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
        self.frame.setMaximumSize(QSize(16777215, 25))
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.groupBox_2 = QGroupBox(self.frame)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setMinimumSize(QSize(50, 0))
        self.horizontalLayout_4 = QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.groupBox_2)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_4.addWidget(self.label_2)

        self.time_max = QSpinBox(self.groupBox_2)
        self.time_max.setObjectName(u"time_max")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.time_max.sizePolicy().hasHeightForWidth())
        self.time_max.setSizePolicy(sizePolicy2)
        self.time_max.setMaximumSize(QSize(39, 16777215))
        self.time_max.setMinimum(1)
        self.time_max.setValue(10)

        self.horizontalLayout_4.addWidget(self.time_max)

        self.label_3 = QLabel(self.groupBox_2)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_4.addWidget(self.label_3)


        self.horizontalLayout_2.addWidget(self.groupBox_2)

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
        self.lbl_test_name.setText(QCoreApplication.translate("Test_basic", u"Test_name", None))
        self.label.setText(QCoreApplication.translate("Test_basic", u"Date:", None))
        self.lbl_test_date.setText(QCoreApplication.translate("Test_basic", u"nn", None))
        self.lbl_test_comments.setText(QCoreApplication.translate("Test_basic", u"comments:", None))
        self.txt_edit_test.setDocumentTitle("")
        self.label_2.setText(QCoreApplication.translate("Test_basic", u"max time:", None))
        self.label_3.setText(QCoreApplication.translate("Test_basic", u"s.", None))
        self.btn_capture.setText(QCoreApplication.translate("Test_basic", u"Capture", None))
        self.check_delay.setText(QCoreApplication.translate("Test_basic", u"w/delay", None))
        self.btn_reset.setText(QCoreApplication.translate("Test_basic", u"Reset", None))
        self.btn_save.setText(QCoreApplication.translate("Test_basic", u"Save", None))
        self.btn_report.setText(QCoreApplication.translate("Test_basic", u"Report", None))
    # retranslateUi

