from encodings import utf_8
from PySide6.QtSerialPort import QSerialPortInfo, QSerialPort
from PySide6.QtCore import QThread, Signal,Slot,QIODevice, QByteArray
from PySide6 import Qt



class receiver_data(QThread):
    data = Signal(str)

    def run(self):
        self.portname = self.Serial_discover()
        self.serial = QSerialPort(
            self.portname,
            baudRate= 9600,
            readyRead=self.receive)
        self.data.emit("Serial port is open")
        self.serial.open(QIODevice.ReadWrite)
        self.send(self.serial.isOpen())
        self.send(self.serial.isReadable())
        self.send_auto()
        while True:
            self.receive()
   
    def Serial_discover(self):
        ports = QSerialPortInfo.availablePorts()
        port = None
        for i in ports:
            manufactured = ["wch.cn", "1a86"]
            description = ["USB-SERIAL CH340", "USB2.0-Serial"]
            if i.manufacturer() in manufactured and i.description() in description:
                port = i
        return port
          
    def receive(self):
        text = self.serial.readLine().data().decode()
        if len(text) != 0:
            
            #text = text.rstrip('\r\n')
            self.data.emit("algo esta entrando")
        else:
            self.data.emit("no entra nada")

            self.send_auto()

            
    def send(self, data):
        if data is not str:
            data = str(data)
        self.data.emit(data)
        
        
    def send_auto(self):
        self.serial.write("33".encode())
        

    def close(self):
        self.serial.close()