# -*- coding: utf-8 -*-

#################################################################
#                                                               #
#                  NAME PROJECT : FULLAXIS                      #
#                   VER. 22.2.25 - GUI PySide6                  #
#                    NAME  VER. : reboot                        #
#               CREATOR : DAVID ÁVILA QUEZADA                   #
#                          AKA: NICOLÁS QUEZADA BAIER           #
#                                                               #
#################################################################

import os
import sys
from time import sleep

os_system = 'win' if os.name == 'nt' else 'linux'

if len(sys.argv) > 1:
    from init import ParameterInput
    parameters = ParameterInput(sys.argv[1], os_system)
    if parameters.final_state == "stop":
        sys.exit()

from fbs_runtime.application_context.PyQt6 import ApplicationContext

from PySide6.QtWidgets import QMainWindow

from plug_hw import verify_receptor_serial, reset_hw


class MainWindows(QMainWindow):
    def __init__(self, port):
        super().__init__()
        self.port_receptor = port
        self.resize(800, 600)
        self.show()
         

if __name__ == "__main__":
    port = verify_receptor_serial()
    context = ApplicationContext()
    windows = MainWindows(port)
    exit_code = context.app.exec()
    reset_hw(port)
    sys.exit(exit_code)