from lib import basic_functions as basic
from datetime import datetime
import json
from lib import PATH_NAME as PATH
import os
## ==> ESTILOS
from lib.styles.widgets import Styles as WStyles
from lib.styles.Frames import Styles as FStyles
from PyQt5.QtWidgets import QWidget, QDialog, QLabel, QPushButton, QMenu


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
            print(widgetToRemove)
            layout.removeWidget(widgetToRemove)
            # remove it from the gui
            widgetToRemove.setParent(None)      
            
    def loginLockNew(self, name, Passw):
        now = datetime.now()
        timestamp = datetime.timestamp(now)
        data = {"name":name, "pass":Passw, "timestamp": timestamp}
        with open(PATH.LOGINLOCK, 'w+') as outfile:
            json.dump(data, outfile)

    def loginLockRead():
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
        return button
        