# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'windows_principal.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QHeaderView,
    QLabel, QListWidget, QListWidgetItem, QPushButton,
    QSizePolicy, QSpacerItem, QTreeWidget, QTreeWidgetItem,
    QVBoxLayout, QWidget)

class Ui_win_principal(object):
    def setupUi(self, win_principal):
        if not win_principal.objectName():
            win_principal.setObjectName(u"win_principal")
        win_principal.resize(1014, 433)
        win_principal.setStyleSheet(u"background-color: rgb(245, 245, 245);")
        self.verticalLayout_2 = QVBoxLayout(win_principal)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_gradient_0 = QFrame(win_principal)
        self.frame_gradient_0.setObjectName(u"frame_gradient_0")
        self.frame_gradient_0.setMinimumSize(QSize(0, 30))
        self.frame_gradient_0.setMaximumSize(QSize(16777215, 30))
        self.frame_gradient_0.setStyleSheet(u"background-color: qlineargradient(spread:reflect, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 rgba(229, 232, 236, 255), stop:1 rgba(245, 245, 245, 255));\n"
"\n"
"")
        self.frame_gradient_0.setFrameShape(QFrame.NoFrame)
        self.frame_gradient_0.setFrameShadow(QFrame.Plain)
        self.frame_gradient_0.setLineWidth(0)

        self.verticalLayout_2.addWidget(self.frame_gradient_0)

        self.frame_central = QFrame(win_principal)
        self.frame_central.setObjectName(u"frame_central")
        self.frame_central.setStyleSheet(u"QFrame#frame_central{\n"
"background-color: rgb(245, 245, 245);\n"
"}\n"
"                                    QTreeView::item {\n"
"                                        padding: 10 10px;\n"
"                                        icon-size:40px;\n"
"                                        color:#434d61;\n"
"                                        show-decoration-selected: 1;\n"
"                                        }\n"
"\n"
"                                    QTreeView::item:hover {\n"
"                                        background: #e9ebed;\n"
"                                    }\n"
"                                    QTreeView::item:selected {\n"
"                                        background: #e2e5e9;\n"
"                                        border-color : red;\n"
"                                    }\n"
"                                    QTreeView::branch {\n"
"                                        background: #f5f5f5;\n"
"                                    }")
        self.horizontalLayout_2 = QHBoxLayout(self.frame_central)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_izq = QFrame(self.frame_central)
        self.frame_izq.setObjectName(u"frame_izq")
        self.frame_izq.setMinimumSize(QSize(80, 0))
        self.frame_izq.setMaximumSize(QSize(80, 16777215))
        self.verticalLayout_3 = QVBoxLayout(self.frame_izq)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 10, 0, 0)
        self.frame_btn = QFrame(self.frame_izq)
        self.frame_btn.setObjectName(u"frame_btn")
        self.frame_btn.setStyleSheet(u"QPushButton{\n"
"color: rgb(114, 126, 150);\n"
"}\n"
"QPushButton:hover{\n"
"color: rgb(114, 126, 150);\n"
"background-color: rgb(226, 229, 233);\n"
"}")
        self.verticalLayout_5 = QVBoxLayout(self.frame_btn)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.btn_new_user = QPushButton(self.frame_btn)
        self.btn_new_user.setObjectName(u"btn_new_user")
        self.btn_new_user.setMinimumSize(QSize(0, 60))
        self.btn_new_user.setFlat(True)

        self.verticalLayout_5.addWidget(self.btn_new_user)

        self.btn_open_file = QPushButton(self.frame_btn)
        self.btn_open_file.setObjectName(u"btn_open_file")
        self.btn_open_file.setMinimumSize(QSize(0, 60))
        self.btn_open_file.setFlat(True)

        self.verticalLayout_5.addWidget(self.btn_open_file)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_2)


        self.verticalLayout_3.addWidget(self.frame_btn)


        self.horizontalLayout_2.addWidget(self.frame_izq)

        self.frame = QFrame(self.frame_central)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(15, 0))
        self.frame.setMaximumSize(QSize(15, 16777215))
        self.frame.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(229, 232, 236, 255), stop:1 rgba(245, 245, 245, 255));\n"
