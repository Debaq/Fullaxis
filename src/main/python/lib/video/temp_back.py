import cv2
import math
import numpy as np

class BlobDetector:
    def __init__(self):
        
        self._contrast = 1.0

        params = cv2.SimpleBlobDetector_Params()
        
        self.position = 0

        # Cambiar umbrales
        params.minThreshold = 50
        params.maxThreshold = 200

        # Filtrar por área
        params.filterByArea = True
        params.minArea = 150

        # Filtrar por circularidad
        params.filterByCircularity = True
        params.minCircularity = 0.1

        # Filtrar por convexidad
        params.filterByConvexity = True
        params.minConvexity = 0.87

        # Filtrar por inercia
        params.filterByInertia = True
        params.minInertiaRatio = 0.01

        ver = (cv2.__version__).split('.')
        if int(ver[0]) < 3:
            self.detector = cv2.SimpleBlobDetector(params)
        else:
            self.detector = cv2.SimpleBlobDetector_create(params)

    def detect(self, image, name, color=(0,0,0)):
        
        image_p = self._prepare_image(image)
        keypoints = self._keypoints(image_p)

        for keypoint in keypoints:
            if len(keypoints) == 1:
                x = int(keypoint.pt[0])
                y = int(keypoint.pt[1])
                s = keypoint.size
                r = int(math.floor(s/2))
                self.position = (x,y,r)
            else:
                keypoints = ()
        


        draw_result = cv2.drawKeypoints(image, keypoints, np.array([]), color,
                                             cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
        image_hugo = self._hugo(image)
        return image_hugo
        


    def _candy(self, image):
        
    def _hugo(self, image):
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)                            

        blurred = cv2.GaussianBlur(gray_image, (3, 3), 0)
        circles = cv2.HoughCircles(blurred, cv2.HOUGH_GRADIENT, dp=1, minDist=300,
                            param1=100, param2=30, minRadius=0, maxRadius=30)

        # Convertir la imagen a BGR para dibujar círculos en color
        colored_image = cv2.cvtColor(gray_image, cv2.COLOR_GRAY2BGR)

        if circles is not None:
            circles = np.uint16(np.around(circles))
            for i in circles[0, :]:
                center = (i[0], i[1])
                # Dibujar el centro del círculo
                cv2.circle(colored_image, center, 1, (0, 100, 100), 3)
                # Dibujar el círculo
                radius = i[2]
                cv2.circle(colored_image, center, radius, (255, 0, 255), 3)
        
        return colored_image
    
    def _prepare_image(self, image):
        image = self.adjust_contrast(image, self._contrast)

        _, img = cv2.threshold(image, 50, 255, cv2.THRESH_BINARY)
        img = cv2.erode(img, None, iterations=3)
        img = cv2.dilate(img, None, iterations=5)
        img = cv2.medianBlur(img, 5)
        
        #image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        #image_bgr = cv2.cvtColor(image_gray, cv2.COLOR_GRAY2BGR)
        #image_cnt = self.adjust_contrast(image_bgr, self._contrast)
        #image_blur =  cv2.bilateralFilter(image_cnt,9,75,75)
        image_edges = cv2.Canny(img,10,50)


        #ret2, image_bin= cv2.threshold(image_blur, 50, 400, cv2.THRESH_BINARY)
        return image_edges
        
    def adjust_contrast(self, img, contrast):
        return cv2.addWeighted(img, contrast, img, 0, 0)
        
    
    def _keypoints(self, image):
        keypoints = self.detector.detect(image)
        return keypoints
    
    def set_contrast(self, value):
        self._contrast = value
        
    def get_position(self):
        return self.position
