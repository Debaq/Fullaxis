# -*- coding: utf-8 -*-

from PyQt5 import QtGui, QtCore
import numpy as np
import pyqtgraph as pg
import old_exchange as old_csv

#QtGui.QApplication.setGraphicsSystem('raster')
app = QtGui.QApplication([])
mw = QtGui.QMainWindow()
mw.setWindowTitle('pyqtgraph example: PlotWidget')
mw.resize(800,800)

cw = QtGui.QWidget()
mw.setCentralWidget(cw)

root = QtGui.QHBoxLayout(cw)
v1 = QtGui.QVBoxLayout()
v2 = QtGui.QVBoxLayout()
root.addLayout(v1)
root.addLayout(v2)
#cw.setLayout(root)

pw = pg.PlotWidget(name='Plot1')  ## giving the plots names allows us to link their axes together
pw.setMenuEnabled(False)
pw2 = pg.PlotWidget(name='Plot2')
pw2.setMenuEnabled(False)

pw3 = pg.PlotWidget(name='Plot3')  ## giving the plots names allows us to link their axes together
pw3.setMenuEnabled(False)
pw4 = pg.PlotWidget(name='Plot4')
pw4.setMenuEnabled(False)

v1.addWidget(pw)
v1.addWidget(pw2)
v2.addWidget(pw3)
v2.addWidget(pw4)

mw.show()

## Create an empty plot curve to be filled later, set its pen

data_raw = old_csv.dataFrame()
data_raw.r_csv("test.csv")


data1 = data_raw.onlyColumn("A")
data2 = data_raw.onlyColumn("B")
data3 = data_raw.onlyColumn("C")
data4 = data_raw.onlyColumn("D")
p1 = pw.plot(data1, pen="r")
p2 = pw2.plot(data2, pen="g")
p3 = pw3.plot(data3, pen="r")
p4 = pw4.plot(data4, pen="g")


## Start Qt event loop unless running in interactive mode or using pyside.
if __name__ == '__main__':
    import sys
    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        QtGui.QApplication.instance().exec_()
