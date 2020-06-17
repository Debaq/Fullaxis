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
"""

import requests

## URL donde esta alojada la API
url = 'https://tmeduca.cl/fullaxis/lib/API.php'


def request_key(name_user, password):
    request_array = {'user':name_user, 'password': password} 
    response = requests.post(url, data=request_array)
    print(response.text)
    
    

    
request_key("NicoQB", 1234)    


#testing_API(1)