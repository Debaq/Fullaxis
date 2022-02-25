from PySide6.QtWidgets import (QWidget)


from lib.uiForm.compare_ui import Ui_widget
import peakutils
import numpy as np
import pyqtgraph as pg

from lib import old_exchange
from lib.ui_functions import UIFunctions as UIFunc
from lib.styles.widgets import Styles as WStyles
#import json


class WidgetCompare(QWidget):
    def __init__(self, *args, **kwargs):
        QWidget.__init__(self, *args, **kwargs)
        self.filedoc1 = None
        self.filedoc2 = None
        self.UI_vertical = Ui_widget()
        self.UI_vertical.setupUi(self)
        self.UI_vertical.btn_range.clicked.connect(self.btnToggle)
        self.UI_vertical.btn_amp.clicked.connect(self.btnToggle)
        self.UI_vertical.btn_pos.clicked.connect(self.btnToggle)
        self.UI_vertical.btn_open1.clicked.connect(lambda:self.openMethod(1))
        self.UI_vertical.btn_open2.clicked.connect(lambda:self.openMethod(2))
        self.UI_vertical.btn_clear.clicked.connect(self.clear)

        self.UI_vertical.label_File1.setText("...")
        self.UI_vertical.label_File2.setText("...")
        self.file1Full = False
        self.file2Full = False
        self.verticalLine = True
        self.range = False
        self.horizontalLine=False
        self.graphBasic()


    def openData(self, filedoc):
        self.filedoc = filedoc
        
        if self.filedoc:
            data_raw = old_exchange.dataFrame() 
            if self.filedoc.endswith('.json'):
                data_raw.read(filedoc, "json")
                data1 = data_raw.onlyColumn("roll")
                data2 = data_raw.onlyColumn("pitch")
                data3 = data_raw.onlyColumn("yaw")
                timeMilli = data_raw.onlyColumn("time")

            if self.filedoc.endswith('.csv'):
                data_raw.read(filedoc, "csv")
                data1 = data_raw.onlyColumn("A")
                data2 = data_raw.onlyColumn("B")
                data3 = data_raw.onlyColumn("C")
                timeMilli = data_raw.onlyColumn("D")


            timeSeg = self.timeSeg(timeMilli)

            data1=self.normalize(data1, timeSeg)
            data2=self.normalize(data2, timeSeg)
            data3=self.normalize(data3, timeSeg)
       
            return data1, data2, data3, timeSeg

    def normalize(self, data, timeSeg):
        y2= data + np.polyval([0.002,-0.08,5], timeSeg)
        y2=peakutils.baseline(y2)
        data = data-y2
        out = data.tolist()
        return out

    def timeSeg(self, Milli):
        time = []
        calibrateTime = Milli[0]
        for x in Milli:
            time.append((x-calibrateTime)/1000)
        return time
    
    def verticalPos(self, data, div):
        sec = min(data)/div
        posVertical = sec*(div-1)
        return posVertical

    def graphBasic(self):
        
        self.pw1 = pg.PlotWidget(name='Plot1') 
        self.pw2 = pg.PlotWidget(name='Plot2')
        self.pw3 = pg.PlotWidget(name='Plot3')  
           
        self.UI_vertical.layout_graph_1.addWidget(self.pw1)
        self.UI_vertical.layout_graph_2.addWidget(self.pw2)
        self.UI_vertical.layout_graph_3.addWidget(self.pw3)



    def graph_1(self, data1, data2, data3, time):
        self.data1 = data1
        self.data2 = data2
        self.data3 = data3
        self.time = time

        p1 = self.pw1.plot(self.time, self.data1, pen="r")
        p2 = self.pw2.plot(self.time, self.data2, pen="r")
        p3 = self.pw3.plot(self.time, self.data3, pen="r")

        self.region1 = pg.LinearRegionItem()
        self.region2 = pg.LinearRegionItem()
        self.region3 = pg.LinearRegionItem()
        self.region1.setZValue(9)
        self.region2.setZValue(9)
        self.region3.setZValue(9)            
        self.region1.setRegion([(max(self.time)-1),max(self.time)])
        self.region2.setRegion([(max(self.time)-1),max(self.time)])
        self.region3.setRegion([(max(self.time)-1),max(self.time)])
        self.pw1.addItem(self.region1, ignoreBounds=False)
        self.pw2.addItem(self.region2, ignoreBounds=False)
        self.pw3.addItem(self.region3, ignoreBounds=False)

        div = 4
        posh1Line = self.verticalPos(self.data1, div)
        posh2Line = self.verticalPos(self.data2, div)
        posh3Line = self.verticalPos(self.data3, div)
        self.v1Line = pg.InfiniteLine(angle=90, movable=True)
        self.h1Line = pg.InfiniteLine(pos=posh1Line, angle=0, movable=True)
        self.v2Line = pg.InfiniteLine(angle=90, movable=True)
        self.h2Line = pg.InfiniteLine(pos=posh2Line,angle=0, movable=True)
        self.v3Line = pg.InfiniteLine(angle=90, movable=True)
        self.h3Line = pg.InfiniteLine(pos=posh3Line, angle=0, movable=True)
        
        self.text_v1Line = pg.InfLineLabel(self.v1Line, text="", position=0.8, movable=True)
        self.text_v2Line = pg.InfLineLabel(self.v2Line, text="", position=0.8, movable=True)
        self.text_v3Line = pg.InfLineLabel(self.v3Line, text="", position=0.8, movable=True)

        self.v1Line.setZValue(10)
        self.v2Line.setZValue(10)
        self.v3Line.setZValue(10)
        self.h1Line.setZValue(10)
        self.h2Line.setZValue(10)
        self.h3Line.setZValue(10)

        self.pw1.addItem(self.v1Line, ignoreBounds=True)
        self.pw1.addItem(self.h1Line, ignoreBounds=True)
        self.pw2.addItem(self.v2Line, ignoreBounds=True)
        self.pw2.addItem(self.h2Line, ignoreBounds=True)
        self.pw3.addItem(self.v3Line, ignoreBounds=True)
        self.pw3.addItem(self.h3Line, ignoreBounds=True)

        self.region1.sigRegionChanged.connect(lambda:self.update(1))
        self.region2.sigRegionChanged.connect(lambda:self.update(2))
        self.region3.sigRegionChanged.connect(lambda:self.update(3))

        self.v1Line.sigDragged.connect(lambda:self.move_drag(1))
        self.v2Line.sigDragged.connect(lambda:self.move_drag(2))
        self.v3Line.sigDragged.connect(lambda:self.move_drag(3))
        self.h1Line.sigDragged.connect(lambda:self.move_drag(4))
        self.h2Line.sigDragged.connect(lambda:self.move_drag(5))
        self.h3Line.sigDragged.connect(lambda:self.move_drag(6))

    
    def graph_2(self, data4, data5, data6, time2):
        self.data4 = data4
        self.data5 = data5
        self.data6 = data6
        self.time2 = time2

        p4 = self.pw1.plot(self.time2, self.data4, pen="c")
        p5 = self.pw2.plot(self.time2, self.data5, pen="c")
        p6 = self.pw3.plot(self.time2, self.data6, pen="c")


    def btnToggle(self):
        if self.UI_vertical.btn_range.isChecked():
            self.range = True
        else:
            self.range = False
        if self.UI_vertical.btn_pos.isChecked():
            self.verticalLine = True
        else:
            self.verticalLine = False
        if self.UI_vertical.btn_amp.isChecked():
            self.horizontalLine=True
        else:
            self.horizontalLine=False

    def move_drag(self, Q):


        self.v1Line.setZValue(10)
        self.v2Line.setZValue(10)
        self.v3Line.setZValue(10)
        self.h1Line.setZValue(10)
        self.h2Line.setZValue(10)
        self.h3Line.setZValue(10)

        if Q == 1:
            if self.verticalLine:
                pos = self.v1Line.value()
                self.v2Line.setPos(pos)
                self.v3Line.setPos(pos)
                pos_text = str(round(pos,3))
                self.text_v1Line.setText(pos_text)
                self.text_v2Line.setText(pos_text)
                self.text_v3Line.setText(pos_text)
            else:
                pos = self.v1Line.value()
                pos_text = str(round(pos,4))
                self.text_v1Line.setText(pos_text)

        if Q == 2:
            if self.verticalLine:
                pos = self.v2Line.value()
                self.v1Line.setPos(pos)
                self.v3Line.setPos(pos)
                pos_text = str(round(pos,4))
                self.text_v1Line.setText(pos_text)
                self.text_v2Line.setText(pos_text)
                self.text_v3Line.setText(pos_text)
            else:
                pos = self.v2Line.value()
                pos_text = str(round(pos,4))
                self.text_v2Line.setText(pos_text)

        if Q == 3:
            if self.verticalLine:
                pos = self.v3Line.value()
                self.v1Line.setPos(pos)
                self.v2Line.setPos(pos)
                pos_text = str(round(pos,4))
                self.text_v1Line.setText(pos_text)
                self.text_v2Line.setText(pos_text)
                self.text_v3Line.setText(pos_text)
            else:
                pos = self.v3Line.value()
                pos_text = str(round(pos,4))
                self.text_v3Line.setText(pos_text)

        if Q == 4:
            pos = self.h1Line.value()
            if self.horizontalLine:
                self.h2Line.setPos(pos)
                self.h3Line.setPos(pos)
            self.UI_vertical.ampPoint_1.setText("%0.2f" % (pos))
        if Q == 5:
            pos = self.h2Line.value()
            if self.horizontalLine:
                self.h1Line.setPos(pos)
                self.h3Line.setPos(pos)
            self.UI_vertical.ampPoint_2.setText("%0.2f" % (pos))
        if Q == 6:
            pos = self.h3Line.value()
            if self.horizontalLine:
                self.h1Line.setPos(pos)
                self.h2Line.setPos(pos)
            self.UI_vertical.ampPoint_3.setText("%0.2f" % (pos))

    def update(self, Q):

        self.region1.setZValue(9)
        self.region2.setZValue(9)
        self.region3.setZValue(9)
        minX_reg1, maxX_reg1 = self.region1.getRegion()
        minX_reg2, maxX_reg2 = self.region2.getRegion()
        minX_reg3, maxX_reg3 = self.region3.getRegion()

        if self.range:
            if Q == 1:
                self.region2.setRegion([minX_reg1,maxX_reg1])
                self.region3.setRegion([minX_reg1,maxX_reg1])
            if Q == 2:
                self.region1.setRegion([minX_reg2,maxX_reg2])
                self.region3.setRegion([minX_reg2,maxX_reg2])
            if Q == 3:
                self.region1.setRegion([minX_reg3,maxX_reg3])
                self.region2.setRegion([minX_reg3,maxX_reg3])


        ampRange_1 = self.closest(self.time, self.data1, maxX_reg1, minX_reg1)
        ampRange_2 = self.closest(self.time, self.data2, maxX_reg2, minX_reg2)
        ampRange_3 = self.closest(self.time, self.data3, maxX_reg3, minX_reg3)
                
        tdelta_reg1 = maxX_reg1-minX_reg1
        tdelta_reg2 = maxX_reg2-minX_reg2
        tdelta_reg3 = maxX_reg3-minX_reg3

        if minX_reg1 > 0 and maxX_reg1 < self.time[-1]:
            self.UI_vertical.lbl_tiempo_1.setText("%0.2f"% (tdelta_reg1))
            self.UI_vertical.lbl_minRoll.setText("%0.2f"% (minX_reg1))
            self.UI_vertical.lbl_maxRoll.setText("%0.2f"% (maxX_reg1))
            self.UI_vertical.ampRange_1.setText("%0.2f"% (ampRange_1))

        if minX_reg2 > 0 and maxX_reg2 < self.time[-1]:
            self.UI_vertical.lbl_tiempo_2.setText("%0.2f"% (tdelta_reg1))
            self.UI_vertical.lbl_minPitch.setText("%0.2f"% (minX_reg2))
            self.UI_vertical.lbl_maxPitch.setText("%0.2f"% (maxX_reg2))
            self.UI_vertical.ampRange_2.setText("%0.2f"% (ampRange_2))



        if minX_reg3 > 0 and maxX_reg3 < self.time[-1]:
            self.UI_vertical.lbl_tiempo_3.setText("%0.2f"% (tdelta_reg3))
            self.UI_vertical.lbl_minYaw.setText("%0.2f"% (minX_reg3))
            self.UI_vertical.lbl_maxYaw.setText("%0.2f"% (maxX_reg3))
            self.UI_vertical.ampRange_3.setText("%0.2f"% (ampRange_3))

    def closest(self, lstin, lstout, maxX, minX): 
        array = np.asarray(lstin)
        index_0 = (np.abs(array - minX)).argmin()
        index_1 = (np.abs(array - maxX)).argmin()
        data_0 = lstout[index_0]
        data_1 = lstout[index_1]
        Amp = abs(data_1-data_0)        
        return Amp
      


    def openMethod(self, ind):
        path = UIFunc.openFile(self)
        if ind == 1:
            data1, data2, data3, timeSeg = self.openData(path[0])
            self.UI_vertical.label_File1.setText(path[0])
            self.UI_vertical.btn_open1.setEnabled(False)
            self.UI_vertical.btn_open1.setStyleSheet(WStyles.btn_disabled)
            self.graph_1(data1, data2, data3, timeSeg)
            
        
        if ind == 2:
            data1, data2, data3, timeSeg = self.openData(path[0])
            self.UI_vertical.label_File2.setText(path[0])
            self.UI_vertical.btn_open2.setEnabled(False)
            self.UI_vertical.btn_open2.setStyleSheet(WStyles.btn_disabled)
            self.graph_2(data1, data2, data3, timeSeg)
        



    def clear (self):
        self.UI_vertical.btn_open1.setEnabled(True)
        self.UI_vertical.btn_open1.setStyleSheet(WStyles.btn_enabled)
        self.UI_vertical.btn_open2.setEnabled(True)
        self.UI_vertical.btn_open2.setStyleSheet(WStyles.btn_enabled)
        self.UI_vertical.label_File1.setText("...")
        self.UI_vertical.label_File2.setText("...")
        self.pw1.plot(clear=True)
        self.pw2.plot(clear=True)
        self.pw3.plot(clear=True)