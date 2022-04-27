import numpy as np
import pyqtgraph as pg
from numpy import roll
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import (QFrame, QHBoxLayout, 
                               QVBoxLayout, QLabel, 
                               QWidget, QSizePolicy,QSpacerItem)

from init import context
from lib.basic_graph_ui import Ui_graph

from scipy.signal import find_peaks, peak_widths


class Widget_basic(QWidget, Ui_graph):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)

class WidgetTUG(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.lastClicked = []
        self.UI_Frame = Widget_basic()
        self.UI_Frame.setupUi(self)
        self.create_memories()
        self.load_variables()
        self.create_qframes()
        self.load_images()
        self.graph_principal()

    def create_qframes(self):
        self.frame_pitch = QFrame(self)
        self.frame_roll = QFrame(self)
        self.frame_yaw = QFrame(self)
        self.layout_pitch = self.create_qlayout_prop(self.frame_pitch)
        self.layout_roll = self.create_qlayout_prop(self.frame_roll)
        self.layout_yaw = self.create_qlayout_prop(self.frame_yaw)
        self.UI_Frame.layout_graph_principal.addWidget(self.frame_pitch)
        self.UI_Frame.layout_graph_principal.addWidget(self.frame_roll)
        self.UI_Frame.layout_graph_principal.addWidget(self.frame_yaw)
    
    def create_qlayout_prop(self, frame:QFrame)->QHBoxLayout:
        layout = QHBoxLayout(frame)
        layout.setSpacing(3)
        layout.setContentsMargins(0, 0, 0, 0)
        return layout
        
    def load_images(self):
        self.helper_image(self.frame_pitch, self.layout_pitch, "pos_pitch.png")
        self.helper_image(self.frame_roll, self.layout_roll, "pos_roll.png")
        self.helper_image(self.frame_yaw, self.layout_yaw, "pos_yaw.png")
    
    def helper_image(self, frame:QFrame, layout:QHBoxLayout, name_image:str) -> None:
        lbl = QLabel(frame)
        image = QPixmap(context.get_resource(name_image))
        image = image.scaledToHeight(115)
        lbl.setPixmap(image)
        layout.addWidget(lbl)
        
    def graph_principal(self):
        self.pw_roll = self.graph_axis("Roll")
        self.pw_pitch = self.graph_axis("Pitch")
        self.pw_yaw = self.graph_axis("Yaw")
        self.pw_roll.show()
        self.pw_pitch.show()
        self.pw_yaw.show()
        self.layout_roll.addWidget(self.pw_roll)
        self.layout_pitch.addWidget(self.pw_pitch)
        self.layout_yaw.addWidget(self.pw_yaw)
        
    def load_variables(self):
        self.dt = 0
        self.stop = False
        self.with_delay = True
        
    def create_memories(self):
        self.mem_time = np.empty(0, dtype=np.float64)
        self.mem_roll = np.empty(0, dtype=np.float64)
        self.mem_pitch = np.empty(0, dtype=np.float64)
        self.mem_yaw = np.empty(0, dtype=np.float64)

    def set_time_max(self, time):
        self.time_max = time
        self.stop = False

    def reset_graph(self):
        self.create_memories()
        self.clear_data()
        self.dt = 0

    def draw_graph(self,data):
        self.mem_time = np.append(self.mem_time , data[3])
        self.update_memories(data)

        peaks_roll, _ = find_peaks(self.mem_roll, distance=10)
        self.pw_roll.plot(x=self.mem_time[peaks_roll], y=self.mem_roll[peaks_roll], symbol='t')
        results_half = peak_widths(self.mem_roll, peaks_roll, rel_height=0.5)
        results_full = peak_widths(self.mem_roll, peaks_roll, rel_height=1)
        print(results_half)
        #line = pg.LineROI([0, 60], [20, 80], width=5, pen=(1,9))
        #self.pw_roll.addItem(line)


        peaks_pitch, _ = find_peaks(self.mem_pitch, distance=10)
        self.pw_pitch.plot(x=self.mem_time[peaks_pitch], y=self.mem_pitch[peaks_pitch], symbol='t')
        peaks_yaw, _ = find_peaks(self.mem_yaw, distance=10)
        self.pw_yaw.plot(x=self.mem_time[peaks_yaw], y=self.mem_yaw[peaks_yaw], symbol='t')


        plot_roll = self.set_curve(self.mem_time, self.mem_roll, pen='r')
        plot_pitch = self.set_curve(self.mem_time, self.mem_pitch, pen='g')
        plot_yaw = self.set_curve(self.mem_time, self.mem_yaw, pen='b')

          
        self.pw_roll.addItem(plot_roll)
        self.pw_pitch.addItem(plot_pitch)
        self.pw_yaw.addItem(plot_yaw)

        self._extracted_from_update_graph_display_9(plot_roll, plot_pitch, plot_yaw)

    def detect_up_stand(self, data) -> list:
        result = 0
        return result 
    
    def set_curve(self, data_x, data_y, pen):
        curve = pg.PlotCurveItem()
        curve.setClickable(True)
        curve.setData(data_x, data_y, pen=pen)
        curve.sigClicked.connect(self.clicked)
        return curve

    def update_memories(self, data, capture=False):
        self.mem_roll = np.append(self.mem_roll,data[0])
        self.mem_pitch = np.append(self.mem_pitch, data[1])
        if not capture:
            self.mem_yaw = np.append(self.mem_yaw, data[2])
        
    def update_graph_display(self, data):
        if self.stop == False:
            if self.mem_time.size == 0:
            #if not self.mem_time:
                self.graph_range(self.pw_roll)
                self.graph_range(self.pw_pitch)
                self.graph_range(self.pw_yaw)
            self.update_memories(data, True)
            self.calibrate_yaw(data[2])
            new_time = self.mem_time_func(data[3])
            self.clear_data()
            plot_roll = self.pw_roll.plot(self.mem_time, self.mem_roll, pen='r', name='curve')
            plot_pitch = self.pw_pitch.plot(self.mem_time, self.mem_pitch, pen='g', name='curve')
            plot_yaw = self.pw_yaw.plot( self.mem_time, self.mem_yaw, pen='b', name='curve')
            if new_time > self.time_max:
                self._extracted_from_update_graph_display_9(plot_roll, plot_pitch, plot_yaw)
                self.stop = True

    def clear_data(self):
        self.pw_roll.clear()
        self.pw_pitch.clear()
        self.pw_yaw.clear()

    def _extracted_from_update_graph_display_9(self, plot_roll, plot_pitch, plot_yaw):
        self.graph_tools(self.pw_roll, plot_roll)
        self.graph_tools(self.pw_pitch, plot_pitch)
        self.graph_tools(self.pw_yaw, plot_yaw)
        

    def calibrate_yaw(self,data) -> float:
        if self.mem_yaw.size == 0:
            self.dyaw = data
            new_yaw = 0
        else:
            new_yaw = data - self.dyaw
        self.mem_yaw = np.append(self.mem_yaw, new_yaw)
        return new_yaw

    def mem_time_func(self, data) -> float:
        data = data/1000
        if self.mem_time.size == 0:
            self.dt = data
            new_time = 0
        else:
            new_time = (data - self.dt)
            last_time_plus = self.mem_time[-1] + .5
            if last_time_plus < new_time and not self.with_delay:
                diff = new_time - self.mem_time[-1]
                self.dt = self.dt + diff + .01
                new_time = (data - self.dt)
        self.mem_time = np.append(self.mem_time, new_time)
        return new_time

    def graph_axis(self, name):
        pw = pg.PlotWidget(name=name)
        pw.setBackground('w')
        pw.setYRange(-90, 90)
        pw.showGrid(x=True, y=True)
        pw.setMenuEnabled(False)
        pw.setLabel('left', name, units='degrees')
        pw.setLabel('bottom', 'Time', units='s')
        pw.setLimits(xMin=0)
        return pw

    def graph_tools(self,axis,plot):
        axis.setLimits(xMax=self.mem_time[-1])
        region = pg.LinearRegionItem()
        region.setZValue(9)
        region.setRegion([3, 5]) 
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
        return [self.mem_roll.tolist(), self.mem_pitch.tolist(), self.mem_yaw.tolist(), self.mem_time.tolist()]
    
    def not_empty_data(self):
        print(self.mem_roll)
        return len(self.mem_roll) > 0
    
    def clicked(self, plot, points):
        print(plot)
        print(points.pos())


class WidgetSOT(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.UI_Frame = Widget_basic()
        self.UI_Frame.setupUi(self)
        self.layout_center = QHBoxLayout()
        self.UI_Frame.layout_graph_principal.addLayout(self.layout_center)
        self.create_memories()
        self.load_variables()
        self.create_qframes()
        self.graph_principal()
        self.load_images()
        self.move_cond_sot(self.state_cond)

    def create_qframes(self) -> None:
        self.frame_cond1 = self.set_qframe_prop()
        self.frame_cond2 = self.set_qframe_prop()
        self.frame_cond3 = self.set_qframe_prop()
        self.frame_cond4 = self.set_qframe_prop()
        self.layout_cond_1 = self.create_qlayout_prop(self.frame_cond1)
        self.layout_cond_2 = self.create_qlayout_prop(self.frame_cond2)
        self.layout_cond_3 = self.create_qlayout_prop(self.frame_cond3)
        self.layout_cond_4 = self.create_qlayout_prop(self.frame_cond4)
        self.layout_center.addWidget(self.frame_cond1)
        self.layout_center.addWidget(self.frame_cond2)
        self.layout_center.addWidget(self.frame_cond3)
        self.layout_center.addWidget(self.frame_cond4)
    
    def set_qframe_prop(self) -> QFrame:
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        frame = QFrame(self)
        sizePolicy.setHeightForWidth(frame.sizePolicy().hasHeightForWidth())
        frame.setSizePolicy(sizePolicy)
        return frame

    def create_qlayout_prop(self, frame:QFrame) -> QVBoxLayout:
        verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, 
                                          QSizePolicy.Expanding)
        layout = QVBoxLayout(frame)
        layout.setSpacing(3)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addItem(verticalSpacer)
        return layout
        
    def load_images(self) -> None:
        self.helper_image(self.frame_cond1, self.layout_cond_1, "sot_eyeo_surf.png")
        self.helper_image(self.frame_cond2, self.layout_cond_2, "sot_eyec_surf.png")
        self.helper_image(self.frame_cond3, self.layout_cond_3, "sot_eyeo_surv.png")
        self.helper_image(self.frame_cond4, self.layout_cond_4, "sot_eyec_surv.png")
    
    def helper_image(self, frame:QFrame, layout:QHBoxLayout, name_image:str) -> None:
        lbl = QLabel(frame)
        image = QPixmap(context.get_resource(name_image))
        image = image.scaledToHeight(115)
        lbl.setPixmap(image)
        layouth = QHBoxLayout()
        verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, 
                                          QSizePolicy.Expanding)
        horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, 
                                       QSizePolicy.Minimum)
        layouth.addItem(horizontalSpacer)
        layouth.addWidget(lbl)
        layouth.addItem(horizontalSpacer)
        layout.addLayout(layouth)
        layout.addItem(verticalSpacer)
        
    def graph_principal(self) ->None:
        self.cond1 = self.graph_cond("condition1")
        self.cond2 = self.graph_cond("condition2")
        self.cond_3 = self.graph_cond("condition3")
        self.cond_4 = self.graph_cond("condition4")
        self.cond1.show()
        self.cond2.show()
        self.cond_3.show()
        self.cond_4.show()
        self.layout_cond_1.addWidget(self.cond1)
        self.layout_cond_2.addWidget(self.cond2)
        self.layout_cond_3.addWidget(self.cond_3)
        self.layout_cond_4.addWidget(self.cond_4)
        self.conditions_graph = [self.cond1, self.cond2, self.cond_3, self.cond_4]

        
    def load_variables(self) -> None:
        self.dt = 0
        self.stop = False
        self.with_delay = True
        self.state_cond = 0
        
    def create_memories(self) -> None:
        model = ([],[],[])
        mem_con = np.array(model)
        self.mem = [mem_con, mem_con, 
                    mem_con, mem_con]

    def reset_graph(self):
        self.create_memories()
        self.clear_data()
        self.dt = 0
        
    def clear_data(self):
        self.cond1.clear()
        self.cond2.clear()
        self.cond_3.clear()
        self.cond_4.clear()
        
    def draw_graph(self,data):
        OStyel = "background-color: rgba(0, 170, 255, 0);"
        self.frame_cond1.setStyleSheet(OStyel)

        mem = [np.array(data[0][0]), np.array(data[0][1]), 
               np.array(data[0][2]), np.array(data[0][3])]
        
        for i in range(len(mem)):
            self.conditions_graph[i].plot(mem[i][0], mem[i][1],pen='b', name='curve')
        
    
    def graph_cond(self, name:str) -> pg.PlotWidget:
        pw = pg.PlotWidget(name=name)
        pw.setBackground('w')
        pw.setYRange(-30, 30)
        pw.setXRange(-30,30)
        pw.showGrid(x=True, y=True)
        pw.setFixedSize(400,400)
        pw.setAspectLocked(lock=True, ratio=1)
        pw.setLabel('left', "ant-pos", units='degrees')
        pw.setLabel('bottom', 'lateral', units='degrees')
        pw.setLimits(xMin=-45, xMax=45, yMin=-45, yMax=45)
        return pw
        

    def set_time_max(self, time:int) -> None:
        self.time_max = time
        self.stop = False
    
    def move_cond_sot(self, state:int)->None:
        conditions = [self.frame_cond1, 
                     self.frame_cond2, 
                     self.frame_cond3, 
                     self.frame_cond4]
        Wstyle = "background-color: rgba(255, 170, 0, 50);"
        OStyel = "background-color: rgba(0, 170, 255, 0);"
        self.state_cond = self.state_cond + state
        if self.state_cond < 0:
            self.state_cond = 3
        if self.state_cond > 3:
            self.state_cond = 0
        for i in range(4):
            if i == self.state_cond:
                conditions[i].setStyleSheet(Wstyle)
            else:
                conditions[i].setStyleSheet(OStyel)
    
    def update_memories(self,data):
        idx_cond = self.state_cond
        time = self.mem_time_func(data[3], idx_cond)
        ant_post = data[1] * -1 
        data = np.array([[data[0]],[ant_post],[time]])
        self.mem[idx_cond] = np.append(self.mem[idx_cond], data, axis=1)
        
        
    def update_graph_display(self, data):
        if self.stop == False:
            idx_cond = self.state_cond
            self.update_memories(data)
            new_time = self.mem[idx_cond][2][-1]
            self.conditions_graph[idx_cond].clear()
            self.conditions_graph[idx_cond].plot(self.mem[idx_cond][0], 
                                           self.mem[idx_cond][1], 
                                           pen='b', name='curve')
            if new_time > self.time_max:
                self.stop = True
                coord = self.max_displacement()
                p_ellipse = pg.EllipseROI(coord[0], coord[1], pen=(3,9))
                self.conditions_graph[idx_cond].addItem(p_ellipse)
                #self.conditions_graph[idx_cond].setXRange(coord[2][0], coord[2][1])
                #self.conditions_graph[idx_cond].setYRange(coord[2][0], coord[2][1])
                self.move_cond_sot(1)

                
    def max_displacement(self) -> float:
        idx_cond = self.state_cond
        max_ant_pos = np.max(self.mem[idx_cond][1])
        max_lat = np.max(self.mem[idx_cond][0])
        min_ant_pos = np.min(self.mem[idx_cond][1])
        min_lat = np.min(self.mem[idx_cond][0])
        size_x = max_lat - min_lat
        size_y = max_ant_pos - min_ant_pos
        
        dist_lat = abs(abs(max_lat) - abs(min_lat))
        dis_ant = abs(abs(max_ant_pos) - abs(min_ant_pos))
        
        if dist_lat > dis_ant:
            very_max= [min_lat, max_lat]
        else:
            very_max = [min_ant_pos, max_ant_pos]
        return ([min_lat, min_ant_pos],[size_x, size_y], very_max)
        
    def mem_time_func(self, data:int, idx:int) -> float:
        data /= 1000
        if self.mem[idx][2].size == 0:
            self.dt = data
            new_time = 0
        else:
            new_time = (data - self.dt)
            last_time_plus = self.mem[idx][2][-1] + .5
            if last_time_plus < new_time and not self.with_delay:
                diff = new_time - self.mem[idx][2][-1]
                self.dt = self.dt + diff + .01
                new_time = (data - self.dt)
        return new_time
    
    def get_data(self) -> None:
        cond_1 = self.mem[0].tolist()
        cond_2 = self.mem[1].tolist()
        cond_3 = self.mem[2].tolist()
        cond_4 = self.mem[3].tolist()
        data = [cond_1, cond_2, cond_3, cond_4]
        return[data]
        
    def not_empty_data(self):
        only_one = self.mem[0].tolist()[0]
        return len(only_one) > 0