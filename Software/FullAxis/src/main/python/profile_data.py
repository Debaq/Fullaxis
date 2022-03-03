#from jmespath import search
from tinydb import Storage, TinyDB, Query
from init import context
from pathlib import Path
import datetime

database_path = Path(context.get_resource('database.json'))

class ProfileData():
    def __init__(self) -> None:
        self.data_base = TinyDB(database_path)
       

    def set_data(self, **kwargs) -> None:
        if kwargs["number_unique"] == "nn":
            kwargs["number_unique"] = self.verify_enumerate()
            self.create_pofile(kwargs)
            return kwargs["number_unique"]
        else:
            #si ya existe debe actualizarce
            print("no hay nada que hacer, ya existe el perfil")
            
    def create_pofile(self, data):
        name_table_profile = "profile_{:05d}".format(data["number_unique"])
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


class ListProfiles():
    def __init__(self):
        self.data_base = TinyDB(database_path)

    
    def get_list_profiles(self):
        profiles = self.data_base.tables()
        data = []
        for i in profiles:
            if i.startswith("profile"):
                data.append(i)
        data.sort()
        return data

    def get_list_profile_full(self):
        list_profile = self.get_list_profiles()
        data = []
        for i in list_profile:
            data.append(self.get_profile_full(i))
        return data
    
    def get_profile_full(self, name_profile):
        return self.data_base.table(name_profile).all()[0]
    
    

class SessionData():
    def __init__(self) -> None:
        path = Path(context.get_resource('database.json'))
        self.data_base = TinyDB(path)

    
    def create_session(self, number_unique):
        name_table_profile = "profile_{:05d}".format(number_unique)
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
        data = self.search_unique_id(index_session, profile)
        return data
    
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
        
    def search_unique_id(self, unique_id, profile):
        search = Query()
        index_session = profile.search(search.unique_id == unique_id)
        return index_session
        
    def search_new_index_session(self, profile):
        search = Query()
        index_session = profile.search(search.type == "index_session")
        return index_session[0]["list_session"]

    def load_sessions(self, name_profile):
        profile = self.data_base.table(name_profile)
        search = Query()
        index_session = profile.search(search.type == "session")
        return index_session


class ActivityData():
    def __init__(self) -> None:
        path = Path(context.get_resource('database.json'))
        self.data_base = TinyDB(path)
    
    def create_activity(self, profile, session, name):
        profile_db = self.data_base.table(profile)
        search = Query()
        print(profile)
        print(session)
        print(name)
        data_session = profile_db.search((search.type == "session")&(search.name == session))
        print(data_session)
        print(data_session[0])
        if not data_session[0]["activity"]:
            idx = 0
        else:
            idx = data_session[0]["activity"][-1] + 1
        date_now = datetime.datetime.now()
        date = "{}.{}.{}".format(date_now.day, date_now.month, date_now.year)
        index_test = "{}.{}".format(data_session[0]["unique_id"], idx)
        profile_db.insert({
            "type" : "test",
            "name" : name,
            "unique_id" : index_test,
            "date_create" : date,
            "data" : [],
            "comments" : "",
            "enable" : True,
            "position" : idx
            })
        self.add_in_session(profile_db,data_session[0]["unique_id"],data_session[0]["activity"],idx)
    
    def add_in_session(self,profile,unique_id,idxs,idx):
        search = Query()
        _idxs = idxs
        _idxs.append(idx)
        profile.update({'activity': _idxs}, search.unique_id == unique_id)


        
        
   