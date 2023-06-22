#from jmespath import search
import datetime
from pathlib import Path

from tinydb import Query, Storage, TinyDB

from base import context

database_path = Path(context.get_resource('database.json'))

class ProfileData():
    def __init__(self) -> None:
        self.data_base = TinyDB(database_path)

    def set_data(self, **kwargs) -> None:
        if kwargs["number_unique"] == "":
            kwargs["number_unique"] = self.verify_enumerate()
            kwargs['type'] = "profile"
            self.create_pofile(kwargs)
            return kwargs["number_unique"]
        else:
            #si ya existe debe actualizarce
            print("no hay nada que hacer, ya existe el perfil")
    
    def get_profile_by_number(self, number_user) -> dict:
        name_table_profile = number_user
        table_profile = self.data_base.table(name_table_profile)
        return table_profile.all()[0]
    
    def create_pofile(self, data):
        name_table_profile = "profile_{:05d}".format(data["number_unique"])
        table_new_profile = self.data_base.table(name_table_profile)
        table_new_profile.insert(data)
    
    def update_profile(self, **kwargs):
        data = kwargs
        data["number_unique"] = int(data["number_unique"])
        name_table_profile = "profile_{:05d}".format(data["number_unique"])
        table_index = self.data_base.table(name_table_profile)
        for key, data in data.items():
            table_index.update({key:data})


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
        return self.add_index() if self.data_base.tables() else self.create_new_base()
        
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
        data = [i for i in profiles if i.startswith("profile")]
        data.sort()
        return data

    def get_list_profile_full(self) -> list:
        list_profile = self.get_list_profiles()
        return [self.get_profile_full(i) for i in list_profile]
    
    def get_profile_full(self, name_profile) -> dict:
        return self.data_base.table(name_profile).all()[0]
    

class SessionData():
    def __init__(self) -> None:
        path = Path(context.get_resource('database.json'))
        self.data_base = TinyDB(path)

    def create_session(self, number_unique) -> int:
        name_table_profile = "profile_{:05d}".format(number_unique)
        profile = self.data_base.table(name_table_profile)
        session_index = self.create_index_session(profile)
        date_now = datetime.datetime.now()
        date = f"{date_now.day}.{date_now.month}.{date_now.year}"
        index_session = f"{number_unique}.{session_index}"
        position = session_index - 1
        name = f"session_{session_index}"
        profile.insert({"type" : "session",
                        "name" : name,
                        "unique_id" : index_session,
                        "date_create" : date,
                        "activity" : [],
                        "enable" : True,
                        "position" : position
                        })
        return self.search_unique_id(index_session, profile)
    
    def create_index_session(self, profile) -> list:
        search = Query()
        if index_session := profile.search(search.type == "index_session"):
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
        return profile.search(search.unique_id == unique_id)
        
    def search_new_index_session(self, profile) -> list:
        search = Query()
        index_session = profile.search(search.type == "index_session")
        return index_session[0]["list_session"]

    def load_sessions(self, name_profile) -> list:
        profile = self.data_base.table(name_profile)
        search = Query()
        return profile.search(search.type == "session")


class ActivityData():
    def __init__(self) -> None:
        path = Path(context.get_resource('database.json'))
        self.data_base = TinyDB(path)
    
    def create_activity(self, profile, session, name) -> dict:
        profile_db = self.data_base.table(profile)
        search = Query()
        data_session = profile_db.search(
            (search.type == "session")&(search.name == session))
        idx = data_session[0]["activity"][-1] + 1 if data_session[0]["activity"] else 0
        date_now = datetime.datetime.now()
        date = f"{date_now.day}.{date_now.month}.{date_now.year}"
        index_test = f'{data_session[0]["unique_id"]}.{idx}'
        data = {
            "type" : "test",
            "name" : name,
            "unique_id" : index_test,
            "date_create" : date,
            "data" : [],
            "comments" : "",
            "enable" : True,
            "position" : idx
            }
        profile_db.insert(data)
        self.add_in_session(profile_db,
                            data_session[0]["unique_id"],
                            data_session[0]["activity"],idx)
        return data
    
    def add_in_session(self,profile,unique_id,idxs,idx)->None:
        search = Query()
        _idxs = idxs
        _idxs.append(idx)
        profile.update({'activity': _idxs}, search.unique_id == unique_id)

    def load_activities(self, name_profile, unique_id ) -> list:
        profile = self.data_base.table(name_profile)
        search = Query()
        index_activity = profile.search(search.type == "test")
        return [i for i in index_activity if i["unique_id"].startswith(unique_id)]
    
    def save_data(self, profile, unique_id, data) -> None:
        profile_db = self.data_base.table(profile)
        search = Query()
        #index_activity = profile_db.search(search.unique_id == unique_id)
        profile_db.update({'data': data}, search.unique_id == unique_id)

    def load_data(self, profile, unique_id) -> list:
        profile_db = self.data_base.table(profile)
        search = Query()
        index_activity = profile_db.search(search.unique_id == unique_id)
        return index_activity[0]["data"]


class DeleteData():
    def __init__(self, name_profile:str, list_id_unique:list) -> None:
        self.data_base = TinyDB(database_path)
        id_unique = self.transform_id_unique(list_id_unique)
        table_active = self.table(name_profile)
        if len(list_id_unique) == 3:
            self.delete_activity(table_active, id_unique)
        elif len(list_id_unique) == 2:
            self.delete_session(table_active, id_unique)
        elif len(list_id_unique) == 1:
            self.delete_profile(table_active, id_unique)
    
    def transform_id_unique(self, list_id_unique:list) -> str:
        id_unique = "".join(f'{i}.' for i in list_id_unique)
        return id_unique[:-1]

    def table(self, name_profile:str) -> TinyDB:
        return self.data_base.table(name_profile)

    def delete_profile(self, table:TinyDB) -> None:
        print("eliminaremos el profile")
    
    def delete_session(self, table:TinyDB, id_unique:str) -> None:
        search = Query()
        session = table.search(search.unique_id == id_unique)
        #table.remove(search.unique_id == id_unique)
        ativities = session[0]["activity"]
        for i in ativities:
            id_unique_activity = f"{id_unique}.{i}"
            self.delete_activity(table, id_unique_activity)
        table.remove(search.unique_id == id_unique)           

        print("eliminaremos la session")

    def delete_activity(self, table:TinyDB, id_unique:str) -> None:
        search = Query()
        table.remove(search.unique_id == id_unique)
        self.modify_index_session(table, id_unique)
        print("eliminaremos la activity")

        
    def modify_index_session(self, table:TinyDB, id_unique:str) -> None:
        p,s,a = id_unique.split(".")
        session_id_unique =  self.transform_id_unique([p,s])
        search = Query()
        session = table.search(search.unique_id == session_id_unique)
        idx_session = session[0]["activity"]
        idx_session.remove(int(a))
        table.update({'activity': idx_session}, search.unique_id == session_id_unique)
        
   