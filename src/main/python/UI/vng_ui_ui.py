# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'vng_ui.ui'
##
## Created by: Qt User Interface Compiler version 6.4.3
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
    QSizePolicy, QTreeWidget, QTreeWidgetItem, QVBoxLayout,
    QWidget)

class Ui_video(object):
    def setupUi(self, video):
        if not video.objectName():
            video.setObjectName(u"video")
        video.resize(400, 300)
        self.verticalLayout = QVBoxLayout(video)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalFrame = QFrame(video)
        self.horizontalFrame.setObjectName(u"horizontalFrame")
        self.horizontalLayout = QHBoxLayout(self.horizontalFrame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")

        self.verticalLayout.addWidget(self.horizontalFrame)

        self.video_central_frame = QFrame(video)
        self.video_central_frame.setObjectName(u"video_central_frame")
        self.video_central_layout = QHBoxLayout(self.video_central_frame)
        self.video_central_layout.setObjectName(u"video_central_layout")
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

        self.video_central_layout.addWidget(self.treeWidget)

        self.video_frame = QFrame(self.video_central_frame)
        self.video_frame.setObjectName(u"video_frame")
        self.video_layout = QHBoxLayout(self.video_frame)
        self.video_layout.setObjectName(u"video_layout")

        self.video_central_layout.addWidget(self.video_frame)


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

    # retranslateUi
