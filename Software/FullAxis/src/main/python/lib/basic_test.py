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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QPushButton, QSizePolicy, QSpacerItem, QTextEdit,
    QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(769, 573)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalFrame = QFrame(Form)
        self.horizontalFrame.setObjectName(u"horizontalFrame")
        self.horizontalFrame.setMaximumSize(QSize(16777215, 100))
        self.verticalLayout_2 = QVBoxLayout(self.horizontalFrame)
        self.verticalLayout_2.setSpacing(3)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, 0, -1, -1)
        self.lbl_test_name = QLabel(self.horizontalFrame)
        self.lbl_test_name.setObjectName(u"lbl_test_name")

        self.horizontalLayout.addWidget(self.lbl_test_name)

        self.lbl_test_date = QLabel(self.horizontalFrame)
        self.lbl_test_date.setObjectName(u"lbl_test_date")

        self.horizontalLayout.addWidget(self.lbl_test_date)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.lbl_test_comments = QLabel(self.horizontalFrame)
        self.lbl_test_comments.setObjectName(u"lbl_test_comments")

        self.verticalLayout_2.addWidget(self.lbl_test_comments)

        self.txt_edit_test = QTextEdit(self.horizontalFrame)
        self.txt_edit_test.setObjectName(u"txt_edit_test")
        self.txt_edit_test.setMaximumSize(QSize(16777215, 50))
        self.txt_edit_test.setReadOnly(True)

        self.verticalLayout_2.addWidget(self.txt_edit_test)


        self.verticalLayout.addWidget(self.horizontalFrame)

        self.widget_test = QWidget(Form)
        self.widget_test.setObjectName(u"widget_test")
        self.layout_test = QHBoxLayout(self.widget_test)
        self.layout_test.setObjectName(u"layout_test")
        self.layout_test.setContentsMargins(-1, 10, -1, -1)
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.layout_test.addItem(self.verticalSpacer_2)


        self.verticalLayout.addWidget(self.widget_test)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, -1, -1, 0)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.btn_capture = QPushButton(Form)
        self.btn_capture.setObjectName(u"btn_capture")

        self.horizontalLayout_2.addWidget(self.btn_capture)

        self.btn_save = QPushButton(Form)
        self.btn_save.setObjectName(u"btn_save")

        self.horizontalLayout_2.addWidget(self.btn_save)

        self.btn_report = QPushButton(Form)
        self.btn_report.setObjectName(u"btn_report")

        self.horizontalLayout_2.addWidget(self.btn_report)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.lbl_test_name.setText(QCoreApplication.translate("Form", u"Test_name", None))
        self.lbl_test_date.setText(QCoreApplication.translate("Form", u"Date:", None))
        self.lbl_test_comments.setText(QCoreApplication.translate("Form", u"comments:", None))
        self.txt_edit_test.setDocumentTitle("")
        self.btn_capture.setText(QCoreApplication.translate("Form", u"Capture", None))
        self.btn_save.setText(QCoreApplication.translate("Form", u"Save", None))
        self.btn_report.setText(QCoreApplication.translate("Form", u"Report", None))
    # retranslateUi

