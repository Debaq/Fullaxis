from UI.Ui_basic_graph_ui import Ui_graph
from PySide6.QtWidgets import QWidget


class Widget_basic(QWidget, Ui_graph):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)