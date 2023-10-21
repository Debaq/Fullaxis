
import cv2
import numpy as np
import math

class EyeDetector:
    def __init__(self):
        # Parámetros intrínsecos estimados
        self.image_width = 1920
        self.FOV_rad = math.radians(70)
        self.f_pixels = (self.image_width / 2) / math.tan(self.FOV_rad / 2)
        self.mtx = np.array([[self.f_pixels, 0, self.image_width/2], 
                             [0, self.f_pixels, 1080/2], 
                             [0, 0, 1]])
        self.dist = np.array([0, 0, 0, 0, 0])  # Suposición inicial

        # Cargar el clasificador de ojos
        self.eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye_tree_eyeglasses.xml')

        # Parámetros de detección
        self.MIN_DISTANCE = 100
        self.MAX_DISTANCE = 500
        self.EYE_SIZE_RANGE = (40, 320)
        
        # Inicializar la captura de video desde la cámara web
        self.cap = cv2.VideoCapture(2)
        self.cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'))


    def process_frame(self):
        ret, frame = self.cap.read()
        if not ret:
            return None, None, None

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        blurred_gray = cv2.GaussianBlur(gray, (5, 5), 0)

        eyes = self.eye_cascade.detectMultiScale(blurred_gray, scaleFactor=1.08, minNeighbors=2, minSize=(self.EYE_SIZE_RANGE[0], self.EYE_SIZE_RANGE[0]), maxSize=(self.EYE_SIZE_RANGE[1], self.EYE_SIZE_RANGE[1]))

        valid_eyes = []
        eye_centers = []

        if len(eyes) == 2:
            d = np.linalg.norm(np.array(eyes[0][:2]) - np.array(eyes[1][:2]))
            if self.MIN_DISTANCE <= d <= self.MAX_DISTANCE:
                valid_eyes = eyes

        for (x, y, w, h) in valid_eyes:
            center = (x + w // 2, y + h // 2)
            eye_centers.append(center)

        left_eye_center = None
        right_eye_center = None

        if len(eye_centers) == 2:
            # Determina cuál es el ojo izquierdo y cuál el derecho basado en la posición x
            if eye_centers[0][0] < eye_centers[1][0]:
                right_eye_center, left_eye_center = eye_centers
                # Dibuja las líneas rojas para el ojo derecho
                cv2.line(frame, (0, right_eye_center[1]), (frame.shape[1], right_eye_center[1]), (0, 0, 255), 2)  # Horizontal
                cv2.line(frame, (right_eye_center[0], 0), (right_eye_center[0], frame.shape[0]), (0, 0, 255), 2)  # Vertical
                # Dibuja las líneas azules para el ojo izquierdo
                cv2.line(frame, (0, left_eye_center[1]), (frame.shape[1], left_eye_center[1]), (255, 0, 0), 2)  # Horizontal
                cv2.line(frame, (left_eye_center[0], 0), (left_eye_center[0], frame.shape[0]), (255, 0, 0), 2)  # Vertical
            else:
                left_eye_center, right_eye_center = eye_centers
                # Dibuja las líneas rojas para el ojo derecho
                cv2.line(frame, (0, right_eye_center[1]), (frame.shape[1], right_eye_center[1]), (0, 0, 255), 2)  # Horizontal
                cv2.line(frame, (right_eye_center[0], 0), (right_eye_center[0], frame.shape[0]), (0, 0, 255), 2)  # Vertical
                # Dibuja las líneas azules para el ojo izquierdo
                cv2.line(frame, (0, left_eye_center[1]), (frame.shape[1], left_eye_center[1]), (255, 0, 0), 2)  # Horizontal
                cv2.line(frame, (left_eye_center[0], 0), (left_eye_center[0], frame.shape[0]), (255, 0, 0), 2)  # Vertical

        return frame, left_eye_center, right_eye_center

    def release(self):
        self.cap.release()

# Uso
eye_detector = EyeDetector()
while True:
    frame, left_eye, right_eye = eye_detector.process_frame()
    if frame is None:
        break
    print(f"Left Eye: {left_eye}, Right Eye: {right_eye}")
    cv2.imshow('haarcascade', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cv2.destroyAllWindows()
eye_detector.release()