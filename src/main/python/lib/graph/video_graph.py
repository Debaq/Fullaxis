from PySide6.QtWidgets import QWidget
from lib.CustomWidgets import CustomLabel
from UI.Ui_vng_ui import Ui_video


class WidgetVNG(QWidget, Ui_video):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUI()

    def initUI(self):
        self.label = CustomLabel()
        self.video_central_layout.addWidget(self.label)

    def action_end(self, save=False, name=None):
        self.label.stop_video(save, name)
