from PySide6.QtCore import QThread, Signal
import serial.tools.list_ports as port
ports = port.comports()

for port, desc, hwid in sorted(ports):
        port = port
        
        
import serial
import time
arduino = serial.Serial(port=port, baudrate=115200, timeout=.1)
def write_read(x):
        arduino.write(bytes(x, 'utf-8'))
        time.sleep(0.05)
        return arduino.readline()


class read_serial(QThread):
        data_signal = Signal()
        def run(self):
                print("hola mundo")
        

if __name__ == '__main__':
        while True:
                num = input("Enter a number: ") # Taking input from user
                value = write_read(num)
                print(value.decode('utf-8').replace("\r\n","")) # printing the value
                

                """
                comandos:
                1000 : tipo de dispositivo
                1001 : MAC
                2X00 : Cambiar Estado
                0   : Estado actual
                1   : Listar conectados
                3X  : Solicitar paquete de informacion del dispositivo X
                """