"\n"
"\n"
"")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_2.addWidget(self.frame)

        self.frame_last_view = QFrame(self.frame_central)
        self.frame_last_view.setObjectName(u"frame_last_view")
        self.frame_last_view.setMinimumSize(QSize(200, 0))
        self.frame_last_view.setMaximumSize(QSize(200, 16777215))
        self.frame_last_view.setLayoutDirection(Qt.LeftToRight)
        self.verticalLayout_4 = QVBoxLayout(self.frame_last_view)
        self.verticalLayout_4.setSpacing(5)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 10, 10, 0)
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(-1, 0, -1, -1)
        self.label = QLabel(self.frame_last_view)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(180, 30))
        self.label.setMaximumSize(QSize(80, 30))
        self.label.setStyleSheet(u" border: 1px none #3d404d;\n"
" border-radius: 5px;\n"
"border-bottom : none;\n"
"background-color: rgb(226, 229, 233);\n"
"color: rgb(65, 127, 249);")
        self.label.setLineWidth(0)
        self.label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label)


        self.verticalLayout_4.addLayout(self.horizontalLayout_3)

        self.line = QFrame(self.frame_last_view)
        self.line.setObjectName(u"line")
        self.line.setStyleSheet(u"color: rgb(231, 233, 239);")
        self.line.setFrameShadow(QFrame.Plain)
        self.line.setFrameShape(QFrame.HLine)

        self.verticalLayout_4.addWidget(self.line)

        self.list_recent = QListWidget(self.frame_last_view)
        self.list_recent.setObjectName(u"list_recent")
        self.list_recent.setFrameShape(QFrame.NoFrame)

        self.verticalLayout_4.addWidget(self.list_recent)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer)


        self.horizontalLayout_2.addWidget(self.frame_last_view)

        self.frame_2 = QFrame(self.frame_central)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(3, 0))
        self.frame_2.setMaximumSize(QSize(3, 16777215))
        self.frame_2.setStyleSheet(u"background-color: rgb(160, 160, 160);")
        self.frame_2.setFrameShape(QFrame.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_2.addWidget(self.frame_2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(-1, -1, -1, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, -1, -1, 0)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.btn_order = QPushButton(self.frame_central)
        self.btn_order.setObjectName(u"btn_order")
        self.btn_order.setFlat(True)

        self.horizontalLayout.addWidget(self.btn_order)

        self.btn_filter = QPushButton(self.frame_central)
        self.btn_filter.setObjectName(u"btn_filter")
        self.btn_filter.setFlat(True)

        self.horizontalLayout.addWidget(self.btn_filter)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.list_user = QTreeWidget(self.frame_central)
        self.list_user.setObjectName(u"list_user")
        self.list_user.setStyleSheet(u"background-color: rgb(245, 245, 245);")
        self.list_user.setInputMethodHints(Qt.ImhMultiLine)
        self.list_user.setFrameShape(QFrame.NoFrame)
        self.list_user.setIconSize(QSize(40, 40))
        self.list_user.header().setVisible(False)

        self.verticalLayout.addWidget(self.list_user)


        self.horizontalLayout_2.addLayout(self.verticalLayout)

        self.frame_3 = QFrame(self.frame_central)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(300, 0))
        self.frame_3.setMaximumSize(QSize(150, 16777215))
        self.frame_3.setStyleSheet(u"background-color: rgb(245, 245, 245);")
        self.frame_3.setFrameShape(QFrame.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_3)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.lbl_logo_selected = QLabel(self.frame_3)
        self.lbl_logo_selected.setObjectName(u"lbl_logo_selected")
        self.lbl_logo_selected.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.lbl_logo_selected)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSpacing(1)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(-1, 10, -1, -1)
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_2)

        self.lbl_name = QLabel(self.frame_3)
        self.lbl_name.setObjectName(u"lbl_name")
        font = QFont()
        font.setBold(True)
        self.lbl_name.setFont(font)
        self.lbl_name.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_4.addWidget(self.lbl_name)

        self.btn_edit_profile = QPushButton(self.frame_3)
        self.btn_edit_profile.setObjectName(u"btn_edit_profile")
        self.btn_edit_profile.setEnabled(False)
        self.btn_edit_profile.setFlat(True)

        self.horizontalLayout_4.addWidget(self.btn_edit_profile)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_3)


        self.verticalLayout_6.addLayout(self.horizontalLayout_4)

        self.lbl_info_profile = QLabel(self.frame_3)
        self.lbl_info_profile.setObjectName(u"lbl_info_profile")
        self.lbl_info_profile.setTextFormat(Qt.RichText)
        self.lbl_info_profile.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_6.addWidget(self.lbl_info_profile)

        self.listWidget = QListWidget(self.frame_3)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setFrameShape(QFrame.NoFrame)

        self.verticalLayout_6.addWidget(self.listWidget)


        self.verticalLayout_7.addLayout(self.verticalLayout_6)

        self.label_2 = QLabel(self.frame_3)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_7.addWidget(self.label_2)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(-1, 0, -1, -1)
        self.btn_tug = QPushButton(self.frame_3)
        self.btn_tug.setObjectName(u"btn_tug")
        self.btn_tug.setEnabled(True)
        self.btn_tug.setMinimumSize(QSize(50, 50))
        self.btn_tug.setMaximumSize(QSize(50, 50))
        self.btn_tug.setFlat(False)

        self.horizontalLayout_5.addWidget(self.btn_tug)

        self.btn_sot = QPushButton(self.frame_3)
        self.btn_sot.setObjectName(u"btn_sot")
        self.btn_sot.setEnabled(True)
        self.btn_sot.setMinimumSize(QSize(50, 50))
        self.btn_sot.setMaximumSize(QSize(50, 50))
        self.btn_sot.setFlat(False)

        self.horizontalLayout_5.addWidget(self.btn_sot)

        self.btn_vng = QPushButton(self.frame_3)
        self.btn_vng.setObjectName(u"btn_vng")
        self.btn_vng.setEnabled(True)
        self.btn_vng.setMinimumSize(QSize(50, 50))
        self.btn_vng.setMaximumSize(QSize(50, 50))
        self.btn_vng.setFlat(False)

        self.horizontalLayout_5.addWidget(self.btn_vng)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_4)


        self.verticalLayout_7.addLayout(self.horizontalLayout_5)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer_3)


        self.horizontalLayout_2.addWidget(self.frame_3)


        self.verticalLayout_2.addWidget(self.frame_central)


        self.retranslateUi(win_principal)

        QMetaObject.connectSlotsByName(win_principal)
    # setupUi

    def retranslateUi(self, win_principal):
        win_principal.setWindowTitle(QCoreApplication.translate("win_principal", u"Form", None))
        self.btn_new_user.setText(QCoreApplication.translate("win_principal", u"new_user", None))
        self.btn_open_file.setText(QCoreApplication.translate("win_principal", u"open_file", None))
        self.label.setText(QCoreApplication.translate("win_principal", u"Recientes", None))
        self.btn_order.setText(QCoreApplication.translate("win_principal", u"order", None))
        self.btn_filter.setText(QCoreApplication.translate("win_principal", u"Filter", None))
        ___qtreewidgetitem = self.list_user.headerItem()
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("win_principal", u"id", None));
        self.lbl_logo_selected.setText("")
        self.lbl_name.setText("")
        self.btn_edit_profile.setText("")
        self.lbl_info_profile.setText(QCoreApplication.translate("win_principal", u"<html><head/><body><p><br/></p></body></html>", None))
        self.label_2.setText("")
        self.btn_tug.setText("")
        self.btn_sot.setText("")
        self.btn_vng.setText("")
    # retranslateUi

