import cv2
import numpy as np

def detect_pupil(image, scale, blur_size, block_size, c_subtract, lower_canny, upper_canny, min_contour_size):
    # Reescalado de la imagen
    h, w = image.shape[:2]
    scaled_image = cv2.resize(image, (int(w * scale), int(h * scale)))
    
    gray = cv2.cvtColor(scaled_image, cv2.COLOR_BGR2GRAY)
    
    # Aplicar filtro Gaussiano
    if blur_size % 2 == 0:
        blur_size += 1  # El tamaño del kernel debe ser impar
    blurred_gray = cv2.GaussianBlur(gray, (blur_size, blur_size), 0)
    cv2.imshow('Gaussian Blur', blurred_gray)
    
    
    # Asegúrate de que block_size sea impar
    if block_size % 2 == 0:
        block_size += 1

    thresholded = cv2.adaptiveThreshold(blurred_gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, 
                                        cv2.THRESH_BINARY_INV, block_size, c_subtract / 10.0) # convertimos c_subtract a float
    cv2.imshow('Gaussian + Thresholding', thresholded)
    
    # Erosión para focalizar en estructuras redondas
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3,3))
    eroded = cv2.erode(thresholded, kernel, iterations=1)
    cv2.imshow('Erode', eroded)
    
    # Aplicar filtro de promediación
    filtered = cv2.blur(eroded, (5,5))
    cv2.imshow('Filtered by Averaging', filtered)
    
    edges = cv2.Canny(filtered, lower_canny, upper_canny)
    cv2.imshow('Gaussian + Thresholding + Edges', edges)
    
    
    contours, _ = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    potential_pupils = []

    if len(contours) > 0:
        for i, contour1 in enumerate(contours):
            for j, contour2 in enumerate(contours):
                if i != j:
                    center = contour1[0][0] # Aquí ajustamos el acceso a la coordenada

                    # Si el contorno1 está dentro del contorno2
                    try:
                        if cv2.pointPolygonTest(contour2, (center[0], center[1]), False) == 1:
                            area1 = cv2.contourArea(contour1)
                            area2 = cv2.contourArea(contour2)
                            
                            # Verifica si el área del contorno1 es razonablemente más pequeña que el contorno2
                            # pero no demasiado pequeña
                            if area1 < area2 * 0.2 and area1 > 100:
                                potential_pupils.append(contour1)
                    except:
                        pass
    # Dibuja los contornos de las posibles pupilas en la imagen
    cv2.drawContours(image, potential_pupils, -1, (0, 255, 0), 2)

    cv2.imshow('Potential Pupils', image)

    return image


roi_center = None
roi_size = 100  # Tamaño del cuadrado, puedes ajustar según lo que necesites

def select_roi(event, x, y, flags, param):
    global roi_center
    if event == cv2.EVENT_LBUTTONDOWN:
        roi_center = (x, y)

cv2.namedWindow('Pupil Detection')
cv2.setMouseCallback('Pupil Detection', select_roi)




def on_change(x):
    pass

# Capturar video desde la webcam
cap = cv2.VideoCapture(0)

# Crear una ventana para los sliders
cv2.namedWindow('Settings', cv2.WINDOW_NORMAL)

# Crear sliders
cv2.createTrackbar('Scale (x0.01)', 'Settings', 100, 150, on_change)  # Valores entre 1.00 y 1.50
cv2.createTrackbar('Blur Size (odd)', 'Settings', 3, 15, on_change)  # Valores entre 3 y 15
cv2.createTrackbar('Block Size (odd)', 'Settings', 11, 31, on_change)  # Valores entre 11 y 31
cv2.createTrackbar('C Subtract (x0.1)', 'Settings', 20, 50, on_change)  # Valores entre 2.0 y 5.0 
cv2.createTrackbar('Lower Canny', 'Settings', 30, 150, on_change) 
cv2.createTrackbar('Upper Canny', 'Settings', 100, 300, on_change) 
cv2.createTrackbar('Min Contour Size', 'Settings', 0, 100, on_change)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    output = frame.copy()
        # Leer valores de los sliders
    blur_size = cv2.getTrackbarPos('Blur Size (odd)', 'Settings')
    lower_canny = cv2.getTrackbarPos('Lower Canny', 'Settings')
    upper_canny = cv2.getTrackbarPos('Upper Canny', 'Settings')
    min_contour_size = cv2.getTrackbarPos('Min Contour Size', 'Settings')
    scale = cv2.getTrackbarPos('Scale (x0.01)', 'Settings') * 0.01
    block_size = cv2.getTrackbarPos('Block Size (odd)', 'Settings')
    c_subtract = cv2.getTrackbarPos('C Subtract (x0.1)', 'Settings')  # Convertimos el valor a float


    if roi_center:
        x1 = max(0, roi_center[0] - roi_size // 2)
        y1 = max(0, roi_center[1] - roi_size // 2)
        x2 = min(frame.shape[1], roi_center[0] + roi_size // 2)
        y2 = min(frame.shape[0], roi_center[1] + roi_size // 2)
        
        roi = frame[y1:y2, x1:x2]
        result_roi = detect_pupil(roi, scale, blur_size, block_size, c_subtract, lower_canny, upper_canny, min_contour_size)
        
        # Superponer los resultados del ROI en la imagen original
        output[y1:y2, x1:x2] = result_roi
    else:
        output = detect_pupil(frame, scale, blur_size, block_size, c_subtract, lower_canny, upper_canny, min_contour_size)

    if not roi_center:
        cv2.destroyWindow('Gaussian Blur')
        cv2.destroyWindow('Gaussian + Thresholding')
        cv2.destroyWindow('Erode')
        cv2.destroyWindow('Gaussian + Thresholding + Edges')
        cv2.destroyWindow('Filtered by Averaging')
        cv2.destroyWindow('Potential Pupils')


    cv2.imshow('Pupil Detection', output)
    if cv2.waitKey(1) == 27:  # salir con 'esc'
        break

cap.release()
cv2.destroyAllWindows()
