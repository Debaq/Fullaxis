from unicodedata import name
from PySide6.QtWidgets import QWidget
import pyqtgraph as pg
from lib.basic_graph_ui import Ui_graph
import random

class Widget_basic(QWidget, Ui_graph):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)

class WidgetTUG(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.UI_Frame = Widget_basic()
        self.UI_Frame.setupUi(self)
        self.graph_principal()
        self.mem_time = []
        self.mem_roll = []
        self.mem_pitch = []
        self.mem_yaw = []
        self.dt = 0
        self.stop = False
        self.with_delay = True

    def set_time_max(self, time):
        self.time_max = time

    def reset_graph(self):
        self.mem_time = []
        self.mem_roll = []
        self.mem_pitch = []
        self.mem_yaw = []
        self.pw_roll.clear()
        self.pw_pitch.clear()
        self.pw_yaw.clear()
        self.dt = 0

    def graph_principal(self):
        self.pw_roll = self.graph_axis("Roll")
        self.pw_pitch = self.graph_axis("Pitch")
        self.pw_yaw = self.graph_axis("Yaw")
        self.pw_roll.show()
        self.pw_pitch.show()
        self.pw_yaw.show()
        self.UI_Frame.layout_graph_principal.addWidget(self.pw_roll)
        self.UI_Frame.layout_graph_principal.addWidget(self.pw_pitch)
        self.UI_Frame.layout_graph_principal.addWidget(self.pw_yaw)

    def draw_graph(self,data):
        self.mem_time = data[0]
        self.mem_roll = data[1]
        self.mem_pitch = data[2]
        self.mem_yaw = data[3]
        plot_roll = self.pw_roll.plot(self.mem_time, self.mem_roll, pen='r', name='curve')
        plot_pitch = self.pw_pitch.plot(self.mem_time, self.mem_pitch, pen='g', name='curve')
        plot_yaw = self.pw_yaw.plot( self.mem_time, self.mem_yaw, pen='b', name='curve')
        self._extracted_from_update_graph_display_9(plot_roll, plot_pitch, plot_yaw)

    def update_graph_display(self, data):
        if self.stop == False:
            if not self.mem_time:
                self.graph_range(self.pw_roll)
                self.graph_range(self.pw_pitch)
                self.graph_range(self.pw_yaw)
            self.mem_roll.append(data[0])
            self.mem_pitch.append(data[1])
            self.calibrate_yaw(data[2])
            new_time = self.mem_time_func(data[3])
            plot_roll = self.pw_roll.plot(self.mem_time, self.mem_roll, pen='r', name='curve')
            plot_pitch = self.pw_pitch.plot(self.mem_time, self.mem_pitch, pen='g', name='curve')
            plot_yaw = self.pw_yaw.plot( self.mem_time, self.mem_yaw, pen='b', name='curve')
            if new_time > self.time_max:
                self._extracted_from_update_graph_display_9(plot_roll, plot_pitch, plot_yaw)
                self.stop = True

    def _extracted_from_update_graph_display_9(self, plot_roll, plot_pitch, plot_yaw):
        self.graph_tools(self.pw_roll, plot_roll)
        self.graph_tools(self.pw_pitch, plot_pitch)
        self.graph_tools(self.pw_yaw, plot_yaw)

    def calibrate_yaw(self,data) -> float:
        if not self.mem_yaw:
            self.dyaw = data
            new_yaw = 0
        else:
            new_yaw = data - self.dyaw
        self.mem_yaw.append(new_yaw)
        return new_yaw

    def mem_time_func(self, data) -> float:
        data = data/1000
        if not self.mem_time:
            self.dt = data
            new_time = 0
        else:
            new_time = (data - self.dt)
            last_time_plus = self.mem_time[-1] + .5
            if last_time_plus < new_time and not self.with_delay:
                diff = new_time - self.mem_time[-1]
                self.dt = self.dt + diff + .01
                new_time = (data - self.dt)
        self.mem_time.append(new_time)
        return new_time

    def graph_axis(self, name):
        pw = pg.PlotWidget(name=name)
        pw.setBackground('w')
        pw.setYRange(-90, 90)
        pw.showGrid(x=True, y=True)

        pw.setLabel('left', name, units='degrees')
        pw.setLabel('bottom', 'Time', units='s')
        return pw

    def graph_tools(self,axis,plot):
        region = pg.LinearRegionItem()
        region.setZValue(9)
        region.setRegion([0, 5]) #limite para no salirse de la pantalla
        vertical_line = pg.InfiniteLine(angle=90, movable=True)
        horizontal_line = pg.InfiniteLine(angle=0, movable=True)
        vertical_line.setPos(0)
        horizontal_line.setPos(0)
        vertical_line.setZValue(10)
        horizontal_line.setZValue(10)
        axis.addItem(vertical_line, ignoreBounds=True)
        axis.addItem(horizontal_line, ignoreBounds=True)
        axis.addItem(region)
        axis.autoRange()

    def graph_range(self, axis):
        axis.setXRange(0, self.time_max)
        
    def get_data(self):
        return [self.mem_time, self.mem_roll, self.mem_pitch, self.mem_yaw]
        


class WidgetSOT(QWidget):
    def __init__(self) -> None:
        super().__init__()
