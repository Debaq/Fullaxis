# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'vng_uiqWUUFg.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFrame,
    QHBoxLayout, QHeaderView, QLabel, QPushButton,
    QSizePolicy, QSlider, QSpacerItem, QTextEdit,
    QTreeWidget, QTreeWidgetItem, QVBoxLayout, QWidget)

class Ui_video(object):
    def setupUi(self, video):
        if not video.objectName():
            video.setObjectName(u"video")
        video.resize(832, 520)
        self.verticalLayout = QVBoxLayout(video)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalFrame = QFrame(video)
        self.horizontalFrame.setObjectName(u"horizontalFrame")
        self.horizontalLayout = QHBoxLayout(self.horizontalFrame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lbl_name_user = QLabel(self.horizontalFrame)
        self.lbl_name_user.setObjectName(u"lbl_name_user")
        font = QFont()
        font.setBold(True)
        self.lbl_name_user.setFont(font)

        self.horizontalLayout.addWidget(self.lbl_name_user)

        self.btn_save = QPushButton(self.horizontalFrame)
        self.btn_save.setObjectName(u"btn_save")

        self.horizontalLayout.addWidget(self.btn_save)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_5)

        self.lbl_test_name = QLabel(self.horizontalFrame)
        self.lbl_test_name.setObjectName(u"lbl_test_name")

        self.horizontalLayout.addWidget(self.lbl_test_name)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.label = QLabel(self.horizontalFrame)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.cb_hardware = QComboBox(self.horizontalFrame)
        self.cb_hardware.setObjectName(u"cb_hardware")

        self.horizontalLayout.addWidget(self.cb_hardware)


        self.verticalLayout.addWidget(self.horizontalFrame)

        self.video_central_frame = QFrame(video)
        self.video_central_frame.setObjectName(u"video_central_frame")
        self.video_central_layout = QHBoxLayout(self.video_central_frame)
        self.video_central_layout.setObjectName(u"video_central_layout")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, -1, -1, -1)
        self.treeWidget = QTreeWidget(self.video_central_frame)
        __qtreewidgetitem = QTreeWidgetItem(self.treeWidget)
        QTreeWidgetItem(__qtreewidgetitem)
        QTreeWidgetItem(__qtreewidgetitem)
        __qtreewidgetitem1 = QTreeWidgetItem(self.treeWidget)
        QTreeWidgetItem(__qtreewidgetitem1)
        QTreeWidgetItem(__qtreewidgetitem1)
        __qtreewidgetitem2 = QTreeWidgetItem(self.treeWidget)
        QTreeWidgetItem(__qtreewidgetitem2)
        QTreeWidgetItem(__qtreewidgetitem2)
        QTreeWidgetItem(self.treeWidget)
        self.treeWidget.setObjectName(u"treeWidget")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.treeWidget.sizePolicy().hasHeightForWidth())
        self.treeWidget.setSizePolicy(sizePolicy)
        self.treeWidget.setMinimumSize(QSize(0, 150))
        self.treeWidget.setMaximumSize(QSize(150, 16777215))

        self.horizontalLayout_4.addWidget(self.treeWidget)

        self.verticalFrame = QFrame(self.video_central_frame)
        self.verticalFrame.setObjectName(u"verticalFrame")
        self.verticalFrame.setMinimumSize(QSize(0, 0))
        self.verticalLayout_3 = QVBoxLayout(self.verticalFrame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.textEdit = QTextEdit(self.verticalFrame)
        self.textEdit.setObjectName(u"textEdit")

        self.verticalLayout_3.addWidget(self.textEdit)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(-1, 0, -1, -1)
        self.btn_play = QPushButton(self.verticalFrame)
        self.btn_play.setObjectName(u"btn_play")

        self.verticalLayout_4.addWidget(self.btn_play)

        self.btn_stop = QPushButton(self.verticalFrame)
        self.btn_stop.setObjectName(u"btn_stop")

        self.verticalLayout_4.addWidget(self.btn_stop)

        self.btn_fix = QPushButton(self.verticalFrame)
        self.btn_fix.setObjectName(u"btn_fix")

        self.verticalLayout_4.addWidget(self.btn_fix)


        self.verticalLayout_3.addLayout(self.verticalLayout_4)


        self.horizontalLayout_4.addWidget(self.verticalFrame)


        self.video_central_layout.addLayout(self.horizontalLayout_4)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.video_central_layout.addItem(self.horizontalSpacer_3)

        self.video_frame = QFrame(self.video_central_frame)
        self.video_frame.setObjectName(u"video_frame")
        self.video_frame.setMinimumSize(QSize(640, 0))
        self.video_frame.setMaximumSize(QSize(640, 16777215))
        self.verticalLayout_2 = QVBoxLayout(self.video_frame)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.cbx_auto = QCheckBox(self.video_frame)
        self.cbx_auto.setObjectName(u"cbx_auto")

        self.horizontalLayout_2.addWidget(self.cbx_auto)

        self.Slicer_OD = QSlider(self.video_frame)
        self.Slicer_OD.setObjectName(u"Slicer_OD")
        self.Slicer_OD.setCursor(QCursor(Qt.SizeHorCursor))
        self.Slicer_OD.setMaximum(255)
        self.Slicer_OD.setTracking(True)
        self.Slicer_OD.setOrientation(Qt.Horizontal)
        self.Slicer_OD.setInvertedAppearance(False)
        self.Slicer_OD.setInvertedControls(False)
        self.Slicer_OD.setTickPosition(QSlider.NoTicks)
        self.Slicer_OD.setTickInterval(6)

        self.horizontalLayout_2.addWidget(self.Slicer_OD)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.Slicer_OI = QSlider(self.video_frame)
        self.Slicer_OI.setObjectName(u"Slicer_OI")
        self.Slicer_OI.setCursor(QCursor(Qt.SizeHorCursor))
        self.Slicer_OI.setOrientation(Qt.Horizontal)

        self.horizontalLayout_2.addWidget(self.Slicer_OI)

        self.btn_configvideo = QPushButton(self.video_frame)
        self.btn_configvideo.setObjectName(u"btn_configvideo")

        self.horizontalLayout_2.addWidget(self.btn_configvideo)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)


        self.video_central_layout.addWidget(self.video_frame)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.video_central_layout.addItem(self.horizontalSpacer_4)


        self.verticalLayout.addWidget(self.video_central_frame)

        self.horizontalFrame_3 = QFrame(video)
        self.horizontalFrame_3.setObjectName(u"horizontalFrame_3")
        self.horizontalLayout_3 = QHBoxLayout(self.horizontalFrame_3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")

        self.verticalLayout.addWidget(self.horizontalFrame_3)


        self.retranslateUi(video)

        QMetaObject.connectSlotsByName(video)
    # setupUi

    def retranslateUi(self, video):
        video.setWindowTitle(QCoreApplication.translate("video", u"Form", None))
        self.lbl_name_user.setText(QCoreApplication.translate("video", u"Nuevo sin guardar", None))
        self.btn_save.setText(QCoreApplication.translate("video", u"Guardar", None))
        self.lbl_test_name.setText("")
        self.label.setText(QCoreApplication.translate("video", u"Dispositivo", None))
        ___qtreewidgetitem = self.treeWidget.headerItem()
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("video", u"Test VNG", None));

        __sortingEnabled = self.treeWidget.isSortingEnabled()
        self.treeWidget.setSortingEnabled(False)
        ___qtreewidgetitem1 = self.treeWidget.topLevelItem(0)
        ___qtreewidgetitem1.setText(0, QCoreApplication.translate("video", u"Calorica", None));
        ___qtreewidgetitem2 = ___qtreewidgetitem1.child(0)
        ___qtreewidgetitem2.setText(0, QCoreApplication.translate("video", u"bitermal alternada", None));
        ___qtreewidgetitem3 = ___qtreewidgetitem1.child(1)
        ___qtreewidgetitem3.setText(0, QCoreApplication.translate("video", u"monotermal alternada", None));
        ___qtreewidgetitem4 = self.treeWidget.topLevelItem(1)
        ___qtreewidgetitem4.setText(0, QCoreApplication.translate("video", u"Nistagmo", None));
        ___qtreewidgetitem5 = ___qtreewidgetitem4.child(0)
        ___qtreewidgetitem5.setText(0, QCoreApplication.translate("video", u"Posicional", None));
        ___qtreewidgetitem6 = ___qtreewidgetitem4.child(1)
        ___qtreewidgetitem6.setText(0, QCoreApplication.translate("video", u"Espontaneo", None));
        ___qtreewidgetitem7 = self.treeWidget.topLevelItem(2)
        ___qtreewidgetitem7.setText(0, QCoreApplication.translate("video", u"Oculomotoras", None));
        ___qtreewidgetitem8 = ___qtreewidgetitem7.child(0)
        ___qtreewidgetitem8.setText(0, QCoreApplication.translate("video", u"sacadas", None));
        ___qtreewidgetitem9 = ___qtreewidgetitem7.child(1)
        ___qtreewidgetitem9.setText(0, QCoreApplication.translate("video", u"seguimiento", None));
        self.treeWidget.setSortingEnabled(__sortingEnabled)

        self.btn_play.setText(QCoreApplication.translate("video", u"Iniciar", None))
        self.btn_stop.setText(QCoreApplication.translate("video", u"Detener", None))
        self.btn_fix.setText(QCoreApplication.translate("video", u"Fijar", None))
        self.cbx_auto.setText(QCoreApplication.translate("video", u"Auto", None))
        self.btn_configvideo.setText("")
    # retranslateUi

