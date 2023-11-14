import os
import time

import cv2
import numpy as np
from lib.video.Detector import PupilDetector
from PySide6.QtCore import Qt, QThread, Signal
from PySide6.QtGui import QImage
from base import context
import os




class OpenCVProcessingThread(QThread):
    sig_change_pixmap = Signal(QImage)
    sig_frame_states = Signal(dict)
    sig_coords = Signal(dict)

    def __init__(self, parent=None, cam_n=0):
        super().__init__(parent)
        self._running = True
        self._flip_horizontal = False
        self.detector_left = PupilDetector("OD")
        self.detector_rigth = PupilDetector("OI")
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
                    self.left_half = frame[:, :width//2]
                    self.right_half = frame[:, width//2:]
                    # Dibujar rectángulos alrededor de las mitades de la imagen
                    #cv2.rectangle(left_half, (0, 0),
                    #              (width//2, height), (255, 255, 255), 2)
                    #cv2.rectangle(right_half, (0, 0),
                    #              (width//2, height), (255, 255, 255), 2)
                    # Definir textos y colores para cada lado


                    # Detectar y dibujar blobs en cada mitad

                    self.right_half = self.detector_rigth.detect(self.right_half)
                    self.left_half = self.detector_left.detect(self.left_half)

                    self.detector_left.set_strategy("hough")
                    self.detector_rigth.set_strategy("hough")
                    
                    result = np.hstack((self.left_half[0], self.right_half[0]))

                    rgb_image = cv2.cvtColor(result, cv2.COLOR_BGR2RGB)
                    h, w, ch = rgb_image.shape
                    bytes_per_line = ch * w
                    convert_to_Qt_format = QImage(
                        rgb_image.data, w, h, bytes_per_line, QImage.Format_RGB888)
                    p = convert_to_Qt_format.scaled(
                        640, 480, Qt.KeepAspectRatio)

                    self.sig_change_pixmap.emit(p)
                    self.update_graph()
    
    def update_graph(self):
        coord = {"r": self.right_half[1], "l": self.left_half[1]}
        self.sig_coords.emit(coord)


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
    def update_method(self, value):
        if 'hough' in value:
            self.detector_left.houghcircle_detector.set_param(value)
            self.detector_rigth.houghcircle_detector.set_param(value)

        
    def open_cap(self):
        if os.name == 'nt':
            self.cap = cv2.VideoCapture(self.cam_n, cv2.CAP_DSHOW)
        else:
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
                self.sig_frame_states.emit(self.record)
                self._running = True
                return cap
            else:
                time.sleep(1)

    def close_cap(self, close_out=False):
        self._running = False
        self.cap.release()
        self.record[2] = False
        self.sig_frame_states.emit(self.record)
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
        

