import usb.core
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
    print('-----------------------------')

