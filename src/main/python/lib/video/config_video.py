from PySide6.QtWidgets import QDialog
from UI.Ui_video_config import Ui_video_config
from PySide6.QtCore import Signal, QCoreApplication
from PySide6.QtWidgets import QSlider, QLabel
import json
from base import context
from lib.dialog_helpers import NameDialog, ErrorMessageBox


class ConfigVideoWindow(QDialog, Ui_video_config):
    slides_values = Signal(dict)

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
            name = dialog.get_name()
            self.data[name] = values
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
