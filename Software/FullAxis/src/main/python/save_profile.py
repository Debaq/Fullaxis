#from jmespath import search
from tinydb import Storage, TinyDB, Query
from init import context
from pathlib import Path
import datetime


class ProfileData():
    def __init__(self) -> None:
        path = Path(context.get_resource('database.json'))
        self.data_base = TinyDB(path)
       

    def set_data(self, **kwargs) -> None:
        if kwargs["number_unique"] == "nn":
            kwargs["number_unique"] = self.verify_enumerate()
            self.create_pofile(kwargs)
            return kwargs["number_unique"]
        else:
            #si ya existe debe actualizarce
            print("no hay nada que hacer, ya existe el perfil")
            
    def create_pofile(self, data):
        name_table_profile = "profile_{}".format(data["number_unique"])
        table_new_profile = self.data_base.table(name_table_profile)
        table_new_profile.insert(data)
        

    def table_index(self) -> list:
        return self.data_base.table('index').all()
        
    def last_index(self, table) -> list:
            return table[0]['list_ids']
        
    def add_index(self) -> int:
        list_index = self.last_index(self.table_index())
        new_index = list_index[-1] + 1
        list_index.append(new_index)
        table_index = self.data_base.table('index')
        search = Query()
        table_index.update({'list_ids': list_index}, search.unique_id == 'index')
        self.update_last_profile(new_index)
        return new_index

    def update_last_profile(self, number):
        search = Query()
        table_index = self.data_base.table('index')
        table_index.update({'last_profile': number}, search.unique_id == 'index')


    def verify_enumerate(self) -> int:
        if not self.data_base.tables():
            return self.create_new_base()
        return self.add_index()
        
    def create_new_base(self) -> int:
        table_index = self.data_base.table('index')
        table_index.insert(
                            {'unique_id' : 'index',
                            'list_ids':[1],
                            'last_profile':1
                            })
        return 1

class SessionData():
    def __init__(self) -> None:
        path = Path(context.get_resource('database.json'))
        self.data_base = TinyDB(path)
    
    def create_session(self, number_unique):
        name_table_profile = "profile_{}".format(number_unique)
        profile = self.data_base.table(name_table_profile)
        session_index = self.create_index_session(profile)
        date_now = datetime.datetime.now()
        date = "{}.{}.{}".format(date_now.day, date_now.month, date_now.year)
        index_session = "{}.{}".format(number_unique, session_index)
        position = session_index - 1
        name = "session_{}".format(session_index)
        profile.insert({"type" : "session",
                        "name" : name,
                        "unique_id" : index_session,
                        "date_create" : date,
                        "activity" : [],
                        "enable" : True,
                        "position" : position
                        })
        return name, position
    def create_index_session(self, profile):
        search = Query()
        index_session = profile.search(search.type == "index_session")
        if index_session:
            list_idx = self.search_new_index_session(profile)
            new_idx = list_idx[-1] + 1
            list_idx.append(new_idx)
            profile.update({'list_session': list_idx}, search.type == 'index_session')
            return new_idx
        else:
            profile.insert({
                "type":"index_session",
                "list_session" : [1]
            })
            return 1
    
    def search_new_index_session(self, profile):
        search = Query()
        index_session = profile.search(search.type == "index_session")
        return index_session[0]["list_session"]



class ActivityData():
    def __init__(self) -> None:
        path = Path(context.get_resource('database.json'))
        self.data_base = TinyDB(path)
    
        
 