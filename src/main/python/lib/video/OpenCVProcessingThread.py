import os
import time

import cv2
import numpy as np
from lib.video.BlobDetector import BlobDetector
from PySide6.QtCore import Qt, QThread, Signal
from PySide6.QtGui import QImage
from base import context



class OpenCVProcessingThread(QThread):
    change_pixmap_signal = Signal(QImage)
    signal_frame_states = Signal(dict)

    def __init__(self, parent=None, cam_n=0):
        super().__init__(parent)
        self._running = True
        self._flip_horizontal = False
        self.blob_detector_left = BlobDetector()
        self.blob_detector_rigth = BlobDetector()
        self.record = [False, 0, False]
        self.cam_n = cam_n

    def run(self):
        # Captura de video desde la cámara por defecto (0)

        self.open_cap()

        while self._running:

            if self._running:
                ret, frame = self.cap.read()
                if ret:
                    if self.record[0]:
                        self.record[1] += 1
                        im_bgr = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
                        self.out.write(im_bgr)

                    height, width = frame.shape[:2]
                    left_half = frame[:, :width//2]
                    right_half = frame[:, width//2:]
                    # Dibujar rectángulos alrededor de las mitades de la imagen
                    cv2.rectangle(left_half, (0, 0),
                                  (width//2, height), (255, 255, 255), 2)
                    cv2.rectangle(right_half, (0, 0),
                                  (width//2, height), (255, 255, 255), 2)
                    # Definir textos y colores para cada lado
                    left_text, left_color = ("Ojo Derecho", (0, 0, 255)) if not self._flip_horizontal else (
                        "Ojo Izquierdo", (255, 0, 0))
                    right_text, right_color = ("Ojo Izquierdo", (255, 0, 0)) if not self._flip_horizontal else (
                        "Ojo Derecho", (0, 0, 255))

                    # Detectar y dibujar blobs en cada mitad
                    left_half = self.blob_detector_left.detect(
                        left_half, "left", left_color)
                    right_half = self.blob_detector_rigth.detect(
                        right_half, "right", right_color)

                    result = np.hstack((left_half, right_half))

                    rgb_image = cv2.cvtColor(result, cv2.COLOR_BGR2RGB)
                    h, w, ch = rgb_image.shape
                    bytes_per_line = ch * w
                    convert_to_Qt_format = QImage(
                        rgb_image.data, w, h, bytes_per_line, QImage.Format_RGB888)
                    p = convert_to_Qt_format.scaled(
                        640, 480, Qt.KeepAspectRatio)

                    self.change_pixmap_signal.emit(p)
    

    def update_config_video(self, slides_values):
        #{'contrast': 50, 'blackligth': 0, 'whitebalance': 4600, 'brightness': -28, 'gamma': 300, 'sharpness': 50, 'hue': 0, 'saturation': 50}
        contrast = slides_values['contrast']
        blacklight = slides_values['blackligth']
        whitebalance = slides_values['whitebalance']
        brightness = slides_values['brightness']
        gamma = slides_values['gamma']
        sharpness = slides_values['sharpness']
        hue = slides_values['hue']
        saturation = slides_values['saturation']
        
        self.cap.set(cv2.CAP_PROP_CONTRAST, contrast)
        self.cap.set(cv2.CAP_PROP_BACKLIGHT , blacklight)
        self.cap.set(cv2.CAP_PROP_WB_TEMPERATURE, whitebalance)
        self.cap.set(cv2.CAP_PROP_BRIGHTNESS, brightness)
        self.cap.set(cv2.CAP_PROP_GAMMA, gamma)
        self.cap.set(cv2.CAP_PROP_SHARPNESS, sharpness)
        self.cap.set(cv2.CAP_PROP_HUE, hue)
        self.cap.set(cv2.CAP_PROP_SATURATION, saturation)

        #print(slides_values)
        
    def open_cap(self):
        self.cap = self.open_camera(self.cam_n)
        self.cap.set(cv2.CAP_PROP_FOURCC,
                     cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'))
        size_frame = (int(self.cap.get(cv2.CAP_PROP_FRAME_WIDTH)),
                      int(self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
        FPS = self.cap.get(cv2.CAP_PROP_FPS)
        fourcc = cv2.VideoWriter_fourcc(*'XVID')
        self.out = cv2.VideoWriter('output.avi', fourcc, FPS, size_frame)

    def open_camera(self, index):
        while True:
            cap = cv2.VideoCapture(index)
            if cap.isOpened():
                print("La cámara se abrió correctamente")
                self.record[2] = True
                self.signal_frame_states.emit(self.record)
                self._running = True
                return cap
            else:
                time.sleep(1)

    def close_cap(self, close_out=False):
        self._running = False
        self.cap.release()
        self.record[2] = False
        self.signal_frame_states.emit(self.record)
        self.out.release()

    def stop(self, save, name):
        self._running = False
        self.close_cap(True)
        self.record[0] = False
        if save:
            time_str = str(time.time())
            time_str = time_str.replace('.', '-')
            name = f"{name}_{time_str}"
            os.rename('output.avi', name)

    def state_record(self):
        self.record = True
        

