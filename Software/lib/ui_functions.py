from lib import basic_functions as basic
from datetime import datetime
import json
from lib import PATH_NAME as PATH
import os
## ==> ESTILOS
from lib.styles.widgets import Styles as WStyles
from lib.styles.Frames import Styles as FStyles
from PyQt5.QtWidgets import QWidget, QDialog, QLabel, QPushButton, QMenu, QSizePolicy, QSpacerItem, QFileDialog
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import Qt, QAbstractTableModel


class UIFunctions():

    def Error(self, text):
        Error_type = text.split(':')
        
        if Error_type[0] == 'CLEAR':
            Error_simbol = ''
            text = ''
        if Error_type[0] == 'E':
            Error_simbol = '<span style=" font-size:10pt;">Ⓧ </span>'
        if Error_type[0] == 'A':
            Error_simbol = '<span style=" font-size:10pt;">‼ </span>'
            
        print(Error_simbol+text)

    def labelUserName(self, text):
        self.ui.lbl_user_title.setText(text)

    def resetLayout(self, layout):
        for i in reversed(range(layout.count())): 
            widgetToRemove = layout.itemAt(i).widget()
            # remove it from the layout list
            layout.removeWidget(widgetToRemove)
            # remove it from the gui
            widgetToRemove.setParent(None)      
            
    def loginLockNew(self, name, Passw):
        now = datetime.now()
        timestamp = datetime.timestamp(now)
        data = {"name":name, "pass":Passw, "timestamp": timestamp}
        with open(PATH.LOGINLOCK, 'w+') as outfile:
            json.dump(data, outfile)

    def loginLockRead(self):
        now = datetime.now()
        timestampnow = datetime.timestamp(now)
        with open(PATH.LOGINLOCK) as json_file:
            data = json.load(json_file)
        name = data['name']
        passw = data['pass']
        timestampold = data['timestamp']
        timestamp = timestampnow - timestampold
        return data
    
    def logout(self):
        try:
            os.remove(PATH.LOGINLOCK)
        except:
            pass
    
    def ButtonText(self, text):
        button = QPushButton(text)
        button.setStyleSheet(WStyles.btn_text)
        return button
        
    def ButtonFlat(self, text):
        button = QPushButton(text)
        button.setStyleSheet(WStyles.btn_flat)
        button.setMinimumHeight(30)
        sizePolicy3 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(button.sizePolicy().hasHeightForWidth())
        button.setSizePolicy(sizePolicy3)
        return button

    def createBtnMenuLat(self, objName, text, ico=None, tooltip=None):
        text_replace = text.replace(" ", "\n")
        button = QPushButton(text_replace)
        button.setObjectName(objName)
        button.setLayoutDirection(Qt.RightToLeft)
        button.setStyleSheet(WStyles.btn_lateral)
        icon = QIcon()
        icon_path = (":/icons_white/icons/png/16x16/cil-"+ico+".png")
        icon.addPixmap(QPixmap(icon_path), QIcon.Normal, QIcon.Off)
        if tooltip != None:
            button.setToolTip(tooltip)
        button.setIcon(icon)
        button.setMinimumSize(0,60)
        button.setFlat(True)
        button.clicked.connect(self.Button)
        self.LateralMenu.UI_LateralMenu.layerBack_frame.addWidget(button)
        return button
               
    def spacer(self, direction = "H"):
        if direction == "V":
            spacerItem = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        if direction == "H":
            spacerItem = QSpacerItem(20, 40, QSizePolicy.Expanding, QSizePolicy.Minimum)
        return spacerItem
    
    def printer(text):
        print(text)
              
    def selectMenu(getStyle):
        select = getStyle + (WStyles.btn_lateralActive)
        return select
    
    ## ==> DESELECT
    def deselectMenu(getStyle):
        print("estoy aca")
        deselect = getStyle.replace(WStyles.btn_lateralActive, "")
        return deselect
    
    def resetStyle(self, widget):
        for w in self.LateralMenu.findChildren(QPushButton):
            if w.objectName() != widget:
                w.setStyleSheet(UIFunctions.deselectMenu(w.styleSheet()))

    def openFile(self):
        path = QFileDialog.getOpenFileName(self, None, 'Open CSV',  'CSV(*.csv)')
        print(path)


 
 
class TableModel(QAbstractTableModel):
    def __init__(self, data):
        super(TableModel, self).__init__()
        self._data = data

    def data(self, index, role):
        if role == Qt.DisplayRole:
            # See below for the nested-list data structure.
            # .row() indexes into the outer list,
            # .column() indexes into the sub-list
            return self._data[index.row()][index.column()]

    def rowCount(self, index):
        # The length of the outer list.
        return len(self._data)

    def columnCount(self, index):
        # The following takes the first sub-list, and returns
        # the length (only works if all rows are an equal length)
        return len(self._data[0])
