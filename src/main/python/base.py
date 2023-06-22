#from fbs_runtime.application_context.PySide6 import ApplicationContext
from PySide6.QtWidgets import QApplication
import pathlib

print(pathlib.Path(__file__).parent.absolute())



class ApplicationContext():
    
    def __init__(self) -> None:
        self.app = QApplication([])
    
    def get_resource(self, path):
        return f"resources/{path}"
       
        
context = ApplicationContext()


