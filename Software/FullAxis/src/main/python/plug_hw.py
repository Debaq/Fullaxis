# -*- coding: utf-8 -*-


import serial
import serial.tools.list_ports
from time import sleep
      
bautrade_hw = 9600


def verify_receptor_serial():
    ports = list(serial.tools.list_ports.comports())
    if ports_hw := [i.device for i in ports]:
        for i in ports_hw:
            hw = serial.Serial( port = i, 
                                baudrate = bautrade_hw, 
                                bytesize=serial.EIGHTBITS,
                                parity=serial.PARITY_NONE,
                                stopbits=serial.STOPBITS_ONE,
                                timeout=1,
                                xonxoff=0,
                                rtscts=0
                                )

            reset_hw(hw)
            def read_response(data):
                return "continue" if data[:3] == "Soy" else "stop"
            
            read = "continue"
            with hw:
                while True:
                    data = hw.readline()
                    if data == b'':
                        hw.write(b'33')
                    try:
                        clean_data = data.decode('utf-8').strip('\r\n')
                        read = read_response(clean_data)
                    except UnicodeDecodeError:
                        print("Error: No se pudo decodificar el mensaje")
                    
                    if read == "stop":
                        break
            return hw

    else:
        return None
            

def reset_hw(hw):
    if not hw.isOpen():
        hw.open()
    hw.setDTR(False)
    sleep(1)
    hw.flushInput()
    hw.setDTR(True)    