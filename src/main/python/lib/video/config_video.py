import json

from base import context
from lib.dialog_helpers import ErrorMessageBox, NameDialog
from PySide6.QtCore import QCoreApplication, QRegularExpression, Signal
from PySide6.QtWidgets import (QDialog, QDoubleSpinBox, QLabel, QSlider,
                               QSpinBox)
from UI.video_config_ui import Ui_video_config


class ConfigVideoWindow(QDialog, Ui_video_config):
    slides_values = Signal(dict)
    strategy_values = Signal(dict)

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle(QCoreApplication.translate(
            "video_config", u"Configuración de Vídeo", None))
        self.setGeometry(100, 100, 300, 200)
        # self.setWindowFlags(Qt.FramelessWindowHint)
        self.slides = self.grid_datas.findChildren(QSlider)
        self.lbl_values = self.grid_datas.findChildren(QLabel)

        self.open_config()
        self.load_preset()
        self.preset_changed_values(self.data['last'], True)
        self.slides_config()
        self.config_btn()

    def config_btn(self):
        self.pushButton_savepreset.clicked.connect(self.save_values)
        self.pushButton_newpreset.clicked.connect(self.create_new_preset)
        self.doubles = self.tab_2.findChildren(QDoubleSpinBox)
        self.spin = self.tab_2.findChildren(QSpinBox)
        for i in self.doubles:
            i.valueChanged.connect(self.houghcircles_setting)
        for i in self.spin:
            i.valueChanged.connect(self.houghcircles_setting)


    def open_config(self):
        with open(context.get_resource('setting/video_config.json'), 'r') as f:
            self.data = json.load(f)

    def load_preset(self):
        for i in self.data:
            if i != 'last':
                self.comboBox_preset.addItem(i)
        self.comboBox_preset.setCurrentText(self.data['last'])
        self.comboBox_preset.currentTextChanged.connect(
            self.preset_changed_values)

    def preset_changed_values(self, preset_name, init=False):
        for i in self.slides:
            name_end = i.objectName().replace('Slider_', '')
            i.setValue(self.data[preset_name][name_end])

        self.slider_changed()
        self.save_values(init)

    def create_new_preset(self):
        values = self.slider_changed()
        dialog = NameDialog()
        if dialog.exec_():
            print("creando")
            name = dialog.get_name()
            self.data[name] = values
            self.data['protect'] = False
            self.comboBox_preset.addItem(name)
            self.comboBox_preset.setCurrentText(name)
            self.save_values()

    def save_values(self, init=False):
        values = self.slider_changed()
        name = self.comboBox_preset.currentText()
        if self.data[name]['protect'] is True:
            if init is False:
                msg = ErrorMessageBox("Error", "No se puede modificar")
                msg.exec_()
        else:
            for i in self.data[name]:
                if i in values:
                    self.data[name][i] = values[i]
            # self.data[name] = values
            self.data['last'] = name
            with open(context.get_resource('setting/video_config.json'), 'w') as f:
                json.dump(self.data, f)

    def slides_config(self):
        for i in self.slides:
            name_end = i.objectName().replace('Slider_', '')
            for j in self.lbl_values:
                if j.objectName().endswith(name_end):
                    j.setText(str(i.value()))
            i.valueChanged.connect(self.slider_changed)

    def slider_changed(self):
        slides_values = {}
        for i in self.slides:
            name_end = i.objectName().replace('Slider_', '')
            val = i.value()
            slides_values[name_end] = val
            for j in self.lbl_values:
                if j.objectName().endswith(name_end):
                    j.setText(str(i.value()))

        self.slides_values.emit(slides_values)
        return slides_values
    
    def houghcircles_setting(self):
        blurred = {'ksizeW' : self.sb_ksize_hough.value(), 
                  'ksizeH': self.sb_ksize_hough.value(), 
                  'sigmaX': self.sb_sigma_hough.value()}
        hough = {'dp':self.sb_dp_hough.value(), 'minDist':self.sb_mindist_hough.value(), 
                 'param1':self.sb_param1_hough.value(), 'param2':self.sb_param2_hough.value(), 
                 'minRadius':self.sb_minrad_hough.value(),'maxRadius':self.sb_maxrad_hough.value()}
        result = {'hough':{'hough': hough, 'blurred': blurred }}
        self.strategy_values.emit(result)

