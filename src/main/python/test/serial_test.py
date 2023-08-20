import serial
import serial.tools.list_ports
import time

class ArduinoConnection:
    def __init__(self):
        self.ser = None
        self.port = self._find_arduino_port()
        self.state = "disconnected"

    def _find_arduino_port(self):
        ports = list(serial.tools.list_ports.comports())
        for port in ports:
            try:
                with serial.Serial(port.device, 9600, timeout=1) as ser:
                    time.sleep(2)  # Espera a que la conexión se establezca
                    response = ser.readline().decode('utf-8').strip()
                    if response == "VNG":
                        ser.close()
                        return port.device
            except (serial.SerialException, serial.SerialTimeoutException):
                pass
        return None

    def connect(self):
        if self.port:
            self.ser = serial.Serial(self.port, 9600)
            time.sleep(3)  # Espera a que la conexión se establezca
            response = self.ser.readline().decode('utf-8').strip()
            print(f"conectado a {response}")
            self.state = "connected"
        else:
            raise ConnectionError("No se encontró el puerto de Arduino")

    def disconnect(self):
        if self.ser:
            self.ser.close()
            self.state = "disconnected"

    def get_state(self):
        return self.state

    def send_instruction(self, instruction):
        if self.state != "connected":
            raise ConnectionError("Arduino no está conectado")

        print(f"enviando instrucción: {instruction}") 
        self.ser.write(instruction.encode('utf-8'))
        response = self.ser.readline().decode('utf-8').strip()
        print(f"la respuesta fue: {response}")
        if response != "ok":
            raise Exception(f"Error al enviar instrucción: {response}")

    def read_buffer(self):
        if self.state != "connected":
            raise ConnectionError("Arduino no está conectado")
        
        return self.ser.readline().decode('utf-8').strip()

# Uso:
arduino = ArduinoConnection()
arduino.connect()
print(arduino.get_state())  # Debería imprimir "connected"
arduino.send_instruction("info")
print(arduino.read_buffer())
arduino.send_instruction("led_on")
arduino.disconnect()
print(arduino.get_state())  # Debería imprimir "disconnected"
