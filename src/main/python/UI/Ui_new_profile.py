# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'new_profile.ui'
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
from PySide6.QtWidgets import (QApplication, QDateEdit, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QLineEdit, QPlainTextEdit,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_new_profile(object):
    def setupUi(self, new_profile):
        if not new_profile.objectName():
            new_profile.setObjectName(u"new_profile")
        new_profile.resize(947, 599)
        new_profile.setStyleSheet(u"background-color: rgb(245, 245, 245);\n"
"QLineEdit{background-color: rgb(255, 255, 255);}\n"
"QPlainTextEdit{background-color: rgb(255, 255, 255);}\n"
"\n"
"")
        self.verticalLayout_2 = QVBoxLayout(new_profile)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(new_profile)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(0, 30))
        self.frame.setMaximumSize(QSize(16777215, 30))
        self.frame.setStyleSheet(u"background-color: qlineargradient(spread:reflect, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 rgba(229, 232, 236, 255), stop:1 rgba(245, 245, 245, 255));\n"
"\n"
"")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)

        self.verticalLayout_2.addWidget(self.frame)

        self.frame_profile_basic = QFrame(new_profile)
        self.frame_profile_basic.setObjectName(u"frame_profile_basic")
        self.gridLayout = QGridLayout(self.frame_profile_basic)
        self.gridLayout.setSpacing(20)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(100, -1, 100, -1)
        self.label_2 = QLabel(self.frame_profile_basic)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)

        self.label_4 = QLabel(self.frame_profile_basic)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 0, 2, 1, 1)

        self.line_lastname = QLineEdit(self.frame_profile_basic)
        self.line_lastname.setObjectName(u"line_lastname")

        self.gridLayout.addWidget(self.line_lastname, 2, 1, 1, 1)

        self.line_name = QLineEdit(self.frame_profile_basic)
        self.line_name.setObjectName(u"line_name")

        self.gridLayout.addWidget(self.line_name, 0, 1, 1, 1)

        self.label_3 = QLabel(self.frame_profile_basic)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 4, 0, 1, 1)

        self.label_9 = QLabel(self.frame_profile_basic)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_9, 4, 2, 1, 1)

        self.input_number = QLabel(self.frame_profile_basic)
        self.input_number.setObjectName(u"input_number")

        self.gridLayout.addWidget(self.input_number, 4, 3, 1, 1)

        self.line_id = QLineEdit(self.frame_profile_basic)
        self.line_id.setObjectName(u"line_id")

        self.gridLayout.addWidget(self.line_id, 4, 1, 1, 1)

        self.line_sex = QLineEdit(self.frame_profile_basic)
        self.line_sex.setObjectName(u"line_sex")

        self.gridLayout.addWidget(self.line_sex, 0, 3, 1, 1)

        self.label = QLabel(self.frame_profile_basic)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.label_5 = QLabel(self.frame_profile_basic)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 2, 2, 1, 1)

        self.input_date_birth = QDateEdit(self.frame_profile_basic)
        self.input_date_birth.setObjectName(u"input_date_birth")
        self.input_date_birth.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.input_date_birth.setDateTime(QDateTime(QDate(2000, 3, 1), QTime(0, 0, 0)))
        self.input_date_birth.setCalendarPopup(True)

        self.gridLayout.addWidget(self.input_date_birth, 2, 3, 1, 1)


        self.verticalLayout_2.addWidget(self.frame_profile_basic)

        self.frame_profile_exams = QFrame(new_profile)
        self.frame_profile_exams.setObjectName(u"frame_profile_exams")
        self.verticalLayout = QVBoxLayout(self.frame_profile_exams)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(100, 20, 100, 20)
        self.label_6 = QLabel(self.frame_profile_exams)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout.addWidget(self.label_6)

        self.text_history = QPlainTextEdit(self.frame_profile_exams)
        self.text_history.setObjectName(u"text_history")

        self.verticalLayout.addWidget(self.text_history)

        self.label_7 = QLabel(self.frame_profile_exams)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout.addWidget(self.label_7)

        self.text_othe_exam = QPlainTextEdit(self.frame_profile_exams)
        self.text_othe_exam.setObjectName(u"text_othe_exam")

        self.verticalLayout.addWidget(self.text_othe_exam)

        self.label_8 = QLabel(self.frame_profile_exams)
        self.label_8.setObjectName(u"label_8")

        self.verticalLayout.addWidget(self.label_8)

        self.text_result = QPlainTextEdit(self.frame_profile_exams)
        self.text_result.setObjectName(u"text_result")

        self.verticalLayout.addWidget(self.text_result)


        self.verticalLayout_2.addWidget(self.frame_profile_exams)

        self.frame_buttons = QFrame(new_profile)
        self.frame_buttons.setObjectName(u"frame_buttons")
        self.horizontalLayout = QHBoxLayout(self.frame_buttons)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(100, 1, 100, 10)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.btn_cancel_new_profile = QPushButton(self.frame_buttons)
        self.btn_cancel_new_profile.setObjectName(u"btn_cancel_new_profile")

        self.horizontalLayout.addWidget(self.btn_cancel_new_profile)

        self.btn_save_new_profile = QPushButton(self.frame_buttons)
        self.btn_save_new_profile.setObjectName(u"btn_save_new_profile")

        self.horizontalLayout.addWidget(self.btn_save_new_profile)


        self.verticalLayout_2.addWidget(self.frame_buttons)

        QWidget.setTabOrder(self.line_name, self.line_lastname)
        QWidget.setTabOrder(self.line_lastname, self.line_id)
        QWidget.setTabOrder(self.line_id, self.line_sex)
        QWidget.setTabOrder(self.line_sex, self.input_date_birth)
        QWidget.setTabOrder(self.input_date_birth, self.text_history)
        QWidget.setTabOrder(self.text_history, self.text_othe_exam)
        QWidget.setTabOrder(self.text_othe_exam, self.text_result)
        QWidget.setTabOrder(self.text_result, self.btn_cancel_new_profile)
        QWidget.setTabOrder(self.btn_cancel_new_profile, self.btn_save_new_profile)

        self.retranslateUi(new_profile)

        QMetaObject.connectSlotsByName(new_profile)
    # setupUi

    def retranslateUi(self, new_profile):
        new_profile.setWindowTitle(QCoreApplication.translate("new_profile", u"Form", None))
        self.label_2.setText(QCoreApplication.translate("new_profile", u"Apellidos:", None))
        self.label_4.setText(QCoreApplication.translate("new_profile", u"Sexo:", None))
        self.label_3.setText(QCoreApplication.translate("new_profile", u"ID:", None))
        self.label_9.setText(QCoreApplication.translate("new_profile", u"id_unique", None))
        self.input_number.setText("")
        self.label.setText(QCoreApplication.translate("new_profile", u"Nombres:", None))
        self.label_5.setText(QCoreApplication.translate("new_profile", u"Fecha de nacimiento:", None))
        self.input_date_birth.setDisplayFormat(QCoreApplication.translate("new_profile", u"dd-MM-yyyy", None))
        self.label_6.setText(QCoreApplication.translate("new_profile", u"Anamesis", None))
        self.label_7.setText(QCoreApplication.translate("new_profile", u"Examenes complementarios", None))
        self.label_8.setText(QCoreApplication.translate("new_profile", u"Resultados", None))
        self.btn_cancel_new_profile.setText(QCoreApplication.translate("new_profile", u"Cancelar", None))
        self.btn_save_new_profile.setText(QCoreApplication.translate("new_profile", u"Crear", None))
    # retranslateUi

