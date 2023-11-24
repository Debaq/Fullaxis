import cv2
import numpy as np


class StraHoughCircles:
    def __init__(self, color = None) -> None:
        self.param_blurred = {'ksizeW' : 3, 'ksizeH': 3, 'sigmaX': 0}
        self.param_hough = {'dp':1, 'minDist':20, 'param1':50, 'param2':30, 'minRadius':0,'maxRadius':0}
        self.last_center = None
        self.max_movement = 10  # por ejemplo, 10 píxeles de movimiento máximo permitido

        if color is None:
            self.color = (255, 0, 255)
        else:
            self.color = color

    def process(self, image):
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)                            

        blurred = cv2.GaussianBlur(gray_image, (self.param_blurred['ksizeW'], self.param_blurred['ksizeH']),
                                   self.param_blurred['sigmaX'])
        circles = cv2.HoughCircles(blurred, cv2.HOUGH_GRADIENT, dp=self.param_hough['dp'],
                                   minDist=self.param_hough['minDist'], param1=self.param_hough['param1'],
                                   param2=self.param_hough['param2'], minRadius=self.param_hough['minRadius'],
                                   maxRadius=self.param_hough['maxRadius'])
        colored_image = cv2.cvtColor(gray_image, cv2.COLOR_GRAY2BGR)
        if circles is not None:
            circles = np.uint16(np.around(circles))
            # Tomamos solo el primer círculo detectado
            center = (circles[0][0][0], circles[0][0][1])
            radius = circles[0][0][2]
            cv2.circle(colored_image, center, 1, (0, 100, 100), 3)
            cv2.circle(colored_image, center, radius, self.color, 3)
        else:
            center = None

        return colored_image, center
    
    def set_param(self, param:dict):
        self.param_blurred = param['hough']['blurred']
        self.param_hough = param['hough']['hough']





