from PySide6.QtCore import QIODevice, Slot
from PySide6.QtSerialPort import QSerialPortInfo, QSerialPort

bautrade_hw = 9600


class FullAxisConnector():
    def __init__(self) -> None:
        port = self.Serial_discover()
        self.Serial_read(port)


    def Serial_discover(self):
        ports = QSerialPortInfo.availablePorts()
        port = None
        for i in ports:
            manufactured = "wch.cn"
            description = "USB-SERIAL CH340"
            if i.manufacturer() == manufactured and i.description() == description:
                port = i

        return port

    def Serial_read(self, port):
        if port is not None:
            self.f_axis_connector = QSerialPort(port, readyRead=self.read_response)
            self.f_axis_connector.setBaudRate(QSerialPort.Baud9600)
            self.f_axis_connector.setDataBits(QSerialPort.Data8)
            self.f_axis_connector.setParity(QSerialPort.NoParity)
            self.f_axis_connector.setStopBits(QSerialPort.OneStop)
            self.f_axis_connector.setFlowControl(QSerialPort.NoFlowControl)
            


    @Slot()
    def read_response(self):
        while self.f_axis_connector.canReadLine():
            line = self.f_axis_connector.readLine().data().decode()
            line = line.rsplit('\r\n')
            print(line)



test = FullAxisConnector()