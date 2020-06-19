## ==> GUI FILE
from Fullaxis import *
from lib.uiForm.ui_home import Ui_HomeWidget
from lib.uiForm.ui_other import Ui_OtherWidget

from lib import basic_functions as basic

from PySide2 import QtCore, QtGui, QtUiTools, QtWidgets


class UIFunctions(MainWindow):
    
    def __init__(self):
        self.Printer()
      
    def toggleFrameOption_L5(self, WidthContract, enable):
        if enable:
            # GET WIDTH
            width = self.ui.FrameOption_L5.width()
            
            minExtend = WidthContract
            standard = 200

            # SET MAX WIDTH
            if width == 200:
                widthExtended = minExtend
                self.ui.lbl_Explorer.setVisible(False)
                self.ui.layoutTitleExplorer_L6.setContentsMargins(0,0,0,0)
                self.ui.btn_ContractExplorer.setText(">")
            else:
                widthExtended = standard
                self.ui.lbl_Explorer.setVisible(True)
                self.ui.layoutTitleExplorer_L6.setContentsMargins(5,0,0,0)
                self.ui.btn_ContractExplorer.setText("<")

            # ANIMATION
            self.animation = QPropertyAnimation(self.ui.FrameOption_L5, b"maximumWidth")
            self.animation.setDuration(300)
            self.animation.setStartValue(width)
            self.animation.setEndValue(widthExtended)
            self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
            self.animation.start()
            

    
    def Error(self, text):
        Error_type = text.split(':')
        
        if Error_type[0] == 'CLEAR':
            Error_simbol = ''
            text = ''
        if Error_type[0] == 'E':
            Error_simbol = '<span style=" font-size:10pt;">Ⓧ </span>'
        if Error_type[0] == 'A':
            Error_simbol = '<span style=" font-size:10pt;">‼ </span>'
            
        self.ui.labelMenuLeftInfo.setText(Error_simbol+text)

    def labelUserName(self, text):
        self.ui.lbl_user_title.setText(text)




    def resetLayout(self, layout):
        for i in reversed(range(layout.count())): 
            widgetToRemove = layout.itemAt(i).widget()
            # remove it from the layout list
            layout.removeWidget(widgetToRemove)
            # remove it from the gui
            widgetToRemove.setParent(None)            
