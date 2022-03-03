# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'list_user.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QHeaderView, QPushButton,
    QSizePolicy, QSpacerItem, QTextEdit, QTreeWidget,
    QTreeWidgetItem, QVBoxLayout, QWidget)

class Ui_List_user(object):
    def setupUi(self, List_user):
        if not List_user.objectName():
            List_user.setObjectName(u"List_user")
        List_user.resize(400, 300)
        self.verticalLayout = QVBoxLayout(List_user)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.textEdit = QTextEdit(List_user)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setMaximumSize(QSize(16777215, 30))
        self.textEdit.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.textEdit.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.verticalLayout.addWidget(self.textEdit)

        self.list_user = QTreeWidget(List_user)
        self.list_user.setObjectName(u"list_user")

        self.verticalLayout.addWidget(self.list_user)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, 6, -1, -1)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.btn_delete_register = QPushButton(List_user)
        self.btn_delete_register.setObjectName(u"btn_delete_register")

        self.horizontalLayout.addWidget(self.btn_delete_register)


        self.verticalLayout.addLayout(self.horizontalLayout)

        QWidget.setTabOrder(self.textEdit, self.list_user)

        self.retranslateUi(List_user)

        QMetaObject.connectSlotsByName(List_user)
    # setupUi

    def retranslateUi(self, List_user):
        List_user.setWindowTitle(QCoreApplication.translate("List_user", u"Form", None))
        self.textEdit.setPlaceholderText(QCoreApplication.translate("List_user", u"Search...", None))
        ___qtreewidgetitem = self.list_user.headerItem()
        ___qtreewidgetitem.setText(4, QCoreApplication.translate("List_user", u"Last Sesion", None));
        ___qtreewidgetitem.setText(3, QCoreApplication.translate("List_user", u"Laste  name", None));
        ___qtreewidgetitem.setText(2, QCoreApplication.translate("List_user", u"First name", None));
        ___qtreewidgetitem.setText(1, QCoreApplication.translate("List_user", u"Id", None));
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("List_user", u"Number", None));
        self.btn_delete_register.setText(QCoreApplication.translate("List_user", u"Delete...", None))
    # retranslateUi

