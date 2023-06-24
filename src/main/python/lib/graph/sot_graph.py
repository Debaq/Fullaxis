import numpy as np
import pyqtgraph as pg
from base import context
from lib.graph.basic_graph import Widget_basic
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import (QFrame, QHBoxLayout, QLabel, QSizePolicy,
                               QSpacerItem, QVBoxLayout, QWidget)


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
        self.helper_image(self.frame_cond1, self.layout_cond_1, "img/sot_eyeo_surf.png")
        self.helper_image(self.frame_cond2, self.layout_cond_2, "img/sot_eyec_surf.png")
        self.helper_image(self.frame_cond3, self.layout_cond_3, "img/sot_eyeo_surv.png")
        self.helper_image(self.frame_cond4, self.layout_cond_4, "img/sot_eyec_surv.png")
    
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
        #self.cond1.show()
        #self.cond2.show()
        #self.cond_3.show()
        #self.cond_4.show()
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