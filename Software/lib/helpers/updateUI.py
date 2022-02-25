# -*- coding: utf-8 -*-

import os, sys
import string
from os import path
from PySide6 import uic
import time
#from PySide6 import pyrcc_main

class updateUI():
    def __init__(self, source):
        super().__init__()

        if source == 0:
            print("esperando actualización de rc y uic")
            self.update_rc()
            self.update_uic()
        
        if source == 1:
            print("esperando actualización de uic")
            self.update_uic()
            
        if source == 2:
            print("esperando actualización de rc")
            self.update_rc()

       
    
    def update_rc(self):
        os.popen('pyrcc5 development/resource/resource.qrc -o resource/resource_rc.py')
        time.sleep(10)

    def update_uic(self):
        path_ui = 'development/Form/'
        path_uiForm = 'lib/uiForm/'
        path_search_ui = os.listdir(path_ui)
        string_search = "import resource_rc"
        String_new = "from resource import resource_rc"

        for Ui in path_search_ui:
            if os.path.isfile(os.path.join(path_ui, Ui)) and Ui.endswith('.ui'):
                extPY = Ui
                newName= extPY.replace(".ui", "_ui.py")
                fileUiOrigin  = path_ui+Ui
                filePy = path_uiForm+newName
                filePyOuput   = open(filePy,"w")
                fileTempOuput = path_uiForm+newName+".temp"
                uic.compileUi(fileUiOrigin, filePyOuput, from_imports = False)
                filePyOuput.close()
                file_input   = open(filePy,"r")
                file_ouput = open(fileTempOuput,'w')
                file_read = file_input.readlines()
                file_input.close()
                for line in file_read:
                    if String_new in line:
                        break
                    if string_search in line:
                        file_ouput.write(line.replace(string_search, String_new))
                    else:
                        file_ouput.write(line)
                        create = True
                file_ouput.close()
                if create:                    
                    os.popen('rm '+filePy)
                    os.popen('mv '+fileTempOuput+' '+filePy)
                    create = False
                else:
                    os.popen('rm '+fileTempOuput) 
            time.sleep(1)
       

