import cv2
import numpy as np


class StraCanny:
    def __init__(self) -> None:
        self.sigma = 0.33

    def process(self, image):
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)                            
        median_val = np.median(gray_image)
        lower_threshold = int(max(0, (1.0 - self.sigma) * median_val))
        upper_threshold = int(min(255, (1.0 + self.sigma) * median_val))
        blurred_image = cv2.GaussianBlur(image, (5, 5), 0)
        image_edges = cv2.Canny(blurred_image,lower_threshold, upper_threshold)
        contours, _ = cv2.findContours(image_edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        for contour in contours:
        # Ignorar contornos pequeños que no son probables que sean pupilas
            if cv2.contourArea(contour) < 5:
                continue
            # Calcular la circularidad del contorno
            perimeter = cv2.arcLength(contour, True)
            area = cv2.contourArea(contour)
            if perimeter == 0:  # Para evitar la división por cero
                continue
            circularity = 4 * np.pi * (area / (perimeter * perimeter))

            if 0.7 < circularity < 1.2:
                # Calcular el centro del contorno
                M = cv2.moments(contour)
                if M["m00"] != 0:
                    cX = int(M["m10"] / M["m00"])
                    cY = int(M["m01"] / M["m00"])
                else:
                    # Esto significa que el área del momento es demasiado pequeña, como para ser una pupila
                    continue

                # Dibujar un círculo en el centro del contorno en la imagen original
                cv2.circle(image_edges, (cX, cY), 2, (255, 0, 0), -1)
        return image_edges



    def set_param(self, param:dict):



