# -*- coding: utf-8 -*-

import os, sys
import string

os.popen('pyrcc5 development/resource/resource.qrc -o resource/resource_rc.py')


path_ui = 'development/Form/'
path_uiForm = 'lib/uiForm/'


#for Ui in path_ui:
#    if os.path.isfile(os.path.join(path_uiForm, Py)) and Py.endswith('.ui'):
#        os.popen()
        



path_search = os.listdir(path_uiForm)
uiPy = []
string_search = "import resource_rc"
String_new = "from resource import resource_rc"

for Py in path_search:
    if os.path.isfile(os.path.join(path_uiForm, Py)) and Py.endswith('.py'):
        uiPy.append(Py)
    
create = False

for Py in uiPy:
    if Py != '__init__.py':
        file_input = open(path_uiForm+Py, 'r')
        file_ouput = open(path_uiForm+Py+'.temp','w')
        file_input_read = file_input.readlines()
        file_input.close()
        for line in file_input_read:
            if String_new in line:
                create = False
                break
            if string_search in line:
                file_ouput.write(line.replace(string_search, String_new))
            else:
                file_ouput.write(line)
                create = True
        file_ouput.close()
        if create:                    
            os.popen('rm '+path_uiForm+Py)
            os.popen('mv '+path_uiForm+Py+'.temp '+path_uiForm+Py)
            create = False
        else:
            os.popen('rm '+path_uiForm+Py+'.temp')