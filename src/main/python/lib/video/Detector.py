import cv2
import math
import numpy as np
from lib.video.StraHoughCircles import StraHoughCircles

class PupilDetector:
    def __init__(self, side, strategy = None):
        self.side = side
        self.color = (0, 0, 255) if side == 'OD' else (255, 0, 0)
        self.strategy = strategy
        self.houghcircle_detector = StraHoughCircles(self.color)

    def detect(self, image):
        if self.strategy is None:
            return image
        if self.strategy == 'hough':
            a,b = self.houghcircle_detector.process(image)
            return a, b
            
        
    def set_strategy(self, strategy):
        self.strategy = strategy

    def get_strategy(self):
        return self.strategy
        
    
