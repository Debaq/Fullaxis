import datetime
from pathlib import Path
from tinydb import Query, TinyDB
from base import context

database_path = Path(context.get_resource('config.json'))

class Preferences():
    def __init__(self) -> None:
        self.data_base = TinyDB(database_path)
    
    def set_data(self, **kwargs:any) -> None:
        name_table = "preferences"
        table = self.data_base.table(name_table)
        table.insert(kwargs)
    
    def get_data_all(self) -> list:
        pass
    
    def get_pref(self, **kwargs:any) -> list:
        pass
    
    def add_history(self, p):
        pass
    
test = Preferences()
prefe = {"languaje" : "es", "len_history":5}

history = [""]