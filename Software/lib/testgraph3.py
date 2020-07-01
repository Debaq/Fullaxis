import numpy as np
import pyqtgraph as pg
from pyqtgraph.Qt import QtGui, QtCore
from pyqtgraph.Point import Point
import old_exchange as old_csv


#generate layout
app = QtGui.QApplication([])
win = pg.GraphicsLayoutWidget(show=True)
win.setWindowTitle('pyqtgraph example: crosshair')
label = pg.LabelItem(justify='right')
win.addItem(label)



p1 = win.addPlot(row=1, col=0)
p2 = win.addPlot(row=2, col=0)
p3 = win.addPlot(row=3, col=0)


region = pg.LinearRegionItem()
region.setZValue(10)
# Add the LinearRegionItem to the ViewBox, but tell the ViewBox to exclude this 
# item when doing auto-range calculations.
#p2.addItem(region, ignoreBounds=True)

p3.addItem(region, ignoreBounds=True)

#pg.dbg()
p1.setAutoVisible(y=True)


#create numpy arrays
data_raw = old_csv.dataFrame()
data_raw.r_csv("test.csv")

#make the numbers large to show that the xrange shows data from 10000 to all the way 0
data1 = data_raw.onlyColumn("A")
data2 = data_raw.onlyColumn("B")
data3 = data_raw.onlyColumn("C")

timeMilli = data_raw.onlyColumn("D")
time = []
calibrateTime = timeMilli[0]
for x in timeMilli:
    time.append((x-calibrateTime)/1000)


p1.plot(time, data1, pen="r")
p2.plot(time, data2, pen="g")
p3.plot(time, data3, pen="w")

def update():
    region.setZValue(10)
    minX, maxX = region.getRegion()
    print("min: ", minX, " max: ", maxX)

    p1.setXRange(minX, maxX, padding=0)    

region.sigRegionChanged.connect(update)

def updateRegion(window, viewRange):
    rgn = viewRange[0]
    region.setRegion(rgn)

p1.sigRangeChanged.connect(updateRegion)

region.setRegion([0, time[-1]])

#cross hair
v1Line = pg.InfiniteLine(angle=90, movable=True)
h1Line = pg.InfiniteLine(angle=0, movable=True)
v2Line = pg.InfiniteLine(angle=90, movable=False)
h2Line = pg.InfiniteLine(angle=0, movable=False)
v3Line = pg.InfiniteLine(angle=90, movable=True)
h3Line = pg.InfiniteLine(angle=0, movable=True)

p1.addItem(v1Line, ignoreBounds=True)
p1.addItem(h1Line, ignoreBounds=True)
p2.addItem(v2Line, ignoreBounds=True)
p2.addItem(h2Line, ignoreBounds=True)
p3.addItem(v3Line, ignoreBounds=True)
p3.addItem(h3Line, ignoreBounds=True)

vb = p1.vb

def mouseMoved(evt):
    pos = evt[0]  ## using signal proxy turns original arguments into a tuple
    if p1.sceneBoundingRect().contains(pos):
        mousePoint = vb.mapSceneToView(pos)
        index = int(mousePoint.x())
        if index > 0 and index < len(data1):
            label.setText("<span style='font-size: 12pt'>x=%0.1f,   <span style='color: red'>y1=%0.1f</span>,   <span style='color: green'>y2=%0.1f</span>" % (mousePoint.x(), data1[index], data2[index]))
        v1Line.setPos(mousePoint.x())
        h1Line.setPos(mousePoint.y())
        #v2Line.setPos(mousePoint.x())
        #h2Line.setPos(mousePoint.y())
       #v3Line.setPos(mousePoint.x())
        #h3Line.setPos(mousePoint.y())        



proxy = pg.SignalProxy(p1.scene().sigMouseMoved, rateLimit=60, slot=mouseMoved)
#p1.scene().sigMouseMoved.connect(mouseMoved)


## Start Qt event loop unless running in interactive mode or using pyside.
if __name__ == '__main__':
    import sys
    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        QtGui.QApplication.instance().exec_()
