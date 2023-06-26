import platform

def list_video_devices_linux():
    import pyudev

    context = pyudev.Context()
    monitor = pyudev.Monitor.from_netlink(context)
    monitor.filter_by(subsystem='video4linux')

    for device in context.list_devices(subsystem='video4linux'):
        print(f"Device '{device.device_node}' hardware ID: {device.get('ID_SERIAL')}")

def list_video_devices_windows():
    import win32com.client

    wmi = win32com.client.GetObject ("winmgmts:")
    for usb in wmi.InstancesOf ("Win32_USBControllerDevice"):
        dev = usb.Dependent
        if 'VID_' in dev:
            print(dev)

def list_video_devices_mac():
    # En macOS, no hay una forma directa de listar los dispositivos de video
    # como en Linux o Windows. Sin embargo, puedes usar el comando 'system_profiler'
    # para obtener información sobre los dispositivos USB, que pueden incluir
    # dispositivos de video. Este es un ejemplo de cómo podrías hacerlo:
    import subprocess

    output = subprocess.check_output('system_profiler SPUSBDataType', shell=True)
    print(output.decode())

# Detecta el sistema operativo actual y llama a la función apropiada
if platform.system() == 'Linux':
    list_video_devices_linux()
elif platform.system() == 'Windows':
    list_video_devices_windows()
elif platform.system() == 'Darwin':  # macOS
    list_video_devices_mac()
else:
    print('Sistema operativo no soportado')
