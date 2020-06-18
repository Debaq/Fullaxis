# -*- coding: utf-8 -*-
#################################################################
#                                                               #
#                  NOMBRE PROYECTO : FULLAXIS                   #
#                       VER. 1.0 - CONECTOR API                 #
#               CREADOR : NICOLÁS QUEZADA QUEZADA               #
#                                                               #
#################################################################
""" 
El siguiente código es para conectarse a la API de Fullaxis
Posee funciones:
     - para obtener las key del servicio de almacenaje
     - para enviar documentos al almacenaje
     - para recuperar docuemtnos del almacenaje 
     
Lógica de funcionamiento:

==================Interfaz====================
|  ▼ usuario y        ◘                   ▲ |
|  ▼ contraseña       ◘  entrega archivos ▲ |
|  ▼ .                ◘  al workspace     ▲ |
|==============API_CONECTOR.py=================
|  ▼ requests         ◘                   ▲ |
|  ▼ Server           ◘  conecta el  srv  ▲ |
|  ▼ .                ◘  al workspace     ▲ |
|  ▼ .                ◘  mediante las keys▲ |
|=================API.php=======================
|  ▼ verifica         ◘                   ▲ |
|  ▼ usuario y        ◘  entrega keys     ▲ |
|  ▼ contraseña       ◘  del server de    ▲ |
|  ▼ .                ◘  almacenaje       ▲ |
===================MYSQL=======================


    ejemplo:
        import API_conector
        Nombre = 'name'
        Password = 'pass123'
        data_conection = API_conector.request_key(Nombre, Password)
        app_key_id = data_conection[0]
        app_key = data_conection[1]
        bucket_name = data_conection[2]
        conection_b2 = API_conector.b2_conect(app_key_id, app_key, bucket_name)
"""

import requests
from b2sdk.v1 import *

## URL donde esta alojada la API
url = 'https://tmeduca.cl/fullaxis/lib/API.php'


def request_key(name_user, password):
    """request_key

    Args:
        name_user (str): Usuario
        password (str): Contraseña

    Returns:
        Lista: lista con [0]app_key_id, [1]app_key, [2]bucket_name
    """
    request_array = {'user':name_user, 'password': password} 
    response = requests.post(url, data=request_array)
    string_response=(response.text)
    string_response=string_response.split(',')
    return string_response
    
       
class b2_conect():
    """
    Para que funcione es necesario correr request_key(), con un usuario y pasword validos
    
    b2 conect permite conectarse al bucket especificado en la base de datos
    - listar los archivos existentes
    - descargar los archivos
    - cargar nuevos archivos
    
    """
    def __init__(self,app_key_id, app_key, app_bucket):
        """conección

        Args:
            app_key_id (str): id obtenido desde la base de datos generado por b2
            app_key ([type]): key obtenida desde la base de datos generado por b2
            app_bucket ([type]): bucket obtenido desde la base de datos generado por b2
        """
        self.info = InMemoryAccountInfo()
        self.b2_api = B2Api(self.info)
        application_key_id = app_key_id
        application_key = app_key
        self.app_bucket_name = app_bucket
        self.b2_api.authorize_account("production", application_key_id, application_key)
        
    
    def request_list(self):
        """request_list

        Returns:
            array: devuelve los archivos en un array, cada elemento posee [0]nombre,[1]timestamp,[2]carpeta
        """
        bucket = self.b2_api.get_bucket_by_name(self.app_bucket_name)
        result = []
        for file_info, folder_name in bucket.ls(show_versions=False):
            info = [file_info.file_name, file_info.upload_timestamp, folder_name]
            result.append(info)
        return result

    def upload_file(self, local_file_path, b2_file_name, file_info):

        bucket = self.b2_api.get_bucket_by_name(self.app_bucket_name)
        bucket.upload_local_file(
            local_file=local_file_path,
            file_name=b2_file_name,
            file_infos=file_info
        )