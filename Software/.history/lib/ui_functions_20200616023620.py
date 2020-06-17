## ==> GUI FILE
from Fullaxis import *
from lib.uiForm.ui_home import Ui_HomeWidget
from lib.uiForm.ui_other import Ui_OtherWidget

class UIFunctions(MainWindow):
    
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
            
            
        
    def Open_home(self):
        widgetHome = Ui_HomeWidget()
        widgetHome.setupUi(self.ui.FrameCenter_L5)
        
    def Open_user(self):
        widgetHome = Ui_HomeWidget()
        widgetHome.setupUi(self.ui.FrameCenter_L5)
    
    def labelMenuLeftInfo(self, text):
        self.ui.labelMenuLeftInfo.setText(text)