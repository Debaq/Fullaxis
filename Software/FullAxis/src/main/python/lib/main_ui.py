# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QMainWindow,
    QPushButton, QSizePolicy, QSpacerItem, QStatusBar,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(915, 704)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(6, 3, 6, 3)
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setMaximumSize(QSize(16777215, 35))
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setSpacing(3)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.btn_new_profile = QPushButton(self.widget)
        self.btn_new_profile.setObjectName(u"btn_new_profile")

        self.horizontalLayout.addWidget(self.btn_new_profile)

        self.btn_open_profile = QPushButton(self.widget)
        self.btn_open_profile.setObjectName(u"btn_open_profile")

        self.horizontalLayout.addWidget(self.btn_open_profile)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.btn_connect = QPushButton(self.widget)
        self.btn_connect.setObjectName(u"btn_connect")

        self.horizontalLayout.addWidget(self.btn_connect)

        self.combo_serial = QComboBox(self.widget)
        self.combo_serial.setObjectName(u"combo_serial")
        self.combo_serial.setInsertPolicy(QComboBox.InsertAtTop)

        self.horizontalLayout.addWidget(self.combo_serial)

        self.btn_view_raw = QPushButton(self.widget)
        self.btn_view_raw.setObjectName(u"btn_view_raw")
        self.btn_view_raw.setEnabled(False)
        self.btn_view_raw.setFlat(False)

        self.horizontalLayout.addWidget(self.btn_view_raw)


        self.verticalLayout.addWidget(self.widget)

        self.widget_central = QWidget(self.centralwidget)
        self.widget_central.setObjectName(u"widget_central")
        self.layout_central = QVBoxLayout(self.widget_central)
        self.layout_central.setSpacing(0)
        self.layout_central.setObjectName(u"layout_central")
        self.layout_central.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout.addWidget(self.widget_central)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        QWidget.setTabOrder(self.btn_new_profile, self.btn_open_profile)
        QWidget.setTabOrder(self.btn_open_profile, self.btn_view_raw)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btn_new_profile.setText(QCoreApplication.translate("MainWindow", u"New Profile", None))
        self.btn_open_profile.setText(QCoreApplication.translate("MainWindow", u"Open Profile", None))
        self.btn_connect.setText(QCoreApplication.translate("MainWindow", u"Connect ...", None))
        self.btn_view_raw.setText(QCoreApplication.translate("MainWindow", u"View Raw", None))
    # retranslateUi

