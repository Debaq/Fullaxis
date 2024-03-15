"""import usb.core
import usb.util
import usb.backend.libusb1


backend = usb.backend.libusb1.get_backend(find_library=lambda x: "C:\\libusb-1.0.20\\MS64\\dll\\libusb-1.0.dll")


devs = usb.core.find(backend=backend, find_all=True)

# Encuentra los dispositivos USB

# Itera sobre los dispositivos
for dev in devs:
    print('Dispositivo encontrado')
    print('ID del producto: ', dev.idProduct)
    print('ID del vendedor: ', dev.idVendor)
    print('Número de serie: ', dev.serial_number)
    print('Clase del dispositivo: ', dev.bDeviceClass)
    print('Subclase del dispositivo: ', dev.bDeviceSubClass)
    print('Protocolo del dispositivo: ', dev.bDeviceProtocol)
    print('Número de configuraciones: ', dev.bNumConfigurations)
    print('Fabricante: ', usb.util.get_string(dev, dev.iManufacturer))
    print('Producto: ', usb.util.get_string(dev, dev.iProduct))
    print('Número de serie: ', usb.util.get_string(dev, dev.iSerialNumber))
    print('-----------------------------')
    print('-----------------------------')"""

"""
from pywinusb import hid

# Obtén todos los dispositivos HID
all_devices = hid.find_all_hid_devices()

# Itera sobre todos los dispositivos
for device in all_devices:
    # Abre el dispositivo para que podamos acceder a sus propiedades
    device.open()

    # Imprime el nombre amigable del dispositivo
    print('Nombre amigable: ', device.product_name)

    # Cierra el dispositivo
    device.close()
"""

import os

class CameraId:
    def __init__(self, name_cam="USB Camera: USB GS CAM"):
        self.cameras_list = []
        if os.name == 'posix':
            self.camera = self.linux(name_cam)
        elif os.name == 'nt':
            self.camera = self.windows(name_cam)

    def get_camera(self):
        return self.camera

    def get_cameras_list(self):
        return self.cameras_list


    def linux(self, name):
        for i in range(10):
            try:
                with open(f"/sys/class/video4linux/video{i}/name","r") as hw_video:
                    hw_name = hw_video.read()
                    hw_name = hw_name.replace("\n","")
                    self.cameras_list.append([hw_name, i])
            except FileNotFoundError:
                self.cameras_list.append(["None", i])
        
        #print(f"cameras found: {cameras}")
        for c in self.cameras_list:
            if  c[0].startswith(name):
                return(True, c[1])
            
        #print("Camera not found")

                
        
            
   
    def windows(self, name):
        import asyncio
        import winsdk.windows.devices.enumeration as windows_devices

        async def get_camera_info():
            return await windows_devices.DeviceInformation.find_all_async(4)

        connected_cameras = asyncio.run(get_camera_info())
        names = [camera.name for camera in connected_cameras]
        print(f"cameras found: {names}")
        if name not in names:
            print("Camera not found")
            return (False, None)
        else:
            camera_index = names.index(name)
            return(True, camera_index)
        


if __name__ == "__main__":
    cam = CameraId()
    cam.get_camera()