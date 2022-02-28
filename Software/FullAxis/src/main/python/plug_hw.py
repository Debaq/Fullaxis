# -*- coding: utf-8 -*-


import serial
import serial.tools.list_ports
from time import sleep
from PySide6.QtCore import Signal, QThread, QIODevice
from PySide6.QtSerialPort import QSerialPortInfo, QSerialPort

bautrade_hw = 9600


def Serial_discover():
    ports = QSerialPortInfo.availablePorts()
    port = None
    for i in ports:
        manufactured = "wch.cn"
        description = "USB-SERIAL CH340"
        if i.manufacturer() == manufactured and i.description() == description:
            port = i
            
    return port
        
 
def Serial_read(port):
    if port is not None:
        f_axis_connector = QSerialPort(port)
        f_axis_connector.setBaudRate(bautrade_hw)
        f_axis_connector.setDataBits(QSerialPort.Data8)
        f_axis_connector.setParity(QSerialPort.NoParity)
        f_axis_connector.setStopBits(QSerialPort.OneStop)
        f_axis_connector.setFlowControl(QSerialPort.NoFlowControl)
        data = f_axis_connector.readLine()
        

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
                        print(data)
                    except UnicodeDecodeError:
                        print("Error: No se pudo decodificar el mensaje")
                    
                    if read == "stop":
                        break
            return hw

    else:
        return None
            

def reset_hw(hw):
    try:
        if not hw.isOpen():
            hw.open()
        hw.setDTR(False)
        sleep(1)
        hw.flushInput()
        hw.setDTR(True)    
    except AttributeError:
        print("Error: no exite dispositivo conectado")

#class receiver_data(QThread):
class receiver_data(QThread):

    data = Signal(object)
     
        
    def run(self):
        self.continue_reading = True
        self.port = verify_receptor_serial()
        self.read_data()

    def read_data(self):
        with self.port:
            while self.continue_reading:
                data = self.port.readline()
                if data == b'':
                    print("nvio dato de activación")
                    self.port.write(b'33')
                try:
                    clean_data = data.decode('utf-8').strip('\r\n')
                except UnicodeDecodeError:
                    print("Error: No se pudo decodificar el mensaje")
                if clean_data[:3] != "Soy":
                    try:
                        roll,pitch,yaw,dt = clean_data.split(',')
                        data = [float(roll),float(pitch),float(yaw),float(dt)]
                        self.data.emit(data)
                    except ValueError:
                        print("Error: No se pudo decodificar el mensaje: {}".format(data))
                        
                           
    def stop_reading(self):
        self.continue_reading = False
#        reset_hw(self.port)
        self.port.close()

