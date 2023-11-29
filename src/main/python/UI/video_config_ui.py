# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'video_config.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
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
    QDoubleSpinBox, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QLayout, QPushButton, QSizePolicy,
    QSlider, QSpacerItem, QSpinBox, QTabWidget,
    QVBoxLayout, QWidget)

class Ui_video_config(object):
    def setupUi(self, video_config):
        if not video_config.objectName():
            video_config.setObjectName(u"video_config")
        video_config.resize(490, 599)
        self.verticalLayout = QVBoxLayout(video_config)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.label_11 = QLabel(video_config)
        self.label_11.setObjectName(u"label_11")

        self.horizontalLayout.addWidget(self.label_11)

        self.comboBox_preset = QComboBox(video_config)
        self.comboBox_preset.setObjectName(u"comboBox_preset")

        self.horizontalLayout.addWidget(self.comboBox_preset)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.line = QFrame(video_config)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line)

        self.tabWidget = QTabWidget(video_config)
        self.tabWidget.setObjectName(u"tabWidget")
        self.Camara = QWidget()
        self.Camara.setObjectName(u"Camara")
        self.verticalLayout_2 = QVBoxLayout(self.Camara)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.grid_datas = QWidget(self.Camara)
        self.grid_datas.setObjectName(u"grid_datas")
        self.gridLayout_2 = QGridLayout(self.grid_datas)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label = QLabel(self.grid_datas)
        self.label.setObjectName(u"label")

        self.gridLayout_2.addWidget(self.label, 1, 0, 1, 1)

        self.Slider_contrast = QSlider(self.grid_datas)
        self.Slider_contrast.setObjectName(u"Slider_contrast")
        self.Slider_contrast.setMaximum(100)
        self.Slider_contrast.setValue(50)
        self.Slider_contrast.setOrientation(Qt.Horizontal)

        self.gridLayout_2.addWidget(self.Slider_contrast, 2, 1, 1, 1)

        self.Slider_blackligth = QSlider(self.grid_datas)
        self.Slider_blackligth.setObjectName(u"Slider_blackligth")
        self.Slider_blackligth.setMaximum(2)
        self.Slider_blackligth.setOrientation(Qt.Horizontal)

        self.gridLayout_2.addWidget(self.Slider_blackligth, 8, 1, 1, 1)

        self.comboBox_powerline = QComboBox(self.grid_datas)
        self.comboBox_powerline.addItem("")
        self.comboBox_powerline.addItem("")
        self.comboBox_powerline.addItem("")
        self.comboBox_powerline.setObjectName(u"comboBox_powerline")

        self.gridLayout_2.addWidget(self.comboBox_powerline, 10, 1, 1, 1)

        self.label_5 = QLabel(self.grid_datas)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_2.addWidget(self.label_5, 4, 0, 1, 1)

        self.label_7 = QLabel(self.grid_datas)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_2.addWidget(self.label_7, 6, 0, 1, 1)

        self.Slider_whitebalance = QSlider(self.grid_datas)
        self.Slider_whitebalance.setObjectName(u"Slider_whitebalance")
        self.Slider_whitebalance.setMinimum(2800)
        self.Slider_whitebalance.setMaximum(6500)
        self.Slider_whitebalance.setSingleStep(10)
        self.Slider_whitebalance.setValue(4600)
        self.Slider_whitebalance.setOrientation(Qt.Horizontal)

        self.gridLayout_2.addWidget(self.Slider_whitebalance, 7, 1, 1, 1)

        self.Slider_brightness = QSlider(self.grid_datas)
        self.Slider_brightness.setObjectName(u"Slider_brightness")
        self.Slider_brightness.setMinimum(-64)
        self.Slider_brightness.setMaximum(64)
        self.Slider_brightness.setOrientation(Qt.Horizontal)

        self.gridLayout_2.addWidget(self.Slider_brightness, 1, 1, 1, 1)

        self.Slider_gamma = QSlider(self.grid_datas)
        self.Slider_gamma.setObjectName(u"Slider_gamma")
        self.Slider_gamma.setMinimum(100)
        self.Slider_gamma.setMaximum(500)
        self.Slider_gamma.setValue(300)
        self.Slider_gamma.setOrientation(Qt.Horizontal)

        self.gridLayout_2.addWidget(self.Slider_gamma, 4, 1, 1, 1)

        self.checkBox_whitebalance = QCheckBox(self.grid_datas)
        self.checkBox_whitebalance.setObjectName(u"checkBox_whitebalance")

        self.gridLayout_2.addWidget(self.checkBox_whitebalance, 9, 1, 1, 1)

        self.Slider_sharpness = QSlider(self.grid_datas)
        self.Slider_sharpness.setObjectName(u"Slider_sharpness")
        self.Slider_sharpness.setMaximum(100)
        self.Slider_sharpness.setValue(50)
        self.Slider_sharpness.setOrientation(Qt.Horizontal)

        self.gridLayout_2.addWidget(self.Slider_sharpness, 6, 1, 1, 1)

        self.Slider_hue = QSlider(self.grid_datas)
        self.Slider_hue.setObjectName(u"Slider_hue")
        self.Slider_hue.setMinimum(-180)
        self.Slider_hue.setMaximum(180)
        self.Slider_hue.setValue(0)
        self.Slider_hue.setOrientation(Qt.Horizontal)

        self.gridLayout_2.addWidget(self.Slider_hue, 3, 1, 1, 1)

        self.label_8 = QLabel(self.grid_datas)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_2.addWidget(self.label_8, 8, 0, 1, 1)

        self.label_6 = QLabel(self.grid_datas)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_2.addWidget(self.label_6, 7, 0, 1, 1)

        self.label_4 = QLabel(self.grid_datas)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_2.addWidget(self.label_4, 3, 0, 1, 1)

        self.Slider_saturation = QSlider(self.grid_datas)
        self.Slider_saturation.setObjectName(u"Slider_saturation")
        self.Slider_saturation.setMaximum(100)
        self.Slider_saturation.setValue(50)
        self.Slider_saturation.setOrientation(Qt.Horizontal)

        self.gridLayout_2.addWidget(self.Slider_saturation, 5, 1, 1, 1)

        self.label_2 = QLabel(self.grid_datas)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_2.addWidget(self.label_2, 2, 0, 1, 1)

        self.label_10 = QLabel(self.grid_datas)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout_2.addWidget(self.label_10, 10, 0, 1, 1)

        self.label_3 = QLabel(self.grid_datas)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_2.addWidget(self.label_3, 5, 0, 1, 1)

        self.checkBox_exposure = QCheckBox(self.grid_datas)
        self.checkBox_exposure.setObjectName(u"checkBox_exposure")
        self.checkBox_exposure.setLayoutDirection(Qt.LeftToRight)
        self.checkBox_exposure.setChecked(False)

        self.gridLayout_2.addWidget(self.checkBox_exposure, 9, 0, 1, 1)

        self.lbl_brightness = QLabel(self.grid_datas)
        self.lbl_brightness.setObjectName(u"lbl_brightness")

        self.gridLayout_2.addWidget(self.lbl_brightness, 1, 2, 1, 1)

        self.lbl_contrast = QLabel(self.grid_datas)
        self.lbl_contrast.setObjectName(u"lbl_contrast")

        self.gridLayout_2.addWidget(self.lbl_contrast, 2, 2, 1, 1)

        self.lbl_hue = QLabel(self.grid_datas)
        self.lbl_hue.setObjectName(u"lbl_hue")

        self.gridLayout_2.addWidget(self.lbl_hue, 3, 2, 1, 1)

        self.lbl_gamma = QLabel(self.grid_datas)
        self.lbl_gamma.setObjectName(u"lbl_gamma")

        self.gridLayout_2.addWidget(self.lbl_gamma, 4, 2, 1, 1)

        self.lbl_saturation = QLabel(self.grid_datas)
        self.lbl_saturation.setObjectName(u"lbl_saturation")

        self.gridLayout_2.addWidget(self.lbl_saturation, 5, 2, 1, 1)

        self.lbl_sharpness = QLabel(self.grid_datas)
        self.lbl_sharpness.setObjectName(u"lbl_sharpness")

        self.gridLayout_2.addWidget(self.lbl_sharpness, 6, 2, 1, 1)

        self.lbl_whitebalance = QLabel(self.grid_datas)
        self.lbl_whitebalance.setObjectName(u"lbl_whitebalance")

        self.gridLayout_2.addWidget(self.lbl_whitebalance, 7, 2, 1, 1)

        self.lbl_blackligth = QLabel(self.grid_datas)
        self.lbl_blackligth.setObjectName(u"lbl_blackligth")

        self.gridLayout_2.addWidget(self.lbl_blackligth, 8, 2, 1, 1)


        self.verticalLayout_2.addWidget(self.grid_datas)

        self.tabWidget.addTab(self.Camara, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.gridLayout = QGridLayout(self.tab_2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.checkBox = QCheckBox(self.tab_2)
        self.checkBox.setObjectName(u"checkBox")

        self.gridLayout.addWidget(self.checkBox, 0, 1, 1, 1)

        self.label_16 = QLabel(self.tab_2)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_16, 4, 5, 1, 1)

        self.label_17 = QLabel(self.tab_2)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_17, 4, 7, 1, 1)

        self.label_19 = QLabel(self.tab_2)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_19, 5, 5, 1, 1)

        self.cb_ksize_equals = QCheckBox(self.tab_2)
        self.cb_ksize_equals.setObjectName(u"cb_ksize_equals")
        self.cb_ksize_equals.setChecked(True)

        self.gridLayout.addWidget(self.cb_ksize_equals, 2, 3, 1, 1)

        self.sb_param1_hough = QDoubleSpinBox(self.tab_2)
        self.sb_param1_hough.setObjectName(u"sb_param1_hough")
        self.sb_param1_hough.setMinimum(0.100000000000000)
        self.sb_param1_hough.setSingleStep(0.100000000000000)
        self.sb_param1_hough.setValue(50.000000000000000)

        self.gridLayout.addWidget(self.sb_param1_hough, 4, 8, 1, 1)

        self.sb_maxrad_hough = QSpinBox(self.tab_2)
        self.sb_maxrad_hough.setObjectName(u"sb_maxrad_hough")

        self.gridLayout.addWidget(self.sb_maxrad_hough, 5, 8, 1, 1)

        self.sb_ksizew_hough = QSpinBox(self.tab_2)
        self.sb_ksizew_hough.setObjectName(u"sb_ksizew_hough")

        self.gridLayout.addWidget(self.sb_ksizew_hough, 2, 5, 1, 1)

        self.label_13 = QLabel(self.tab_2)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_13, 2, 1, 1, 1)

        self.label_14 = QLabel(self.tab_2)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_14, 2, 6, 1, 1)

        self.label_21 = QLabel(self.tab_2)
        self.label_21.setObjectName(u"label_21")

        self.gridLayout.addWidget(self.label_21, 2, 4, 1, 1)

        self.label_18 = QLabel(self.tab_2)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_18, 5, 1, 1, 1)

        self.sb_param2_hough = QDoubleSpinBox(self.tab_2)
        self.sb_param2_hough.setObjectName(u"sb_param2_hough")
        self.sb_param2_hough.setMinimum(0.100000000000000)
        self.sb_param2_hough.setSingleStep(0.100000000000000)
        self.sb_param2_hough.setValue(30.000000000000000)

        self.gridLayout.addWidget(self.sb_param2_hough, 5, 2, 1, 1)

        self.sb_mindist_hough = QDoubleSpinBox(self.tab_2)
        self.sb_mindist_hough.setObjectName(u"sb_mindist_hough")
        self.sb_mindist_hough.setMinimum(0.100000000000000)
        self.sb_mindist_hough.setSingleStep(0.100000000000000)
        self.sb_mindist_hough.setValue(20.000000000000000)

        self.gridLayout.addWidget(self.sb_mindist_hough, 4, 6, 1, 1)

        self.sb_dp_hough = QDoubleSpinBox(self.tab_2)
        self.sb_dp_hough.setObjectName(u"sb_dp_hough")
        self.sb_dp_hough.setMinimum(0.100000000000000)
        self.sb_dp_hough.setSingleStep(0.100000000000000)
        self.sb_dp_hough.setValue(1.000000000000000)

        self.gridLayout.addWidget(self.sb_dp_hough, 4, 2, 1, 1)

        self.label_12 = QLabel(self.tab_2)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_12, 3, 1, 1, 8)

        self.sb_ksizeh_hough = QSpinBox(self.tab_2)
        self.sb_ksizeh_hough.setObjectName(u"sb_ksizeh_hough")
        self.sb_ksizeh_hough.setMinimum(1)
        self.sb_ksizeh_hough.setSingleStep(1)
        self.sb_ksizeh_hough.setStepType(QAbstractSpinBox.DefaultStepType)
        self.sb_ksizeh_hough.setValue(1)

        self.gridLayout.addWidget(self.sb_ksizeh_hough, 2, 2, 1, 1)

        self.label_15 = QLabel(self.tab_2)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_15, 4, 1, 1, 1)

        self.sb_minrad_hough = QSpinBox(self.tab_2)
        self.sb_minrad_hough.setObjectName(u"sb_minrad_hough")

        self.gridLayout.addWidget(self.sb_minrad_hough, 5, 6, 1, 1)

        self.sb_sigma_hough = QDoubleSpinBox(self.tab_2)
        self.sb_sigma_hough.setObjectName(u"sb_sigma_hough")
        self.sb_sigma_hough.setSingleStep(0.100000000000000)

        self.gridLayout.addWidget(self.sb_sigma_hough, 2, 7, 1, 1)

        self.label_20 = QLabel(self.tab_2)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_20, 5, 7, 1, 1)

        self.label_9 = QLabel(self.tab_2)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_9, 1, 1, 1, 8)

        self.tabWidget.addTab(self.tab_2, "")
        self.Canny = QWidget()
        self.Canny.setObjectName(u"Canny")
        self.tabWidget.addTab(self.Canny, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.tabWidget.addTab(self.tab_4, "")

        self.verticalLayout.addWidget(self.tabWidget)

        self.pushButton_resetpreset = QPushButton(video_config)
        self.pushButton_resetpreset.setObjectName(u"pushButton_resetpreset")

        self.verticalLayout.addWidget(self.pushButton_resetpreset)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.pushButton_savepreset = QPushButton(video_config)
        self.pushButton_savepreset.setObjectName(u"pushButton_savepreset")

        self.horizontalLayout_2.addWidget(self.pushButton_savepreset)

        self.pushButton_newpreset = QPushButton(video_config)
        self.pushButton_newpreset.setObjectName(u"pushButton_newpreset")

        self.horizontalLayout_2.addWidget(self.pushButton_newpreset)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.pushButton_ok = QPushButton(video_config)
        self.pushButton_ok.setObjectName(u"pushButton_ok")

        self.verticalLayout.addWidget(self.pushButton_ok)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer)

        QWidget.setTabOrder(self.comboBox_preset, self.tabWidget)
        QWidget.setTabOrder(self.tabWidget, self.checkBox)
        QWidget.setTabOrder(self.checkBox, self.sb_ksizeh_hough)
        QWidget.setTabOrder(self.sb_ksizeh_hough, self.cb_ksize_equals)
        QWidget.setTabOrder(self.cb_ksize_equals, self.sb_ksizew_hough)
        QWidget.setTabOrder(self.sb_ksizew_hough, self.sb_sigma_hough)
        QWidget.setTabOrder(self.sb_sigma_hough, self.sb_dp_hough)
        QWidget.setTabOrder(self.sb_dp_hough, self.sb_param2_hough)
        QWidget.setTabOrder(self.sb_param2_hough, self.sb_mindist_hough)
        QWidget.setTabOrder(self.sb_mindist_hough, self.sb_minrad_hough)
        QWidget.setTabOrder(self.sb_minrad_hough, self.sb_param1_hough)
        QWidget.setTabOrder(self.sb_param1_hough, self.sb_maxrad_hough)
        QWidget.setTabOrder(self.sb_maxrad_hough, self.pushButton_resetpreset)
        QWidget.setTabOrder(self.pushButton_resetpreset, self.pushButton_savepreset)
        QWidget.setTabOrder(self.pushButton_savepreset, self.pushButton_newpreset)
        QWidget.setTabOrder(self.pushButton_newpreset, self.pushButton_ok)
        QWidget.setTabOrder(self.pushButton_ok, self.Slider_whitebalance)
        QWidget.setTabOrder(self.Slider_whitebalance, self.Slider_blackligth)
        QWidget.setTabOrder(self.Slider_blackligth, self.Slider_contrast)
        QWidget.setTabOrder(self.Slider_contrast, self.Slider_hue)
        QWidget.setTabOrder(self.Slider_hue, self.checkBox_exposure)
        QWidget.setTabOrder(self.checkBox_exposure, self.checkBox_whitebalance)
        QWidget.setTabOrder(self.checkBox_whitebalance, self.comboBox_powerline)
        QWidget.setTabOrder(self.comboBox_powerline, self.Slider_brightness)
        QWidget.setTabOrder(self.Slider_brightness, self.Slider_sharpness)
        QWidget.setTabOrder(self.Slider_sharpness, self.Slider_saturation)
        QWidget.setTabOrder(self.Slider_saturation, self.Slider_gamma)

        self.retranslateUi(video_config)

        self.tabWidget.setCurrentIndex(1)
        self.comboBox_powerline.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(video_config)
    # setupUi

    def retranslateUi(self, video_config):
        video_config.setWindowTitle(QCoreApplication.translate("video_config", u"Form", None))
        self.label_11.setText(QCoreApplication.translate("video_config", u"Preset", None))
        self.label.setText(QCoreApplication.translate("video_config", u"Brightness", None))
        self.comboBox_powerline.setItemText(0, QCoreApplication.translate("video_config", u"Disabled", None))
        self.comboBox_powerline.setItemText(1, QCoreApplication.translate("video_config", u"50Hz", None))
        self.comboBox_powerline.setItemText(2, QCoreApplication.translate("video_config", u"60Hz", None))

        self.label_5.setText(QCoreApplication.translate("video_config", u"Gamma", None))
        self.label_7.setText(QCoreApplication.translate("video_config", u"Sharpness", None))
        self.checkBox_whitebalance.setText(QCoreApplication.translate("video_config", u"White Balance, Automatic ", None))
        self.label_8.setText(QCoreApplication.translate("video_config", u"Blackligth Compensation", None))
        self.label_6.setText(QCoreApplication.translate("video_config", u"White Balance Temperature", None))
        self.label_4.setText(QCoreApplication.translate("video_config", u"Hue", None))
        self.label_2.setText(QCoreApplication.translate("video_config", u"Contrast", None))
        self.label_10.setText(QCoreApplication.translate("video_config", u"Power Line Frecuency", None))
        self.label_3.setText(QCoreApplication.translate("video_config", u"Saturation", None))
        self.checkBox_exposure.setText(QCoreApplication.translate("video_config", u"Exposure, dynamic framerate", None))
        self.lbl_brightness.setText("")
        self.lbl_contrast.setText("")
        self.lbl_hue.setText("")
        self.lbl_gamma.setText("")
        self.lbl_saturation.setText("")
        self.lbl_sharpness.setText("")
        self.lbl_whitebalance.setText("")
        self.lbl_blackligth.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Camara), QCoreApplication.translate("video_config", u"Camara", None))
        self.checkBox.setText(QCoreApplication.translate("video_config", u"Activate", None))
        self.label_16.setText(QCoreApplication.translate("video_config", u"minDist", None))
        self.label_17.setText(QCoreApplication.translate("video_config", u"param1", None))
        self.label_19.setText(QCoreApplication.translate("video_config", u"minRadius", None))
        self.cb_ksize_equals.setText(QCoreApplication.translate("video_config", u"=", None))
        self.label_13.setText(QCoreApplication.translate("video_config", u"KsizeH", None))
        self.label_14.setText(QCoreApplication.translate("video_config", u"Sigma", None))
        self.label_21.setText(QCoreApplication.translate("video_config", u"KsizeW", None))
        self.label_18.setText(QCoreApplication.translate("video_config", u"Param2", None))
        self.label_12.setText(QCoreApplication.translate("video_config", u"Circles", None))
        self.label_15.setText(QCoreApplication.translate("video_config", u"dp", None))
        self.label_20.setText(QCoreApplication.translate("video_config", u"MaxRadius", None))
        self.label_9.setText(QCoreApplication.translate("video_config", u"Blurred", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("video_config", u"HoughCircles", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Canny), QCoreApplication.translate("video_config", u"Canny", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("video_config", u"Blobs", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QCoreApplication.translate("video_config", u"P\u00e1gina", None))
        self.pushButton_resetpreset.setText(QCoreApplication.translate("video_config", u"Reset Preset", None))
        self.pushButton_savepreset.setText(QCoreApplication.translate("video_config", u"Save preset", None))
        self.pushButton_newpreset.setText(QCoreApplication.translate("video_config", u"Create new preset", None))
        self.pushButton_ok.setText(QCoreApplication.translate("video_config", u"OK", None))
    # retranslateUi

