# -*- coding: utf-8 -*-

################################################################################
# Form generated from reading UI file 'mainbkhiGu.ui'
##
# Created by: Qt User Interface Compiler version 6.5.0
##
# WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
                           QFont, QFontDatabase, QGradient, QIcon,
                           QImage, QKeySequence, QLinearGradient, QPainter,
                           QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QMainWindow,
                               QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
                               QWidget)
from lib.CustomWidgets import DraggableWidget
from lib.Ui_constructors import set_button_icon


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 492)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background-color: rgb(61, 64, 77)\n"
                                         "")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(2, 0, 2, 2)
        self.frame_win_bar = DraggableWidget()
        self.frame_win_bar.setObjectName(u"frame_win_bar")
        self.frame_win_bar.setMinimumSize(QSize(0, 43))
        self.frame_win_bar.setMaximumSize(QSize(16777215, 40))
        
        self.horizontalLayout = QHBoxLayout(self.frame_win_bar)
        self.horizontalLayout.setSpacing(2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(2, 5, 0, 0)
        self.layotu_btn_tabs = QHBoxLayout()
        self.layotu_btn_tabs.setObjectName(u"layotu_btn_tabs")
        self.layotu_btn_tabs.setContentsMargins(0, -1, -1, -1)
        self.btn_menu = QPushButton(self.frame_win_bar)
        self.btn_menu.setObjectName(u"btn_menu")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.btn_menu.sizePolicy().hasHeightForWidth())
        self.btn_menu.setSizePolicy(sizePolicy)
        self.btn_menu.setMinimumSize(QSize(0, 25))
        
        self.btn_menu.setFlat(False)

        self.layotu_btn_tabs.addWidget(self.btn_menu)

        self.horizontalLayout.addLayout(self.layotu_btn_tabs)
        self.tabs_widget = QWidget(self.frame_win_bar)
        self.tabs_widget.setObjectName(u"tabs_widgets")

        self.tabs_layout = QHBoxLayout(self.tabs_widget)
        self.tabs_layout.setObjectName(u"tabs_layout")
        self.tabs_layout.setSpacing(2)
        self.tabs_layout.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout.addWidget(self.tabs_widget)

        self.btn_new = QPushButton(self.frame_win_bar)
        self.btn_new.setObjectName(u"btn_new")
        self.btn_new.setMinimumSize(QSize(0, 25))
        self.btn_new.setFlat(True)

        self.horizontalLayout.addWidget(self.btn_new)

        self.horizontalSpacer = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.btn_min = QPushButton(self.frame_win_bar)
        self.btn_min.setObjectName(u"btn_min")
        self.btn_min.setMinimumSize(QSize(30, 40))
        font = QFont()
        font.setFamilies([u"Noto Rashi Hebrew Thin"])
        font.setPointSize(16)
        self.btn_min.setFont(font)
        self.btn_min.setFlat(True)

        self.horizontalLayout.addWidget(self.btn_min)

        self.btn_max = QPushButton(self.frame_win_bar)
        self.btn_max.setObjectName(u"btn_max")
        self.btn_max.setMinimumSize(QSize(30, 40))
        self.btn_max.setMaximumSize(QSize(20, 40))
        font1 = QFont()
        font1.setFamilies([u"Noto Rashi Hebrew Thin"])
        font1.setPointSize(16)
        font1.setBold(False)
        self.btn_max.setFont(font1)
        self.btn_max.setLayoutDirection(Qt.LeftToRight)
        self.btn_max.setFlat(True)

        self.horizontalLayout.addWidget(self.btn_max)

        self.btn_exit = QPushButton(self.frame_win_bar)
        self.btn_exit.setObjectName(u"btn_exit")
        self.btn_exit.setMinimumSize(QSize(30, 40))
        self.btn_exit.setMaximumSize(QSize(20, 40))
        self.btn_exit.setFont(font)
        self.btn_exit.setFlat(True)

        self.horizontalLayout.addWidget(self.btn_exit)

        self.verticalLayout.addWidget(self.frame_win_bar)

        self.frame_central = QFrame(self.centralwidget)
        self.frame_central.setObjectName(u"frame")
        self.frame_central.setStyleSheet(u"background-color: rgb(245,245,245);")
        self.layout_central = QVBoxLayout(self.frame_central)
        self.layout_central.setSpacing(0)
        self.layout_central.setObjectName(u"layout_central")
        self.layout_central.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout.addWidget(self.frame_central)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate(
            "MainWindow", u"MainWindow", None))
        self.btn_menu.setText(QCoreApplication.translate(
            "MainWindow", u" FullAxis ", None))
        self.btn_new.setText(
            QCoreApplication.translate("MainWindow", u"+", None))
        self.btn_min.setText(QCoreApplication.translate(
            "MainWindow", u"\u2014", None))
        self.btn_max.setText(QCoreApplication.translate(
            "MainWindow", u"\u25a1", None))
        self.btn_exit.setText(
            QCoreApplication.translate("MainWindow", u"X", None))
    # retranslateUi
        self.conf_buttons()
    
    def conf_buttons(self):
        set_button_icon(self.btn_min, "fa5.window-minimize", color='white', size=15)
        set_button_icon(self.btn_max, "fa5.window-maximize", color='white', size=15)
        set_button_icon(self.btn_exit, "ph.x-square", color='white', size=30)
        set_button_icon(self.btn_new, "ph.file-plus", color='white', size=25)

        self.btn_exit.clicked.connect(self.close)
        self.btn_min.clicked.connect(self.showMinimized)
        self.btn_max.clicked.connect(self._toggle_maxmin)

    def _toggle_maxmin(self):
        if self.isMaximized():
            self.showNormal()
            self.resize(1200, 650)
            set_button_icon(self.btn_max, "fa5.window-maximize", color='white', size=15)
        else:
            set_button_icon(self.btn_max, "fa5.window-restore", color='white', size=15)

            self.showMaximized()