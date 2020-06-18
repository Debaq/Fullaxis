# -*- coding: utf-8 -*-

import json
import os

def read_setting(file):
    path = 'resource/setting/'+file
    return(read_json(path))
    
    
def read_json(path):
    try:
        with open(path) as json_file:
            data = json.load(json_file)
        return data
    except:
        pass
    

def Printer(text):
    print(text)