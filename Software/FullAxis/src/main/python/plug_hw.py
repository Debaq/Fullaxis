# -*- coding: utf-8 -*-


import serial
import serial.tools.list_ports
from time import sleep
from PySide6.QtCore import Signal, QThread
import signal
import sys

bautrade_hw = 115200


class FullAxisReceptor():
    def __init__(self) -> None:
        pass
        #port = self.search_port()
        #self.connection = self.activate_connection(port)
        #self.reset(self.connection)
        
    def search_port(self):
        ports = list(serial.tools.list_ports.comports())
        manufactured = ["wch.cn", "1a86"]
        description = ["USB-SERIAL CH340", "USB2.0-Serial","USB-SERIAL CH340 (COM7)","USB-SERIAL CH340 (COM3),USB-SERIAL CH340 (COM4),USB-SERIAL CH340 (COM5)"]
        vid = [6790]
        pid = [29987]
        port = None
        if ports :
            for p in ports:
                #if p.description in description and p.pid in pid and p.vid in vid:
                if p.description in description :

                    port = p.device
        return port    
               
               
    def search_ports(self):
        data = []
        ports = serial.tools.list_ports.comports()
        for i in ports:
            port = [i.device, i.name,i.description,i.hwid,i.vid,i.pid,i.serial_number,i.location,i.manufacturer,i.product,i.interface]
            data.append(port)

            
        
        return data
    
                
    def reset(self,hw):
        try:
            if not hw.isOpen():
                hw.open()
            hw.setDTR(False)
            sleep(1)
            hw.flushInput()
            hw.setDTR(True)    
        except AttributeError:
            return None

            

    def activate_connection(self,port):
        try:
            hw = serial.Serial(port = port, 
                                baudrate = bautrade_hw, 
                                bytesize=serial.EIGHTBITS,
                                parity=serial.PARITY_NONE,
                                stopbits=serial.STOPBITS_ONE,
                                timeout=1,
                                xonxoff=0,
                                rtscts=1)
            return hw
        except AttributeError:
            print("Error: no exite dispositivo conectado")
            return None
    
    def is_open(self):
        return self.connection.isOpen()
    
    def activate_receptor(self):
        self.connection.write(b'51')
        
    def read_line(self):
        error = False
        try:
            line = self.connection.readline().decode().replace("\r\n","")
           
        except UnicodeDecodeError:
            error = True
        if error == False:
            if line[:3] != "Soy":
                try:
                    roll,pitch,yaw,dt = line.split(',')
                    data = [float(roll),float(pitch),float(yaw),float(dt)]
                    return data
                except ValueError:
                   self.activate_receptor()
        


#w = FullAxisReceptor()
#w.activate_receptor()  
#while True:
    #print(w.read_line())


class ReceiverData(QThread):
    data = Signal(object)

    def run(self):
        self.connector = FullAxisReceptor()
        self.connector.activate_receptor()
        self.continue_reading = True
        self.read = True
        self.read_data()

    def read_data(self):
        while True:
            while self.read:
                data = self.connector.read_line()
                if data !=None:
                    self.data.emit(data)
                

    def stop_reading(self, a = True):
        if a:
            self.read = False
        else:
            self.read = True
        

if __name__ == "__main__":

    W = FullAxisReceptor()
    W.activate_receptor()
    while True:
        print(W.read_line())