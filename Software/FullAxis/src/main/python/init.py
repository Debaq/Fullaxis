# -*- coding: utf-8 -*-

from fbs_runtime.application_context.PyQt6 import ApplicationContext
context = ApplicationContext()


class ParameterInput():
    """
        permite actualizar el programa en formato no freeze
        solo es un metodo de desarrollo
        cualquier intento de hacerlo funcionar en producción 
        podrá saltar un error
    """
    def __init__(self, i, os_system) -> None:
        self.final_state = None
        double_dash_pos = i.find("--")
        if double_dash_pos == -1:
            self.help()
        else:
            _, action = i.split("--")
            self.activate(action, os_system)


    def activate(self, action, os_system):
        if action == "update-all":
            self.update_all(os_system)
        elif action == "update-uic":
            self.update_uic(os_system)
        elif action == "update-rc":
            self.update_rc(os_system)
        elif action == "update-uic-run":
            self.update_uic_run(os_system)
        else:
            self.help()

    def update_all(self, os_system):
        print("update-all")
        self.final_state = "stop"
    
    def update_uic(self, os_system):
        print("update-uic")
        self.final_state = "stop"
    
    def update_rc(self, os_system):
        print("update-rc")
        self.final_state = "stop"
    
    def update_uic_run(self, os_system):
        print("update-uic-run")
        self.final_state = "continue"
        
    def help(self):
        print("""
Error : Opción desconocida.
            
    Use: python Fullaxis.py
         python Fullaxis.py <opción>
            
        Opciones:
            --update-all        :   actualiza los archivos .ui y .rc
            --update-uic        :   actualiza los archivos .ui en devolpment/Form
            --update-rc         :   actualiza los archivos .rc en devolpment/resource
            --update-uic-run    :   actualiza los archivos .ui en devolpment/Form y corre el programa
        """)
        self.final_state = "stop"
