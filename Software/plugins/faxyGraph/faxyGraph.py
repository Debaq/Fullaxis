from PyQt5.QtWidgets import (QApplication, QDialog, QLabel, QMainWindow, QMenu,
                             QStyleFactory, QTableView, QVBoxLayout, QWidget, 
                             QVBoxLayout, QHBoxLayout)

from PyQt5.QtGui import QIcon, QTableWidgetItem
from PyQt5 import QtCore


from lib.uiForm.graph_ui import Ui_widget
import peakutils
import numpy as np
import pyqtgraph as pg

from lib import old_exchange
import lib.old_exchange as old_csv
from lib.ui_functions import UIFunctions as UIFunc
import ezodf
from lib.styles.widgets import Styles as WStyles

class WidgetGraph(QWidget):
    def __init__(self, filedoc=None, *args, **kwargs):
        QWidget.__init__(self, *args, **kwargs)
        self.UI_vertical = Ui_widget()
        self.UI_vertical.setupUi(self)
        self.UI_vertical.btn_insert.clicked.connect(self.addRowTable)
        self.UI_vertical.btn_copyThis.clicked.connect(self.copyLine)
        self.UI_vertical.btn_clear.clicked.connect(self.clearTable)
        self.UI_vertical.btn_copyAll.clicked.connect(self.copyAll)
        self.UI_vertical.btn_range.clicked.connect(self.btnToggle)
        self.UI_vertical.btn_amp.clicked.connect(self.btnToggle)
        self.UI_vertical.btn_pos.clicked.connect(self.btnToggle)
        self.UI_vertical.btn_ods.clicked.connect(self.btnOds)
        self.UI_vertical.btn_savearea.clicked.connect(self.saveArea)
        self.UI_vertical.btn_savearea.setStyleSheet(WStyles.btn_disabled)


        self.verticalLine = True
        self.range = False
        self.horizontalLine=False
        self.clip = QApplication.clipboard()

        if filedoc:
            data_raw = old_exchange.dataFrame() 
            if filedoc.endswith('.json'):
                data_raw.read(filedoc, "json")
                self.data1 = data_raw.onlyColumn("roll")
                self.data2 = data_raw.onlyColumn("pitch")
                self.data3 = data_raw.onlyColumn("yaw")
                self.timeMilli = data_raw.onlyColumn("time")

            if filedoc.endswith('.csv'):
                data_raw.read(filedoc, "csv")
                self.data1 = data_raw.onlyColumn("A")
                self.data2 = data_raw.onlyColumn("B")
                self.data3 = data_raw.onlyColumn("C")

                self.timeMilli = data_raw.onlyColumn("D")

            self.data1=self.normalize(self.data1)
            self.data2=self.normalize(self.data2)
            #self.data3=self.normalize(self.data3)


            self.time()
            y2= self.data3 + np.polyval([0.002,-0.08,5], self.time)
            y2=peakutils.baseline(y2)
            self.data3 = self.data3-y2
            self.graph()

    def normalize(self, data):
        prom = np.mean([max(data),min(data)])
        out = []
        for x in data:
            inY = x
            if prom < 0:
                inY = inY+prom
            else:
                inY = inY-prom
            out.append(inY)
        return out

    def time(self):
        self.time = []
        calibrateTime = self.timeMilli[0]
        for x in self.timeMilli:
            self.time.append((x-calibrateTime)/1000)
    
    def verticalPos(self, data, div):
        sec = min(data)/div
        posVertical = sec*(div-1)
        return posVertical

    def graph(self):
        self.region1 = pg.LinearRegionItem()
        self.region2 = pg.LinearRegionItem()
        self.region3 = pg.LinearRegionItem()
        self.region1.setZValue(9)
        self.region2.setZValue(9)
        self.region3.setZValue(9)            
        self.region1.setRegion([(max(self.time)-1),max(self.time)])
        self.region2.setRegion([(max(self.time)-1),max(self.time)])
        self.region3.setRegion([(max(self.time)-1),max(self.time)])
                    
        pw1 = pg.PlotWidget(name='Plot1') 
        pw2 = pg.PlotWidget(name='Plot2')
        pw3 = pg.PlotWidget(name='Plot3')  

        pw1.addItem(self.region1, ignoreBounds=False)
        pw2.addItem(self.region2, ignoreBounds=False)
        pw3.addItem(self.region3, ignoreBounds=False)

        self.UI_vertical.layout_graph_1.addWidget(pw1)
        self.UI_vertical.layout_graph_2.addWidget(pw2)
        self.UI_vertical.layout_graph_3.addWidget(pw3)

        p1 = pw1.plot(self.time, self.data1, pen="c")
        p2 = pw2.plot(self.time, self.data2, pen="g")
        p3 = pw3.plot(self.time, self.data3, pen="r")

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

        self.v1Line.setZValue(10)
        self.v2Line.setZValue(10)
        self.v3Line.setZValue(10)
        self.h1Line.setZValue(10)
        self.h2Line.setZValue(10)
        self.h3Line.setZValue(10)

        pw1.addItem(self.v1Line, ignoreBounds=True)
        pw1.addItem(self.h1Line, ignoreBounds=True)
        pw2.addItem(self.v2Line, ignoreBounds=True)
        pw2.addItem(self.h2Line, ignoreBounds=True)
        pw3.addItem(self.v3Line, ignoreBounds=True)
        pw3.addItem(self.h3Line, ignoreBounds=True)

        self.region1.sigRegionChanged.connect(lambda:self.update(1))
        self.region2.sigRegionChanged.connect(lambda:self.update(2))
        self.region3.sigRegionChanged.connect(lambda:self.update(3))

        self.v1Line.sigDragged.connect(lambda:self.move_drag(1))
        self.v2Line.sigDragged.connect(lambda:self.move_drag(2))
        self.v3Line.sigDragged.connect(lambda:self.move_drag(3))
        self.h1Line.sigDragged.connect(lambda:self.move_drag(4))
        self.h2Line.sigDragged.connect(lambda:self.move_drag(5))
        self.h3Line.sigDragged.connect(lambda:self.move_drag(6))

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
        if Q == 2:
            if self.verticalLine:
                pos = self.v2Line.value()
                self.v1Line.setPos(pos)
                self.v3Line.setPos(pos)
        if Q == 3:
            if self.verticalLine:
                pos = self.v3Line.value()
                self.v1Line.setPos(pos)
                self.v2Line.setPos(pos)
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
            
            self.UI_vertical.btn_savearea.setEnabled(True)
            self.UI_vertical.btn_savearea.setStyleSheet(WStyles.btn_enabled)
            if Q == 1:
                self.region2.setRegion([minX_reg1,maxX_reg1])
                self.region3.setRegion([minX_reg1,maxX_reg1])
            if Q == 2:
                self.region1.setRegion([minX_reg2,maxX_reg2])
                self.region3.setRegion([minX_reg2,maxX_reg2])
            if Q == 3:
                self.region1.setRegion([minX_reg3,maxX_reg3])
                self.region2.setRegion([minX_reg3,maxX_reg3])
        else:
            self.UI_vertical.btn_savearea.setEnabled(False)
            self.UI_vertical.btn_savearea.setStyleSheet(WStyles.btn_disabled)

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

    def addRowTable(self):
        data = [self.UI_vertical.ampPoint_1.text(),
                self.UI_vertical.ampRange_1.text(),
                self.UI_vertical.lbl_tiempo_1.text(),
                self.UI_vertical.lbl_minRoll.text(),
                self.UI_vertical.lbl_maxRoll.text(),
                self.UI_vertical.ampPoint_2.text(),
                self.UI_vertical.ampRange_2.text(),
                self.UI_vertical.lbl_tiempo_2.text(),
                self.UI_vertical.lbl_minPitch.text(),
                self.UI_vertical.lbl_maxPitch.text(),
                self.UI_vertical.ampPoint_3.text(),
                self.UI_vertical.ampRange_3.text(),
                self.UI_vertical.lbl_tiempo_3.text(),
                self.UI_vertical.lbl_minYaw.text(),
                self.UI_vertical.lbl_maxYaw.text()]

        rowPosition = self.UI_vertical.tableWidget.rowCount()
        self.UI_vertical.tableWidget.insertRow(rowPosition)
        for x in range(len(data)):
            self.UI_vertical.tableWidget.setItem(rowPosition , x, QTableWidgetItem(data[x]))

    def copyLine(self):

            selectedIndexes = self.UI_vertical.tableWidget.selectedIndexes()
            out = []
            
            for x in range(len(selectedIndexes)):
                data = selectedIndexes[x].data(QtCore.Qt.DisplayRole)
                out.append(data)
            
            stringData = str(out).replace('[','')
            stringData = stringData.replace(']','')
            stringData = stringData.replace('\'','')
            
            self.clip.setText(stringData)

    def clearTable(self):
        rowTotal = self.UI_vertical.tableWidget.rowCount()
        for x in range(rowTotal):
            self.UI_vertical.tableWidget.removeRow(x)
        rowTotal = self.UI_vertical.tableWidget.rowCount()
        if rowTotal > 0:
            self.clearTable()

    def copyAll(self):
            rowPosition = self.UI_vertical.tableWidget.rowCount()
            self.UI_vertical.tableWidget.setSelectionBehavior(QTableView.SelectRows)
            self.UI_vertical.tableWidget.setSelectionMode(QTableView.SingleSelection)
            string= ""
            for x in range(rowPosition):
                self.UI_vertical.tableWidget.selectRow(x)
                selectedIndexes = self.UI_vertical.tableWidget.selectedIndexes()
                out = []
                for x in range(len(selectedIndexes)):
                    data = selectedIndexes[x].data(QtCore.Qt.DisplayRole)
                    out.append(data)
                string = string + str(out) + '\n'

            stringData = string.replace('[','')
            stringData = stringData.replace(']','')
            stringData = stringData.replace('\'','')
            stringData = stringData.replace('\n,','\n')

            self.clip.setText(stringData)

    def btnOds(self):

        rowPosition = self.UI_vertical.tableWidget.rowCount()
        self.UI_vertical.tableWidget.setSelectionBehavior(QTableView.SelectRows)
        self.UI_vertical.tableWidget.setSelectionMode(QTableView.SingleSelection)
        colrow = [["aRoll(punto)", "aRoll(segm)","Roll-delta(segm)","tRoll(segm A)", 
                   "tRoll(segm B)", "aPitch(punto)", "aPitch(segm)","Pitch-delta(segm)",
                   "tPitch(segm A)", "tPitch(segm B)", "aYaw(punto)", "aYaw(segm)",
                   "Yaw-delta(segm)","tYaw(segm A)", "tYaw(segm B)" ]]
        for x in range(rowPosition):
            self.UI_vertical.tableWidget.selectRow(x)
            selectedIndexes = self.UI_vertical.tableWidget.selectedIndexes()
            out = []
            for x in range(len(selectedIndexes)):
                data = selectedIndexes[x].data(QtCore.Qt.DisplayRole)
                out.append(data)
            colrow.append(out)
        NROWS = len(colrow)
        try:
            NCOLS = len(colrow[1])
            save = self.saveMethod()
            if save[0] != '':
                name = save[0]+'.ods'
                ods = ezodf.newdoc('ods', name)
                sheet = ezodf.Sheet('Muestra', size=(NROWS, NCOLS))
                ods.sheets += sheet

                for row in range(NROWS):
                    for col in range(NCOLS):
                        content = colrow[row][col]
                        print(content)
                        sheet[row, col].set_value(content)

                ods.save()
        except:
            pass

    def saveMethod(self):
        path = UIFunc.saveFile(self)
        return path

    def saveArea(self):
        print("okidoki")