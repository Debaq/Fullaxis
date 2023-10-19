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

    def detect(self, image, color=(0,0,0)):
                # 1. Carga la imagen
        
        # 2. Reduce la resolución (por ejemplo, reduciendo a la mitad)
        small = cv2.resize(image, (0,0), fx=0.5, fy=0.5)
        
        # 3. Carga el clasificador de ojos
        eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')
        
        # 4. Convierte la imagen reducida a escala de grises
        gray_small = cv2.cvtColor(small, cv2.COLOR_BGR2GRAY)
        
        # 5. Detecta los ojos en la imagen reducida
        eyes = eye_cascade.detectMultiScale(gray_small)

        # 6. Si necesitas las coordenadas de los ojos en la imagen original, escala las coordenadas
        eyes_original = [(int(x*2), int(y*2), int(w*2), int(h*2)) for (x,y,w,h) in eyes]


            
        for (x, y, w, h) in eyes_original:
            if x >= 0 and y >= 0 and x + w <= gray_small.shape[1] and y + h <= gray_small.shape[0]:
            # 1. Acota el área del ojo
                roi_gray = gray_small[y:y+h, x:x+w]
                
                # 2. Binarización utilizando umbral adaptativo
                thresh = cv2.adaptiveThreshold(roi_gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 2)

                # 3. Detección de contornos
                contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
                if contours:
                    # 4. Elige el contorno más grande (suponiendo que es la pupila)
                    c = max(contours, key=cv2.contourArea)
                    # Encuentra el círculo del contorno
                    (cx, cy), radius = cv2.minEnclosingCircle(c)
                    center = (int(cx), int(cy))
                    radius = int(radius)
                    # Dibuja el círculo en la imagen original
                    cv2.circle(image, (x + center[0], y + center[1]), radius, (0, 255, 0), 2)
            else:
                continue
            
        return image
            

    
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
