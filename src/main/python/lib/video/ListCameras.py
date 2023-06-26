import usb.core
import usb.util

# Encuentra los dispositivos USB
devs = usb.core.find(find_all=True)

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
    print('ID del vendedor:', hex(dev.idVendor))
    print('ID del producto:', hex(dev.idProduct))
    print('-----------------------------')
